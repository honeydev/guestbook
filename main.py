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
    from app.models.notes import Notes
    from app.connection import Connection

    users = Notes(Connection.get_connection())
    return render_template('index.html', app_name=APP_NAME, notes=users.select_all())


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)

    def get_method():
        return render_template(
            'registration.jinja', app_name=APP_NAME, form=form
        )

    if request.method == 'GET':
        return get_method()
