from flask import Blueprint, request
import jwt
import os
from . import db
from .models import Users, Room

merchant = Blueprint('merchant', __name__)
JWT_SECRET = os.environ.get("SECRET")
@merchant.route('/', methods=['POST'])
def make_a_merchant():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    command = None
    command = request.get_json()["direction"]


    print(f'user herrrrrrrre:{user.username}')

    return (user.current_room)