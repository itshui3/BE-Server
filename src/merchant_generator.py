from .models import Merchant

merchant = Merchant(
    name = 'Merchant',
    inventory = 'leg_armor-1 helmet-1 green_potion-3 red_potion-3 white_potion-3 blue_potion-3',
    gold = 1000,
    HP = 1000,
    attack = 1000,
    view_inventory = "",
    buy_from = "",
    sell_to = ""
)

# print(merchant.inventory)

from . import db, create_app
app = create_app()
app.app_context().push()

def commit_merchant(merchant):
    with app.app_context():
        db.session.add(merchant)
        db.session.commit()

commit_merchant(merchant)