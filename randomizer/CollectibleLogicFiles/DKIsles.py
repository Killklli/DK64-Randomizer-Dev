'Collectible logic file for DK Isles.'
_A=None
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Collectible
LogicRegions={Regions.TrainingGrounds:[Collectible(Collectibles.coin,Kongs.donkey,lambda l:True,_A,3),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A),Collectible(Collectibles.coin,Kongs.any,lambda l:l.vines and l.shockwave,_A)],Regions.IslesMain:[Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A),Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave and l.jetpack,_A)],Regions.Prison:[Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A)],Regions.BananaFairyRoom:[],Regions.JungleJapesLobby:[],Regions.AngryAztecLobby:[],Regions.CrocodileIsleBeyondLift:[],Regions.IslesSnideRoom:[],Regions.FranticFactoryLobby:[],Regions.GloomyGalleonLobby:[],Regions.CabinIsle:[Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave,_A)],Regions.FungiForestLobby:[],Regions.CrystalCavesLobby:[],Regions.CreepyCastleLobby:[Collectible(Collectibles.coin,Kongs.any,lambda l:l.shockwave and l.balloon,_A)],Regions.HideoutHelmLobby:[]}