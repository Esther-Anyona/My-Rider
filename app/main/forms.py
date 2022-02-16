from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SearchField
from wtforms.validators import InputRequired

class SearchForm(FlaskForm):
    search = SearchField('search location', validators=[InputRequired()])
    submit = SubmitField('Submit')

class UsrForm(FlaskForm):
    pick_up = SearchField('search location', validators=[InputRequired()])
    Destination = SearchField('search location', validators=[InputRequired()])
    submit = SubmitField('Submit')
    r_now = SearchField('Request Now', validators=[InputRequired()])
    s_later = SearchField('Request later', validators=[InputRequired()])