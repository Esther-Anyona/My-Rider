from . import main

@main.route('/')
def index():
  return '<h1>Welcome to Ride Link<h1>'