import csv
import json

try:
    with open('/home/samat/didactic-eureka/data/people.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        #next(reader)
        with open('/home/samat/didactic-eureka/data/task.json', 'w') as json_file:
            rows = {}
            for i in reader:
                print(i)
                query_row = {i[0] : i[1]}
                rows.update(query_row)
            json.dump(rows, json_file, separators=(',', ':'))
except IOError:
    print("Error with peoples csv file")