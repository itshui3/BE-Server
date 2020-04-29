from models import NPC
from items import items as defined_items

shopkeeper = NPC(
    name = 'Shopkeeper',
    description = "Will make you an offer you can't refuse",
    items = {'sword_truth': defined_items['sword_truth']},
    gold = 1000,
    HP = 1000,
    isHostile = False,
    attack = 1000

)

print(shopkeeper)