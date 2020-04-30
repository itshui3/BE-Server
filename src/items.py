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
    if room.items is None: #check if there are items in room
        return jsonify({"error":'There are no items in the room'})
    else:
        room_inv = parse_inventory(room.items)
    
    userItems = {}
    if user.items is not None: #parse user items if they are setup
        userItems = parse_inventory(user.items)
    
    if command == 'get':

        if item in room_inv:
            if room_inv[item] > 1:
                room_inv[item] -= 1
                room.items = unparse_inventory(room_inv)
                userItems.update(room_inv[item])
            else:
                new_item = {item: 1}
                userItems.update(new_item)
                user.items = unparse_inventory(userItems)
                del room_inv[item]
                print(f'\nRoom items after get: {room_inv}-length: {len(room_inv)}\n')
                if len(room_inv) == 0:
                    print('no items left')
                    room.items = None
                else:
                    print('some items left')
                    room.items = unparse_inventory(room_inv)
                
            db.session.commit()
            return userItems
        else:
            return jsonify({"error": "Item not found in room"})
    elif command == 'drop':
        if item in userItems:
            if room_inv[item] > 1:
                room_inv[item] += 1
                room.items = unparse_inventory(room_inv)
                #remove item from user inventory
                del userItems[item]
                user.items = unparse_inventory(userItems)
            
            else: #if room inventory is none
                new_item = {item: 1}
                room_inv.update(new_item)
                room_inv.items = unparse_inventory(room_inv)
                del userItems[item]
                user.items = unparse_inventory(userItems)
            # db.session.commit()
            return userItems

                

        else:
            return jsonify({"error": "Item not found in user inventory"})
            

    else:
        return jsonify({"error": "Command invalid... check your spelling?"})

    return room_inv