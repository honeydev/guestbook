from app.fixtures_utils.fixtures_parser import FixturesParser
from app.connection import Connection


class FixtureLoaderException(Exception):
    """ Fixture exceptions. """


class UsersLoader:

    def load(self, user_fixture: dict) -> None:
        connection: Connection = Connection.get_connection()
        connection.insert(f'''
            INSERT INTO users (login, hash) VALUES (
                "{user_fixture['login']}",
                "{user_fixture['hash']}"
                )
        ''')


class NotesLoader:

    def load(self, note_fixture: dict) -> None:
        connection: Connection = Connection.get_connection()
        connection.insert(f'''
            INSERT INTO notes (title, body, author, user_id) VALUES (
                "{note_fixture['title']}",
                "{note_fixture['body']}",
                "{note_fixture['author']}",
                "{note_fixture['user_id']}"
                )
        ''')



class FixturesLoader:

    LOADERS = {
        'users': UsersLoader,
        'notes': NotesLoader
    }

    def __init__(self, fixtures_parser: FixturesParser):
        self._fixtures_parser: FixturesParser = fixtures_parser

    def load(self, fixture_type: str) -> None:
        parsed_fixtures = self._fixtures_parser.parse(fixture_type)

        for fixture in parsed_fixtures:
            self._load_fixture_in_db(fixture)


    def _load_fixture_in_db(self, parsed_fixture: dict) -> None:
        try:
            loader = self.LOADERS[parsed_fixture['type']]()
        except KeyError:
            raise FixtureLoaderException(
                f'Unknown fixture type {parsed_fixture["type"]}'
            )
        loader.load(parsed_fixture)
