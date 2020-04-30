from flask import Blueprint, request
import jwt
import os
from . import db
from .models import Users, Room, Item
from .utils import parse_inventory, unparse_inventory, map_inventory

items_blueprint = Blueprint('items', __name__)
JWT_SECRET = os.environ.get("SECRET")

@items_blueprint.route('/', methods=['POST'])
def the_stuff():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    room = db.session.query(Room).filter_by(title = user.current_room).first()
    items = db.session.query(Item).all()
    command = None
    command = request.get_json()["command"]
    
    print(f'\nCurrent room: {room.title} items:{room.items}\n')

    room_inv = {}
    if room.items is None: #check if there are items in room
        return 'There are no items in the room'
    else:
        room_inv = parse_inventory(room.items)
    
    userItems = {}
    if user.items is not None: #parse user items if they are setup
        userItems = parse_inventory(user.items)
    
    if command == 'get':
        print('getting')
        item = request.get_json()["item"]
        if item in room_inv:
            return 'Item found'
        else:
            return 'Item not found in room'
    else:
        return 'Command invalid... check your spelling?'

    return room_inv