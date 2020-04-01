import pandas as pd
from collections import OrderedDict

import numpy as np


boolean_T_F_set = {"T", "F"}
boolean_1_0_set = {1, 0}
boolean_float_set = {1.0, 0.0}
boolean_true = ["T", 1]


class SchemaInferences:
    def __init__(self, df, logger):
        """
        :type df: pd.DataFrame
        """
        self.df = df
        self.logger = logger
        self._data_types = OrderedDict()
        self._python_data_types = OrderedDict()
        self._postgres_data_types = OrderedDict()

    # @staticmethod
    # def convert_to_boolean(value):
    #     if pd.isna(value):
    #         return np.nan
    #     else:
    #         return True if value in boolean_true else False

    def determine_if_bool_column(self, column):
        column_series = self.df[column]
        self.logger.debug('Colunm Name: {0}'.format(column))
        self.logger.debug('Colunm Dtype: {0}'.format(column_series.dtype))
        self.logger.debug('Sample Column Contents: {0}:'.format(column_series.values[:5]))

        unique_values = set(column_series.unique())
        unique_values_set = {item for item in unique_values if pd.notna(item)}

        if unique_values_set == boolean_T_F_set or unique_values_set == boolean_1_0_set or unique_values_set == boolean_float_set:
            return True
        else:
            return False
            # self.df[column] = self.df[column].apply(SchemaInferences.convert_to_boolean, convert_dtype=True)
            # print(self.df[column])
            # self.df.assign(test_col=SchemaInferences.convert_to_boolean)
            # print(self.df)

    def get_initial_underlying_data_types(self):
        if self._data_types:
            return self._data_types
        else:
            for column in self.df:
                self._data_types[column] = self.df[column].dtype
            return self._data_types

    def create_converted_data_types(self):
        self.get_initial_underlying_data_types()
        for col, dtype in self._data_types.items():
            bool_column = self.determine_if_bool_column(col)
            if bool_column:
                self._python_data_types[col] = "bool"
                self._postgres_data_types[col] = "BOOLEAN"
            elif "int" in str(dtype):
                self._python_data_types[col] = "int"
                self._postgres_data_types[col] = "INTEGER"
            elif str(dtype) == "object":
                self._python_data_types[col] = "str"
                self._postgres_data_types[col] = "VARCHAR(250)"
            elif "float" in str(dtype):
                self._python_data_types[col] = "float"
                self._postgres_data_types[col] = "FLOAT8"
            elif "bool" in str(dtype):
                self._python_data_types[col] = "bool"
                self._postgres_data_types[col] = "BOOLEAN"
            else:
                raise Exception("didn't find datatype for col: {col}, np_type: {np}".format(col = col, np = dtype))


    @property
    def python_data_types(self):
        if not self._python_data_types:
            self.create_converted_data_types()
        return self._python_data_types

    @property
    def postgres_data_types(self):
        if not self._postgres_data_types:
            self.create_converted_data_types()
        return self._postgres_data_types