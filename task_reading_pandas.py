import pandas as pd
import json
import test_cases

def reading_data_by_pandas(path: str):
    print("reading csv file ...")
    return pd.read_csv(path)

if __name__ == '__main__':
    # run test case
    test_cases.load_test_data()
    test_cases.close_test_data_file()

    # read file by using pandas
    df = reading_data_by_pandas('/home/samat/didactic-eureka/data/people.csv')

    # change column names Mapping task
    df = df.rename(columns={
        "given_name": "Name", 
        "family_name": "Surname",
        "date_of_birth": "Date",
        "place_of_birth": "Place"
    })
    print("Mapping data from csv to json done")
    # add new column
    df['Fullname'] = df['Name'] + " " + df['Surname']

    # write file to path
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    
    with open('/home/samat/didactic-eureka/data/task_pandas.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(parsed, indent=4))
    print("Transform data from csv to json done")