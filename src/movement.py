from flask import Blueprint, request
import jwt
import os
from . import db
from .models import Users, Room

movement = Blueprint('movement', __name__)
JWT_SECRET = os.environ.get("SECRET")
@movement.route('/', methods=['POST'])
def make_a_moose():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId)

    current_room = db.session.query(Room).filter_by(title = user['current_room'])


    command = None
    try: # Error handling # 1 : Handles cases of failing to get the json attribute from request body
            # ie. not sure what kind of error/ possibly server error
        command = request.get_json()['direction']
    except:
        print('failed to get direction from post req')
        return 'failed to get direction from post request'
    if command: # Error handling # 2 : Handles cases of command not being present
            # ie. client error, did not send proper request body
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
            return user

    elif command == 'e':
        if current_room['east'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['east']
            user['current_room'] = moveTo
            return user

    elif command == 's':
        if current_room['south'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['south']
            user['current_room'] = moveTo
            return user

    elif command == 'w':
        if current_room['west'] is None:
            return 'ya done goofed, no room here'
        else:
            moveTo = current_room['west']
            user['current_room'] = moveTo
            return user