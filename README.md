# didactic-eureka


### Simple version 
task_reading.py

### Pandas using version
task_reading_pandas.py

### test case file where you could test file and path
test_cases.py


### Docker task version
### Requirements

Make sure you have recent versions of Docker and Docker Compose.

### Building the images

This will build all of the images referenced in the Docker Compose file. You will need to re-run this after making code changes.

```
docker-compose build
```

### Starting MySQL

To start up the MySQL database. This will will take a short while to run the database’s start-up scripts.

```
docker-compose up database
```

Optional: if you want to connect to the MySQL database via the command-line client. This may be useful for looking at the database schema or data.

```
docker-compose run database mysql --host=database --user=codetest --password=swordfish codetest
```

### Running you code
docker-compose run task

### Cleaning up

To tidy up, bringing down all the containers and deleting them.

```
docker-compose down