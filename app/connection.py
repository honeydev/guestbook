import os
import sqlite3

from main import DATABASE, TEST_DATABASE, TEST_MODE, APP_DIR


class Connection:

    def __init__(self, db: str):
        self._db = APP_DIR + '/' + db
        self._connect = sqlite3.connect(self._db)
        self._cursor = self._connect.cursor()

    def __del__(self):
        self._connect.close()

    def create(self, query: str) -> None:
        self._cursor.execute(query)

    def select(self, query) -> dict:
        self._cursor.execute(query)
        return {
            'headers': list(
                map(lambda description: description[0], self._cursor.description)
            ),
            'values': self._cursor.fetchall()
        }

    def insert(self, query) -> int:
        self._cursor.execute(query)
        self._connect.commit()
        return self._cursor.lastrowid

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def get_database(cls):
        if TEST_MODE:
            return TEST_DATABASE
        return DATABASE

    @classmethod
    def drop(cls):
        os.remove(f'{APP_DIR}/' + cls.get_database())

    @classmethod
    def get_connection(cls):
        return Connection(cls.get_database())
