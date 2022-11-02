'Stores the data for each potential kasplat location.'
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.MapsAndExits import Maps
class KasplatLocation:
	'Class which stores name and logic for a kasplat location.'
	def __init__(A,*,name='No Location',map_id=0,kong_lst=[],coords=[0,0,0],xmin=0,xmax=0,zmin=0,zmax=0,region,additional_logic=None,vanilla=False):
		'Initialize with given parameters.';B=additional_logic;A.name=name;A.map=map_id;A.kong_lst=kong_lst;A.coords=coords;A.bounds=[xmin,xmax,zmin,zmax];A.selected=False;A.vanilla=vanilla;A.region_id=region
		if B is None:A.additional_logic=lambda l:_A
		else:A.additional_logic=B
	def setKasplat(A,state=_A):"Set Kasplat's collection state.";A.selected=state
KasplatLocationList={Levels.JungleJapes:[KasplatLocation(name='Japes Kasplat: Behind Rambi Wall',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[870,280,3578],xmin=740,xmax=990,zmin=3500,zmax=3700,region=Regions.BeyondRambiGate),KasplatLocation(name='Japes Kasplat: On top of mountain',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1592,989,2443],xmin=1570,xmax=1650,zmin=2380,zmax=2490,region=Regions.JapesTopOfMountain),KasplatLocation(name='Japes Kasplat: Beehive Area',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2270,552,3153],xmin=2180,xmax=2450,zmin=3050,zmax=3280,region=Regions.JapesBeyondFeatherGate),KasplatLocation(name='Japes Kasplat: Lower area of Tunnel to Beehive',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2769,335,2071],region=Regions.JapesBeyondCoconutGate1,vanilla=_A),KasplatLocation(name='Japes Kasplat: Upper area of Tunnel to Beehive',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3180,437,2379],region=Regions.JapesBeyondCoconutGate1,vanilla=_A),KasplatLocation(name='Japes Kasplat: Underground',map_id=Maps.JapesUnderGround,kong_lst=[Kongs.chunky],coords=[427,20,456],region=Regions.JapesCatacomb,additional_logic=lambda l:l.pineapple,vanilla=_A),KasplatLocation(name='Japes Kasplat: Near Speedy Swing Sortie Bonus',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2014,251,2767],region=Regions.JapesBeyondCoconutGate2,vanilla=_A),KasplatLocation(name='Japes Kasplat: Near Painting Room',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[884,280,2578],region=Regions.JapesBeyondCoconutGate2,vanilla=_A),KasplatLocation(name="Japes Kasplat: Inside Tiny's Cage",map_id=Maps.JungleJapes,kong_lst=[Kongs.tiny],coords=[1333,280,1938],xmin=1320,xmax=1360,zmin=1910,zmax=1960,region=Regions.JapesBeyondCoconutGate2,additional_logic=lambda l:Events.Rambi in l.Events and l.Slam and l.tiny),KasplatLocation(name='Japes Kasplat: Starting Area',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[899,280,640],xmin=800,xmax=1100,zmin=460,zmax=800,region=Regions.JungleJapesMain),KasplatLocation(name='Japes Kasplat: Diddy Cave',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2461,280,548],xmin=2370,xmax=2620,zmin=350,zmax=650,region=Regions.JapesBeyondPeanutGate),KasplatLocation(name='Japes Kasplat: In the river',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1600,165,1700],xmin=1550,xmax=1650,zmin=1650,zmax=1800,region=Regions.JungleJapesMain,additional_logic=lambda l:l.swim and(l.oranges or l.HasGun(Kongs.any)or l.HasInstrument(Kongs.any))),KasplatLocation(name='Japes Kasplat: In the water near Rambi Wall',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[382,140,2818],xmin=360,xmax=500,zmin=2700,zmax=2900,region=Regions.BeyondRambiGate,additional_logic=lambda l:l.swim and(l.oranges or l.HasGun(Kongs.any)or l.HasInstrument(Kongs.any))),KasplatLocation(name="Japes Kasplat: Near Cranky's",map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1675,280,4197],xmin=1420,xmax=1950,zmin=4050,zmax=4350,region=Regions.JapesBeyondCoconutGate2),KasplatLocation(name='Japes Kasplat: In the T&S Alcove',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[773,538,2320],xmin=720,xmax=800,zmin=2295,zmax=2380,region=Regions.JungleJapesMain,additional_logic=lambda l:l.vines),KasplatLocation(name='Japes Kasplat: Inside the Mountain',map_id=Maps.JapesMountain,kong_lst=[Kongs.diddy],coords=[551,101,1192],xmin=525,xmax=576,zmin=1078,zmax=1236,region=Regions.Mine),KasplatLocation(name='Japes Kasplat: Inside the Shell',map_id=Maps.JapesTinyHive,kong_lst=[Kongs.tiny],coords=[1371,213,1400],xmin=1217,xmax=1468,zmin=1288,zmax=1482,region=Regions.TinyHive),KasplatLocation(name='Japes Kasplat: Up the Hill to the Painting Room',map_id=Maps.JungleJapes,kong_lst=[Kongs.lanky,Kongs.tiny],coords=[544,370,1815],xmin=508,xmax=583,zmin=1778,zmax=1927,region=Regions.JungleJapesMain,additional_logic=lambda l:l.lanky and l.handstand or l.tiny and l.twirl),KasplatLocation(name='Japes Kasplat: In the Minecart Exit',map_id=Maps.JungleJapes,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1105,290,1965],xmin=1080,xmax=1124,zmin=1945,zmax=1985,region=Regions.JungleJapesMain)],Levels.AngryAztec:[KasplatLocation(name='Aztec Kasplat: In the Stealthy Snoop Tunnel',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2738,120,4763],xmin=2640,xmax=2825,zmin=4650,zmax=4850,region=Regions.AztecDonkeyQuicksandCave),KasplatLocation(name='Aztec Kasplat: On the Oasis',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2467,116,990],xmin=2350,xmax=2500,zmin=880,zmax=1050,region=Regions.AngryAztecOasis),KasplatLocation(name="Aztec Kasplat: On the Llama's Cage",map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2130,310,1588],xmin=2110,xmax=2155,zmin=1525,zmax=1590,region=Regions.AngryAztecOasis,additional_logic=lambda l:l.vines or l.jetpack and l.isdiddy),KasplatLocation(name='Aztec Kasplat: Near the giant boulder',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3782,120,2391],xmin=3660,xmax=4060,zmin=2310,zmax=2510,region=Regions.AngryAztecMain),KasplatLocation(name='Aztec Kasplat: Behind the DK Stone Door',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1363,162,738],region=Regions.AngryAztecOasis,additional_logic=lambda l:l.coconut and(l.strongKong and l.isdonkey or l.settings.damage_amount=='default'),vanilla=_A),KasplatLocation(name='Aztec Kasplat: In the lava room in Llama Temple',map_id=Maps.AztecLlamaTemple,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1378,420,3632],region=Regions.LlamaTempleBack,vanilla=_A),KasplatLocation(name='Aztec Kasplat: Near the Hunky Chunky Barrel',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3162,120,1845],region=Regions.AngryAztecMain,vanilla=_A),KasplatLocation(name='Aztec Kasplat: On Tiny Temple',map_id=Maps.AngryAztec,kong_lst=[Kongs.diddy],coords=[3169,445,647],region=Regions.AngryAztecOasis,additional_logic=lambda l:l.jetpack,vanilla=_A),KasplatLocation(name='Aztec Kasplat: In the Vase Room',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[406,138,701],xmin=300,xmax=420,zmin=650,zmax=750,region=Regions.BetweenVinesByPortal,additional_logic=lambda l:l.chunky and l.pineapple),KasplatLocation(name='Aztec Kasplat: Behind the 5-Door Temple',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1997,280,3500],xmin=1970,xmax=2020,zmin=3470,zmax=3520,region=Regions.AngryAztecMain),KasplatLocation(name="Aztec Kasplat: Near Snide's",map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3969,190,4037],xmin=3930,xmax=4020,zmin=3990,zmax=4080,region=Regions.AngryAztecMain),KasplatLocation(name='Aztec Kasplat: Below the Llama in Llama Temple',map_id=Maps.AztecLlamaTemple,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1964,472,2408],xmin=1860,xmax=2010,zmin=2360,zmax=2440,region=Regions.LlamaTemple),KasplatLocation(name='Aztec Kasplat: In the Free Tiny Room',map_id=Maps.AztecTinyTemple,kong_lst=[Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[453,345,1465],xmin=140,xmax=720,zmin=1200,zmax=1700,region=Regions.TempleUnderwater),KasplatLocation(name='Aztec Kasplat: In Chunky 5-Door Temple',map_id=Maps.AztecChunky5DTemple,kong_lst=[Kongs.chunky],coords=[936,122,2027],region=Regions.ChunkyTemple,additional_logic=lambda l:l.ischunky and l.pineapple,vanilla=_A),KasplatLocation(name='Aztec Kasplat: Behind the Beetle Race',map_id=Maps.AngryAztec,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[4458,81,2924],xmin=4364,xmax=4510,zmin=2887,zmax=2942,region=Regions.AngryAztecMain),KasplatLocation(name='Aztec Kasplat: Inside the Llama Temple Matching Game',map_id=Maps.AztecLlamaTemple,kong_lst=[Kongs.lanky],coords=[1080,642,2240],xmin=1009,xmax=1161,zmin=2130,zmax=2332,region=Regions.LlamaTemple,additional_logic=lambda l:l.grape),KasplatLocation(name='Aztec Kasplat: Inside Tiny Temple by Mini Monkey Barrel',map_id=Maps.AztecTinyTemple,kong_lst=[Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1767,330,1093],xmin=1761,xmax=1821,zmin=1053,zmax=1113,region=Regions.TempleStart),KasplatLocation(name='Aztec Kasplat: In Donkey 5-Door Temple',map_id=Maps.AztecDonkey5DTemple,kong_lst=[Kongs.donkey],coords=[99,21,390],xmin=68,xmax=130,zmin=321,zmax=450,region=Regions.DonkeyTemple,additional_logic=lambda l:l.coconut and l.isdonkey)],Levels.FranticFactory:[KasplatLocation(name='Factory Kasplat: Starting Area',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1712,837,2389],xmin=1680,xmax=1740,zmin=2300,zmax=2440,region=Regions.FranticFactoryStart),KasplatLocation(name='Factory Kasplat: Near the Power Hut',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1464,127,865],xmin=1400,xmax=1540,zmin=840,zmax=920,region=Regions.ChunkyRoomPlatform),KasplatLocation(name='Factory Kasplat: Down the pole covered by a Hatch',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[646,460,1792],xmin=600,xmax=700,zmin=1740,zmax=1820,region=Regions.BeyondHatch),KasplatLocation(name='Factory Kasplat: In the Dark Room',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2053,7,573],xmin=2000,xmax=2100,zmin=500,zmax=850,region=Regions.BeyondHatch,additional_logic=lambda l:l.punch and l.chunky),KasplatLocation(name='Factory Kasplat: On the lowest platform in Production Room',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[633,157,1672],xmin=550,xmax=730,zmin=1645,zmax=1705,region=Regions.MiddleCore),KasplatLocation(name='Factory Kasplat: Near the slippery pipe in Production Room',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[782,557,1686],region=Regions.UpperCore,vanilla=_A),KasplatLocation(name='Factory Kasplat: At the base of Production Room',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[509,0,1591],region=Regions.BeyondHatch,vanilla=_A),KasplatLocation(name='Factory Kasplat: In Research & Development',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[4148,1336,1016],region=Regions.RandD,vanilla=_A),KasplatLocation(name='Factory Kasplat: Below the pole to the DK Arcade Machine',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1296,6,240],region=Regions.BeyondHatch,vanilla=_A),KasplatLocation(name='Factory Kasplat: In Block Tower Room',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2234,1026,1372],region=Regions.Testing,vanilla=_A),KasplatLocation(name="Factory Kasplat: Near Snide's",map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1579,811,2197],xmin=1510,xmax=1660,zmin=2120,zmax=2240,region=Regions.Testing),KasplatLocation(name='Factory Kasplat: In the Power Shed',map_id=Maps.FactoryPowerHut,kong_lst=[Kongs.donkey],coords=[116,2,121],xmin=68,xmax=151,zmin=66,zmax=154,region=Regions.PowerHut),KasplatLocation(name='Factory Kasplat: In R&D by the Slot Car Race',map_id=Maps.FranticFactory,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3701,1264,1405],xmin=3659,xmax=3718,zmin=1385,zmax=1459,region=Regions.RandD),KasplatLocation(name="Factory Kasplat: Inside Tiny's Shooting Game",map_id=Maps.FranticFactory,kong_lst=[Kongs.tiny],coords=[2504,1107,938],xmin=2472,xmax=2558,zmin=859,zmax=942,region=Regions.Testing,additional_logic=lambda l:l.mini),KasplatLocation(name='Factory Kasplat: Inside the Crusher Room',map_id=Maps.FactoryCrusher,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[484,1,491],xmin=451,xmax=510,zmin=414,zmax=509,region=Regions.InsideCore),KasplatLocation(name='Factory Kasplat: Past the Tiny Bonus Barrel in Upper Production',map_id=Maps.FranticFactory,kong_lst=[Kongs.tiny],coords=[380,859,1600],xmin=373,xmax=387,zmin=1589,zmax=1610,region=Regions.UpperCore,additional_logic=lambda l:l.twirl),KasplatLocation(name="Factory Kasplat: In Lanky's Piano Game",map_id=Maps.FranticFactory,kong_lst=[Kongs.lanky],coords=[3504,1265,550],xmin=3459,xmax=3510,zmin=487,zmax=563,region=Regions.RandD,additional_logic=lambda l:l.trombone)],Levels.GloomyGalleon:[KasplatLocation(name='Galleon Kasplat: On the Lighthouse island',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1631,1611,4162],xmin=1625,xmax=1670,zmin=4100,zmax=4185,region=Regions.LighthousePlatform),KasplatLocation(name="Galleon Kasplat: On Diddy's Gold Tower",map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2037,1750,769],region=Regions.TreasureRoomDiddyGoldTower,vanilla=_A),KasplatLocation(name='Galleon Kasplat: In the Alcove near the Lighthouse',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[699,1564,4093],region=Regions.LighthouseSurface,vanilla=_A),KasplatLocation(name='Galleon Kasplat: On the platforms in Cannon Game Room',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1308,1610,2794],region=Regions.GalleonBeyondPineappleGate,additional_logic=lambda l:Events.WaterSwitch in l.Events,vanilla=_A),KasplatLocation(name="Galleon Kasplat: Near the T&S near Cranky's",map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2806,1890,2969],region=Regions.GalleonPastVines,vanilla=_A),KasplatLocation(name='Galleon Kasplat: On the Cactus near the sunken submarine',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[4372,1650,1031],region=Regions.Shipyard,vanilla=_A),KasplatLocation(name='Galleon Kasplat: On the Crown Pad',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3323,1680,2387],xmin=3240,xmax=3360,zmin=2370,zmax=2500,region=Regions.GloomyGalleonStart,additional_logic=lambda l:l.punch and l.chunky),KasplatLocation(name="Galleon Kasplat: Next to Cranky's",map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3314,1792,2498],xmin=3260,xmax=3370,zmin=2440,zmax=2540,region=Regions.GloomyGalleonStart),KasplatLocation(name='Galleon Kasplat: Inside the Lighthouse at the Top',map_id=Maps.GalleonLighthouse,kong_lst=[Kongs.donkey],coords=[448,721,514],xmin=426,xmax=475,zmin=501,zmax=530,region=Regions.Lighthouse),KasplatLocation(name='Galleon Kasplat: Inside the Mechfish',map_id=Maps.GalleonMechafish,kong_lst=[Kongs.diddy],coords=[314,25,528],xmin=303,xmax=322,zmin=497,zmax=537,region=Regions.Mechafish),KasplatLocation(name="Galleon Kasplat: On Lanky's Gold Tower",map_id=Maps.GloomyGalleon,kong_lst=[Kongs.lanky],coords=[1658,2042,490],xmin=1650,xmax=1664,zmin=481,zmax=498,region=Regions.TreasureRoom,additional_logic=lambda l:l.balloon),KasplatLocation(name="Galleon Kasplat: In Chunky's Drunk Ship",map_id=Maps.GalleonSickBay,kong_lst=[Kongs.chunky],coords=[571,21,922],xmin=522,xmax=637,zmin=852,zmax=944,region=Regions.SickBay),KasplatLocation(name='Galleon Kasplat: On the Middle Deck of the Shipwreck',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3076,1791,3377],xmin=3016,xmax=3128,zmin=3342,zmax=3426,region=Regions.GloomyGalleonStart),KasplatLocation(name='Galleon Kasplat: Starting Area',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2087,1621,2836],xmin=2055,xmax=2143,zmin=2772,zmax=2924,region=Regions.GloomyGalleonStart),KasplatLocation(name='Galleon Kasplat: Inside a Punchable Chest',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3537,1671,3905],xmin=3536,xmax=3538,zmin=3904,zmax=3906,region=Regions.GloomyGalleonStart,additional_logic=lambda l:l.punch and l.chunky),KasplatLocation(name='Galleon Kasplat: Also on the Cactus near the sunken submarine',map_id=Maps.GloomyGalleon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[4398,1651,1007],xmin=4354,xmax=4405,zmin=1003,zmax=1052,region=Regions.Shipyard)],Levels.FungiForest:[KasplatLocation(name='Forest Kasplat: Behind the Diddy Dark Barn',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3150,273,4332],xmin=3100,xmax=3200,zmin=4330,zmax=4420,region=Regions.MillArea),KasplatLocation(name='Forest Kasplat: Behind the beanstalk',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1853,230,473],xmin=1780,xmax=1890,zmin=380,zmax=780,region=Regions.WormArea),KasplatLocation(name='Forest Kasplat: Near the rocketbarrel near the Giant Mushroom',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[183,241,756],xmin=100,xmax=380,zmin=650,zmax=940,region=Regions.GiantMushroomArea),KasplatLocation(name='Forest Kasplat: On the top floor of the Giant Mushroom',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[850,1250,550],xmin=770,xmax=1060,zmin=530,zmax=580,region=Regions.MushroomUpperExterior),KasplatLocation(name='Forest Kasplat: Near the sleeping Rabbit',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2335,143,3639],xmin=2150,xmax=2450,zmin=3540,zmax=3730,region=Regions.HollowTreeArea),KasplatLocation(name="Forest Kasplat: Near the T&S near the Owl's Tree",map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[543,194,3748],xmin=320,xmax=850,zmin=3600,zmax=4080,region=Regions.HollowTreeArea),KasplatLocation(name="Forest Kasplat: Behind DK's Barn",map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3693,115,1546],region=Regions.ThornvineArea,vanilla=_A),KasplatLocation(name='Forest Kasplat: Inside the Giant Mushroom',map_id=Maps.ForestGiantMushroom,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[329,534,402],region=Regions.MushroomUpper,vanilla=_A),KasplatLocation(name="Forest Kasplat: Under the Owl's Tree",map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1270,249,3927],region=Regions.HollowTreeArea,vanilla=_A),KasplatLocation(name='Forest Kasplat: On a low platform on the exterior of Giant Mushroom',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1209,389,678],region=Regions.MushroomLowerExterior,vanilla=_A),KasplatLocation(name='Forest Kasplat: On a high platform on the exterior of Giant Mushroom',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[732,979,597],region=Regions.MushroomNightExterior,vanilla=_A),KasplatLocation(name='Forest Kasplat: Behind the Cuckoo Clock',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2297,604,2318],xmin=2275,xmax=2350,zmin=2250,zmax=2400,region=Regions.FungiForestStart),KasplatLocation(name='Forest Kasplat: Inside the mill',map_id=Maps.ForestMillFront,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[360,0,450],xmin=200,xmax=600,zmin=360,zmax=500,region=Regions.GrinderRoom),KasplatLocation(name='Forest Kasplat: In the moat around the Giant Mushroom',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1009,100,576],xmin=740,xmax=1120,zmin=540,zmax=630,region=Regions.GiantMushroomArea,additional_logic=lambda l:l.swim and(l.oranges or l.HasGun(Kongs.any)or l.HasInstrument(Kongs.any))),KasplatLocation(name='Forest Kasplat: At the very top of the Giant Mushroom',map_id=Maps.FungiForest,kong_lst=[Kongs.diddy,Kongs.lanky],coords=[949,1501,1010],xmin=852,xmax=962,zmin=974,zmax=1063,region=Regions.MushroomUpperExterior,additional_logic=lambda l:l.jetpack or l.handstand),KasplatLocation(name='Forest Kasplat: On the Mill Roof',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[4275,377,3639],xmin=4248,xmax=4300,zmin=3609,zmax=3664,region=Regions.MillArea),KasplatLocation(name='Forest Kasplat: In the Minecart Exit Well',map_id=Maps.FungiForest,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[5352,240,3677],xmin=5333,xmax=5386,zmin=3655,zmax=3706,region=Regions.MillArea),KasplatLocation(name='Forest Kasplat: In the Lanky Mushroom Slam Room',map_id=Maps.ForestLankyMushroomsRoom,kong_lst=[Kongs.lanky],coords=[289,2,308],xmin=250,xmax=309,zmin=266,zmax=344,region=Regions.MushroomLankyMushroomsRoom),KasplatLocation(name='Forest Kasplat: In the Spider Boss',map_id=Maps.ForestSpider,kong_lst=[Kongs.tiny],coords=[275,173,722],xmin=208,xmax=358,zmin=653,zmax=780,region=Regions.SpiderRoom),KasplatLocation(name='Forest Kasplat: In the Winch Room',map_id=Maps.ForestWinchRoom,kong_lst=[Kongs.diddy],coords=[300,1,280],xmin=267,xmax=336,zmin=227,zmax=335,region=Regions.WinchRoom),KasplatLocation(name="Forest Kasplat: In Chunky's Face Shooting Room",map_id=Maps.ForestChunkyFaceRoom,kong_lst=[Kongs.chunky],coords=[248,1,294],xmin=200,xmax=335,zmin=209,zmax=384,region=Regions.MushroomChunkyRoom)],Levels.CrystalCaves:[KasplatLocation(name="Caves Kasplat: Near Snide's",map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1242,65,585],xmin=1160,xmax=1340,zmin=500,zmax=640,region=Regions.CavesSnideArea),KasplatLocation(name="Caves Kasplat: In the room with Tiny's Bonus Barrel",map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[485,181,2495],xmin=360,xmax=550,zmin=2350,zmax=2600,region=Regions.CavesBonusCave),KasplatLocation(name='Caves Kasplat: Inside an Ice Shield',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[768,50,801],xmin=720,xmax=800,zmin=750,zmax=830,region=Regions.IglooArea,additional_logic=lambda l:Events.CavesLargeBoulderButton in l.Events),KasplatLocation(name='Caves Kasplat: On the Cabin with 5 Doors',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3645,343,1865],xmin=3590,xmax=3650,zmin=1580,zmax=1880,region=Regions.CabinArea),KasplatLocation(name="Caves Kasplat: Across the river from Candy's",map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3003,123,1569],xmin=2982,xmax=3013,zmin=1535,zmax=1621,region=Regions.CabinArea),KasplatLocation(name='Caves Kasplat: In the room with the Giant Boulder',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1915,280,2676],xmin=1830,xmax=2040,zmin=2590,zmax=2770,region=Regions.BoulderCave),KasplatLocation(name='Caves Kasplat: Near the Ice Castle',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1705,285,745],region=Regions.CrystalCavesMain,vanilla=_A),KasplatLocation(name="Caves Kasplat: In the Hidden Room by Funky's",map_id=Maps.CrystalCaves,kong_lst=[Kongs.diddy,Kongs.tiny],coords=[3517,286,767],region=Regions.CavesBlueprintCave,vanilla=_A),KasplatLocation(name="Caves Kasplat: On the platform near Funky's",map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2783,366,927],region=Regions.CavesBlueprintPillar,vanilla=_A),KasplatLocation(name='Caves Kasplat: By the Far Warp 2',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2911,379,1858],region=Regions.CabinArea,vanilla=_A),KasplatLocation(name='Caves Kasplat: On the 5-Door Igloo',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[577,142,1285],region=Regions.IglooArea,vanilla=_A),KasplatLocation(name='Caves Kasplat: In the water by the Baboon Blast Pad',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1340,14,2047],xmin=1240,xmax=1490,zmin=1920,zmax=2170,region=Regions.CrystalCavesMain),KasplatLocation(name="Caves Kasplat: Inbetween Funky's and the Ice Castle",map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2659,140,1158],xmin=2622,xmax=2690,zmin=1126,zmax=1179,region=Regions.CrystalCavesMain),KasplatLocation(name='Caves Kasplat: At the Start of the Beetle Race',map_id=Maps.CavesLankyRace,kong_lst=[Kongs.lanky],coords=[1367,5111,647],xmin=1355,xmax=1399,zmin=632,zmax=657,region=Regions.CavesLankyRace),KasplatLocation(name='Caves Kasplat: With the Giant Kosha',map_id=Maps.CrystalCaves,kong_lst=[Kongs.tiny],coords=[1768,232,3645],xmin=1753,xmax=1892,zmin=3543,zmax=3675,region=Regions.GiantKosha),KasplatLocation(name="Caves Kasplat: In Diddy's Igloo",map_id=Maps.CavesDiddyIgloo,kong_lst=[Kongs.diddy],coords=[265,1,290],xmin=192,xmax=333,zmin=201,zmax=391,region=Regions.DiddyIgloo),KasplatLocation(name="Caves Kasplat: In Donkey's Shooting Cabin",map_id=Maps.CavesDonkeyCabin,kong_lst=[Kongs.donkey],coords=[377,1,429],xmin=345,xmax=395,zmin=385,zmax=466,region=Regions.DonkeyCabin),KasplatLocation(name='Caves Kasplat: In the Gorilla Gone Cave',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2578,14,426],xmin=2513,xmax=2674,zmin=391,zmax=543,region=Regions.CrystalCavesMain,additional_logic=lambda l:l.punch and l.chunky),KasplatLocation(name='Caves Kasplat: Starting Area',map_id=Maps.CrystalCaves,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1756,-28,236],xmin=1658,xmax=1819,zmin=174,zmax=323,region=Regions.CrystalCavesMain)],Levels.CreepyCastle:[KasplatLocation(name='Castle Kasplat: Behind the Mausoleum',map_id=Maps.CastleLowerCave,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1839,320,1278],xmin=1790,xmax=1900,zmin=1160,zmax=1360,region=Regions.LowerCave),KasplatLocation(name='Castle Kasplat: Inside the Dungeon',map_id=Maps.CastleDungeon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[526,195,2013],xmin=480,xmax=600,zmin=1866,zmax=2139,region=Regions.Dungeon),KasplatLocation(name='Castle Kasplat: Near the T&S at the back of Castle',map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1655,371,2048],xmin=1600,xmax=1720,zmin=1970,zmax=2090,region=Regions.CreepyCastleMain),KasplatLocation(name='Castle Kasplat: Inside the Ballroom',map_id=Maps.CastleBallroom,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[547,45,613],xmin=340,xmax=770,zmin=330,zmax=880,region=Regions.Ballroom),KasplatLocation(name='Castle Kasplat: At the top of the Castle',map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1388,1732,1353],xmin=1250,xmax=1450,zmin=1180,zmax=1500,region=Regions.CreepyCastleMain),KasplatLocation(name='Castle Kasplat: Inside the Tree',map_id=Maps.CastleTree,kong_lst=[Kongs.donkey],coords=[937,400,1424],region=Regions.CastleTree,additional_logic=lambda l:l.coconut and l.isdonkey,vanilla=_A),KasplatLocation(name='Castle Kasplat: In the Lower Cave straight ahead',map_id=Maps.CastleLowerCave,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1112,200,1242],region=Regions.LowerCave,vanilla=_A),KasplatLocation(name='Castle Kasplat: Near the upper Warp 2',map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1892,904,1626],region=Regions.CreepyCastleMain,vanilla=_A),KasplatLocation(name='Castle Kasplat: Near the Crypt Entrance on a lone platform',map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[66,392,911],region=Regions.CreepyCastleMain,vanilla=_A),KasplatLocation(name="Castle Kasplat: Near Candy's",map_id=Maps.CastleUpperCave,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[536,220,2205],region=Regions.UpperCave,vanilla=_A),KasplatLocation(name='Castle Kasplat: In the water near the Tree',map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[845,330,235],xmin=780,xmax=930,zmin=150,zmax=300,region=Regions.CreepyCastleMain,additional_logic=lambda l:l.swim and(l.oranges or l.HasGun(Kongs.any)or l.HasInstrument(Kongs.any))),KasplatLocation(name="Castle Kasplat: Near Cranky's Hut",map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[435,1136,1389],xmin=320,xmax=540,zmin=1335,zmax=1455,region=Regions.CreepyCastleMain),KasplatLocation(name='Castle Kasplat: Near the Rocketbarrel by the drawbridge',map_id=Maps.CreepyCastle,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[195,623,542],xmin=140,xmax=220,zmin=500,zmax=570,region=Regions.CreepyCastleMain),KasplatLocation(name='Castle Kasplat: Inside the Greenhouse Maze',map_id=Maps.CastleGreenhouse,kong_lst=[Kongs.lanky],coords=[347,1,596],xmin=320,xmax=377,zmin=569,zmax=625,region=Regions.Greenhouse),KasplatLocation(name='Castle Kasplat: By the Mysterious Pedestal in the Museum',map_id=Maps.CastleMuseum,kong_lst=[Kongs.tiny],coords=[1007,201,1509],xmin=975,xmax=1054,zmin=1430,zmax=1568,region=Regions.MuseumBehindGlass,additional_logic=lambda l:l.monkeyport),KasplatLocation(name='Castle Kasplat: In a Cage in the Dungeon',map_id=Maps.CastleDungeon,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[800,196,2216],xmin=778,xmax=814,zmin=2208,zmax=2232,region=Regions.Dungeon,additional_logic=lambda l:l.punch),KasplatLocation(name='Castle Kasplat: By the Entrance to the Minecart',map_id=Maps.CastleCrypt,kong_lst=[Kongs.donkey],coords=[1517,196,2316],xmin=1468,xmax=1582,zmin=2265,zmax=2406,region=Regions.Crypt,additional_logic=lambda l:l.coconut),KasplatLocation(name='Castle Kasplat: In the Library',map_id=Maps.CastleLibrary,kong_lst=[Kongs.donkey],coords=[354,191,495],xmin=257,xmax=430,zmin=456,zmax=573,region=Regions.Library),KasplatLocation(name='Castle Kasplat: In the Clouds',map_id=Maps.CreepyCastle,kong_lst=[Kongs.diddy],coords=[1860,2032,1340],xmin=1850,xmax=1882,zmin=1335,zmax=1359,region=Regions.CreepyCastleMain,additional_logic=lambda l:l.jetpack)],Levels.DKIsles:[KasplatLocation(name='Isles Kasplat: On the Beaver Beach',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[3557,497,1555],xmin=3410,xmax=3740,zmin=1460,zmax=1950,region=Regions.IslesMain),KasplatLocation(name='Isles Kasplat: Inside Factory Lobby above the DK Portal',map_id=Maps.FranticFactoryLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[676,134,372],xmin=640,xmax=710,zmin=330,zmax=430,region=Regions.FranticFactoryLobby,additional_logic=lambda l:l.grab and l.donkey),KasplatLocation(name='Isles Kasplat: Inside Hideout Helm Lobby',map_id=Maps.HideoutHelmLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[335,191,637],region=Regions.HideoutHelmLobby,additional_logic=lambda l:l.scope and l.coconut,vanilla=_A),KasplatLocation(name='Isles Kasplat: Inside Creepy Castle Lobby',map_id=Maps.CreepyCastleLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[577,71,766],region=Regions.CreepyCastleLobby,additional_logic=lambda l:l.coconut and l.donkey,vanilla=_A),KasplatLocation(name='Isles Kasplat: Inside Crystal Caves Lobby',map_id=Maps.CrystalCavesLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1674,13,685],region=Regions.CrystalCavesLobby,additional_logic=lambda l:l.punch and l.chunky,vanilla=_A),KasplatLocation(name='Isles Kasplat: Inside Factory Lobby in the ? Box',map_id=Maps.FranticFactoryLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[244,20,155],region=Regions.FranticFactoryLobby,additional_logic=lambda l:l.punch and l.chunky,vanilla=_A),KasplatLocation(name='Isles Kasplat: Inside Gloomy Galleon Lobby',map_id=Maps.GloomyGalleonLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[762,119,900],region=Regions.GloomyGalleonLobby,vanilla=_A),KasplatLocation(name='Isles Kasplat: Inside the Rock which is blown up',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[4449,552,1673],xmin=4260,xmax=4560,zmin=1520,zmax=1780,region=Regions.IslesMain,additional_logic=lambda l:Events.IslesChunkyBarrelSpawn in l.Events and l.hunkyChunky and l.Slam and l.chunky),KasplatLocation(name='Isles Kasplat: At the back of Kroc Isle halfway up',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2357,1199,3903],xmin=2320,xmax=2440,zmin=3855,zmax=3910,region=Regions.CrocodileIsleBeyondLift),KasplatLocation(name='Isles Kasplat: On the Big X Platform',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1578,499,457],xmin=1475,xmax=1685,zmin=330,zmax=565,region=Regions.IslesMain),KasplatLocation(name='Isles Kasplat: Behind the house to Fungi Lobby',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2449,1498,785],xmin=2430,xmax=2480,zmin=760,zmax=800,region=Regions.CabinIsle),KasplatLocation(name='Isles Kasplat: On the upper platform in Caves Lobby',map_id=Maps.CrystalCavesLobby,kong_lst=[Kongs.diddy],coords=[794,281,707],xmin=774,xmax=824,zmin=673,zmax=747,region=Regions.CrystalCavesLobby,additional_logic=lambda l:l.jetpack),KasplatLocation(name='Isles Kasplat: Behind the Feather Gate in Aztec Lobby',map_id=Maps.AngryAztecLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1073,1,675],xmin=973,xmax=1143,zmin=653,zmax=708,region=Regions.AngryAztecLobby,additional_logic=lambda l:l.feather),KasplatLocation(name='Isles Kasplat: Inside the Prison Sprint Cage',map_id=Maps.KLumsy,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[1328,96,373],xmin=1327,xmax=1329,zmin=372,zmax=374,region=Regions.Prison,additional_logic=lambda l:l.sprint),KasplatLocation(name='Isles Kasplat: Inside Jungle Japes Lobby',map_id=Maps.JungleJapesLobby,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[456,5,528],xmin=262,xmax=653,zmin=293,zmax=642,region=Regions.JungleJapesLobby),KasplatLocation(name='Isles Kasplat: By the Upper Monkeyport Pad',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2420,1721,3883],xmin=2350,xmax=2474,zmin=3847,zmax=3926,region=Regions.IslesMain,additional_logic=lambda l:l.monkeyport and l.tiny),KasplatLocation(name="Isles Kasplat: Near Snide's",map_id=Maps.IslesSnideRoom,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[463,1,304],xmin=394,xmax=553,zmin=164,zmax=382,region=Regions.IslesSnideRoom),KasplatLocation(name='Isles Kasplat: On top of Angry Aztec Lobby',map_id=Maps.Isles,kong_lst=[Kongs.diddy],coords=[3510,1175,1739],xmin=3483,xmax=3532,zmin=1697,zmax=1765,region=Regions.CabinIsle,additional_logic=lambda l:Events.IslesDiddyBarrelSpawn in l.Events and l.jetpack and l.isdiddy),KasplatLocation(name='Isles Kasplat: Beneath the Waterfall',map_id=Maps.Isles,kong_lst=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],coords=[2966,410,1108],xmin=2957,xmax=3016,zmin=1091,zmax=1137,region=Regions.IslesMain,additional_logic=lambda l:l.swim and(l.oranges or l.HasGun(Kongs.any)or l.HasInstrument(Kongs.any)))]}