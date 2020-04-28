from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

from dotenv import load_dotenv

load_dotenv()

import os

db = SQLAlchemy()  # init orm for building tables/fields/constraints


def create_app():
    app = Flask(__name__)

    dburl = os.environ.get("DATABASE_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = dburl
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    migrate = Migrate(app, db)

    db.init_app(app)

    from .auth import auth

    app.register_blueprint(auth)

    return app
