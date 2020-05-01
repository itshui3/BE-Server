import re

def parse_inventory(parse_list):
    #seperate list by space (item) and - (qty)
    parsed_list = re.split(r'[-\s*]', parse_list)
    inventory = {}
    if len(parsed_list) > 1:
        for i in range(0, len(parsed_list), 2):
            item = parsed_list[i]
            qty = int(parsed_list[i+1])
            inventory.update({item:qty})
    else:
        print(parsed_list)
        # inventory.update(parsed_list)
    return inventory

def unparse_inventory(unparsed_dict):
    #combine inventory dict to string: 'item-qty item-qty'
    if len(unparsed_dict) == 0:
        return None
    newList = ""
    for item, qty in unparsed_dict.items():
        newList = newList + f'{item}-{qty} '
    newList = newList[:-1] #remove last space at end of string
    return newList

def map_inventory(items, inventory):
    # map item price and description to inventory
    inventory_details = []
    for item in items:
        for key, value in inventory.items():
            if key == item.name:
                # print(key, item.price)
                inventory_details.append(
                    {
                        f'{item.name}':{
                            "name":item.name,
                            "quantity":value,
                            "title": item.title,
                            "description": item.description,
                            "price": item.price,
                            "action": item.action,
                            "damage": item.damage,
                            "heal": item.heal,
                            "armor": item.armor
                        }
                    })
    return inventory_details

def find_price(item_to_check, items):
    price = 0
    for item in items:
        if item_to_check == item.name:
            price = item.price
    return price

def map_rooms(rooms):
    floor = []
    for room in rooms:
        floor.append({
            "title": room.title,
            "north": room.north,
            "south": room.south,
            "east": room.east,
            "west": room.west
        })
    return floor
