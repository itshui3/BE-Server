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
    #room_1-key: make_room(Room, title, description, floor)
    '1-a1': make_room(Room, '1-a1', 'This is the beginning', 'Floor 1'),
    '1-a2': make_room(Room, '1-a2', 'Another room', 'Floor 1'),
    '1-a3': make_room(Room, '1-a3', 'Third times the charm', 'Floor 1'),
    '1-a4': make_room(Room, '1-a4', 'Forth times the charm', 'Floor 1'),
    '1-a5': make_room(Room, '1-a5', 'Fifth times the charm', 'Floor 1'),

    '1-b1': make_room(Room, '1-b1', 'Its a B room', 'Floor 1'),
    '1-b2': make_room(Room, '1-b2', 'Its a B room', 'Floor 1'),
    '1-b3': make_room(Room, '1-b3', 'Its a B room', 'Floor 1'),
    '1-b4': make_room(Room, '1-b4', 'Its a B room', 'Floor 1'),
    '1-b5': make_room(Room, '1-b5', 'Its a B room', 'Floor 1'),

    '1-c1': make_room(Room, '1-c1', 'Its a c room', 'Floor 1'),
    '1-c2': make_room(Room, '1-c2', 'Its a c room', 'Floor 1'),
    '1-c3': make_room(Room, '1-c3', 'Its a c room', 'Floor 1'),
    '1-c4': make_room(Room, '1-c4', 'Its a c room', 'Floor 1'),
    '1-c5': make_room(Room, '1-c5', 'Its a c room', 'Floor 1'),

    '1-d1': make_room(Room, '1-d1', 'Its a d room', 'Floor 1'),
    '1-d2': make_room(Room, '1-d2', 'Its a d room', 'Floor 1'),
    '1-d3': make_room(Room, '1-d3', 'Its a d room', 'Floor 1'),
    '1-d4': make_room(Room, '1-d4', 'Its a d room', 'Floor 1'),
    '1-d5': make_room(Room, '1-d5', 'Its a d room', 'Floor 1'),

    '1-e1': make_room(Room, '1-e1', 'Its a e room', 'Floor 1'),
    '1-e2': make_room(Room, '1-e2', 'Its a e room', 'Floor 1'),
    '1-e3': make_room(Room, '1-e3', 'Its a e room', 'Floor 1'),
    '1-e4': make_room(Room, '1-e4', 'Its a e room', 'Floor 1'),
    '1-e5': make_room(Room, '1-e5', 'Its a e room', 'Floor 1'),

}

def link_rooms(rooms):
    rooms['1-a1'].east = rooms['1-a2'].title
    rooms['1-a2'].east = rooms['1-a3'].title
    rooms['1-a2'].south = rooms['1-b2'].title
    rooms['1-a3'].east = rooms['1-a4'].title
    rooms['1-a4'].east = rooms['1-a5'].title
    rooms['1-a5'].south = rooms['1-b5'].title

    rooms['1-b1'].east = rooms['1-b2'].title
    rooms['1-b1'].south = rooms['1-c1'].title
    # rooms['1-b2'].west = rooms['1-b1'].title #(Will be added in back track function)
    rooms['1-b3'].east = rooms['1-b4'].title
    rooms['1-b4'].south = rooms['1-c4'].title
    # rooms['1-b5'].north = rooms['1-a5'].title #(Will be added in back track function)

    rooms['1-c1'].east = rooms['1-c2'].title
    rooms['1-c2'].east = rooms['1-c3'].title
    rooms['1-c3'].north = rooms['1-b3'].title
    rooms['1-c4'].east = rooms['1-c5'].title
    rooms['1-c5'].south = rooms['1-d5'].title

    rooms['1-d1'].east = rooms['1-d2'].title
    rooms['1-d1'].south = rooms['1-e1'].title
    rooms['1-d2'].east = rooms['1-d3'].title
    rooms['1-d2'].south = rooms['1-e2'].title
    rooms['1-d3'].east = rooms['1-d4'].title
    rooms['1-d4'].east = rooms['1-d5'].title
    rooms['1-d4'].south = rooms['1-e4'].title

    rooms['1-e2'].east = rooms['1-e3'].title
    rooms['1-e4'].east = rooms['1-e5'].title