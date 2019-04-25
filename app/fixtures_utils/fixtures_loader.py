import sqlite3

from main import DATABASE
from app.fixtures_utils.fixtures_parser import FixturesParser


class FixtureLoaderException(Exception):
    pass


class NotesLoader:

    def load(self, note_fixture: dict) -> None:
        connect = sqlite3.connect(DATABASE)
        cursor = connect.cursor()
        cursor.execute(f'''
            INSERT INTO notes (title, body, author) VALUES (
                "{note_fixture['title']}",
                "{note_fixture['body']}",
                "{note_fixture['author']}"
                )
        ''')
        connect.commit()
        connect.close()



class FixturesLoader:

    LOADERS = {
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
