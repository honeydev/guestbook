import os

from flask import Flask


app = Flask(__name__)

APP_NAME = 'Guestbook'
APP_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_FOLDER = APP_DIR + '/fixtures'
DATABASE = 'database.db'

@app.route('/')
def index():
    return 'Hello world'
