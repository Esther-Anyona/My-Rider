from . import main
from flask import render_template,session, request,redirect,url_for,abort, flash
from ..models import User
from .. import db
from .forms import UpdateUserProfile
from flask_login import login_required, current_user



@main.route('/')
def index():
  return render_template('home.html')

# Testing
# @main.route('/')
# def user():
#   return render_template('user.html')

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

@main.route('/review/<int:rider_id>', methods = ['GET','POST'])
@login_required
def review(rider_id):
    review_form = ReviewForm()
    rider = Rider.query.get(rider_id)
    reviews = Review.query.filter_by(rider_id = rider_id).all()
    if review_form.validate_on_submit():
        review = review_form.review.data
        new_review = Review(review=review, rider_id=rider_id, user_id=user_id)
        new_review.save_review()
        return redirect(url_for('.review',rider_id = rider_id ))
    return render_template('review.html',rider = rider, reviews=reviews, review_form=review_form)
