from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class HireForm(FlaskForm):
	Location = StringField("Location",validators=[Required()])
	Language = StringField("Language",validators=[Required()])
	submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")

class bio(FlaskForm):

    bio = StringField('Tell us about you',id='bio', validators=[Required()])
    submit = SubmitField('Update')