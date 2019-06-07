import unittest
from unittest import TestCase

from faker import Faker
from werkzeug.security import generate_password_hash

from app.connection import Connection
from app.models.users import Users
from app.models.common import ModelException
from setup import setup_db


class TestCreate(TestCase):

    def setUp(self):
        setup_db()
        self._users = Users(Connection.get_connection())
        self._faker = Faker()

    def test_create_user(self):

        user_data = {
            "login": self._faker.user_name(),
            "hash": generate_password_hash(self._faker.password())
        }

        user = self._users.create_one(user_data)

        self.assertEqual(user_data['login'], user['login'])
        self.assertEqual(user_data['hash'], user['hash'])
        self.assertIn('id', user)

        with self.assertRaises(ModelException):
            self._users.create_one(user_data)

    def tearDown(self):
        Connection.drop()


if __name__ == '__main__':
    unittest.main()
