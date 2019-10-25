# post process the Pills By Distributor Results
# Provide Percentage of Total and Place Commas in the Number results
import csv

PILLS_BY_DIST_I='./pill_totals_by_manufacturers.tsv'
PILLS_BY_DIST_O='./pill_totals_by_manufacturers_o.tsv'
def main():
        total_pills = 0
        pretty_rows=[]
        rows = []
        with open(PILLS_BY_DIST_I) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            for row in csv_reader:
                total_pills += int(row[1])
                rows.append(row)

            for row in rows:
                pills = '{0:,.0f}'.format(float(row[1]))
                percent = '{}%'.format(round(float(row[1])/total_pills*100,1))
                pretty_rows.append((row[0],pills,percent))

        # Dangerous Code as it will overwrite our input file
        with open(PILLS_BY_DIST_O, mode='w') as csv_file:
            pills_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            pills_writer.writerow(['manufacturer', 'total_count','percentage'])

            for pretty_row in pretty_rows:
                pills_writer.writerow(pretty_row)

if __name__=="__main__":
    main()
