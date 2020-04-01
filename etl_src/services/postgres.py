import contextlib

import psycopg2


@contextlib.contextmanager
def post_gres(failures = 0):
    """
    postgresql://<username>:<password>@<hostname>:<port>/<database>
    """
    connection_string = "postgresql://etl:etl@db:5432/etl"
    connection = psycopg2.connect(connection_string)

    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        connection.commit()
        cursor.close()
        connection.close()
        failures += 1


class PostGresRowInserter:
    def __init__(self, table, cols, cursor, logger):
        self.table = table
        self.cols = cols
        self.col_string, self.input_string = PostGresRowInserter.create_col_and_val_string(self.cols)
        self.insert_statement = ""
        self.cursor = cursor
        self.create_insert_statement()
        self.logger = logger

    @staticmethod
    def create_col_and_val_string(cols):
        col_string = ''
        insert_string = ''
        for column in cols:
            col_string += '"{0}", '.format(column)
            insert_string += "{0}, ".format('%s')
        return col_string[:-2], insert_string[:-2]


    def create_insert_statement(self):
        self.insert_statement = "INSERT INTO {table} ({columns}) VALUES ({values})".format(
            table=self.table,
            columns=self.col_string,
            values=self.input_string
        )

    def insert_into_database(self, values):
        self.logger.debug(self.insert_statement)
        self.logger.debug(values)
        self.cursor.execute(self.insert_statement, values)
