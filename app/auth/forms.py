from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,FileField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('Desired Username', validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(),Email()])
    password = PasswordField('Desire Password', validators=[Required(),EqualTo('password_confirm','Passwords must match!')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    bio = TextAreaField('Tell us about yourself', validators=[Required()])
    submit = SubmitField('SignUp')