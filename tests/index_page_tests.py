import unittest
import requests

from tests.common import BaseTest
from main import APP_HOST
from app.fixtures_utils.fixtures_parser import FixturesParser


class TestNotes(BaseTest):

    def setUp(self) -> None:
        super().setUp()
        fixture_parser: FixturesParser = FixturesParser()
        self._note_fixtures = fixture_parser.parse(fixture_type='notes')

    def test_notes_view(self):
        response = requests.get(url=APP_HOST)
        response_html = response.text

        for note_fixture in self._note_fixtures:

            self.assertIn(note_fixture['title'], response_html)
            self.assertIn(note_fixture['body'], response_html)
            self.assertIn(note_fixture['author'], response_html)


if __name__ == '__main__':
    unittest.main()
