from flask import Blueprint, request
import jwt
import os
# from somewhere import User
# from somewhere import Room
# from .models import Users
from . import db
from .models import Users

movement = Blueprint('movement', __name__)
JWT_SECRET = os.environ.get("SECRET")
@movement.route('/', methods=['GET', 'POST'])
def make_a_moose():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId)

    # position = user['position'] - a user's position will have the same string literal as a room's title


    if request.method == 'POST':
        # Grab player record with player Id

        # Use it to determine current occupied room
        # Determine direction player needs to move based on POST req
        # Use current occupied room's direction attribute to determine which room player needs to be in to fulfil the movement req
        # Send back info that FE needs to describe a new character state

        command = None
        try: # Error handling # 1 : Handles cases of failing to get the json attribute from request body
                # ie. not sure what kind of error/ possibly server error
            command = request.get_json()['direction']
        except:
            print('failed to get direction from post req')
        
        if command: # Error handling # 2 : Handles cases of command not being present
                # ie. client error, did not send proper request body
            print(command)
        else:
            print('no command')

    return 'hi'