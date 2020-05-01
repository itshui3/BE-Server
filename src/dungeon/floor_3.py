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
    #room_key: make_room(Room, title, description, floor)
    "3-a1": make_room(Room, "3-a1", "A stone throne stands on a foot-high circular dais in the center of this cold chamber. The throne and dais bear the simple adornments of patterns of crossed lines -- a pattern also employed around each door to the room.", "Floor 3"),
    "3-a2": make_room(Room, "3-a2", "A wall that holds a seat with a hole in it is in this chamber. It's a privy! The noisome stench from the hole leads you to believe that the privy sees regular use.", "Floor 3"),
    "3-a3": make_room(Room, "3-a3", "The burble of water reaches your ears after you open the door to this room. You see the source of the noise in the far wall: a large fountain artfully carved to look like a seashell with the figure of a seacat spewing clear water into its basin.", "Floor 3"),
    "3-a4": make_room(Room, "3-a4", "This room holds six dry circular basins large enough to hold a man and a dry fountain at its center. All possess chipped carvings of merfolk and other sea creatures. It looks like this room once served some group of people as a bath.", "Floor 3"),
    "3-a5": make_room(Room, "3-a5", "Fifth times the charm", "Floor 3"),

    "3-b1": make_room(Room, "3-b1", "A glow escapes this room through its open doorways. The masonry between every stone emanates an unnatural orange radiance. Glancing quickly about the room, you note that each stone bears the carving of someone's name.", "Floor 3"),
    "3-b2": make_room(Room, "3-b2", "A huge stewpot hangs from a thick iron tripod over a crackling fire in the center of this chamber. A hole in the ceiling allows some of the smoke from the fire to escape, but much of it expands across the ceiling and rolls down to fill the room in a dark fog. Other details are difficult to make out, but some creature must be nearby, because it smells like a good soup is cooking.", "Floor 3"),
    "3-b3": make_room(Room, "3-b3", "You've opened the door to a torture chamber. Several devices of degradation, pain, and death stand about the room, all of them showing signs of regular use. The wood of the rack is worn smooth by struggling bodies, and the iron maiden appears to be occupied by a corpse.", "Floor 3"),
    "3-b4": make_room(Room, "3-b4", "This short hall leads to another door. On either side of the hall, niches are set into the wall within which stand clay urns. One of the urns has been shattered, and its contents have spilled onto its shelf and the floor. Amid the ash it held, you see blackened chunks of something that might be bone.", "Floor 3"),
    "3-b5": make_room(Room, "3-b5", "Corpses and pieces of corpses hang from hooks that dangle from chains attached to thick iron rings. Most appear humanoid but a few of the body parts appear more monstrous. You don't see any heads, hands, or feet -- all seem to have been chopped or torn off. Neither do you see any guts in the horrible array, but several thick leather sacks hang from hooks in the walls, and they are suspiciously wet and the leather looks extremely taut -- as if it' under great strain.", "Floor 3"),

    "3-c1": make_room(Room, "3-c1", "This small chamber seems divided into three parts. The first has several hooks on the walls from which hang dusty robes. An open curtain separates that space from the next, which has a dry basin set in the floor. Beyond that lies another parted curtain behind which you can see several straw mats in a semicircle pointing toward a statue of a dog-headed man.", "Floor 3"),
    "3-c2": make_room(Room, "3-c2", "When looking into this chamber, you're confronted by a thousand reflections of yourself looking back. Mirrored walls set at different angles fill the room. A path seems to wind through the mirrors, although you can't tell where it leads.", "Floor 3"),
    "3-c3": make_room(Room, "3-c3", "A large forge squats against the far wall of this room, and coals glow dimly inside. Before the forge stands a wide block of iron with a heavy-looking hammer lying atop it, no doubt for use in pounding out shapes in hot metal. Other forge tools hang in racks nearby, and a barrel of water and bellows rest on the floor nearby.", "Floor 3"),
    "3-c4": make_room(Room, "3-c4", "This chamber is clearly a prison. Small barred cells line the walls, leaving a 15-foot-wide pathway for a guard to walk. Channels run down either side of the path next to the cages, probably to allow the prisoners' waste to flow through the grates on the other side of the room. The cells appear empty but your vantage point doesn't allow you to see the full extent of them all.", "Floor 3"),
    "3-c5": make_room(Room, "3-c5", "You push open the stone door to this room and note that the only other exit is a door made of wood. It and the table shoved against it are warped and swollen. Indeed, the table only barely deserves that description. Its surface is rippled into waves and one leg doesn't even touch the floor. The door shows signs of someone trying to chop through from the other side, but it looks like they gave up.", "Floor 3"),

    "3-d1": make_room(Room, "3-d1", "This otherwise bare room has one distinguishing feature. The stone around one of the other doors has been pulled over its edges, as though the rock were as soft as clay and could be moved with fingers. The stone of the door and wall seems hastily molded together.", "Floor 3"),
    "3-d2": make_room(Room, "3-d2", "You enter a small room and your steps echo. Looking about, you're uncertain why, but then a wall vanishes and reveals an enormous chamber. The wall was an illusion and whoever cast it must be nearby!", "Floor 3"),
    "3-d3": make_room(Room, "3-d3", "You feel a sense of foreboding upon peering into this cavernous chamber. At its center lies a low heap of refuse, rubble, and bones atop which sit several huge broken eggshells. Judging by their shattered remains, the eggs were big enough to hold a crouching man, making you wonder how large -- and where -- the mother is.", "Floor 3"),
    "3-d4": make_room(Room, "3-d4", "This small chamber is a bloody mess. The corpse of a minotaur lies on the floor, its belly carved out. The creature's innards are largely missing, and yet you detect no other wounds. Bloody, froglike footprints track away from the corpse and out an open door.", "Floor 3"),
    "3-d5": make_room(Room, "3-d5", "A chill crawls up your spine and out over your skin as you look upon this room. The carvings on the wall are magnificent, a symphony in stonework -- but given the themes represented, it might be better described as a requiem. Scenes of death, both violent and peaceful, appear on every wall framed by grinning skeletons and ghoulish forms in ragged cloaks.", "Floor 3"),

    "3-e1": make_room(Room, "3-e1", "A pungent, earthy odor greets you as you pull open the door and peer into this room. Mushrooms grow in clusters of hundreds all over the floor. Looking into the room is like looking down on a forest. Tall tangles of fungus resemble forested hills, the barren floor looks like a plain between the woods, and even a trickle of water and a puddle of water that pools in a low spot bears a resemblance to a river and lake, respectively.", "Floor 3"),
    "3-e2": make_room(Room, "3-e2", "You pull open the door and hear the scrape of its opening echo throughout what must be a massive room. Peering inside, you see a vast cavern. Stalactites drip down from the ceiling in sharp points while flowstone makes strange shapes on the floor.", "Floor 3"),
    "3-e3": make_room(Room, "3-e3", "You find this chamber lit dimly by guttering candles that squat in small hills of melted wax. The smell of their smoke hits your nose along with an odor that is reminiscent of the sea. Someone has taken a large amount of salt and drawn a broad circular symbol on the floor with the candles situated equidistantly around it. Atop the salt, someone traced the symbol with a black powder that glints a dull silver in the candlelight.", "Floor 3"),
    "3-e4": make_room(Room, "3-e4", "This chamber holds one occupant: the statue of a male figure with elven features but the broad, muscular body of a hale human. It kneels on the floor as though fallen to that posture. Both its arms reach upward in supplication, and its face is a mask of grief. Two great feathered wings droop from its back, both sculpted to look broken. The statue is skillfully crafted.", "Floor 3"),
    "3-e5": make_room(Room, "3-e5", "The door to this room swings open easily on well-oiled hinges. Beyond it you see that the chamber walls have been disguised by wood paneling, and the stone ceiling and floor are hidden by bright marble tiles. Several large and well-stuffed chairs are arranged about the room along with some small reading tables.", "Floor 3"),

}

def link_rooms(rooms):
    # from left to right then top to bottom direction  --   rooms["3-"].east = rooms["3-"].title
    rooms["3-a1"].east = rooms["3-a2"].title
    rooms["3-a1"].south = rooms["3-b1"].title
    rooms["3-a2"].east = rooms["3-a3"].title
    rooms["3-a3"].south = rooms["3-b3"].title
    rooms["3-a4"].east = rooms["3-a5"].title
    rooms["3-a5"].south = rooms["3-b5"].title

    rooms["3-b1"].east = rooms["3-b2"].title
    rooms["3-b3"].east = rooms["3-b4"].title
    rooms["3-b4"].south = rooms["3-c4"].title
    rooms["3-b5"].south = rooms["3-c5"].title

    rooms["3-c1"].east = rooms["3-c2"].title
    rooms["3-c1"].south = rooms["3-d1"].title
    rooms["3-c2"].east = rooms["3-c3"].title
    rooms["3-c3"].south = rooms["3-d3"].title
    rooms["3-c4"].east = rooms["3-c5"].title
    rooms["3-c5"].south = rooms["3-d5"].title

    rooms["3-d1"].east = rooms["3-d2"].title
    rooms["3-d1"].south = rooms["3-e1"].title
    rooms["3-d2"].south = rooms["3-e2"].title
    rooms["3-d3"].east = rooms["3-d4"].title
    rooms["3-d4"].south = rooms["3-e4"].title
    rooms["3-d5"].south = rooms["3-e5"].title

    rooms["3-e1"].west = rooms["4-e5"].title
    rooms["3-e2"].east = rooms["3-e3"].title
    rooms["3-e4"].east = rooms["3-e5"].title
