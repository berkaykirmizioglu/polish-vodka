from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def my_length_check(form, field):
    if field.data < 18:
        raise ValidationError('Age must be greater then to 18')


class AgeForm(FlaskForm):
    age = IntegerField('Type your age', validators=[DataRequired(), my_length_check])
    accept = BooleanField('Please click checkbox to agree with page rules', default=False, validators=[DataRequired()])
    submit = SubmitField('Submit')
