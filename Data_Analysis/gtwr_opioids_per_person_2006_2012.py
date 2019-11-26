import pandas as pd

IN_DATA = './Scaled Independent Variable Analysis/Mortality Outcome GTWR Model SCALED Outputs 2006-2012.csv'

OUT_DATA='./Scaled Independent Variable Analysis/gtwr_opioids_per_person_2006_2012.csv'


def process_data():
    in_data = pd.read_csv(IN_DATA, sep=',', converters={'County_cd': lambda x: str(x)})
    drop_fields = ["name.x", "state.x","county","state.y","deaths_clean","mortality_rate","log_mortality","opioids_in_gm",
                   "opioid_perpersonstd", "hhincome_cleanstd","age_cleanstd","white_clean","percent_whitestd","coef_intercept",
                   "coef_hhincome_clean", "coef_age_clean","coef_pop_clean","longitude","latitude","optional"]
    in_data = in_data.drop(drop_fields, axis=1)
    # fips,name.x,year,coef_opioids_perperson
    #in_data = in_data.pivot_table('coef_opioids_perperson', ['fips', 'name.x'], 'year')
    in_data = in_data.pivot_table(index = ['fips'], columns = 'year', values = 'coef_opioids_perperson')
    in_data.reindex_axis(['2006', '2007', '2008','2009', '2010', '2011','2012'], axis=1)
    in_data = in_data.reset_index()
    in_data.rename(columns={'fips': 'county_id'}, inplace=True)
    print(in_data.columns)
    in_data[2006] *= 100
    in_data[2007] *= 100
    in_data[2008] *= 100
    in_data[2009] *= 100
    in_data[2010] *= 100
    in_data[2011] *= 100
    in_data[2012] *= 100
    return in_data



if __name__=='__main__':
    out_data = process_data()
    out_data.to_csv(OUT_DATA, index=False,header=True)


