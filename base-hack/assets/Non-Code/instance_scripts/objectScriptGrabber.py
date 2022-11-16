'Grab object scripts.'
_AO='new_absolute_address'
_AN='/setup.bin'
_AM='Map Paths'
_AL='Mad Jack Platform (Blue)'
_AK='Mad Jack Platform (White)'
_AJ='Large Aztec Door'
_AI='Large Wooden Door'
_AH='Submerged Pot'
_AG='Mushrooms (Small)'
_AF='Pink Flowers'
_AE='Blue Flowers'
_AD='Warning Lights'
_AC='Propeller'
_AB='Question Mark Box'
_AA='Wall Panel'
_A9='Triangle Pad'
_A8='Stone Monkey Face'
_A7='Tree Stump'
_A6='Bamboo Gate'
_A5='Golden Banana'
_A4='Small plant'
_A3='Coffin Door'
_A2="Snide's HQ"
_A1='Banana Medal'
_A0='Training Grounds'
_z='Creepy Castle'
_y='Main Menu'
_x='DK Rap'
_w='Crystal Caves'
_v="Troff 'n' Scoff"
_u='Nintendo Logo'
_t='Angry Aztec'
_s='Batty Barrel Bandit! (easy)'
_r='Frantic Factory'
_q="Candy's Music Shop"
_p='Jungle Japes'
_o='Spotlight'
_n='Broken Ship Piece'
_m='DK Star'
_l='Night Gate'
_k="K. Rool's Ship"
_j='Wooden Pole'
_i='Metal Object'
_h='Wood panel small'
_g='Metal Platform'
_f='Metal Panel'
_e='Flame'
_d='Yellow Flowers'
_c="Cranky's Lab"
_b='entries'
_a='wb'
_Z='Boulder'
_Y='Wooden Door'
_X='Target'
_W='Stone Monkey Head'
_V='Big Blue wall panel'
_U='Crystal'
_T='if (loadedActorCount != 0) {'
_S='Light'
_R='Barrel'
_Q='Door'
_P='Metal Grate'
_O='Ladder'
_N='Metal Bars'
_M='absolute_address'
_L='do {'
_K='Plant'
_J='Power Beam'
_I='Tree'
_H='output_filename'
_G='name'
_F="Snide's Mechanism"
_E='Metal Door'
_D='big'
_C='index'
_B='}'
_A='-'
import gzip,math,os,shutil,tkinter as tk,zlib
from tkinter import filedialog
from typing import BinaryIO
root=tk.Tk()
root.withdraw()
maps=['Test Map',"Funky's Store",'DK Arcade',"K. Rool Barrel: Lanky's Maze",'Jungle Japes: Mountain',_c,'Jungle Japes: Minecart',_p,'Jungle Japes: Army Dillo','Jetpac','Kremling Kosh! (very easy)','Stealthy Snoop! (normal, no logo)','Jungle Japes: Shell',"Jungle Japes: Lanky's Cave",'Angry Aztec: Beetle Race',"Snide's H.Q.","Angry Aztec: Tiny's Temple",'Hideout Helm','Teetering Turtle Trouble! (very easy)','Angry Aztec: Five Door Temple (DK)','Angry Aztec: Llama Temple','Angry Aztec: Five Door Temple (Diddy)','Angry Aztec: Five Door Temple (Tiny)','Angry Aztec: Five Door Temple (Lanky)','Angry Aztec: Five Door Temple (Chunky)',_q,_r,'Frantic Factory: Car Race','Hideout Helm (Level Intros, Game Over)','Frantic Factory: Power Shed','Gloomy Galleon',"Gloomy Galleon: K. Rool's Ship",_s,"Jungle Japes: Chunky's Cave",'DK Isles Overworld',"K. Rool Barrel: DK's Target Game",'Frantic Factory: Crusher Room','Jungle Japes: Barrel Blast',_t,'Gloomy Galleon: Seal Race',_u,'Angry Aztec: Barrel Blast',_v,'Gloomy Galleon: Shipwreck (Diddy, Lanky, Chunky)','Gloomy Galleon: Treasure Chest','Gloomy Galleon: Mermaid','Gloomy Galleon: Shipwreck (DK, Tiny)','Gloomy Galleon: Shipwreck (Lanky, Tiny)','Fungi Forest','Gloomy Galleon: Lighthouse',"K. Rool Barrel: Tiny's Mushroom Game",'Gloomy Galleon: Mechanical Fish','Fungi Forest: Ant Hill','Battle Arena: Beaver Brawl!','Gloomy Galleon: Barrel Blast','Fungi Forest: Minecart',"Fungi Forest: Diddy's Barn","Fungi Forest: Diddy's Attic","Fungi Forest: Lanky's Attic","Fungi Forest: DK's Barn",'Fungi Forest: Spider','Fungi Forest: Front Part of Mill','Fungi Forest: Rear Part of Mill','Fungi Forest: Mushroom Puzzle','Fungi Forest: Giant Mushroom','Stealthy Snoop! (normal)','Mad Maze Maul! (hard)','Stash Snatch! (normal)','Mad Maze Maul! (easy)','Mad Maze Maul! (normal)','Fungi Forest: Mushroom Leap','Fungi Forest: Shooting Game',_w,'Battle Arena: Kritter Karnage!','Stash Snatch! (easy)','Stash Snatch! (hard)',_x,'Minecart Mayhem! (easy)','Busy Barrel Barrage! (easy)','Busy Barrel Barrage! (normal)',_y,'Title Screen (Not For Resale Version)','Crystal Caves: Beetle Race','Fungi Forest: Dogadon','Crystal Caves: Igloo (Tiny)','Crystal Caves: Igloo (Lanky)','Crystal Caves: Igloo (DK)',_z,'Creepy Castle: Ballroom','Crystal Caves: Rotating Room','Crystal Caves: Shack (Chunky)','Crystal Caves: Shack (DK)','Crystal Caves: Shack (Diddy, middle part)','Crystal Caves: Shack (Tiny)',"Crystal Caves: Lanky's Hut",'Crystal Caves: Igloo (Chunky)','Splish-Splash Salvage! (normal)','K. Lumsy','Crystal Caves: Ice Castle','Speedy Swing Sortie! (easy)','Crystal Caves: Igloo (Diddy)','Krazy Kong Klamour! (easy)','Big Bug Bash! (very easy)','Searchlight Seek! (very easy)','Beaver Bother! (easy)','Creepy Castle: Tower','Creepy Castle: Minecart','Kong Battle: Battle Arena','Creepy Castle: Crypt (Lanky, Tiny)','Kong Battle: Arena 1','Frantic Factory: Barrel Blast','Gloomy Galleon: Pufftoss','Creepy Castle: Crypt (DK, Diddy, Chunky)','Creepy Castle: Museum','Creepy Castle: Library','Kremling Kosh! (easy)','Kremling Kosh! (normal)','Kremling Kosh! (hard)','Teetering Turtle Trouble! (easy)','Teetering Turtle Trouble! (normal)','Teetering Turtle Trouble! (hard)',_s,'Batty Barrel Bandit! (normal)','Batty Barrel Bandit! (hard)','Mad Maze Maul! (insane)','Stash Snatch! (insane)','Stealthy Snoop! (very easy)','Stealthy Snoop! (easy)','Stealthy Snoop! (hard)','Minecart Mayhem! (normal)','Minecart Mayhem! (hard)','Busy Barrel Barrage! (hard)','Splish-Splash Salvage! (hard)','Splish-Splash Salvage! (easy)','Speedy Swing Sortie! (normal)','Speedy Swing Sortie! (hard)','Beaver Bother! (normal)','Beaver Bother! (hard)','Searchlight Seek! (easy)','Searchlight Seek! (normal)','Searchlight Seek! (hard)','Krazy Kong Klamour! (normal)','Krazy Kong Klamour! (hard)','Krazy Kong Klamour! (insane)','Peril Path Panic! (very easy)','Peril Path Panic! (easy)','Peril Path Panic! (normal)','Peril Path Panic! (hard)','Big Bug Bash! (easy)','Big Bug Bash! (normal)','Big Bug Bash! (hard)','Creepy Castle: Dungeon','Hideout Helm (Intro Story)','DK Isles (DK Theatre)','Frantic Factory: Mad Jack','Battle Arena: Arena Ambush!','Battle Arena: More Kritter Karnage!','Battle Arena: Forest Fracas!','Battle Arena: Bish Bash Brawl!','Battle Arena: Kamikaze Kremlings!','Battle Arena: Plinth Panic!','Battle Arena: Pinnacle Palaver!','Battle Arena: Shockwave Showdown!','Creepy Castle: Basement','Creepy Castle: Tree',"K. Rool Barrel: Diddy's Kremling Game","Creepy Castle: Chunky's Toolshed",'Creepy Castle: Trash Can','Creepy Castle: Greenhouse','Jungle Japes Lobby','Hideout Helm Lobby',"DK's House",'Rock (Intro Story)','Angry Aztec Lobby','Gloomy Galleon Lobby','Frantic Factory Lobby',_A0,'Dive Barrel','Fungi Forest Lobby','Gloomy Galleon: Submarine','Orange Barrel','Barrel Barrel','Vine Barrel','Creepy Castle: Crypt','Enguarde Arena','Creepy Castle: Car Race','Crystal Caves: Barrel Blast','Creepy Castle: Barrel Blast','Fungi Forest: Barrel Blast','Fairy Island','Kong Battle: Arena 2','Rambi Arena','Kong Battle: Arena 3','Creepy Castle Lobby','Crystal Caves Lobby',"DK Isles: Snide's Room",'Crystal Caves: Army Dillo','Angry Aztec: Dogadon','Training Grounds (End Sequence)','Creepy Castle: King Kut Out','Crystal Caves: Shack (Diddy, upper part)',"K. Rool Barrel: Diddy's Rocketbarrel Game","K. Rool Barrel: Lanky's Shooting Game",'K. Rool Fight: DK Phase','K. Rool Fight: Diddy Phase','K. Rool Fight: Lanky Phase','K. Rool Fight: Tiny Phase','K. Rool Fight: Chunky Phase','Bloopers Ending',"K. Rool Barrel: Chunky's Hidden Kremling Game","K. Rool Barrel: Tiny's Pony Tail Twirl Game","K. Rool Barrel: Chunky's Shooting Game","K. Rool Barrel: DK's Rambi Game",'K. Lumsy Ending',"K. Rool's Shoe","K. Rool's Arena",'UNKNOWN 216','UNKNOWN 217','UNKNOWN 218','UNKNOWN 219','UNKNOWN 220','UNKNOWN 221']
hud_items=['Coloured banana','Banana coin','Ammo','Homing ammo','Orange',_U,'Film','Instrument','GB Count?(Left)','GB Count (Bottom)',_A1,'Minecart/Minigame Coin','Blueprint','Coloured Bananas (???)','Banana coins (???)']
songs=['Silence','Jungle Japes (Starting Area)',_c,'Jungle Japes (Minecart)','Jungle Japes (Army Dillo)','Jungle Japes (Caves/Underground)',"Funky's Hut",'Unused Coin Pickup','Bonus Minigames','Triangle Trample','Guitar Gazump','Bongo Blast','Trombone Tremor','Saxaphone Slam',_t,'Transformation','Mini Monkey','Hunky Chunky','GB/Key Get','Angry Aztec (Beetle Slide)','Oh Banana','Angry Aztec (Temple)','Company Coin Get','Banana Coin Get','Going through Vulture Ring','Angry Aztec (Dogadon)','Angry Aztec (5DT)','Frantic Factory (Car Race)',_r,_A2,'Jungle Japes (Tunnels)',_q,'Minecart Coin Get','Melon Slice Get','Pause Menu','Crystal Coconut Get','Rambi','Angry Aztec (Tunnels)','Water Droplets','Frantic Factory (Mad Jack)','Success','Start (To pause game)','Failure','DK Transition (Opening)','DK Transition (Closing)','Unused High-Pitched Japes','Fairy Tick','Melon Slice Drop','Angry Aztec (Chunky Klaptraps)','Frantic Factory (Crusher Room)','Jungle Japes (Baboon Blast)','Frantic Factory (R&D)','Frantic Factory (Production Room)',_v,'Boss Defeat','Angry Aztec (Baboon Blast)','Gloomy Galleon (Outside)','Boss Unlock','Awaiting Entering the Boss','Generic Twinkly Sounds','Gloomy Galleon (Pufftoss)','Gloomy Galleon (Seal Race)','Gloomy Galleon (Tunnels)','Gloomy Galleon (Lighthouse)','Battle Arena','Drop Coins (Minecart)','Fairy Nearby','Checkpoint','Fungi Forest (Day)','Blueprint Get','Fungi Forest (Night)','Strong Kong','Rocketbarrel Boost','Orangstand Sprint','Fungi Forest (Minecart)',_x,'Blueprint Drop','Gloomy Galleon (2DS)','Gloomy Galleon (5DS/Submarine)','Gloomy Galleon (Pearls Chest)','Gloomy Galleon (Mermaid Palace)','Fungi Forest (Dogadon)','Mad Maze Maul',_w,'Crystal Caves (Giant Kosha Tantrum)','Nintendo Logo (Old?)','Success (Races)','Failure (Races & Try Again)','Bonus Barrel Introduction','Stealthy Snoop','Minecart Mayhem','Gloomy Galleon (Mechanical Fish)','Gloomy Galleon (Baboon Blast)','Fungi Forest (Anthill)','Fungi Forest (Barn)','Fungi Forest (Mill)','Generic Seaside Sounds','Fungi Forest (Spider)','Fungi Forest (Mushroom Top Rooms)','Fungi Forest (Giant Mushroom)','Boss Introduction','Tag Barrel (All of them)','Crystal Caves (Beetle Race)','Crystal Caves (Igloos)','Mini Boss',_z,'Creepy Castle (Minecart)','Baboon Balloon','Gorilla Gone','DK Isles',"DK Isles (K Rool's Ship)",'DK Isles (Banana Fairy Island)',"DK Isles (K-Lumsy's Prison)",'Hideout Helm (Blast-O-Matic On)','Move Get','Gun Get','Hideout Helm (Blast-O-Matic Off)','Hideout Helm (Bonus Barrels)','Crystal Caves (Cabins)','Crystal Caves (Rotating Room)','Crystal Caves (Tile Flipping)','Creepy Castle (Tunnels)','Intro Story Medley',_A0,'Enguarde','K-Lumsy Celebration','Creepy Castle (Crypt)','Headphones Get','Pearl Get','Creepy Castle (Dungeon w/ Chains)','Angry Aztec (Lobby)','Jungle Japes (Lobby)','Frantic Factory (Lobby)','Gloomy Galleon (Lobby)',_y,'Creepy Castle (Inner Crypts)','Creepy Castle (Ballroom)','Creepy Castle (Greenhouse)',"K Rool's Theme",'Fungi Forest (Winch)','Creepy Castle (Wind Tower)','Creepy Castle (Tree)','Creepy Castle (Museum)','BBlast Final Star','Drop Rainbow Coin','Rainbow Coin Get','Normal Star','Bean Get','Crystal Caves (Army Dillo)','Creepy Castle (Kut Out)','Creepy Castle (Dungeon w/out Chains)','Banana Medal Get',"K Rool's Battle",'Fungi Forest (Lobby)','Crystal Caves (Lobby)','Creepy Castle (Lobby)','Hideout Helm (Lobby)','Creepy Castle (Trash Can)','End Sequence','K-Lumsy Ending',_p,"Jungle Japes (Cranky's Area)",'K Rool Takeoff','Crystal Caves (Baboon Blast)','Fungi Forest (Baboon Blast)','Creepy Castle (Baboon Blast)',"DK Isles (Snide's Room)","K Rool's Entrance",'Monkey Smash','Fungi Forest (Rabbit Race)','Game Over','Wrinkly Kong','100th CB Get',"K Rool's Defeat",_u]
object_modeltwo_types=['Nothing','Thin Flame?',_A,_I,_A,_d,_A,_A,'Xmas Holly?',_A,'CB Single (Diddy)','Large Wooden Panel','Flames','CB Single (DK)','Large Iron Bars Panel','Goo Hand',_e,'Homing Ammo Crate',_A3,'Coffin Lid','Skull','Wooden Crate','CB Single (Tiny)','Shield','Metal thing','Coffin',_f,'Rock Panel','Banana Coin (Tiny)','Banana Coin (DK)','CB Single (Lanky)','CB Single (Chunky)',_I,_A,_f,'Banana Coin (Lanky)','Banana Coin (Diddy)',_f,'Metal Panel Red','Banana Coin (Chunky)','Metal Panel Grey',_I,_A,'CB Bunch (DK)','Hammock','Small jungle bush plant',_A,_A4,'Bush',_A,_A,_A,'Metal Bridge','Large Blue Crystal',_K,_K,_A,'White Flowers','Stem 4 Leaves',_A,_A,_A4,_A,_A,_A,_A,_A,'Yellow Flower','Blade of Grass Large','Lilypad?',_K,'Iron Bars','Nintendo Coin','Metal Floor',_A,_A,'Bull Rush',_A,_A,'Metal box/platform','K Crate',_A,'Wooden panel',_A,_A,_A,'Orange','Watermelon Slice',_I,_I,_I,'Tree (Black)',_A,'Light Green platform',_A,_A,_A,_A,'Brick Wall',_A,_A,_A,_A,'Wrinkly Door (Tiny)',_A,_A,_A,'Conveyor Belt',_I,_I,_I,_A,'Primate Punch Switch','Hi-Lo toggle machine','Breakable Metal Grate',_c,_A5,_g,_N,_A,'Metal fence',_A2,"Funky's Armory",_A,'Blue lazer field',_A,_A6,_A,_A7,'Breakable Hut','Mountain Bridge',_A7,_A6,_A,'Blue/green tree',_A,'Mushroom',_A,'Disco Ball','2 Door (5DS)','3 Door (5DS)','Map of DK island','Crystal Coconut','Ammo Crate',_A1,'Peanut','Simian Slam Switch (Chunky, Green)','Simian Slam Switch (Diddy, Green)','Simian Slam Switch (DK, Green)','Simian Slam Switch (Lanky, Green)','Simian Slam Switch (Tiny, Green)','Baboon Blast Pad','Film','Chunky Rotating Room',_A8,_A8,'Aztec Panel blue',_A,'Ice Floor','Ice Pole',_V,_V,_V,_V,'KONG Letter (K)','KONG Letter (O)','KONG Letter (N)','KONG Letter (G)','Bongo Pad','Guitar Pad','Saxaphone Pad',_A9,'Trombone Pad',_h,_h,_h,'Wood Panel small',_AA,_AA,'Stone Monkey Face (Not Solid)','Feed Me Totem','Melon Crate','Lava Platform','Rainbow Coin','Green Switch','Coconut Indicator','Snake Head','Matching Game Board',_W,'Large metal section','Production Room Crusher',_g,_i,_i,_i,'Gong','Platform','Bamboo together',_N,_X,'Wooden object',_O,_O,'Wooden pole','Blue panel',_O,'Grey Switch','D Block for toy world','Hatch (Factory)',_N,'Raisable Metal Platform','Metal Cage','Simian Spring Pad','Power Shed','Metal platform','Sun Lighting effect panel',_j,_j,_j,_A,_AB,'Blueprint (Tiny)','Blueprint (DK)','Blueprint (Chunky)','Blueprint (Diddy)','Blueprint (Lanky)','Tree Dark','Rope',_A,_A,'Lever','Green Croc Head (Minecart)','Metal Gate with red/white stripes',_A,'Purple Croc Head (Minecart)','Wood panel','DK coin','Wooden leg',_A,'Wrinkly Door (Lanky)','Wrinkly Door (DK)','Wrinkly Door (Chunky)','Wrinkly Door (Diddy)','Torch','Number Game (1)','Number Game (2)','Number Game (3)','Number Game (4)','Number Game (5)','Number Game (6)','Number Game (7)','Number Game (8)','Number Game (9)','Number Game (10)','Number Game (11)','Number Game (12)','Number Game (13)','Number Game (14)','Number Game (15)','Number Game (16)','Bad Hit Detection Wheel','Breakable Gate',_A,'Picture of DK island','White flashing thing',_R,'Gorilla Gone Pad','Monkeyport Pad','Baboon Balloon Pad',_S,_S,_R,_R,_R,_R,'Pad','Red Light','Breakable X Panel','Power Shed Screen','Crusher','Floor Panel','Metal floor panel mesh',_E,_E,_E,_E,_E,_E,'Toyz Box','O Pad','Bonus Barrel Trap','Sun Idol',"Candy's Shop",'Pineapple Switch','Peanut Switch','Feather Switch','Grape Switch','Coconut Switch',_A,'Kong Pad','Boss Door','Troff n Scoff Feed Pad','Metal Bars horizontal',_N,'Harbour Gate',_k,_g,_A,_e,_e,'Scoff n Troff platform','Troff n Scoff Banana Count Pad (DK)','Torch',_A,_A,_A,'Boss Key','Machine',_E,_E,_E,_E,'Piano Game','Troff n Scoff Banana Count Pad (Diddy)','Troff n Scoff Banana Count Pad (Lanky)','Troff n Scoff Banana Count Pad (Chunky)','Troff n Scoff Banana Count Pad (Tiny)','Door 1342','Door 3142','Door 4231','1 Switch (Red)','2 Switch (Blue)','3 Switch (Orange)','4 Switch (Green)',_A,'Metal Archway','Green Crystal thing','Red Crystal thing',_AC,'Large Metal Bar','Ray Sheild?',_A,_A,_A,_A,_S,_X,_O,_N,'Red Feather','Grape','Pinapple','Coconut','Rope','On Button','Up Button','Metal barrel or lid','Simian Slam Switch (Chunky, Red)','Simian Slam Switch (Diddy, Red)','Simian Slam Switch (DK, Red)','Simian Slam Switch (Lanky, Red)','Simian Slam Switch (Tiny, Red)','Simian Slam Switch (Chunky, Blue)','Simian Slam Switch (Diddy, Blue)','Simian Slam Switch (DK, Blue)','Simian Slam Switch (Lanky, Blue)','Simian Slam Switch (Tiny, Blue)',_P,'Pendulum','Weight',_Q,'Day Switch','Night Switch','Hands','Bell','Grate',_U,_U,_U,_Q,'Gate','Breakable Door',_l,'Night Grate','Unknown',_P,'Mill Pulley Mechanism','Metal Bar','Water Wheel','Crusher','Coveyor Belt',_l,_AB,'Spider Web','Grey Croc Head','Caution Sign (Falling Rocks)',_Q,'Battle Crown',_A,_A,'Dogadon Arena Background','Skull Door (Small)','Skull Door (Big)',_A,'Tombstone',_A,_m,"K. Rool's Throne",'Bean',_J,_J,_J,_J,_J,_J,_J,_J,_J,_J,_AD,'K. Rool Door',_P,'Crown Door','Coin Door','Medal Barrier (DK)','Medal Barrier (Diddy)','Medal Barrier (Tiny)','Medal Barrier (Chunky)','Medal Barrier (Lanky)','I Door (Helm, DK)','V Door (Helm, Diddy)','III Door (Helm, Tiny)','II Door (Helm, Chunky)','IV Door (Helm, Lanky)',_E,'Stone Wall','Pearl','Small Door',_A,'Cloud',_AD,_Q,'Mushroom (Yellow)','Mushroom (Purple)','Mushroom (Blue)','Mushroom (Green)','Mushroom (Red)','Mushroom Puzzle Instructions','Face Puzzle Board','Mushroom','Small Torch','DK Arcade Machine','Simian Slam Switch (Any Kong?)','Spotlight (Crown Arena?)','Battle Crown Pad','Seaweed',_S,'Dust?','Moon Trapdoor',_O,'Mushroom Board',_m,'Wooden Box','Yellow CB Powerup','Blue CB Powerup','Coin Powerup?','DK Coin',_F,_F,_F,_F,_F,_F,_F,_F,_F,_F,_F,_AE,'Plant (Green)','Plant (Brown)',_K,_AF,_AF,_K,_d,_d,_K,_AE,'Blue Flower',_K,_K,'Red Flowers','Red Flower',_AG,_AG,'Purple Flowers',_I,'Cactus','Cactus','Ramp',_AH,_AH,_O,_O,'Floor Texture?','Iron Gate','Day Gate',_l,'Cabin Door','Ice Wall (Breakable)','Igloo Door','Castle Top','Ice Dome','Boulder Pad',_X,'Metal Gate','CB Bunch (Lanky)','CB Bunch (Chunky)','CB Bunch (Tiny)','CB Bunch (Diddy)','Blue Aura','Ice Maze','Rotating Room','Light + Barrier',_S,'Trapdoor',_AI,'Warp 5 Pad','Warp 3 Pad','Warp 4 Pad','Warp 2 Pad','Warp 1 Pad','Large Door','Library Door (Revolving?)','Blue Platform','White Platform','Wooden Platform','Wooden Bridge',_Y,_P,_E,'Large Metal Door','Rotating Chair','Baboon Balloon Pad (with platform)',_AJ,_AJ,_AI,'Large Breakable Wooden Door','Pineapple Switch (Rotating)',': Pad',_A9,'+ Pad',_W,_W,_W,_Q,_n,_n,_n,'Flotsam',_P,'Treasure Chest','Up Switch','Down Switch',_m,'Enguarde Door','Trash Can','Fluorescent Tube','Wooden Door Half','Stone Platform','Stone Panel','Stone Panel (Rotating)','Wrinkly Door Wheel',_Y,'Wooden Panel','Electricity Shields?','Unknown','Boulder Pad (Red)','Candelabra','Banana Peel','Skull+Candle','Metal Box','1 Switch','2 Switch','3 Switch','4 Switch','Metal Grate (Breakable?)','Pound The X Platform',_Y,'Chandelier','Bone Door',_N,'4 Door (5DS)','5 Door (5DS)','Door (Llama Temple)',_A3,_N,_P,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_Z,_Z,'K. Rool Ship Jaw Bottom','Blast-O-Matic Cover?','Blast-O-Matic Cover',_Q,'Platform',_AC,_k,_AK,_AK,_AL,_AL,'Skull Gate (Minecart)','Dogadon Arena Outer','Boxing Ring Corner (Red)','Boxing Ring Corner (Green)','Boxing Ring Corner (Blue)','Boxing Ring Corner (Yellow)','Lightning Rod','Green Electricity','Blast-O-Matic',_X,_o,_A,'Vine',"Director's Chair",_o,_o,'Boom Microphone','Auditions Sign','Banana Hoard',_Z,_Z,'Rareware GB',_A,_A,_A,_A,'Platform (Crystal Caves Minigame)','King Kut Out Arm (Bloopers)','Rareware Coin',_A5,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,'Rock',_k,_A,_A,_A,_Y,_A,_A,_A,'Nothing?','Troff n Scoff Portal','Level Entry/Exit','K. Lumsy Key Indicator?',_A,_A,_A,_A,_A,'Red Bell','Green Bell','Race Checkpoint']
trigger_types=['Unknown 0x00','Unknown 0x01','Unknown 0x02','Boss Door Trigger','Unknown 0x04','Cutscene Trigger','Unknown 0x06','Unknown 0x07','Unknown 0x08','Loading Zone (0x9)','Cutscene Trigger (0xA)','Unknown 0x0B','Loading Zone + Objects','Loading Zone (0xD)','Unknown 0x0E','Warp Trigger','Loading Zone (0x10)','Loading Zone (0x11)','Coin Shower Trigger','Detransform Trigger (0x13)','Boss Loading Zone','Autowalk Trigger','Sound Trigger','Cutscene Trigger (0x17)','Unknown 0x18','Unknown 0x19','Gravity Trigger','Slide Trigger','Unslide Trigger','Loading Zone (Zipper)','Song Trigger','Unknown 0x1F','Cutscene Trigger (0x20)','Unknown 0x21','Unknown 0x22','Unknown 0x23','Detransform Trigger (0x24)','Chunk Texture Load Trigger','K. Lumsy Code Activator']
relevant_pointer_tables=[{_C:1,_G:'Map Geometry',_H:'geometry.bin'},{_C:2,_G:'Map Walls',_H:'walls.bin'},{_C:3,_G:'Map Floors',_H:'floors.bin'},{_C:8,_G:'Map Cutscenes',_H:'cutscenes.bin'},{_C:9,_G:'Map Setups',_H:'setup.bin'},{_C:10,_G:'Map Data 0xA',_H:'map_0x0a.bin'},{_C:15,_G:_AM,_H:'paths.bin'},{_C:16,_G:_AM,_H:'character_spawners.bin'},{_C:18,_G:'Map Loading Zones',_H:'loading_zones.bin'},{_C:21,_G:'Map Data 0x15',_H:'map_0x15.bin'},{_C:23,_G:'Map Exits',_H:'exits.bin'}]
num_tables=32
pointer_tables=[]
pointer_table_offsets=[1055824,1063120,1063360,1735712]
main_pointer_table_offset=pointer_table_offsets[0]
folder_append=['_us','_pal','_jp','_kiosk']
setup_table_index=9
script_table_index=10
files={}
tab_indentation=0
folder_removal=[]
version=0
def getTriggerTypeName(index):
	'Convert Trigger type into a name string.';A=index
	if A<len(trigger_types)-1:return trigger_types[A]
	return'Type %s'%hex(A)
def getSongName(index):
	'Convert song index into name.';A=index
	if A<len(songs)-1:return songs[A]
	return'Song %s'%hex(A)
def getTOrF(value):
	'Get truthiness from value.'
	if value==0:return'False'
	return'True'
def getSetOrNot(value):
	'Get set or unset from value.'
	if value==0:return"Don't Set"
	return'Set'
def display(file,string):
	'Display function upon being passed a string.';A=string;global tab_indentation
	if A[-1:]!='{':
		if A[-1:]!=_B:A+=';'
	for B in range(tab_indentation):A='\t'+A
	if A[-1:]=='{':tab_indentation+=1
	elif A[-1:]==_B:tab_indentation-=1
	file.write(A+'\n')
def grabConditional(param_1,ScriptCommand,params,behaviour,param_3,file):
	'Convert conditional into series of C-like Functions.';V='if (%s >= FUN_80614A54(PlayerPointer)) {';U='if (%s < FUN_80614A54(PlayerPointer)) {';T='if (*(byte *)(behaviour + %s) >= %s) {';S='if (*(byte *)(behaviour + %s) < %s) {';R='if (x1C_svar6 >= %s) {';Q='if (x1C_svar6 < %s) {';P='x17_successful = 1';O='if (true) {';N='xA_successful = 0';K=ScriptCommand;J='while (true) {';I='!';H='if (1 == 0) {';G='if (player_count != 0) {';B=params;A=file;C=K&32767;F=K&32768;D='';E=I
	if F!=0:F=1;D=I;E=''
	else:D='';E=I
	if C==0:display(A,'if (%strue) {'%D)
	elif C==1:display(A,'if (*(byte *)(behaviour + %s) %s== %s) {'%(hex(B[1]+72),D,str(B[0])))
	elif C==2:display(A,'x2_successful = 0');display(A,'x2_focusedPlayerNumber = 0');display(A,G);display(A,_L);display(A,'x2_focusedPlayerNumber_ = x2_focusedPlayerNumber');display(A,'x2_focusedPlayerNumber = (x2_focusedPlayerNumber_ + 1) & 0xFF');display(A,'if (*(byte *)(character_change_pointer[x2_focusedPlayerNumber_]->does_player_exist) != 0) {');display(A,'x2_focusedPlayerPointer = *(int *)(character_change_pointer[x2_focusedPlayerNumber_)]->character_pointer)');display(A,'if (*(byte *)(x2_focusedPlayerPointer->locked_to_pad) == 1) {');display(A,'if (this->id == *(short *)(x2_focusedPlayerPointer->standingOnObjectM2Index)) {');display(A,'x2_successful = 1');display(A,_B);display(A,_B);display(A,_B);display(A,'} while (x2_focusedPlayerNumber < player_count)');display(A,_B);display(A,'if (x2_successful %s== 1) {'%D)
	elif C==3:display(A,H)
	elif C==4:display(A,'if (*(ushort *)(behaviour + %s) %s== %s) {'%(hex(B[1]*2+68),D,str(B[0])))
	elif C==5:display(A,'if (FUN_806425FC(%s,%s) %s== 0) {'%(str(B[0]),str(B[1]),E))
	elif C==6:display(A,'if (*(code *)(%s)(behaviour,this->id,%s,%s) %s== 0) {'%(hex(2155118664+B[0]*4),str(B[1]),str(B[2]),E))
	elif C==7:display(A,'if (FUN_80642500(behaviour + 0x14,%s,%s) %s== 0) {'%(str(B[0]),str(B[1]),E))
	elif C==8:display(A,'if (*(byte *)(behaviour + 0x51) %s== 0) {'%E)
	elif C==9:display(A,'if (*(byte *)(behaviour + 0x52) %s== 0) {'%E)
	elif C==10:display(A,N);display(A,'xA_focusedPlayerNumber = 0');display(A,G);display(A,_L);display(A,'xA_focusedPlayerNumber_ = xA_focusedPlayerNumber');display(A,'xA_focusedPlayerNumber = (xA_focusedPlayerNumber_ + 1) & 0xFF');display(A,'if (*(byte *)(character_change_pointer[xA_focusedPlayerNumber_]->does_player_exist) != 0) {');display(A,'xA_focusedPlayerPointer = *(int *)(character_change_pointer[xA_focusedPlayerNumber_]->character_pointer)');display(A,N);display(A,'if (*(byte *)(xA_focusedPlayerPointer->locked_to_pad) == 2) {');display(A,'if (this->id == *(short *)(xA_focusedPlayerPointer->standingOnObjectM2Index)) {');display(A,'xA_successful = 1');display(A,_B);display(A,_B);display(A,_B);display(A,'} while (xA_focusedPlayerNumber < player_count)');display(A,_B);display(A,'if (xA_successful %s== 1) {'%D)
	elif C==11:display(A,'xB_successful = 0');display(A,'xB_focusedPlayerNumber = 0');display(A,G);display(A,_L);display(A,'xB_focusedPlayerNumber_ = xB_focusedPlayerNumber');display(A,'xB_focusedPlayerNumber = (xB_focusedPlayerNumber_ + 1) & 0xFF');display(A,'if (*(byte *)(character_change_pointer[xB_focusedPlayerNumber_]->does_player_exist) != 0) {');display(A,'xB_focusedPlayerPointer = *(int *)(character_change_pointer[xB_focusedPlayerNumber_]->character_pointer)');display(A,'if (*(byte *)(xB_focusedPlayerPointer->locked_to_pad) == 3) {');display(A,'if (*(byte *)(xB_focusedPlayerPointer->unk0x12F == %s)) {'%str(B[0]));display(A,'if (this->id == *(short *)(xB_focusedPlayerPointer->standingOnObjectM2Index)) {');display(A,'xB_successful = 1');display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,'} while (xB_focusedPlayerNumber < player_count)');display(A,_B);display(A,'if (xB_successful %s== 1) {'%D)
	elif C==12:display(A,'if (%s(((((FLOAT_807F621C == FLOAT_807F61FC) && (FLOAT_807F6220 == 1729.11706543)) && ((FLOAT_807F6224 == 3433.54956055 && ((FLOAT_807F6228 == 330 && (FLOAT_807F622C == 170)))))) && (FLOAT_807F6230 == 0)) && (FLOAT_807F6234 == 1))) {'%E)
	elif C==13:display(A,'xC_successful = 0');display(A,'xC_focusedPlayerNumber = 0');display(A,G);display(A,_L);display(A,'xC_focusedPlayerNumber_ = xC_focusedPlayerNumber');display(A,'xC_focusedPlayerNumber = (xC_focusedPlayerNumber_ + 1) & 0xFF');display(A,'if (*(byte *)(character_change_pointer[xC_focusedPlayerNumber_]->does_player_exist) != 0) {');display(A,'xC_focusedPlayerPointer = *(int *)(character_change_pointer[xC_focusedPlayerNumber_]->character_pointer)');display(A,'if (*(byte *)(xC_focusedPlayerPointer->locked_to_pad) == 1) {');display(A,'if (this->id == *(short *)(xC_focusedPlayerPointer->standingOnObjectM2Index)) {');display(A,'if (this->id == *(byte *)(xC_focusedPlayerPointer->unk0x10E == %s)) {'%str(B[0]));display(A,'xC_successful = 1');display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,'} while (xC_focusedPlayerNumber < player_count)');display(A,_B);display(A,'if (xC_successful %s== 1) {'%D)
	elif C==14:display(A,'if (FUN_80641F70(param_1,%s) %s== 0) {'%(str(B[0]),E))
	elif C==15:display(A,'if (FUN_80723C98(*(word *) (behaviour + 0x38)) %s== 0) {'%E)
	elif C==16:
		L='';M=''
		if B[1]!=-1:L='(*(byte *)(behaviour + 0x5C) != %s) || '%str(B[1])
		if B[0]!=0:M='(FUN_8067ACC0(*(ushort *)(behaviour + 0x5E)) & %s)'%str(B[0]);display(A,'if ((((*(byte *)(behaviour + 0x5C) == 0) || %s%s)) || (canHitSwitch() == 0)) {'%(L,M));display(A,'x10_uvar9 = 0');display(A,'} else {');display(A,'FUN_80641724(ObjectModel2ArrayPointer[id2index(this->id)].object_type)');display(A,'x10_uvar9 = 1');display(A,_B);display(A,'if (x10_uvar9 %s== 1) {'%D)
		elif F==1:display(A,O)
		else:display(A,H)
	elif C==17:display(A,'x11_successful = false');display(A,_T);display(A,'x11_focusedArraySlot = &loadedActorArray');display(A,'x11_focusedActor = loadedActorArray');display(A,J);display(A,'x11_focusedArraySlot = x11_focusedArraySlot + 8');display(A,'if ((*(uint *)(x11_focusedActor->object_properties_bitfield) & 0x2000) == 0) {');display(A,'if (*(int *)(x11_focusedActor->actor_type) == %s) {'%str(B[0]));display(A,'if (x11_focusedActor->locked_to_pad == 1) {');display(A,'if (this->id == *(short *)(x11_focusedActor->standingOnObjectM2Index)) {');display(A,'x11_successful = true');display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,'if ((&loadedActorArray + (loadedActorCount * 8) <= x11_focusedArraySlot) || (x11_successful)) break;');display(A,_B);display(A,_B);display(A,'if (%sx11_successful) {'%D)
	elif C==18:display(A,'x12_successful = false');display(A,_T);display(A,'x12_focusedArraySlot = &loadedActorArray');display(A,'x12_focusedActor = loadedActorArray');display(A,J);display(A,'x12_focusedArraySlot = x12_focusedArraySlot + 8');display(A,'if ((*(uint *)(x12_focusedActor->object_properties_bitfield) & 0x2000) == 0) {');display(A,'if (*(int *)(x12_focusedActor->actor_type) == %s) {'%str(B[0]));display(A,'if (x12_focusedActor->locked_to_pad == 1) {');display(A,'if (this->id == *(short *)(x12_focusedActor->standingOnObjectM2Index)) {');display(A,'if (*(short *)(x12_focusedActor->unk10E) == %s) {'%str(B[1]));display(A,'x12_successful = true');display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,'if ((&loadedActorArray + (loadedActorCount * 8) <= x12_focusedArraySlot) || (x12_successful)) break;');display(A,'x12_focusedActor = *x12_focusedArraySlot');display(A,_B);display(A,_B);display(A,'if (%sx12_successful) {'%D)
	elif C==19:display(A,'if (isPlayerWithinDistanceOfObject(%s) %s== 0) {'%(str(B[0]),E))
	elif C==20:display(A,'x14_successful_count = 0');display(A,'x14_focusedArraySlot = &loadedActorArray');display(A,_T);display(A,'x14_focusedActor = loadedActorArray');display(A,J);display(A,'x14_focusedArraySlot = x14_focusedArraySlot + 8');display(A,'if ((*(uint *)(x14_focusedActor->object_properties_bitfield) & 0x2000) == 0) {');display(A,'if (*(int *)(x14_focusedActor->actor_type) == %s) {'%str(B[0]));display(A,'if (x14_focusedActor->locked_to_pad == 1) {');display(A,'if (this->id == *(short *)(x14_focusedActor->standingOnObjectM2Index)) {');display(A,'if (*(short *)(x14_focusedActor->unk10E) == %s) {'%str(B[1]));display(A,'x14_successful_count = true');display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,'if ((&loadedActorArray + (loadedActorCount * 8) <= x14_focusedArraySlot)) break;');display(A,'x14_focusedActor = *x14_focusedArraySlot');display(A,_B);display(A,_B);display(A,'if (x14_successful_count %s== %s) {'%(D,str(B[2])))
	elif C==21:display(A,'if (FUN_80650D04(this->id,%s) %s== 0) {'%(str(B[0]),E))
	elif C==22:display(A,'if ((LevelStateBitfield & %s) != 0) {'%hex(B[0]*65536+B[1]))
	elif C==23:
		display(A,'x17_successful = 0');display(A,'x17_focusedPlayerNumber = 0');display(A,G);display(A,_L);display(A,'x17_focusedPlayerNumber_ = x17_focusedPlayerNumber');display(A,'x17_focusedPlayerNumber = (x17_focusedPlayerNumber_ + 1) & 0xFF');display(A,'if (*(byte *)(character_change_pointer[x17_focusedPlayerNumber_]->does_player_exist) != 0) {');display(A,'x17_focusedPlayerPointer = *(int *)(character_change_pointer[x17_focusedPlayerNumber_]->character_pointer)');display(A,'if (*(byte *)(x17_focusedPlayerPointer->control_state) == %s) {'%str(B[0]))
		if B[1]==0:display(A,P)
		else:display(A,'if (x17_focusedPlayerPointer->control_state_progress == %s) {'%str(B[1]));display(A,P);display(A,_B)
		display(A,_B);display(A,_B);display(A,'} while (x17_focusedPlayerNumber < player_count)');display(A,_B);display(A,'if (x17_successful %s== 1) {'%D)
	elif C==24:
		display(A,'x18_successful = 0');display(A,'if (*(byte *)(behaviour + 0x5C) != 0) {')
		if B[1]!=-1:display(A,'if (*(byte *)(behaviour + 0x5C) == %s){'%str(B[1]))
		display(A,'if ((*(ushort *)(behaviour + 0x5E) == %s) && canHitSwitch() != 0) {'%str(B[0]));display(A,'FUN_80641724(ObjectModel2Array[id2index(this->id)].object_type)');display(A,'x18_successful = 1');display(A,_B)
		if B[1]!=-1:display(A,_B)
		display(A,_B);display(A,'if (x18_successful %s== 1) {'%D)
	elif C==25:display(A,'if (*(int *)(PlayerPointer->ActorType) %s== %s) {'%(D,str(B[0])))
	elif C==26:display(A,'if (*(byte *)(character_change_pointer->unk0x2C0) %s== %s) {'%(D,str(B[0])))
	elif C==27:display(A,'if (*(byte *)(character_change_pointer->unk0x2C1) %s== 0){'%E)
	elif C==28:
		display(A,'x1C_svar6 = 80650a70()')
		if B[1]==0:
			if F==0:display(A,Q%str(B[2]))
			else:display(A,R%str(B[2]))
		elif B[1]==1:
			if F==0:display(A,R%str(B[2]))
			else:display(A,Q%str(B[2]))
		else:display(A,H)
	elif C==29:
		if B[0]==0:
			if F==0:display(A,S%(hex(72+B[2]),str(B[1])))
			else:display(A,T%(hex(72+B[2]),str(B[1])))
		elif B[0]==1:
			if F==0:display(A,T%(hex(72+B[2]),str(B[1])))
			else:display(A,S%(hex(72+B[2]),str(B[1])))
		else:display(A,H)
	elif C==30:display(A,'if ((FUN_80726D7C() & 0xFF) %s== 0){'%E)
	elif C==31:
		if F==0:display(A,H)
		else:display(A,O)
	elif C==32:display(A,'if ((FUN_806422D8() & 0xFF) %s== 0){'%E)
	elif C==33:display(A,'x21_successful = 0');display(A,'x21_focusedPlayerNumber = 0');display(A,G);display(A,_L);display(A,'x21_focusedPlayerNumber_ = x21_focusedPlayerNumber');display(A,'x21_focusedPlayerNumber = (x21_focusedPlayerNumber_ + 1) & 0xFF');display(A,'if (*(byte *)(character_change_pointer[x21_focusedPlayerNumber_]->does_player_exist) != 0) {');display(A,'x21_focusedPlayerPointer = *(int *)(character_change_pointer[x21_focusedPlayerNumber_]->character_pointer)');display(A,'if (*(byte *)(x21_focusedPlayerPointer->control_state_progress) == %s) {'%str(B[0]));display(A,'x21_successful = 1');display(A,_B);display(A,_B);display(A,_B);display(A,_B);display(A,'if (x21_successful %s== 1) {'%D)
	elif C==34:display(A,'if (touchingModelTwoById(%s) %s== 0) {'%(hex(B[0]),E))
	elif C==35:display(A,'if (CutsceneActive %s== 1) {'%D)
	elif C==36:display(A,'x24_focusedActor = getSpawnerTiedActor(%s,0)'%str(B[0]));display(A,'if (*(byte *)(x24_focusedActor->control_state) %s== %s) {'%(D,str(B[1])))
	elif C==37:display(A,'if (%s(*(byte *)CurrentCollectableBase->SlamLvl => %s)) {'%(D,str(B[0])))
	elif C==38:display(A,'if ((*(uint *)(PlayerPointer->unk0x368) & %s) %s== 0) {'%(hex(B[0]*65536+B[1]),E))
	elif C==39:display(A,'if ((*(uint *)(PlayerPointer->effectBitfield) & %s) %s== 0) {'%(hex(B[0]*65536+B[1]),E))
	elif C==40:display(A,'if ((*(byte *)(behaviour + 0x9A) & 1) %s== 0) {'%D)
	elif C==41:display(A,'if (notTouchingActorSpawnerWithinRan(%s,%s,%s) %s== 0) {'%(str(B[0]),str(B[1]),str(B[2]),E))
	elif C==42:
		if F==0:display(A,'if (BYTE_807F61F8 != 0 || *(byte *)(PTR_0x807F61F0->control_state) == 5) {')
		else:display(A,'if (BYTE_807F61F8 == 0 && *(byte *)(PTR_0x807F61F0->control_state) != 5) {')
	elif C==43:display(A,'if (BYTE_807F61F8 %s== 0) {'%E)
	elif C==44:display(A,'if (FUN_80689BAC(%s) %s== 0) {'%(str(B[0]),E))
	elif C==45:display(A,"if (checkFlag(%s>%s,'Permanent') %s== 0) {"%(hex(math.floor(B[0]/8)),str(B[0]%8),E))
	elif C==46:display(A,"if (getAndSetActorSpawnerControlStateFromActorSpawnerID(%s,0,'%s') %s== %s) {"%(str(B[0]),getSetOrNot(0),D,str(B[1])))
	elif C==47:display(A,'if ((isCharacterSpawnerInState7(%s) & 0xFF) %s== 0) {'%(str(B[0]&255),E))
	elif C==48:display(A,'if (*(byte *)(PlayerPointer->unk0xD1) %s== %s) {'%(D,str(B[0])))
	elif C==49:display(A,'x31_ivar10_4 = id2index(&WORD_807F6240[%s])'%str(B[0]));display(A,'if (ObjectModel2ArrayPointer[x31_ivar10_4]->behaviour_pointer[%s] %s== %s) {'%(hex(72+B[2]),D,str(B[1])))
	elif C==50:display(A,'if (*(ushort *)PreviousMap %s== %s) {'%(D,str(B[0])))
	elif C==51:
		if B[0]==0:
			if F==0:display(A,U%str(B[1]))
			else:display(A,V%str(B[1]))
		elif B[0]==1:
			if F==0:display(A,V%str(B[1]))
			else:display(A,U%str(B[1]))
		else:display(A,H)
	elif C==52:
		display(A,'x34_uvar4 == FUN_806C8D2C(%s)'%str(B[0]))
		if F==0:display(A,'if (%s <= &character_collectable_base[(BYTE_807FC929 * 0x5E) + (0x306 * x34_uvar4)] {'%str(B[1]))
		else:display(A,'if (%s > &character_collectable_base[(BYTE_807FC929 * 0x5E) + (0x306 * x34_uvar4)] {'%str(B[1]))
	elif C==53:display(A,'if (*(byte *)PlayerPointer->0xD0 %s== %s) {'%(D,str(B[0])))
	elif C==54:display(A,"if (checkFlag(%s>%s,'Temporary') %s== 0) {"%(hex(math.floor(B[0]/8)),str(B[0]%8),E))
	elif C==55:display(A,'FUN_80650D8C(this->id,%s,austack30,austack36)'%str(B[0]));display(A,'if (austack30[0] %s== %s) {'%(D,str(B[1])))
	elif C==56:display(A,'if (%s(*(byte *)Character < 5)) {'%D)
	elif C==57:display(A,'if ((%s& *(ushort *)PlayerPointer->CollisionQueue->TypeBitfield) %s== 0) {'%(str(B[0]),E))
	elif C==58:display(A,'if (((1 << %s) & BYTE_807F693E) %s== 0) {'%(str(B[0]),E))
	elif C==59:display(A,"if (checkFlag(%s>%s,'Global') %s== 0) {"%(hex(math.floor(B[0]/8)),str(B[0]%8),E))
	elif C==60:display(A,'if (PlayerPointer->chunk %s== %s) {'%(D,str(B[0])))
	elif C==61:display(A,'if (BYTE_807F6903 %s== 0) {'%E)
	else:display(A,'if ([%s,%s,%s,%s]) {'%(str(C),str(B[0]),str(B[1]),str(B[2])))
def grabExecution(param_1,ScriptCommand,params,behaviour,param_3,file):
	'Convert execution into a series of C-Like lines.';W='if (x8d_ivar6 == 0) {';V='FUN_806CF398(PlayerPointer)';U='if (BYTE_807F61F8 != 0) {';T='InitMapChange_TransferredActor(%s,%s,0,0)';S='FUN_806335B0((&WORD_807F6240)[%s],1,%s)';R='if ((&WORD_807F6240)[%s] != -1) {';Q='*(short *)(behaviour + %s) = FUN_80605044(this->id,%s,%s,%s)';P='if (*(short *)(behaviour + %s) < 0) {';O='FUN_80642844(%s,%s,behaviour)';I='else {';B=params;A=file;C=ScriptCommand
	if C==0:display(A,'FUN_80642748(%s,%s,%s)'%(str(B[0]),str(B[1]),str(behaviour)))
	elif C==1:display(A,'*(byte *)(behaviour + %s) = %s'%(hex(B[1]+75),str(B[0])))
	elif C==2:display(A,'FUN_80723284(*(int*)(behaviour + 0x38),%s)'%str(B[0]))
	elif C==3:
		if B[0]==0:display(A,'*(short *)(behaviour + %s) = %s'%(hex(B[2]*2+68),str(B[1])))
		else:display(A,'*(short *)(behaviour + %s) = *(short *)(behaviour + %s)'%(hex(B[2]*2+68),hex(B[1]*4+20)))
	elif C==4:display(A,'FUN_80723484(*(int *)(behaviour + 0x38))');display(A,'FUN_807238D4(*(int *)(behaviour + 0x38),0x807F621C,0x807F6220,0x807F6224)')
	elif C==5:display(A,'FUN_806418E8(%s,%s,behaviour)'%(str(B[0]),str(B[1])))
	elif C==6:display(A,'*(float *)(behaviour + %s) = %s'%(hex(B[0]*4+20),str(B[1]/10)))
	elif C==7:display(A,'*(code *)(%s)(behaviour,this->id,%s,%s)'%(hex(2155118192+B[0]*4),str(B[1]),str(B[2])))
	elif C==8:display(A,O%(str(B[0]),str(B[1])))
	elif C==9:display(A,'if ((FLOAT_807F621C != FLOAT_807F61FC) || (FLOAT_807F6224 != 3433.54956055)) {');display(A,'FUN_80642480(%s)'%str(B[0]));display(A,_B)
	elif C==10:display(A,'*(byte *)(behaviour + 0x50) = %s'%str(B[0]));display(A,'*(float *)(behaviour + 0x78) = %s'%str(B[1]/100));display(A,'*(float *)(behaviour + 0x7C) = %s'%str(B[2]/100))
	elif C==11:display(A,'*(short *)(behaviour + 0x80) = %s'%str(B[0]));display(A,'*(short *)(behaviour + 0x82) = %s'%str(B[1]))
	elif C==12:display(A,'*(short *)(behaviour + 0x84) = %s'%str(B[0]));display(A,'*(short *)(behaviour + 0x86) = %s'%str(B[1]))
	elif C==13:display(A,'*(short *)(behaviour + 0x88) = %s'%str(B[0]));display(A,'*(short *)(behaviour + 0x8A) = %s'%str(B[1]))
	elif C==14:display(A,P%hex((B[0]&1)*2+16));display(A,Q%(hex((B[0]&1)*2+16),str(B[0]),str(B[2]&127),str(B[1]&2)));display(A,_B)
	elif C==15:
		D=B[1]
		if B[1]<0:D=D+127
		J=D>>7&255;K=J;D=B[2]
		if B[2]<0:D=D+127
		H=D>>7&255
		if J==0:K=127
		if H==0:H=255
		display(A,'FUN_806085DC(this->id,%s,%s,%s)'%(str(B[0]),str(H),str(K)))
	elif C==16:display(A,'x10_temp = *(short *)(behaviour + %s)'%hex(B[1]*2+16));display(A,'if (-1 < x10_temp) {');display(A,'FUN_80605380(x10_temp)');display(A,'*(short *)(behaviour + %s) = 0xFFFF'%hex(B[1]*2+16));display(A,_B)
	elif C==17:display(A,'FUN_806508B4(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==18:display(A,'FUN_8065092C(this->id,%s)'%str(B[0]))
	elif C==19:display(A,'FUN_80650998(this->id,%s)'%str(B[0]))
	elif C==20:display(A,'FUN_80650A04(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==21:display(A,'FUN_80650b50(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==22:display(A,'FUN_80650BBC(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==23:display(A,'FUN_80650C28(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==24:display(A,'FUN_80650C98(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==25:display(A,'setCharacterChangeParameters(%s,0,0)'%str(B[0]))
	elif C==26:display(A,'FUN_80650AD8(this->id,%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2]/100)))
	elif C==27:display(A,R%str(B[0]));display(A,S%(str(B[0]),str(B[1])));display(A,_B)
	elif C==28:display(A,'if ((&WORD_807F6240)[id2index(%s)] != -1) {'%str(B[0]));display(A,'x1C_ivar7 = (&WORD_807F6240)[%s]'%str(B[0]));display(A,'if ((x1C_ivar7 != -1) && (ObjectModel2ArrayPointer[x1C_ivar7].behaviour != 0)) {');display(A,'x1C_puvar10 = ObjectModel2ArrayPointer[x1C_ivar7].behaviour + %s'%str(B[1]));display(A,'x1C_puvar10[0x48] = x1C_puvar10[0x48] + %s'%str(B[2]));display(A,_B);display(A,_B)
	elif C==29:display(A,O%(str(B[0]),str(B[1])))
	elif C==30:display(A,'FUN_80642748(%s,%s,behaviour)'%(str(B[0]),str(B[1])))
	elif C==31:display(A,'FUN_807232EC(*(int *)(behaviour + 0x38),%s)'%str(B[0]))
	elif C==32:display(A,'FUN_80723380(*(int *)(behaviour + 0x38),%s)'%str(B[0]))
	elif C==33:display(A,'FUN_80723320(*(int *)(behaviour + 0x38),%s)'%str(B[0]))
	elif C==34:display(A,'*(int *)(behaviour + 0x38) = FUN_80723020(FLOAT_807F6220,FLOAT_807F6224,%s)'%str(B[2]))
	elif C==35:display(A,'FUN_80723428(*(int *)(behaviour + 0x38))');display(A,'*(int *)(behaviour + 0x38) = 0xFFFFFFFF')
	elif C==36:display(A,'FUN_8072334C(*(int *)(behaviour + 0x38),%s)'%str(B[0]))
	elif C==37:display(A,'playCutsceneFromModelTwoScript(behaviour,%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==38:display(A,'FUN_8064199C(behaviour,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==39:display(A,'FUN_80634EA4(this->id,%s,%s)'%(str(B[0]),str(B[1]&255)))
	elif C==40:display(A,'FUN_80635018(this->id,%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==41:display(A,'FUN_8061EF4C(0x29,PlayerPointer->unk0x27C,%s,%s,FLOAT_807F621C)'%(str(B[0]&255),str(B[1])))
	elif C==42:display(A,'ObjectModel2ArrayPointer[id2Index(this->id)]->unk0x3C = %s'%str(B[0]))
	elif C==43:display(A,'FUN_80636014(this->id,1)')
	elif C==44:display(A,'FUN_806335B0(this->id,1,%s')%str(B[0]);display(A,'FUN_8067A9F0(0,PlayerPointer)')
	elif C==45:
		display(A,'x2d_counter = 0');display(A,'x2d_PTR_focusedLoadedActor = &PTR_DAT_807FB930');display(A,_T);display(A,_L);display(A,'x2d_ADDR_focusedLoadedActor = *x2d_PTR_focusedLoadedActor');display(A,'x2d_counter = x2d_counter + 1');display(A,'if ((*(uint *)(x2d_ADDR_focusedLoadedActor->object_properties_bitfield_1) & 0x2000) == 0) {');display(A,'if (x2d_ADDR_focusedLoadedActor->locked_to_pad == 0x1) {');display(A,'if (this->id == *(word *)(x2d_ADDR_focusedLoadedActor->unk0x10C)) {')
		if B[0]==0:display(A,'*(ushort *)(x2d_ADDR_focusedLoadedActor->unk0x68) = *(ushort *)(x2d_ADDR_focusedLoadedActor->unk0x68) & 0xFFFB')
		else:display(A,'*(ushort *)(x2d_ADDR_focusedLoadedActor->unk0x68) = *(ushort *)(x2d_ADDR_focusedLoadedActor->unk0x68) | 4')
		display(A,_B);display(A,_B);display(A,_B);display(A,'x2d_PTR_focusedLoadedActor = x2d_PTR_focusedLoadedActor + 8');display(A,'x2d_finishedArray = x2d_counter < loadedActorCount');display(A,'} while(x2d_finishedArray)');display(A,_B)
	elif C==46:display(A,'FUN_80651BC0(%s,%s)'%(str(B[0]),str(B[1])))
	elif C==47:display(A,'FUN_8060B49C(PlayerPointer,%s)'%str(B[0]))
	elif C==48:display(A,'InitMapChange(%s,0)'%str(B[0]))
	elif C==49:
		if B[2]&256!=0:display(A,'SetIntroStoryPlaying(2)');display(A,"setNextTransitionType('Fade (Wrong Cutscene)')")
		if B[2]&255==0:display(A,T%(str(B[0]),str(B[1])))
		elif B[2]&255==1:display(A,'InitMapChange_TransferredActor(%s,%s,0,1)'%(str(B[0]),str(B[1])))
		elif B[2]&255==2:display(A,'InitMapChange_TransferredActor(%s,%s,0,3)'%(str(B[0]),str(B[1])))
		else:display(A,T%(str(B[0]),str(B[1])))
	elif C==50:display(A,'InitMapChange_ParentMap(%s,%s)'%(str(B[0]),str(B[1])))
	elif C==51:display(A,'FUN_8062B86C(%s,(float)%s,(float)%s)'%(str(B[0]),str(B[1]),str(B[2]/100)))
	elif C==52:display(A,'FUN_8062B8A4(%s,(float)%s,(float)%s)'%(str(B[0]),str(B[1]),str(B[2]/100)))
	elif C==53:display(A,'FUN_80641C98(%s,%s,this->id)'%(str(B[0]),str(B[1])))
	elif C==54:display(A,'FUN_80641BCC(%s,%s,this->id)'%(str(B[0]),str(B[1])))
	elif C==55:display(A,'FUN_80679200(PlayerPointer,0,0x400000,%s)'%str(B[0]&255))
	elif C==56:display(A,'FUN_80651be0(%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==57:display(A,'*(byte *)(behaviour + 0x4F) = %s'%str(B[0]))
	elif C==58:display(A,'// Execution Type 0x3A stripped from final. Parameters: %s, %s, %s'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==59:display(A,'*(uint *)(PlayerPointer->unk0x368) = *(uint *)(PlayerPointer->unk0x368) & ~%s'%hex(B[0]*65536+B[1]))
	elif C==60:display(A,'if (*(int *)(behaviour + 0x94) != 0) {');display(A,'FUN_806782C0(*(int *)(behaviour + 0x94))');display(A,'*(int *)(behaviour + 0x94) = 0');display(A,_B)
	elif C==61:display(A,'*(byte *)(behaviour + 0x67) = %s'%str(B[0]))
	elif C==62:display(A,'*(byte *)(behaviour + 0x6F) = %s'%str(B[0]))
	elif C==63:display(A,'*(byte *)(behaviour + 0x6E) = %s'%str(B[0]))
	elif C==64:display(A,'*(int *)LevelStateBitfield = *(int *)LevelStateBitfield | %s'%hex(B[0]*65536+B[1]))
	elif C==65:display(A,'WORD_807F6904 = 1')
	elif C==66:display(A,'FUN_80634CC8(this->id,%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==67:display(A,'if (%s == 1) {'%str(B[0]));display(A,'*(int *)(behaviour + 0x8) = *(int *)(behaviour + %s)'%hex(B[1]*4+20));display(A,'*(int *)(behaviour + 0xC) = *(int *)(behaviour + %s)'%hex(B[2]*4+20));display(A,_B);display(A,I);display(A,'*(float *)(behaviour + 0x8) = %s'%str(B[1]/10));display(A,'*(float *)(behaviour + 0xC) = %s'%str(B[2]/10));display(A,_B)
	elif C==68:display(A,'WORD_807F6906 = %s'%str(B[0]));display(A,'WORD_807F6908 = %s'%str(B[1]))
	elif C==69:display(A,'*(byte *)(behaviour + 0x60) = %s'%str(B[0]));display(A,'*(ushort *)(behaviour + 0x62) = %s'%str(B[1]));display(A,'*(byte *)(behaviour + 0x66) = %s'%str(B[2]))
	elif C==70:display(A,'*(byte *)(behaviour + 0x70) = %s'%str(B[0]))
	elif C==71:display(A,'*(byte *)(behaviour + 0x71) = %s'%str(B[0]))
	elif C==72:display(A,'FUN_80604BE8(*(byte *)(behaviour + %s,%s,%s)'%(hex(B[0]*2+17),str(B[1]/100),str(B[2])))
	elif C==73:display(A,'FUN_8067ABC0(%s,FLOAT_807F621C,FLOAT_807F6220,FLOAT_807F6224)'%str(B[2]))
	elif C==74:display(A,'FUN_8063393C(this->id,1,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==75:display(A,'FUN_8072ED9C(this->id,%s,%s)'%(str(B[0]),str(B[1])))
	elif C==76:display(A,'x4C_temp = FUN_80650A70()');display(A,'x4C_temp = (x4C_temp + %s)'%hex(B[1]));display(A,'if (x4C_temp < 0) {');display(A,'x4C_temp = 0');display(A,_B);display(A,'FUN_80650A04(this->id,%s,x4C_temp)'%str(B[0]))
	elif C==77:
		display(A,'x4D_svar12 = SpawnModelTwoObject(0,%s,FLOAT_807F690C,FLOAT_807F6910,FLOAT_807F6914)'%str(B[0]))
		if B[1]==0:display(A,'FUN_80641B00(x4D_svar12,this->id,%s)'%str(B[2]))
		end
	elif C==78:display(A,'FUN_807146A4(%s)'%str(B[0]));display(A,'FUN_807149B8(1)');display(A,'FUN_80714B84(0)')
	elif C==79:
		display(A,'if (BYTE_807F6938 != 0x10) {')
		if B[0]==-2:display(A,'(&WORD_807F6918)[BYTE_807F6938] = ObjectModel2ArrayPointer[id2index(this->id)]->id')
		else:display(A,'(&WORD_807F6918)[BYTE_807F6938] = %s'%str(B[0]))
		display(A,'BYTE_807F6938 = BYTE_807F6938 + 1')
	elif C==80:display(A,R%str(B[0]));display(A,S%(str(B[0]),str(B[1])));display(A,_B)
	elif C==81:display(A,'FUN_806F4F50(this->id,FLOAT_807F621C,FLOAT_807F6220,FLOAT_807F6224)')
	elif C==82:display(A,'// Execution Type 0x52 stripped from final. Parameters: %s,%s,%s'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==83:display(A,'// Execution Type 0x53 stripped from final. Parameters: %s,%s,%s'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==84:display(A,'x54_ivar7 = id2index((&WORD_807F6240)[%s])'%str(B[0]));display(A,'if (x54_ivar7 != -1) {');display(A,'FUN_8064199C(ObjectModel2ArrayPointer[x54_ivar7].behaviour,%s,%s)'%(str(B[1]),str(B[2])));display(A,_B)
	elif C==85:display(A,'FUN_8062B630(%s,%s)'%(str(B[0]),str(B[1])))
	elif C==86:display(A,'FUN_80724994(1,%s,0,0)'%str(B[0]))
	elif C==87:display(A,'FUN_80659620(&uStack52,&uStack56,&uStack60,WORD_807F693A)');display(A,'FUN_80659670(%s + fStack32, %s + fStack56,extraout_a0,extraout_a1, %s + fStack60, WORD_807F693A)'%(str(B[0]/1000),str(B[1]/1000),str(B[0]/1000)))
	elif C==88:display(A,'x58_temp = FUN_805FFE50(%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])));display(A,'if (x58_temp == 0) {');display(A,'FUN_8063DB3C(%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])));display(A,_B)
	elif C==89:display(A,'FUN_80724994(3,%s,%s,0)'%(str(B[0]),str(B[1])))
	elif C==90:display(A,'*(ushort *)(behaviour + 0x68) = %s'%str(B[0]));display(A,'*(ushort *)(behaviour + 0x6A) = %s'%str(B[1]));display(A,'*(ushort *)(behaviour + 0x6C) = %s'%str(B[2]))
	elif C==91:display(A,'FUN_806C92C4(%s)'%str(B[0]))
	elif C==92:display(A,'FUN_80724A9C(%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==93:display(A,'setNextTransitionType(%s)'%str(B[0]))
	elif C==94:display(A,'FUN_80641874()')
	elif C==95:display(A,'*(uint *)(PlayerPointer->ExtraInfo->unk0x1F0) = *(uint *)(PlayerPointer->ExtraInfo->unk0x1F0 | %s'%hex(B[0]*65536+B[1]))
	elif C==96:display(A,'FUN_8065F134()')
	elif C==97:
		if B[2]==0:display(A,"playSong('%s', 1)"%getSongName(B[0]))
		else:display(A,"playSong('%s', %s)"%(getSongName(B[0]),str(B[2]/255)))
	elif C==98:display(A,'WORD_807F693A = %s'%str(B[0]))
	elif C==99:display(A,'FUN_8068B830()')
	elif C==100:display(A,'FUN_8068B8FC()')
	elif C==101:display(A,'*(byte *)(behaviour + %s) = (byte *)(behaviour + %s) + %s'%(hex(B[1]+75),hex(B[1]+75),str(B[0])))
	elif C==102:display(A,'if (BYTE_807F61F8 == 0) {');display(A,'spawnActor(TimerController)');display(A,'temp = CurrentActorPointer');display(A,'WORD_807F61F4 = PTR_PTR_807FBB44');display(A,'CurrentActorPointer = mainmemory.read_u32_be(0x7FBB44)');display(A,'spawnTimer(0xDC,0x2A,%s)'%str(B[0]));display(A,'BYTE_807F61F8 = 1');display(A,'WORD_807F61F0 = PTR_PTR_807FBB44');display(A,'CurrentActorPointer = temp');display(A,_B)
	elif C==103:display(A,U);display(A,'FUN_806A2B08()');display(A,_B)
	elif C==104:display(A,U);display(A,'FUN_806782C0(DWORD_807F61F0)');display(A,'FUN_806782C0(DWORD_807F61F4)');display(A,_B)
	elif C==105:display(A,'FUN_80661398()')
	elif C==106:display(A,'FUN_806613E8(%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2]/100)))
	elif C==107:display(A,"setFlag(%s>%s,%s,'Permanent')"%(hex(math.floor(B[0]/8)),str(B[0]%8),getTOrF(B[1])))
	elif C==108:display(A,'FUN_80631B8C(%s)'%str(B[0]))
	elif C==109:display(A,'FUN_8063A8C4(this->id,1,%s)'%str(B[0]/100))
	elif C==110:display(A,'BYTE_807F693F = %s'%str(B[0]))
	elif C==111:display(A,'?playMusic(%s,%s)'%(str(B[0]),str(B[1]&255)))
	elif C==112:display(A,'FUN_80602C6C(%s,%s)'%(str(B[0]),str(B[1]/255)))
	elif C==113:display(A,'FUN_80602DC4()')
	elif C==114:display(A,"getAndSetActorSpawnerControlStateFromActorSpawnerID(%s,%s,'%s')"%(str(B[0]),str(B[1]&255),getSetOrNot(1)))
	elif C==115:display(A,'FUN_806EB178(0,%s,%s,%s)'%(str(B[0]),str(B[1]),str(B[2])))
	elif C==116:display(A,'*(byte *)(behaviour + 0x9B) = *(byte *)(behaviour + 0x9B) | %s'%hex(B[0]))
	elif C==117:display(A,"changeTriggerActiveStateOfFirstInstanceOfType('%s',%s)"%(getTriggerTypeName(B[0]),str(B[1])))
	elif C==118:display(A,'x76_counter = 0');display(A,'x76_focusedLoadedActorSlot = &loadedActorArray');display(A,_T);display(A,_L);display(A,'x76_focusedLoadedActor = *x76_focusedLoadedActorSlot');display(A,'if ((*(uint *)(x76_focusedLoadedActor->object_properties_bitfield) & 0x2000) == 0) {');display(A,'if (x76_focusedLoadedActor->locked_to_pad == 1) {');display(A,'if (this->id == *(short *)(x76_focusedLoadedActor->unk0x10c)) {');display(A,'FUN_80679200(x76_focusedLoadedActor,0,8,0)');display(A,_B);display(A,_B);display(A,_B);display(A,'x76_counter = x76_counter + 1');display(A,'x76_focusedLoadedActorSlot = x76_focusedLoadedActorSlot + 8');display(A,'} while (x76_counter < loadedActorCount)');display(A,_B)
	elif C==119:display(A,'FUN_80650794(this->id,%s,%s,%s)'%(str(B[0]),str(B[1]&255),str(B[2]/1000)))
	elif C==120:display(A,'FUN_806335B0(this->id,1,%s)'%str(B[0]));display(A,'PlayerPointer->unk0x3A4 = uStack40');display(A,'PlayerPointer->unk0x3A8 = uStack44');display(A,'PlayerPointer->unk0x3AC = uStack48')
	elif C==121:display(A,"setFlag(%s>%s,%s,'Temporary')"%(hex(math.floor(B[0]/8)),str(B[0]%8),getTOrF(B[1])))
	elif C==122:display(A,'FUN_80661264(%s,%s)'%(str(B[0]&255),str(B[0]&255)))
	elif C==123:display(A,'FUN_806335B0(this->id,%s)'%str(B[1]));display(A,'FUN_8072ECFC(%s)'%str(B[0]))
	elif C==124:display(A,'BYTE_80748094 = %s'%str(B[0]))
	elif C==125:display(A,P%hex(2*B[1]+16));display(A,Q%(hex(2*B[1]+16),str(B[0]),str(B[2]&127),str(B[1]&2)));display(A,_B)
	elif C==126:
		E=B[1]
		if B[1]<0:E=E+127
		G=E>>7&255;E=B[2]
		if B[2]<0:E=E+127
		L=E>>7&255;M=L
		if G==0:G=127
		if L==0:M=255
		display(A,'if (BYTE_80748094 < 1) {');display(A,'playSFX(%s,0x7FFF,0x427C0000,%s)'%(str(B[0]),str(G/127)));display(A,_B);display(A,I);display(A,'FUN_806335B0(this->id,1,BYTE_80748094)');display(A,'FUN_806086CC(%s,%s,%s,%s,0.3,0)'%(str(M),str(G),str(B[1]&127),str(B[2]&127)));display(A,_B)
	elif C==127:
		if B[1]==0:F=0
		elif B[1]==1:F=1
		elif B[1]==2:F=2
		elif B[1]==3:F=3
		else:F=0
		display(A,'FUN_8072EE0C(this->id,%s,%s)'%(str(B[0]),str(F)))
	elif C==128:display(A,'save()')
	elif C==129:display(A,'BYTE_807F693E = BYTE_807F693E | (1 << %s)'%str(B[0]))
	elif C==130:display(A,'BYTE_807F693E = BYTE_807F693E & ~(1 << %s)'%str(B[0]))
	elif C==131:
		N='Unknown %s'%hex(B[0])
		if B[0]in hud_items:N=hud_items[B[0]]
		display(A,'setHUDItemAsInfinite(%s,%s,%s)'%(N,str(B[1]),getTOrF(B[2])))
	elif C==132:display(A,"setFlag(%s>%s,%s,'Global')"%(hex(math.floor(B[0]/8)),str(B[0]%8),getTOrF(B[1])))
	elif C==133:display(A,'FUN_8062D1A8()')
	elif C==134:display(A,V);display(A,'InitMapChange_TransferredActor(0x2A,0,%s,2)'%str(B[0]))
	elif C==135:display(A,'warpOutOfBonusGame()')
	elif C==136:display(A,'DWORD_807FBB68 = DWORD_807FBB68 | %s'%hex(B[0]*65536+B[1]))
	elif C==137:display(A,'DWORD_807FBB68 = DWORD_807FBB68 & ~%s'%hex(B[0]*65536+B[1]))
	elif C==138:display(A,'FUN_806417BC(%s,%s)'%(str(B[0]),str(B[1])))
	elif C==139:display(A,'*(uint *)(PlayerPointer->unk0x36C) = *(uint *)(PlayerPointer->unk0x36C) & ~%s'%hex(B[0]*65536+B[1]))
	elif C==140:display(A,'*(uint *)(PlayerPointer->unk0x36C) = *(uint *)(PlayerPointer->unk0x36C) | %s'%hex(B[0]*65536+B[1]))
	elif C==141:display(A,"next_transition_type = 'Fade'");display(A,V);display(A,'x8d_uvar5 = getWorld(CurrentMap,0)');display(A,'x8d_ivar6 = isLobby(CurrentMap)');display(A,'x8d_ivar7 = x8d_uvar5');display(A,W);display(A,'warpOutOfLevel(x8d_ivar7)');display(A,_B);display(A,I);display(A,'x8d_svar12 = *(short *)(&DAT_8074809C + (x8d_ivar7 * 2))');display(A,'x8d_dstack88 = (short)(&WORD_807480AC)[x8d_ivar7]');display(A,"x8d_uvar9 = isFlagSet(*(short *)(&DAT_807480BC + (x8d_ivar7 * 2)),'Permanent')");display(A,'if ((x8d_uvar9 == 0) && (x8d_svar12 == 0x57)) {');display(A,'x8d_dstack88 = 0x15');display(A,_B);display(A,'x8d_ivar6 = DetermineLevel_NewLevel()');display(A,W);display(A,'InitMapChange(x8d_svar12,x8d_dstack88)');display(A,_B)
	elif C==142:display(A,'FUN_8066C904(&ObjectModel2ArrayPointer[id2index(this->id)]->unk0x28)')
	elif C==143:display(A,'FUN_806348B4(&ObjectModel2ArrayPointer[id2index(this->id)]->unk0x48)')
	elif C==144:display(A,'BYTE_807F6902 = %s'%str(B[0]))
	elif C==145:display(A,'*(float *)(PlayerPointer->velocity) = %s'%str(B[0]))
	elif C==146:display(A,'*(uint *)(PlayerPointer->unk0x368) = *(uint *)(PlayerPointer->unk0x368) | 0x40000800')
	elif C==147:display(A,'FUN_8061F510(%s,%s)'%(str(B[0]&255),str(B[1]&255)))
	elif C==148:display(A,'FUN_80724994(2,%s,0,0)'%str(B[0]))
	elif C==149:display(A,'WORD_807F693C = 0x80')
	elif C==150:display(A,'BYTE_807F6903 = %s'%str(B[0]))
	else:display(A,'[%s,%s,%s,%s]'%(str(C),str(B[0]),str(B[1]),str(B[2])))
def readData(data,size,read_location):'Read data from a file.';A=read_location;return bytereadToInt(data[A:A+size])
def grabScripts(data,file_path):
	'Grab Scripts from file.';c='\t}\n';b='_type';a='_id';T='\t\t"x": ';S='w';M=',\n';D=file_path;C=data;global tab_indentation;global folder_removal;A=0;K=readData(C,2,A)
	if K==0:folder_removal.append(D)
	elif K>0:
		N=[]
		with open(f"{D}/scripts.raw",_a)as d:d.write(C)
		with open(D+_AN,'rb')as B:
			with open(D+'/setup.json',S)as e:
				B.seek(0);f=bytereadToInt(B.read(4));F=4
				for n in range(f):B.seek(F+42);g=bytereadToInt(B.read(2));B.seek(F+40);h=bytereadToInt(B.read(2));B.seek(F);i=bytereadToInt(B.read(4));B.seek(F+4);j=bytereadToInt(B.read(4));B.seek(F+8);k=bytereadToInt(B.read(4));N.append({a:g,b:h,'_x':i,'_y':j,'_z':k});F+=48;e.write(str(N))
		print(D+': '+str(K));A+=2
		if not os.path.exists(D):os.mkdir(D)
		for l in range(K):
			tab_indentation=0;L=readData(C,2,A);H=0;U=0;V=0;W=0
			for G in N:
				if G[a]==L:H=G[b];U=G['_x'];V=G['_y'];W=G['_z']
			I='Unknown '+hex(H)
			if H<len(object_modeltwo_types)-1:I=object_modeltwo_types[H]
			I=make_safe_filename(I).replace('?','')
			with open(D+'/'+I+'_'+str(hex(L))+'.json',S)as E:E.write('{\n');E.write('\t"_id": '+hex(L)+M);E.write('\t"_type": '+hex(H)+M);E.write('\t"coordinates": {\n');E.write(T+hex(U)+M);E.write(T+hex(V)+M);E.write(T+hex(W));E.write(c);E.write(c)
			with open(D+'/'+I+'_'+str(hex(L))+'.code',S)as O:
				m=readData(C,2,A+2);o=readData(C,2,A+4);A+=6
				for G in range(m):
					tab_indentation=0;X=readData(C,2,A);A+=2;l={}
					if X>0:
						for P in range(X):
							Q=readData(C,2,A);A+=2;J=[]
							for Y in range(3):J.append(readData(C,2,A));A+=2
							grabConditional(0,Q,J,0,0,O)
					Z=readData(C,2,A);A+=2
					if Z>0:
						for P in range(Z):
							Q=readData(C,2,A);A+=2;J=[]
							for Y in range(3):J.append(readData(C,2,A));A+=2
							grabExecution(0,Q,J,0,0,O)
					for P in range(tab_indentation):
						R=_B
						for Y in range(tab_indentation-P-1):R='\t'+R
						O.write(R+'\n')
def getFileInfo(absolute_address):
	'Get file information.';A=absolute_address
	if hex(A)in files:return files[hex(A)]
def getOriginalUncompressedSize(fh,pointer_table_index,file_index):'Get original uncompressed size.';global pointer_tables;A=pointer_tables[26][_b][pointer_table_index][_M]+file_index*4;fh.seek(A);return int.from_bytes(fh.read(4),_D)
def addFileToDatabase(absolute_address,data,uncompressed_size):
	'Add file to database.';B=False;A=absolute_address;global files;global pointer_tables;C=B
	for D in pointer_tables:
		if D[_M]==A:C=True;break
	files[hex(A)]={_AO:A,'has_been_modified':B,'is_bigger_than_original':B,'has_been_written_to_rom':C,'data':data,'uncompressed_size':uncompressed_size}
def parsePointerTables(fh):
	'Parse pointer tables.';I='next_absolute_address';F='num_entries';B=fh;global pointer_tables;global main_pointer_table_offset;global maps;global num_tables;B.seek(main_pointer_table_offset);C=0
	while C<num_tables:E=int.from_bytes(B.read(4),_D)+main_pointer_table_offset;pointer_tables.append({_C:C,_M:E,_AO:E,F:0,_b:[]});C+=1
	B.seek(main_pointer_table_offset+num_tables*4)
	for A in pointer_tables:A[F]=int.from_bytes(B.read(4),_D)
	for A in pointer_tables:
		if A[F]>0:
			C=0
			while C<A[F]:B.seek(A[_M]+C*4);G=int.from_bytes(B.read(4),_D);E=(G&2147483647)+main_pointer_table_offset;J=(int.from_bytes(B.read(4),_D)&2147483647)+main_pointer_table_offset;A[_b].append({_C:C,_M:E,I:J,'bit_set':G&2147483648>0});C+=1
	for A in pointer_tables:
		if A[_C]==script_table_index-(version==3)or A[_C]==setup_table_index-(version==3):
			for D in A[_b]:
				H=D[I]-D[_M]
				if H>0:B.seek(D[_M]);K=B.read(H);addFileToDatabase(D[_M],K,getOriginalUncompressedSize(B,A[_C],D[_C]))
def make_safe_filename(s):
	'Generate safe filename.'
	def A(c):
		if c.isalnum():return c
		else:return'_'
	return ''.join((A(B)for B in s)).rstrip('_')
def extractMaps(src_file):
	'Extract Map Data.';global maps
	for (A,C) in enumerate(maps):B=f"map_scripts{folder_append[version]}/"+str(A)+' - '+make_safe_filename(C);os.mkdir(B);extractMap(src_file,A,B)
def extractMap(src_file,mapIndex,mapPath):
	'Extract one map data.';I=mapIndex;D=mapPath;global pointer_tables;global files;global num_tables;global relevant_pointer_tables;global folder_removal;L=setup_table_index-(version==3);M=script_table_index-(version==3);N=[L,M];G=[0,0];E=0
	with open(src_file,'rb')as A:
		for J in N:
			A.seek(main_pointer_table_offset+num_tables*4+4*J);O=int.from_bytes(A.read(4),_D)
			if O>I:
				A.seek(main_pointer_table_offset+4*J);P=main_pointer_table_offset+int.from_bytes(A.read(4),_D);A.seek(P+4*I);K=main_pointer_table_offset+(int.from_bytes(A.read(4),_D)&2147483647);Q=main_pointer_table_offset+(int.from_bytes(A.read(4),_D)&2147483647);H=Q-K;G[E]=H
				if H>0:
					A.seek(K);B=A.read(H)
					with open('temp.bin',_a)as C:C.write(B)
					if int.from_bytes(B[0:1],_D)==31 and int.from_bytes(B[1:2],_D)==139:F=zlib.decompress(B,15+32)
					else:F=B
					if E==0:
						R=D+_AN
						with open(R,_a)as C:C.write(F)
					elif E==1:
						S=D+'/scripts.bin'
						with open(S,_a)as C:C.write(F)
						grabScripts(F,D)
			E+=1
	if G[0]+G[1]==0:folder_removal.append(D)
def bytereadToInt(read):
	'Convert bytes to an int.';A=0
	for B in list(read):A=A*256+B
	return A
def extractScripts():
	'Extract scripts from ROM.';G='Invalid version';global folder_removal;global pointer_table_offsets;global main_pointer_table_offset;global folder_append;global version;D=folder_append[0];A=filedialog.askopenfilename()
	with open(A,'rb')as B:
		H=int.from_bytes(B.read(1),_D)
		if H!=128:print('File is little endian. Convert to big endian and re-run');exit()
		else:
			B.seek(61);I=int.from_bytes(B.read(1),_D);E=int.from_bytes(B.read(1),_D);version=-1
			if I==80:version=3
			elif E==69:version=0
			elif E==74:version=2
			elif E==80:version=1
			else:print(G);exit()
			main_pointer_table_offset=pointer_table_offsets[version];D=folder_append[version]
	if version<0 or version>3:print(G);exit()
	folder_removal=[];F=f"./map_scripts{D}"
	if os.path.exists(F):shutil.rmtree(F)
	os.mkdir(f"./map_scripts{D}");extractMaps(A)
	for C in folder_removal:
		if os.path.exists(C):
			for J in os.listdir(C):
				A=os.path.join(C,J)
				try:
					if os.path.isfile(A)or os.path.islink(A):os.unlink(A)
					elif os.path.isdir(A):shutil.rmtree(A)
				except Exception as K:print('Failed to delete %s. Reason: %s'%(A,K))
			os.rmdir(C)
extractScripts()