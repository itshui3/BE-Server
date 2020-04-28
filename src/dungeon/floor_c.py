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
    'a1': make_room(Room, 'a1', 'This is the beginning', 'Floor C'),
    'a2': make_room(Room, 'a2', 'Another room', 'Floor C'),
    'a3': make_room(Room, 'a3', 'Third times the charm', 'Floor C'),
    'a4': make_room(Room, 'a4', 'Forth times the charm', 'Floor C'),
    'a5': make_room(Room, 'a5', 'Fifth times the charm', 'Floor C'),

    'b1': make_room(Room, 'b1', 'Its a B room', 'Floor C'),
    'b2': make_room(Room, 'b2', 'Its a B room', 'Floor C'),
    'b3': make_room(Room, 'b3', 'Its a B room', 'Floor C'),
    'b4': make_room(Room, 'b4', 'Its a B room', 'Floor C'),
    'b5': make_room(Room, 'b5', 'Its a B room', 'Floor C'),

    'c1': make_room(Room, 'c1', 'Its a c room', 'Floor C'),
    'c2': make_room(Room, 'c2', 'Its a c room', 'Floor C'),
    'c3': make_room(Room, 'c3', 'Its a c room', 'Floor C'),
    'c4': make_room(Room, 'c4', 'Its a c room', 'Floor C'),
    'c5': make_room(Room, 'c5', 'Its a c room', 'Floor C'),

    'd1': make_room(Room, 'd1', 'Its a d room', 'Floor C'),
    'd2': make_room(Room, 'd2', 'Its a d room', 'Floor C'),
    'd3': make_room(Room, 'd3', 'Its a d room', 'Floor C'),
    'd4': make_room(Room, 'd4', 'Its a d room', 'Floor C'),
    'd5': make_room(Room, 'd5', 'Its a d room', 'Floor C'),

    'e1': make_room(Room, 'e1', 'Its a e room', 'Floor C'),
    'e2': make_room(Room, 'e2', 'Its a e room', 'Floor C'),
    'e3': make_room(Room, 'e3', 'Its a e room', 'Floor C'),
    'e4': make_room(Room, 'e4', 'Its a e room', 'Floor C'),
    'e5': make_room(Room, 'e5', 'Its a e room', 'Floor C'),

}