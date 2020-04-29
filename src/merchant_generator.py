from .models import Merchant
from .items import items

merchant = Merchant(
    name = 'Merchant',
    inventory = {'leg_armor':items['leg_armor'], 'helmet':items['helmet'], 'green_potion':items['green_potion'], 'blue_potion':items['blue_potion']},
    gold = 1000,
    HP = 1000,
    attack = 1000,
    view_inventory = "",
    buy_from = "",
    sell_to = ""
)

# print(merchant.inventory)