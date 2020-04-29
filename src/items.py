from flask import Blueprint, request
import jwt
import os
from __init__ import db
from models import Item, Users, Room

#define items
items = {

#weapons    
'sword_truth': Item(
    title = "Sword of Truth",
    description = "Live or die by the truth",
    price = 50,
    action = "Slice",
    damage = 50,
    heal = 0,
    armor = 0,
    reusable = True
),

'sword_magic': Item(
    title = "Sword of Magic",
    description = "Magical sword gives +1 heal on every swing",
    price = 75,
    action = "Slice + Magic",
    damage = 75,
    heal = 1,
    armor = 0,
    reusable = True
),

'sword_destiny': Item(
    title = "Sword of Destiny",
    description = "Your destiny awaits... +2 heal on every swing",
    price = 100,
    action = "Slice + Magic",
    damage = 100,
    heal = 2,
    armor = 0,
    reusable = True
),

#special items
'green_potion': Item(
    title = "Green Potion",
    description = "A not so delicious concoction +50 heal (1 use)",
    price = 50,
    action = "Power",
    damage = 0,
    heal = 50,
    armor = 0,
    reusable = False
),

'red_potion': Item(
    title = "Red Potion",
    description = "Potion #9, beware who you drink this in front of... +60 heal (1 use)",
    price = 60,
    action = "Power",
    damage = 0,
    heal = 60,
    armor = 0,
    reusable = False
),

'white_potion': Item(
    title = "White Potion",
    description = "Pineapple and coconut, you're ready for the beach... +70 heal (1 use)",
    price = 70,
    action = "Power",
    damage = 0,
    heal = 70,
    armor = 0,
    reusable = False
),

'blue_potion': Item(
    title = "Blue Potion",
    description = "Adios to what ails ya... +80 heal (1 use)",
    price = 80,
    action = "Power",
    damage = 0,
    heal = 80,
    armor = 0,
    reusable = False
),

#armor
'helmet': Item(
    title = "Shiny helmet",
    description = "A gleaming helmet that blinds enemies from the glare +50 armor",
    price = 50,
    action = "Protects noggin",
    damage = 0,
    heal = 0,
    armor = 50,
    reusable = True
),

'chest_armor': Item(
    title = "Chest armor",
    description = "Protects your heart from any who look in +100 armor",
    price = 100,
    action = "Protects heart",
    damage = 0,
    heal = 0,
    armor = 100,
    reusable = True
),

'leg_armor': Item(
    title = "Leg armor",
    description = "Keeps your legs in one piece +25 armor",
    price = 25,
    action = "Protects legs",
    damage = 0,
    heal = 0,
    armor = 25,
    reusable = True
)
}

# print(items)


items = Blueprint('items', __name__)
JWT_SECRET = os.environ.get("SECRET")

@items.route('/', methods=['POST'])
def the_stuff():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId)
