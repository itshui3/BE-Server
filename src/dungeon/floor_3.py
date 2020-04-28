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
    '3-a1': make_room(Room, '3-a1', 'This is the beginning', 'Floor 3'),
    '3-a2': make_room(Room, '3-a2', 'Another room', 'Floor 3'),
    '3-a3': make_room(Room, '3-a3', 'Third times the charm', 'Floor 3'),
    '3-a4': make_room(Room, '3-a4', 'Forth times the charm', 'Floor 3'),
    '3-a5': make_room(Room, '3-a5', 'Fifth times the charm', 'Floor 3'),

    '3-b1': make_room(Room, '3-b1', 'Its a B room', 'Floor 3'),
    '3-b2': make_room(Room, '3-b2', 'Its a B room', 'Floor 3'),
    '3-b3': make_room(Room, '3-b3', 'Its a B room', 'Floor 3'),
    '3-b4': make_room(Room, '3-b4', 'Its a B room', 'Floor 3'),
    '3-b5': make_room(Room, '3-b5', 'Its a B room', 'Floor 3'),

    '3-c1': make_room(Room, '3-c1', 'Its a c room', 'Floor 3'),
    '3-c2': make_room(Room, '3-c2', 'Its a c room', 'Floor 3'),
    '3-c3': make_room(Room, '3-c3', 'Its a c room', 'Floor 3'),
    '3-c4': make_room(Room, '3-c4', 'Its a c room', 'Floor 3'),
    '3-c5': make_room(Room, '3-c5', 'Its a c room', 'Floor 3'),

    '3-d1': make_room(Room, '3-d1', 'Its a d room', 'Floor 3'),
    '3-d2': make_room(Room, '3-d2', 'Its a d room', 'Floor 3'),
    '3-d3': make_room(Room, '3-d3', 'Its a d room', 'Floor 3'),
    '3-d4': make_room(Room, '3-d4', 'Its a d room', 'Floor 3'),
    '3-d5': make_room(Room, '3-d5', 'Its a d room', 'Floor 3'),

    '3-e1': make_room(Room, '3-e1', 'Its a e room', 'Floor 3'),
    '3-e2': make_room(Room, '3-e2', 'Its a e room', 'Floor 3'),
    '3-e3': make_room(Room, '3-e3', 'Its a e room', 'Floor 3'),
    '3-e4': make_room(Room, '3-e4', 'Its a e room', 'Floor 3'),
    '3-e5': make_room(Room, '3-e5', 'Its a e room', 'Floor 3'),

}