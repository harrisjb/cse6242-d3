import os
import csv

CDC_DATA_DIR='./'
FILE_NM='Mortality-{}.txt'

def main():
    print('running...')
    years = [2006]
    counties = {}
    for year in years:
        file_nm=FILE_NM.format(year)
        full_path= '{}/{}'.format(CDC_DATA_DIR,file_nm)

        print(os.getcwd())
        print(full_path)
        if os.path.exists(full_path):
            counties = aggrigate_county_data_by_year(full_path, year, counties)

    write_county_data_by_year(counties)

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def aggrigate_county_data_by_year(file_nm, year,counties):
    with open(file_nm) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            #print(row)
            county     = row[1]
            code       = row[2]
            deaths     = row[3]
            if is_float(row[4]):
                population = float(row[4])
            else:
                print(row[4])
                population = 0
            key = '{}{}'.format(code, county)
            counties[key] = {year: population}

    return counties

def write_county_data_by_year(counties):
    with open('population_by_county.csv', mode='w') as csv_file:
        county_data_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Header for CSV
        county_data_writer.writerow(['county_id','state','county', '2006'])
        for row_dict_key in counties.keys():
            years = counties[row_dict_key]
            code,state,county = parse_key(row_dict_key)
            print("{} {} {} {}".format(code, state, county, years))
            county_data_writer.writerow([code,state,county,
                                   get_population(years, 2006)
                                   ])

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
                total_deaths += get_population(years, year)

            county_data_writer.writerow([zip,state,county,total_deaths])

def get_population(years,year):
    #print("***{} {} ***".format(year,years.keys()))
    key = year
    print("{} {}".format(key, list(years.keys())))
    if key in list(years.keys()):
        return years[key]
    else:
        return 0

def parse_key(key):
    code = key[0:5]
    county =key[5:-11]
    state = key[-2:]
    return code,state,county

if __name__== '__main__':
    main()