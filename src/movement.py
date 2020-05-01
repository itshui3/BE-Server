from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Npc, Merchant, Item
from .utils import map_rooms

from .monster_catalogue import monster_catalogue, monster_machine
from random import randint

movement = Blueprint('movement', __name__)
JWT_SECRET = os.environ.get("SECRET")
@movement.route('/', methods=['POST'])
def make_a_movement():
    
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    room = db.session.query(Room).filter_by(title = user.current_room).first()

    direction = None
    direction = request.get_json()["direction"]

    current_room = None
    try:
        current_room = db.session.query(Room).filter_by(title = user.current_room).first()
    except:
        print('could not access current_room properly')
        return {"error": 'something went wrong with accessing current_room'}


    if current_room.NPCs is not None:
        print(current_room.NPCs)
        return {"error": 'monster present, deal with it before leaving the room'}

    # Directional Interface: Checks direction in post and performs request
    if direction == 'n':
        if current_room.north is None:
            return {"error": 'No room in this direction'}
        else:
            moveTo = current_room.north
            print(f'\nmoveTo: {moveTo}\n')
            user.current_room = moveTo
            db.session.commit()

            room = user.current_room
            newRoom = db.session.query(Room).filter_by(title = room).first()
            floor = db.session.query(Room).filter_by(floor = newRoom.floor).all()
            floor_map = map_rooms(floor)

            serialuser = {
                "id": int(user.id),
                "username": str(user.username),
                "character_name": str(user.character_name),
                "character_type": str(user.character_type),
                "portrait": str(user.portrait),
                "HP": int(user.HP),
                "MP": int(user.MP),
                "attack": int(user.attack),
                "gold": int(user.gold),
                "encounter_cd": int(user.encounter_cd),
                "current_room": str(user.current_room)
            }

            serialroom = {
                "id": newRoom.id,
                "title": newRoom.title,
                "description": newRoom.description,
                "floor": newRoom.floor,
                "items": newRoom.items,
                "NPCs": newRoom.NPCs,
                "mobs": newRoom.mobs,
                "north": newRoom.north,
                "east": newRoom.east,
                "south": newRoom.south,
                "west": newRoom.west
            }

            npc = None
            if newRoom.NPCs is not None:
                mynpc = db.session.query(Npc).filter_by(ref = newRoom.NPCs).first()
                npc = {
                    "id": mynpc.id,
                    "name": mynpc.name,
                    "description": mynpc.description,
                    "items": mynpc.items,
                    "gold": mynpc.gold,
                    "HP": mynpc.HP,
                    "isHostile": mynpc.isHostile,
                    "attack": mynpc.attack
                }
            else: #random spawn
                if randint(0, 10) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mynpc = db.session.query(Npc).filter_by(ref = spawnThis).first()
                    npc = {
                        "id": mynpc.id,
                        "name": mynpc.name,
                        "description": mynpc.description,
                        "items": mynpc.items,
                        "gold": mynpc.gold,
                        "HP": mynpc.HP,
                        "isHostile": mynpc.isHostile,
                        "attack": mynpc.attack
                    }
                    newRoom.NPCs = spawnThis
                    db.session.commit()

            controls = {
                "user": serialuser,
                "room": serialroom,
                "npc": npc,
                "map": floor_map
            }

            return controls

    elif direction == 'e':
        if current_room.east is None:
            return {"error": 'No room in this direction'}
        else:
            moveTo = current_room.east
            print(f'\nmoveTo: {moveTo}\n')
            user.current_room = moveTo
            db.session.commit()

            room = user.current_room
            newRoom = db.session.query(Room).filter_by(title = room).first()
            floor = db.session.query(Room).filter_by(floor = newRoom.floor).all()
            floor_map = map_rooms(floor)

            serialuser = {
                "id": int(user.id),
                "username": str(user.username),
                "character_name": str(user.character_name),
                "character_type": str(user.character_type),
                "portrait": str(user.portrait),
                "HP": int(user.HP),
                "MP": int(user.MP),
                "attack": int(user.attack),
                "gold": int(user.gold),
                "encounter_cd": int(user.encounter_cd),
                "current_room": str(user.current_room)
            }

            serialroom = {
                "id": newRoom.id,
                "title": newRoom.title,
                "description": newRoom.description,
                "floor": newRoom.floor,
                "items": newRoom.items,
                "NPCs": newRoom.NPCs,
                "mobs": newRoom.mobs,
                "north": newRoom.north,
                "east": newRoom.east,
                "south": newRoom.south,
                "west": newRoom.west
            }

            npc = None
            if newRoom.NPCs is not None:
                mynpc = db.session.query(Npc).filter_by(ref = newRoom.NPCs).first()
                npc = {
                    "id": mynpc.id,
                    "name": mynpc.name,
                    "description": mynpc.description,
                    "items": mynpc.items,
                    "gold": mynpc.gold,
                    "HP": mynpc.HP,
                    "isHostile": mynpc.isHostile,
                    "attack": mynpc.attack
                }
            else: #random spawn
                if randint(0, 10) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mynpc = db.session.query(Npc).filter_by(ref = spawnThis).first()
                    npc = {
                        "id": mynpc.id,
                        "name": mynpc.name,
                        "description": mynpc.description,
                        "items": mynpc.items,
                        "gold": mynpc.gold,
                        "HP": mynpc.HP,
                        "isHostile": mynpc.isHostile,
                        "attack": mynpc.attack
                    }
                    newRoom.NPCs = spawnThis
                    db.session.commit()
                    print('randomly spawned mob', npc)

            controls = {
                "user": serialuser,
                "room": serialroom,
                "npc": npc,
                "map": floor_map
            }

            return controls

    elif direction == 's':
        if current_room.south is None:
            return {"error": 'No room in this direction'}
        else:
            moveTo = current_room.south
            print(f'\nmoveTo: {moveTo}\n')
            user.current_room = moveTo
            db.session.commit()

            room = user.current_room
            newRoom = db.session.query(Room).filter_by(title = room).first()
            floor = db.session.query(Room).filter_by(floor = newRoom.floor).all()
            floor_map = map_rooms(floor)
            
            serialuser = {
                "id": int(user.id),
                "username": str(user.username),
                "character_name": str(user.character_name),
                "character_type": str(user.character_type),
                "portrait": str(user.portrait),
                "HP": int(user.HP),
                "MP": int(user.MP),
                "attack": int(user.attack),
                "gold": int(user.gold),
                "encounter_cd": int(user.encounter_cd),
                "current_room": str(user.current_room)
            }

            serialroom = {
                "id": newRoom.id,
                "title": newRoom.title,
                "description": newRoom.description,
                "floor": newRoom.floor,
                "items": newRoom.items,
                "NPCs": newRoom.NPCs,
                "mobs": newRoom.mobs,
                "north": newRoom.north,
                "east": newRoom.east,
                "south": newRoom.south,
                "west": newRoom.west
            }
            npc = None
            if newRoom.NPCs is not None:
                mynpc = db.session.query(Npc).filter_by(ref = newRoom.NPCs).first()
                npc = {
                    "id": mynpc.id,
                    "name": mynpc.name,
                    "description": mynpc.description,
                    "items": mynpc.items,
                    "gold": mynpc.gold,
                    "HP": mynpc.HP,
                    "isHostile": mynpc.isHostile,
                    "attack": mynpc.attack
                }
            else: #random spawn
                if randint(0, 10) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mynpc = db.session.query(Npc).filter_by(ref = spawnThis).first()
                    npc = {
                        "id": mynpc.id,
                        "name": mynpc.name,
                        "description": mynpc.description,
                        "items": mynpc.items,
                        "gold": mynpc.gold,
                        "HP": mynpc.HP,
                        "isHostile": mynpc.isHostile,
                        "attack": mynpc.attack
                    }
                    newRoom.NPCs = spawnThis
                    db.session.commit()
                    print('randomly spawned mob', npc)

            controls = {
                "user": serialuser,
                "room": serialroom,
                "npc": npc,
                "map": floor_map
            }

            return controls

    elif direction == 'w':
        if current_room.west is None:
            return {"error": 'No room in this direction'}
        else:
            moveTo = current_room.west
            print(f'\nmoveTo: {moveTo}\n')
            user.current_room = moveTo
            db.session.commit()

            room = user.current_room
            newRoom = db.session.query(Room).filter_by(title = room).first()
            floor = db.session.query(Room).filter_by(floor = newRoom.floor).all()
            floor_map = map_rooms(floor)
            
            serialuser = {
                "id": int(user.id),
                "username": str(user.username),
                "character_name": str(user.character_name),
                "character_type": str(user.character_type),
                "portrait": str(user.portrait),
                "HP": int(user.HP),
                "MP": int(user.MP),
                "attack": int(user.attack),
                "gold": int(user.gold),
                "encounter_cd": int(user.encounter_cd),
                "current_room": str(user.current_room)
            }

            serialroom = {
                "id": newRoom.id,
                "title": newRoom.title,
                "description": newRoom.description,
                "floor": newRoom.floor,
                "items": newRoom.items,
                "NPCs": newRoom.NPCs,
                "mobs": newRoom.mobs,
                "north": newRoom.north,
                "east": newRoom.east,
                "south": newRoom.south,
                "west": newRoom.west
            }

            npc = None
            if newRoom.NPCs is not None:
                mynpc = db.session.query(Npc).filter_by(ref = newRoom.NPCs).first()
                npc = {
                    "id": mynpc.id,
                    "name": mynpc.name,
                    "description": mynpc.description,
                    "items": mynpc.items,
                    "gold": mynpc.gold,
                    "HP": mynpc.HP,
                    "isHostile": mynpc.isHostile,
                    "attack": mynpc.attack
                }
            else: #random spawn
                if randint(0, 10) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mynpc = db.session.query(Npc).filter_by(ref = spawnThis).first()
                    npc = {
                        "id": mynpc.id,
                        "name": mynpc.name,
                        "description": mynpc.description,
                        "items": mynpc.items,
                        "gold": mynpc.gold,
                        "HP": mynpc.HP,
                        "isHostile": mynpc.isHostile,
                        "attack": mynpc.attack
                    }
                    print('randomly spawned mob', npc)
                    newRoom.NPCs = spawnThis
                    db.session.commit()

            controls = {
                "user": serialuser,
                "room": serialroom,
                "npc": npc,
                "map": floor_map
            }

            return controls