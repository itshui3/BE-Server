from models import Room

from dungeon.floor1.a import a1, a2

#declare rooms
rooms = {
    'a1': a1.make_room(Room),
    'a2': a2.make_room(Room)
}

#link rooms together
rooms['a1'].west = rooms['a2']
rooms['a2'].east = rooms['a1']

#test print next room
print(rooms['a1'].west.title)
print(rooms['a2'].east.title)