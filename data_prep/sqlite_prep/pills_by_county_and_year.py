import sqlite3
import csv
import random

# This program requires that initialize_county.sql is run and that the view pills_county is
# successfully created.

SQLITE_FILE = '/mnt/data1/Data/opioid_data/pills.db'
OUTPUT_FILE = './data/pills_sold_by_county_{}.csv'
QUERY = '''
select COUNTY_CODE, BUYER_STATE, BUYER_COUNTY, sum(DOSAGE_UNIT) as total_pills
   from pills_county
   where
        BUYER_BUS_ACT in (
            'RETAIL PHARMACY',
            'CHAIN PHARMACY',
            'PRACTITIONER',
            'PRACTITIONER-DW/30',
            'PRACTITIONER-DW/100',
            'PRACTITIONER-DW/275'
        ) and
        TRANSACTION_CODE == 'S' and
        Measure == 'TAB' and
        DRUG_NAME in ('OXYCODONE', 'HYDROCODONE') and
        REPORTER_BUS_ACT == 'DISTRIBUTOR' and
        trans_year={} 
    GROUP BY BUYER_STATE, BUYER_COUNTY;
'''


def get_pills_sold_by_county_and_year():
    for year in range(2006,2013):
        print("Processing year {}".format(year))
        output_file = OUTPUT_FILE.format(year)
        with open(output_file, mode='w') as csv_file:
            pills_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Header for CSV
            pills_writer.writerow(['County_cd', 'State','County_nm','pills'])

            query = QUERY.format(year)
            connection = sqlite3.connect(SQLITE_FILE)
            cursor = connection.cursor()
            cursor.execute(query)
            for row in cursor:
                county_code = '00000' if row[0] is None else row[0]
                state =row[1]
                county_nm=row[2]
                pills=row[3]
                pills_writer.writerow((county_code,state,county_nm,pills))

if __name__=="__main__":
    get_pills_sold_by_county_and_year()