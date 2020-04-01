import unittest

from etl_src.schema_migrations.create import create_create_statement_from_data

def test_create_create_statement_from_data():
    create_create_statement_from_data("../.