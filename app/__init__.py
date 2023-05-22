from flask import Flask
import sqlite3
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# from flask_migrate import Migrate
sql_conn = sqlite3.connect("app.db", check_same_thread=False)

sql_cursor = sql_conn.cursor()
sql_cursor.execute("SELECT * FROM user;")
tables = sql_cursor.fetchall()
print(tables)
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # database instance
migrate = Migrate(app, db) # migration engine instance
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
