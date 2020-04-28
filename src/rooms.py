from models import Room

class A1(Room):
    def __init__(self, title, description, items, NPCs, north, east, south, west):
        super().__init__(title, description, items, NPCs, north, east, south, west)

    def __str__(self):
        return f'{self.title}, {self.description}'

rooms = []

rooms.append(A1(
    title='Room A1',
    description='This is the beginning',
    items=['item1'],
    NPCs=['none'],
    north=None,
    east=None,
    south=None,
    west=None

))

print(rooms)