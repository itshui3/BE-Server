def make_room(Room, title, description, floor):
    return Room(
        title = title,
        description = description,
        floor = floor,
        items = None,
        NPCs = None,
        mobs = None,
        north = None,
        east = None,
        south = None,
        west = None
    )

def make_floor(Room):
    return {
    #room_key: make_room(Room, title, description, floor)
    '4-a1': make_room(Room, '4-a1', 'This is the Deginning', 'Floor 4'),
    '4-a2': make_room(Room, '4-a2', 'Another room', 'Floor 4'),
    '4-a3': make_room(Room, '4-a3', 'Third times the charm', 'Floor 4'),
    '4-a4': make_room(Room, '4-a4', 'Forth times the charm', 'Floor 4'),
    '4-a5': make_room(Room, '4-a5', 'Fifth times the charm', 'Floor 4'),

    '4-b1': make_room(Room, '4-b1', 'Its a b room', 'Floor 4'),
    '4-b2': make_room(Room, '4-b2', 'Its a b room', 'Floor 4'),
    '4-b3': make_room(Room, '4-b3', 'Its a b room', 'Floor 4'),
    '4-b4': make_room(Room, '4-b4', 'Its a b room', 'Floor 4'),
    '4-b5': make_room(Room, '4-b5', 'Its a b room', 'Floor 4'),

    '4-c1': make_room(Room, '4-c1', 'Its a c room', 'Floor 4'),
    '4-c2': make_room(Room, '4-c2', 'Its a c room', 'Floor 4'),
    '4-c3': make_room(Room, '4-c3', 'Its a c room', 'Floor 4'),
    '4-c4': make_room(Room, '4-c4', 'Its a c room', 'Floor 4'),
    '4-c5': make_room(Room, '4-c5', 'Its a c room', 'Floor 4'),

    '4-d1': make_room(Room, '4-d1', 'Its a d room', 'Floor 4'),
    '4-d2': make_room(Room, '4-d2', 'Its a d room', 'Floor 4'),
    '4-d3': make_room(Room, '4-d3', 'Its a d room', 'Floor 4'),
    '4-d4': make_room(Room, '4-d4', 'Its a d room', 'Floor 4'),
    '4-d5': make_room(Room, '4-d5', 'Its a d room', 'Floor 4'),

    '4-e1': make_room(Room, '4-e1', 'Its a e room', 'Floor 4'),
    '4-e2': make_room(Room, '4-e2', 'Its a e room', 'Floor 4'),
    '4-e3': make_room(Room, '4-e3', 'The final battle', 'Floor 4'),
    '4-e4': make_room(Room, '4-e4', 'Its a e room', 'Floor 4'),
    '4-e5': make_room(Room, '4-e5', 'Its a e room', 'Floor 4'),

}

def link_rooms(rooms):
    # from left to right then top to bottom direction  --   rooms['4-'].east = rooms['4-'].title
    rooms['4-a1'].east = rooms['4-a2'].title
    rooms['4-a1'].south = rooms['4-b1'].title
    rooms['4-a2'].east = rooms['4-a3'].title
    rooms['4-a3'].east = rooms['4-a4'].title
    rooms['4-a4'].east = rooms['4-a5'].title
    rooms['4-a5'].south = rooms['4-b5'].title

    rooms['4-b2'].east = rooms['4-b3'].title
    rooms['4-b2'].south = rooms['4-c2'].title
    rooms['4-b3'].east = rooms['4-b4'].title
    rooms['4-b3'].south = rooms['4-c3'].title
    rooms['4-b4'].east = rooms['4-b5'].title

    rooms['4-c1'].east = rooms['4-c2'].title
    rooms['4-c1'].south = rooms['4-d1'].title
    rooms['4-c3'].south = rooms['4-d3'].title
    rooms['4-c4'].east = rooms['4-c5'].title
    rooms['4-c5'].south = rooms['4-d5'].title

    rooms['4-d1'].east = rooms['4-d2'].title
    rooms['4-d1'].south = rooms['4-e1'].title
    rooms['4-d2'].south = rooms['4-e2'].title
    rooms['4-d3'].east = rooms['4-d4'].title
    rooms['4-d4'].south = rooms['4-e4'].title
    rooms['4-d5'].south = rooms['4-e5'].title

    rooms['4-e2'].east = rooms['4-e3'].title
    rooms['4-e4'].east = rooms['4-e5'].title