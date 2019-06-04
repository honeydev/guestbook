from wtforms import (
    Form, StringField, PasswordField, validators
)


class RegistrationForm(Form):

    login = StringField('login', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.Length(min=4, max=25),
        validators.DataRequired(),
        validators.EqualTo('password_repeat', message='Passwords must match')
    ])
    password_repeat = PasswordField('Repeat Password')
