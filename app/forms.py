from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField, DecimalField
from wtforms.validators import DataRequired, Required
from flask_wtf import FlaskForm

class Subscribe_form(FlaskForm):
    Topic = TextAreaField('Topic', validators=[DataRequired()])
    submit = SubmitField('Subscribe')
    

class Publish_form(FlaskForm):
    Input = TextAreaField('Input', validators=[DataRequired()])
    submit = SubmitField('Publish')


class Index_form(FlaskForm):
    Broker = TextAreaField('Broker (e.g sungura1-angani-ke-host.africastalking.com)', validators=[DataRequired()])
    port = DecimalField('Port (e.g 10883)', validators=[DataRequired()])
    user = TextAreaField('user', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    client = TextAreaField('client(e.g Anto)', validators=[DataRequired()])
    submit = SubmitField('submit')
