from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Merchant, Item
from .utils import parse_inventory, unparse_inventory, map_inventory, find_price

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

    inventory = parse_inventory(merchant.inventory)
    inventory_details = map_inventory(items, inventory)
    userItems = {}
    if user.items is not None:
        userItems = parse_inventory(user.items)

    # print(f'\nmerchant inventory: {inventory}')
    # print(f'\ndetails: {inventory_details}')

    if command == 'peruse':

        return jsonify(inventory_details)

    elif command == 'buy':
        buy_item = request.get_json()["buy_item"]
        if buy_item is None:
            return jsonify({"error":'buy_item is not specified'})

        elif buy_item in inventory:
            if inventory[buy_item] < 1:
                return jsonify({"error":"Item is out of stock"})
            else:
                price = find_price(buy_item, items)
                print(f'Price found: {price}')
                inventory[buy_item] -= 1
                updateInv = unparse_inventory(inventory)
                merchant.inventory = str(updateInv)

                if price > user.gold:
                    return jsonify({"error":"You do not have enough gold to purchase"})
                else: #if user has enough gold
                    user.gold = user.gold - price

                    if user.items: #check if user has items

                        if buy_item in userItems: #check if item is already in user items
                            userItems[buy_item] += 1

                        else: #if user doesn't already have item, add
                            userItems.update({buy_item: 1})
                        user.items = unparse_inventory(userItems) #unparse user items into string

                    else: #if user doesn't have items, create item&qty
                        userItems = {buy_item: 1}
                        user.items = f'{buy_item}-1'

                    db.session.commit()
                    userItems.update({"gold": user.gold, "items": user.items})
                    return userItems

        else:
            return jsonify({"error":'Item is not in inventory'})
    elif command == 'sell':
        sell_item = request.get_json()["sell_item"]
        if sell_item is None: #check if sell_item exists
            return jsonify({"error":"sell_item not specified"})
        else: #if sell_item exists
            if sell_item in userItems:
                print(f'Qty in user items: {userItems[sell_item]}')
                if userItems[sell_item] > 1: #check item qty in user inventory
                    userItems[sell_item] -= 1
                    updateItems = unparse_inventory(userItems)
                    user.items = str(updateItems)
                    #add item to merchant inventory
                    if sell_item in inventory:
                        inventory[sell_item] += 1
                        merchant.inventory = unparse_inventory(inventory)
                        price = find_price(sell_item, items)
                        user.gold += (price - 10)
                    db.session.commit()
                    userItems.update({"gold": user.gold, "items": user.items})
                    return userItems

                elif userItems[sell_item] == 1: #check if user inventory is last one
                    print('deleting')
                    del userItems[sell_item]
                    if userItems:#check if there are user items left
                        updateItems = unparse_inventory(userItems)
                        user.items = str(updateItems)
                        inventory[sell_item] += 1
                        merchant.inventory = unparse_inventory(inventory)
                        price = find_price(sell_item, items)
                        user.gold += (price - 10)
                        db.session.commit()
                        userItems.update({"gold": user.gold, "items": user.items})
                        return userItems
                    else:
                        inventory[sell_item] += 1
                        merchant.inventory = unparse_inventory(inventory)
                        price = find_price(sell_item, items)
                        user.gold += (price - 10)
                        user.items = None
                        db.session.commit()
                        userItems.update({"gold": user.gold, "items": user.items})
                        return userItems
                # return userItems
            else:
                return jsonify({"error":'Item is not in user items'})
        
        # return "Sell stuff"
    else:
        return jsonify({"error":"Incorrect or unknown command"})