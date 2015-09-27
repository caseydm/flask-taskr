# project/forms.py


from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DateRequired


class AddTaskForm(Form):
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DateRequired()])
    due_date = DateField(
        'Date Due (mm/dd/yyyy)',
        validators=[DateRequired()], format='%m/%d/%Y'
    )
    priority = SelectField(
        'Priority',
        validators=[DateRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
            ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
        ]
    )
    status = IntegerField('Status')
