from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField) # BooleanField
from wtforms.validators import (Length, EqualTo, InputRequired, ValidationError)
from ImagePantry.models import users

class CreateAccountForm(FlaskForm):
    name     = StringField('Name', validators=[
                InputRequired(message="This field can't be blank"), 
                Length(min=2, max=32, message="Must be at least 2 characters")])
    password = PasswordField('Password', validators=[
                InputRequired(message="This field can't be blank"), 
                Length(min=6, max=255, message="Password must be at least 6 characters")])
    confirm  = PasswordField('Confirm password', validators=[
                InputRequired(), Length(min=6,max=255), 
                EqualTo('password', message='Passwords must match')])
    submit   = SubmitField('Create account')

    def validate_username(self):
        res = users.find_one({ "name": self.name.data })
        if res:
            raise ValidationError(f'This username is taken')

class LoginForm(FlaskForm):
    name     = StringField('Name', validators=[
                InputRequired(message="This field can't be blank"), 
                Length(min=2, max=32)])
    password = PasswordField('Password', validators=[
                InputRequired(message="This field can't be blank"), 
                Length(min=6, max=255, message="Password must be at least 6 characters")])
    submit   = SubmitField('Login')

    def validate_email(self):
        user = users.find_one({ "name": self.name.data })
        if user is None:
            raise ValidationError('Wrong username')