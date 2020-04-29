from models import Item

items = {}

sword = Item(
    title = "Sword of Truth",
    description = "Live or die by the truth",
    price = 50,
    action = "Slice",
    damage = 50,
    heal = 0,
    armor = 0,
    reusable = True
)

green_potion = Item(
    title = "Green Potion",
    description = "A delicious concotion",
    price = 50,
    action = "Power",
    damage = 0,
    heal = 50,
    armor = 0,
    reusable = True
)

items.update({'sword': sword})
items.update({'green_potion': green_potion})
print(items)