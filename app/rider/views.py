from . import rider
from flask import render_template,request,redirect,url_for
from app.rider import forms

@rider.route('/rider')
def rider():
    return render_template('rider/rider.html')
