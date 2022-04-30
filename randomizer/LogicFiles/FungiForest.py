'Logic file for Fungi Forest.'
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
LogicRegions={Regions.FungiForestStart:Region('Fungi Forest Start',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestDonkeyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.donkey]>=75),LocationLogic(Locations.ForestDiddyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.diddy]>=75),LocationLogic(Locations.ForestLankyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.lanky]>=75),LocationLogic(Locations.ForestTinyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.tiny]>=75),LocationLogic(Locations.ForestChunkyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.chunky]>=75)],[Event(Events.ForestEntered,lambda l:_A),Event(Events.Night,lambda l:l.HasGun(Kongs.any)),Event(Events.WormGatesOpened,lambda l:(l.feather and l.tiny)and(l.pineapple and l.chunky))],[TransitionFront(Regions.FungiForestLobby,lambda l:_A,Transitions.ForestToIsles),TransitionFront(Regions.ForestMinecarts,lambda l:l.Slam and l.ischunky),TransitionFront(Regions.GiantMushroomArea,lambda l:_A),TransitionFront(Regions.MillArea,lambda l:_A),TransitionFront(Regions.WormArea,lambda l:Events.WormGatesOpened in l.Events)]),Regions.ForestMinecarts:Region('Forest Minecarts',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestChunkyMinecarts,lambda l:l.ischunky)],[],[TransitionFront(Regions.FungiForestStart,lambda l:_A)],Transitions.ForestMainToCarts),Regions.GiantMushroomArea:Region('Giant Mushroom Area',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestDiddyTopofMushroom,lambda l:l.jetpack and l.isdiddy,_A)],[Event(Events.HollowTreeGateOpened,lambda l:l.grape and l.lanky)],[TransitionFront(Regions.FungiForestStart,lambda l:_A),TransitionFront(Regions.MushroomLower,lambda l:_A,Transitions.ForestMainToLowerMushroom),TransitionFront(Regions.MushroomLowerExterior,lambda l:l.jetpack),TransitionFront(Regions.MushroomUpperExterior,lambda l:l.jetpack),TransitionFront(Regions.HollowTreeArea,lambda l:Events.HollowTreeGateOpened in l.Events),TransitionFront(Regions.CrankyForest,lambda l:_A)]),Regions.MushroomLower:Region('Mushroom Lower',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestTinyMushroomBarrel,lambda l:l.superSlam and l.istiny,_A)],[Event(Events.MushroomCannonsSpawned,lambda l:l.coconut and l.peanut and l.grape and l.feather and l.pineapple and l.donkey and l.diddy and l.lanky and l.tiny and l.chunky),Event(Events.DonkeyMushroomSwitch,lambda l:l.superSlam and l.donkey)],[TransitionFront(Regions.GiantMushroomArea,lambda l:_A,Transitions.ForestLowerMushroomToMain),TransitionFront(Regions.MushroomLowerExterior,lambda l:_A,Transitions.ForestLowerMushroomToLowerExterior),TransitionFront(Regions.MushroomUpper,lambda l:Events.MushroomCannonsSpawned in l.Events)]),Regions.MushroomLowerExterior:Region('Mushroom Lower Exterior',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestKasplatLowerMushroomExterior,lambda l:_A)],[],[TransitionFront(Regions.GiantMushroomArea,lambda l:_A),TransitionFront(Regions.MushroomLower,lambda l:_A,Transitions.ForestLowerExteriorToLowerMushroom),TransitionFront(Regions.MushroomUpper,lambda l:_A,Transitions.ForestLowerExteriorToUpperMushroom),TransitionFront(Regions.ForestBaboonBlast,lambda l:l.blast and l.isdonkey)]),Regions.ForestBaboonBlast:Region('Forest Baboon Blast',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestDonkeyBaboonBlast,lambda l:l.isdonkey,_A)],[],[TransitionFront(Regions.MushroomLowerExterior,lambda l:_A)]),Regions.MushroomUpper:Region('Mushroom Upper',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestDonkeyMushroomCannons,lambda l:Events.MushroomCannonsSpawned in l.Events and Events.DonkeyMushroomSwitch in l.Events),LocationLogic(Locations.ForestKasplatInsideMushroom,lambda l:_A)],[],[TransitionFront(Regions.MushroomLower,lambda l:_A),TransitionFront(Regions.MushroomLowerExterior,lambda l:_A,Transitions.ForestUpperMushroomToLowerExterior),TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestUpperMushroomToUpperExterior),TransitionFront(Regions.MushroomNightDoor,lambda l:_A)]),Regions.MushroomNightDoor:Region('Mushroom Night Door',Levels.FungiForest,_B,_C,[],[],[TransitionFront(Regions.MushroomUpper,lambda l:_A),TransitionFront(Regions.MushroomNightExterior,lambda l:Events.Night in l.Events,Transitions.ForestNightToExterior)]),Regions.MushroomNightExterior:Region('Mushroom Night Exterior',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestKasplatUpperMushroomExterior,lambda l:_A)],[],[TransitionFront(Regions.MushroomNightDoor,lambda l:Events.Night in l.Events,Transitions.ForestExteriorToNight),TransitionFront(Regions.GiantMushroomArea,lambda l:_A)]),Regions.MushroomUpperExterior:Region('Mushroom Upper Exterior',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestBattleArena,lambda l:_A)],[],[TransitionFront(Regions.MushroomUpper,lambda l:_A,Transitions.ForestUpperExteriorToUpperMushroom),TransitionFront(Regions.MushroomNightExterior,lambda l:_A),TransitionFront(Regions.GiantMushroomArea,lambda l:_A),TransitionFront(Regions.MushroomChunkyRoom,lambda l:l.superSlam and l.ischunky,Transitions.ForestExteriorToChunky),TransitionFront(Regions.MushroomLankyZingersRoom,lambda l:l.handstand and l.superSlam and l.islanky,Transitions.ForestExteriorToZingers),TransitionFront(Regions.MushroomLankyMushroomsRoom,lambda l:l.handstand and l.superSlam and l.islanky,Transitions.ForestExteriorToMushrooms),TransitionFront(Regions.ForestBossLobby,lambda l:_A)]),Regions.MushroomChunkyRoom:Region('Mushroom Chunky Room',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestChunkyFacePuzzle,lambda l:l.pineapple and l.ischunky)],[],[TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestChunkyToExterior)]),Regions.MushroomLankyZingersRoom:Region('Mushroom Lanky Zingers Room',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestLankyZingers,lambda l:l.islanky)],[],[TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestZingersToExterior)]),Regions.MushroomLankyMushroomsRoom:Region('Mushroom Lanky Mushrooms Room',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestLankyColoredMushrooms,lambda l:l.Slam and l.islanky,_A)],[],[TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestMushroomsToExterior)]),Regions.HollowTreeArea:Region('Hollow Tree Area',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestDiddyOwlRace,lambda l:Events.Night in l.Events and l.jetpack and l.guitar and l.isdiddy,_A),LocationLogic(Locations.ForestLankyRabbitRace,lambda l:l.trombone and l.sprint and l.lanky),LocationLogic(Locations.ForestKasplatOwlTree,lambda l:_A)],[],[TransitionFront(Regions.GiantMushroomArea,lambda l:Events.HollowTreeGateOpened in l.Events),TransitionFront(Regions.Anthill,lambda l:l.mini and l.saxophone,Transitions.ForestTreeToAnthill),TransitionFront(Regions.ForestBossLobby,lambda l:_A)]),Regions.Anthill:Region('Anthill',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestTinyAnthill,lambda l:l.istiny)],[Event(Events.Bean,lambda l:l.istiny)],[TransitionFront(Regions.HollowTreeArea,lambda l:_A,Transitions.ForestAnthillToTree)]),Regions.MillArea:Region('Mill Area',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestDonkeyMill,lambda l:Events.ConveyorActivated in l.Events and Events.Night in l.Events and l.donkey),LocationLogic(Locations.ForestDiddyCagedBanana,lambda l:Events.WinchRaised in l.Events and Events.Night in l.Events and l.diddy)],[],[TransitionFront(Regions.FungiForestStart,lambda l:_A),TransitionFront(Regions.MillChunkyArea,lambda l:l.punch and l.ischunky,Transitions.ForestMainToChunkyMill),TransitionFront(Regions.MillTinyArea,lambda l:Events.MillBoxBroken in l.Events and l.mini and l.istiny,Transitions.ForestMainToTinyMill),TransitionFront(Regions.GrinderRoom,lambda l:_A,Transitions.ForestMainToGrinder),TransitionFront(Regions.MillRafters,lambda l:Events.Night in l.Events and l.spring and l.isdiddy,Transitions.ForestMainToRafters),TransitionFront(Regions.WinchRoom,lambda l:Events.Night in l.Events and l.superSlam and l.isdiddy,Transitions.ForestMainToWinch),TransitionFront(Regions.MillAttic,lambda l:Events.Night in l.Events,Transitions.ForestMainToAttic),TransitionFront(Regions.ThornvineArea,lambda l:Events.Night in l.Events),TransitionFront(Regions.Snide,lambda l:_A),TransitionFront(Regions.ForestBossLobby,lambda l:_A)]),Regions.MillChunkyArea:Region('Mill Chunky Area',Levels.FungiForest,_B,-1,[],[Event(Events.GrinderActivated,lambda l:l.triangle and l.ischunky),Event(Events.MillBoxBroken,lambda l:l.punch and l.ischunky)],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestChunkyMillToMain),TransitionFront(Regions.MillTinyArea,lambda l:_A)]),Regions.MillTinyArea:Region('Mill Tiny Area',Levels.FungiForest,_B,-1,[],[],[TransitionFront(Regions.MillArea,lambda l:l.mini and l.istiny,Transitions.ForestTinyMillToMain),TransitionFront(Regions.MillChunkyArea,lambda l:_A),TransitionFront(Regions.SpiderRoom,lambda l:Events.Night in l.Events,Transitions.ForestTinyMillToSpider),TransitionFront(Regions.GrinderRoom,lambda l:l.mini and l.istiny,Transitions.ForestTinyMillToGrinder)]),Regions.SpiderRoom:Region('Spider Room',Levels.FungiForest,_B,Regions.MillTinyArea,[LocationLogic(Locations.ForestTinySpiderBoss,lambda l:l.feather and l.istiny)],[],[TransitionFront(Regions.MillTinyArea,lambda l:_A,Transitions.ForestSpiderToTinyMill)]),Regions.GrinderRoom:Region('Grinder Room',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestChunkyKegs,lambda l:Events.GrinderActivated in l.Events and Events.ConveyorActivated in l.Events and l.chunky)],[Event(Events.ConveyorActivated,lambda l:l.superSlam and l.grab and l.donkey)],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestGrinderToMain),TransitionFront(Regions.MillTinyArea,lambda l:l.mini and l.istiny,Transitions.ForestGrinderToTinyMill)]),Regions.MillRafters:Region('Mill Rafters',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestDiddyRafters,lambda l:l.isdiddy),LocationLogic(Locations.ForestBananaFairyRafters,lambda l:l.camera)],[],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestRaftersToMain)]),Regions.WinchRoom:Region('Winch Room',Levels.FungiForest,_B,-1,[],[Event(Events.WinchRaised,lambda l:l.peanut and l.charge and l.isdiddy)],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestWinchToMain)]),Regions.MillAttic:Region('Mill Attic',Levels.FungiForest,_B,TransitionFront(Regions.FungiForestStart,lambda l:l.superSlam and l.islanky),[LocationLogic(Locations.ForestLankyAttic,lambda l:l.superSlam and(l.homing or l.settings.hard_shooting)and l.grape and l.islanky)],[],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestAtticToMain)]),Regions.ThornvineArea:Region('Thornvine Area',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestKasplatNearBarn,lambda l:_A)],[],[TransitionFront(Regions.MillArea,lambda l:Events.Night in l.Events),TransitionFront(Regions.ThornvineBarn,lambda l:l.superSlam and l.isdonkey,Transitions.ForestMainToBarn),TransitionFront(Regions.ForestBossLobby,lambda l:_A)]),Regions.ThornvineBarn:Region('Thornvine Barn',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestDonkeyBarn,lambda l:l.Slam and l.isdonkey,_A),LocationLogic(Locations.ForestBananaFairyThornvines,lambda l:l.camera)],[],[TransitionFront(Regions.ThornvineArea,lambda l:_A,Transitions.ForestBarnToMain)]),Regions.WormArea:Region('Worm Area',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestTinyBeanstalk,lambda l:Events.Bean in l.Events and l.saxophone and l.mini and l.tiny),LocationLogic(Locations.ForestChunkyApple,lambda l:l.hunkyChunky and l.chunky)],[],[TransitionFront(Regions.FungiForestStart,lambda l:_A),TransitionFront(Regions.FunkyForest,lambda l:_A),TransitionFront(Regions.ForestBossLobby,lambda l:Events.Night in l.Events)]),Regions.ForestBossLobby:Region('Forest Boss Lobby',Levels.FungiForest,_A,_C,[],[],[TransitionFront(Regions.ForestBoss,lambda l:l.IsBossReachable(Levels.FungiForest))]),Regions.ForestBoss:Region('Forest Boss',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestKey,lambda l:l.IsBossBeatable(Levels.FungiForest))],[],[])}