import os

from flask import Flask, render_template, request, redirect, url_for, session

from app.forms.registartion import RegistrationForm
from app.forms.login import LoginForm


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
    return render_template(
        'index.html', app_name=APP_NAME, notes=users.select_all(),
        auth=session.get('auth'), user=session.get('user')
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    from app.auth.actions import login as login_action

    if session['auth']:
        return redirect(url_for('index'))

    form = LoginForm(request.form)

    def post_method():
        login_result = login_action(request.form)

        if login_result:
            session['auth'] = True
            session['user'] = login_result.get_data()['user']
            return redirect(url_for('index'))

        form.login.errors.append(login_result.get_message())

        return render_template('login.jinja', app_name=APP_NAME, form=form)

    if request.method == 'POST' and form.validate():
        return post_method()

    return render_template('login.jinja', app_name=APP_NAME, form=form)


@app.route('/logout', methods=['GET'])
def logout():
    session['auth'] = False
    session['user'] = None
    return redirect(url_for('index'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    from app.auth.actions import register as register_action

    if session['auth']:
        return redirect(url_for('index'))

    form = RegistrationForm(request.form)

    def get_method():
        return render_template(
            'registration.jinja', app_name=APP_NAME, form=form
        )

    def post_method():
        register_result = register_action(request.form)

        if register_result:
            return redirect(url_for('login'))

        form.login.errors.append(register_result.get_message())

        return render_template(
            'register.jinja', app_name=APP_NAME, form=form
        )

    if request.method == 'POST' and form.validate():
        return post_method()

    return get_method()
