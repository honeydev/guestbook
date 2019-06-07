from werkzeug.security import generate_password_hash
from app.connection import Connection

from app.models.users import Users


def user_factory(login: str, password: str) -> dict:
    users = Users(Connection.get_connection())
    user = users.create_one({
        'login': login,
        'hash': generate_password_hash(password)
    })
    user['password'] = password
    return user
