import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
# 'postgresql://jackfros:kAZt3AnRHa7S0dPpZw7zEXdSoeQPZg1Qh@dpg-cgb0ppt269v4icoivk4g-a:5432/fyyur_app_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
