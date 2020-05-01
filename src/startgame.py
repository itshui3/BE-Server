from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Npc
from .utils import map_rooms

startgame = Blueprint('startgame', __name__)
JWT_SECRET = os.environ.get("SECRET")
@startgame.route('/', methods=['GET'])
def get_character_info():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    room = db.session.query(Room).filter_by(title = user.current_room).first()
    floor = db.session.query(Room).filter_by(floor = room.floor).all()
    floor_map = map_rooms(floor)

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
        "items": user.items,
        "gold": user.gold,
        "encounter_cd": user.encounter_cd,
        "current_room": user.current_room
    }

    serialroom = {
        "id": room.id,
        "title": room.title,
        "description": room.description,
        "floor": room.floor,
        "items": room.items,
        "NPCs": room.NPCs,
        "mobs": room.mobs,
        "north": room.north,
        "east": room.east,
        "south": room.south,
        "west": room.west
    }
    cerealmob = None
    if room.mobs is not None:
        npc = db.session.query(Npc).filter_by(id = room.mobs).first()
        cerealmob = {
            "id": npc.id,
            "name": npc.name,
            "description": npc.description,
            "items": npc.items,
            "gold": npc.gold,
            "HP": npc.HP,
            "isHostile": npc.isHostile,
            "attack": npc.attack
        }

    controls = {
        "user": cerealuser,
        "room": serialroom,
        "map": floor_map,
        "npc": cerealmob
    }

    return controls