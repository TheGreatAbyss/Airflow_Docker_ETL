from time import sleep

from etl_src.etl_pipelines.csv import CSV
from etl_src.schemas.identities import identities_schema, primary_key
from etl_src.services.postgres import post_gres, PostGresRowInserter
from etl_src.util.logging import init_logging


def identities_etl(pretend_start_ds, pretend_end_ds):
    sleep(10)

    TABLE = "identities"

    logger = init_logging("identities_etl")

    with post_gres() as cursor:
        row_inserter = PostGresRowInserter(TABLE, list(identities_schema.keys()), primary_key, cursor, logger)
        csv_pipeline = CSV("/app/data/train_identity.csv", TABLE, identities_schema, row_inserter, logger)
        csv_pipeline.run_etl()
        csv_pipeline.print_report_and_exit_program()

