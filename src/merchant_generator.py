from .models import Merchant
from .items import items

merchant_1 = Merchant(
    name = 'Merchant 1',
    inventory = {'leg_armor':items['leg_armor']},
    gold = 1000,
    hp = 1000,
    attack = 1000,
    view_inventory = "",
    buy_from = "",
    sell_to = ""
)