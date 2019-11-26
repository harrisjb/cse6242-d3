import csv

# This code adds the FIPS county codes to the Wpost-OpioidWeight-ByStateCounty query output

BASE_DIR = './data'

FIPS_CDS = "arcos_buyer_county_codes.csv"
OPIOID_BY_WEIGHT = "Wpost-OpioidWeight-ByStateCounty.csv"
OPIOID_BY_WEIGHT_FIPS = "Wpost-OpioidWeight-ByFips.csv"


def process_data():
    fips_data = {}
    opioid_by_weight_data = []
    fips_cds = "{}/{}".format(BASE_DIR, FIPS_CDS)
    with open(fips_cds) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            state = row[0]
            county = row[1]
            county_code = row[2]
            key = "{}{}".format(state, county)
            fips_data[key] = county_code

    opioid_by_weight = "{}/{}".format(BASE_DIR, OPIOID_BY_WEIGHT)
    with open(opioid_by_weight) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            # "reporter_county", "reporter_state", "total_gms"
            reporter_county = row[0]
            reporter_state = row[1]
            total_gms = row[2]
            key = "{}{}".format(reporter_state, reporter_county)
            if key in fips_data:
                fips_cd = fips_data[key]
            else:
                print("Key not found {}".format(key))
                fips_cd = "NA"

            row = [fips_cd, reporter_state, reporter_county, total_gms]
            opioid_by_weight_data.append(row)

    opioid_by_weight_fips = "{}/{}".format(BASE_DIR, OPIOID_BY_WEIGHT_FIPS)
    with open(opioid_by_weight_fips, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Header for CSV
        writer.writerow(['fips_cd', 'reporter_state', 'reporter_county', 'total_gms'])

        for row in opioid_by_weight_data:
            writer.writerow(row)


if __name__ == "__main__":
    process_data()
