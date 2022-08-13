'Data of the song breakdowns in ROM.'
from enum import IntEnum,auto
from randomizer.Enums.SongType import SongType
class Song:
	'Class used for managing song objects.'
	def __init__(A,name,type=SongType.System,group=None,memory=None,channel=0,prevent_rando=False):'Init SONG objects.\n\n        Args:\n            name (str): Name of the song.\n            type (enum, optional): Songtype enum of the item. Defaults to SongType.System.\n        ';A.name=name;A.type=type;A.group=group;A.memory=memory;A.channel=channel;A.prevent_rando=prevent_rando
class SongGroup(IntEnum):'Used to avoid overloading a song or group of songs with larger music data which can crash the game.';JungleJapes=auto();AngryAztec=auto();FranticFactory=auto();GloomyGalleon=auto();FungiForest=auto();CrystalCaves=auto();Isles=auto();Self=auto()
song_data=[Song('Silence',type=SongType.System,memory=0),Song('Jungle Japes (Starting Area)',type=SongType.BGM,group=SongGroup.JungleJapes,memory=257,channel=1),Song("Cranky's Lab",type=SongType.BGM,memory=256,channel=1),Song('Jungle Japes (Minecart)',type=SongType.BGM,memory=392,channel=2),Song('Jungle Japes (Army Dillo)',type=SongType.BGM,memory=393,channel=2),Song('Jungle Japes (Caves/Underground)',type=SongType.BGM,memory=256,channel=1),Song("Funky's Hut",type=SongType.BGM,memory=256,channel=1),Song('Unused Coin Pickup',type=SongType.System,memory=1088),Song('Bonus Minigames',type=SongType.BGM,memory=393,channel=2),Song('Triangle Trample',type=SongType.Event,memory=2242),Song('Guitar Gazump',type=SongType.Event,memory=2242),Song('Bongo Blast',type=SongType.Event,memory=2242),Song('Trombone Tremor',type=SongType.Event,memory=2242),Song('Saxaphone Slam',type=SongType.Event,memory=2242),Song('Angry Aztec',type=SongType.BGM,group=SongGroup.AngryAztec,memory=256,channel=1),Song('Transformation',type=SongType.Event,memory=2612),Song('Mini Monkey',type=SongType.BGM,group=SongGroup.Self,memory=410,channel=4),Song('Hunky Chunky',type=SongType.BGM,group=SongGroup.Self,memory=410,channel=4),Song('GB/Key Get',type=SongType.Fanfare,memory=2244),Song('Angry Aztec (Beetle Slide)',type=SongType.BGM,memory=265,channel=2),Song('Oh Banana',type=SongType.Fanfare,memory=2749),Song('Angry Aztec (Temple)',type=SongType.BGM,memory=257,channel=1),Song('Company Coin Get',type=SongType.Fanfare,memory=1591),Song('Banana Coin Get',type=SongType.Fanfare,memory=1591),Song('Going through Vulture Ring',type=SongType.Fanfare,memory=1607),Song('Angry Aztec (Dogadon)',type=SongType.BGM,memory=256,channel=1),Song('Angry Aztec (5DT)',type=SongType.BGM,memory=256,channel=1),Song('Frantic Factory (Car Race)',type=SongType.BGM,memory=392,channel=2),Song('Frantic Factory',type=SongType.BGM,group=SongGroup.FranticFactory,memory=256,channel=1),Song("Snide's HQ",type=SongType.BGM,memory=256,channel=1),Song('Jungle Japes (Tunnels)',type=SongType.BGM,group=SongGroup.Self,memory=394,channel=2),Song("Candy's Music Shop",type=SongType.BGM,memory=256,channel=1),Song('Minecart Coin Get',type=SongType.Fanfare,memory=1599),Song('Melon Slice Get',type=SongType.Fanfare,memory=1599),Song('Pause Menu',type=SongType.BGM,group=SongGroup.Self,memory=468,channel=11),Song('Crystal Coconut Get',type=SongType.Fanfare,memory=1599),Song('Rambi',type=SongType.BGM,group=SongGroup.JungleJapes,memory=408,channel=4),Song('Angry Aztec (Tunnels)',type=SongType.BGM,group=SongGroup.AngryAztec,memory=402,channel=3),Song('Water Droplets',type=SongType.Ambient,memory=2324),Song('Frantic Factory (Mad Jack)',type=SongType.BGM,memory=256,channel=1),Song('Success',type=SongType.Event,memory=2253),Song('Start (To pause game)',type=SongType.Fanfare,memory=2142),Song('Failure',type=SongType.Event,memory=2205),Song('DK Transition (Opening)',type=SongType.System,memory=2132),Song('DK Transition (Closing)',type=SongType.System,memory=2132),Song('Unused High-Pitched Japes',type=SongType.Fanfare,memory=1092),Song('Fairy Tick',type=SongType.Fanfare,memory=2245),Song('Melon Slice Drop',type=SongType.Fanfare,memory=1589),Song('Angry Aztec (Chunky Klaptraps)',type=SongType.BGM,memory=392,channel=2),Song('Frantic Factory (Crusher Room)',type=SongType.BGM,memory=256,channel=1),Song('Jungle Japes (Baboon Blast)',type=SongType.BGM,memory=256,channel=1),Song('Frantic Factory (R&D)',type=SongType.BGM,group=SongGroup.FranticFactory,memory=394,channel=2),Song('Frantic Factory (Production Room)',type=SongType.BGM,group=SongGroup.FranticFactory,memory=394,channel=2),Song("Troff 'n' Scoff",type=SongType.BGM,memory=256,channel=1),Song('Boss Defeat',type=SongType.Event,memory=2202),Song('Angry Aztec (Baboon Blast)',type=SongType.BGM,memory=256,channel=1),Song('Gloomy Galleon (Outside)',type=SongType.BGM,group=SongGroup.GloomyGalleon,memory=257,channel=1),Song('Boss Unlock',type=SongType.Event,memory=152),Song('Awaiting Entering the Boss',type=SongType.BGM,memory=400,channel=3),Song('Generic Twinkly Sounds',type=SongType.Ambient,memory=2356),Song('Gloomy Galleon (Pufftoss)',type=SongType.BGM,memory=264,channel=2),Song('Gloomy Galleon (Seal Race)',type=SongType.BGM,memory=392,channel=2),Song('Gloomy Galleon (Tunnels)',type=SongType.BGM,group=SongGroup.Self,memory=395,channel=2),Song('Gloomy Galleon (Lighthouse)',type=SongType.BGM,memory=256,channel=1),Song('Battle Arena',type=SongType.BGM,memory=256,channel=1),Song('Drop Coins (Minecart)',type=SongType.Fanfare,memory=1093),Song('Fairy Nearby',type=SongType.Ambient,memory=2341),Song('Checkpoint',type=SongType.Fanfare,memory=1095),Song('Fungi Forest (Day)',type=SongType.BGM,group=SongGroup.FungiForest,memory=257,channel=1),Song('Blueprint Get',type=SongType.Fanfare,memory=1221),Song('Fungi Forest (Night)',type=SongType.BGM,group=SongGroup.FungiForest,memory=392,channel=2),Song('Strong Kong',type=SongType.BGM,group=SongGroup.Self,memory=410,channel=4),Song('Rocketbarrel Boost',type=SongType.BGM,group=SongGroup.Self,memory=402,channel=3),Song('Orangstand Sprint',type=SongType.BGM,group=SongGroup.Self,memory=400,channel=3),Song('Fungi Forest (Minecart)',type=SongType.BGM,memory=256,channel=1),Song('DK Rap',type=SongType.BGM,memory=2304,channel=1),Song('Blueprint Drop',type=SongType.Fanfare,memory=1597),Song('Gloomy Galleon (2DS)',type=SongType.BGM,memory=256,channel=1),Song('Gloomy Galleon (5DS/Submarine)',type=SongType.BGM,memory=256,channel=1),Song('Gloomy Galleon (Pearls Chest)',type=SongType.BGM,memory=256,channel=1),Song('Gloomy Galleon (Mermaid Palace)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Dogadon)',type=SongType.BGM,memory=392,channel=2),Song('Mad Maze Maul',type=SongType.BGM,memory=392,channel=2),Song('Crystal Caves',type=SongType.BGM,group=SongGroup.CrystalCaves,memory=257,channel=1),Song('Crystal Caves (Giant Kosha Tantrum)',type=SongType.BGM,group=SongGroup.CrystalCaves,memory=403,channel=3),Song('Nintendo Logo (Old?)',type=SongType.System,memory=258),Song('Success (Races)',type=SongType.Event,memory=280),Song('Failure (Races & Try Again)',type=SongType.Event,memory=280),Song('Bonus Barrel Introduction',type=SongType.BGM,memory=256,channel=1),Song('Stealthy Snoop',type=SongType.BGM,memory=392,channel=2),Song('Minecart Mayhem',type=SongType.BGM,memory=256,channel=1),Song('Gloomy Galleon (Mechanical Fish)',type=SongType.BGM,memory=257,channel=1),Song('Gloomy Galleon (Baboon Blast)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Anthill)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Barn)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Mill)',type=SongType.BGM,memory=256,channel=1),Song('Generic Seaside Sounds',type=SongType.Ambient,memory=2322),Song('Fungi Forest (Spider)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Mushroom Top Rooms)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Giant Mushroom)',type=SongType.BGM,memory=256,channel=1),Song('Boss Introduction',type=SongType.BGM,memory=256,channel=1),Song('Tag Barrel (All of them)',type=SongType.System,memory=458),Song('Crystal Caves (Beetle Race)',type=SongType.BGM,memory=264,channel=2),Song('Crystal Caves (Igloos)',type=SongType.BGM,memory=256,channel=1),Song('Mini Boss',type=SongType.BGM,memory=426,channel=6),Song('Creepy Castle',type=SongType.BGM,memory=257,channel=1),Song('Creepy Castle (Minecart)',type=SongType.BGM,memory=256,channel=1),Song('Baboon Balloon',type=SongType.Event,memory=410),Song('Gorilla Gone',type=SongType.BGM,memory=400,channel=3),Song('DK Isles',type=SongType.BGM,group=SongGroup.Isles,memory=257,channel=1),Song("DK Isles (K Rool's Ship)",type=SongType.BGM,group=SongGroup.Isles,memory=265,channel=2),Song('DK Isles (Banana Fairy Island)',type=SongType.BGM,group=SongGroup.Isles,memory=257,channel=1),Song("DK Isles (K-Lumsy's Prison)",type=SongType.BGM,group=SongGroup.Isles,memory=257,channel=1),Song('Hideout Helm (Blast-O-Matic On)',type=SongType.BGM,memory=256,channel=1),Song('Move Get',type=SongType.Fanfare,memory=2194),Song('Gun Get',type=SongType.Fanfare,memory=2194),Song('Hideout Helm (Blast-O-Matic Off)',type=SongType.BGM,memory=256,channel=1),Song('Hideout Helm (Bonus Barrels)',type=SongType.BGM,memory=392,channel=2),Song('Crystal Caves (Cabins)',type=SongType.BGM,memory=256,channel=1),Song('Crystal Caves (Rotating Room)',type=SongType.BGM,memory=256,channel=1),Song('Crystal Caves (Tile Flipping)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Tunnels)',type=SongType.BGM,memory=256,channel=1),Song('Intro Story Medley',type=SongType.BGM,memory=256,channel=1),Song('Training Grounds',type=SongType.BGM,memory=257,channel=1),Song('Enguarde',type=SongType.BGM,group=SongGroup.GloomyGalleon,memory=408,channel=4),Song('K-Lumsy Celebration',type=SongType.Event,memory=272),Song('Creepy Castle (Crypt)',type=SongType.BGM,memory=256,channel=1),Song('Headphones Get',type=SongType.Fanfare,memory=1212),Song('Pearl Get',type=SongType.Fanfare,memory=1086),Song('Creepy Castle (Dungeon w/ Chains)',type=SongType.BGM,memory=256,channel=1),Song('Angry Aztec (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Jungle Japes (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Frantic Factory (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Gloomy Galleon (Lobby)',type=SongType.BGM,memory=257,channel=1),Song('Main Menu',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Inner Crypts)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Ballroom)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Greenhouse)',type=SongType.BGM,memory=256,channel=1),Song("K Rool's Theme",type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Winch)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Wind Tower)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Tree)',type=SongType.BGM,memory=257,channel=1),Song('Creepy Castle (Museum)',type=SongType.BGM,memory=256,channel=1),Song('BBlast Final Star',type=SongType.Fanfare,memory=1093),Song('Drop Rainbow Coin',type=SongType.Fanfare,memory=1607),Song('Rainbow Coin Get',type=SongType.Fanfare,memory=1607),Song('Normal Star',type=SongType.Fanfare,memory=1605),Song('Bean Get',type=SongType.Fanfare,memory=1605),Song('Crystal Caves (Army Dillo)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Kut Out)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Dungeon w/out Chains)',type=SongType.BGM,memory=256,channel=1),Song('Banana Medal Get',type=SongType.Fanfare,memory=1605),Song("K Rool's Battle",type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Crystal Caves (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Hideout Helm (Lobby)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Trash Can)',type=SongType.BGM,memory=256,channel=1),Song('End Sequence',type=SongType.BGM,memory=256,channel=1),Song('K-Lumsy Ending',type=SongType.BGM,memory=256,channel=1),Song('Jungle Japes',type=SongType.BGM,group=SongGroup.JungleJapes,memory=257,channel=1),Song("Jungle Japes (Cranky's Area)",type=SongType.BGM,group=SongGroup.JungleJapes,memory=256,channel=1),Song('K Rool Takeoff',type=SongType.System,memory=256,channel=1),Song('Crystal Caves (Baboon Blast)',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Baboon Blast)',type=SongType.BGM,memory=256,channel=1),Song('Creepy Castle (Baboon Blast)',type=SongType.BGM,memory=256,channel=1),Song("DK Isles (Snide's Room)",type=SongType.BGM,memory=256,channel=1),Song("K Rool's Entrance",type=SongType.BGM,memory=256,channel=1),Song('Monkey Smash',type=SongType.BGM,memory=256,channel=1),Song('Fungi Forest (Rabbit Race)',type=SongType.BGM,memory=392,channel=2),Song('Game Over',type=SongType.Event,memory=472),Song('Wrinkly Kong',type=SongType.BGM,group=SongGroup.Self,memory=394,channel=2),Song('100th CB Get',type=SongType.System,memory=1605),Song("K Rool's Defeat",type=SongType.System,memory=24),Song('Nintendo Logo',type=SongType.BGM,memory=264,channel=2)]