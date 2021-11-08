import pandas as pd
import csv

# test data file path, the fils is a csv file.
test_data_file_path = '/home/samat/didactic-eureka/data/test_data.csv'
# test data file object
test_data_file_object = None
# test data row list.
test_data_row_list = list()
# load test data from ./test_data.csv file.
def load_test_data():
    global test_data_file_object, test_data_row_list
    # open test data csv file.
    test_data_file_object = open(test_data_file_path, 'r')
    # read the csv file and return the text line list.
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    for row in csv_reader:
        test_data_row_list.append(row)
    print('open and load data from test_data.csv complete.')
# close and release the test data file object.
def close_test_data_file():
    global test_data_file_object
    if test_data_file_object is not None:
        test_data_file_object.close()
        test_data_file_object = None
        print('close file test_data.csv complete.')

load_test_data()
close_test_data_file()
# read file by using pandas
df = pd.read_csv('/home/samat/didactic-eureka/data/people.csv')

# change column names
df = df.rename(columns={
    "given_name": "Name", 
    "family_name": "Surname",
    "date_of_birth": "Date",
    "place_of_birth": "Place"
    })

df['Fullname'] = df['Name'] + " " + df['Surname']

# write file to path
df.to_json ('/home/samat/didactic-eureka/data/task_pandas.json')