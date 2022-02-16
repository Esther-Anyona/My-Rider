from . import main
from flask import render_template,request,redirect,url_for
from .forms import SearchForm,UsrForm
@main.route('/')
def index():
  return '<h1>Welcome to Ride Link<h1>'

@main.route('/domie_user')
def domie_user():
  return render_template('domie-user.html')