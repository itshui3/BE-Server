from models import Room

from dungeon.floor1.a import a1

test = a1.make_room(Room)

#declare rooms
rooms = {
    'a1': Room(
        title='Room A1',
        description='This is the beginning',
        items={},
        NPCs={},
        north=None,
        east=None,
        south=None,
        west=None
    ),
    'a2': Room(
        title='Room A2',
        description='Another room',
        items={},
        NPCs={},
        north=None,
        east=None,
        south=None,
        west=None
    )
}

#link rooms together
rooms['a1'].west = rooms['a2']
rooms['a2'].east = rooms['a1']

#test print next room
# print(rooms['a1'].west.title)
# print(rooms['a2'].east.title)

print(test.title)