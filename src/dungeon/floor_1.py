def make_room(Room, title, description, floor):
    return Room(
        title = title,
        description = description,
        floor = floor,
        items = None,
        NPCs = None,
        mobs = None,
        north = None,
        east = None,
        south = None,
        west = None
    )

def make_floor(Room):
    return {
    #room_1-key: make_room(Room, title, description, floor)
    "1-a1": make_room(Room, "1-a1", "This is the beginning", "Floor 1"),
    "1-a2": make_room(Room, "1-a2", "Thick cobwebs fill the corners of the room, and wisps of webbing hang from the ceiling and waver in a wind you can barely feel. One corner of the ceiling has a particularly large clot of webbing within which a goblin's bones are tangled.", "Floor 1"),
    "1-a3": make_room(Room, "1-a3", "Tapestries decorate the walls of this room. Although they may once have been brilliant in hue, they now hang in graying tatters. Despite the damage of time and neglect, you can perceive once-grand images of wizards' towers, magical beasts, and symbols of spellcasting. The tapestry that is in the best condition bulges out weirdly, as though someone stands behind it (an armless statue of a female human spellcaster).", "Floor 1"),
    "1-a4": make_room(Room, "1-a4", "Rats inside the room shriek when they hear the door open, then they run in all directions from a putrid corpse lying in the center of the floor. As these creatures crowd around the edges of the room, seeking to crawl through a hole in one corner, they fight one another. The stinking corpse in the middle of the room looks human, but the damage both time and the rats have wrought are enough to make determining its race by appearance an extremely difficult task at best.", "Floor 1"),
    "1-a5": make_room(Room, "1-a5", "Neither light nor darkvision can penetrate the gloom in this chamber. An unnatural shade fills it, and the room's farthest reaches are barely visible. Near the room's center, you can just barely perceive a lump about the size of a human lying on the floor. (It might be a dead body, a pile of rags, or a sleeping monster that can take advantage of the room's darkness.)", "Floor 1"),

    "1-b1": make_room(Room, "1-b1", "Burning torches in iron sconces line the walls of this room, lighting it brilliantly. At the room's center lies a squat stone altar, its top covered in recently spilled blood. A channel in the altar funnels the blood down its side to the floor where it fills grooves in the floor that trace some kind of pattern or symbol around the altar. Unfortunately, you can't tell what it is from your vantage point.", "Floor 1"),
    "1-b2": make_room(Room, "1-b2", "A liquid-filled pit extends to every wall of this chamber. The liquid lies about 10 feet below your feet and is so murky that you can't see its bottom. The room smells sour. A rope bridge extends from your door to the room's other exit.", "Floor 1"),
    "1-b3": make_room(Room, "1-b3", "Fire crackles and pops in a small cooking fire set in the center of the room. The smoke from a burning rat on a spit curls up through a hole in the ceiling. Around the fire lie several fur blankets and a bag. It looks like someone camped here until not long ago, but then left in a hurry.", "Floor 1"),
    "1-b4": make_room(Room, "1-b4", "A flurry of bats suddenly flaps through the doorway, their screeching barely audible as they careen past your heads. They flap past you into the rooms and halls beyond. The room from which they came seems barren at first glance.", "Floor 1"),
    "1-b5": make_room(Room, "1-b5", "Rusting spikes line the walls and ceiling of this chamber. The dusty floor shows no sign that the walls move over it, but you can see the skeleton of some humanoid impaled on some wall spikes nearby.", "Floor 1"),

    "1-c1": make_room(Room, "1-c1", "You open the door, and the reek of garbage assaults your nose. Looking inside, you see a pile of refuse and offal that nearly reaches the ceiling. In the ceiling above it is a small hole that is roughly as wide as two human hands. No doubt some city dweller high above disposes of his rubbish without ever thinking about where it goes.", "Floor 1"),
    "1-c2": make_room(Room, "1-c2", "You open the door, and the room comes alive with light and music. A sourceless, warm glow suffuses the chamber, and a harp you cannot see plays soothing sounds. Unfortunately, the rest of the chamber isn't so inviting. The floor is strewn with the smashed remains of rotting furniture. It looks like the room once held a bed, a desk, a chest, and a chair.", "Floor 1"),
    "1-c3": make_room(Room, "1-c3", "A skeleton dressed in moth-eaten garb lies before a large open chest in the rear of this chamber. The chest is empty, but you note two needles projecting from the now-open lock. Dust coats something sticky on the needles' points.", "Floor 1"),
    "1-c4": make_room(Room, "1-c4", "Rounded green stones set in the floor form a snake's head that points in the direction of the doorway you stand in. The body of the snake flows back and toward the wall to go round about the room in ever smaller circles, creating a spiral pattern on the floor. Similar green-stone snakes wend along the walls, seemingly at random heights, and their long bodies make wave shapes.", "Floor 1"),
    "1-c5": make_room(Room, "1-c5", "The manacles set into the walls of this room give you the distinct impression that it was used as a prison and torture chamber, although you can see no evidence of torture devices. One particularly large set of manacles -- big enough for an ogre -- have been broken open.", "Floor 1"),

    "1-d1": make_room(Room, "1-d1", "You gaze into the room and hundreds of skulls gaze coldly back at you. They're set in niches in the walls in a checkerboard pattern, each skull bearing a half-melted candle on its head. The grinning bones stare vacantly into the room, which otherwise seems empty.", "Floor 1"),
    "1-d2": make_room(Room, "1-d2", "Unlike the flagstone common throughout the dungeon, this room is walled and floored with black marble veined with white. The ceiling is similarly marbled, but the thick pillars that hold it up are white. A brown stain drips down one side of a nearby pillar.", "Floor 1"),
    "1-d3": make_room(Room, "1-d3", "A huge iron cage lies on its side in this room, and its gate rests open on the floor. A broken chain lies under the door, and the cage is on a rotting corpse that looks to be a hobgoblin. Another corpse lies a short distance away from the cage. It lacks a head.", "Floor 1"),
    "1-d4": make_room(Room, "1-d4", "This room is a tomb. Stone sarcophagi stand in five rows of three, each carved with the visage of a warrior lying in state. In their center, one sarcophagus stands taller than the rest. Held up by six squat pillars, its stone bears the carving of a beautiful woman who seems more asleep than dead. The carving of the warriors is skillful but seems perfunctory compared to the love a sculptor must have lavished upon the lifelike carving of the woman.", "Floor 1"),
    "1-d5": make_room(Room, "1-d5", "A dim bluish light suffuses this chamber, its source obvious at a glance. Blue-glowing lichen and violet-glowing moss cling to the ceiling and spread across the floor. It even creeps down and up each wall, as if the colonies on the floor and ceiling are growing to meet each other. Their source seems to be a glowing, narrow crack in the ceiling, the extent of which you cannot gauge from your position. The air in the room smells fresh and damp.", "Floor 1"),

    "1-e1": make_room(Room, "1-e1", "You open the door to confront a room of odd pillars. Water rushes down from several holes in the ceiling, and each hole is roughly a foot wide. The water pours in columns that fall through similar holes in the floor, flowing down to some unknown depth. Each of the eight pillars of water drops as much liquid as a stream in winter thaw. The floor is damp and looks slippery.", "Floor 1"),
    "1-e2": make_room(Room, "1-e2", "This room smells strange, no doubt due to the weird sheets of black slime that drip from cracks in the ceiling and spread across the floor. The slime seeps from the shattered stone of the ceiling at a snails crawl, forming a mess of dangling walls of gook. As you watch, a bit of the stuff separates from a sheet and drops to the ground with a wet plop.", "Floor 1"),
    "1-e3": make_room(Room, "1-e3", "This room is hung with hundreds of dusty tapestries. All show signs of wear: moth holes, scorch marks, dark stains, and the damage of years of neglect. They hang on all the walls and hang from the ceiling to brush against the floor, blocking your view of the rest of the room.", "Floor 1"),
    "1-e4": make_room(Room, "1-e4", "You catch a whiff of the unmistakable metallic tang of blood as you open the door. The floor is covered with it, and splashes of blood spatter the walls. Some drops even reach the ceiling. It looks fresh, but you don't see any bodies or footprints leaving the chamber.", "Floor 1"),
    "1-e5": make_room(Room, "1-e5", "Three low, oblong piles of rubble lie near the center of this small room. Each has a weapon jutting upright from one end -- a longsword, a spear, and a quarterstaff. The piles resemble cairns used to bury dead adventurers.", "Floor 1"),

}

def link_rooms(rooms):
    # from left to right in "forward" direction  --   rooms["1-"].east = rooms["1-"].title
    rooms["1-a1"].east = rooms["1-a2"].title
    rooms["1-a2"].east = rooms["1-a3"].title
    rooms["1-a2"].south = rooms["1-b2"].title
    rooms["1-a3"].east = rooms["1-a4"].title
    rooms["1-a4"].east = rooms["1-a5"].title
    rooms["1-a5"].south = rooms["1-b5"].title

    rooms["1-b1"].east = rooms["1-b2"].title
    rooms["1-b1"].south = rooms["1-c1"].title
    # rooms["1-b2"].west = rooms["1-b1"].title #(Will be added in back track function)
    rooms["1-b3"].east = rooms["1-b4"].title
    rooms["1-b4"].south = rooms["1-c4"].title
    # rooms["1-b5"].north = rooms["1-a5"].title #(Will be added in back track function)

    rooms["1-c1"].east = rooms["1-c2"].title
    rooms["1-c2"].east = rooms["1-c3"].title
    rooms["1-c3"].north = rooms["1-b3"].title
    rooms["1-c4"].east = rooms["1-c5"].title
    rooms["1-c5"].south = rooms["1-d5"].title

    rooms["1-d1"].east = rooms["1-d2"].title
    rooms["1-d1"].south = rooms["1-e1"].title
    rooms["1-d2"].east = rooms["1-d3"].title
    rooms["1-d2"].south = rooms["1-e2"].title
    rooms["1-d3"].east = rooms["1-d4"].title
    rooms["1-d4"].east = rooms["1-d5"].title
    rooms["1-d4"].south = rooms["1-e4"].title

    rooms["1-e2"].east = rooms["1-e3"].title
    rooms["1-e4"].east = rooms["1-e5"].title
    rooms["1-e5"].east = rooms["2-e1"].title