'Logic file for Crystal Caves.'
_C=None
_B=False
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MinigameType import MinigameType
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.LogicClasses import Event,LocationLogic,Region,TransitionFront
LogicRegions={Regions.CrystalCavesMain:Region('Crystal Caves Main',Levels.CrystalCaves,_A,_C,[LocationLogic(Locations.CavesDonkeyMedal,lambda l:l.ColoredBananas[Levels.CrystalCaves][Kongs.donkey]>=75),LocationLogic(Locations.CavesDiddyMedal,lambda l:l.ColoredBananas[Levels.CrystalCaves][Kongs.diddy]>=75),LocationLogic(Locations.CavesLankyMedal,lambda l:l.ColoredBananas[Levels.CrystalCaves][Kongs.lanky]>=75),LocationLogic(Locations.CavesTinyMedal,lambda l:l.ColoredBananas[Levels.CrystalCaves][Kongs.tiny]>=75),LocationLogic(Locations.CavesChunkyMedal,lambda l:l.ColoredBananas[Levels.CrystalCaves][Kongs.chunky]>=75),LocationLogic(Locations.CavesDiddyJetpackBarrel,lambda l:l.jetpack and l.isdiddy,MinigameType.BonusBarrel),LocationLogic(Locations.CavesTinyMonkeyportIgloo,lambda l:l.monkeyport and l.mini and l.twirl and l.tiny),LocationLogic(Locations.CavesChunkyGorillaGone,lambda l:l.punch and l.gorillaGone and l.chunky),LocationLogic(Locations.CavesKasplatNearLab,lambda l:not l.settings.kasplat_location_rando),LocationLogic(Locations.CavesKasplatNearCandy,lambda l:not l.settings.kasplat_location_rando)],[Event(Events.CavesEntered,lambda l:_A),Event(Events.CavesSmallBoulderButton,lambda l:l.chunky)],[TransitionFront(Regions.CrystalCavesLobby,lambda l:_A,Transitions.CavesToIsles),TransitionFront(Regions.CavesBlueprintCave,lambda l:l.mini and l.twirl and l.tiny),TransitionFront(Regions.CavesBonusCave,lambda l:l.mini and l.tiny),TransitionFront(Regions.CavesBlueprintPillar,lambda l:l.jetpack and l.diddy),TransitionFront(Regions.CavesBananaportSpire,lambda l:l.jetpack and l.diddy),TransitionFront(Regions.BoulderCave,lambda l:l.punch),TransitionFront(Regions.CavesLankyRace,lambda l:l.superSlam and l.balloon and l.islanky,Transitions.CavesMainToRace),TransitionFront(Regions.FrozenCastle,lambda l:l.superSlam and l.islanky,Transitions.CavesMainToCastle),TransitionFront(Regions.IglooArea,lambda l:_A),TransitionFront(Regions.CabinArea,lambda l:_A),TransitionFront(Regions.FunkyCaves,lambda l:_A),TransitionFront(Regions.CrankyCaves,lambda l:_A),TransitionFront(Regions.Snide,lambda l:l.punch),TransitionFront(Regions.CavesBossLobby,lambda l:l.punch),TransitionFront(Regions.CavesBaboonBlast,lambda l:l.blast and l.isdonkey)]),Regions.CavesBlueprintCave:Region('Caves Blueprint Cave',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesKasplatNearFunky,lambda l:not l.settings.kasplat_location_rando)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:l.mini and l.istiny)]),Regions.CavesBonusCave:Region('Caves Bonus Cave',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesTinyCaveBarrel,lambda l:_A,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:l.mini and l.istiny)]),Regions.CavesBlueprintPillar:Region('Caves Blueprint Pillar',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesKasplatPillar,lambda l:not l.settings.kasplat_location_rando)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A)]),Regions.CavesBananaportSpire:Region('Caves Bananaport Spire',Levels.CrystalCaves,_B,_C,[],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A)]),Regions.CavesBaboonBlast:Region('Caves Baboon Blast',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesDonkeyBaboonBlast,lambda l:l.isdonkey,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A)]),Regions.BoulderCave:Region('Boulder Cave',Levels.CrystalCaves,_A,_C,[],[Event(Events.CavesLargeBoulderButton,lambda l:Events.CavesSmallBoulderButton in l.Events and l.hunkyChunky and l.chunky)],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A),TransitionFront(Regions.CavesBossLobby,lambda l:_A)]),Regions.CavesLankyRace:Region('Caves Lanky Race',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesLankyBeetleRace,lambda l:l.sprint and l.islanky)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A,Transitions.CavesRaceToMain)],Transitions.CavesMainToRace),Regions.FrozenCastle:Region('Frozen Castle',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesLankyCastle,lambda l:l.Slam and l.islanky)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A,Transitions.CavesCastleToMain)]),Regions.IglooArea:Region('Igloo Area',Levels.CrystalCaves,_A,_C,[LocationLogic(Locations.CavesChunkyTransparentIgloo,lambda l:Events.CavesLargeBoulderButton in l.Events and l.chunky),LocationLogic(Locations.CavesKasplatOn5DI,lambda l:not l.settings.kasplat_location_rando)],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A),TransitionFront(Regions.GiantKosha,lambda l:Events.CavesLargeBoulderButton in l.Events and l.monkeyport and l.istiny),TransitionFront(Regions.DonkeyIgloo,lambda l:(l.settings.high_req or l.jetpack)and l.bongos and l.isdonkey,Transitions.CavesIglooToDonkey),TransitionFront(Regions.DiddyIgloo,lambda l:(l.settings.high_req or l.jetpack)and l.guitar and l.isdiddy,Transitions.CavesIglooToDiddy),TransitionFront(Regions.LankyIgloo,lambda l:(l.settings.high_req or l.jetpack)and l.trombone and l.islanky,Transitions.CavesIglooToLanky),TransitionFront(Regions.TinyIgloo,lambda l:(l.settings.high_req or l.jetpack)and l.saxophone and l.istiny,Transitions.CavesIglooToTiny),TransitionFront(Regions.ChunkyIgloo,lambda l:(l.settings.high_req or l.jetpack)and l.triangle and l.ischunky,Transitions.CavesIglooToChunky)]),Regions.GiantKosha:Region('Giant Kosha',Levels.CrystalCaves,_B,-1,[],[Event(Events.GiantKoshaDefeated,lambda l:l.shockwave or l.saxophone)],[]),Regions.DonkeyIgloo:Region('Donkey Igloo',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesDonkey5DoorIgloo,lambda l:l.isdonkey)],[],[TransitionFront(Regions.IglooArea,lambda l:_A,Transitions.CavesDonkeyToIgloo)]),Regions.DiddyIgloo:Region('Diddy Igloo',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesDiddy5DoorIgloo,lambda l:l.isdiddy)],[],[TransitionFront(Regions.IglooArea,lambda l:_A,Transitions.CavesDiddyToIgloo)]),Regions.LankyIgloo:Region('Lanky Igloo',Levels.CrystalCaves,_B,-1,[LocationLogic(Locations.CavesLanky5DoorIgloo,lambda l:l.balloon and l.islanky)],[],[TransitionFront(Regions.IglooArea,lambda l:_A,Transitions.CavesLankyToIgloo)]),Regions.TinyIgloo:Region('Tiny Igloo',Levels.CrystalCaves,_B,-1,[LocationLogic(Locations.CavesTiny5DoorIgloo,lambda l:l.Slam and l.istiny),LocationLogic(Locations.CavesBananaFairyIgloo,lambda l:l.camera)],[],[TransitionFront(Regions.IglooArea,lambda l:_A,Transitions.CavesTinyToIgloo)]),Regions.ChunkyIgloo:Region('Chunky Igloo',Levels.CrystalCaves,_B,-1,[LocationLogic(Locations.CavesChunky5DoorIgloo,lambda l:l.ischunky)],[],[TransitionFront(Regions.IglooArea,lambda l:_A,Transitions.CavesChunkyToIgloo)]),Regions.CabinArea:Region('Cabin Area',Levels.CrystalCaves,_A,_C,[],[],[TransitionFront(Regions.CrystalCavesMain,lambda l:_A),TransitionFront(Regions.RotatingCabin,lambda l:l.bongos and l.isdonkey,Transitions.CavesCabinToRotating),TransitionFront(Regions.DonkeyCabin,lambda l:l.bongos and l.isdonkey,Transitions.CavesCabinToDonkey),TransitionFront(Regions.DiddyLowerCabin,lambda l:l.guitar and l.isdiddy,Transitions.CavesCabinToDiddyLower),TransitionFront(Regions.DiddyUpperCabin,lambda l:l.guitar and l.isdiddy,Transitions.CavesCabinToDiddyUpper),TransitionFront(Regions.LankyCabin,lambda l:l.trombone and l.balloon and l.islanky,Transitions.CavesCabinToLanky),TransitionFront(Regions.TinyCabin,lambda l:l.saxophone and l.istiny,Transitions.CavesCabinToTiny),TransitionFront(Regions.ChunkyCabin,lambda l:l.triangle and l.ischunky,Transitions.CavesCabinToChunky),TransitionFront(Regions.CandyCaves,lambda l:_A),TransitionFront(Regions.CavesBossLobby,lambda l:l.jetpack or l.balloon)]),Regions.RotatingCabin:Region('Rotating Cabin',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesDonkeyRotatingCabin,lambda l:l.Slam and l.isdonkey),LocationLogic(Locations.CavesBattleArena,lambda l:l.Slam)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesRotatingToCabin)]),Regions.DonkeyCabin:Region('Donkey Cabin',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesDonkey5DoorCabin,lambda l:(l.homing or l.settings.hard_shooting)and l.coconut and l.isdonkey)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesDonkeyToCabin)]),Regions.DiddyLowerCabin:Region('Diddy Lower Cabin',Levels.CrystalCaves,_B,-1,[LocationLogic(Locations.CavesDiddy5DoorCabinLower,lambda l:l.isdiddy)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesDiddyLowerToCabin)]),Regions.DiddyUpperCabin:Region('Diddy Upper Cabin',Levels.CrystalCaves,_B,-1,[LocationLogic(Locations.CavesDiddy5DoorCabinUpper,lambda l:(l.guitar or l.shockwave)and l.spring and l.jetpack and l.isdiddy),LocationLogic(Locations.CavesBananaFairyCabin,lambda l:l.camera and(l.guitar or l.shockwave)and l.spring and l.jetpack and l.isdiddy)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesDiddyUpperToCabin)]),Regions.LankyCabin:Region('Lanky Cabin',Levels.CrystalCaves,_B,-1,[LocationLogic(Locations.CavesLanky1DoorCabin,lambda l:l.sprint and l.balloon and l.islanky)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesLankyToCabin)]),Regions.TinyCabin:Region('Tiny Cabin',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesTiny5DoorCabin,lambda l:l.istiny)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesTinyToCabin)]),Regions.ChunkyCabin:Region('Chunky Cabin',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesChunky5DoorCabin,lambda l:l.gorillaGone and l.Slam and l.ischunky,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.CabinArea,lambda l:_A,Transitions.CavesChunkyToCabin)]),Regions.CavesBossLobby:Region('Caves Boss Lobby',Levels.CrystalCaves,_A,_C,[],[],[TransitionFront(Regions.CavesBoss,lambda l:l.IsBossReachable(Levels.CrystalCaves))]),Regions.CavesBoss:Region('Caves Boss',Levels.CrystalCaves,_B,_C,[LocationLogic(Locations.CavesKey,lambda l:l.IsBossBeatable(Levels.CrystalCaves))],[],[])}