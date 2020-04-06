import contextlib

import psycopg2


@contextlib.contextmanager
def post_gres(failures=0):
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
    def __init__(self, table, cols, primary_key, cursor, logger):
        self.table = table
        self.cols = cols
        self.primary_key = primary_key
        self.cursor = cursor
        self.logger = logger
        self.col_string = PostGresRowInserter.create_column_string(cols)

    @staticmethod
    def create_column_string(cols):
        combiner = lambda col: '"{0}", '.format(col)
        column_string = "".join(list(map(combiner, cols)))
        return column_string[:-2]

    @staticmethod
    def create_val_string(vals):
        def combiner(val):
            if not val:
                return 'NULL, '
            if type(val) is str:
                formatted = val.replace("'", "\\'")
                return "'{0}', ".format(formatted)
            else:
                return "{0}, ".format(val)
        column_string = "".join(list(map(combiner, vals)))
        return column_string[:-2]

    @staticmethod
    def create_upsert_set_string(cols, vals):
        zipped = zip(cols, vals)
        upsert_string = ""
        for col, val in zipped:
            if val:
                if type(val) is str:
                    formatted = val.replace("'", "\\'")
                    upsert_string +=  '"{0}" = \'{1}\', '.format(col, formatted)
                else:
                    upsert_string += '"{0}" = {1}, '.format(col, val)
        return upsert_string[:-2]

    def create_insert_statement(self, vals_list):
        vals = PostGresRowInserter.create_val_string(vals_list)
        upsert_string = PostGresRowInserter.create_upsert_set_string(self.cols, vals_list)

        return """
        INSERT INTO {table} ({columns}) VALUES ({values})
        ON CONFLICT ( "{primary_key}" )
        DO UPDATE SET {upsert_string}      
        """.format(
            table=self.table,
            columns=self.col_string,
            values=vals,
            upsert_string=upsert_string,
            primary_key=self.primary_key
        )

    def insert_into_database(self, values):
        insert_statement = self.create_insert_statement(values)
        self.logger.debug(insert_statement)
        self.logger.debug(values)
        self.cursor.execute(insert_statement)
