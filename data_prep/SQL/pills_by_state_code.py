import sqlite3
import csv
import random

SQLITE_FILE = '/mnt/data1/Data/opioid_data/pills.db'


# Create a Dictionary of states keyed by State CODE
# We use the Code to Find the Name Which maps to the topojson Map
def load_states():
    states = {}
    with open('./topojson/states-10m.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            states[row[1]] = row[2]
    return states


def get_total_pills_sold_for_each_state_by_year():
    connection = sqlite3.connect(SQLITE_FILE)
    cursor = connection.cursor()
    data_by_state = {}
    trans_years = [2006, 2007, 2008, 2009, 2010, 2011, 2012]
    for trans_year in trans_years:
        cursor.execute('SELECT BUYER_STATE, sum(QUANTITY) FROM pills WHERE trans_year={ty} GROUP BY BUYER_STATE'
              .format(ty=trans_year))
        print("processing year {}".format(trans_year))
        buyer_state=0
        total_pills=1
        for row in cursor:
            if trans_year == 2006:
                data_by_state[row[buyer_state]] = {trans_year: row[total_pills]}
            else:
                data_by_state[row[buyer_state]].update({trans_year: row[total_pills]})

    return data_by_state

# Write the data in a format acceptable by the d3js script
def write_total_pills_sold_for_each_state_by_year(data_by_state, states):
    with open('pills_by_state.csv', mode='w') as csv_file:
        pills_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Header for CSV
        pills_writer.writerow(['state', 2006, 2007, 2008, 2009, 2010, 2011, 2012])

        for row_dict_key in data_by_state.keys():
            should_write, name = get_state_name(states, row_dict_key)
            if should_write:
                pills_writer.writerow([name,
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2006),
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2007),
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2008),
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2009),
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2010),
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2011),
                                       get_pills_for_state_year(data_by_state, row_dict_key, 2012)])


# Get the State Name form the State Code
def get_state_name(states, row_dict_key):
    #Exlude these State Codes that are not on the Map
    exclude = ['AE', 'GU', 'MP', 'PR', 'PW', 'VI']
    ret_val = (False, None)
    print(states)
    if row_dict_key in exclude:
        return ret_val
    else:
        try:
            print("[{}]".format(row_dict_key))
            name = states[row_dict_key]
            print(name)
            ret_val = (True, name)
        except:
            print("Exception {}".format(row_dict_key))

    return ret_val


def get_pills_for_state_year(data_by_state, row_dict_key, year):
    ret_val = 0
    try:
        ret_val = data_by_state[row_dict_key][year]
    except:
        print("No Data for {} in {}".format(row_dict_key, year))

    return ret_val


# Used to test the process before running against the full DB
def stub_total_pills_sold_for_each_state_by_year():
    data_by_state = {}
    data_2006 = [('MA',500),('GA',200),('VI',10)]
    data_2007 = [('MA',600),('GA',300),('VI',20)]
    trans_years = [2006, 2007]
    for trans_year in trans_years:
        print("processing year {}".format(trans_year))
        buyer_state=0
        total_pills=1
        if trans_year == 2007:
            cursor = data_2007
        else:
            cursor = data_2006

        for row in cursor:
            if trans_year == 2006:
                data_by_state[row[buyer_state]] = {trans_year: row[total_pills]}
            else:
                data_by_state[row[buyer_state]].update({trans_year: row[total_pills]})

    return data_by_state

if __name__ == '__main__':
    states = load_states()
    pills_sold = get_total_pills_sold_for_each_state_by_year()
    #pills_sold = stub_total_pills_sold_for_each_state_by_year()
    write_total_pills_sold_for_each_state_by_year(pills_sold, states)

