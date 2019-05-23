import unittest
from unittest import TestCase

import requests

from app.fixtures_utils.fixtures_parser import FixturesParser


class TestNotes(TestCase):

    def setUp(self):
        fixtures_parser: FixturesParser = FixturesParser()
        self._note_fixtures: tuple = fixtures_parser.parse(fixture_type='notes')

    def test_notes_view(self):
        response = requests.get(url='http://localhost:5000')
        response_html = response.text

        for note_fixture in self._note_fixtures:
            self.assertIn(note_fixture['title'], response_html)
            self.assertIn(note_fixture['body'], response_html)
            self.assertIn(note_fixture['author'], response_html)


if __name__ == '__main__':
    unittest.main()
