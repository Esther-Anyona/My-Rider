from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import InputRequired

class UpdateUserProfile(FlaskForm):
    location = StringField("What's your location?",validators = [InputRequired()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    review = TextAreaField('Review a rider',validators=[InputRequired()])
    submit = SubmitField('Review')
    
class UsrForm(FlaskForm):
    pick_up = StringField('Enter location', validators=[InputRequired()])
    Destination = StringField('Enter Destination', validators=[InputRequired()])
    r_now = StringField('Request Now', validators=[InputRequired()])

