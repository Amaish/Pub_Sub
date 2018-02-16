from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired

class Subscribe_form(FlaskForm):
    Topic = TextAreaField('Topic', validators=[DataRequired()])
    submit = SubmitField('Subscribe')

class Publish_form(FlaskForm):
    Input = TextAreaField('Input', validators=[DataRequired()])
    submit = SubmitField('Publish')