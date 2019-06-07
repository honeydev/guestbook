from wtforms import (
    Form, StringField, PasswordField, validators
)


class LoginForm(Form):

    login = StringField('Login', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])
