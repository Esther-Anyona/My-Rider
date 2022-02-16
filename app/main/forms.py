from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired



class UpdateUserProfile(FlaskForm):
    location = StringField("What's your location?",validators = [InputRequired()])
    submit = SubmitField('Submit')