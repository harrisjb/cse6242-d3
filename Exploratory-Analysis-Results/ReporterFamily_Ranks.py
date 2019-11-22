import csv

BASE_DIR = './data'

RANK_BY_UNIT = "Wpost-ReporterFamily-RanksBy-DosageUnit.csv"
RANK_BY_WEIGHT = "Wpost-ReporterFamily-RanksBy-OpioidWeight.csv"

def write_data(reporter_family_data, total_units, total_weight):
    pretty_rows = []
    for key in reporter_family_data.keys():
        data = reporter_family_data[key]
        total_dosage = data[0]
        total_gms = data[1]
        percent_dosage = '{}%'.format(round(total_dosage / total_units * 100, 2))
        percent_gms = '{}%'.format(round(total_gms / total_weight * 100, 2))
        pretty_rows.append((key, format_nbr(total_dosage), percent_dosage,format_nbr(total_gms),percent_gms))

    with open('./data/reporter_family_ranks_o.tsv', mode='w') as csv_file:
        pills_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Header for CSV
        pills_writer.writerow(['distributor', 'total_dosage', 'percent_dosage','total_gms', 'percent_gms'])

        for pretty_row in pretty_rows:
            pills_writer.writerow(pretty_row)

def format_nbr(dosage_in):
    if int(dosage_in) > 10 ** 9:  # Billion
        dosage_out = '{0:,.1f} billion'.format(float(dosage_in) / 10 ** 9)
    elif int(dosage_in) > 10 ** 6:  # Millions
        dosage_out = '{0:,.1f} million'.format(float(dosage_in) / 10 ** 6)
    else:
        dosage_out = '{0:,.1f}'.format(float(dosage_in))
    return dosage_out


def fetch_data():
    total_units = 0
    total_weight = 0
    reporter_family_data = {}
    rank_by_unit_file = "{}/{}".format(BASE_DIR,RANK_BY_UNIT)
    with open(rank_by_unit_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            reporter_family = row[0]
            total_dosage = float(row[1])
            total_units += total_dosage
            reporter_family_data[reporter_family] = total_dosage

    rank_by_weight_file = "{}/{}".format(BASE_DIR, RANK_BY_WEIGHT)
    with open(rank_by_weight_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            reporter_family = row[0]
            total_gms = float(row[1])
            total_weight += total_gms
            if reporter_family in reporter_family_data:
                total_dosage = reporter_family_data[reporter_family]
                reporter_family_data[reporter_family] = [total_dosage,total_gms]
            else:
                reporter_family_data[reporter_family] = [0,total_gms]

    return reporter_family_data, total_units, total_weight



if __name__=="__main__":
    reporter_family_data, total_units, total_weight = fetch_data()
    write_data(reporter_family_data, total_units, total_weight)
