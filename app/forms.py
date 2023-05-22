from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, EmailField, SubmitField
from wtforms.validators import Email, EqualTo, InputRequired, Length
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=12)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    first_name = StringField('First name', validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField('Last name', validators=[InputRequired()])
    dob = DateField('Date of Birth', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=10)])
    password2 = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')    