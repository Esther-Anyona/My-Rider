from . import main
from flask import render_template,request,redirect,url_for
from .forms import UsrForm
from app.main import forms


@main.route('/')
def index():
  return '<h1>Welcome to Ride Link<h1>'

@main.route('/usr', )
def usr():
  loc=request.args.get('loc')


  return render_template('usr.html')
@main.route('/usrform', methods=['POST','GET'])
def usrform():
  form=UsrForm()
  if request.method == 'POST':
    pick_up = request.form.get('pick_up')
    Destination = request.form.get('Destination')
    r_now = request.form.get('r_now')

    

  return render_template('usr.html',form=form)