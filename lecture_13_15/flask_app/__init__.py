import os
from flask import Flask
#from flask_app.config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
#app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)
app.config['SECRET_KEY'] = SECRET_KEY

from flask_app import routes
# @app.route('/') # Задаем ответ сервера при входе в корень сайта.
# def index():
#     return 'Hello, world!'
