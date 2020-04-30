from flask import Blueprint, request
import jwt
import os
from . import db
from .models import Users, Room, Merchant, Item
from .utils import parse_inventory, unparse_inventory

merchant = Blueprint('merchant', __name__)
JWT_SECRET = os.environ.get("SECRET")
@merchant.route('/', methods=['POST'])

def make_a_merchant():
    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    merchant = db.session.query(Merchant).first()
    items = db.session.query(Item).all()
    command = None
    command = request.get_json()["command"]
    buy_item = request.get_json()["buy_item"]

    inventory = parse_inventory(merchant.inventory)

    print(f'\nmerchant inventory: {inventory}')
    
    newInventory = unparse_inventory(inventory)

    print(f'newInventory: {newInventory}')

    print(f'\nitems: {items}')
    if command == 'peruse':

        return inventory

    elif command == 'buy':

        return "Buying item"
    else:
        return "Incorrect or unknown command"