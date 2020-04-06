FROM python:3.7

ENV AIRFLOW_HOME /airflow
ENV AIRFLOW__CORE__DAGS_FOLDER /app/dags
EXPOSE 8080

RUN apt-get update
RUN apt-get install vim -y

ADD . app
WORKDIR /app
ENV PYTHONPATH /app

RUN /app/docker_pip_installation.sh
RUN airflow initdb

ENTRYPOINT ["/app/start_airflow.sh"]