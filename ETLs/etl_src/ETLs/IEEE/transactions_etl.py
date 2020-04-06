from time import sleep

from etl_src.etl_pipelines.csv import CSV
from etl_src.schemas.transactions import transactions_schema, primary_key
from etl_src.services.postgres import post_gres, PostGresRowInserter
from etl_src.util.logging import init_logging


def transactions_etl(pretend_start_ds, pretend_end_ds):
    TABLE = "transactions"

    logger = init_logging("transactions_etl")

    sleep(10)
    with post_gres() as cursor:
        row_inserter = PostGresRowInserter(TABLE, list(transactions_schema.keys()), primary_key, cursor, logger)
        csv_pipeline = CSV("/app/data/train_transaction.csv", TABLE, transactions_schema, row_inserter, logger)
        csv_pipeline.run_etl()
        csv_pipeline.print_report_and_exit_program()

