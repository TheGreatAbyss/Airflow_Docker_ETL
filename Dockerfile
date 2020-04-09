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

# Add Tini
# https://github.com/krallin/tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Run your program under Tini
CMD ["/app/start_airflow.sh"]
# or docker run your-image /your/program ...
