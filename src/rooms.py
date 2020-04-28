from models import Room

from dungeon import floor_1, floor_2, floor_3, floor_4

#declare rooms
rooms = {}

#add floors to rooms
rooms = (floor_1.make_floor(Room))
rooms.update(floor_2.make_floor(Room))
rooms.update(floor_3.make_floor(Room))
rooms.update(floor_4.make_floor(Room))

#link rooms together
rooms['1-a1'].east = rooms['1-a2'].title
# rooms['1-a2'].west = rooms['1-a1']  <--- if user wants to back track to previous room or use connect_backtrack
rooms['1-a2'].south = rooms['1-a3'].title
rooms['1-a3'].east = rooms['1-a4'].title
rooms['1-a4'].east = rooms['1-a5'].title

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

# print(rooms)

# current = 0
# for room in rooms.items():
#     current += 1
#     print(current, room)