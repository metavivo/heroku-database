# This file, __init__, signals to python that all files in the directory should be treated
# as a single package. app.app_factory referes to app_factory.py in the directory app.
# This is the prefered format for publishing flask apps on Heroku.

# Import the buildApp function from app_factory
from app.app_factory import buildApp
flask_app = buildApp()
