'Logic file for Fungi Forest.'
_C=None
_B=False
_A=True
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MinigameType import MinigameType
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Time import Time
from randomizer.Enums.Transitions import Transitions
from randomizer.LogicClasses import Event,LocationLogic,Region,TransitionFront
LogicRegions={Regions.FungiForestStart:Region('Fungi Forest Start',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestDonkeyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.donkey]>=l.settings.medal_cb_req),LocationLogic(Locations.ForestDiddyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.diddy]>=l.settings.medal_cb_req),LocationLogic(Locations.ForestLankyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.lanky]>=l.settings.medal_cb_req),LocationLogic(Locations.ForestTinyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.tiny]>=l.settings.medal_cb_req),LocationLogic(Locations.ForestChunkyMedal,lambda l:l.ColoredBananas[Levels.FungiForest][Kongs.chunky]>=l.settings.medal_cb_req)],[Event(Events.ForestEntered,lambda l:_A),Event(Events.Night,lambda l:l.HasGun(Kongs.any)),Event(Events.WormGatesOpened,lambda l:(l.feather and l.tiny)and(l.pineapple and l.chunky))],[TransitionFront(Regions.FungiForestLobby,lambda l:_A,Transitions.ForestToIsles),TransitionFront(Regions.ForestMinecarts,lambda l:l.Slam and l.ischunky),TransitionFront(Regions.GiantMushroomArea,lambda l:_A),TransitionFront(Regions.MillArea,lambda l:_A),TransitionFront(Regions.WormArea,lambda l:l.settings.open_levels or Events.WormGatesOpened in l.Events)]),Regions.ForestMinecarts:Region('Forest Minecarts',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestChunkyMinecarts,lambda l:l.ischunky or l.settings.free_trade_items)],[],[TransitionFront(Regions.FungiForestStart,lambda l:_A)],Transitions.ForestMainToCarts),Regions.GiantMushroomArea:Region('Giant Mushroom Area',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestDiddyTopofMushroom,lambda l:l.jetpack and l.isdiddy,MinigameType.BonusBarrel)],[Event(Events.HollowTreeGateOpened,lambda l:l.grape and l.lanky)],[TransitionFront(Regions.FungiForestStart,lambda l:_A),TransitionFront(Regions.MushroomLower,lambda l:_A,Transitions.ForestMainToLowerMushroom),TransitionFront(Regions.MushroomLowerExterior,lambda l:l.jetpack and l.isdiddy),TransitionFront(Regions.MushroomUpperExterior,lambda l:l.jetpack and l.isdiddy),TransitionFront(Regions.HollowTreeArea,lambda l:l.settings.open_levels or Events.HollowTreeGateOpened in l.Events),TransitionFront(Regions.CrankyForest,lambda l:_A)]),Regions.MushroomLower:Region('Mushroom Lower',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestTinyMushroomBarrel,lambda l:l.superSlam and l.istiny,MinigameType.BonusBarrel)],[Event(Events.MushroomCannonsSpawned,lambda l:l.coconut and l.peanut and l.grape and l.feather and l.pineapple and l.donkey and l.diddy and l.lanky and l.tiny and l.chunky),Event(Events.DonkeyMushroomSwitch,lambda l:l.superSlam and l.donkey)],[TransitionFront(Regions.GiantMushroomArea,lambda l:_A,Transitions.ForestLowerMushroomToMain),TransitionFront(Regions.MushroomLowerExterior,lambda l:_A,Transitions.ForestLowerMushroomToLowerExterior),TransitionFront(Regions.MushroomUpper,lambda l:Events.MushroomCannonsSpawned in l.Events)]),Regions.MushroomLowerExterior:Region('Mushroom Lower Exterior',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestKasplatLowerMushroomExterior,lambda l:not l.settings.kasplat_rando)],[],[TransitionFront(Regions.GiantMushroomArea,lambda l:_A),TransitionFront(Regions.MushroomLower,lambda l:_A,Transitions.ForestLowerExteriorToLowerMushroom),TransitionFront(Regions.MushroomUpper,lambda l:_A,Transitions.ForestLowerExteriorToUpperMushroom),TransitionFront(Regions.ForestBaboonBlast,lambda l:l.blast and l.isdonkey)]),Regions.ForestBaboonBlast:Region('Forest Baboon Blast',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestDonkeyBaboonBlast,lambda l:l.isdonkey,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.MushroomLowerExterior,lambda l:_A)]),Regions.MushroomUpper:Region('Mushroom Upper',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestDonkeyMushroomCannons,lambda l:Events.MushroomCannonsSpawned in l.Events and Events.DonkeyMushroomSwitch in l.Events),LocationLogic(Locations.ForestKasplatInsideMushroom,lambda l:not l.settings.kasplat_rando)],[],[TransitionFront(Regions.MushroomLower,lambda l:_A),TransitionFront(Regions.MushroomLowerExterior,lambda l:_A,Transitions.ForestUpperMushroomToLowerExterior),TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestUpperMushroomToUpperExterior),TransitionFront(Regions.MushroomNightDoor,lambda l:l.vines)]),Regions.MushroomNightDoor:Region('Mushroom Night Door',Levels.FungiForest,_B,_C,[],[],[TransitionFront(Regions.MushroomUpper,lambda l:_A),TransitionFront(Regions.MushroomNightExterior,lambda l:_A,Transitions.ForestNightToExterior,time=Time.Night)]),Regions.MushroomNightExterior:Region('Mushroom Night Exterior',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestKasplatUpperMushroomExterior,lambda l:not l.settings.kasplat_rando)],[],[TransitionFront(Regions.MushroomNightDoor,lambda l:_A,Transitions.ForestExteriorToNight,time=Time.Night),TransitionFront(Regions.GiantMushroomArea,lambda l:_A)]),Regions.MushroomUpperExterior:Region('Mushroom Upper Exterior',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestBattleArena,lambda l:not l.settings.crown_placement_rando)],[],[TransitionFront(Regions.MushroomUpper,lambda l:_A,Transitions.ForestUpperExteriorToUpperMushroom),TransitionFront(Regions.MushroomNightExterior,lambda l:_A),TransitionFront(Regions.GiantMushroomArea,lambda l:_A),TransitionFront(Regions.MushroomChunkyRoom,lambda l:l.superSlam and l.ischunky,Transitions.ForestExteriorToChunky),TransitionFront(Regions.MushroomLankyZingersRoom,lambda l:l.handstand and l.superSlam and l.islanky,Transitions.ForestExteriorToZingers),TransitionFront(Regions.MushroomLankyMushroomsRoom,lambda l:l.handstand and l.superSlam and l.islanky,Transitions.ForestExteriorToMushrooms),TransitionFront(Regions.ForestBossLobby,lambda l:not l.settings.tns_location_rando)]),Regions.MushroomChunkyRoom:Region('Mushroom Chunky Room',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestChunkyFacePuzzle,lambda l:l.pineapple and l.superSlam and l.ischunky)],[],[TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestChunkyToExterior)]),Regions.MushroomLankyZingersRoom:Region('Mushroom Lanky Zingers Room',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestLankyZingers,lambda l:l.islanky or l.settings.free_trade_items)],[],[TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestZingersToExterior)]),Regions.MushroomLankyMushroomsRoom:Region('Mushroom Lanky Mushrooms Room',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestLankyColoredMushrooms,lambda l:l.Slam and(l.islanky or l.settings.free_trade_items),MinigameType.BonusBarrel)],[],[TransitionFront(Regions.MushroomUpperExterior,lambda l:_A,Transitions.ForestMushroomsToExterior)]),Regions.HollowTreeArea:Region('Hollow Tree Area',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestDiddyOwlRace,lambda l:l.TimeAccess(Regions.HollowTreeArea,Time.Night)and l.jetpack and l.guitar and l.isdiddy,MinigameType.BonusBarrel),LocationLogic(Locations.ForestLankyRabbitRace,lambda l:l.TimeAccess(Regions.HollowTreeArea,Time.Day)and l.trombone and l.sprint and l.lanky),LocationLogic(Locations.ForestKasplatOwlTree,lambda l:not l.settings.kasplat_rando)],[],[TransitionFront(Regions.GiantMushroomArea,lambda l:l.settings.open_levels or Events.HollowTreeGateOpened in l.Events),TransitionFront(Regions.Anthill,lambda l:l.mini and l.saxophone,Transitions.ForestTreeToAnthill),TransitionFront(Regions.ForestBossLobby,lambda l:not l.settings.tns_location_rando)]),Regions.Anthill:Region('Anthill',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestTinyAnthill,lambda l:(l.istiny or l.settings.free_trade_items)and l.oranges)],[Event(Events.Bean,lambda l:(l.istiny or l.settings.free_trade_items)and l.oranges)],[TransitionFront(Regions.HollowTreeArea,lambda l:_A,Transitions.ForestAnthillToTree)]),Regions.MillArea:Region('Mill Area',Levels.FungiForest,_A,_C,[LocationLogic(Locations.ForestDonkeyMill,lambda l:l.TimeAccess(Regions.MillArea,Time.Night)and Events.ConveyorActivated in l.Events and l.donkey),LocationLogic(Locations.ForestDiddyCagedBanana,lambda l:l.TimeAccess(Regions.MillArea,Time.Night)and Events.WinchRaised in l.Events and l.diddy)],[],[TransitionFront(Regions.FungiForestStart,lambda l:_A),TransitionFront(Regions.MillChunkyArea,lambda l:l.punch and l.ischunky,Transitions.ForestMainToChunkyMill,time=Time.Day),TransitionFront(Regions.MillTinyArea,lambda l:Events.MillBoxBroken in l.Events and l.mini and l.istiny,Transitions.ForestMainToTinyMill),TransitionFront(Regions.GrinderRoom,lambda l:_A,Transitions.ForestMainToGrinder,time=Time.Day),TransitionFront(Regions.MillRafters,lambda l:l.spring and l.isdiddy,Transitions.ForestMainToRafters,time=Time.Night),TransitionFront(Regions.WinchRoom,lambda l:l.superSlam and l.isdiddy,Transitions.ForestMainToWinch,time=Time.Night),TransitionFront(Regions.MillAttic,lambda l:_A,Transitions.ForestMainToAttic,time=Time.Night),TransitionFront(Regions.ThornvineArea,lambda l:_A,time=Time.Night),TransitionFront(Regions.Snide,lambda l:_A,time=Time.Day),TransitionFront(Regions.ForestBossLobby,lambda l:not l.settings.tns_location_rando,time=Time.Day)]),Regions.MillChunkyArea:Region('Mill Chunky Area',Levels.FungiForest,_B,-1,[],[Event(Events.GrinderActivated,lambda l:l.triangle and l.ischunky),Event(Events.MillBoxBroken,lambda l:l.punch and l.ischunky)],[TransitionFront(Regions.MillArea,lambda l:l.ischunky,Transitions.ForestChunkyMillToMain,time=Time.Day),TransitionFront(Regions.MillTinyArea,lambda l:_A)]),Regions.MillTinyArea:Region('Mill Tiny Area',Levels.FungiForest,_B,-1,[],[],[TransitionFront(Regions.MillArea,lambda l:Events.MillBoxBroken in l.Events and l.mini and l.istiny,Transitions.ForestTinyMillToMain),TransitionFront(Regions.MillChunkyArea,lambda l:_A),TransitionFront(Regions.SpiderRoom,lambda l:_A,Transitions.ForestTinyMillToSpider,time=Time.Night),TransitionFront(Regions.GrinderRoom,lambda l:l.mini and l.istiny,Transitions.ForestTinyMillToGrinder)]),Regions.SpiderRoom:Region('Spider Room',Levels.FungiForest,_B,Regions.MillTinyArea,[LocationLogic(Locations.ForestTinySpiderBoss,lambda l:l.HasGun(Kongs.tiny)or l.settings.free_trade_items and l.HasGun(Kongs.any))],[],[TransitionFront(Regions.MillTinyArea,lambda l:_A,Transitions.ForestSpiderToTinyMill)]),Regions.GrinderRoom:Region('Grinder Room',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestChunkyKegs,lambda l:Events.GrinderActivated in l.Events and Events.ConveyorActivated in l.Events and l.chunky and l.barrels)],[Event(Events.ConveyorActivated,lambda l:l.superSlam and l.grab and l.donkey)],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestGrinderToMain,time=Time.Day),TransitionFront(Regions.MillTinyArea,lambda l:l.mini and l.istiny,Transitions.ForestGrinderToTinyMill)]),Regions.MillRafters:Region('Mill Rafters',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestDiddyRafters,lambda l:l.guitar and l.isdiddy),LocationLogic(Locations.ForestBananaFairyRafters,lambda l:l.guitar and l.isdiddy and l.camera)],[],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestRaftersToMain)]),Regions.WinchRoom:Region('Winch Room',Levels.FungiForest,_B,-1,[],[Event(Events.WinchRaised,lambda l:l.peanut and l.charge and l.isdiddy)],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestWinchToMain)]),Regions.MillAttic:Region('Mill Attic',Levels.FungiForest,_B,TransitionFront(Regions.FungiForestStart,lambda l:l.superSlam and l.islanky),[LocationLogic(Locations.ForestLankyAttic,lambda l:l.superSlam and(l.homing or l.settings.hard_shooting)and l.grape and l.islanky)],[],[TransitionFront(Regions.MillArea,lambda l:_A,Transitions.ForestAtticToMain)]),Regions.ThornvineArea:Region('Thornvine Area',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestKasplatNearBarn,lambda l:not l.settings.kasplat_rando)],[],[TransitionFront(Regions.MillArea,lambda l:_A,time=Time.Night),TransitionFront(Regions.ThornvineBarn,lambda l:l.superSlam and l.isdonkey and(l.strongKong or l.settings.damage_amount=='default'),Transitions.ForestMainToBarn),TransitionFront(Regions.ForestBossLobby,lambda l:not l.settings.tns_location_rando)]),Regions.ThornvineBarn:Region('Thornvine Barn',Levels.FungiForest,_B,-1,[LocationLogic(Locations.ForestDonkeyBarn,lambda l:l.Slam and l.isdonkey and l.vines,MinigameType.BonusBarrel),LocationLogic(Locations.ForestBananaFairyThornvines,lambda l:l.Slam and l.camera)],[],[TransitionFront(Regions.ThornvineArea,lambda l:_A,Transitions.ForestBarnToMain)]),Regions.WormArea:Region('Worm Area',Levels.FungiForest,_A,-1,[LocationLogic(Locations.ForestTinyBeanstalk,lambda l:Events.Bean in l.Events and l.saxophone and l.mini and l.istiny),LocationLogic(Locations.ForestChunkyApple,lambda l:Events.WormGatesOpened in l.Events and l.hunkyChunky and l.ischunky and l.barrels)],[],[TransitionFront(Regions.FungiForestStart,lambda l:Events.WormGatesOpened in l.Events),TransitionFront(Regions.FunkyForest,lambda l:_A),TransitionFront(Regions.ForestBossLobby,lambda l:not l.settings.tns_location_rando,time=Time.Night)]),Regions.ForestBossLobby:Region('Forest Boss Lobby',Levels.FungiForest,_A,_C,[],[],[TransitionFront(Regions.ForestBoss,lambda l:l.IsBossReachable(Levels.FungiForest))]),Regions.ForestBoss:Region('Forest Boss',Levels.FungiForest,_B,_C,[LocationLogic(Locations.ForestKey,lambda l:l.IsBossBeatable(Levels.FungiForest))],[],[])}