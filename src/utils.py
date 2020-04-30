import re

def parse_inventory(parse_list):
    #seperate list by space (item) and - (qty)
    parsed_list = re.split(r'[-\s*]', parse_list)
    inventory = {}
    for i in range(0, len(parsed_list), 2):
        item = parsed_list[i]
        qty = int(parsed_list[i+1])
        inventory.update({item:qty})
    return inventory

def unparse_inventory(uparsed_dict):
    #combine inventory dict to string: 'item-qty item-qty'
    newList = ""
    for item, qty in uparsed_dict.items():
        newList = newList + f'{item}-{qty} '
    newList = newList[:-1] #remove last space at end of string
    return newList

def map_inventory(items, inventory):
# map item price and description to inventory
    inventory_details = []
    for item in items:
        for key, value in inventory.items():
            if key == item.name:
                print(key, item.price)
                inventory_details.append({"name": item.name, "quantity":value, "title": item.title, "description": item.description, "price": item.price, "action": item.action, "damage": item.damage, "heal": item.heal, "armor": item.armor,})
    return inventory_details