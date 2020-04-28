from flask import Blueprint, request

movement = Blueprint('movement', __name__)

@movement.route('/', methods=['GET', 'POST'])
def make_a_moose():
    if request.method == 'POST':
        # Grab player record
        # Use it to determine current occupied room
        # Determine direction player needs to move based on POST req
        # Use current occupied room's direction attribute to determine which room player needs to be in to fulfil the movement req
        # Send back info that FE needs to describe a new character state
        command = request.get_json()
        print(command)

    return 'hi'