import sqlite3

from app.connection import Connection
from app.models.common import ModelException, ModelNotFoundException
from app.models.common import BaseModel


class Users(BaseModel):

    def __init__(self, connection: Connection):
        self._connection: Connection = connection

    def select_all():
        pass

    def select_one(self, identifier: str, identifier_value) -> dict:
        query_result: dict = self._connection.select(
            f'SELECT * FROM users WHERE {identifier} = "{identifier_value}"'
        )

        if len(query_result['values']) > self.SELECT_ONE_SELECTION_MAX_LEN:
            raise ModelException('User notes must be in one exemplar in db.')

        if len(query_result['values']) < 1:
            raise ModelNotFoundException(
                f'User winth {identifier} {identifier_value} not found in db!'
            )

        merged_notes: list = self._merge_headers_with_notes(query_result)
        return merged_notes[0]

    def create_one(self, user_data: dict) -> dict:
        try:
            user_id: int = self._connection.insert(
                f'''
                    INSERT INTO users(login, hash) VALUES (
                        "{user_data['login']}",
                        "{user_data['hash']}"
                        )
                '''
            )
        except sqlite3.IntegrityError:
            raise ModelException(
                f'User with login {user_data["login"]} already exists.'
                )
        return self.select_one(identifier='id', identifier_value=user_id)
