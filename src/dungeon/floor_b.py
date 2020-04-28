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
    'a1': make_room(Room, 'a1', 'This is the beginning', 'Floor B'),
    'a2': make_room(Room, 'a2', 'Another room', 'Floor B'),
    'a3': make_room(Room, 'a3', 'Third times the charm', 'Floor B'),
    'a4': make_room(Room, 'a4', 'Forth times the charm', 'Floor B'),
    'a5': make_room(Room, 'a5', 'Fifth times the charm', 'Floor B'),

    'b1': make_room(Room, 'b1', 'Its a B room', 'Floor B'),
    'b2': make_room(Room, 'b2', 'Its a B room', 'Floor B'),
    'b3': make_room(Room, 'b3', 'Its a B room', 'Floor B'),
    'b4': make_room(Room, 'b4', 'Its a B room', 'Floor B'),
    'b5': make_room(Room, 'b5', 'Its a B room', 'Floor B'),

    'c1': make_room(Room, 'c1', 'Its a c room', 'Floor B'),
    'c2': make_room(Room, 'c2', 'Its a c room', 'Floor B'),
    'c3': make_room(Room, 'c3', 'Its a c room', 'Floor B'),
    'c4': make_room(Room, 'c4', 'Its a c room', 'Floor B'),
    'c5': make_room(Room, 'c5', 'Its a c room', 'Floor B'),

    'd1': make_room(Room, 'd1', 'Its a d room', 'Floor B'),
    'd2': make_room(Room, 'd2', 'Its a d room', 'Floor B'),
    'd3': make_room(Room, 'd3', 'Its a d room', 'Floor B'),
    'd4': make_room(Room, 'd4', 'Its a d room', 'Floor B'),
    'd5': make_room(Room, 'd5', 'Its a d room', 'Floor B'),

    'e1': make_room(Room, 'e1', 'Its a e room', 'Floor B'),
    'e2': make_room(Room, 'e2', 'Its a e room', 'Floor B'),
    'e3': make_room(Room, 'e3', 'Its a e room', 'Floor B'),
    'e4': make_room(Room, 'e4', 'Its a e room', 'Floor B'),
    'e5': make_room(Room, 'e5', 'Its a e room', 'Floor B'),

}