import pandas as pd

BASE_DIR = './data'

# "Notes"	"County"	"County Code"	Deaths	Population	Crude Rate
def fetch_data():
    # Load the data to be processed
    file_name="{}/GTWR_Model_Output.csv".format(BASE_DIR)
    data_set = pd.read_csv(file_name, sep=',',converters={'fips': lambda x: str(x)})
    print(data_set.columns)
    print("data_set (rows, columns) {}\n".format(data_set.shape))
    print("data_set missing values \n{}\n".format(data_set.isnull().sum()))
    return data_set

def convert_population(x):
    ret_val=-1
    try:
        ret_val = int(x)
    except:
        pass
    return ret_val

def clean_data(data_set,year):
    data_set = data_set[data_set['year'] == year]
    drop_fields = ["optional", "longitude", "latitude","county","state.y"]
    data_set = data_set.drop(drop_fields, axis=1)

    print(data_set.head())
    return data_set



if __name__=='__main__':
    year=2006
    data_set = fetch_data()
    data_set = clean_data(data_set,year)
    file_name = "{}/GTWR_Model_Output_{}.csv".format(BASE_DIR,year)
    data_set.to_csv(file_name, index=None, header=True)


