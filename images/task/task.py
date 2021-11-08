#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import mysql.connector
from mysql.connector import errorcode
import config as cfg

mydb = mysql.connector.connect(
    host = cfg.database_name, 
    user = cfg.database_user, 
    password = cfg.database_password, 
    charset = cfg.database_charset)
    
cursor = mydb.cursor()
cursor.execute("use codetest")
print("db connected")

for command in cfg.uft_commands:
    cursor.execute(command)

print("utf commands run")

cursor.execute("drop table if exists peoples;")
print("tables drop")

for table_name, command in cfg.tables.items():
    cursor.execute(command)
    print("table created " + table_name)
    
try:
    with open('/data/people.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        id_count = cursor.lastrowid
        for row in reader:
            cursor.execute(
                (cfg.insert_tables["peoples"]), (id_count, row[0], row[1], row[2], row[3]))
            id_count = cursor.lastrowid + 1
except IOError:
    print("Error with peoples csv file")

cursor.execute(cfg.main_query)
print("main query run")

# Get data from database 
main_data = cursor.fetchall()

try:
    with open('/data/task_docker.json', 'w') as json_file:
        rows = {}
        data = []
        # Here is my mapping and add new column 
        for i in main_data:
            content = {'id': i[0], 
                'given_name': i[1], 
                'family_name': i[2], 
                'date_of_birth': i[3], 
                'place': i[4],
                'fullname': i[1] + " " + i[2]}

            data.append(content)
            content = {}
        json.dump(data, json_file, indent=4)
except IOError:
    print("Error with output file")

print("Data loaded")

## Close connection
mydb.commit()
cursor.close()
mydb.close()