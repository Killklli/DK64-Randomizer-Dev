'Collectible logic file for Angry Aztec.'
_B=True
_A=None
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Collectible
LogicRegions={Regions.AngryAztecStart:[],Regions.BetweenVinesByPortal:[Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:l.pineapple,_A,4)],Regions.AngryAztecOasis:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:l.coconut and l.strongKong,_A,2),Collectible(Collectibles.bunch,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,1),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,2),Collectible(Collectibles.coin,Kongs.donkey,lambda l:l.coconut and l.strongKong,_A,3),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,4),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,4)],Regions.TempleStart:[Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.Slam and l.peanut,_A,3),Collectible(Collectibles.banana,Kongs.diddy,lambda l:l.Slam,_A,3),Collectible(Collectibles.bunch,Kongs.chunky,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,4),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,3)],Regions.TempleUnderwater:[Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,7),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,9),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.banana,Kongs.tiny,lambda l:l.mini,_A,5),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,2),Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,4)],Regions.AngryAztecMain:[Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,2),Collectible(Collectibles.balloon,Kongs.donkey,lambda l:l.coconut,_A,1),Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,4),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:_B,_A,3),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.jetpack,_A,1),Collectible(Collectibles.bunch,Kongs.diddy,lambda l:l.jetpack,_A,1),Collectible(Collectibles.banana,Kongs.diddy,lambda l:_B,_A,4),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,10),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,5),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,10),Collectible(Collectibles.banana,Kongs.chunky,lambda l:_B,_A,6),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.diddy,lambda l:_B,_A,4),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,4),Collectible(Collectibles.coin,Kongs.lanky,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.vines,_A,4)],Regions.AztecDonkeyQuicksandCave:[Collectible(Collectibles.bunch,Kongs.donkey,lambda l:l.strongKong,_A,4),Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:_B,_A,4)],Regions.AztecBaboonBlast:[],Regions.DonkeyTemple:[Collectible(Collectibles.coin,Kongs.donkey,lambda l:l.coconut,_A,2)],Regions.DiddyTemple:[Collectible(Collectibles.balloon,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.peanut,_A,1),Collectible(Collectibles.coin,Kongs.diddy,lambda l:l.peanut,_A,1)],Regions.LankyTemple:[Collectible(Collectibles.balloon,Kongs.lanky,lambda l:l.grape,_A,1)],Regions.TinyTemple:[Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,1),Collectible(Collectibles.coin,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.coin,Kongs.tiny,lambda l:l.feather,_A,1)],Regions.ChunkyTemple:[Collectible(Collectibles.balloon,Kongs.chunky,lambda l:l.pineapple,_A,2),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.pineapple,_A,1),Collectible(Collectibles.coin,Kongs.chunky,lambda l:l.pineapple,_A,1)],Regions.AztecTinyRace:[],Regions.LlamaTemple:[Collectible(Collectibles.banana,Kongs.donkey,lambda l:_B,_A,15),Collectible(Collectibles.banana,Kongs.lanky,lambda l:_B,_A,6),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:lambda l:_B,_A,1),Collectible(Collectibles.balloon,Kongs.lanky,lambda l:lambda l:Events.AztecLlamaSpit in l.Events and l.grape and l.swim,_A,2),Collectible(Collectibles.bunch,Kongs.lanky,lambda l:lambda l:l.grape and l.vines,_A,1),Collectible(Collectibles.balloon,Kongs.tiny,lambda l:l.feather,_A,1),Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,3),Collectible(Collectibles.coin,Kongs.donkey,lambda l:_B,_A,5),Collectible(Collectibles.coin,Kongs.lanky,lambda l:l.grape and l.Slam and l.vines,_A,2),Collectible(Collectibles.coin,Kongs.tiny,lambda l:_B,_A,3)],Regions.LlamaTempleBack:[Collectible(Collectibles.banana,Kongs.tiny,lambda l:_B,_A,2),Collectible(Collectibles.bunch,Kongs.tiny,lambda l:l.Slam or l.twirl,_A,2)]}