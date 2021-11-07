import pandas as pd
import pysftp

myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print ("Connection succesfully stablished ... ")

    # Define the file that you want to download from the remote directory
    remoteFilePath = '/var/integraweb-db-backups/TUTORIAL.txt'

    # Define the local path where the file will be saved
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
    localFilePath = './TUTORIAL.txt'

    sftp.get(remoteFilePath, localFilePath)

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