from __init__ import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    #password = db.Column(). Hi jimmy
    portrait = db.Column(db.String(1024))
    HP = db.Column(db.Integer)
    MP = db.Column(db.Integer)
    #items
    # current_room = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    #move
    attack = db.Column(db.Integer)
    #use_item
    #examine

    def __init__(self, username, password, portait, HP, MP, items, current_room, gold, move, attack, use_item, examine):
        self.name = name
        self.password = password
        self.portait = portait
        self.HP = HP
        self.MP = MP
        self.items = items
        self.current_room = current_room
        self.gold = gold
        self.move = move
        self.attack = attack
        self.use_item = use_item
        self.examine = examine

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    items = db.Column(db.String(1024))
    NPCs = db.Column(db.String(1024))
    def __init__(self, title, description, items, NPCs, north, east, south, west):
        self.title = title
        self.description = description
        self.items = items
        self.NPCs = NPCs
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    def __str__(self):
        return f'{self.title}, {self.description}, {self.items}, {self.NPCs}, {self.north}, {self.east}, {self.south}, {self.west}'

class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    items = db.Column(db.String(1024))
    gold = db.Column(db.Integer)
    HP = db.Column(db.Integer)
    isHostile = db.Column(db.Boolean)
    attack = db.Column(db.Integer)

    def __init__(self, name, description, items, gold, HP, isHostile, attack):
        self.name = name
        self.title = title
        self.description = description
        self.items = items
        self.gold = gold
        self.HP = HP
        self.isHostile = isHostile
        self.attack = attack

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    #view inventory
    #buy from
    #sell to

    def __init__(self, name, view_inventory, buy_from, sell_to):
        self.name = name
        self.view_inventory = view_inventory
        self.buy_from = buy_from
        self.sell_to = sell_to

class Item:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(1024))
    price = db.Column(db.Integer)
    action = db.Column(db.String(1024))
    resuseable = db.Column(db.Boolean)

    def __init__(self, title, description, price, action, reusable):
        self.title = title
        self.description = description
        self.price = price
        self.action = action
        self.resuseable = reusable