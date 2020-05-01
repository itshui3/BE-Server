from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Npc, Merchant, Item
from .utils import map_rooms, parse_inventory

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


    if current_room.mobs is not None:
        # Need to return interface too
        print(current_room.mobs)
        return {"error": 'Monster present, deal with it before leaving the room!'}

    # Directional Interface
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
                "items": str(user.items),
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
            if newRoom.mobs is not None:
                mynpc = db.session.query(Npc).filter_by(id = newRoom.mobs).first()
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
                if randint(0, 2) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mob = monster_machine[spawnThis]
                    mob = Npc(
                        mob[0],
                        mob[1],
                        mob[2],
                        mob[3],
                        mob[4],
                        mob[5],
                        mob[6],
                        mob[7],
                    )
                    db.session.add(mob)
                    db.session.commit()
                    mob = db.session.query(Npc).all()[-1]

                    npc = {
                        "id": mob.id,
                        "name": mob.name,
                        "description": mob.description,
                        "items": mob.items,
                        "gold": mob.gold,
                        "HP": mob.HP,
                        "isHostile": mob.isHostile,
                        "attack": mob.attack
                    }
                    newRoom.mobs = npc["id"]
                    db.session.commit()

            message = {
                "message": [
                    f"You have been attacked by a monster"
                ]
            }

            controls = {
                "user": serialuser,
                "room": serialroom,
                "npc": npc,
                "map": floor_map,
                "combat": message
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
                "items": str(user.items),
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
            if newRoom.mobs is not None:
                mynpc = db.session.query(Npc).filter_by(id = newRoom.mobs).first()
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
                if randint(0, 2) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mob = monster_machine[spawnThis]
                    mob = Npc(
                        mob[0],
                        mob[1],
                        mob[2],
                        mob[3],
                        mob[4],
                        mob[5],
                        mob[6],
                        mob[7],
                    )
                    db.session.add(mob)
                    db.session.commit()
                    mob = db.session.query(Npc).all()[-1]

                    npc = {
                        "id": mob.id,
                        "name": mob.name,
                        "description": mob.description,
                        "items": mob.items,
                        "gold": mob.gold,
                        "HP": mob.HP,
                        "isHostile": mob.isHostile,
                        "attack": mob.attack
                    }
                    newRoom.mobs = npc["id"]
                    db.session.commit()

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
                "items": str(user.items),
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
            if newRoom.mobs is not None:
                mynpc = db.session.query(Npc).filter_by(id = newRoom.mobs).first()
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
                if randint(0, 2) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mob = monster_machine[spawnThis]
                    mob = Npc(
                        mob[0],
                        mob[1],
                        mob[2],
                        mob[3],
                        mob[4],
                        mob[5],
                        mob[6],
                        mob[7],
                    )
                    db.session.add(mob)
                    db.session.commit()
                    mob = db.session.query(Npc).all()[-1]

                    npc = {
                        "id": mob.id,
                        "name": mob.name,
                        "description": mob.description,
                        "items": mob.items,
                        "gold": mob.gold,
                        "HP": mob.HP,
                        "isHostile": mob.isHostile,
                        "attack": mob.attack
                    }
                    newRoom.mobs = npc["id"]
                    db.session.commit()

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
                "items": str(user.items),
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
            if newRoom.mobs is not None:
                mynpc = db.session.query(Npc).filter_by(id = newRoom.mobs).first()
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
                #Add comment to save
            else: #random spawn
                if randint(0, 2) == 0:
                    floor = newRoom.floor.split(' ')
                    monster_list = monster_catalogue["dungeon_1"][floor[1]].split(' ')
                    spawnThis = monster_list[randint(0, len(monster_list)-1)]
                    mob = monster_machine[spawnThis]
                    mob = Npc(
                        mob[0],
                        mob[1],
                        mob[2],
                        mob[3],
                        mob[4],
                        mob[5],
                        mob[6],
                        mob[7],
                    )
                    db.session.add(mob)
                    db.session.commit()
                    mob = db.session.query(Npc).all()[-1]

                    npc = {
                        "id": mob.id,
                        "name": mob.name,
                        "description": mob.description,
                        "items": mob.items,
                        "gold": mob.gold,
                        "HP": mob.HP,
                        "isHostile": mob.isHostile,
                        "attack": mob.attack
                    }
                    newRoom.mobs = npc["id"]
                    db.session.commit()

            controls = {
                "user": serialuser,
                "room": serialroom,
                "npc": npc,
                "map": floor_map
            }

            return controls