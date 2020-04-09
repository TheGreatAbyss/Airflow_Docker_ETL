#!/bin/bash

cmd=$1

case $cmd in
    'etl-run') docker run --net etl-network -it --rm -v $PWD/ETLs:/app etl-application python ./etl_src/entry_point.py --job_and_func=ETLs.IEEE.identities_etl.identities_etl --start_date=2017-04-25 --end_date=2017-05-15
    ;;
    'etl-shell') docker run --net etl-network -it --rm -v $PWD/ETLs:/app etl-application bash
    ;;
    'etl-build-image') docker build --no-cache -t etl-application -f ./ETLs/Dockerfile .
    ;;
    'airflow-build') docker-compose build
    ;;
    'airflow-start') docker-compose up
    ;;
    'airflow-stop') docker-compose down
    ;;
    'airflow-shell') docker-compose run -v $PWD:/app app python -m etl_src.ETLs.IEEE.transactions_etl
    ;;
    'run-migration') docker run --net etl-network -it --rm etl-application python /app/migrations/migrations.py
    ;;
    '') echo "Usage: $0 <command>"; exit 1
    ;;
    *) echo "Unknown command: $cmd"; exit 1
    ;;
esac