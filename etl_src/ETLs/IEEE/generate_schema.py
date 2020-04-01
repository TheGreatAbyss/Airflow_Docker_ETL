"""
This only exists as a quick way to generate the schema and create the tables
You may have to increase the default Docker memory to run
"""
import pandas as pd

from etl_src.util.logging import init_logging
from etl_src.util.schema_inferences import SchemaInferences

logger = init_logging("test_schema_inferences")

df = pd.read_csv("/app/data/train_transaction.csv")
logger.info("Read DF")
schema_inferences = SchemaInferences(df, logger)
converted_data_types = schema_inferences.create_converted_data_types()

logger.info("transaction_python")
for col, dtype in schema_inferences.python_data_types.items():
    print('"{col}": {dtype},'.format(col = col, dtype = dtype))

logger.info("transaction_post_gres")
for col, dtype in schema_inferences.postgres_data_types.items():
    print('"{col}" {dtype},'.format(col = col, dtype = dtype))

df = pd.read_csv("/app/data/train_identity.csv")
logger.info("Read DF")
schema_inferences = SchemaInferences(df, logger)
converted_data_types = schema_inferences.create_converted_data_types()

logger.info("identity_python")
for col, dtype in schema_inferences.python_data_types.items():
    print('"{col}": {dtype},'.format(col = col, dtype = dtype))

logger.info("identity_post_gres")
for col, dtype in schema_inferences.postgres_data_types.items():
    print('"{col}" {dtype},'.format(col = col, dtype = dtype))