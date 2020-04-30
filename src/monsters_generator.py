from .models import Npc
from . import db, create_app
app = create_app()
app.app_context().push()

monsters = {
    "goblin": Npc(
        'Goblin', 
        'goblin',
        'an ugly or grotesque sprite that is usually mischievous and sometimes evil and malicious', 
        'Club', 
        10, # Gold
        15, # HP
        True, # isHostile
        4 # Attack
    ),

    "slime": Npc(
        'Slime', 
        'slime',
        'an amorphous, shapeless, gooey creature', 
        'Red Potion', 
        3, 
        8, 
        True, 
        1
    ),

    "black_rat": Npc(
        'Black Rat', 
        'black_rat',
        'a medium-sized, slender brownish-or grayish-black rat with coarse fur and a long, sparsely haired, scaly tail', 
        '', 
        1, 
        4, 
        True, 
        5
    ),

    "hobgoblin": Npc(
        "Hobgoblin",
        "hobgoblin",
        "Larger, smarter cousins to goblins.",
        '',
        45,
        40,
        True,
        10
    )

    "ogre": Npc(
        "Ogre",
        "ogre",
        "Appearing as giant humanoids with obesely muscular bodies and large heads, these creatures stand between 9 to 10 feet tall and easily weigh more than 600 lbs.",
        '',
        300,
        85,
        True,
        30
    ),

    "bug_bear": Npc(
        "Bug Bear",
        "bug_bear",
        "Massive humanoid creatures distantly related to goblins and hobgoblins but larger and stronger.",
        '',
        350,
        70,
        True,
        20
    )

    "mind_flayer": Npc(
        'Mind Flayer',
        'mind_flayer',
        'Also known as Illithids, mind flayers are aberrants that dwell underground. They enslave races other races and their powerful psionic abilities make them a feared race.',
        '',
        0,
        110,
        True,
        50
    ),

    "beholder": Npc(
        'Beholder',
        'beholder',
        'Sometimes called a sphere of many eyes, or an eye tyrant. These large orb-shaped beings have ten eyestalks and one central eye, each containing powerful magic.',
        '',
        3000,
        300,
        True,
        150
    ),

    "lich": Npc(
        'Lich',
        'lich',
        'A type of undead creature. These powerful cadavers were once mortal wizards whose greed for eternal life and endless knowledge caused them to embrace undeath.',
        '',
        50000,
        100,
        True,
        100
    )
}
