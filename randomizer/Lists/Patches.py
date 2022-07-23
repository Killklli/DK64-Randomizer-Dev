'Designates Dirt Patch Location Properties.'
_B='Reduce scale'
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Time import Time
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Enums.Levels import Levels
import randomizer.Logic
class DirtPatchData:
	'Information about the dirt patch location.'
	def __init__(A,*,name='',level='',map_id=0,vanilla=False,x=0,y=0,z=0,rotation=0,group=0,logicregion='',logic=0,resize=''):'Initialize with given parameters.';B=vanilla;A.name=name;A.level_name=level;A.map_id=map_id;A.vanilla=B;A.x=x;A.y=y;A.z=z;A.rotation=rotation;A.selected=B;A.group=group;A.logicregion=logicregion;A.logic=logic;A.resize=resize
	def setPatch(A,used):"Set patch's state regarding rando.";A.selected=used
DirtPatchLocations=[DirtPatchData(name='DK Isles: On Aztec Building',level=Levels.DKIsles,map_id=Maps.Isles,x=3509.673,y=1170.0,z=1733.509,rotation=1784,vanilla=_A,group=3,logicregion=Regions.CabinIsle,logic=lambda l:Events.IslesDiddyBarrelSpawn in l.Events and l.jetpack and l.isdiddy and l.shockwave,resize=''),DirtPatchData(name='DK Isles: Under Caves Lobby Entrance',level=Levels.DKIsles,map_id=Maps.Isles,x=2401.601,y=800.0,z=1571.532,rotation=4028,vanilla=_A,group=3,logicregion=Regions.IslesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles: Front of Fungi Building',level=Levels.DKIsles,map_id=Maps.Isles,x=2647.643,y=1498.0,z=929.797,rotation=748,vanilla=_A,group=2,logicregion=Regions.CabinIsle,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Training Grounds: Banana Hoard',level=Levels.DKIsles,map_id=Maps.TrainingGrounds,x=2497.648,y=191.0,z=1036.583,rotation=0,vanilla=_A,group=1,logicregion=Regions.TrainingGrounds,logic=lambda l:l.vines and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Training Grounds: Rear Inside Tunnel',level=Levels.DKIsles,map_id=Maps.TrainingGrounds,x=1223.714,y=37.208,z=2200.538,rotation=1002,vanilla=_A,group=1,logicregion=Regions.TrainingGrounds,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="DK Isles - K Lumsy: Inside K. Lumsy's Cage",level=Levels.DKIsles,map_id=Maps.KLumsy,x=1499.675,y=95.0,z=1233.831,rotation=2736,vanilla=_A,group=5,logicregion=Regions.Prison,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Creepy Castle Lobby: Castle Lobby',level=Levels.DKIsles,map_id=Maps.CreepyCastleLobby,x=579.809,y=245.5,z=681.709,rotation=2074,vanilla=_A,group=14,logicregion=Regions.CreepyCastleLobby,logic=lambda l:l.chunky and l.balloon and l.islanky and l.shockwave,resize=''),DirtPatchData(name='DK Isles: Isles Boulders',level=Levels.DKIsles,map_id=Maps.Isles,x=2813.0,y=1058.0,z=2054.0,rotation=3959,group=3,logicregion=Regions.IslesMain,logic=lambda l:l.vines and l.shockwave,resize=''),DirtPatchData(name='DK Isles: Behind BFI',level=Levels.DKIsles,map_id=Maps.Isles,x=754.0,y=500.0,z=2386.0,rotation=807,group=4,logicregion=Regions.IslesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles: Back of Kroc Isle (Lower)',level=Levels.DKIsles,map_id=Maps.Isles,x=2019.0,y=590.0,z=4146.0,rotation=1615,group=6,logicregion=Regions.IslesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles: Back of Kroc Isle (Middle)',level=Levels.DKIsles,map_id=Maps.Isles,x=2350.0,y=1199.0,z=3887.0,rotation=1956,group=6,logicregion=Regions.CrocodileIsleBeyondLift,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles: Kroc Isle Left Arm',level=Levels.DKIsles,map_id=Maps.Isles,x=2313.0,y=1620.0,z=3214.0,rotation=3891,group=6,logicregion=Regions.IslesMain,logic=lambda l:l.monkeyport and l.istiny and l.shockwave,resize=''),DirtPatchData(name='DK Isles: In Fungi Boulder',level=Levels.DKIsles,map_id=Maps.Isles,x=3516.0,y=500.0,z=633.0,rotation=1934,group=2,logicregion=Regions.IslesMain,logic=lambda l:l.GalleonKey and l.shockwave,resize=''),DirtPatchData(name='DK Isles: Behind Fungi Building',level=Levels.DKIsles,map_id=Maps.Isles,x=2436.0,y=1498.0,z=817.0,rotation=637,group=2,logicregion=Regions.CabinIsle,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles: Behind Aztec Building',level=Levels.DKIsles,map_id=Maps.Isles,x=3643.0,y=1020.0,z=1790.0,rotation=2742,group=3,logicregion=Regions.IslesMainUpper,logic=lambda l:l.vines and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Banana Fairy Room: Behind Fairy Chair',level=Levels.DKIsles,map_id=Maps.BananaFairyRoom,x=835.0,y=37.0,z=563.0,rotation=1080,group=4,logicregion=Regions.BananaFairyRoom,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Banana Fairy Room: Behind the Rareware Door',level=Levels.DKIsles,map_id=Maps.BananaFairyRoom,x=644.0,y=37.0,z=1085.0,rotation=2048,group=4,logicregion=Regions.BananaFairyRoom,logic=lambda l:l.BananaFairies>=20 and l.shockwave,resize=''),DirtPatchData(name='DK Isles - K Lumsy: Under K. Lumsy',level=Levels.DKIsles,map_id=Maps.KLumsy,x=1020.0,y=50.0,z=1001.0,rotation=682,group=5,logicregion=Regions.Prison,logic=lambda l:l.CanAccessKrool()and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Hideout Helm Lobby: Bonus Barrel Platform',level=Levels.DKIsles,map_id=Maps.HideoutHelmLobby,x=683.0,y=196.0,z=638.0,rotation=1024,group=7,logicregion=Regions.HideoutHelmLobby,logic=lambda l:l.gorillaGone and l.ischunky and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Hideout Helm Lobby: Blueprint Platform',level=Levels.DKIsles,map_id=Maps.HideoutHelmLobby,x=325.0,y=191.0,z=643.0,rotation=0,group=7,logicregion=Regions.HideoutHelmLobby,logic=lambda l:l.coconut and l.scope and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Jungle Japes Lobby: Near Tag Barrel',level=Levels.DKIsles,map_id=Maps.JungleJapesLobby,x=713.0,y=4.0,z=266.0,rotation=1945,group=8,logicregion=Regions.JungleJapesLobby,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Angry Aztec Lobby: Behind Feather Door',level=Levels.DKIsles,map_id=Maps.AngryAztecLobby,x=1128.0,y=0.0,z=586.0,rotation=694,group=9,logicregion=Regions.AngryAztecLobby,logic=lambda l:l.feather and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Frantic Factory Lobby: High Platform',level=Levels.DKIsles,map_id=Maps.FranticFactoryLobby,x=674.0,y=133.0,z=376.0,rotation=1024,group=10,logicregion=Regions.FranticFactoryLobby,logic=lambda l:l.grab and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Gloomy Galleon Lobby: Behind Mini Monkey Gate',level=Levels.DKIsles,map_id=Maps.GloomyGalleonLobby,x=838.0,y=99.0,z=232.0,rotation=978,group=11,logicregion=Regions.GloomyGalleonLobby,logic=lambda l:l.mini and l.superSlam and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Fungi Forest Lobby: Behind Gorilla Gone Door',level=Levels.DKIsles,map_id=Maps.FungiForestLobby,x=99.0,y=4.0,z=533.0,rotation=1024,group=12,logicregion=Regions.FungiForestLobby,logic=lambda l:l.coconut and l.peanut and l.grape and l.feather and l.pineapple and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Fungi Forest Lobby: On Tag Crate',level=Levels.DKIsles,map_id=Maps.FungiForestLobby,x=436.0,y=46.0,z=252.0,rotation=1024,group=12,logicregion=Regions.FungiForestLobby,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Crystal Caves Lobby: On the Lava',level=Levels.DKIsles,map_id=Maps.CrystalCavesLobby,x=387.0,y=2.0,z=207.0,rotation=785,group=13,logicregion=Regions.CrystalCavesLobby,logic=lambda l:l.punch and l.strongKong and l.isdonkey and l.shockwave,resize=''),DirtPatchData(name='DK Isles - Creepy Castle Lobby: Behind the entrance',level=Levels.DKIsles,map_id=Maps.CreepyCastleLobby,x=577.0,y=60.0,z=67.0,rotation=773,group=14,logicregion=Regions.CreepyCastleLobby,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Isles Snide Room: Next to Snides',level=Levels.DKIsles,map_id=Maps.IslesSnideRoom,x=576.0,y=0.0,z=450.0,rotation=341,group=6,logicregion=Regions.IslesSnideRoom,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Training Grounds: On the entrance hill',level=Levels.DKIsles,map_id=Maps.TrainingGrounds,x=1108.0,y=220.0,z=701.0,rotation=3026,group=1,logicregion=Regions.TrainingGrounds,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Training Grounds: On the rear hill',level=Levels.DKIsles,map_id=Maps.TrainingGrounds,x=1086.0,y=252.0,z=1833.0,rotation=489,group=1,logicregion=Regions.TrainingGrounds,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='DK Isles - Treehouse: Back of the treehouse',level=Levels.DKIsles,map_id=Maps.Treehouse,x=288.0,y=85.0,z=488.0,rotation=3072,group=1,logicregion=Regions.Treehouse,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: On Painting Hill',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=550.814,y=370.167,z=1873.436,rotation=1070,vanilla=_A,group=1,logicregion=Regions.JungleJapesMain,logic=lambda l:l.handstand or l.twirl and l.shockwave,resize=''),DirtPatchData(name="Jungle Japes: Inside Diddy's Cavern",level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=2475.0,y=280.0,z=508.0,rotation=2427,group=3,logicregion=Regions.JapesBeyondPeanutGate,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes - Japes Mountain: On a Barrel',level=Levels.JungleJapes,map_id=Maps.JapesMountain,x=691.0,y=135.0,z=753.0,rotation=2013,group=5,logicregion=Regions.Mine,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Minecart Exit',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1108.0,y=288.0,z=1970.0,rotation=2707,group=1,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Jungle Japes: Under Chunky's Barrel",level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=2345.0,y=551.0,z=3152.0,rotation=1160,group=6,logicregion=Regions.JapesBeyondFeatherGate,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Near Cannon to Diddy-freeing cage',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1274.0,y=520.0,z=2225.0,rotation=2275,group=4,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Fell off the vines',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1166.0,y=230.0,z=2595.0,rotation=3128,group=8,logicregion=Regions.JapesBeyondCoconutGate2,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: On the useless Lanky ramp',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=2234.0,y=338.0,z=3242.0,rotation=2241,group=2,logicregion=Regions.JapesBeyondCoconutGate2,logic=lambda l:l.handstand and l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Cranky-tunnel Crossing',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1633.0,y=210.0,z=3015.0,rotation=2161,group=2,logicregion=Regions.JapesBeyondCoconutGate2,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Directly behind Cranky',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1697.0,y=280.0,z=4088.0,rotation=0,group=2,logicregion=Regions.JapesBeyondCoconutGate2,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Jungle Japes: Next to topright's hut",level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1409.0,y=280.0,z=4367.0,rotation=2142,group=2,logicregion=Regions.JapesBeyondCoconutGate2,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Behind Chunky Boulder',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=2433.0,y=280.0,z=1114.0,rotation=3784,group=2,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Inside the first tunnel - later half',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1812.0,y=280.0,z=797.0,rotation=1171,group=3,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Next to level entrance',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=754.0,y=286.0,z=824.0,rotation=796,group=3,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Jungle Japes: Next to first tunnel entrance',level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1357.0,y=283.0,z=205.0,rotation=3572,group=3,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Jungle Japes: Behind Diddy's Mountain",level=Levels.JungleJapes,map_id=Maps.JungleJapes,x=1542.0,y=790.0,z=2578.0,rotation=2969,group=4,logicregion=Regions.JungleJapesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Oasis',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=2426.34,y=115.5,z=960.642,rotation=2618,vanilla=_A,group=1,logicregion=Regions.AngryAztecStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec - Aztec Chunky5D Temple: Chunky 5DT',level=Levels.AngryAztec,map_id=Maps.AztecChunky5DTemple,x=652.778,y=85.0,z=1544.845,rotation=1036,vanilla=_A,group=7,logicregion=Regions.ChunkyTemple,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Behind Chunky Cage',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=4395.0,y=120.0,z=2409.0,rotation=2992,group=5,logicregion=Regions.AngryAztecMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Entrance tunnel - near DK door',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=1372.0,y=120.0,z=1125.0,rotation=4084,group=6,logicregion=Regions.AngryAztecStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Next to Tiny Temple - left',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=3184.0,y=153.0,z=343.0,rotation=4009,group=1,logicregion=Regions.AngryAztecStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Next to Tiny Temple - right',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=3489.0,y=153.0,z=702.0,rotation=3001,group=1,logicregion=Regions.AngryAztecStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Behind Llama Cage',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=2070.0,y=153.0,z=1706.0,rotation=3424,group=1,logicregion=Regions.AngryAztecStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec - Aztec Tiny Temple: Main room back-left',level=Levels.AngryAztec,map_id=Maps.AztecTinyTemple,x=1727.0,y=284.0,z=649.0,rotation=3417,group=2,logicregion=Regions.TempleStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec - Aztec Tiny Temple: Next to Tiny cage',level=Levels.AngryAztec,map_id=Maps.AztecTinyTemple,x=565.0,y=344.0,z=1146.0,rotation=3959,group=2,logicregion=Regions.TempleUnderwater,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Next to Candy',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=2421.0,y=120.0,z=489.0,rotation=3492,group=1,logicregion=Regions.AngryAztecStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Next to Llama Temple',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=3110.0,y=160.0,z=3193.0,rotation=284,group=3,logicregion=Regions.AngryAztecMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Next to Snide',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=4028.0,y=120.0,z=4505.0,rotation=1496,group=3,logicregion=Regions.AngryAztecMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Behind Gong-tower',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=4524.0,y=80.0,z=2936.0,rotation=3663,group=3,logicregion=Regions.AngryAztecMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec: Left of Gong-tower',level=Levels.AngryAztec,map_id=Maps.AngryAztec,x=4190.0,y=80.0,z=3011.0,rotation=3902,group=3,logicregion=Regions.AngryAztecMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec - Aztec Llama Temple: Next to Llama Left',level=Levels.AngryAztec,map_id=Maps.AztecLlamaTemple,x=1729.0,y=472.0,z=2198.0,rotation=1649,group=4,logicregion=Regions.LlamaTemple,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Angry Aztec - Aztec Llama Temple: Next to Llama Right',level=Levels.AngryAztec,map_id=Maps.AztecLlamaTemple,x=1777.0,y=472.0,z=2592.0,rotation=608,group=4,logicregion=Regions.LlamaTemple,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Dark Room',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1850.584,y=6.5,z=666.077,rotation=3110,vanilla=_A,group=3,logicregion=Regions.BeyondHatch,logic=lambda l:l.punch and l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Toy Room Under Stairs',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=2015.0,y=1026.0,z=1364.0,rotation=3026,group=2,logicregion=Regions.Testing,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Middle of Entrance Room',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1264.0,y=830.0,z=2550.0,rotation=0,group=1,logicregion=Regions.FranticFactoryStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Clock-in room left',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1130.0,y=842.0,z=2130.0,rotation=432,group=1,logicregion=Regions.FranticFactoryStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Clock-in room right',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1409.0,y=842.0,z=2104.0,rotation=3618,group=1,logicregion=Regions.FranticFactoryStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Frantic Factory: Halfway the hatch near entrance - next to the window - Tiny's 10 CB",level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=642.0,y=459.0,z=1796.0,rotation=4073,group=1,logicregion=Regions.BeyondHatch,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Tunnel to production room',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=70.0,y=6.0,z=1350.0,rotation=193,group=1,logicregion=Regions.BeyondHatch,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Next to DK Arcade',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1784.0,y=1106.0,z=1273.0,rotation=0,group=4,logicregion=Regions.BeyondHatch,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Near Snide',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1603.0,y=810.0,z=2210.0,rotation=2163,group=5,logicregion=Regions.Testing,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Frantic Factory: On Diddy's Block Tower",level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=2384.0,y=1266.0,z=1379.0,rotation=2013,group=2,logicregion=Regions.Testing,logic=lambda l:l.spring and l.shockwave,resize=_B),DirtPatchData(name="Frantic Factory: In Lanky's Piano Room",level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=3470.0,y=1264.0,z=303.0,rotation=113,group=3,logicregion=Regions.RandD,logic=lambda l:l.trombone and l.shockwave,resize=''),DirtPatchData(name="Frantic Factory: In Diddy's Pincode enemies room",level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=4463.0,y=1336.0,z=551.0,rotation=3528,group=3,logicregion=Regions.RandD,logic=lambda l:l.guitar and l.shockwave,resize=''),DirtPatchData(name="Frantic Factory: In front of Chunky's toyboss room",level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=4345.0,y=1416.0,z=1354.0,rotation=2654,group=3,logicregion=Regions.RandD,logic=lambda l:l.punch and l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Near Funky',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=1656.0,y=1113.0,z=502.0,rotation=273,group=2,logicregion=Regions.Testing,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Frantic Factory: Tiny race entry area',level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=3544.0,y=1264.0,z=1301.0,rotation=95,group=3,logicregion=Regions.FactoryTinyRaceLobby,logic=lambda l:l.mini and l.shockwave,resize=''),DirtPatchData(name="Frantic Factory: R&D lever room - by Tiny's barrel",level=Levels.FranticFactory,map_id=Maps.FranticFactory,x=3693.0,y=1263.0,z=1412.0,rotation=1604,group=3,logicregion=Regions.RandD,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon - Galleon Lighthouse: Interior Rear',level=Levels.GloomyGalleon,map_id=Maps.GalleonLighthouse,x=457.54,y=0.0,z=716.299,rotation=18,vanilla=_A,group=1,logicregion=Regions.Lighthouse,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: On the ship near Cranky',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=3068.0,y=1790.0,z=3386.0,rotation=2048,group=3,logicregion=Regions.GloomyGalleonStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Next to cannon in cannonball room',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=1310.0,y=1610.0,z=3055.0,rotation=2048,group=4,logicregion=Regions.GalleonBeyondPineappleGate,logic=lambda l:Events.WaterSwitch in l.Events and l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Entrance tunnel - under tag barrel',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=2534.0,y=1610.0,z=3231.0,rotation=3094,group=3,logicregion=Regions.GloomyGalleonStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Next to Lighthouse ladder',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=1611.0,y=1610.0,z=3933.0,rotation=3652,group=1,logicregion=Regions.LighthouseArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Under Diddy Barrel',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=1340.0,y=1660.0,z=4043.0,rotation=910,group=1,logicregion=Regions.LighthouseArea,logic=lambda l:l.shockwave,resize=_B),DirtPatchData(name="Gloomy Galleon - Galleon Lighthouse: Behind Whomp's Fortress floor 2",level=Levels.GloomyGalleon,map_id=Maps.GalleonLighthouse,x=453.0,y=200.0,z=596.0,rotation=0,group=1,logicregion=Regions.Lighthouse,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Gloomy Galleon - Galleon Lighthouse: On top of Whomp's Fortress",level=Levels.GloomyGalleon,map_id=Maps.GalleonLighthouse,x=418.0,y=720.0,z=497.0,rotation=3572,group=1,logicregion=Regions.Lighthouse,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon - Galleon Sick Bay: Chunky ship entrance',level=Levels.GloomyGalleon,map_id=Maps.GalleonSickBay,x=628.0,y=20.0,z=229.0,rotation=2048,group=2,logicregion=Regions.SickBay,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon - Galleon Sick Bay: Chunky ship - backleft corner',level=Levels.GloomyGalleon,map_id=Maps.GalleonSickBay,x=701.0,y=20.0,z=899.0,rotation=2525,group=2,logicregion=Regions.SickBay,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon - Galleon Sick Bay: Chunky ship - behind the non-alcoholic tower',level=Levels.GloomyGalleon,map_id=Maps.GalleonSickBay,x=159.0,y=20.0,z=920.0,rotation=978,group=2,logicregion=Regions.SickBay,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Next to Cannonball - in front',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=1366.0,y=1610.0,z=2586.0,rotation=0,group=4,logicregion=Regions.GalleonBeyondPineappleGate,logic=lambda l:Events.WaterSwitch in l.Events and l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Next to Cannonball - behind',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=1261.0,y=1610.0,z=2588.0,rotation=0,group=4,logicregion=Regions.GalleonBeyondPineappleGate,logic=lambda l:Events.WaterSwitch in l.Events and l.shockwave,resize=''),DirtPatchData(name="Gloomy Galleon: Behind Chunky's Big GB Chest",level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=3564.0,y=1670.0,z=3944.0,rotation=2503,group=3,logicregion=Regions.GloomyGalleonStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: Behind the ship you shoot onto with the cannon',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=3199.0,y=1670.0,z=3463.0,rotation=2264,group=3,logicregion=Regions.GloomyGalleonStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Gloomy Galleon: In front of Cranky',level=Levels.GloomyGalleon,map_id=Maps.GloomyGalleon,x=3309.0,y=1790.0,z=2456.0,rotation=170,group=3,logicregion=Regions.GloomyGalleonStart,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Beanstalk',level=Levels.FungiForest,map_id=Maps.FungiForest,x=2279.848,y=228.931,z=600.56,rotation=1020,vanilla=_A,group=1,logicregion=Regions.WormArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Mill Grass',level=Levels.FungiForest,map_id=Maps.FungiForest,x=4674.706,y=149.873,z=4165.153,rotation=2584,vanilla=_A,group=2,logicregion=Regions.MillArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Top of Owl Tree',level=Levels.FungiForest,map_id=Maps.FungiForest,x=1268.0,y=575.0,z=3840.0,rotation=34,group=5,logicregion=Regions.HollowTreeArea,logic=lambda l:l.jetpack and l.isdiddy and l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Near BBlast',level=Levels.FungiForest,map_id=Maps.FungiForest,x=752.0,y=589.0,z=1296.0,rotation=534,group=4,logicregion=Regions.MushroomLowerExterior,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Under the Owl Tree',level=Levels.FungiForest,map_id=Maps.FungiForest,x=1274.0,y=249.0,z=3686.0,rotation=2048,group=5,logicregion=Regions.HollowTreeArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Owl and Rabbit area - near Diddy Barrel',level=Levels.FungiForest,map_id=Maps.FungiForest,x=549.0,y=189.0,z=3940.0,rotation=1080,group=5,logicregion=Regions.HollowTreeArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Fungi Forest: Next to Rabbit's house",level=Levels.FungiForest,map_id=Maps.FungiForest,x=2297.0,y=142.0,z=3703.0,rotation=2946,group=5,logicregion=Regions.HollowTreeArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Fungi Forest - Forest Mill Front: Inside the water mill - near DK's levers",level=Levels.FungiForest,map_id=Maps.ForestMillFront,x=234.0,y=0.0,z=229.0,rotation=352,group=3,logicregion=Regions.GrinderRoom,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Fungi Forest - Forest Mill Back: Inside the water mill - near Chunky's coins (Chunky's punch door)",level=Levels.FungiForest,map_id=Maps.ForestMillBack,x=608.0,y=0.0,z=585.0,rotation=2707,group=3,logicregion=Regions.MillChunkyArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Next to Diddy Pad',level=Levels.FungiForest,map_id=Maps.FungiForest,x=3396.0,y=272.0,z=4551.0,rotation=345,group=2,logicregion=Regions.MillArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest - Forest Thornvine Barn: Next to ladder',level=Levels.FungiForest,map_id=Maps.ForestThornvineBarn,x=80.0,y=4.0,z=627.0,rotation=2048,group=6,logicregion=Regions.ThornvineBarn,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest - Forest Giant Mushroom: Next to a cannon',level=Levels.FungiForest,map_id=Maps.ForestGiantMushroom,x=127.0,y=1189.0,z=532.0,rotation=1137,group=4,logicregion=Regions.MushroomUpper,logic=lambda l:l.twirl or l.donkey and l.shockwave,resize=''),DirtPatchData(name='Fungi Forest - Forest Giant Mushroom: Next to the cannon below the night door',level=Levels.FungiForest,map_id=Maps.ForestGiantMushroom,x=763.0,y=739.0,z=513.0,rotation=3163,group=4,logicregion=Regions.MushroomUpper,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Next to Crusher Output',level=Levels.FungiForest,map_id=Maps.FungiForest,x=4404.0,y=162.0,z=3520.0,rotation=1525,group=2,logicregion=Regions.MillArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: On the Tomato Field',level=Levels.FungiForest,map_id=Maps.FungiForest,x=3158.0,y=228.0,z=768.0,rotation=989,group=1,logicregion=Regions.WormArea,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Fungi Forest: Near Funky with the fenced in Chunky coins',level=Levels.FungiForest,map_id=Maps.FungiForest,x=3635.0,y=186.0,z=936.0,rotation=2947,group=1,logicregion=Regions.WormArea,logic=lambda l:l.TimeAccess(Regions.WormArea,Time.Night)and l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Giant Kosha Room',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=1820.313,y=231.833,z=3596.593,rotation=2006,vanilla=_A,group=5,logicregion=Regions.GiantKosha,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Crystal Caves: Near lankey's 1DC - lower",level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=2735.0,y=162.0,z=1795.0,rotation=1103,group=1,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Crystal Caves: Near Funky under Diddy's barrel",level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=3013.0,y=253.0,z=931.0,rotation=3716,group=2,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Crystal Caves: Near Diddy's top 5D Cabin door",level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=3610.0,y=343.0,z=1761.0,rotation=3072,group=1,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Near Tag barrel at 5D Cabin',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=3631.0,y=260.0,z=1534.0,rotation=3111,group=1,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Next to Ice Castle',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=2125.0,y=257.0,z=1054.0,rotation=3584,group=2,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Crystal Caves: Next to Lankey's 1DC - upper",level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=2404.0,y=276.0,z=1947.0,rotation=227,group=1,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Crystal Caves: Next to Donkey's 1DC - left",level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=2961.0,y=281.0,z=2370.0,rotation=2400,group=1,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name="Crystal Caves: Next to Donkey's 1DC - right",level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=2666.0,y=282.0,z=2494.0,rotation=2225,group=1,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves - Caves Frozen Castle: Next to Slam Puzzle - left',level=Levels.CrystalCaves,map_id=Maps.CavesFrozenCastle,x=311.0,y=0.0,z=194.0,rotation=3800,group=2,logicregion=Regions.FrozenCastle,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves - Caves Frozen Castle: Next to Slam Puzzle - right',level=Levels.CrystalCaves,map_id=Maps.CavesFrozenCastle,x=227.0,y=0.0,z=404.0,rotation=1786,group=2,logicregion=Regions.FrozenCastle,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: On top of the Igloo',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=576.0,y=142.0,z=1285.0,rotation=1092,group=3,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Under tag barrel near igloo',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=221.0,y=48.0,z=1412.0,rotation=3276,group=3,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Near Primate Punch wall opposite cranky',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=1416.0,y=298.0,z=2430.0,rotation=2275,group=4,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Near Primate Punch wall near entrance',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=2264.0,y=13.0,z=248.0,rotation=3219,group=4,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Crystal Caves: Near Primate Punch wall near snide',level=Levels.CrystalCaves,map_id=Maps.CrystalCaves,x=1473.0,y=98.0,z=850.0,rotation=375,group=4,logicregion=Regions.CrystalCavesMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Top of Castle near shop',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=655.9,y=1794.167,z=1386.9,rotation=3094,vanilla=_A,group=5,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Near the Catacombs Door',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=1319.0,y=523.0,z=1885.0,rotation=3151,group=4,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Upper Gravestone',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=746.0,y=521.0,z=1873.0,rotation=3280,group=4,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Top of Castle near fence',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=1696.0,y=1731.0,z=1384.0,rotation=1479,group=5,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Ballroom: Ballroom - Back Left',level=Levels.CreepyCastle,map_id=Maps.CastleBallroom,x=261.0,y=40.0,z=241.0,rotation=546,group=1,logicregion=Regions.Ballroom,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Ballroom: Ballroom - Back Right',level=Levels.CreepyCastle,map_id=Maps.CastleBallroom,x=825.0,y=40.0,z=258.0,rotation=3310,group=1,logicregion=Regions.Ballroom,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Museum: Museum - Pillar Front',level=Levels.CreepyCastle,map_id=Maps.CastleMuseum,x=1003.0,y=200.0,z=1513.0,rotation=2969,group=2,logicregion=Regions.MuseumBehindGlass,logic=lambda l:l.monkeyport and l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Museum: Museum - Pillar Back Right',level=Levels.CreepyCastle,map_id=Maps.CastleMuseum,x=1238.0,y=200.0,z=1612.0,rotation=2628,group=2,logicregion=Regions.MuseumBehindGlass,logic=lambda l:l.monkeyport and l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Museum: Museum - Pillar Back Left',level=Levels.CreepyCastle,map_id=Maps.CastleMuseum,x=1236.0,y=200.0,z=1400.0,rotation=3697,group=2,logicregion=Regions.MuseumBehindGlass,logic=lambda l:l.monkeyport and l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Next to Greenhouse',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=1588.0,y=1391.0,z=1870.0,rotation=2309,group=5,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Crypt: 3Kong crypt entrance',level=Levels.CreepyCastle,map_id=Maps.CastleCrypt,x=626.0,y=240.0,z=1674.0,rotation=3072,group=3,logicregion=Regions.Crypt,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Mausoleum: 2kong crypt entrance',level=Levels.CreepyCastle,map_id=Maps.CastleMausoleum,x=731.0,y=240.0,z=1068.0,rotation=3072,group=3,logicregion=Regions.Mausoleum,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Between the catacombs door and Tiny Kasplat',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=245.0,y=366.0,z=1810.0,rotation=3766,group=4,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Next to the Drawing Drawbridge',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=662.0,y=548.0,z=522.0,rotation=2814,group=4,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle: Next to Lanky coin tree (near catacombs door)',level=Levels.CreepyCastle,map_id=Maps.CreepyCastle,x=1691.0,y=372.0,z=1995.0,rotation=3561,group=4,logicregion=Regions.CreepyCastleMain,logic=lambda l:l.shockwave,resize=''),DirtPatchData(name='Creepy Castle - Castle Dungeon: Under the chunky balloon without coins',level=Levels.CreepyCastle,map_id=Maps.CastleDungeon,x=316.0,y=115.0,z=2525.0,rotation=1024,group=3,logicregion=Regions.Dungeon,logic=lambda l:l.punch and l.shockwave,resize='')]