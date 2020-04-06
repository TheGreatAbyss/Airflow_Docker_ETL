#!/bin/bash

# start the scheduler
echo "Starting Scheduler"
airflow scheduler --daemon &
echo "Scheduler started"

# start the web server, default port is 8080
echo "starting webserver"
airflow webserver -p 8080
echo "web server started"

