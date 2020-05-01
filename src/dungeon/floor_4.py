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
    "4-a1": make_room(Room, "4-a1", "Many small desks with high-backed chairs stand in three long rows in this room. Each desk has an inkwell, book stand, and a partially melted candle in a rusting tin candleholder. Everything is covered with dust.", "Floor 4"),
    "4-a2": make_room(Room, "4-a2", "You round the corner to see a ghastly scene. A semitranslucent figure hangs in the air, studded with crossbow bolts and with blood pouring from every wound. It reaches toward you in a pleading gesture, points to the walls on either side of the room, and then vanishes. Once it has gone, you notice small holes in the walls, each just large enough for a bolt to pass through.", "Floor 4"),
    "4-a3": make_room(Room, "4-a3", "You open the door and before you is a dragon's hoard of treasure. Coins cover every inch of the room, and jeweled objects of precious metal jut up from the money like glittering islands in a sea of gold.", "Floor 4"),
    "4-a4": make_room(Room, "4-a4", "You open the door to reveal a 10-foot-by-10-foot room with a floor studded with spikes. The bones of some creature lie among the spikes and some insects scuttle away from the desiccated remains. No other doors are in the room, and it appears the door you opened was created to blend in with the walls. Additionally, you see no ceiling. You must be at the bottom of a very deep spiked pit.", "Floor 4"),
    "4-a5": make_room(Room, "4-a5", "You open the door to a long narrow room with a high ceiling. Three thick circles of wood rest on wooden stands. You're not certain what they are because you came into the room behind them.", "Floor 4"),

    "4-b1": make_room(Room, "4-b1", "You open the door to what must be a combat training room. Rough fighting circles are scratched into the surface of the floor. Wooden fighting dummies stand waiting for someone to attack them. A few punching bags hang from the ceiling. There's something peculiar about it all though. Every dummy is stocky and each has a bedraggled piece of leather hanging from its head that could be a long mask or a beard.", "Floor 4"),
    "4-b2": make_room(Room, "4-b2", "This small room contains several pieces of well-polished wood furniture. Eight ornate, high-backed chairs surround a long oval table, and a side table stands next to the far exit. All bear delicate carvings of various shapes. One bears carvings of skulls and bones, another is carved with shields and magic circles, and a third is carved with shapes like flames and lightning strokes.", "Floor 4"),
    "4-b3": make_room(Room, "4-b3", "The strong, sour-sweet scent of vinegar assaults your nose as you enter this room. Sundered casks and broken bottle glass line the walls of this room. Clearly this was someone's wine cellar for a time. The shards of glass are somewhat dusty, and the spilled wine is nothing more than a sticky residue in some places. Only one small barrel remains unbroken amid the rubbish.", "Floor 4"),
    "4-b4": make_room(Room, "4-b4", "Looking into this room, you note four pits in the floor. A wide square is nearest you, a triangular pit beyond it, and a little farther than both lie two circular pits. The room is rectangular nearest you but it widens into a larger rounded chamber starting just beyond the rectangular pit. You note that many flagstones, ceiling tiles, and wall blocks are carved with a skull emblem of some kind, whose dark openings emulate the layout of the pits. You've opened a door in the 'chin' and are looking up at the face.", "Floor 4"),
    "4-b5": make_room(Room, "4-b5", "This room looks like it was designed by drow. Rusted metal tiles create a huge mosaic of a spider in the floor, and someone set up rusted gratings like draperies of webs. At the far end of the chamber, the carving of a spider squats on the floor. It's about 3 feet tall and seems molded into the floor. Beyond it stands tall double doors of stone, their surface covered in a glittering web of gold.", "Floor 4"),

    "4-c1": make_room(Room, "4-c1", "You peer through the open doorway into a broad, pillared hall. The columns of stone are carved as tree trunks and seem placed at random like trees in a forest. Stone root systems crawl out into the floor and marble branches expand across the ceiling. You even note a few carvings of small birds and squirrels. Beautiful as they are, the sculpting doesn't appear elven, and it's nothing dwarves would carve.", "Floor 4"),
    "4-c2": make_room(Room, "4-c2", "This small room is lined with benchlike seats on all the walls. The seats all have holes in their top, like a privy. Facing stones on the front of the benches prevent you from seeing how deep the holes go. It looks like a communal bathroom.", "Floor 4"),
    "4-c3": make_room(Room, "4-c3", "In the center of this large room lies a 30-foot-wide round pit, its edges lined with rusting iron spikes. About 5 feet away from the pit's edge stand several stone semicircular benches. The scent of sweat and blood lingers, which makes the pit's resemblance to a fighting pit or gladiatorial arena even stronger.", "Floor 4"),
    "4-c4": make_room(Room, "4-c4", "This room is a small antechamber before two titanic bronze doors. Each stands 20 feet tall and is about 7 feet wide. The double doors are peaked at their centers, but unlike many sets of double doors, their division isn't in the center. Instead, the crack between the doors resembles a crooked bolt of lightning, which a figure in a cloud carved in the stone above the door appears to be hurling. The lightning bolt strikes down roughly 2 feet to the right of center. The figure in the clouds is deliberately indistinct, but it appears male, having a beard and male proportions. The stroke of bronze electricity hits a tower that seems small compared to the figure. This tower cracks down the center, continuing the gap between the doors until it reaches the ground. To either side of the tower lie pastoral scenes of hillsides dotted with sheep. There doesn't appear to be a lock or handles.", "Floor 4"),
    "4-c5": make_room(Room, "4-c5", "You poke your head through the break in the wall and look upon a room of titanic size. It is clearly an enormous mausoleum built to the proportions of giants. Huge niches are set into the walls within which you can discern giant bones. Stern-looking statues of stone giants stand 20 feet tall against the walls, and in the center of the room lies a 15-foot-long sarcophagus.", "Floor 4"),

    "4-d1": make_room(Room, "4-d1", "This chamber holds an odd contraption of metal and wood. It's a 20-foot-diameter circular platform that is tilted heavily to one side. Beneath it you can discern mechanisms that seem to attach to a large crank not far away. Above the platform hang metal weights on thin chains, which in turn are attached to discs and belts that are attached to other winches. It seems as though turning the winches turns and tilts the platform and sets the weights to moving.", "Floor 4"),
    "4-d2": make_room(Room, "4-d2", "You inhale a briny smell like the sea as you crack open the door to this chamber. Within you spy the source of the scent: a dark and still pool of brackish water within a low circular wall. Above it stands a strange statue of a lobster-headed and clawed woman. The statue is nearly 15 feet tall and holds the lobster claws crossed over its naked breasts.", "Floor 4"),
    "4-d3": make_room(Room, "4-d3", "Stinking smoke wafts up from braziers made of skulls set around the edges of this room. The walls bear scratch marks and lines of soot that form crude pictures and what looks like words in some language [Goblin]. To the left lies a pile of rubbish and rubble heaped into a crude dais. The dais has upon it an ironbound chest that has been painted with a goblinlike face. Furs and skins of unknown origin are strewn haphazardly about the floor before the dais.", "Floor 4"),
    "4-d4": make_room(Room, "4-d4", "This small bare chamber holds nothing but a large ironbound chest, which is big enough for a man to fit in and bears a heavy iron lock. The floor has a layer of undisturbed dust upon it.", "Floor 4"),
    "4-d5": make_room(Room, "4-d5", "This hall is choked with corpses. The bodies of orcs and ogres lie in tangled heaps where they died, and the floor is sticky with dried blood. It looks like the orcs and ogres were fighting. Some side was the victor but you're not sure which one. The bodies are largely stripped of valuables, but a few broken weapons jut from the slain or lie discarded on the floor.", "Floor 4"),

    "4-e1": make_room(Room, "4-e1", "You round the corner of the hall to confront a passage nearly blocked with crates, barrels, and chests. It seems someone set them up to barricade the hall. Three barrels are set up as seats near gaps in the barricade, no doubt the place where archers waited for foes. A rusting and torn breastplate hangs from a rope near the wall.", "Floor 4"),
    "4-e2": make_room(Room, "4-e2", "You smelled smoke as you moved down the hall, and rounding the corner into this room you see why. Every surface bears scorch marks and ash piles on the floor. The room reeks of fire and burnt flesh. Either a great battle happened here or the room bears some fire danger you cannot see for no flames light the room anymore.", "Floor 4"),
    "4-e3": make_room(Room, "4-e3", "The final battle. This hall stinks with the wet, pungent scent of mildew. Black mold grows in tangled veins across the walls and parts of the floor. Despite the smell, it looks like it might be safe to travel through. A path of stone clean of mold wends its way through the hallway.", "Floor 4"),
    "4-e4": make_room(Room, "4-e4", "You open the door and a gout of flame rushes at your face. A wave of heat strikes you at the same time and light fills the hall. The room beyond the door is ablaze! An inferno engulfs the place, clinging to bare rock and burning without fuel.", "Floor 4"),
    "4-e5": make_room(Room, "4-e5", "You peer into this room and spot the white orb of a skull lying on the floor. Suddenly a stone falls from the ceiling and smashes the skull to pieces. An instant later, another stone from the ceiling drops to strike the floor and shatter. You hear a low rumbling and cracking noise.", "Floor 4"),

}

def link_rooms(rooms):
    # from left to right then top to bottom direction  --   rooms["4-"].east = rooms["4-"].title
    rooms["4-a1"].east = rooms["4-a2"].title
    rooms["4-a1"].south = rooms["4-b1"].title
    rooms["4-a2"].east = rooms["4-a3"].title
    rooms["4-a3"].east = rooms["4-a4"].title
    rooms["4-a4"].east = rooms["4-a5"].title
    rooms["4-a5"].south = rooms["4-b5"].title

    rooms["4-b2"].east = rooms["4-b3"].title
    rooms["4-b2"].south = rooms["4-c2"].title
    rooms["4-b3"].east = rooms["4-b4"].title
    rooms["4-b3"].south = rooms["4-c3"].title
    rooms["4-b4"].east = rooms["4-b5"].title

    rooms["4-c1"].east = rooms["4-c2"].title
    rooms["4-c1"].south = rooms["4-d1"].title
    rooms["4-c3"].south = rooms["4-d3"].title
    rooms["4-c4"].east = rooms["4-c5"].title
    rooms["4-c5"].south = rooms["4-d5"].title

    rooms["4-d1"].east = rooms["4-d2"].title
    rooms["4-d1"].south = rooms["4-e1"].title
    rooms["4-d2"].south = rooms["4-e2"].title
    rooms["4-d3"].east = rooms["4-d4"].title
    rooms["4-d4"].south = rooms["4-e4"].title
    rooms["4-d5"].south = rooms["4-e5"].title

    rooms["4-e2"].east = rooms["4-e3"].title
    rooms["4-e4"].east = rooms["4-e5"].title