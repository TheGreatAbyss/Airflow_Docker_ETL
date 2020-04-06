
import csv
import logging
import sys

from collections import OrderedDict


class CSV:
    def __init__(self, file, table, schema, row_inserter, logger):
        """
        :type file: str
        :type table: str
        :type schema: OrderedDict
        :type logger: logging.Logger
        """
        self.file = file
        self.table = table
        self.schema = schema
        self.columns = list(self.schema.keys())
        self.row_inserter = row_inserter
        self.logger = logger
        self.exit_status = 0
        self.conversion_errors = 0
        self.insertion_errors = 0
        self.rows_inserted = 0

    def apply_conversion(self, value, idx):
        col = self.columns[idx]
        try:
            self.logger.debug(col)
            self.logger.debug(value)
            return self.schema[col](value)
        except Exception as e:
            msg = "Failed to convert table: {table}, column: {column}, type: {type}, value: {value}".format(
                table=self.table,
                column=col,
                type=self.schema[col],
                value=value
            )
            self.logger.error(msg)
            self.exit_status = 1
            self.conversion_errors += 1

    def run_etl(self):
        with open(self.file, 'r') as fh:
            csv_reader = csv.reader(fh, delimiter=',')
            next(csv_reader, None)
            for row in csv_reader:
                converted = []
                for idx, item in enumerate(row):
                    converted.append(self.apply_conversion(item, idx))
                self.row_inserter.insert_into_database(converted)
                self.rows_inserted += 1
                if self.rows_inserted % 10000 == 0:
                    self.logger.info("Inserted {0} rows so far".format(self.rows_inserted))

    def print_report_and_exit_program(self):
        self.logger.info("""
        ETL for {table} completed with {rows} rows inserted, {errors} conversion_errors and {insertion} insertion_errors
        """.format(
            table = self.table,
            rows = self.rows_inserted,
            errors = self.conversion_errors,
            insertion = self.insertion_errors
        ))
        sys.exit(self.exit_status)

