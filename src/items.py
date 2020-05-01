from flask import Blueprint, request, jsonify
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
    item = request.get_json()["item"]
    
    print(f'\nCurrent room: {room.title} items:{room.items}\n')

    room_inv = {}
    if room.items:#check if there are items in room
        room_inv = parse_inventory(room.items)
    
    userItems = {}
    if user.items is not None: #parse user items if they are setup
        userItems = parse_inventory(user.items)
    
    if command == 'look':
        return room_inv

    if command == 'get':

        if item in room_inv:
            if room_inv[item] > 1:
                room_inv[item] -= 1
                room.items = unparse_inventory(room_inv)
                if item in userItems:
                    userItems[item] += 1
                else:
                    userItems.update({item: 1})
                user.items = unparse_inventory(userItems)

            else:
                if item in userItems:
                    userItems[item] += 1
                else:
                    userItems.update({item: 1})
                user.items = unparse_inventory(userItems)
                del room_inv[item]
                room.items = unparse_inventory(room_inv)
            
            db.session.commit()
            return userItems
        else:
            return jsonify({"error": "Item not found in room"})
    elif command == 'drop':
        if item in userItems:

            if item in room_inv: #check if item is inventory
                room_inv[item] += 1
                room.items = unparse_inventory(room_inv)
                if userItems[item] > 1:
                    userItems[item] -= 1
                else:
                    del userItems[item]
                user.items = unparse_inventory(userItems)
    
            else: #if item is not in room inventory
                room_inv.update({item: 1})
                room.items = unparse_inventory(room_inv)
                if userItems[item] > 1:
                    userItems[item] -= 1
                else:
                    del userItems[item]
                user.items = unparse_inventory(userItems)
            db.session.commit()
            return userItems

        else:
            return jsonify({"error": "Item not found in user inventory"})            

    else:
        return jsonify({"error": "Command invalid... check your spelling?"})

    return room_inv