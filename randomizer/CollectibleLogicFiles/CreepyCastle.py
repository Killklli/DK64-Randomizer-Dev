'Collectible logic file for Creepy Castle.'
_B=True
_A=None
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Collectible
LogicRegions={Regions.CreepyCastleMain:[Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,45),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.jetpack,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.jetpack,_A,1),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,45),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A,1),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.jetpack,_A,4),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.jetpack,_A,2),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.CastleBaboonBlast:[Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,5)],Regions.CastleTree:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.punch and l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.punch,_A,3)],Regions.Library:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:l.superDuperSlam,_A,2)],Regions.Ballroom:[Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.jetpack,_A,3),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3)],Regions.MuseumBehindGlass:[Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:l.monkeyport,_A,1),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather and l.monkeyport,_A,1)],Regions.Tower:[Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape,_A,1)],Regions.Greenhouse:[Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,6),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3)],Regions.TrashCan:[Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,2)],Regions.Shed:[Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,4)],Regions.Museum:[Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.LowerCave:[Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,4)],Regions.Crypt:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.charge and l.peanut,_A,1),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:l.punch and l.pineapple,_A,2),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.charge and l.peanut,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.punch and l.pineapple,_A,3)],Regions.Mausoleum:[Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape and l.sprint,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.lanky,lambda l:l.grape and l.sprint,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:l.twirl,_A,2)],Regions.UpperCave:[Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,30),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:l.twirl,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.Dungeon:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:l.superDuperSlam,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.punch,_A,2),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.punch,_A,2),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.superDuperSlam and l.peanut,_A,1),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape and l.superDuperSlam,_A,1),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape and l.superDuperSlam and l.trombone and l.balloon,_A,1),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.punch and l.pineapple,_A,2),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.lanky,lambda l:l.superDuperSlam and l.trombone and l.balloon,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.punch,_A,3)]}