from app.connection import Connection
from app.models.common import ModelException, ModelNotFoundException
from app.models.common import BaseModel


class Notes(BaseModel):

    def __init__(self, connection: Connection):
        self._connection: Connection = connection

    def select_all(self) -> list:
        query_result: dict = self._connection.select(
            f'SELECT * FROM notes'
        )
        return self._merge_headers_with_notes(query_result)

    def select_one(self, identifier: str, identifier_value) -> dict:
        query_result: dict = self._connection.select(
            f'SELECT * FROM notes WHERE {identifier} = "{identifier_value}"'
        )

        if len(query_result['values']) > self.SELECT_ONE_SELECTION_MAX_LEN:
            raise ModelException('Notes notes must be in one exemplar in db.')

        if len(query_result['values']) < 1:
            raise ModelNotFoundException(
                f'Notes winth {identifier} {identifier_value} not found in db!'
            )

        merged_notes: list = self._merge_headers_with_notes(query_result)
        return merged_notes[0]

    def create_one(self, notes_data: dict) -> dict:
        user_id: int = self._connection.insert(
            f'''
                INSERT INTO notes(title, body, author, user_id) VALUES (
                    "{notes_data['title']}",
                    "{notes_data['body']}",
                    "{notes_data['author']}",
                    "{notes_data['user_id']}"
                    )
            '''
        )
        return self.select_one(identifier='id', identifier_value=user_id)
