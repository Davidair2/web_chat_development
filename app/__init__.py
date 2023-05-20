from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_manager, LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # database instance
migrate = Migrate(app, db) # migration engine instance
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models