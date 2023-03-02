from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserSignUpForm(FlaskForm):
    #email,password,first_name,last_name
    email = StringField('Email', validators = [DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username')
    password = PasswordField('Password', validators = [DataRequired()])
    password1 = PasswordField('Confirm Password', validators = [DataRequired()])
    submit_button = SubmitField('Submit')
    

    
class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()
    
class ChangePassword(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit_button = SubmitField('Submit')