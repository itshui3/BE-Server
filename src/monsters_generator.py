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
    )
}
