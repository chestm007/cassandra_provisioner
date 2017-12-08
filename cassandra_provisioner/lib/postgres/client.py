import psycopg2
from psycopg2 import extras
from ..service import Service


class PostgresClient(Service):
    def __init__(self, config):
        self.connection = None
        self.config = config.postgres

    def connect(self):
        self.connection = psycopg2.connect(
            user=self.config.user,
            password=self.config.password,
            host=self.config.host,
            database=self.config.database)

    def _get_new_cursor(self):
        return self.connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor)

    def _get_one_row(self, query, params=None):
        c = self._get_new_cursor()
        c.execute(query, params)
        return c.fetchall()
        pass

    def _get_many_rows(self, query, params=None):
        c = self._get_new_cursor()
        c.execute(query, params)
        return c.fetchall()
