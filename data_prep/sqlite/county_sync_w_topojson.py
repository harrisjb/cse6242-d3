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
SQLITE_PILLS_DB = '/mnt/data1/Data/opioid_data/pills.db'
COUNTIES_FROM_PILLS_DB='./counties_from_pills_db.csv'
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



def load_counties_pills_db():
    counties = []
    if not os.path.exists(COUNTIES_FROM_PILLS_DB):
        get_buyer_counties()

    with open(COUNTIES_FROM_PILLS_DB) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            state_cd = row[0]
            county_nm = row[1]
            #if 'VA' == state_cd:
            county_nm = county_nm.replace(" CITY","")
            if state_cd in ['PR','PW','AE','MP']:
                pass
            elif county_nm == 'null':
                pass
            else:
                counties.append([state_cd,county_nm])

    return counties

def check_if_county_topojson(topojson,pills_db):
    for county in pills_db:
        key = "{}-{}".format(county[0], county[1])
        if key not in topojson:
            print("key not found {}".format(key))

#Create a csv file with ALL the States and County Names from the pills BD
def get_buyer_counties():
    connection = sqlite3.connect(SQLITE_PILLS_DB)
    counties =[]
    cursor = connection.cursor()
    cursor.execute('SELECT BUYER_STATE, BUYER_COUNTY FROM pills GROUP BY BUYER_STATE, BUYER_COUNTY')
    for row in cursor:
        counties.append([row[0],row[1]])

    with open(COUNTIES_FROM_PILLS_DB, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for county in counties:
            state_cd = county[0]
            county_name = county[1]
            csv_writer.writerow([state_cd, county_name])
    return counties

if __name__ == '__main__':
    topojson = load_counties_topojson()
    pills_db = load_counties_pills_db()
    check_if_county_topojson(topojson, pills_db)