from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class HireForm(FlaskForm):
	Location = StringField("Location",validators=[Required()])
	Language = StringField("Language",validators=[Required()])
	submit = SubmitField('submit')