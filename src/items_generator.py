from .models import Item

#define items
items = {

#weapons    
    'sword_truth': Item(
        name = 'sword_truth',
        title = "Sword of Truth",
        description = "Live or die by the truth",
        price = 50,
        action = "Slice",
        damage = 50,
        heal = 0,
        armor = 0,
        reusable = True
    ),

    'sword_magic': Item(
        name = 'sword_magic',
        title = "Sword of Magic",
        description = "Magical sword gives +1 heal on every swing",
        price = 75,
        action = "Slice + Magic",
        damage = 75,
        heal = 1,
        armor = 0,
        reusable = True
    ),

    'sword_destiny': Item(
        name = 'sword_destiny',
        title = "Sword of Destiny",
        description = "Your destiny awaits... +2 heal on every swing",
        price = 100,
        action = "Slice + Magic",
        damage = 100,
        heal = 2,
        armor = 0,
        reusable = True
    ),

    #special items
    'green_potion': Item(
        name = 'green_potion',
        title = "Green Potion",
        description = "A not so delicious concoction +50 heal (1 use)",
        price = 50,
        action = "Power",
        damage = 0,
        heal = 50,
        armor = 0,
        reusable = False
    ),

    'red_potion': Item(
        name = 'red_potion',
        title = "Red Potion",
        description = "Potion #9, beware who you drink this in front of... +60 heal (1 use)",
        price = 60,
        action = "Power",
        damage = 0,
        heal = 60,
        armor = 0,
        reusable = False
    ),

    'white_potion': Item(
        name = 'white_potion',
        title = "White Potion",
        description = "Pineapple and coconut, you're ready for the beach... +70 heal (1 use)",
        price = 70,
        action = "Power",
        damage = 0,
        heal = 70,
        armor = 0,
        reusable = False
    ),

    'blue_potion': Item(
        name = 'blue_potion',
        title = "Blue Potion",
        description = "Adios to what ails ya... +80 heal (1 use)",
        price = 80,
        action = "Power",
        damage = 0,
        heal = 80,
        armor = 0,
        reusable = False
    ),

    #armor
    'helmet': Item(
        name = 'helmet',
        title = "Shiny helmet",
        description = "A gleaming helmet that blinds enemies from the glare +50 armor",
        price = 50,
        action = "Protects noggin",
        damage = 0,
        heal = 0,
        armor = 50,
        reusable = True
    ),

    'chest_armor': Item(
        name = 'chest_armor',
        title = "Chest armor",
        description = "Protects your heart from any who look in +100 armor",
        price = 100,
        action = "Protects heart",
        damage = 0,
        heal = 0,
        armor = 100,
        reusable = True
    ),

    'leg_armor': Item(
        name = 'leg_armor',
        title = "Leg armor",
        description = "Keeps your legs in one piece +25 armor",
        price = 25,
        action = "Protects legs",
        damage = 0,
        heal = 0,
        armor = 25,
        reusable = True
    )
}

# print(items)

# commit_items(items)