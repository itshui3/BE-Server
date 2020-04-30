from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Merchant, Item
from .utils import parse_inventory, unparse_inventory, map_inventory

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

    # print(f'Db merchant inventory {merchant.inventory}')
    inventory = parse_inventory(merchant.inventory)

    print(f'\nmerchant inventory: {inventory}')
    inventory_details = map_inventory(items, inventory)
    # print(f'\ndetails: {inventory_details}')

    if command == 'peruse':

        return jsonify(inventory_details)

    elif command == 'buy':

        if buy_item is None:
            return 'buy_item is not specified'
        elif buy_item in inventory:

            if inventory[buy_item] < 1:
                return "Item is out of stock"
            else:
                price = 0
                for item in items:
                    if buy_item == item.name:
                        price = item.price
                # print(f'Price: {price}')
                inventory[buy_item] -= 1
                newInv = unparse_inventory(inventory)
                merchant.inventory = str(newInv)
                user.gold = user.gold - price
                # print(f'Gold: {user.gold}')
                # print(user.items)
                userItems = {}
                if user.items: #check if user has items
                    userItems = parse_inventory(user.items) #parse user items into dict
                    if buy_item in userItems: #check if item is already in user items
                        userItems[buy_item] += 1
                    else: #if user doesn't already have item, add
                        userItems.update({buy_item: 1})
                    user.items = unparse_inventory(userItems) #unparse user items into string
                else: #if user doesn't have items, create item&qty
                    userItems = {buy_item: 1}
                    user.items = f'{buy_item}-1'
                db.session.commit()
                userItems.update({"gold": user.gold})
                return userItems
        else:
            return 'Item is not in inventory'

    else:
        return "Incorrect or unknown command"