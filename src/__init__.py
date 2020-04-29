from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_cors import CORS

from dotenv import load_dotenv

load_dotenv()

import os

import pusher

PUSHER_ID = os.environ.get("PUSHER_ID")
PUSHER_KEY = os.environ.get("PUSHER_KEY")
PUSHER_SECRET = os.environ.get("PUSHER_SECRET")

pusher_client = pusher.Pusher(
    app_id=PUSHER_ID, key=PUSHER_KEY, secret=PUSHER_SECRET, cluster="us2", ssl=True
)

db = SQLAlchemy()  # init orm for building tables/fields/constraints

CORS_ORIGIN = os.environ.get("CORS_ORIGIN")


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": CORS_ORIGIN}})

    dburl = os.environ.get("DATABASE_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = dburl
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    migrate = Migrate(app, db)
    db.init_app(app)

    # Route Registry
    # from .public import public
    # app.register_blueprint(public)

    # Auth Routes
    from .auth import auth

    app.register_blueprint(auth)

    playerPrefix = "/player"
    # player Routes
    from .movement import movement

    app.register_blueprint(movement, url_prefix=playerPrefix + "/movement")

    from .items import items_blueprint

    app.register_blueprint(items_blueprint, url_prefix=playerPrefix + "/items")

    return app
