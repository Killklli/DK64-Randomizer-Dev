'Contains functions related to setting up the pool of shuffled items.'
_B='vanilla'
_A='shuffled'
import itertools
from random import shuffle
from randomizer.Enums.Events import Events
import randomizer.Enums.Kongs as KongObject
from randomizer.Enums.Items import Items
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Types import Types
from randomizer.Lists.Item import ItemFromKong
from randomizer.Lists.LevelInfo import LevelInfoList
from randomizer.Lists.Location import DonkeyMoveLocations,DiddyMoveLocations,LankyMoveLocations,TinyMoveLocations,ChunkyMoveLocations,SharedMoveLocations,TrainingBarrelLocations,LocationList
from randomizer.Lists.ShufflableExit import ShufflableExits
def PlaceConstants(settings):
	'Place items which are to be put in a hard-coded location.';E='levels';A=settings
	if A.key_8_helm:LocationList[Locations.HelmKey].PlaceItem(Items.HideoutHelmKey)
	if A.shuffle_loading_zones==E and Types.Key not in A.shuffled_location_types:
		for C in LevelInfoList.values():
			if not ShufflableExits[C.TransitionTo].shuffled:LocationList[C.KeyLocation].PlaceConstantItem(C.KeyItem)
			else:F=ShufflableExits[C.TransitionTo].shuffledId;G=[A for A in LevelInfoList.values()if A.TransitionTo==F][0];LocationList[G.KeyLocation].PlaceConstantItem(C.KeyItem)
		LocationList[Locations.HelmKey].PlaceConstantItem(Items.HideoutHelmKey)
	B=[]
	if A.kong_rando:B.append(Types.Kong)
	if not A.unlock_all_moves and A.move_rando!='off':
		B.append(Types.Shop)
		if A.training_barrels==_A:B.append(Types.TrainingBarrel)
		if A.shockwave_status!=_B:B.append(Types.Shockwave)
	if A.shuffle_loading_zones==E:B.append(Types.Key)
	B.extend(A.shuffled_location_types);H=[A for A in Types if A not in B]
	for D in LocationList:
		if LocationList[D].type in H:LocationList[D].PlaceDefaultItem()
	if A.starting_kongs_count==5:LocationList[Locations.DiddyKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.LankyKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.TinyKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.ChunkyKong].PlaceConstantItem(Items.NoItem)
	if A.unlock_all_moves:LocationList[Locations.SimianSlam].PlaceConstantItem(Items.NoItem);LocationList[Locations.SuperSimianSlam].PlaceConstantItem(Items.NoItem);LocationList[Locations.SuperDuperSimianSlam].PlaceConstantItem(Items.NoItem);LocationList[Locations.BaboonBlast].PlaceConstantItem(Items.NoItem);LocationList[Locations.StrongKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.GorillaGrab].PlaceConstantItem(Items.NoItem);LocationList[Locations.ChimpyCharge].PlaceConstantItem(Items.NoItem);LocationList[Locations.RocketbarrelBoost].PlaceConstantItem(Items.NoItem);LocationList[Locations.SimianSpring].PlaceConstantItem(Items.NoItem);LocationList[Locations.Orangstand].PlaceConstantItem(Items.NoItem);LocationList[Locations.BaboonBalloon].PlaceConstantItem(Items.NoItem);LocationList[Locations.OrangstandSprint].PlaceConstantItem(Items.NoItem);LocationList[Locations.MiniMonkey].PlaceConstantItem(Items.NoItem);LocationList[Locations.PonyTailTwirl].PlaceConstantItem(Items.NoItem);LocationList[Locations.Monkeyport].PlaceConstantItem(Items.NoItem);LocationList[Locations.HunkyChunky].PlaceConstantItem(Items.NoItem);LocationList[Locations.PrimatePunch].PlaceConstantItem(Items.NoItem);LocationList[Locations.GorillaGone].PlaceConstantItem(Items.NoItem);LocationList[Locations.CoconutGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.PeanutGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.GrapeGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.FeatherGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.PineappleGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.AmmoBelt1].PlaceConstantItem(Items.NoItem);LocationList[Locations.HomingAmmo].PlaceConstantItem(Items.NoItem);LocationList[Locations.AmmoBelt2].PlaceConstantItem(Items.NoItem);LocationList[Locations.SniperSight].PlaceConstantItem(Items.NoItem);LocationList[Locations.Bongos].PlaceConstantItem(Items.NoItem);LocationList[Locations.Guitar].PlaceConstantItem(Items.NoItem);LocationList[Locations.Trombone].PlaceConstantItem(Items.NoItem);LocationList[Locations.Saxophone].PlaceConstantItem(Items.NoItem);LocationList[Locations.Triangle].PlaceConstantItem(Items.NoItem);LocationList[Locations.MusicUpgrade1].PlaceConstantItem(Items.NoItem);LocationList[Locations.ThirdMelon].PlaceConstantItem(Items.NoItem);LocationList[Locations.MusicUpgrade2].PlaceConstantItem(Items.NoItem);LocationList[Locations.CameraAndShockwave].PlaceConstantItem(Items.NoItem)
def AllItems(settings):
	'Return all shuffled items.';B=settings;A=[]
	if Types.Blueprint in B.shuffled_location_types:A.extend(Blueprints(B))
	if Types.Banana in B.shuffled_location_types:A.extend(GoldenBananaItems())
	if Types.Coin in B.shuffled_location_types:A.extend(CompanyCoinItems())
	if Types.Crown in B.shuffled_location_types:A.extend(BattleCrownItems())
	if Types.Key in B.shuffled_location_types:A.extend(Keys())
	if Types.Medal in B.shuffled_location_types:A.extend(BananaMedalItems())
	if B.move_rando!='off':
		A.extend(DonkeyMoves);A.extend(DiddyMoves);A.extend(LankyMoves);A.extend(TinyMoves);A.extend(ChunkyMoves);A.extend(ImportantSharedMoves)
		if B.training_barrels==_A:A.extend(TrainingBarrelAbilities().copy())
		if B.shockwave_status=='shuffled_decoupled':A.append(Items.Camera);A.append(Items.Shockwave)
		else:A.append(Items.CameraAndShockwave)
	if B.kong_rando:A.extend(Kongs(B))
	return A
def AllKongMoves():'Return all moves.';A=[];A.extend(DonkeyMoves);A.extend(DiddyMoves);A.extend(LankyMoves);A.extend(TinyMoves);A.extend(ChunkyMoves);A.extend(ImportantSharedMoves);return A
def AllMovesForOwnedKongs(kongs):
	'Return all moves for the given list of Kongs.';B=kongs;A=[]
	if KongObject.Kongs.donkey in B:A.extend(DonkeyMoves)
	if KongObject.Kongs.diddy in B:A.extend(DiddyMoves)
	if KongObject.Kongs.lanky in B:A.extend(LankyMoves)
	if KongObject.Kongs.tiny in B:A.extend(TinyMoves)
	if KongObject.Kongs.chunky in B:A.extend(ChunkyMoves)
	A.extend(ImportantSharedMoves);return A
def Blueprints(settings):'Return all blueprint items.';A=[Items.DKIslesDonkeyBlueprint,Items.DKIslesDiddyBlueprint,Items.DKIslesLankyBlueprint,Items.DKIslesTinyBlueprint,Items.DKIslesChunkyBlueprint,Items.JungleJapesDonkeyBlueprint,Items.JungleJapesDiddyBlueprint,Items.JungleJapesLankyBlueprint,Items.JungleJapesTinyBlueprint,Items.JungleJapesChunkyBlueprint,Items.AngryAztecDonkeyBlueprint,Items.AngryAztecDiddyBlueprint,Items.AngryAztecLankyBlueprint,Items.AngryAztecTinyBlueprint,Items.AngryAztecChunkyBlueprint,Items.FranticFactoryDonkeyBlueprint,Items.FranticFactoryDiddyBlueprint,Items.FranticFactoryLankyBlueprint,Items.FranticFactoryTinyBlueprint,Items.FranticFactoryChunkyBlueprint,Items.GloomyGalleonDonkeyBlueprint,Items.GloomyGalleonDiddyBlueprint,Items.GloomyGalleonLankyBlueprint,Items.GloomyGalleonTinyBlueprint,Items.GloomyGalleonChunkyBlueprint,Items.FungiForestDonkeyBlueprint,Items.FungiForestDiddyBlueprint,Items.FungiForestLankyBlueprint,Items.FungiForestTinyBlueprint,Items.FungiForestChunkyBlueprint,Items.CrystalCavesDonkeyBlueprint,Items.CrystalCavesDiddyBlueprint,Items.CrystalCavesLankyBlueprint,Items.CrystalCavesTinyBlueprint,Items.CrystalCavesChunkyBlueprint,Items.CreepyCastleDonkeyBlueprint,Items.CreepyCastleDiddyBlueprint,Items.CreepyCastleLankyBlueprint,Items.CreepyCastleTinyBlueprint,Items.CreepyCastleChunkyBlueprint];return A
def BlueprintAssumedItems():'Items which are assumed to be owned while placing blueprints.';return Keys()+KeyAssumedItems()
def KeyAssumedItems():'Items which are assumed to be owned while placing keys.';return CompanyCoinItems()+CoinAssumedItems()
def CoinAssumedItems():'Items which are assumed to be owned while placing keys.';return BattleCrownItems()+CrownAssumedItems()
def CrownAssumedItems():'Items which are assumed to be owned while placing keys.';return BananaMedalItems()+MedalAssumedItems()
def MedalAssumedItems():'Items which are assumed to be owned while placing keys.';return GoldenBananaItems()
def Keys():'Return all key items.';return[Items.JungleJapesKey,Items.AngryAztecKey,Items.FranticFactoryKey,Items.GloomyGalleonKey,Items.FungiForestKey,Items.CrystalCavesKey,Items.CreepyCastleKey,Items.HideoutHelmKey]
def Kongs(settings):
	'Return Kong items depending on settings.';B=settings;A=[]
	if B.starting_kongs_count!=5:A=[Items.Donkey,Items.Diddy,Items.Lanky,Items.Tiny,Items.Chunky];A.remove(ItemFromKong(B.starting_kong))
	return A
def GetKongForItem(item):
	'Return Kong object from kong-type item.';A=item
	if A==Items.Donkey:return KongObject.Kongs.donkey
	elif A==Items.Diddy:return KongObject.Kongs.diddy
	elif A==Items.Lanky:return KongObject.Kongs.lanky
	elif A==Items.Tiny:return KongObject.Kongs.tiny
	else:return KongObject.Kongs.chunky
def Guns(settings):
	'Return all gun items.';A=[]
	if not settings.unlock_all_moves:A.extend([Items.Coconut,Items.Peanut,Items.Grape,Items.Feather,Items.Pineapple])
	return A
def Instruments(settings):
	'Return all instrument items.';A=[]
	if not settings.unlock_all_moves:A.extend([Items.Bongos,Items.Guitar,Items.Trombone,Items.Saxophone,Items.Triangle])
	return A
def TrainingBarrelAbilities():'Return all training barrel abilities.';A=[Items.Vines,Items.Swim,Items.Oranges,Items.Barrels];return A
def Upgrades(settings):
	'Return all upgrade items.';B=settings;A=[]
	if B.training_barrels==_A:A.extend(TrainingBarrelAbilities())
	if not B.unlock_all_moves:
		A.extend(itertools.repeat(Items.ProgressiveSlam,3-1))
		if B.progressive_upgrades:A.extend(itertools.repeat(Items.ProgressiveDonkeyPotion,3));A.extend(itertools.repeat(Items.ProgressiveDiddyPotion,3));A.extend(itertools.repeat(Items.ProgressiveLankyPotion,3));A.extend(itertools.repeat(Items.ProgressiveTinyPotion,3));A.extend(itertools.repeat(Items.ProgressiveChunkyPotion,3))
		else:A.extend([Items.BaboonBlast,Items.StrongKong,Items.GorillaGrab,Items.ChimpyCharge,Items.RocketbarrelBoost,Items.SimianSpring,Items.Orangstand,Items.BaboonBalloon,Items.OrangstandSprint,Items.MiniMonkey,Items.PonyTailTwirl,Items.Monkeyport,Items.HunkyChunky,Items.PrimatePunch,Items.GorillaGone])
		A.append(Items.HomingAmmo);A.append(Items.SniperSight);A.extend(itertools.repeat(Items.ProgressiveAmmoBelt,2));A.extend(itertools.repeat(Items.ProgressiveInstrumentUpgrade,3))
	if B.shockwave_status!='start_with':
		if B.shockwave_status in(_B,_A):A.append(Items.CameraAndShockwave)
		else:A.append(Items.Camera);A.append(Items.Shockwave)
	return A
def HighPriorityItems(settings):'Get all items which are of high importance logically.';B=settings;A=[];A.extend(Kongs(B));A.extend(Guns(B));A.extend(Instruments(B));A.extend(Upgrades(B));return A
def CompanyCoinItems():'Return the Company Coin items to be placed.';A=[];A.append(Items.NintendoCoin);A.append(Items.RarewareCoin);return A
def GoldenBananaItems():'Return a list of GBs to be placed.';A=[];A.extend(itertools.repeat(Items.GoldenBanana,161));return A
def BananaMedalItems():'Return a list of Banana Medals to be placed.';A=[];A.extend(itertools.repeat(Items.BananaMedal,40));return A
def BattleCrownItems():'Return a list of Crowns to be placed.';A=[];A.extend(itertools.repeat(Items.BattleCrown,10));return A
DonkeyMoves=[Items.Coconut,Items.Bongos,Items.BaboonBlast,Items.StrongKong,Items.GorillaGrab]
DiddyMoves=[Items.Peanut,Items.Guitar,Items.ChimpyCharge,Items.RocketbarrelBoost,Items.SimianSpring]
LankyMoves=[Items.Grape,Items.Trombone,Items.Orangstand,Items.BaboonBalloon,Items.OrangstandSprint]
TinyMoves=[Items.Feather,Items.Saxophone,Items.MiniMonkey,Items.PonyTailTwirl,Items.Monkeyport]
ChunkyMoves=[Items.Pineapple,Items.Triangle,Items.HunkyChunky,Items.PrimatePunch,Items.GorillaGone]
ImportantSharedMoves=[Items.ProgressiveSlam,Items.ProgressiveSlam,Items.SniperSight,Items.HomingAmmo]
JunkSharedMoves=[Items.ProgressiveAmmoBelt,Items.ProgressiveAmmoBelt,Items.ProgressiveInstrumentUpgrade,Items.ProgressiveInstrumentUpgrade,Items.ProgressiveInstrumentUpgrade]
ProgressiveSharedMovesSet={Items.ProgressiveAmmoBelt,Items.ProgressiveInstrumentUpgrade,Items.ProgressiveSlam}