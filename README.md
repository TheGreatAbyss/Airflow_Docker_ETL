# Apache Airflow Pretend ETL - Fully Dockerized
This repo contains a pretend ETL running with [Apache Airflow](https://airflow.apache.org/)

The repo provides the following functionality:
1.  The top level of this repo will create a docker application of two containers using Docker-compose.  
    The first runs Apache Airflow, and the second runs PostGres
    
1. The ETLs folder contains a self contained Python ETL application that performs an ETL on some sample data.
It contains a DockerFile for building this application as a Docker image

1.  When running Airflow in the docker application mentioned above, Airflow will run the ETL application 
as a Docker Image using the DockerOperator.  The ETL will continue to run on the schedule set in the
ieee.py dag  
You can monitor it on the Airflow UI at `localhost:8080`.  
Be sure to either turn the schedule on, or run it manually 
 

#### Requirements:
1. Install Docker if not already installed: https://www.docker.com/

### Installation:
1. Pull down this repo with git clone
1. In the ETLs directory create a folder called data, and place the sample data in it.  I didn't include it because it's too large
1. In the top level directory create another folder called postgres-data, this is where post-gres will maintain state when the container is not running
1. Build the swarm containing Airflow and Postgres:  
    ```
    ./util.sh airflow-build
    ```
1. Build the ETL application:
    ```
    ./util.sh etl-build-image
    ``` 
1. Start the airflow and postgres application:
   ```
   ./util.sh airflow-start
   ``` 
1. Create the tables in postgres using a pretend migration tool:
    ```
    ./util.sh run-migration
    ```
1. View the Airflow UI at: http://localhost:8080/

You can also test the jobs manually using just the ETL application container with:
    ```
    './util.sh etl-run'
    ```

Note:  The airflow container mounts to your docker socket at `/var/run/docker.sock`.

### Stopping the application
**Important** To stop the application run
```
./util-sh airflow-stop
```
This runs `docker-compose down`. 
It's important to stop the application with this command as it will remove the created containers.  If you do not
do this when stopping the containers then the airflow process may not be properly terminated.  
When you running docker-compose up again it will simply restart the existing container, 
which my cause issues with already running processes.  


# Development
### Using Pycharm PE
The best way to do local development on this repo is with PyCharm Professional Edition using 
the Docker image is the interpreter.  
1. Run build-image if not already done: `./util.sh etl-build-image`
1. Point Pycharm PE interpreter at the image: 
```
Pycharm -> Preferences -> Project -> Project Interpreter -> Click Drown Down -> Show All -> "+" 
-> Docker -> Etl-application
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

