from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired, Required
from flask_wtf import FlaskForm

class Subscribe_form(FlaskForm):
    Topic = TextAreaField('Topic', validators=[DataRequired()])
    submit = SubmitField('Subscribe')
    #myChoices = #number of choices
    #myField = SelectField(u'Field name', choices = myChoices, validators = [Required()])

class Publish_form(FlaskForm):
    Input = TextAreaField('Input', validators=[DataRequired()])
    submit = SubmitField('Publish')
