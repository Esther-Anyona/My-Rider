from flask import render_template, redirect, request, url_for, flash, session
from . import auth
from ..models import User
from .. import db
from .forms import RegistrationFormUser, LoginFormUser
from flask_login import login_user,logout_user,login_required
from ..email import mail_message

@auth.route('auth/login/user',methods=['GET','POST'])
def login_users():
    login_form_user = LoginFormUser()
    if login_form_user.validate_on_submit():
        user = User.query.filter_by(email = login_form_user.email.data).first()
        if user is not None and user.verify_password(login_form_user.password.data):
            login_user(user,login_form_user.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('auth/login_user.html', login_form_user = login_form_user)

@auth.route('auth/register/user',methods = ["GET","POST"])
def register_user():
    form_user = RegistrationFormUser()
    if form_user.validate_on_submit():
        user = User(email = form_user.email.data, username = form_user.username.data,password = form_user.password.data, phone_number = form_user.phone_number.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Ride Link","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login_users'))
    return render_template('auth/register_user.html',registration_form_user = form_user)

@auth.route('auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


