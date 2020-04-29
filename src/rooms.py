from .models import Room

from .dungeon import floor_1, floor_2, floor_3, floor_4

from .items import items

#declare rooms
rooms = {}

#add floors to rooms
rooms = (floor_1.make_floor(Room))
rooms.update(floor_2.make_floor(Room))
rooms.update(floor_3.make_floor(Room))
rooms.update(floor_4.make_floor(Room))

#link rooms together
floor_1.link_rooms(rooms)
floor_2.link_rooms(rooms)
floor_3.link_rooms(rooms)
floor_4.link_rooms(rooms)

#This function checks all the rooms to ensure they are connected to the previous room
def connect_backtrack(rooms):
    for key, current_room in rooms.items():
        if current_room.north: #if there is a connection to next room at north
            next_room = current_room.north #get next room from current
            rooms[next_room].south = current_room.title #connect next room's opposite direction to current room
            # print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.north} At: north")
            # print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].south} At: south")

        if current_room.east: #if there is a connection to next room at east
            next_room = current_room.east #get next room from current
            rooms[next_room].west = current_room.title #connect next room's opposite direction to current room
            # print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.east} At: east")
            # print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].west} At: west")

        if current_room.south: #if there is a connection to next room at south
            next_room = current_room.south #get next room from current
            rooms[next_room].north = current_room.title #connect next room's opposite direction to current room
            # print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.south} At: south")
            # print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].north} At: north")

        if current_room.west: #if there is a connection to next room at west
            next_room = current_room.west #get next room from current
            rooms[next_room].east = current_room.title #connect next room's opposite direction to current room
            # print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.west} At: west")
            # print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].east} At: east")

connect_backtrack(rooms)

#This function prints all room connections
def print_connections(rooms):
    for key, room in rooms.items():
        if room.north:
            print(f"Room: {room.title} Connects to: {room.north} At: north")
        if room.east:
            print(f"Room: {room.title} Connects to: {room.east} At: east")
        if room.south:
            print(f"Room: {room.title} Connects to: {room.south} At: south")
        if room.west:
            print(f"Room: {room.title} Connects to: {room.west} At: west")

# print_connections(rooms)

#add items to rooms
rooms['1-a2'].items = {'sword_truth':(items['sword_truth'])}
rooms['1-b5'].items = {'green_potion':(items['green_potion'])}
rooms['1-e1'].items = {'helmet':(items['helmet'])}

rooms['2-b4'].items = {'red_potion':(items['red_potion'])}
rooms['2-c5'].items = {'sword_magic':(items['sword_magic'])}

rooms['3-a4'].items = {'white_potion':(items['white_potion'])}
rooms['3-b2'].items = {'chest_armor':(items['chest_armor'])}

rooms['4-c4'].items = {'blue_potion':(items['blue_potion'])}
rooms['4-b1'].items = {'sword_destiny':(items['sword_destiny'])}

#This function prints all items in rooms to check they exist
def print_all_items(rooms):
    for key, room in rooms.items():
        if room.items:
            for keyi, item in room.items.items():
                print(f'Room: {room.title} contains: {item.title}')

# print_all_items(rooms)

# print(rooms)