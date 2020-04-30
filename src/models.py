from flask_login import UserMixin

from . import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    character_name = db.Column(db.String(100))
    character_type = db.Column(db.String(100))
    portrait = db.Column(db.String(1024))
    HP = db.Column(db.Integer)
    MP = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    encounter_cd = db.Column(db.Integer)
    current_room = db.Column(db.String(20))
    items = db.Column(db.String(1024))
    #move
    #use_item
    #examine

    def __init__(self, username, password, character_name, character_type, portrait, HP, MP, attack, items=None, gold=500, encounter_cd=0, current_room="1-a1"):
        self.username = username
        self.password = password
        self.character_name = character_name
        self.character_type = character_type
        self.portrait = portrait
        self.HP = HP
        self.MP = MP
        self.current_room = current_room
        self.gold = gold
        self.attack = attack
        self.encounter_cd = encounter_cd
        self.items = items
        # self.move = move
        # self.use_item = use_item
        # self.examine = examine

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    floor = db.Column(db.String(20))
    items = db.Column(db.String(1024))
    NPCs = db.Column(db.String(1024))
    mobs = db.Column(db.String(1024))
    north = db.Column(db.String(20))
    east = db.Column(db.String(20))
    south = db.Column(db.String(20))
    west = db.Column(db.String(20))

    def __init__(self, title, description, floor, items, NPCs, mobs, north, east, south, west):
        self.title = title
        self.description = description
        self.floor = floor
        self.items = items
        self.NPCs = NPCs
        self.mobs = mobs
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    def __str__(self):
        return f'{self.title}, {self.description}, {self.floor}, {self.items}, {self.NPCs}, {self.north}, {self.east}, {self.south}, {self.west}'

class Npc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    ref = db.Column(db.String(64), unique=True) 
    description = db.Column(db.String(1024))
    items = db.Column(db.String(1024))
    gold = db.Column(db.Integer)
    HP = db.Column(db.Integer)
    isHostile = db.Column(db.Boolean)
    attack = db.Column(db.Integer)

    def __init__(self, name, ref, description, items, gold, HP, isHostile, attack):
        self.name = name
        self.ref = ref
        self.description = description
        self.items = items
        self.gold = gold
        self.HP = HP
        self.isHostile = isHostile
        self.attack = attack

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    inventory = db.Column(db.String(1024))
    gold = db.Column(db.Integer)
    HP = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    #view inventory
    #buy from
    #sell to

    def __init__(self, name, inventory, gold, HP, attack, view_inventory, buy_from, sell_to):
        self.name = name
        self.inventory = inventory
        self.gold = gold
        self.HP = HP
        self.attack = attack
        self.view_inventory = view_inventory
        self.buy_from = buy_from
        self.sell_to = sell_to

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    price = db.Column(db.Integer)
    action = db.Column(db.String(1024))
    damage = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    armor = db.Column(db.Integer)
    resuseable = db.Column(db.Boolean)
    
    def __init__(self, name, title, description, price, action, damage, heal, armor, reusable):
        self.name = name
        self.title = title
        self.description = description
        self.price = price
        self.action = action
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.resuseable = reusable
