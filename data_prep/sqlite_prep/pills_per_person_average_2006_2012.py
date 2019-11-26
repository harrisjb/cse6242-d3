import pandas as pd

BASE_DIR = './data'

# County_cd,State_nm,County_nm,2006,2007,2008,2009,2010,2011,2012
def fetch_data():
    # Load the data to be processed
    file_name="{}/pills_sold_by_county_and_years.csv".format(BASE_DIR)
    data_set = pd.read_csv(file_name, sep=',',converters={'County_cd': lambda x: str(x),
                                                          '2006': lambda x: convert_pills(x),
                                                          '2007': lambda x: convert_pills(x),
                                                          '2008': lambda x: convert_pills(x),
                                                          '2009': lambda x: convert_pills(x),
                                                          '2010': lambda x: convert_pills(x),
                                                          '2011': lambda x: convert_pills(x),
                                                          '2012': lambda x: convert_pills(x)})
    print(data_set.columns)
    print("data_set (rows, columns) {}\n".format(data_set.shape))
    print("data_set missing values \n{}\n".format(data_set.isnull().sum()))
    return data_set

def convert_pills(x):
    ret_val=0
    try:
        ret_val = int(float(x))
        if ret_val < 0:
            ret_val = 0
    except:
        pass
    print(ret_val)
    return ret_val

# County_cd,State_nm,County_nm,2006,2007,2008,2009,2010,2011,2012
# county_id,State_nm,County_nm,avgerage_pills
def clean_data(data_set):
    data_set['total'] = data_set['2006'] + \
                    data_set['2007'] + \
                    data_set['2008'] + \
                    data_set['2009'] + \
                    data_set['2010'] + \
                    data_set['2011'] + \
                    data_set['2012']
    data_set['avgerage_pills'] = round(data_set['total'] / 7, 0)
    data_set = data_set.drop(['2006','2007','2008','2009','2010','2011','2012','total'], axis=1)


    return data_set



if __name__=='__main__':
    data_set = fetch_data()
    data_set = clean_data(data_set)
    file_name = "{}/pills_per_person_average_2006_2012.csv".format(BASE_DIR)
    data_set.to_csv(file_name, index=None, header=True)


