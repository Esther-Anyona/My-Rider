from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import InputRequired

class UpdateUserProfile(FlaskForm):
    location = StringField("What's your location?",validators = [InputRequired()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    review = TextAreaField('Review a rider',validators=[InputRequired()])
    submit = SubmitField('Review')