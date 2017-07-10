from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class SchedulerForm(Form):
    date = DateField('DatePicker', format='%Y-%m-%d', validators=[DataRequired()])
