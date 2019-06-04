from unittest import TestCase
from setup import setup_db

from app.connection import Connection


class BaseTest(TestCase):

    def setUp(self) -> None:
        setup_db()

    def tearDown(self) -> None:
        Connection.drop()
