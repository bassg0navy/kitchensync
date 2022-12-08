from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, flash, redirect, url_for, abort
from flask_login import (LoginManager, login_user, logout_user, current_user, login_required)
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
bootstrap = Bootstrap5(app)
bcrypt = Bcrypt()


# MongoDB
client = MongoClient('host.docker.internal', 27017)
db = client['imagePantry']

# Login Manager #
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login'
login_manager.login_message_category = 'info'

from ImagePantry import routes, forms, models