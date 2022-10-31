'List of maps with in-game index.'
_d='From T&S'
_c='From Castle (Front)'
_b='From Fungi (Low)'
_a='From Fungi (PPunch Door)'
_Z='From Fungi (Front)'
_Y="From T&S (Snide's)"
_X='From Mill (Front)'
_W='From Galleon (DK Entrance)'
_V='From Galleon (Lanky Entrance)'
_U='From Galleon (Diddy Entrance)'
_T='From Car Race'
_S='From Beetle Race'
_R='From Lower Cave'
_Q='From Galleon (Tiny Entrance)'
_P='From Minecart'
_O='From Castle Lobby'
_N='From Caves Lobby'
_M='From Fungi Lobby'
_L='From Galleon Lobby'
_K='From Factory Lobby'
_J='From Aztec Lobby'
_I='From Japes Lobby'
_H='From Training Grounds'
_G="From Candy's"
_F='From Castle Main'
_E="From Funky's"
_D="From Cranky's"
_C='From BBlast'
_B="From Snide's"
_A='From DK Isles'
from enum import IntEnum
from randomizer.LogicClasses import Regions,TransitionBack
from randomizer.Enums.Levels import Levels
class Maps(IntEnum):'List of Maps with in-game index.';Isles=34;BananaFairyRoom=189;JungleJapesLobby=169;AngryAztecLobby=173;IslesSnideRoom=195;FranticFactoryLobby=175;GloomyGalleonLobby=174;FungiForestLobby=178;CrystalCavesLobby=194;CreepyCastleLobby=193;HideoutHelmLobby=170;TrainingGrounds=176;Treehouse=171;KLumsy=97;JungleJapes=7;JapesTinyHive=12;JapesLankyCave=13;JapesMountain=4;JapesMinecarts=6;JapesUnderGround=33;JapesBaboonBlast=37;AngryAztec=38;AztecTinyTemple=16;AztecDonkey5DTemple=19;AztecDiddy5DTemple=21;AztecLanky5DTemple=23;AztecTiny5DTemple=22;AztecChunky5DTemple=24;AztecTinyRace=14;AztecLlamaTemple=20;AztecBaboonBlast=41;FranticFactory=26;FactoryTinyRace=27;FactoryPowerHut=29;FactoryCrusher=36;FactoryBaboonBlast=110;GloomyGalleon=30;GalleonLighthouse=49;GalleonMermaidRoom=45;GalleonSickBay=31;GalleonSealRace=39;GalleonTreasureChest=44;GalleonSubmarine=179;GalleonMechafish=51;Galleon5DShipDKTiny=46;Galleon5DShipDiddyLankyChunky=43;Galleon2DShip=47;GalleonBaboonBlast=54;FungiForest=48;ForestMinecarts=55;ForestGiantMushroom=64;ForestChunkyFaceRoom=71;ForestLankyZingersRoom=70;ForestLankyMushroomsRoom=63;ForestAnthill=52;ForestMillFront=61;ForestMillBack=62;ForestSpider=60;ForestRafters=56;ForestWinchRoom=57;ForestMillAttic=58;ForestThornvineBarn=59;ForestBaboonBlast=188;CrystalCaves=72;CavesLankyRace=82;CavesFrozenCastle=98;CavesDonkeyIgloo=86;CavesDiddyIgloo=100;CavesLankyIgloo=85;CavesTinyIgloo=84;CavesChunkyIgloo=95;CavesRotatingCabin=89;CavesDonkeyCabin=91;CavesDiddyLowerCabin=92;CavesDiddyUpperCabin=200;CavesLankyCabin=94;CavesTinyCabin=93;CavesChunkyCabin=90;CavesBaboonBlast=186;CreepyCastle=87;CastleTree=164;CastleLibrary=114;CastleBallroom=88;CastleMuseum=113;CastleTinyRace=185;CastleTower=105;CastleGreenhouse=168;CastleTrashCan=167;CastleShed=166;CastleLowerCave=183;CastleCrypt=112;CastleMinecarts=106;CastleMausoleum=108;CastleUpperCave=151;CastleDungeon=163;CastleBaboonBlast=187;HideoutHelm=17;JapesBoss=8;AztecBoss=197;FactoryBoss=154;GalleonBoss=111;FungiBoss=83;CavesBoss=196;CastleBoss=199;KroolDonkeyPhase=203;KroolDiddyPhase=204;KroolLankyPhase=205;KroolTinyPhase=206;KroolChunkyPhase=207;BattyBarrelBanditVEasy=32;BattyBarrelBanditEasy=121;BattyBarrelBanditNormal=122;BattyBarrelBanditHard=123;BigBugBashVEasy=102;BigBugBashEasy=148;BigBugBashNormal=149;BigBugBashHard=150;BusyBarrelBarrageEasy=78;BusyBarrelBarrageNormal=79;BusyBarrelBarrageHard=131;MadMazeMaulEasy=68;MadMazeMaulNormal=69;MadMazeMaulHard=66;MadMazeMaulInsane=124;MinecartMayhemEasy=77;MinecartMayhemNormal=129;MinecartMayhemHard=130;BeaverBotherEasy=104;BeaverBotherNormal=136;BeaverBotherHard=137;TeeteringTurtleTroubleVEasy=18;TeeteringTurtleTroubleEasy=118;TeeteringTurtleTroubleNormal=119;TeeteringTurtleTroubleHard=120;StealthySnoopVEasy=126;StealthySnoopEasy=127;StealthySnoopNormal=65;StealthySnoopHard=128;StashSnatchEasy=74;StashSnatchNormal=67;StashSnatchHard=75;StashSnatchInsane=125;SplishSplashSalvageEasy=133;SplishSplashSalvageNormal=96;SplishSplashSalvageHard=132;SpeedySwingSortieEasy=99;SpeedySwingSortieNormal=134;SpeedySwingSortieHard=135;KrazyKongKlamourEasy=101;KrazyKongKlamourNormal=141;KrazyKongKlamourHard=142;KrazyKongKlamourInsane=143;SearchlightSeekVEasy=103;SearchlightSeekEasy=138;SearchlightSeekNormal=139;SearchlightSeekHard=140;KremlingKoshVEasy=10;KremlingKoshEasy=115;KremlingKoshNormal=116;KremlingKoshHard=117;PerilPathPanicVEasy=144;PerilPathPanicEasy=145;PerilPathPanicNormal=146;PerilPathPanicHard=147;HelmBarrelDKTarget=35;HelmBarrelDKRambi=212;HelmBarrelDiddyKremling=165;HelmBarrelDiddyRocketbarrel=201;HelmBarrelLankyMaze=3;HelmBarrelLankyShooting=202;HelmBarrelTinyPTT=210;HelmBarrelTinyMush=50;HelmBarrelChunkyHidden=209;HelmBarrelChunkyShooting=211;JapesCrown=53;AztecCrown=73;FactoryCrown=155;GalleonCrown=156;ForestCrown=159;CavesCrown=160;CastleCrown=161;HelmCrown=162;SnidesCrown=158;LobbyCrown=157;Cranky=5;Candy=25;Funky=1;Snide=15
RegionMapList={Regions.Treehouse:Maps.Treehouse,Regions.TrainingGrounds:Maps.TrainingGrounds,Regions.IslesMain:Maps.Isles,Regions.IslesMainUpper:Maps.Isles,Regions.CrocodileIsleBeyondLift:Maps.Isles,Regions.IslesSnideRoom:Maps.IslesSnideRoom,Regions.CabinIsle:Maps.Isles,Regions.BananaFairyRoom:Maps.BananaFairyRoom,Regions.JungleJapesLobby:Maps.JungleJapesLobby,Regions.AngryAztecLobby:Maps.AngryAztecLobby,Regions.FranticFactoryLobby:Maps.FranticFactoryLobby,Regions.GloomyGalleonLobby:Maps.GloomyGalleonLobby,Regions.FungiForestLobby:Maps.FungiForestLobby,Regions.CrystalCavesLobby:Maps.CrystalCavesLobby,Regions.CreepyCastleLobby:Maps.CreepyCastleLobby,Regions.JungleJapesMain:Maps.JungleJapes,Regions.JapesBeyondCoconutGate1:Maps.JungleJapes,Regions.JapesBeyondCoconutGate2:Maps.JungleJapes,Regions.JapesBeyondPeanutGate:Maps.JungleJapes,Regions.JapesBeyondFeatherGate:Maps.JungleJapes,Regions.TinyHive:Maps.JapesTinyHive,Regions.BeyondRambiGate:Maps.JungleJapes,Regions.JapesLankyCave:Maps.JapesLankyCave,Regions.Mine:Maps.JapesMountain,Regions.JapesMinecarts:Maps.JapesMinecarts,Regions.JapesCatacomb:Maps.JapesUnderGround,Regions.JapesBaboonBlast:Maps.JapesBaboonBlast,Regions.AngryAztecStart:Maps.AngryAztec,Regions.BetweenVinesByPortal:Maps.AngryAztec,Regions.AngryAztecOasis:Maps.AngryAztec,Regions.TempleStart:Maps.AztecTinyTemple,Regions.TempleUnderwater:Maps.AztecTinyTemple,Regions.AngryAztecMain:Maps.AngryAztec,Regions.DonkeyTemple:Maps.AztecDonkey5DTemple,Regions.DiddyTemple:Maps.AztecDiddy5DTemple,Regions.LankyTemple:Maps.AztecLanky5DTemple,Regions.TinyTemple:Maps.AztecTiny5DTemple,Regions.ChunkyTemple:Maps.AztecChunky5DTemple,Regions.AztecTinyRace:Maps.AztecTinyRace,Regions.LlamaTemple:Maps.AztecLlamaTemple,Regions.LlamaTempleBack:Maps.AztecLlamaTemple,Regions.AztecBaboonBlast:Maps.AztecBaboonBlast,Regions.FranticFactoryStart:Maps.FranticFactory,Regions.Testing:Maps.FranticFactory,Regions.RandD:Maps.FranticFactory,Regions.FactoryTinyRaceLobby:Maps.FranticFactory,Regions.FactoryTinyRace:Maps.FactoryTinyRace,Regions.ChunkyRoomPlatform:Maps.FranticFactory,Regions.PowerHut:Maps.FactoryPowerHut,Regions.BeyondHatch:Maps.FranticFactory,Regions.InsideCore:Maps.FactoryCrusher,Regions.MiddleCore:Maps.FranticFactory,Regions.UpperCore:Maps.FranticFactory,Regions.FactoryBaboonBlast:Maps.FactoryBaboonBlast,Regions.GloomyGalleonStart:Maps.GloomyGalleon,Regions.GalleonPastVines:Maps.GloomyGalleon,Regions.GalleonBeyondPineappleGate:Maps.GloomyGalleon,Regions.LighthouseSurface:Maps.GloomyGalleon,Regions.LighthousePlatform:Maps.GloomyGalleon,Regions.LighthouseUnderwater:Maps.GloomyGalleon,Regions.LighthouseSnideAlcove:Maps.GloomyGalleon,Regions.Lighthouse:Maps.GalleonLighthouse,Regions.MermaidRoom:Maps.GalleonMermaidRoom,Regions.SickBay:Maps.GalleonSickBay,Regions.Shipyard:Maps.GloomyGalleon,Regions.SealRace:Maps.GalleonSealRace,Regions.TreasureRoom:Maps.GloomyGalleon,Regions.TinyChest:Maps.GalleonTreasureChest,Regions.Submarine:Maps.GalleonSubmarine,Regions.Mechafish:Maps.GalleonMechafish,Regions.LankyShip:Maps.Galleon2DShip,Regions.TinyShip:Maps.Galleon2DShip,Regions.BongosShip:Maps.Galleon5DShipDKTiny,Regions.SaxophoneShip:Maps.Galleon5DShipDKTiny,Regions.GuitarShip:Maps.Galleon5DShipDiddyLankyChunky,Regions.TromboneShip:Maps.Galleon5DShipDiddyLankyChunky,Regions.TriangleShip:Maps.Galleon5DShipDiddyLankyChunky,Regions.GalleonBaboonBlast:Maps.GalleonBaboonBlast,Regions.FungiForestStart:Maps.FungiForest,Regions.ForestMinecarts:Maps.ForestMinecarts,Regions.GiantMushroomArea:Maps.FungiForest,Regions.MushroomLower:Maps.ForestGiantMushroom,Regions.MushroomLowerExterior:Maps.FungiForest,Regions.MushroomUpper:Maps.ForestGiantMushroom,Regions.MushroomNightDoor:Maps.ForestGiantMushroom,Regions.MushroomNightExterior:Maps.FungiForest,Regions.MushroomUpperExterior:Maps.FungiForest,Regions.MushroomChunkyRoom:Maps.ForestChunkyFaceRoom,Regions.MushroomLankyMushroomsRoom:Maps.ForestLankyMushroomsRoom,Regions.MushroomLankyZingersRoom:Maps.ForestLankyZingersRoom,Regions.HollowTreeArea:Maps.FungiForest,Regions.Anthill:Maps.ForestAnthill,Regions.MillArea:Maps.FungiForest,Regions.MillChunkyArea:Maps.ForestMillBack,Regions.MillTinyArea:Maps.ForestMillBack,Regions.SpiderRoom:Maps.ForestSpider,Regions.GrinderRoom:Maps.ForestMillFront,Regions.MillRafters:Maps.ForestRafters,Regions.WinchRoom:Maps.ForestWinchRoom,Regions.MillAttic:Maps.ForestMillAttic,Regions.ThornvineArea:Maps.FungiForest,Regions.ThornvineBarn:Maps.ForestThornvineBarn,Regions.WormArea:Maps.FungiForest,Regions.ForestBaboonBlast:Maps.ForestBaboonBlast,Regions.CrystalCavesMain:Maps.CrystalCaves,Regions.BoulderCave:Maps.CrystalCaves,Regions.CavesLankyRace:Maps.CavesLankyRace,Regions.FrozenCastle:Maps.CavesFrozenCastle,Regions.IglooArea:Maps.CrystalCaves,Regions.GiantKosha:Maps.CrystalCaves,Regions.DonkeyIgloo:Maps.CavesDonkeyIgloo,Regions.DiddyIgloo:Maps.CavesDiddyIgloo,Regions.LankyIgloo:Maps.CavesLankyIgloo,Regions.TinyIgloo:Maps.CavesTinyIgloo,Regions.ChunkyIgloo:Maps.CavesChunkyIgloo,Regions.CabinArea:Maps.CrystalCaves,Regions.RotatingCabin:Maps.CavesRotatingCabin,Regions.DonkeyCabin:Maps.CavesDonkeyCabin,Regions.DiddyLowerCabin:Maps.CavesDiddyLowerCabin,Regions.DiddyUpperCabin:Maps.CavesDiddyUpperCabin,Regions.LankyCabin:Maps.CavesLankyCabin,Regions.TinyCabin:Maps.CavesTinyCabin,Regions.ChunkyCabin:Maps.CavesChunkyCabin,Regions.CavesBaboonBlast:Maps.CavesBaboonBlast,Regions.CreepyCastleMain:Maps.CreepyCastle,Regions.CastleWaterfall:Maps.CreepyCastle,Regions.CastleTree:Maps.CastleTree,Regions.Library:Maps.CastleLibrary,Regions.Ballroom:Maps.CastleBallroom,Regions.MuseumBehindGlass:Maps.CastleMuseum,Regions.CastleTinyRace:Maps.CastleTinyRace,Regions.Tower:Maps.CastleTower,Regions.Greenhouse:Maps.CastleGreenhouse,Regions.TrashCan:Maps.CastleTrashCan,Regions.Shed:Maps.CastleShed,Regions.Museum:Maps.CastleMuseum,Regions.LowerCave:Maps.CastleLowerCave,Regions.Crypt:Maps.CastleCrypt,Regions.CastleMinecarts:Maps.CastleMinecarts,Regions.Mausoleum:Maps.CastleMausoleum,Regions.UpperCave:Maps.CastleUpperCave,Regions.Dungeon:Maps.CastleDungeon,Regions.CastleBaboonBlast:Maps.CastleBaboonBlast}
LevelMapTable={Levels.JungleJapes:[Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.JapesMountain,Maps.JapesMinecarts,Maps.JapesUnderGround,Maps.JapesBaboonBlast],Levels.AngryAztec:[Maps.AngryAztec,Maps.AztecTinyTemple,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecTinyRace,Maps.AztecLlamaTemple,Maps.AztecBaboonBlast],Levels.FranticFactory:[Maps.FranticFactory,Maps.FactoryTinyRace,Maps.FactoryPowerHut,Maps.FactoryCrusher,Maps.FactoryBaboonBlast],Levels.GloomyGalleon:[Maps.GloomyGalleon,Maps.GalleonLighthouse,Maps.GalleonMermaidRoom,Maps.GalleonSickBay,Maps.GalleonSealRace,Maps.GalleonTreasureChest,Maps.GalleonSubmarine,Maps.GalleonMechafish,Maps.Galleon5DShipDKTiny,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon2DShip,Maps.GalleonBaboonBlast],Levels.FungiForest:[Maps.FungiForest,Maps.ForestMinecarts,Maps.ForestGiantMushroom,Maps.ForestChunkyFaceRoom,Maps.ForestLankyZingersRoom,Maps.ForestLankyMushroomsRoom,Maps.ForestAnthill,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestSpider,Maps.ForestRafters,Maps.ForestWinchRoom,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestBaboonBlast],Levels.CrystalCaves:[Maps.CrystalCaves,Maps.CavesLankyRace,Maps.CavesFrozenCastle,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesChunkyIgloo,Maps.CavesRotatingCabin,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CavesBaboonBlast],Levels.CreepyCastle:[Maps.CreepyCastle,Maps.CastleTree,Maps.CastleLibrary,Maps.CastleBallroom,Maps.CastleMuseum,Maps.CastleTinyRace,Maps.CastleTower,Maps.CastleGreenhouse,Maps.CastleTrashCan,Maps.CastleShed,Maps.CastleLowerCave,Maps.CastleCrypt,Maps.CastleMinecarts,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleDungeon,Maps.CastleBaboonBlast],Levels.DKIsles:[Maps.Isles,Maps.BananaFairyRoom,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.IslesSnideRoom,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.TrainingGrounds,Maps.Treehouse,Maps.KLumsy],Levels.HideoutHelm:[Maps.HideoutHelm]}
def getLevelFromMap(map_enum):
	'Get level from map index referencing lookup table.'
	for A in LevelMapTable:
		if map_enum in LevelMapTable[A]:return A
	return None
MapExitTable={Maps.TrainingGrounds:[_A,'From Treehouse'],Maps.Treehouse:['Test Cutscene',_H],Maps.Isles:[_H,'From K-Lumsy',_I,_J,_K,_L,_M,'From Helm Lobby','From Banana Fairy Isle',"From Snide's Room",_N,_O,'From K Rool',_H],Maps.JungleJapes:[_I,'From Beehive','From Mountain','From Cranky','From Funky','From Painting Room',_B,_C,'From Underground','From T&S (Diddy Cave)','From T&S (Near Cannon)','From ? (Other hill near SSSortie)','From T&S (Near Pool Fairy)','From ? (Near Pool Fairy)',_P,_I,'From DK Rap (DKTV Demo)','From Japes Lobby (Intro)'],Maps.AngryAztec:[_J,'From Tiny Temple','From Llama Temple','From Tiny 5DTemple','From Chunky 5DTemple','From DK 5DTemple','From Diddy 5DTemple','From Lanky 5DTemple',_G,_B,_D,_C,"From T&S (Candy's)",'From T&S (W5)','From T&S (5DTemple)',"From T&S (Cranky's)","From T&S (Funky's)",_S,_E,_J],Maps.FranticFactory:[_K,'From Arcade Area (near Tiny BP)','From Tiny BP Area (To Arcade Area)','From Power Shed','From R&D Area (To Storage Room)',_B,_E,_D,'From Crusher Room','From T&S (Block Tower)','From T&S (Arcade)','From T&S (R&D)','From T&S (Production Room)','From T&S (Storage Room)','From ? (Near Bad Hit Detection Man)',_C,_T,_G,_K],Maps.GloomyGalleon:[_L,'From Diddy 5DShip','From Chunky 5DShip','From Lanky 5DShip','From Treasure Chest','From Mermaid','From Tiny 5DShip','From Donkey 5DShip','From Tiny 2DShip','From Lanky 2DShip','From Lighthouse','From Seasick Ship','From T&S (Cactus)',"From T&S (Near Cranky's)",'From T&S (2DShip)','From T&S (Enguarde Door)',_C,_B,_G,'From Seal Race','From T&S (Meme Hole)','From Submarine',_D,_E,_L],Maps.Galleon5DShipDiddyLankyChunky:[_U,'From Galleon (Chunky Entrance)',_V,_U],Maps.Galleon5DShipDKTiny:[_W,_Q,_W],Maps.Galleon2DShip:[_Q,_V,_Q],Maps.FungiForest:[_M,'From Mill Attic','From Winch','From Rafters','From Thornvine Barn','From Mill (PPunch Door)',_X,'From Mill (Tiny Hole)','From G. Mush (Low)','From G. Mush (Low Middle)','From G. Mush (Middle)','From G. Mush (High Middle)','From G. Mush (High)','From Face Puzzle (Chunky)','From Mushrooms Room (Lanky)','From Zingers Room (Lanky)',_P,_D,_E,_B,'From T&S (DK Barn)',_Y,'From T&S (Beanstalk)','From Anthill','From T&S (G. Mush)','From T&S (Tree)',_C,'From Fungi Lobby (?)',_M],Maps.ForestMillFront:[_Z,'From Mill (Rear)',_Z],Maps.ForestMillBack:[_a,'From Spider Boss',_X,'From Fungi (Tiny Hole)',_a],Maps.ForestGiantMushroom:[_b,'From Fungi (Middle)','From Fungi (Low Middle)','From Fungi (High Middle)','From Fungi (High)',_b],Maps.CrystalCaves:[_N,'From Diddy 5DIgloo','From DK 5DIgloo','From Lanky 5DIgloo','From Chunky 5DIgloo','From Tiny 5DIgloo',_S,'From ? (Near Rotating Room)','From ? (Near 1DC)','From ? (Near 5DC)','From ? (Near W3 Room)','From ? (5DIgloo W3, Beta T&S)',_D,_E,'From DK 5DCabin','From Chunky 5DCabin','From Tiny 5DCabin','From Diddy Lower 5DCabin','From Diddy Upper 5DCabin','From Rotating Cabin','From Lanky Cabin',_G,_B,_Y,'From T&S (Rotating Room)','From T&S (1DC)','From T&S (Giant Boulder)','From ? (Behind W3 Room)',_C,'From ? (Giant Kosha Room)','From Tile Flipping','From DK Treehouse (Secret Exit)',_N],Maps.CreepyCastle:[_O,'From Tree (Drain)','From Tunnel (Front)','From T&S (W2)',_R,'From Tunnel (Rear)','From T&S (Rear)','From Museum','From Greenhouse (Start)','From Shed','From T&S (W4)','From Ballroom','From Library (Start)','From Library (End)','From Tower','From Tree (Entrance)','From Trash Can',_C,_D,_B,'From Greenhouse (End)','From Castle Lobby (Intro)',_O],Maps.CastleBallroom:[_F,'From Museum (Monkeyport)',_F],Maps.CastleCrypt:[_R,_P,_R],Maps.CastleMuseum:[_F,_T,'From Ballroom (Monkeyport)',_F],Maps.CastleLibrary:['From Castle Main (Start)','From Castle Main (End)'],Maps.CastleUpperCave:[_c,_G,'From Castle (Rear)',_d,'From Dungeon',_c],Maps.CastleLowerCave:[_F,_E,_d,'From Crypt (DK/Diddy/Chunky)','From Mausoleum (Lanky/Tiny)',_F],Maps.JungleJapesLobby:[_A,'From Japes',_A],Maps.AngryAztecLobby:[_A,'From Aztec',_A],Maps.GloomyGalleonLobby:[_A,'From Galleon',_A],Maps.FranticFactoryLobby:[_A,'From Factory',_A],Maps.FungiForestLobby:[_A,'From Fungi',_A],Maps.CreepyCastleLobby:[_A,'From Castle',_A],Maps.CrystalCavesLobby:[_A,'From Caves',_A]}
def GetMapId(regionId):'Get the map id of a transition.';return RegionMapList[regionId]
def GetExitId(back):
	'Get exit id of a transition.';A=GetMapId(back.regionId)
	if A in MapExitTable:return MapExitTable[A].index(back.name)
	else:return 0