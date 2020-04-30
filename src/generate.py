from . import db, create_app
from .models import Item, Room, Merchant, Npc

app = create_app()
app.app_context().push()

from .items_generator import items

def commit_items(items):
    with app.app_context():
        delete_rows = db.session.query(Item).delete()
        print(f'Items deleted: {delete_rows}')
        db.session.commit()
        for key, item in items.items():
            db.session.add(item)
        db.session.commit()
commit_items(items)

from .rooms_generator import rooms

def commit_rooms(rooms):
    with app.app_context():
        delete_rows = db.session.query(Room).delete()
        print(f'Rooms deleted: {delete_rows}')
        db.session.commit()
        for key, room in rooms.items():
            db.session.add(room)
        db.session.commit()

commit_rooms(rooms)

from .merchant_generator import merchant

def commit_merchant(merchant):
    with app.app_context():
        delete_rows = db.session.query(Merchant).delete()
        print(f'Merchant deleted: {delete_rows}')
        db.session.commit()
        db.session.add(merchant)
        db.session.commit()

commit_merchant(merchant)

from .monsters_generator import monsters

def commit_monster(monsters):
    with app.app_context():
        delete_rows = db.session.query(Npc).delete()
        print(f'Npcs deleted: {delete_rows}')
        db.session.commit()
        for key, monster in monsters.items():
            db.session.add(monster)
        db.session.commit()

commit_monster(monsters)