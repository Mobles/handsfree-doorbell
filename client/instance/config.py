SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskapp.db'  # Sqlalchemy database connection info
SECRET_KEY = 'FWEJFWEF9WPFW8FI92JM3'  # Secret key used for flask cookies

WIFI_SSID = 'CatchAll Doorbell'
WIFI_PASSWORD = 'cAtchAll'

TESTING = False
#Do not edit below unless you're experienced with Python!
import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), '..', 'logs'))
LOG_PATH = os.path.join(location, 'catchall.log')