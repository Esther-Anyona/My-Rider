from lib2to3.pgen2 import driver
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import InputRequired

class UpdateUserProfile(FlaskForm):
    location = StringField("What's your location?",validators = [InputRequired()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    driver_id = StringField("Enter the id of the driver", validators=[InputRequired()])
    review = TextAreaField('Review a rider',validators=[InputRequired()])
    submit = SubmitField('Review')
    
class UserForm(FlaskForm):
    pick_up = StringField('Enter location', validators=[InputRequired()])
    submit = SubmitField('Search')
