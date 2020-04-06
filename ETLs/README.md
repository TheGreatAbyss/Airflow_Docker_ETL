### Pretend Application that can exist separate from this repo

This folder contains a pretend ETL application.  In a real production environment this would be a 
separate repo that saves images to your Docker repository.  

In this repo example as well as a production environment, Airflow uses the DockerOperator to simply 
`docker run` the deployed image with this etl application code inside of it.   I only included it in the same repo
as airflow for convenience sake

To build the image in this folder use the `./util.sh etl-build-image` command