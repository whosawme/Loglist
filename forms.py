from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField, validators, TextAreaField


class DataForm(FlaskForm):
    message = StringField('Data', [validators.Required()])
    last_message = TextAreaField('LastMessage', default="add")
    submit = SubmitField('Submit')