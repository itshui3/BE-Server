from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

from dotenv import load_dotenv

load_dotenv()

import os

db = SQLAlchemy()  # init orm for building tables/fields/constraints


def create_app():
    app = Flask(__name__)

<<<<<<< HEAD
    # DB Configs
    dburl = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = dburl
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
||||||| merged common ancestors
    dburl = os.environ.get('DATABASE_URL')

    app.config['SQLALCHEMY_DATABASE_URI'] = dburl
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

=======
    dburl = os.environ.get("DATABASE_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = dburl
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

>>>>>>> eef7fb5152b7f31cff64c073ef7413fa9cfee57c
    migrate = Migrate(app, db)
    db.init_app(app)

<<<<<<< HEAD
    # Route Registry
    from .public import public
    app.register_blueprint(public)
||||||| merged common ancestors
    from .public import public

    app.register_blueprint(public)
=======
    from .auth import auth

    app.register_blueprint(auth)
>>>>>>> eef7fb5152b7f31cff64c073ef7413fa9cfee57c

<<<<<<< HEAD
    playerPrefix = '/player'
    # player Routes
    from .routes.movement import movement
    app.register_blueprint(movement, url_prefix=playerPrefix + '/movement')

    return app
||||||| merged common ancestors
    return app
=======
    return app
>>>>>>> eef7fb5152b7f31cff64c073ef7413fa9cfee57c
