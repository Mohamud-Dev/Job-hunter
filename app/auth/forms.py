from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, PasswordField
from wtforms.validators import ValidationError, Email, Required, EqualTo
from ..models import User
from wtforms import TextAreaField,FileField


class SignUp(FlaskForm):
    username = StringField('Username:', validators=[Required()] )
    email = StringField('Email:', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(),EqualTo('confirm_password', 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    # def validate_username(self,data_field):
    #     if User.query.filter_by(username = data_field.data).first():
    #         raise ValidationError('username already exists')

    # def validate_email(self, data_field):
    #     if User.query.filter_by(email = data_field.data):
    #         raise ValidationError('The email address has already been used')



class SignIn(FlaskForm):
    username = StringField('Username:', validators=[Required()] )
    email = StringField('Email:', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    Remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')




class RegistrationForm(FlaskForm):
    username = StringField('Desired Username', validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(),Email()])
    password = PasswordField('Desire Password', validators=[Required(),EqualTo('password_confirm','Passwords must match!')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    bio = TextAreaField('Tell us about yourself', validators=[Required()])
    submit = SubmitField('SignUp')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

