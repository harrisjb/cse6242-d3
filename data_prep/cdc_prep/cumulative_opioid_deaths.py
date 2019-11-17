import pandas as pd

BASE_DIR = './data'

# "Notes"	"County"	"County Code"	Deaths	Population	Crude Rate
def fetch_data():
    # Load the data to be processed
    file_name="{}/Mortality_2006_2012.txt".format(BASE_DIR)
    data_set = pd.read_csv(file_name, sep='\t',converters={'County Code': lambda x: str(x),
                                                           'Population': lambda x: convert_population(x)})
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

def clean_data(data_set):
    get_state = lambda x: x[-2:]
    get_county_nm = lambda x: x[:-11]
    encode_suppressed = lambda x: 1 if x=='Suppressed' or x=='Missing' else int(x)

    data_set["State"] = data_set["County"].apply(get_state)
    data_set["County_nm"] = data_set["County"].apply(get_county_nm)
    data_set["Deaths"] = data_set["Deaths"].apply(encode_suppressed)
    data_set = data_set.drop(["County"], axis=1)
    data_set = data_set.drop(["Notes"], axis=1)
    data_set = data_set.drop(["Crude Rate"], axis=1)
    data_set.rename(columns={'County Code': 'County_cd'}, inplace=True)
    data_set['Deaths_Per_pop'] = round(data_set['Deaths'] / (data_set['Population']/100000), 0)

    data_set = data_set.drop(["Deaths"], axis=1)
    data_set = data_set.drop(["Population"], axis=1)
    data_set = data_set.sort_values('Deaths_Per_pop')
    print(data_set.head())
    return data_set



if __name__=='__main__':
    data_set = fetch_data()
    data_set = clean_data(data_set)
    file_name = "{}/Mortality_2006_2012.csv".format(BASE_DIR)
    data_set.to_csv(file_name, index=None, header=True)


