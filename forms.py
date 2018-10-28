from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators


class RegistrationForm(Form):
    name = StringField('Name',
            [validators.Length(min=3, max=50)])
    username = StringField('Username',
            [validators.Length(min=3, max=25)])
    email = StringField('Email',
            [validators.Email()])
    password = PasswordField('Password',
            [validators.Length(min=8, max=50),validators.EqualTo('confirm_password',message='Password must match')])
    confirm_password = PasswordField('Confirm Password')
    #submit=SubmitField("Register")


class LoginForm(Form):
    username = StringField('Username',
            [validators.DataRequired()])
    password = PasswordField('Password',
            [validators.DataRequired()])
    #submit=SubmitField("Login")