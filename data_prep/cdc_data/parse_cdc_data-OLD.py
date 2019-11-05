import os
import csv

CDC_DATA_DIR='/mnt/data1/Data/opioid_data/CDC_Overdose_Mortality_By_County'
FILE_NM='{}CDCOverdoseMortalityByCounty.txt'

def main():
    print('running...')
    years = [2006,2007,2008,2009,2010,2011,2012]
    counties = {}
    for year in years:
        file_nm=FILE_NM.format(year)
        full_path= '{}/{}'.format(CDC_DATA_DIR,file_nm)
        if os.path.exists(full_path):
            counties =aggrigate_county_data_by_year(full_path,counties)

    write_county_data_by_year(counties)


def aggrigate_county_data_by_year(file_nm,counties):
    count=0
    total_deaths=0

    with open(file_nm) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            # If this is a row we should process
            if row[0] == '':
                count +=1
                #print("{} {}".format(count,row))
                #get required data
                year = row[1]
                county = row[5]
                zip = row[6]
                deaths= int(row[7])
                total_deaths += deaths
                key = '{}{}'.format(zip,county)
                if key in counties.keys():
                    years = counties[key]
                    if year in years.keys():
                        years[year] += deaths
                    else:
                        years[year] = deaths
                else:
                    counties[key]={year:deaths}
    #print("count {} deaths {}".format(count, total_deaths))
    return counties

def write_county_data_by_year(counties):
    with open('deaths_by_county.csv', mode='w') as csv_file:
        county_data_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Header for CSV
        county_data_writer.writerow(['county_id','state','county', '2006', '2007', '2008', '2009', '2010', '2011', '2012'])
        for row_dict_key in counties.keys():
            years = counties[row_dict_key]
            zip,state,county = parse_key(row_dict_key)
            #print("{} {} {}".format(state, county,years))
            county_data_writer.writerow([zip,state,county,
                                   get_deaths(years, 2006),
                                   get_deaths(years, 2007),
                                   get_deaths(years, 2008),
                                   get_deaths(years, 2009),
                                   get_deaths(years, 2010),
                                   get_deaths(years, 2011),
                                   get_deaths(years, 2012)])

def write_county_data_cumulative(counties):
    with open('deaths_by_county.csv', mode='w') as csv_file:
        county_data_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Header for CSV
        county_data_writer.writerow(['county_id','state','county', 'deaths'])
        for row_dict_key in counties.keys():
            years = counties[row_dict_key]
            zip,state,county = parse_key(row_dict_key)
            #print("{} {} {}".format(state, county,years))
            total_deaths=0
            for year in [2006,2007,2008,2009,20010,2011,2012]:
                total_deaths += get_deaths(years, year)

            county_data_writer.writerow([zip,state,county,total_deaths])

def get_deaths(years,year):
    #print("***{} {} ***".format(year,years.keys()))
    key = str(year)
    if key in years.keys():
        return years[key]
    else:
        return 0

def parse_key(key):
    zip = key[0:5]
    county =key[5:-11]
    state = key[-2:]
    return zip,state,county

if __name__== '__main__':
    main()