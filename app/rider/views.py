from . import rider
from flask import render_template,request,redirect,url_for
from app.rider import forms

@rider.route('/rder')
def rder():
    return 'hi kenya'
