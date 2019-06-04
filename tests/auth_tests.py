
import requests
import unittest
from faker import Faker

from main import APP_HOST
from app.factories import user_factory
from tests.common import BaseTest


class TestRegister(BaseTest):

    def setUp(self) -> None:
        super().setUp()
        self._faker = Faker()

    def test_register_user(self):

        user_data = {
            "login": self._faker.user_name(),
            "password": self._faker.password()
        }
        user_data['password_repeat'] = user_data['password']

        response = requests.post(
            url=APP_HOST + '/registration',
            data=user_data
        )

        self.assertEqual(response.url, APP_HOST + '/login')


class LoginUser(BaseTest):

    def setUp(self) -> None:
        super().setUp()
        self._faker = Faker()

    def test_login(self):

        user = user_factory(self._faker.user_name(), self._faker.password())

        response = requests.post(
            url=APP_HOST + '/login',
            data={
                'login': user['login'],
                'password': user['password']
            }
        )

        self.assertEqual(response.url, APP_HOST + '/')


if __name__ == '__main__':
    unittest.main()
