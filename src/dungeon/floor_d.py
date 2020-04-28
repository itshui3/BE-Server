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

def make_floor(Room):
    return {
    #room_key: make_room(Room, title, description, floor)
    'a1': make_room(Room, 'a1', 'This is the Deginning', 'Floor D'),
    'a2': make_room(Room, 'a2', 'Another room', 'Floor D'),
    'a3': make_room(Room, 'a3', 'Third times the charm', 'Floor D'),
    'a4': make_room(Room, 'a4', 'Forth times the charm', 'Floor D'),
    'a5': make_room(Room, 'a5', 'Fifth times the charm', 'Floor D'),

    'b1': make_room(Room, 'b1', 'Its a b room', 'Floor D'),
    'b2': make_room(Room, 'b2', 'Its a b room', 'Floor D'),
    'b3': make_room(Room, 'b3', 'Its a b room', 'Floor D'),
    'b4': make_room(Room, 'b4', 'Its a b room', 'Floor D'),
    'b5': make_room(Room, 'b5', 'Its a b room', 'Floor D'),

    'c1': make_room(Room, 'c1', 'Its a c room', 'Floor D'),
    'c2': make_room(Room, 'c2', 'Its a c room', 'Floor D'),
    'c3': make_room(Room, 'c3', 'Its a c room', 'Floor D'),
    'c4': make_room(Room, 'c4', 'Its a c room', 'Floor D'),
    'c5': make_room(Room, 'c5', 'Its a c room', 'Floor D'),

    'd1': make_room(Room, 'd1', 'Its a d room', 'Floor D'),
    'd2': make_room(Room, 'd2', 'Its a d room', 'Floor D'),
    'd3': make_room(Room, 'd3', 'Its a d room', 'Floor D'),
    'd4': make_room(Room, 'd4', 'Its a d room', 'Floor D'),
    'd5': make_room(Room, 'd5', 'Its a d room', 'Floor D'),

    'e1': make_room(Room, 'e1', 'Its a e room', 'Floor D'),
    'e2': make_room(Room, 'e2', 'Its a e room', 'Floor D'),
    'e3': make_room(Room, 'e3', 'Its a e room', 'Floor D'),
    'e4': make_room(Room, 'e4', 'Its a e room', 'Floor D'),
    'e5': make_room(Room, 'e5', 'Its a e room', 'Floor D'),

}