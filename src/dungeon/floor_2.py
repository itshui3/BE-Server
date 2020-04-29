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
    '2-a1': make_room(Room, '2-a1', 'This is the beginning', 'Floor 2'),
    '2-a2': make_room(Room, '2-a2', 'Another room', 'Floor 2'),
    '2-a3': make_room(Room, '2-a3', 'Third times the charm', 'Floor 2'),
    '2-a4': make_room(Room, '2-a4', 'Forth times the charm', 'Floor 2'),
    '2-a5': make_room(Room, '2-a5', 'Fifth times the charm', 'Floor 2'),

    '2-b1': make_room(Room, '2-b1', 'Its a B room', 'Floor 2'),
    '2-b2': make_room(Room, '2-b2', 'Its a B room', 'Floor 2'),
    '2-b3': make_room(Room, '2-b3', 'Its a B room', 'Floor 2'),
    '2-b4': make_room(Room, '2-b4', 'Its a B room', 'Floor 2'),
    '2-b5': make_room(Room, '2-b5', 'Its a B room', 'Floor 2'),

    '2-c1': make_room(Room, '2-c1', 'Its a c room', 'Floor 2'),
    '2-c2': make_room(Room, '2-c2', 'Its a c room', 'Floor 2'),
    '2-c3': make_room(Room, '2-c3', 'Its a c room', 'Floor 2'),
    '2-c4': make_room(Room, '2-c4', 'Its a c room', 'Floor 2'),
    '2-c5': make_room(Room, '2-c5', 'Its a c room', 'Floor 2'),

    '2-d1': make_room(Room, '2-d1', 'Its a d room', 'Floor 2'),
    '2-d2': make_room(Room, '2-d2', 'Its a d room', 'Floor 2'),
    '2-d3': make_room(Room, '2-d3', 'Its a d room', 'Floor 2'),
    '2-d4': make_room(Room, '2-d4', 'Its a d room', 'Floor 2'),
    '2-d5': make_room(Room, '2-d5', 'Its a d room', 'Floor 2'),

    '2-e1': make_room(Room, '2-e1', 'Its a e room', 'Floor 2'),
    '2-e2': make_room(Room, '2-e2', 'Its a e room', 'Floor 2'),
    '2-e3': make_room(Room, '2-e3', 'Its a e room', 'Floor 2'),
    '2-e4': make_room(Room, '2-e4', 'Its a e room', 'Floor 2'),
    '2-e5': make_room(Room, '2-e5', 'Its a e room', 'Floor 2'),

}

def link_rooms(rooms):
    # from left to right then top to bottom direction  --   rooms['2-'].east = rooms['2-'].title
    rooms['2-a1'].east = rooms['2-a2'].title
    rooms['2-a1'].south = rooms['2-b1'].title
    rooms['2-a2'].east = rooms['2-a3'].title
    rooms['2-a3'].east = rooms['2-a4'].title

    rooms['2-a3'].south = rooms['2-b3'].title
    rooms['2-a4'].east = rooms['2-a5'].title
    rooms['2-a5'].south = rooms['2-b5'].title

    rooms['2-b1'].east = rooms['2-b2'].title
    rooms['2-b2'].south = rooms['2-c2'].title
    rooms['2-b3'].south = rooms['2-c3'].title
    rooms['2-b4'].east = rooms['2-b5'].title

    rooms['2-c1'].east = rooms['2-c2'].title
    #c2.north = b2
    #c3.north = b3
    rooms['2-c4'].east = rooms['2-c5'].title
    rooms['2-c4'].south = rooms['2-d4'].title
    rooms['2-c5'].south = rooms['2-d5'].title

    #d1.north = c1
    rooms['2-d1'].south = rooms['2-e1'].title
    rooms['2-d2'].east = rooms['2-d3'].title
    rooms['2-d2'].south = rooms['2-e2'].title
    rooms['2-d3'].east = rooms['2-d4'].title
    #d4.north = c4
    #d5.north = c5
    rooms['2-d5'].south = rooms['2-e5'].title

    rooms['2-e1'].east = rooms['2-e2'].title
    #e2.north = d2
    rooms['2-e3'].east = rooms['2-e4'].title
    rooms['2-e3'].south = rooms['3-a3'].title
    rooms['2-e4'].east = rooms['2-e5'].title
    #e5.north = d5