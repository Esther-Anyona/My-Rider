from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired


class UsrForm(FlaskForm):
    pick_up = StringField('Enter location', validators=[InputRequired()])
    Destination = StringField('Enter Destination', validators=[InputRequired()])
    r_now = StringField('Request Now', validators=[InputRequired()])
