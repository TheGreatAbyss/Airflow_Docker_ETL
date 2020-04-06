FROM python:3.7

ADD ./ETLs app
WORKDIR /app
ENV PYTHONPATH /app

RUN /app/docker_pip_installation.sh

#CMD ["python -m etl_src.entry_point"]