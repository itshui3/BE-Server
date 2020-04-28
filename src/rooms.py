from models import Room

# from dungeon.floor1.a import a1, a2

def make_room(Room, title, description, floor):
    return Room(
        title = title,
        description = description,
        floor = floor,
        items = {},
        NPCs = {},
        north = None,
        east = None,
        south = None,
        west = None
    )

#declare rooms
rooms = {
#room_key: make_room(Room, title, description, floor)
    'a1': make_room(Room, 'a1', 'This is the beginning', 'Floor A'),
    'a2': make_room(Room, 'a2', 'Another room', 'Floor A'),
    'a3': make_room(Room, 'a3', 'Third times the charm', 'Floor A'),
    'a4': make_room(Room, 'a4', 'Forth times the charm', 'Floor A'),
    'a5': make_room(Room, 'a5', 'Fifth times the charm', 'Floor A'),

    'b1': make_room(Room, 'b1', 'Its a B room', 'Floor A'),
    'b2': make_room(Room, 'b2', 'Its a B room', 'Floor A'),
    'b3': make_room(Room, 'b3', 'Its a B room', 'Floor A'),
    'b4': make_room(Room, 'b4', 'Its a B room', 'Floor A'),
    'b5': make_room(Room, 'b5', 'Its a B room', 'Floor A'),

    'c1': make_room(Room, 'c1', 'Its a c room', 'Floor A'),
    'c2': make_room(Room, 'c2', 'Its a c room', 'Floor A'),
    'c3': make_room(Room, 'c3', 'Its a c room', 'Floor A'),
    'c4': make_room(Room, 'c4', 'Its a c room', 'Floor A'),
    'c5': make_room(Room, 'c5', 'Its a c room', 'Floor A'),

    'd1': make_room(Room, 'd1', 'Its a d room', 'Floor A'),
    'd2': make_room(Room, 'd2', 'Its a d room', 'Floor A'),
    'd3': make_room(Room, 'd3', 'Its a d room', 'Floor A'),
    'd4': make_room(Room, 'd4', 'Its a d room', 'Floor A'),
    'd5': make_room(Room, 'd5', 'Its a d room', 'Floor A'),

    'e1': make_room(Room, 'e1', 'Its a e room', 'Floor A'),
    'e2': make_room(Room, 'e2', 'Its a e room', 'Floor A'),
    'e3': make_room(Room, 'e3', 'Its a e room', 'Floor A'),
    'e4': make_room(Room, 'e4', 'Its a e room', 'Floor A'),
    'e5': make_room(Room, 'e5', 'Its a e room', 'Floor A'),

}

#link rooms together
rooms['a1'].east = rooms['a2'].title
# rooms['a2'].west = rooms['a1']  <--- if user wants to back track to previous room
rooms['a2'].east = rooms['a3']
rooms['a3'].east = rooms['a4']
rooms['a4'].east = rooms['a5']

def connect_backtrack(rooms):
    for key, room in rooms.items():
        if room.north:
            next_room = rooms[key].north.title
            rooms[next_room].south = rooms[key]
            print(f"Back track room: {rooms[next_room].title} To: {room.title} At: south")
        if room.east:
            next_room = rooms[key].east.title
            rooms[next_room].west = rooms[key]
            print(f"Back track room: {rooms[next_room].title} To: {room.title} At: west")
        if room.south:
            next_room = rooms[key].south.title
            rooms[next_room].north = rooms[key]
            print(f"Back track room: {rooms[next_room].title} To: {room.title} At: north")
        if room.west:
            next_room = rooms[key].west.title
            rooms[next_room].east = rooms[key]
            print(f"Back track room: {rooms[next_room].title} To: {room.title} At: east")

connect_backtrack(rooms)

#test print next room connection
def print_connections(rooms):
    for key, room in rooms.items():
        if room.north:
            print(f"Room: {room.title} Connects to: {room.north.title} At: north")
        if room.east:
            print(f"Room: {room.title} Connects to: {room.east.title} At: east")
        if room.south:
            print(f"Room: {room.title} Connects to: {room.south.title} At: south")
        if room.west:
            print(f"Room: {room.title} Connects to: {room.west.title} At: west")

# print_connections(rooms)

# print(rooms['a2'].east.title)