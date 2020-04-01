import unittest
import pandas as pd

from collections import OrderedDict
from numpy import dtype

from etl_src.util.logging import init_logging
from etl_src.util.schema_inferences import SchemaInferences

test_data = {"int_col": [45, 67, 54],
             "string_col": ["Bernie", "is a", "dog"],
             "bool_one_col": [0, None, 1],
             "bool_two_col": ["T", "F", None]}

logger = init_logging("test_schema_inferences")

test_schema_inferences = SchemaInferences(pd.DataFrame(test_data), logger)


def test_replace_bool_columns():
    # expected_bol_one_series = pd.Series([False, np.nan, True])
    # expected_bol_two_series = pd.Series([True, False, np.nan])

    assert(True == test_schema_inferences.determine_if_bool_column("bool_one_col"))
    assert (True == test_schema_inferences.determine_if_bool_column("bool_two_col"))
    # logger.info(test_schema_inferences.df["bool_one_col"])
    # logger.info(test_schema_inferences.df["bool_two_col"])
    # assert(test_schema_inferences.df["bool_one_col"].equals(expected_bol_one_series))
    # assert(test_schema_inferences.df["bool_two_col"].equals(expected_bol_two_series))


def test_data_types():
    # test_schema_inferences.replace_bool_columns()
    test_schema_inferences.create_converted_data_types()
    data_types = test_schema_inferences.python_data_types
    print(data_types)
    expected = OrderedDict([('int_col', 'int'), ('string_col', 'str'), ('bool_one_col', 'bool'), ('bool_two_col', 'bool')])
    assert(data_types == expected)