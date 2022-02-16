from . import main
from flask import render_template,session, request,redirect,url_for,abort, flash
from ..models import User


@main.route('/')
def index():
  return render_template('home.html')

@main.route('/user')
def user():
  return render_template('user.html')