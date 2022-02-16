from . import main
from flask import render_template,session, request,redirect,url_for,abort, flash
from ..models import User
from .. import db
from .forms import UpdateUserProfile
from flask_login import login_required, current_user



@main.route('/')
def index():
  return render_template('home.html')

@main.route('/user')
def user():
  return render_template('user.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile_users.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateUserProfile()

    if form.validate_on_submit():
        user.location = form.location.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_user.html',form =form)