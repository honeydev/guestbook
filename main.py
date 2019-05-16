import os

import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

APP_NAME = 'Guestbook'
APP_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_FOLDER = APP_DIR + '/fixtures'
DATABASE = 'database.db'

@app.route('/')
def index():
    connect = sqlite3.connect(DATABASE)
    cursor = connect.cursor()
    notes_query = cursor.execute("SELECT * FROM notes")
    headers = tuple(map(lambda description: description[0], notes_query.description))
    notes = notes_query.fetchall()
    notes_dicts = list(
        map(lambda row: dict(zip(headers, row)), notes)
    )

    return render_template('index.html', app_name=APP_NAME, notes=notes_dicts)
