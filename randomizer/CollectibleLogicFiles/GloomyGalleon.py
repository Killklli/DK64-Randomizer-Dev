'Collectible logic file for Gloomy Galleon.'
_B=True
_A=None
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Collectible
LogicRegions={Regions.GloomyGalleonStart:[Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,2),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape and l.punch and l.chunky,_A,2),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,4),Collectible(Collectibles.banana,Kongs.tiny,lambda l:l.vines,_A,3),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:l.vines,_A,1),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,1),Collectible(Collectibles.banana,Kongs.chunky,lambda l:l.vines,_A,3),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.GalleonBeyondPineappleGate:[Collectible(Collectibles.bunch,Kongs.tiny,lambda l:Events.WaterSwitch in l.Events,_A,3),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple and Events.WaterSwitch in l.Events,_A,1),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.LighthouseArea:[Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut and Events.WaterSwitch in l.Events,_A,1),Collectible(Collectibles.banana,Kongs.donkey,lambda l:Events.LighthouseEnguarde in l.Events,_A,10),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.jetpack,_A,2),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,4),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,10),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.jetpack,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:Events.LighthouseEnguarde in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.chunky,lambda l:Events.WaterSwitch in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.GalleonBaboonBlast:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,2)],Regions.Lighthouse:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,4),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A,1)],Regions.MermaidRoom:[Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3)],Regions.SickBay:[Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,4),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:l.punch,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.punch,_A,3)],Regions.Shipyard:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,10),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,6),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,4),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape,_A,1),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,3),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:Events.WaterSwitch in l.Events,_A,1),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.donkey,lambda l:Events.WaterSwitch in l.Events,_A,4),Collectible(Collectibles.coin,Kongs.donkey,lambda l:Events.ShipyardEnguarde in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,4),Collectible(Collectibles.coin,Kongs.diddy,lambda l:Events.ShipyardEnguarde in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:Events.ShipyardEnguarde in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:Events.ShipyardEnguarde in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:Events.ShipyardEnguarde in l.Events,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,5)],Regions.SealRace:[],Regions.TreasureRoom:[Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:Events.WaterSwitch in l.Events,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:Events.WaterSwitch in l.Events and l.balloon,_A,4),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1)],Regions.TinyChest:[Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,4)],Regions.Submarine:[],Regions.Mechafish:[],Regions.LankyShip:[Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,1)],Regions.TinyShip:[Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,2)],Regions.BongosShip:[Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,10),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3)],Regions.GuitarShip:[Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,4),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,2)],Regions.TromboneShip:[Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3)],Regions.SaxophoneShip:[Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,8),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,2)],Regions.TriangleShip:[]}