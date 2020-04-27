from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from dotenv import load_dotenv
load_dotenv()

import os

db = SQLAlchemy() # init orm for building tables/fields/constraints

def create_app():
    app = Flask(__name__)

    dburl = os.environ.get('DATABASE_URL')

    app.config['SQLALCHEMY_DATABASE_URI'] = dburl
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    migrate = Migrate(app, db)

    db.init_app(app)

    from .public import public

    app.register_blueprint(public)

    return app