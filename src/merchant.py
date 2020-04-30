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

    print(f'Db merchant inventory {merchant.inventory}')

    inventory = parse_inventory(merchant.inventory)

    print(f'\nmerchant inventory: {inventory}')

    print(f'\nitems: {items}')
    if command == 'peruse':

        return inventory

    elif command == 'buy':

        if buy_item is None:
            return 'buy_item is not specified'
        elif buy_item in inventory:

            if inventory[buy_item] < 1:
                return "Item is out of stock"
            else:
                print(items[buy_item].price)
                inventory[buy_item] -= 1
                newInv = unparse_inventory(inventory)
                merchant.inventory = str(newInv)
                # db.session.commit()
                return inventory
        else:
            return 'Item is not in inventory'

    else:
        return "Incorrect or unknown command"