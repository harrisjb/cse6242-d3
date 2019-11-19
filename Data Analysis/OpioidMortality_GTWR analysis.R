## CSE6242 Team Project
## TEAM HACKS AND HACKERS

## IMPLEMENTING GEOGRAPHICAL AND TEMPORAL WEIGHTED REGRESSION (GTWR) TO ASSESS THE OPIOID-MORTALITY ASSOCIATION IN THE US FROM 2006-2012

# (1). Required Libraries
library(GWmodel)
library(sp)
library(sgdal)
library(countyweather) ## contains the county centers dataframe, with centroid longitude and latitude for each FIPS county code
library(ggplot2)

# (2). Importing the dataset
opioid_df = read.csv("WPost-cdc-census-yearlymerge-AnalyticsFrame-17Nov2019.csv", header=T)


## data cleaning
# (a) set mortality == -1 (suppressed data) as missing
opioid_df$deaths_clean <- opioid_df$deaths
opioid_df$deaths_clean[opioid_df$deaths_clean == -1] <- NA

# (b) for US census data variables, keep only those estimates that have a margin of error within 15% of the estimate
opioid_df$pop_clean <- ifelse((abs(opioid_df$population_moe) < opioid_df$population*0.15 | opioid_df$population_moe ==-555555555), opioid_df$population, NA)
opioid_df$hhincome_clean <- ifelse((abs(opioid_df$median_hhincome_moe) < opioid_df$median_hhincome*0.15), opioid_df$median_hhincome, NA)
opioid_df$age_clean <- ifelse((abs(opioid_df$median_age_moe) < opioid_df$median_age*0.15), opioid_df$median_age, NA)
opioid_df$white_clean <- ifelse((abs(opioid_df$white_alone_moe) < opioid_df$white_alone*0.15), opioid_df$white_alone, NA)
opioid_df$percent_white <- opioid_df$white_clean/opioid_df$pop_clean * 100
opioid_df$mortality_rate <- opioid_df$deaths_clean/opioid_df$pop_clean * 100000

# log transform mortality rate
opioid_df$log_mortality <- log(opioid_df$mortality_rate)

# (c) visualize the data
sum(is.na(opioid_df$deaths_clean))
summary(opioid_df$deaths_clean)
summary(opioid_df$deaths)
summary(opioid_df$opioids_in_gm)
hist(opioid_df$deaths_clean)
hist(opioid_df$mortality_rate)
hist(opioid_df$opioids_in_gm)
hist(opioid_df$log_mortality)
boxplot(opioid_df$opioids_in_gm)
boxplot(opioid_df$opioids_in_gm~opioid_df$year)
boxplot(opioid_df$deaths_clean~opioid_df$year)
boxplot(opioid_df$mortality_rate~opioid_df$year)
boxplot(opioid_df$log_mortality~opioid_df$year) # increases over time
boxplot(opioid_df$age_clean)
boxplot(opioid_df$hhincome_clean)
boxplot(opioid_df$percent_white)
boxplot(opioid_df$pop_clean)
scatter.smooth(opioid_df$opioids_in_gm, opioid_df$deaths_clean) 
global_association <- lm(log_mortality ~ opioids_in_gm + hhincome_clean + age_clean + pop_clean + percent_white, data = opioid_df)
summary (global_association)

## merge with lat/long data
opioid_df$fips <- opioid_df$geoid
merged_data <- merge(county_centers, opioid_df, by="fips")

# Sanity check, assert proper merging of county by FIP code
#county_check <- within(merged_data, name<-data.frame(do.call('rbind', strsplit(as.character(name), ',', fixed=TRUE))))
#all(county_check$county.y == county_check$name.X1) ## TRUE

#subset the data and convert to spatial points dataframe
varlist <- c("fips", "name.x", "state.x", "county", "state.y", "year", "longitude", "latitude", 
             "deaths_clean", "mortality_rate", "log_mortality", "opioids_in_gm", "pop_clean", 
             "hhincome_clean", "age_clean", "white_clean", "percent_white" )
analysis_data <- subset(merged_data, select = varlist)
analysis_data <- subset(analysis_data, state.y!=15)
analysis_data <- subset(analysis_data, !(is.na(deaths_clean)) & !(is.na(pop_clean)) & !(is.na(hhincome_clean)))
coordinates(analysis_data) <- ~longitude + latitude
aea.proj <- "+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=37.5 +lon_0=-102
              +x_0=180 +y_0=50 +ellps=GRS80 +datum=NAD83 +units=m"
proj4string(analysis_data) <- CRS("+proj=longlat")
analysis_data <- spTransform(analysis_data, CRS(aea.proj))
class(analysis_data)

## GTWR Analysis

#(a) identify bandwidth with fixed kernel (fixed distance, but varying number of nearest neighbours)

fixedbisquare_bw <- bw.gtwr(log_mortality ~ opioids_in_gm + hhincome_clean + age_clean + pop_clean + percent_white, data=analysis_data,
                     obs.tv = analysis_data$year, approach = "AICc", kernel = "bisquare", adaptive = F, lamda = 0.05, t.units = "year", ksi = 0,
                      verbose = TRUE)

fixedgaussian_bw <- bw.gtwr(log_mortality ~ opioids_in_gm + hhincome_clean + age_clean + pop_clean + percent_white, data=analysis_data,
                     obs.tv = analysis_data$year, approach = "AICc", kernel = "gaussian", adaptive = F, lamda = 0.05, t.units = "year", ksi = 0,
                     verbose = TRUE)

## lowest AIC for the bandwidth obtained using fixed gaussian kernel
#Run the GTWR model with the fixed gaussian bandwidth
gtwr_model <- gtwr(log_mortality ~ opioids_in_gm + hhincome_clean + age_clean + pop_clean + percent_white, data=analysis_data, 
                    obs.tv = analysis_data$year, st.bw = fixedgaussian_bw, kernel="gaussian",
                    adaptive=FALSE, p=2, theta=0, longlat=F,lamda=0.05,t.units = "year",ksi=0)

gtwr_model ## summary of model

## add the coefficients to the analysis dataset

results <- as.data.frame(gtwr_model1$SDF)
head(results)
analysis_data$coef_intercept <- results$Intercept
analysis_data$coef_opioids_in_gm <- results$opioids_in_gm
analysis_data$coef_hhincome_clean <- results$hhincome_clean
analysis_data$coef_age_clean <- results$age_clean
analysis_data$coef_pop_clean <- results$pop_clean
analysis_data$coef_pop_clean <- results$percent_white
analysis_data$coef_opioids_per1000_gm <- results$opioids_in_gm*1000 # scaled coefficient to a 1000 gm increase in yearly opiod

write.csv(analysis_data, "Mortality Outcome GTWR Model Outputs 2006-2012.csv", row.names=FALSE) # output complete case data with coefficients for mapping in D3




