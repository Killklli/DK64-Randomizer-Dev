'Collectible logic file for Jungle Japes.'
_B=True
_A=None
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Collectible
LogicRegions={Regions.JungleJapesMain:[Collectible(Collectibles.banana,Kongs.donkey,lambda l:l.vines,_A,5),Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,6),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,7),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,2),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.lanky,lambda l:l.handstand,_A,3),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.donkey,lambda l:l.vines,_A,3),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave and(l.handstand and l.lanky or l.twirl and l.tiny),_A,1)],Regions.JapesBaboonBlast:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,2)],Regions.JapesBeyondCoconutGate1:[Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,10),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3)],Regions.JapesBeyondCoconutGate2:[Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,9),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:Events.Rambi in l.Events,_A,1),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:Events.Rambi in l.Events,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:l.handstand,_A,6),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:l.handstand,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:Events.Rambi in l.Events,_A,1),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape,_A,1),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:Events.Rambi in l.Events,_A,1),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.donkey,lambda l:l.coconut,_A,3),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3)],Regions.JapesBeyondFeatherGate:[Collectible(Collectibles.bunch,Kongs.tiny,lambda l:l.mini,_A,3),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:l.mini,_A,3),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:l.hunkyChunky,_A,4),Collectible(Collectibles.coin,Kongs.tiny,lambda l:Events.JapesSpawnW5 in l.Events,_A,5),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.JapesBeyondPeanutGate:[Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:l.grape,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3)],Regions.Mine:[Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.Slam,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.Slam and l.charge,_A,1),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.Slam and l.peanut,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.charge,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.Slam,_A,1)],Regions.JapesLankyCave:[Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,2),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape,_A,1),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,2)],Regions.BeyondRambiGate:[Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,7),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,5)],Regions.TinyHive:[Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,8),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,2)],Regions.JapesCatacomb:[Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)]}