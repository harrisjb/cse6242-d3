import sqlite3
import csv
import random

SQLITE_FILE = '/mnt/data1/Data/opioid_data/pills.db'


# Create a Dictionary of counties keyed by State CODE County Name
# We use the Code to Find the County ID Which maps to the topojson Map
def load_counties_topojson():
    counties = {}
    with open('../topojson/counties-10m.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # Remove al Dashes in County Names and make them upper case
            county_nm = row[4].replace("-"," ").upper()
            # Remove quote marks in county names
            county_nm = county_nm.replace("'","")
            # Change Abbrieveation to SAINT
            if (county_nm.find('ST. ') != -1):
                county_nm = county_nm.replace('ST. ','SAINT ')

            key = "{}-{}".format(row[1],county_nm)
            counties[key] = row[2]
    return counties



def get_total_pills_sold_for_each_county_by_year():
    connection = sqlite3.connect(SQLITE_FILE)
    cursor = connection.cursor()
    data_by_county = {}
    trans_years = [2006, 2007, 2008, 2009, 2010, 2011, 2012]
    for trans_year in trans_years:
        cursor.execute('SELECT BUYER_STATE, BUYER_COUNTY, sum(QUANTITY) FROM pills WHERE trans_year={ty} GROUP BY BUYER_STATE, BUYER_COUNTY'
              .format(ty=trans_year))
        print("processing year {}".format(trans_year))
        buyer_state = 0
        buyer_county = 1
        total_pills = 2
        for row in cursor:
            key = "{}-{}".format(row[buyer_state],row[buyer_county])
            if key not in data_by_county:
                data_by_county[key] = {trans_year: row[total_pills]}
            else:
                data_by_county[key].update({trans_year: row[total_pills]})

    return data_by_county

# Write the data in a format acceptable by the d3js script
def write_total_pills_sold_for_each_county_by_year(data_by_county, counties):
    with open('pills_by_county.csv', mode='w') as csv_file:
        pills_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Header for CSV
        pills_writer.writerow(['county_id', 2006, 2007, 2008, 2009, 2010, 2011, 2012])

        for row_dict_key in data_by_county.keys():
            should_write, county_id = get_county_id(counties, row_dict_key)
            if should_write:
                pills_writer.writerow([county_id,
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2006),
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2007),
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2008),
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2009),
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2010),
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2011),
                                       get_pills_for_county_year(data_by_county, row_dict_key, 2012)])


# Get the State Name form the State Code
def get_county_id(counties, row_dict_key):
    # Exlude these State Codes that are not on the Map
    exclude = ['AE', 'GU', 'MP', 'PR', 'PW', 'VI']
    ret_val = (False, None)

    # VA Counties have CITY tacked to the end of there County Name
    # So we just drop that so it will map with topojson
    county_nm = row_dict_key.replace(" CITY", "")

    if row_dict_key[0:2] in exclude:
        print("Excluding {}".format(row_dict_key))
        return ret_val
    #if the county field is null we drop it
    elif (row_dict_key.find('-NULL') != -1):
        print("Excluding {}".format(row_dict_key))
        return ret_val
    else:
        try:
            #print("[{}]".format(row_dict_key))
            county_id = counties[row_dict_key]
            #print(county_id)
            ret_val = (True, county_id)
        except:
            print("Exception {}".format(row_dict_key))

    return ret_val


def get_pills_for_county_year(data_by_county, row_dict_key, year):
    ret_val = 0
    try:
        ret_val = data_by_county[row_dict_key][year]
    except:
        print("Exception {} {}".format(row_dict_key, year))

    return ret_val


# Used to test the process before running against the full DB
def stub_total_pills_sold_for_each_county_by_year():
    data_by_county = {}
    data_2006 = [('MA','BARNSTABLE',500),('GA','SPALDING',200),('VI','ex',10)]
    data_2007 = [('MA','BARNSTABLE',600),('GA','SPALDING',300),('VI','ex',20)]
    trans_years = [2006, 2007]
    for trans_year in trans_years:
        print("processing year {}".format(trans_year))
        buyer_state=0
        buyer_county=1
        total_pills=2
        if trans_year == 2007:
            cursor = data_2007
        else:
            cursor = data_2006

        for row in cursor:
            key = "{}-{}".format(row[buyer_state],row[buyer_county])
            if key not in data_by_county:
                data_by_county[key] = {trans_year: row[total_pills]}
            else:
                data_by_county[key].update({trans_year: row[total_pills]})

    return data_by_county

if __name__ == '__main__':
    counties_topojson = load_counties_topojson()
    pills_sold = get_total_pills_sold_for_each_county_by_year()
    #pills_sold = stub_total_pills_sold_for_each_county_by_year()
    write_total_pills_sold_for_each_county_by_year(pills_sold, counties_topojson)

