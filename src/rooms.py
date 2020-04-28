from models import Room

from dungeon import floor_a, floor_b, floor_c, floor_d

#declare rooms
rooms = {}

#add floors to rooms
rooms.update(floor_a.make_floor(Room))
rooms.update(floor_b.make_floor(Room))
rooms.update(floor_c.make_floor(Room))
rooms.update(floor_d.make_floor(Room))

#link rooms together
rooms['a1'].east = rooms['a2'].title
# rooms['a2'].west = rooms['a1']  <--- if user wants to back track to previous room or use connect_backtrack
rooms['a2'].south = rooms['a3'].title
rooms['a3'].east = rooms['a4'].title
rooms['a4'].east = rooms['a5'].title

def connect_backtrack(rooms):
    for key, current_room in rooms.items():
        if current_room.north: #if there is a connection to next room at north
            next_room = current_room.north #get next room from current
            rooms[next_room].south = current_room.title #connect next room's opposite direction to current room
            print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.north} At: north")
            print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].south} At: south")

        if current_room.east: #if there is a connection to next room at east
            next_room = current_room.east #get next room from current
            rooms[next_room].west = current_room.title #connect next room's opposite direction to current room
            print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.east} At: east")
            print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].west} At: west")

        if current_room.south: #if there is a connection to next room at south
            next_room = current_room.south #get next room from current
            rooms[next_room].north = current_room.title #connect next room's opposite direction to current room
            print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.south} At: south")
            print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].north} At: north")

        if current_room.west: #if there is a connection to next room at west
            next_room = current_room.west #get next room from current
            rooms[next_room].east = current_room.title #connect next room's opposite direction to current room
            print(f"\nCurrent room: {current_room.title} goes forwards to {current_room.west} At: west")
            print(f"   Next room: {rooms[next_room].title} goes backward to {rooms[next_room].east} At: east")

connect_backtrack(rooms)

#test print next room connection
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

# print(rooms['a2'].east.title)

# test = floor_a.make_floor(Room)

# print(test)