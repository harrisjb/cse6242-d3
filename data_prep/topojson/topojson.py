import json
import csv
'''
Processing the topojson map data requires that you be able to map state NAMES (not two character codes) to the 
topojson geometries property name. Likewise with County Names either the names must match geometries properties names 
or the 5 digit county id.

Here we parse the jason and create csv file that can be used to preprocess our data to work with these maps
'''

# Loads the State Names and Codes into a Dictionary keyed by State Name
def load_state_codes():
    state_codes = {}
    with open('./data/state_codes_by_name.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            state_codes[row[0]] = row[1]

    return state_codes


# Loads Counties json and parses the State Names
# Uses State_Codes Dictionary to Find Code for Name
# Writes ID, CODE, and NAME to csv file
def create_states_csv():
    state_codes = load_state_codes()
    states_data = []
    with open('./data/counties-10m.json') as json_file:
        data = json.load(json_file)
        for state in data['objects']['states']['geometries']:
            states_data.append([state['id'], state['properties']['name']])

    with open('./data/states-10m.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        states_data.sort()
        for state in states_data:
            id = state[0]
            state_name = state[1]
            state_code = state_codes[state_name]
            csv_writer.writerow([id, state_code, state_name])


# Load the States ID, CODE and Name into a Dictionary
def load_state_codes_and_ids():
    state_codes = {}
    with open('./data/states-10m.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            state_codes[row[0]] = {'code': row[1], 'name': row[2]}

    return state_codes


# Load the County Data
def create_counties_csv():
    counties_data = []
    state_codes_and_ids = load_state_codes_and_ids()
    with open('./data/counties-10m.json') as json_file:
        data = json.load(json_file)
        for county in data['objects']['counties']['geometries']:
            counties_data.append([county['id'], county['properties']['name']])

    with open('./data/counties-10m.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        counties_data.sort()
        for county in counties_data:
            county_id = county[0]
            state_id = county_id[0:2]
            county_name = county[1]
            state_code = state_codes_and_ids[state_id]['code']
            state_name = state_codes_and_ids[state_id]['name']
            csv_writer.writerow([state_id, state_code, county_id, state_name, county_name])


if __name__ == '__main__':
    create_states_csv()
    create_counties_csv()
