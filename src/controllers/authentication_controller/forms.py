from wtforms import Form, StringField, PasswordField, validators, IntegerField


class UserLoginForm(Form):
    username = StringField('username', [validators.DataRequired(), validators.Length(min=1, max=25)])
    password = PasswordField('password', [validators.DataRequired(), validators.Length(min=1, max=200)])
