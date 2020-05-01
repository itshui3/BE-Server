from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Npc, Merchant, Item

from random import randint

combat = Blueprint('combat', __name__)
JWT_SECRET = os.environ.get("SECRET")
@combat.route('/', methods=['POST'])
def execute_combat_command():

    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    command = None
    command = request.get_json()["command"]

    current_room = db.session.query(Room).filter_by(title = user.current_room).first()

    if current_room.mobs is None:
        if command == 'run':
            print('\n\n', f"{user.character_name} started running around.", '\n\n')
        else:
            print('\n\n', f"{user.character_name} attempted attacking in a Room not occupied by a hostile.", '\n\n')
        error = {
            "error": 'No monster present.'
        }
        return error

    else:
        
        print('\n\n', "Starting attacking ["+str(current_room.NPCs)+"]", '\n\n')
        current_enemy = db.session.query(Npc).filter_by(id = current_room.mobs).first()

        if command == 'attack':
            # print('\n\n', current_enemy, '\n\n')
            # Take user's attack and subtract monster's hp by that amount
            current_enemy.HP -= user.attack

            # Take monster's attack and subtract user's hp by that amount
            user.HP -= current_enemy.attack
            db.session.commit()
            if current_enemy.HP <= 0:

                current_room.mobs = None # Check if this kills mob

                db.session.delete(current_enemy)
                db.session.commit()

            # Return interface
            cerealuser = {
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
            cerealmob = {
                "id": current_enemy.id,
                "name": current_enemy.name,
                "description": current_enemy.description,
                "items": current_enemy.items,
                "gold": current_enemy.gold,
                "HP": current_enemy.HP,
                "isHostile": current_enemy.isHostile,
                "attack": current_enemy.attack
            }
            cerealroom = {
                "id": current_room.id,
                "title": current_room.title,
                "description": current_room.description,
                "floor": current_room.floor,
                "items": current_room.items,
                "NPCs": current_room.NPCs,
                "mobs": current_room.mobs,
                "north": current_room.north,
                "east": current_room.east,
                "south": current_room.south,
                "west": current_room.west
            }
            message = [
                f"You attack a {current_enemy.name} and deal {user.attack} damage.", 
                f"{current_enemy.name} has {current_enemy.HP} health points remaining.",
                f"{current_enemy.name} attacks you dealing {current_enemy.attack} damage.",
                f"You have {user.HP} health points remaining."
            ]

            print(
                '\n\n', 
                f"{user.character_name} attacks a {current_enemy.name} and deals {user.attack} damage.\n{current_enemy.name} has {current_enemy.HP} health points remaining.", 
                '\n\n',
                f"{current_enemy.name} attacks {user.character_name} dealing {current_enemy.attack} damage.\n{user.character_name} has {user.HP} health points remaining."
            )
            if current_enemy.HP < 1:
                message.append(f"You have slain the {current_enemy.name}.")
            controls = {
                "user": cerealuser,
                "mob": cerealmob,
                "room": cerealroom,
                "combat": {
                    "message": message
                }
            }
            return controls

        elif command == 'run':
            # If monster type is special, cannot run
            # Otherwise, there is a chance that mob will disappear
            npc = db.session.query(Npc).filter_by(id = current_room.mobs).first()

            current_room.mobs = None
            db.session.delete(npc)
            db.session.commit()

            cerealuser = {
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
            cerealroom = {
                "id": current_room.id,
                "title": current_room.title,
                "description": current_room.description,
                "floor": current_room.floor,
                "items": current_room.items,
                "mobs": current_room.mobs,
                "NPCs": current_room.NPCs,
                "north": current_room.north,
                "east": current_room.east,
                "south": current_room.south,
                "west": current_room.west
            }

            message = {
                "message": [
                    "You ran away from the monster, good job."
                ]
            }

            fleeMsgs = [
                f"{user.character_name} fled from the scene of battle.",
                f"{user.character_name} demonstrated that cowardice is the solution with the highest chance for survival. 100%.",
                f"{user.character_name} ran.",
                f"{user.character_name} succumbed to excessive fear.",
                f"{user.character_name} exercised self-concern.",
                f"{user.character_name} demonstrated a severe lack of spine.",
                f"{user.character_name} got scurred.",
                f"{user.character_name} decided it just wasn't worth it in a game that doesn't yield exp for slain mobs."
            ]
            print('\n\n'+fleeMsgs[randint(0, len(fleeMsgs)-1)]+'\n\n')
            controls = {
                "user": cerealuser,
                # "npc": cerealmob,
                "room": cerealroom,
                "combat": message
            }
            return controls