import sqlite3
import csv
import random
import pandas as pd

SQLITE_FILE = '/mnt/data1/Data/opioid_data/pills.db'
BASE_DIR = './data'

QUERY = '''
select Revised_Company_Name, sum(DOSAGE_UNIT) as total_pills
   from dea_arcos_wpost
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
        REPORTER_BUS_ACT == 'DISTRIBUTOR'
    group by Revised_Company_Name
    order by total_pills desc
    limit 100;
'''


def get_total_pills_sold_by_manufacturer():
    total_pills = 0
    rows = []
    connection = sqlite3.connect(SQLITE_FILE)
    cursor = connection.cursor()
    cursor.execute(QUERY)
    for row in cursor:
        total_pills += int(row[1])
        rows.append(row)
    write_data(rows,total_pills)

def write_data(rows,total_pills):
    pretty_rows = []
    for row in rows:
        if int(row[1]) > 10**9: # Billion
            pills = '{0:,.1f} billion'.format(float(row[1])/10**9)
        elif int(row[1]) > 10**6: # Millions
            pills = '{0:,.1f} million'.format(float(row[1])/10**6)
        else:
            pills = '{0:,.1f}'.format(float(row[1]))

        percent = '{}%'.format(round(float(row[1]) / total_pills * 100, 2))
        pretty_rows.append((row[0], pills, percent))

    with open('./data/pill_totals_by_manufacturer_o.tsv', mode='w') as csv_file:
        pills_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Header for CSV
        pills_writer.writerow(['manufacturer', 'total_count', 'percentage'])

        for pretty_row in pretty_rows:
            pills_writer.writerow(pretty_row)


def fetch_data():
    total_pills = 0
    rows = []

    file_name="{}/top_pill_manufacturers_2006_2012.csv".format(BASE_DIR)
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            pills = int(float(row[1]))
            total_pills += pills
            rows.append((row[0],pills))
        write_data(rows, total_pills)


if __name__=="__main__":
    fetch_data()
    #get_total_pills_sold_by_manufacturer()