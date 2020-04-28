from flask import Blueprint

movement = Blueprint('movement', __name__)

@movement.route('/', methods=['GET', 'POST'])
def make_a_moose():
    return 'hi'