from flask import Blueprint, request
import jwt
import os
from . import db
from .models import Users, Room

movement = Blueprint('movement', __name__)
JWT_SECRET = os.environ.get("SECRET")
@movement.route('/', methods=['POST'])
def make_a_movement():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId)
    command = None
    command = request.get_json()["direction"]

    print(db.session.query(Room).filter_by(title = user['current_room']))
    # print(current_room)
    rooms = db.session.query(Room).all()

    print('\n\n', rooms, '\n\n')
    try:
        command = request.get_json()['direction']
    except:
        print('failed to get direction from post req')
        return 'failed to get direction from post request'
    if command:
        print(command)
    else:
        print('no command')
        return 'command not set'

    # Directional Interface
    if command == 'n':
        if current_room['north'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['north']
            user['current_room'] = moveTo

            controls = {
                user: user,
                room: user['current_room'],
                #inventory ? inventory : null
                #npc ? npc : null
                #mob ? mob : null
            }

            return controls

    elif command == 'e':
        if current_room['east'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['east']
            user['current_room'] = moveTo
            
            controls = {
                user: user,
                room: user['current_room'],
                #inventory ? inventory : null
                #npc ? npc : null
                #mob ? mob : null
            }

            return controls

    elif command == 's':
        if current_room['south'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['south']
            user['current_room'] = moveTo
            
            controls = {
                user: user,
                room: user['current_room'],
                #inventory ? inventory : null
                #npc ? npc : null
                #mob ? mob : null
            }

            return controls

    elif command == 'w':
        if current_room['west'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['west']
            user['current_room'] = moveTo
            
            controls = {
                user: user,
                room: user['current_room'],
                #inventory ? inventory : null
                #npc ? npc : null
                #mob ? mob : null
            }

            return controls