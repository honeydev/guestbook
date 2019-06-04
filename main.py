import os

import sqlite3
from flask import Flask, render_template, request

from app.forms.registartion import RegistrationForm

app = Flask(__name__)


APP_NAME = 'Guestbook'
APP_HOST = os.environ.get('APP_HOST')
APP_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_FOLDER = APP_DIR + '/fixtures'
DATABASE = 'database.db'
TEST_DATABASE = 'test_database.db'
TEST_MODE = bool(os.environ.get('TEST_MODE'))


@app.route('/')
def index():
    connect = sqlite3.connect(DATABASE)
    cursor = connect.cursor()
    notes_query = cursor.execute("SELECT * FROM notes")
    headers = tuple(
        map(lambda description: description[0], notes_query.description)
    )
    notes = notes_query.fetchall()
    notes_dicts = list(
        map(lambda row: dict(zip(headers, row)), notes)
    )

    return render_template('index.html', app_name=APP_NAME, notes=notes_dicts)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)

    def get_method():
        return render_template(
            'registration.jinja', app_name=APP_NAME, form=form
        )

    if request.method == 'GET':
        return get_method()
