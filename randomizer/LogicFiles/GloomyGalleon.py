'Logic file for Gloomy Galleon.'
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
LogicRegions={Regions.GloomyGalleonStart:Region('Gloomy Galleon Start',Levels.GloomyGalleon,_A,_C,[LocationLogic(Locations.GalleonDonkeyMedal,lambda l:l.ColoredBananas[Levels.GloomyGalleon][Kongs.donkey]>=l.settings.medal_cb_req),LocationLogic(Locations.GalleonDiddyMedal,lambda l:l.ColoredBananas[Levels.GloomyGalleon][Kongs.diddy]>=l.settings.medal_cb_req),LocationLogic(Locations.GalleonLankyMedal,lambda l:l.ColoredBananas[Levels.GloomyGalleon][Kongs.lanky]>=l.settings.medal_cb_req),LocationLogic(Locations.GalleonTinyMedal,lambda l:l.ColoredBananas[Levels.GloomyGalleon][Kongs.tiny]>=l.settings.medal_cb_req),LocationLogic(Locations.GalleonChunkyMedal,lambda l:l.ColoredBananas[Levels.GloomyGalleon][Kongs.chunky]>=l.settings.medal_cb_req),LocationLogic(Locations.GalleonChunkyChest,lambda l:l.punch and l.chunky),LocationLogic(Locations.GalleonBattleArena,lambda l:not l.settings.crown_placement_rando and l.punch and l.chunky),LocationLogic(Locations.GalleonBananaFairybyCranky,lambda l:l.camera and l.punch and l.chunky)],[Event(Events.GalleonEntered,lambda l:_A),Event(Events.GalleonLankySwitch,lambda l:l.Slam and l.lanky),Event(Events.GalleonTinySwitch,lambda l:l.Slam and l.tiny),Event(Events.LighthouseGateOpened,lambda l:l.coconut and l.donkey),Event(Events.ShipyardGateOpened,lambda l:_A)],[TransitionFront(Regions.GloomyGalleonLobby,lambda l:_A,Transitions.GalleonToIsles),TransitionFront(Regions.GalleonPastVines,lambda l:l.vines),TransitionFront(Regions.GalleonBeyondPineappleGate,lambda l:l.pineapple and l.chunky),TransitionFront(Regions.LighthouseSurface,lambda l:l.settings.open_levels or Events.LighthouseGateOpened in l.Events),TransitionFront(Regions.Shipyard,lambda l:Events.ShipyardGateOpened in l.Events),TransitionFront(Regions.CrankyGalleon,lambda l:_A)]),Regions.GalleonPastVines:Region('Galleon Past Vines',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonKasplatNearLab,lambda l:not l.settings.kasplat_rando)],[],[TransitionFront(Regions.GloomyGalleonStart,lambda l:_A),TransitionFront(Regions.GalleonBossLobby,lambda l:not l.settings.tns_location_rando)]),Regions.GalleonBeyondPineappleGate:Region('Galleon Beyond Pineapple Gate',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonChunkyCannonGame,lambda l:Events.WaterSwitch in l.Events and l.ischunky and l.barrels),LocationLogic(Locations.GalleonKasplatCannons,lambda l:not l.settings.kasplat_rando and Events.WaterSwitch in l.Events)],[],[TransitionFront(Regions.GloomyGalleonStart,lambda l:_A)]),Regions.LighthouseSurface:Region('Lighthouse Surface',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonKasplatLighthouseArea,lambda l:not l.settings.kasplat_rando)],[Event(Events.GalleonChunkyPad,lambda l:l.triangle and l.chunky)],[TransitionFront(Regions.GloomyGalleonStart,lambda l:l.settings.open_levels or Events.LighthouseGateOpened in l.Events),TransitionFront(Regions.LighthouseUnderwater,lambda l:l.swim),TransitionFront(Regions.LighthousePlatform,lambda l:Events.WaterSwitch in l.Events),TransitionFront(Regions.LighthouseSnideAlcove,lambda l:Events.WaterSwitch in l.Events)]),Regions.LighthousePlatform:Region('Lighthouse Platform',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonDiddyShipSwitch,lambda l:Events.ActivatedLighthouse in l.Events and l.jetpack and l.Slam and l.isdiddy)],[Event(Events.MechafishSummoned,lambda l:l.jetpack and l.guitar and l.isdiddy)],[TransitionFront(Regions.LighthouseSurface,lambda l:_A),TransitionFront(Regions.Lighthouse,lambda l:l.Slam and l.isdonkey,Transitions.GalleonLighthouseAreaToLighthouse),TransitionFront(Regions.SickBay,lambda l:Events.ActivatedLighthouse in l.Events and l.Slam and l.ischunky,Transitions.GalleonLighthouseAreaToSickBay),TransitionFront(Regions.GalleonBaboonBlast,lambda l:l.blast and l.isdonkey)]),Regions.LighthouseUnderwater:Region('Lighthouse Underwater',Levels.GloomyGalleon,_A,_C,[LocationLogic(Locations.GalleonLankyEnguardeChest,lambda l:Events.LighthouseEnguarde in l.Events and l.lanky)],[Event(Events.WaterSwitch,lambda l:_A),Event(Events.LighthouseEnguarde,lambda l:l.lanky)],[TransitionFront(Regions.LighthouseSurface,lambda l:_A),TransitionFront(Regions.MermaidRoom,lambda l:l.mini and l.istiny,Transitions.GalleonLighthousAreaToMermaid),TransitionFront(Regions.GalleonBossLobby,lambda l:not l.settings.tns_location_rando)]),Regions.LighthouseSnideAlcove:Region('Lighthouse Snide Alcove',Levels.GloomyGalleon,_A,_C,[],[],[TransitionFront(Regions.LighthouseSurface,lambda l:_A),TransitionFront(Regions.Snide,lambda l:_A)]),Regions.GalleonBaboonBlast:Region('Galleon Baboon Blast',Levels.GloomyGalleon,_B,_C,[],[Event(Events.SealReleased,lambda l:l.isdonkey)],[TransitionFront(Regions.LighthousePlatform,lambda l:_A)]),Regions.Lighthouse:Region('Lighthouse',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonDonkeyLighthouse,lambda l:Events.ActivatedLighthouse in l.Events and(l.isdonkey or l.settings.free_trade_items))],[Event(Events.ActivatedLighthouse,lambda l:l.settings.high_req or l.Slam and l.grab and l.isdonkey)],[TransitionFront(Regions.LighthousePlatform,lambda l:_A,Transitions.GalleonLighthouseToLighthouseArea)]),Regions.MermaidRoom:Region('Mermaid Room',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonTinyPearls,lambda l:Events.PearlsCollected in l.Events and(l.istiny or l.settings.free_trade_items))],[],[TransitionFront(Regions.LighthouseUnderwater,lambda l:_A,Transitions.GalleonMermaidToLighthouseArea)]),Regions.SickBay:Region('Sick Bay',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonChunkySeasick,lambda l:l.punch and l.ischunky)],[],[TransitionFront(Regions.LighthousePlatform,lambda l:_A,Transitions.GalleonSickBayToLighthouseArea)]),Regions.Shipyard:Region('Shipyard',Levels.GloomyGalleon,_A,_C,[LocationLogic(Locations.GalleonDonkeyFreetheSeal,lambda l:Events.SealReleased in l.Events and(l.isdonkey or l.settings.free_trade_items)),LocationLogic(Locations.GalleonKasplatNearSub,lambda l:not l.settings.kasplat_rando)],[Event(Events.ShipyardTreasureRoomOpened,lambda l:Events.ShipyardEnguarde in l.Events and Events.WaterSwitch in l.Events)],[TransitionFront(Regions.GloomyGalleonStart,lambda l:l.settings.shuffle_loading_zones=='all'or Events.ShipyardGateOpened in l.Events),TransitionFront(Regions.ShipyardUnderwater,lambda l:l.swim),TransitionFront(Regions.SealRace,lambda l:Events.SealReleased in l.Events and Events.WaterSwitch in l.Events and l.isdonkey,Transitions.GalleonShipyardToSeal),TransitionFront(Regions.CandyGalleon,lambda l:_A),TransitionFront(Regions.FunkyGalleon,lambda l:_A)]),Regions.ShipyardUnderwater:Region('Shipyard Underwater',Levels.GloomyGalleon,_A,_C,[],[Event(Events.ShipyardEnguarde,lambda l:l.lanky)],[TransitionFront(Regions.TreasureRoom,lambda l:Events.ShipyardTreasureRoomOpened in l.Events),TransitionFront(Regions.Submarine,lambda l:l.mini and l.istiny,Transitions.GalleonShipyardToSubmarine),TransitionFront(Regions.Mechafish,lambda l:Events.MechafishSummoned in l.Events and l.isdiddy),TransitionFront(Regions.LankyShip,lambda l:Events.GalleonLankySwitch in l.Events and l.islanky,Transitions.GalleonShipyardToLanky),TransitionFront(Regions.TinyShip,lambda l:Events.GalleonTinySwitch in l.Events and l.istiny,Transitions.GalleonShipyardToTiny),TransitionFront(Regions.BongosShip,lambda l:l.bongos and l.isdonkey,Transitions.GalleonShipyardToBongos),TransitionFront(Regions.GuitarShip,lambda l:l.guitar and l.isdiddy,Transitions.GalleonShipyardToGuitar),TransitionFront(Regions.TromboneShip,lambda l:l.trombone and l.islanky,Transitions.GalleonShipyardToTrombone),TransitionFront(Regions.SaxophoneShip,lambda l:l.saxophone and l.istiny,Transitions.GalleonShipyardToSaxophone),TransitionFront(Regions.TriangleShip,lambda l:Events.GalleonChunkyPad in l.Events and l.ischunky,Transitions.GalleonShipyardToTriangle),TransitionFront(Regions.GalleonBossLobby,lambda l:not l.settings.tns_location_rando)]),Regions.SealRace:Region('Seal Race',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonDonkeySealRace,lambda l:l.isdonkey or l.settings.free_trade_items)],[],[TransitionFront(Regions.Shipyard,lambda l:_A,Transitions.GalleonSealToShipyard)],Transitions.GalleonShipyardToSeal),Regions.TreasureRoom:Region('Treasure Room',Levels.GloomyGalleon,_A,_C,[LocationLogic(Locations.GalleonLankyGoldTower,lambda l:l.balloon and l.islanky,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:Events.ShipyardTreasureRoomOpened in l.Events and l.swim),TransitionFront(Regions.TinyChest,lambda l:l.mini and l.istiny and l.swim,Transitions.GalleonTreasureToChest),TransitionFront(Regions.TreasureRoomDiddyGoldTower,lambda l:Events.WaterSwitch in l.Events and l.spring and l.diddy)]),Regions.TreasureRoomDiddyGoldTower:Region('Treasure Room Diddy Gold Tower',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonDiddyGoldTower,lambda l:l.spring and l.isdiddy,MinigameType.BonusBarrel),LocationLogic(Locations.GalleonKasplatGoldTower,lambda l:not l.settings.kasplat_rando)],[Event(Events.TreasureRoomTeleporterUnlocked,lambda l:l.spring and l.isdiddy)],[TransitionFront(Regions.TreasureRoom,lambda l:_A)]),Regions.TinyChest:Region('Tiny Chest',Levels.GloomyGalleon,_B,-1,[],[Event(Events.PearlsCollected,lambda l:_A)],[TransitionFront(Regions.TreasureRoom,lambda l:_A,Transitions.GalleonChestToTreasure)]),Regions.Submarine:Region('Submarine',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonTinySubmarine,lambda l:l.istiny or l.settings.free_trade_items,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonSubmarineToShipyard)]),Regions.Mechafish:Region('Mechafish',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonDiddyMechafish,lambda l:l.HasGun(Kongs.diddy)or l.settings.free_trade_items and l.HasGun(Kongs.any))],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A)]),Regions.LankyShip:Region('Lanky Ship',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonLanky2DoorShip,lambda l:l.islanky or l.settings.free_trade_items)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonLankyToShipyard)]),Regions.TinyShip:Region('Tiny Ship',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonTiny2DoorShip,lambda l:l.istiny or l.settings.free_trade_items,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonTinyToShipyard)]),Regions.BongosShip:Region('Bongos Ship',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonDonkey5DoorShip,lambda l:l.isdonkey or l.settings.free_trade_items,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonBongosToShipyard)]),Regions.GuitarShip:Region('Guitar Ship',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonDiddy5DoorShip,lambda l:l.isdiddy or l.settings.free_trade_items,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonGuitarToShipyard)]),Regions.TromboneShip:Region('Trombone Ship',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonLanky5DoorShip,lambda l:l.islanky or l.settings.free_trade_items)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonTromboneToShipyard)]),Regions.SaxophoneShip:Region('Saxophone Ship',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonTiny5DoorShip,lambda l:l.istiny or l.settings.free_trade_items),LocationLogic(Locations.GalleonBananaFairy5DoorShip,lambda l:l.camera)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonSaxophoneToShipyard)]),Regions.TriangleShip:Region('Triangle Ship',Levels.GloomyGalleon,_B,-1,[LocationLogic(Locations.GalleonChunky5DoorShip,lambda l:l.ischunky or l.settings.free_trade_items,MinigameType.BonusBarrel)],[],[TransitionFront(Regions.ShipyardUnderwater,lambda l:_A,Transitions.GalleonTriangleToShipyard)]),Regions.GalleonBossLobby:Region('Galleon Boss Lobby',Levels.GloomyGalleon,_A,_C,[],[],[TransitionFront(Regions.GalleonBoss,lambda l:l.IsBossReachable(Levels.GloomyGalleon))]),Regions.GalleonBoss:Region('Galleon Boss',Levels.GloomyGalleon,_B,_C,[LocationLogic(Locations.GalleonKey,lambda l:l.IsBossBeatable(Levels.GloomyGalleon))],[],[])}