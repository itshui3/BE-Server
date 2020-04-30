import re

def parse_inventory(parse_list):
    #seperate list by space (item) and - (qty)
    parsed_list = re.split(r'[-\s]', parse_list)
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
    return newList