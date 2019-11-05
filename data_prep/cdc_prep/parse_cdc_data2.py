import pandas as pd

BASE_DIR = './data'

def fetch_data(year):
    # Load the data to be preccessed
    file_name="{}/Mortality_{}.txt".format(BASE_DIR,year)
    data_set = pd.read_csv(file_name, sep='\t',converters={'County Code': lambda x: str(x)})
    print(data_set.columns)
    print("data_set (rows, columns) {}\n".format(data_set.shape))
    print("data_set missing values \n{}\n".format(data_set.isnull().sum()))
    return data_set

def clean_data(data_set):
    get_state = lambda x: x[-2:]
    get_county_nm = lambda x: x[:-11]
    encode_suppressed = lambda x: -1 if x=='Suppressed' else x

    data_set["State"] = data_set["County"].apply(get_state)
    data_set["County_nm"] = data_set["County"].apply(get_county_nm)
    data_set["Deaths"] = data_set["Deaths"].apply(encode_suppressed)
    data_set = data_set.drop(["County"], axis=1)
    data_set = data_set.drop(["Notes"], axis=1)
    data_set = data_set.drop(["Crude Rate"], axis=1)
    data_set.rename(columns={'County Code': 'County_Code'}, inplace=True)
    print(data_set.head())
    return data_set

if __name__=='__main__':
    for year in range(2006,2013):
        data_set = fetch_data(year)
        data_set = clean_data(data_set)
        file_name = "{}/Mortality_{}.csv".format(BASE_DIR,year)
        data_set.to_csv(file_name, index=None, header=True)


