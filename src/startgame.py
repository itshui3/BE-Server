from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users

startgame = Blueprint('startgame', __name__)
JWT_SECRET = os.environ.get("SECRET")
@startgame.route('/', methods=['GET'])
def get_character_info():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()

    cerealuser = {
        "id": user.id,
        "username": user.username,
        "password": user.password,
        "character_name": user.character_name,
        "character_type": user.character_type,
        "portrait": user.portrait,
        "HP": user.HP,
        "MP": user.MP,
        "attack": user.attack,
        "gold": user.gold,
        "encounter_cd": user.encounter_cd,
        "current_room": user.current_room
    }

    return cerealuser