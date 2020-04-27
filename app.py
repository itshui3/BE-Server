from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# I dunno what this is for

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:4214@localhost:5432/objectdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # init orm for building tables/fields/constraints
ma = Marshmallow(app) # init marshmallow

# User Entity
# username
# password
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    #password = db.Column(). Hi jimmy

    def __init__(self, username):
        self.username = username

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    # north
    # east
    # south
    # west
    def __init__(self, name):
        self.name = name

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/', methods=['GET'])
def get_index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)