def make_room(Room):
    return Room(
        title='Room A2',
        description='Another room',
        items={},
        NPCs={},
        north=None,
        east=None,
        south=None,
        west=None
    )