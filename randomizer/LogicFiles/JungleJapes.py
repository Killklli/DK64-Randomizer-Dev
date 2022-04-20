'Logic file for Jungle Japes.'
_C=None
_B=False
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.LogicClasses import Event,LocationLogic,Region,TransitionFront
LogicRegions={Regions.JungleJapesMain:Region('Jungle Japes Main',Levels.JungleJapes,_A,_C,[LocationLogic(Locations.JapesDonkeyMedal,lambda l:l.ColoredBananas[Levels.JungleJapes][Kongs.donkey]>=75),LocationLogic(Locations.JapesDiddyMedal,lambda l:l.ColoredBananas[Levels.JungleJapes][Kongs.diddy]>=75),LocationLogic(Locations.JapesLankyMedal,lambda l:l.ColoredBananas[Levels.JungleJapes][Kongs.lanky]>=75),LocationLogic(Locations.JapesTinyMedal,lambda l:l.ColoredBananas[Levels.JungleJapes][Kongs.tiny]>=75),LocationLogic(Locations.JapesChunkyMedal,lambda l:l.ColoredBananas[Levels.JungleJapes][Kongs.chunky]>=75),LocationLogic(Locations.DiddyKong,lambda l:l.HasGun(l.settings.diddy_freeing_kong)),LocationLogic(Locations.JapesDonkeyFrontofCage,lambda l:l.HasKong(l.settings.diddy_freeing_kong)),LocationLogic(Locations.JapesDonkeyFreeDiddy,lambda l:l.HasGun(l.settings.diddy_freeing_kong)),LocationLogic(Locations.JapesDonkeyCagedBanana,lambda l:Events.JapesDonkeySwitch in l.Events and l.donkey),LocationLogic(Locations.JapesDiddyCagedBanana,lambda l:Events.JapesDiddySwitch1 in l.Events and l.diddy),LocationLogic(Locations.JapesDiddyMountain,lambda l:Events.JapesDiddySwitch2 in l.Events and l.diddy),LocationLogic(Locations.JapesLankyCagedBanana,lambda l:Events.JapesLankySwitch in l.Events and l.lanky),LocationLogic(Locations.JapesTinyCagedBanana,lambda l:Events.JapesTinySwitch in l.Events and l.tiny),LocationLogic(Locations.JapesChunkyBoulder,lambda l:l.chunky),LocationLogic(Locations.JapesChunkyCagedBanana,lambda l:Events.JapesChunkySwitch and l.chunky),LocationLogic(Locations.JapesBattleArena,lambda l:_A)],[Event(Events.JapesEntered,lambda l:_A),Event(Events.JapesSpawnW5,lambda l:Events.JapesDiddySwitch2)],[TransitionFront(Regions.JungleJapesLobby,lambda l:_A,Transitions.JapesToIsles),TransitionFront(Regions.JapesBeyondPeanutGate,lambda l:l.peanut and l.diddy),TransitionFront(Regions.JapesBeyondCoconutGate1,lambda l:l.coconut and l.donkey),TransitionFront(Regions.JapesBeyondCoconutGate2,lambda l:l.coconut and l.donkey),TransitionFront(Regions.Mine,lambda l:l.peanut and l.isdiddy,Transitions.JapesMainToMine),TransitionFront(Regions.JapesLankyCave,lambda l:l.peanut and l.diddy and l.handstand and l.islanky,Transitions.JapesMainToLankyCave),TransitionFront(Regions.JapesCatacomb,lambda l:l.Slam and l.chunkyAccess,Transitions.JapesMainToCatacomb),TransitionFront(Regions.FunkyJapes,lambda l:_A),TransitionFront(Regions.Snide,lambda l:_A),TransitionFront(Regions.JapesBossLobby,lambda l:_A),TransitionFront(Regions.JapesBaboonBlast,lambda l:l.blast and l.isdonkey)]),Regions.JapesBaboonBlast:Region('Japes Baboon Blast',Levels.JungleJapes,_B,_C,[LocationLogic(Locations.JapesDonkeyBaboonBlast,lambda l:l.isdonkey)],[],[TransitionFront(Regions.JungleJapesMain,lambda l:_A)]),Regions.JapesBeyondPeanutGate:Region('Japes Beyond Peanut Gate',Levels.JungleJapes,_B,_C,[LocationLogic(Locations.JapesDiddyTunnel,lambda l:l.isdiddy),LocationLogic(Locations.JapesLankyGrapeGate,lambda l:l.grape and l.islanky,_A),LocationLogic(Locations.JapesTinyFeatherGateBarrel,lambda l:l.feather and l.istiny,_A)],[],[TransitionFront(Regions.JungleJapesMain,lambda l:_A),TransitionFront(Regions.JapesBossLobby,lambda l:_A)]),Regions.JapesBeyondCoconutGate1:Region('Japes Beyond Coconut Gate 1',Levels.JungleJapes,_B,_C,[LocationLogic(Locations.JapesKasplatLeftTunnelNear,lambda l:_A),LocationLogic(Locations.JapesKasplatLeftTunnelFar,lambda l:_A)],[],[TransitionFront(Regions.JungleJapesMain,lambda l:_A),TransitionFront(Regions.JapesBeyondFeatherGate,lambda l:l.feather and l.tinyAccess)]),Regions.JapesBeyondFeatherGate:Region('Japes Beyond Feather Gate',Levels.JungleJapes,_A,-1,[LocationLogic(Locations.JapesTinyStump,lambda l:l.mini and l.tiny),LocationLogic(Locations.JapesChunkyGiantBonusBarrel,lambda l:l.hunkyChunky and l.ischunky,_A)],[],[TransitionFront(Regions.JapesBeyondCoconutGate1,lambda l:_A),TransitionFront(Regions.TinyHive,lambda l:l.mini and l.istiny,Transitions.JapesMainToTinyHive)]),Regions.TinyHive:Region('Tiny Hive',Levels.JungleJapes,_B,-1,[LocationLogic(Locations.JapesTinyBeehive,lambda l:l.Slam and l.istiny)],[],[TransitionFront(Regions.JapesBeyondFeatherGate,lambda l:_A,Transitions.JapesTinyHiveToMain)]),Regions.JapesBeyondCoconutGate2:Region('Japes Beyond Coconut Gate 2',Levels.JungleJapes,_A,_C,[LocationLogic(Locations.JapesLankySlope,lambda l:l.handstand and l.islanky,_A),LocationLogic(Locations.JapesKasplatNearPaintingRoom,lambda l:_A),LocationLogic(Locations.JapesKasplatNearLab,lambda l:_A)],[Event(Events.Rambi,lambda l:l.coconut),Event(Events.JapesDonkeySwitch,lambda l:Events.Rambi in l.Events and l.Slam and l.donkey),Event(Events.JapesDiddySwitch1,lambda l:Events.Rambi in l.Events and l.Slam and l.diddy),Event(Events.JapesLankySwitch,lambda l:Events.Rambi in l.Events and l.Slam and l.lanky),Event(Events.JapesTinySwitch,lambda l:Events.Rambi in l.Events and l.Slam and l.tiny)],[TransitionFront(Regions.JungleJapesMain,lambda l:_A),TransitionFront(Regions.BeyondRambiGate,lambda l:Events.Rambi in l.Events),TransitionFront(Regions.CrankyJapes,lambda l:_A)]),Regions.BeyondRambiGate:Region('Beyond Rambi Gate',Levels.JungleJapes,_B,-1,[LocationLogic(Locations.JapesBananaFairyRambiCave,lambda l:l.camera)],[Event(Events.JapesChunkySwitch,lambda l:l.Slam and l.ischunky)],[TransitionFront(Regions.JapesBeyondCoconutGate2,lambda l:_A),TransitionFront(Regions.JapesBossLobby,lambda l:_A)]),Regions.JapesLankyCave:Region('Japes Lanky Cave',Levels.JungleJapes,_B,TransitionFront(Regions.JungleJapesMain,lambda l:l.Slam and l.islanky),[LocationLogic(Locations.JapesLankyFairyCave,lambda l:l.grape and l.Slam and l.islanky),LocationLogic(Locations.JapesBananaFairyLankyCave,lambda l:l.grape and l.camera and l.Slam and l.islanky)],[],[TransitionFront(Regions.JungleJapesMain,lambda l:_A,Transitions.JapesLankyCaveToMain)]),Regions.Mine:Region('Mine',Levels.JungleJapes,_B,-1,[],[Event(Events.JapesDiddySwitch2,lambda l:l.Slam and l.isdiddy)],[TransitionFront(Regions.JungleJapesMain,lambda l:_A,Transitions.JapesMineToMain),TransitionFront(Regions.JapesMinecarts,lambda l:l.charge and l.Slam and l.isdiddy)]),Regions.JapesMinecarts:Region('Japes Minecarts',Levels.JungleJapes,_B,_C,[LocationLogic(Locations.JapesDiddyMinecarts,lambda l:l.isdiddy)],[],[TransitionFront(Regions.JungleJapesMain,lambda l:_A)],Transitions.JapesMineToCarts),Regions.JapesCatacomb:Region('Japes Catacomb',Levels.JungleJapes,_B,_C,[LocationLogic(Locations.JapesChunkyUnderground,lambda l:l.pineapple and l.ischunky),LocationLogic(Locations.JapesKasplatUnderground,lambda l:l.pineapple)],[],[TransitionFront(Regions.JungleJapesMain,lambda l:_A,Transitions.JapesCatacombToMain)]),Regions.JapesBossLobby:Region('Japes Boss Lobby',Levels.JungleJapes,_A,_C,[],[],[TransitionFront(Regions.JapesBoss,lambda l:l.IsBossBeatable(Levels.JungleJapes)and sum(l.ColoredBananas[Levels.JungleJapes])>=l.settings.BossBananas[Levels.JungleJapes])]),Regions.JapesBoss:Region('Japes Boss',Levels.JungleJapes,_B,_C,[LocationLogic(Locations.JapesKey,lambda l:_A)],[],[])}