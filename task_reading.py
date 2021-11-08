import csv
import json
import test_cases

def csv_to_json_mapping(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        print("Succesfully read file")
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Mapping task
            rows["name"] = rows.pop("given_name")
            rows["surname"] = rows.pop("family_name")
            rows["date"] = rows.pop("date_of_birth")
            rows["place"] = rows.pop("place_of_birth")
            # Assuming a column name unique something
            # be the primary key
            key = rows['name'] + "_" + rows['surname']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    print("Transformation done")
    
if __name__ == '__main__':

    # Decide the two file paths according to your
    csvFilePath = '/home/samat/didactic-eureka/data/people.csv'
    jsonFilePath = '/home/samat/didactic-eureka/data/task.json'

    # unit test
    test_cases.load_test_data(csvFilePath)
    test_cases.close_test_data_file()

    # Call the csv_to_json_mapping function
    try:
        print("Starting read csv file")
        csv_to_json_mapping(csvFilePath, jsonFilePath)
        print("Finished")
    except IOError:
        print("Error with peoples csv file")