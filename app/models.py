from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

# @login_manager.user_loader
# def load_user(user_id):
#   if session['account_type'] == 'User':
#       return User.query.get(int(user_id))
#   elif session['account_type'] == 'Rider':
#       return Rider.query.get(int(user_id))
#   else:
#       return None
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db. Column(db.String(255), index=True)
    email = db. Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    phone_number = db.Column(db.Integer, unique=True)
    location = db. Column(db.String(255))
    reviews = db.relationship('Review',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"User{self.username}"



class Rider(UserMixin, db.Model):
    __tablename__='riders'
    id = db.Column(db.Integer, primary_key=True)
    username = db. Column(db.String(255), index=True)
    email = db. Column(db.String(255), unique=True, index=True)
    password_secure = db.Column(db.String(255))
    phone_number = db.Column(db.Integer, unique=True)
    number_plate = db. Column(db.String(255), unique=True)
    location = db. Column(db.String(255))
    profile_pic_path = db. Column(db.String(255))
    reviews = db.relationship('Review',backref='rider',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f"Rider{self.username}"

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    rider_id = db.Column(db.Integer,db.ForeignKey('riders.id'))
    time = db.Column(db.DateTime, default=datetime.utcnow)


    def save_review(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Review:{self.review}'