from . import main

@main.route('/')
def index():
  return '<h1>Welcome to Ride Link where all your needs are catered for.<h1>'