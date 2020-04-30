from .models import Npc

from . import db, create_app
app = create_app()
app.app_context().push()

def commit_monster(monster):
    with app.app_context():
        db.session.add(monster)
        db.session.commit()

goblin = Npc(
  'Goblin', 
  'goblin',
  'an ugly or grotesque sprite that is usually mischievous and sometimes evil and malicious', 
  'Club', 
  10, # Gold
  15, # HP
  True, # isHostile
  4 # Attack
)

commit_monster(goblin)

slime = Npc(
  'Slime', 
  'slime',
  'an amorphous, shapeless, gooey creature', 
  'Red Potion', 
  3, 
  8, 
  True, 
  1
)

commit_monster(slime)

black_rat = Npc(
  'Black Rat', 
  'black_rat',
  ' a medium-sized, slender brownish-or grayish-black rat with coarse fur and a long, sparsely haired, scaly tail', 
  '', 
  1, 
  4, 
  True, 
  5
)

commit_monster(black_rat)
db.session.commit()