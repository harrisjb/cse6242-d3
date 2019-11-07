import pandas as pd

CDC_DATA = '../cdc_prep/data_for_analysis/Mortality_{}.csv'
ARCOS_DATA='./data/pills_sold_by_county_{}.csv'
COMBINED_DATA='./data/pills_sold_by_county_and_years.csv'
COUNTY_MASTER='../topojson/data/counties-10m.csv'

def load_master():
    # State_cd_num,State_cd_alpha,County_cd,State_nm,County_nm
    county_master = pd.read_csv(COUNTY_MASTER, sep=',', converters={'County_cd': lambda x: str(x)})
    county_master = county_master.drop(["State_cd_num","State_cd_alpha"], axis=1)

    return county_master

def convert_population(x):
    ret_val=-1
    try:
        ret_val = int(x)
    except:
        pass
    return ret_val

def fetch_data(year):
    # Load the data to be processed
    # County_code,Deaths,Population,State,County_nm
    cdc_dataframe = pd.read_csv(CDC_DATA.format(year), sep=',',converters={'County_cd': lambda x: str(x),
                                                                           'Population': lambda x: convert_population(x)})
    cdc_dataframe = cdc_dataframe.drop(["Deaths","State","County_nm"], axis=1)

    # County_code,State,County_nm,pills
    arcros_dataframe = pd.read_csv(ARCOS_DATA.format(year), sep=',',converters={'County_cd': lambda x: str(x)})
    arcros_dataframe = arcros_dataframe.drop(["State", "County_nm"], axis=1)
    return cdc_dataframe, arcros_dataframe

def map_data(county_master, cdc_dataframe, arcros_dataframe, year):
    county_master = pd.merge(county_master, cdc_dataframe, on='County_cd', how='left')
    county_master['Population'] = county_master['Population'].fillna(-1)
    county_master = pd.merge(county_master, arcros_dataframe, on='County_cd', how='left')
    county_master['pills'] = county_master['pills'].fillna(0)
    county_master[year] = round(county_master['pills'] / county_master['Population'],0)
    county_master = county_master.drop(["Population", "pills"], axis=1)
    return county_master

if __name__=='__main__':
    county_master = load_master()
    for year in range(2006,2013):
        cdc_dataframe, arcros_dataframe = fetch_data(year)
        county_master = map_data(county_master, cdc_dataframe, arcros_dataframe, year)

    county_master.to_csv(COMBINED_DATA, index=None, header=True)


