def make_room(Room):
    return Room(
        title='Room A1',
        description='This is the beginning',
        items={},
        NPCs={},
        north=None,
        east=None,
        south=None,
        west=None
    )