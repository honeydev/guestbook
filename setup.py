import sqlite3

from main import DATABASE


connect = sqlite3.connect(DATABASE)
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        title VARCHAR(50) NOT NULL,
        body VARCHAR(500) NOT NULL,
        author CHAR(30) NOT NULL,
        creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
        )
''')


from app.fixtures_utils.fixtures_parser import FixturesParser
from app.fixtures_utils.fixtures_loader import FixturesLoader
parser = FixturesParser()
loader = FixturesLoader(parser)
loader.load('notes')
import pdb; pdb.set_trace()
connect.close()
