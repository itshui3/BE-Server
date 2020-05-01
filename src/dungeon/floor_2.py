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
    "2-a1": make_room(Room, "2-a1", "Huge rusted metal blades jut out of cracks in the walls, and rusting spikes project down from the ceiling almost to the floor. This room may have once been trapped heavily, but someone triggered them, apparently without getting killed. The traps were never reset and now seem rusted in place.", "Floor 2"),
    "2-a2": make_room(Room, "2-a2", "Several round pits lie in the floor of the room before you. Spaced roughly equally apart, each is about 15 feet in diameter and appears about 20 feet deep. A lattice of thick iron bars covers the top of each pit, and each lattice has a door of iron bars that can be lifted open. The pits smell of sweat and offal, but the room seems unoccupied.", "Floor 2"),
    "2-a3": make_room(Room, "2-a3", "Many doors fill the room ahead. Doors of varied shape, size, and design are set in every wall and even the ceiling and floor. Barely a hand's width lies between one door and the next. All the doors but the one you entered by are shut, and many have obvious locks.", "Floor 2"),
    "2-a4": make_room(Room, "2-a4", "A strange ceiling is the focal point of the room before you. It's honeycombed with hundreds of holes about as wide as your head. They seem to penetrate the ceiling to some height beyond a couple feet, but you can't be sure from your vantage point.", "Floor 2"),
    "2-a5": make_room(Room, "2-a5", "This chamber was clearly smaller at one time, but something knocked down the wall that separated it from an adjacent room. Looking into that space, you see signs of another wall knocked over. It doesn't appear that anyone made an effort to clean up the rubble, but some paths through see more usage than others.", "Floor 2"),

    "2-b1": make_room(Room, "2-b1", "A chill wind blows against you as you open the door. Beyond it, you see that the floor and ceiling are nothing but iron grates. Above and below the grates the walls extend up and down with no true ceiling or floor within your range of vision. It's as though the chamber is a bridge through the shaft of a great well. Standing on the edge of this shaft, you feel a chill wind pass down it and over your shoulder into the hall beyond.", "Floor 2"),
    "2-b2": make_room(Room, "2-b2", "This room is shattered. A huge crevasse shears the chamber in half, and the ground and ceilings are tilted away from it. It's as though the room was gripped in two enormous hands and broken like a loaf of bread. Someone has torn a tall stone door from its hinges somewhere else in the dungeon and used it to bridge the 15-foot gap of the chasm between the two sides of the room. Whatever did that must have possessed tremendous strength because the door is huge, and the enormous hinges look bent and mangled.", "Floor 2"),
    "2-b3": make_room(Room, "2-b3", "A pit yawns open before you just on the other side of the door's threshold. The entire floor of the room has fallen into a second room beneath it. Across the way you can spy a door in the wall now 15 feet off the rubble-strewn floor, and near the center of the room stands a thick column of mortared stone that appears to hold the spiral staircase that leads down to what was the lower level.", "Floor 2"),
    "2-b4": make_room(Room, "2-b4", "As the door opens, it scrapes up frost from a floor covered in ice. The room before you looks like an ice cave. A tunnel wends its way through solid ice, and huge icicles and pillars of frozen water block your vision of its farthest reaches.", "Floor 2"),
    "2-b5": make_room(Room, "2-b5", "A 30-foot-tall demonic idol dominates this room of black stone. The potbellied statue is made of red stone, and its grinning face holds what looks to be two large rubies in place of eyes. A fire burns merrily in a wide brazier the idol holds in its lap.", "Floor 2"),

    "2-c1": make_room(Room, "2-c1", "Several exits lead from this room, but only one is within the mouth of a man. The door opposite you stands within an intricate stone carving of a man's wide-open mouth. The man's nose and eyes loom over the door while his sculpted hair splays out across the wall on either side.", "Floor 2"),
    "2-c2": make_room(Room, "2-c2", "The door creaks open, which somewhat overshadows the sound of bubbling liquid. Before you is a room about which alchemists dream. Three tables bend beneath a clutter of bottles of liquid and connected glass piping. Several bookshelves stand nearby stuffed to overfilling with a jumble of books, jars, bottles, bags, and boxes. The alchemist who set this all up doesn't seem to be present, but a beaker of green fluid boils over a burner on one of the tables.", "Floor 2"),
    "2-c3": make_room(Room, "2-c3", "The scent of earthy decay assaults your nose upon peering through the open door to this room. Smashed bookcases and their sundered contents litter the floor. Paper rots in mold-spotted heaps, and shattered wood grows white fungus.", "Floor 2"),
    "2-c4": make_room(Room, "2-c4", "Several white marble busts that rest on white pillars dominate this room. Most appear to be male or female humans of middle age, but one clearly bears small horns projecting from its forehead and another is spread across the floor in a thousand pieces, leaving one pillar empty.", "Floor 2"),
    "2-c5": make_room(Room, "2-c5", " A dozen statues stand or kneel in this room, and each one lacks a head and stands in a posture of action or defense. All are garbed for battle. It's difficult to tell for sure without their heads, but two appear to be dwarves, one might be an elf, six appear human, and the rest look like they might be orcs.", "Floor 2"),

    "2-d1": make_room(Room, "2-d1", "A rusted portcullis stands just beyond the door. Looking into the room, you see three other exits, similarly blocked by portcullises. Four skeletons dressed in aged clothing and rusting armor lie on the floor in the room against the walls. They seem in poses of repose rather than violence.", "Floor 2"),
    "2-d2": make_room(Room, "2-d2", "This tiny room holds a curious array of machinery. Winches and levers project from every wall, and chains with handles dangle from the ceiling. On a nearby wall, you note a pictogram of what looks like a scythe on a chain.", "Floor 2"),
    "2-d3": make_room(Room, "2-d3", "This narrow room at first appears to be a dead-end corridor, but then you note several metal plates on the walls set at about eye height. Looking more closely, you see that one of these plates is slid aside to reveal a peephole.", "Floor 2"),
    "2-d4": make_room(Room, "2-d4", "You open the door to a scene of carnage. Two male humans, a male elf, and a female dwarf lie in drying pools of their blood. It seems that they might once have been wearing armor, except for the elf, who remains dressed in a blue robe. Clearly they lost some battle and victors stripped them of their valuables.", "Floor 2"),
    "2-d5": make_room(Room, "2-d5", "The door in front of you seems to be stuck.", "Floor 2"),

    "2-e1": make_room(Room, "2-e1", "This chamber served as an armory for some group of creatures. Armor and weapon racks line the walls and rusty and broken weapons litter the floor. It hasn't been used in a long time, and all the useful weapons have been taken but for a single sword. Unlike the other weapons in the room, this one gleams untarnished in the light.", "Floor 2"),
    "2-e2": make_room(Room, "2-e2", "There's a hiss as you open this door, and you smell a sour odor, like something rotten or fermented. Inside you see a small room lined with dusty shelves, crates, and barrels. It looks like someone once used this place as a larder, but it has been a long time since anyone came to retrieve food from it.", "Floor 2"),
    "2-e3": make_room(Room, "2-e3", "A horrendous, overwhelming stench wafts from the room before you. Small cages containing small animals and large insects line the walls. Some of the creatures look sickly and alive but most are clearly dead. Their rotting corpses and the unclean cages no doubt result in the zoo's foul odor. A cat mews weakly from its cage, but the other creatures just silently shrink back into their filthy prisons.", "Floor 2"),
    "2-e4": make_room(Room, "2-e4", "A cluster of low crates surrounds a barrel in the center of this chamber. Atop the barrel lies a stack of copper coins and two stacks of cards, one face up. Meanwhile, atop each crate rests a fan of five face-down playing cards. A thin layer of dust covers everything. Clearly someone meant to return to their game of cards.", "Floor 2"),
    "2-e5": make_room(Room, "2-e5", "This chamber of well-laid stones holds a wide bas-relief of a pastoral scene. In it you see a mountain like Mount Waterdeep, except that Castle Waterdeep and the city are missing. Instead, a small fishing village is a short way from a walled complex with several tall towers.", "Floor 2"),

}

def link_rooms(rooms):
    # from left to right then top to bottom direction  --   rooms["2-"].east = rooms["2-"].title
    rooms["2-a1"].east = rooms["2-a2"].title
    rooms["2-a1"].south = rooms["2-b1"].title
    rooms["2-a2"].east = rooms["2-a3"].title
    rooms["2-a3"].east = rooms["2-a4"].title

    rooms["2-a3"].south = rooms["2-b3"].title
    rooms["2-a4"].east = rooms["2-a5"].title
    rooms["2-a5"].south = rooms["2-b5"].title

    rooms["2-b1"].east = rooms["2-b2"].title
    rooms["2-b2"].south = rooms["2-c2"].title
    rooms["2-b3"].south = rooms["2-c3"].title
    rooms["2-b4"].east = rooms["2-b5"].title

    rooms["2-c1"].east = rooms["2-c2"].title
    rooms["2-c1"].south = rooms["2-d1"].title
    #c2.north = b2
    #c3.north = b3
    rooms["2-c4"].east = rooms["2-c5"].title
    rooms["2-c4"].south = rooms["2-d4"].title
    rooms["2-c5"].south = rooms["2-d5"].title

    #d1.north = c1
    rooms["2-d1"].south = rooms["2-e1"].title
    rooms["2-d2"].east = rooms["2-d3"].title
    rooms["2-d2"].south = rooms["2-e2"].title
    rooms["2-d3"].east = rooms["2-d4"].title
    #d4.north = c4
    #d5.north = c5
    rooms["2-d5"].south = rooms["2-e5"].title

    rooms["2-e1"].east = rooms["2-e2"].title
    #e2.north = d2
    rooms["2-e3"].east = rooms["2-e4"].title
    rooms["2-e3"].south = rooms["3-a3"].title
    rooms["2-e4"].east = rooms["2-e5"].title
    #e5.north = d5