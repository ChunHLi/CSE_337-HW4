from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

OPERATION_CHOICES = [('wordcount', 'wordcount'), ('charactercount', 'charactercount'), ('mostfrequent5', 'mostfrequent5')]


class SubmissionForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    delimiter = TextAreaField('Delimiter')
    operationname = SelectField('Operation', choices=OPERATION_CHOICES)
    submit = SubmitField(label='Submit')