# Installation

docker-compose build
docker-compose run app python /app/migrations/migrations.py

#### Requirements:
1. Install Docker if not already installed: https://www.docker.com/

### Basic steps to build application and run the ETL using Apache Airflow:
1. Pull down this repo with git clone
1. In your working directory create a folder called data, and place the sample data in it.  I didn't include it because it's too large
1. Create another folder called postgres-data, this is where post-gres will maintain state when the image is not running
1. Build two docker images, one with Airflow and one with Postgres: `docker-compose build`
1. Create the tables in postgres using a pretend migration tool: `docker-compose run app python /app/migrations/migrations.py`
1. You can then manually run the two ETLS with:  
```
docker-compose run app python -m etl_src.ETLs.IEEE.transactions_etl
docker-compose run app python -m etl_src.ETLs.IEEE.identities_etl
```
1. To run the full application with Airflow simply run `docker-compose up`
1. View the Airflow UI at: http://localhost:8080/


# Development
The recommended way to do development within this repo is to use an IDE that supports Docker as
a Python interpreter.  I recommend using Pycharm Professional, but if that is not available
visual studio code is free and also supports this:  https://code.visualstudio.com/docs/remote/containers 

note:  It might be possible to build airflow in a Virtualenv using Pipenv for local dev, but I encountered 
pipenv installation errors

To run the application using your local development folder mounted:
```
docker-compose run -v $PWD:/app app python -m etl_src.ETLs.IEEE.transactions_etl
```

Be sure to rebuild after any changes 

### Using Pycharm PE
The best way to do local development on this repo is with PyCharm Professional Edition using 
the Docker image is the interpreter.  
1. Run build-image if not already done: `./util.sh build-image`
1. Point Pycharm PE interpreter at the image: 
```
Pycharm -> Preferences -> Project -> Project Interpreter -> Click Drown Down -> Show All -> "+" 
-> Docker Compose -> ./docker-compose.yml -> app
```

### Testing Airflow DAGS and Tasks
To test Airflow Dags and Tasks you can enter into a container with app already running 
```
# Get the container ID
docker ps

# Connect to it:
docker exec -it [container id] bash
```

Run various tests 
```
# Test for errors in DAG
python dags/tutorial.py 

# Test run a specific task
airflow test tutorial print_date 2015-06-01

# Run a DAG for a range of dates
airflow backfill tutorial -s 2015-06-01 -e 2015-06-07 
```

