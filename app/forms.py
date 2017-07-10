from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class SchedulerForm(FlaskForm):
    date = DateField('DatePicker', format='%Y-%m-%d', validators=[DataRequired()])
