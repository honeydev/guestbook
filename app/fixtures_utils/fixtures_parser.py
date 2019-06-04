import os
import json


from main import FIXTURES_FOLDER


class FixturesParser:

    def __init__(self):
        fixtures_names: list = [fixture for _, _, fixture in os.walk(FIXTURES_FOLDER)][0]
        self._fixtures = []
        for fixture_name in fixtures_names:
            self._fixtures.append(f'{FIXTURES_FOLDER}/{fixture_name}')

    def parse(self, fixture_type: str = 'all') -> tuple:

        fixtures: dict = tuple(
            self._parse_fixture_file(fixture_file)
            for fixture_file in self._fixtures
        )

        if fixture_type == 'all':
            return fixtures

        return tuple(
            filter(lambda fixture: fixture['type'] == fixture_type, fixtures)
        )

    def _parse_fixture_file(self, fixture_file: str) -> dict:
        with open(fixture_file, 'r') as f:
            return json.load(f)
