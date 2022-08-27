'Shuffles the locations of shops.'
import random,randomizer.Logic as Logic
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.MapsAndExits import Maps
from randomizer.LogicClasses import TransitionFront
from randomizer.Spoiler import Spoiler
class ShopLocation:
	'Class which stores data for a shop location.'
	def __init__(A,shop,map,containing_region,shop_exit,locked=False):'Initialize with given parameters.';B=shop_exit;A.shop=shop;A.map=map;A.locked=locked;A.new_shop=shop;A.containing_region=containing_region;A.shop_exit=B;A.new_shop_exit=B
	def setShop(A,shop):'Assign new shop to shop location object.';A.new_shop=shop.shop;A.new_shop_exit=shop.shop_exit
available_shops={Levels.DKIsles:[ShopLocation(Regions.CrankyGeneric,Maps.TrainingGrounds,Regions.TrainingGrounds,Regions.CrankyIsles),ShopLocation(Regions.Snide,Maps.IslesSnideRoom,Regions.IslesSnideRoom,Regions.Snide)],Levels.JungleJapes:[ShopLocation(Regions.CrankyGeneric,Maps.JungleJapes,Regions.JapesBeyondCoconutGate2,Regions.CrankyJapes),ShopLocation(Regions.Snide,Maps.JungleJapes,Regions.JungleJapesMain,Regions.Snide),ShopLocation(Regions.FunkyGeneric,Maps.JungleJapes,Regions.JungleJapesMain,Regions.FunkyJapes)],Levels.AngryAztec:[ShopLocation(Regions.CrankyGeneric,Maps.AngryAztec,Regions.AngryAztecMain,Regions.CrankyAztec),ShopLocation(Regions.CandyGeneric,Maps.AngryAztec,Regions.AngryAztecStart,Regions.CandyAztec),ShopLocation(Regions.FunkyGeneric,Maps.AngryAztec,Regions.AngryAztecMain,Regions.FunkyAztec),ShopLocation(Regions.Snide,Maps.AngryAztec,Regions.AngryAztecMain,Regions.Snide)],Levels.FranticFactory:[ShopLocation(Regions.CrankyGeneric,Maps.FranticFactory,Regions.BeyondHatch,Regions.CrankyFactory),ShopLocation(Regions.CandyGeneric,Maps.FranticFactory,Regions.BeyondHatch,Regions.CandyFactory),ShopLocation(Regions.FunkyGeneric,Maps.FranticFactory,Regions.Testing,Regions.FunkyFactory),ShopLocation(Regions.Snide,Maps.FranticFactory,Regions.Testing,Regions.Snide)],Levels.GloomyGalleon:[ShopLocation(Regions.CrankyGeneric,Maps.GloomyGalleon,Regions.GloomyGalleonStart,Regions.CrankyGalleon),ShopLocation(Regions.CandyGeneric,Maps.GloomyGalleon,Regions.Shipyard,Regions.CandyGalleon,locked=True),ShopLocation(Regions.FunkyGeneric,Maps.GloomyGalleon,Regions.Shipyard,Regions.FunkyGalleon,locked=True),ShopLocation(Regions.Snide,Maps.GloomyGalleon,Regions.LighthouseArea,Regions.Snide)],Levels.FungiForest:[ShopLocation(Regions.CrankyGeneric,Maps.FungiForest,Regions.GiantMushroomArea,Regions.CrankyForest),ShopLocation(Regions.FunkyGeneric,Maps.FungiForest,Regions.WormArea,Regions.FunkyForest),ShopLocation(Regions.Snide,Maps.FungiForest,Regions.MillArea,Regions.Snide)],Levels.CrystalCaves:[ShopLocation(Regions.CrankyGeneric,Maps.CrystalCaves,Regions.CrystalCavesMain,Regions.CrankyCaves),ShopLocation(Regions.CandyGeneric,Maps.CrystalCaves,Regions.CabinArea,Regions.CandyCaves),ShopLocation(Regions.FunkyGeneric,Maps.CrystalCaves,Regions.CrystalCavesMain,Regions.FunkyCaves),ShopLocation(Regions.Snide,Maps.CrystalCaves,Regions.CavesSnideArea,Regions.Snide)],Levels.CreepyCastle:[ShopLocation(Regions.CrankyGeneric,Maps.CreepyCastle,Regions.CreepyCastleMain,Regions.CrankyCastle),ShopLocation(Regions.CandyGeneric,Maps.CastleUpperCave,Regions.UpperCave,Regions.CandyCastle),ShopLocation(Regions.FunkyGeneric,Maps.CastleLowerCave,Regions.LowerCave,Regions.FunkyCastle),ShopLocation(Regions.Snide,Maps.CreepyCastle,Regions.CreepyCastleMain,Regions.Snide)]}
def ShuffleShopLocations(spoiler):
	'Shuffle Shop locations within their own pool inside the level.';E=spoiler
	for B in available_shops:
		C=available_shops[B]
		for A in C:A.setShop(A)
	F={}
	for B in available_shops:
		if B==Levels.DKIsles and E.settings.shuffle_loading_zones=='all':continue
		C=available_shops[B];D=[]
		for A in C:
			if not A.locked:G=Logic.Regions[A.containing_region];G.exits=[exit for exit in G.exits if exit.dest!=A.shop_exit];D.append(A)
		random.shuffle(D);H={};I=0
		for (K,A) in enumerate(C):
			if not A.locked:A.setShop(D[I]);H[A.shop]=A.new_shop;I+=1;J=Logic.Regions[A.containing_region];J.exits.append(TransitionFront(A.new_shop_exit,lambda l:True))
		F[B]=H
	E.shuffled_shop_locations=F