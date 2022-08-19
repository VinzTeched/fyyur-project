import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SECRET_KEY = "fyyur"

# Disable FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database
database_name = "fyyur"
database_path = "postgresql://{}:{}@{}/{}".format(
    "postgres", "postgres", "localhost:5432", database_name
)

SQLALCHEMY_DATABASE_URI = database_path
