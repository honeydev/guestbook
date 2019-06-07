from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users import Users
from app.models.common import ModelException, ModelNotFoundException
from app.connection import Connection
from app.factories import user_factory


class AuthResult:

    def __init__(
            self, success: bool, message: str = '', data: dict = {}
    ) -> None:
        self._success = success
        self._message = message
        self._data = data

    def __bool__(self) -> bool:
        return self._success

    def get_message(self) -> str:
        return self._message

    def get_data(self):
        return self._data


def login(form):
    users = Users(Connection.get_connection())
    try:
        target_user: dict = users.select_one(
            identifier='login', identifier_value=form.get('login')
        )
        if check_password_hash(target_user['hash'], form.get('password')):
            return AuthResult(True, data={'user': target_user})
        return AuthResult(False, 'Invalid password!')
    except (ModelException, ModelNotFoundException) as e:
        return AuthResult(False, str(e))


def register(form):
    try:
        user_factory(form.get('login'), form.get('password'))
    except ModelException as e:
        return AuthResult(False, str(e))
    return AuthResult(True)
