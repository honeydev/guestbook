from app.connection import Connection

from app.fixtures_utils.fixtures_parser import FixturesParser
from app.fixtures_utils.fixtures_loader import FixturesLoader


def setup_db():

    connect = Connection.get_connection()

    connect.create('''
        CREATE TABLE IF NOT EXISTS users (
            login VARCHAR(20) NOT NULL UNIQUE,
            hash VARCHAR(100) NOT NULL,
            registred TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
            )
    ''')

    connect.create('''
        CREATE TABLE IF NOT EXISTS notes (
            title VARCHAR(50) NOT NULL,
            body VARCHAR(500) NOT NULL,
            author CHAR(30) NOT NULL,
            creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            user_id INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )
    ''')

    parser = FixturesParser()
    loader = FixturesLoader(parser)
    loader.load('users')
    loader.load('notes')


if __name__ == '__main__':
    setup_db()
