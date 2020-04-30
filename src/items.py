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
    user = db.session.query(Users).filter_by(id = userId)
    room = db.session.query(Room).filter_by(title = user.current_room).first()

    print(f'Current room')
