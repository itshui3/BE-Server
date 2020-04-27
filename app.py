from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Entity
# username
# password
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    #password = db.Column(). Hi jimmy
    portrait = db.Column(db.String(1024))
    HP = db.Column(db.Integer)
    MP = db.Column(db.Integer)
    #items
    # current_room = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    #move
    attack = db.Column(db.Integer)
    #use_item
    #examine


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    items = db.Column(db.String(1024))
    NPCs = db.Column(db.String(1024))
    # north
    # east
    # south
    # west

class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    items = db.Column(db.String(1024))
    gold = db.Column(db.Integer)
    HP = db.Column(db.Integer)
    isHostile = db.Column(db.Boolean)
    attack = db.Column(db.Integer)

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #view inventory
    #buy from
    #sell to

class Item:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    price = db.Column(db.Integer)
    action = db.Column(db.String(1024))
    resuseable = db.Column(db.Boolean)


@app.route('/', methods=['GET'])
def get_index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)