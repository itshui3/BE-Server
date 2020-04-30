from flask import Blueprint, request
import jwt
import os
import re
from . import db
from .models import Users, Room, Merchant, Item

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

    inventoryList = re.split(r'[-\s]', merchant.inventory)

    inventory = {}
    for i in range(0, len(inventoryList), 2):
        item = inventoryList[i]
        qty = int(inventoryList[i+1])
        inventory.update({item:qty})

    print(f'\nmerchant inventory: {inventory}')

    newInventory = ""
    for item, qty in inventory.items():
        newInventory = newInventory + f'{item}-{qty} '

    print(f'newInventory: {newInventory}')

    print(f'\nitems: {items}')
    if command == 'peruse':
        
        peruse = {
        }

        return inventory

    elif command == 'buy':
        print(f'buying: {buy_item}')
        return "Buying item"
    else:
        return "Incorrect or unknown command"