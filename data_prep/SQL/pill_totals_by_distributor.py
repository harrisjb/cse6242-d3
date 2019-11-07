import sqlite3
import csv
import random

SQLITE_FILE = '/mnt/data1/Data/opioid_data/pills.db'

QUERY = '''
select Reporter_family, sum(DOSAGE_UNIT) as total_pills
   from pills
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
    group by Reporter_family
    order by total_pills desc
    limit 100;
'''


def get_total_pills_sold_by_distributor():
    total_pills = 0
    pretty_rows = []
    rows = []
    connection = sqlite3.connect(SQLITE_FILE)
    cursor = connection.cursor()
    cursor.execute(QUERY)
    for row in cursor:
        total_pills += int(row[1])
        rows.append(row)

    for row in rows:
        if int(row[1]) > 10**9: # Billion
            pills = '{0:,.1f} billion'.format(float(row[1])/10**9)
        elif int(row[1]) > 10**6: # Millions
            pills = '{0:,.1f} million'.format(float(row[1])/10**6)
        else:
            pills = '{0:,.1f}'.format(float(row[1]))

        percent = '{}%'.format(round(float(row[1]) / total_pills * 100, 1))
        pretty_rows.append((row[0], pills, percent))

    with open('./data/pill_totals_by_distributor_o.tsv', mode='w') as csv_file:
        pills_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Header for CSV
        pills_writer.writerow(['distributor', 'total_count', 'percentage'])

        for pretty_row in pretty_rows:
            pills_writer.writerow(pretty_row)

if __name__=="__main__":
    get_total_pills_sold_by_distributor()