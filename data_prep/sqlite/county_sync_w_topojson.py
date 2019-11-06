import sqlite3
import csv
import os
import random

#########################################################
'''
After preprocessing the data we have 15 County Names that
do not Match with the topojason file. 

We are correctly mapping 99.52% 

This could be rectified with a Custom Mapper but this has not been written

State, County 
AL,    DE KALB
FL,    DE SOTO
FL,    MIAMI-DADE
IL,    DEWITT
IL,    LA SALLE
IN,    DE KALB
IN,    LA PORTE
IN,    ST JOSEPH
LA,    LA SALLE
LA,    ST JOHN THE BAPTIST
MO,    SAINTE GENEVIEVE
NM,    DONA ANA
NV,    CARSON
TX,    DE WITT
VA,    JAMES

'''
SQLITE_ARCOS_DB = '/mnt/data1/Data/opioid_data/pills.db'
BUYER_COUNTIES= './data/arcos_buyer_counties.csv'
REPORTER_COUNTIES= './data/arcos_reporter_counties.csv'
BUYER_COUNTY_CODES= './data/arcos_buyer_county_codes.csv'
REPORTER_COUNTY_CODES= './data/arcos_reporter_county_codes.csv'

COUNTIES_10M='../topojson/counties-10m.csv'


# Create a Dictionary of counties keyed by State CODE County Name
# We use the Codes to Find the County ID Which maps to the topojson Map
def load_counties_topojson():
    counties = {}
    with open(COUNTIES_10M) as csv_file:
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


def load_buyer_counties():
    if not os.path.exists(BUYER_COUNTIES):
        get_arcos_counties('SELECT BUYER_STATE, BUYER_COUNTY FROM pills GROUP BY BUYER_STATE, BUYER_COUNTY',
                           BUYER_COUNTIES)
    return load_arcos_counties(BUYER_COUNTIES)

def load_reporter_counties():
    if not os.path.exists(REPORTER_COUNTIES):
        get_arcos_counties('SELECT REPORTER_STATE, REPORTER_COUNTY FROM pills GROUP BY REPORTER_STATE, REPORTER_COUNTY',REPORTER_COUNTIES)
    return load_arcos_counties(REPORTER_COUNTIES)

def load_arcos_counties(file_nm):
    counties = {}

    with open(file_nm) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            state_cd = row[0]
            county_nm = row[1]
            # Remove counties prefix of CITY
            county_nm = county_nm.replace(" CITY","")
            # Codes to Ignore
            # AS,American Samoa
            # GU,Guam
            # MP,Commonwealth of the Northern Mariana Islands
            # PR,Puerto Rico
            # VI,United States Virgin Islands
            # AE Armed forces in Europe
            # PW ????
            if state_cd in ['PW','AE','MP']:
                pass
            elif county_nm == 'null':
                pass
            else:
                key = "{}-{}".format(state_cd, county_nm)
                counties[key]=[row[0],row[1]]

    return counties

def map_to_county_topojson(topojson, arcos_counties, file_nm):
    with open(file_nm, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['State', 'County', 'County_Code'])
        for county_key in arcos_counties.keys():
            arcos_county = arcos_counties[county_key]
            state_cd = arcos_county[0]
            county_name = arcos_county[1]
            if county_key in topojson:
                county_code = topojson[county_key]
                csv_writer.writerow([state_cd, county_name, county_code])
            else:
                print("key not found {}".format(county_key))
        for manual_map in get_manual_map():
            csv_writer.writerow([manual_map[0], manual_map[1], manual_map[2]])

def get_manual_map():
    manual_map=[
        ('AL','DE KALB','01049'),
        ('FL','DE SOTO','12027'),
        ('FL','MIAMI-DADE','12086'),
        ('IL','DEWITT','17039'),
        ('IL','LA SALLE','17099'),
        ('IN','DE KALB','18033'),
        ('IN','LA PORTE','18091'),
        ('IN','ST JOSEPH','18141'),
        ('LA','LA SALLE','22059'),
        ('LA','ST JOHN THE BAPTIST','22095'),
        ('MD','BALTIMORE','24005'),
        ('MO','SAINT LOUIS','29189'),
        ('MO','SAINTE GENEVIEVE','29186'),
        ('NM','DONA ANA','35013'),
        ('NV','CARSON CITY','32510'),
        ('PR','ANASCO','72011'),
        ('PR','BAYAMON','72021'),
        ('PR','CANOVANAS','72029'),
        ('PR','CATANO','72033'),
        ('PR','COMERIO','72045'),
        ('PR','GUANICA','72055'),
        ('PR','JUANA DIAZ','72075'),
        ('PR','LAS MARIAS','72083'),
        ('PR','LOIZA','72087'),
        ('PR','MANATI','72091'),
        ('PR','MAYAGUEZ','72097'),
        ('PR','PENUELAS','72111'),
        ('PR','RINCON','72117'),
        ('PR','RIO GRANDE','72119'),
        ('PR','SAN GERMAN','72125'),
        ('PR','SAN SEBASTIAN','72131'),
        ('TX','DE WITT','48123'),
        ('VA','FAIRFAX','51059'),
        ('VA','FRANKLIN','51067'),
        ('VA','JAMES CITY','51095'),
        ('VA','RICHMOND','51159'),
        ('VA','ROANOKE','51161')
        ]
    return manual_map

#Create a csv file with ALL the States and County Names from the arcos BD by seller or buyer
def get_arcos_counties(sql,file_nm):
    connection = sqlite3.connect(SQLITE_ARCOS_DB)
    counties =[]
    cursor = connection.cursor()
    cursor.execute(sql)
    for row in cursor:
        counties.append([row[0],row[1]])

    with open(file_nm, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for county in counties:
            state_cd = county[0]
            county_name = county[1]
            csv_writer.writerow([state_cd, county_name])
    return counties

if __name__ == '__main__':
    topojson = load_counties_topojson()
    reporter_counties = load_reporter_counties()
    map_to_county_topojson(topojson, reporter_counties, REPORTER_COUNTY_CODES)
    buyer_counties = load_buyer_counties()
    map_to_county_topojson(topojson, buyer_counties,BUYER_COUNTY_CODES)