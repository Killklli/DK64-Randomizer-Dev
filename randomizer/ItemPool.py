'Contains functions related to setting up the pool of shuffled items.'
import itertools
from random import shuffle
import randomizer.Enums.Kongs as KongObject
from randomizer.Enums.Items import Items
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Transitions import Transitions
from randomizer.Lists.Item import ItemFromKong
from randomizer.Lists.LevelInfo import LevelInfoList
from randomizer.Lists.Location import LocationList
from randomizer.Lists.ShufflableExit import ShufflableExits
def PlaceConstants(settings):
	'Place items which are to be put in a hard-coded location.';D='levels';B=settings
	if B.shuffle_loading_zones==D:
		for C in LevelInfoList.values():
			if not ShufflableExits[C.TransitionTo].shuffled:LocationList[C.KeyLocation].PlaceConstantItem(C.KeyItem)
			else:E=ShufflableExits[C.TransitionTo].shuffledId;F=[A for A in LevelInfoList.values()if A.TransitionTo==E][0];LocationList[F.KeyLocation].PlaceConstantItem(C.KeyItem)
	if B.shuffle_items!='all':
		A=[]
		if B.shuffle_items=='moves':A.extend(DonkeyMoveLocations);A.extend(DiddyMoveLocations);A.extend(LankyMoveLocations);A.extend(TinyMoveLocations);A.extend(ChunkyMoveLocations);A.extend(SharedMoveLocations)
		if B.kong_rando:A.append(Locations.DiddyKong);A.append(Locations.LankyKong);A.append(Locations.TinyKong);A.append(Locations.ChunkyKong)
		if B.shuffle_loading_zones==D:A.append(Locations.JapesKey);A.append(Locations.AztecKey);A.append(Locations.FactoryKey);A.append(Locations.GalleonKey);A.append(Locations.ForestKey);A.append(Locations.CavesKey);A.append(Locations.CastleKey)
		G=[B for B in LocationList if B not in A]
		for H in G:LocationList[H].PlaceDefaultItem()
	if B.training_barrels=='normal':LocationList[Locations.IslesVinesTrainingBarrel].PlaceConstantItem(Items.Vines);LocationList[Locations.IslesSwimTrainingBarrel].PlaceConstantItem(Items.Swim);LocationList[Locations.IslesOrangesTrainingBarrel].PlaceConstantItem(Items.Oranges);LocationList[Locations.IslesBarrelsTrainingBarrel].PlaceConstantItem(Items.Barrels)
	elif B.training_barrels=='startwith':LocationList[Locations.IslesVinesTrainingBarrel].PlaceConstantItem(Items.NoItem);LocationList[Locations.IslesSwimTrainingBarrel].PlaceConstantItem(Items.NoItem);LocationList[Locations.IslesOrangesTrainingBarrel].PlaceConstantItem(Items.NoItem);LocationList[Locations.IslesBarrelsTrainingBarrel].PlaceConstantItem(Items.NoItem)
	if B.starting_kongs_count==5:LocationList[Locations.DiddyKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.LankyKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.TinyKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.ChunkyKong].PlaceConstantItem(Items.NoItem)
	if B.unlock_all_moves:LocationList[Locations.SimianSlam].PlaceConstantItem(Items.NoItem);LocationList[Locations.SuperSimianSlam].PlaceConstantItem(Items.NoItem);LocationList[Locations.SuperDuperSimianSlam].PlaceConstantItem(Items.NoItem);LocationList[Locations.BaboonBlast].PlaceConstantItem(Items.NoItem);LocationList[Locations.StrongKong].PlaceConstantItem(Items.NoItem);LocationList[Locations.GorillaGrab].PlaceConstantItem(Items.NoItem);LocationList[Locations.ChimpyCharge].PlaceConstantItem(Items.NoItem);LocationList[Locations.RocketbarrelBoost].PlaceConstantItem(Items.NoItem);LocationList[Locations.SimianSpring].PlaceConstantItem(Items.NoItem);LocationList[Locations.Orangstand].PlaceConstantItem(Items.NoItem);LocationList[Locations.BaboonBalloon].PlaceConstantItem(Items.NoItem);LocationList[Locations.OrangstandSprint].PlaceConstantItem(Items.NoItem);LocationList[Locations.MiniMonkey].PlaceConstantItem(Items.NoItem);LocationList[Locations.PonyTailTwirl].PlaceConstantItem(Items.NoItem);LocationList[Locations.Monkeyport].PlaceConstantItem(Items.NoItem);LocationList[Locations.HunkyChunky].PlaceConstantItem(Items.NoItem);LocationList[Locations.PrimatePunch].PlaceConstantItem(Items.NoItem);LocationList[Locations.GorillaGone].PlaceConstantItem(Items.NoItem);LocationList[Locations.CoconutGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.PeanutGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.GrapeGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.FeatherGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.PineappleGun].PlaceConstantItem(Items.NoItem);LocationList[Locations.AmmoBelt1].PlaceConstantItem(Items.NoItem);LocationList[Locations.HomingAmmo].PlaceConstantItem(Items.NoItem);LocationList[Locations.AmmoBelt2].PlaceConstantItem(Items.NoItem);LocationList[Locations.SniperSight].PlaceConstantItem(Items.NoItem);LocationList[Locations.Bongos].PlaceConstantItem(Items.NoItem);LocationList[Locations.Guitar].PlaceConstantItem(Items.NoItem);LocationList[Locations.Trombone].PlaceConstantItem(Items.NoItem);LocationList[Locations.Saxophone].PlaceConstantItem(Items.NoItem);LocationList[Locations.Triangle].PlaceConstantItem(Items.NoItem);LocationList[Locations.MusicUpgrade1].PlaceConstantItem(Items.NoItem);LocationList[Locations.ThirdMelon].PlaceConstantItem(Items.NoItem);LocationList[Locations.MusicUpgrade2].PlaceConstantItem(Items.NoItem)
	if B.unlock_fairy_shockwave:LocationList[Locations.CameraAndShockwave].PlaceConstantItem(Items.NoItem)
def AllItems(settings):
	'Return all shuffled items.';B=settings;A=[]
	if B.shuffle_items=='all':A.extend(Blueprints(B));A.extend(HighPriorityItems(B));A.extend(LowPriorityItems(B));A.extend(ExcessItems(B))
	elif B.shuffle_items=='moves':A.extend(DonkeyMoves);A.extend(DiddyMoves);A.extend(LankyMoves);A.extend(TinyMoves);A.extend(ChunkyMoves);A.extend(ImportantSharedMoves)
	if B.kong_rando:A.extend(Kongs(B))
	return A
def AllKongMoves():'Return all moves.';A=[];A.extend(DonkeyMoves);A.extend(DiddyMoves);A.extend(LankyMoves);A.extend(TinyMoves);A.extend(ChunkyMoves);A.extend(ImportantSharedMoves);return A
def OwnedKongMoves(kongs):
	'Return all moves for the given list of Kongs.';B=kongs;A=[]
	if KongObject.Kongs.donkey in B:A.extend(DonkeyMoves)
	if KongObject.Kongs.diddy in B:A.extend(DiddyMoves)
	if KongObject.Kongs.lanky in B:A.extend(LankyMoves)
	if KongObject.Kongs.tiny in B:A.extend(TinyMoves)
	if KongObject.Kongs.chunky in B:A.extend(ChunkyMoves)
	return A
def Blueprints(settings):'Return all blueprint items.';A=[Items.DKIslesDonkeyBlueprint,Items.DKIslesDiddyBlueprint,Items.DKIslesLankyBlueprint,Items.DKIslesTinyBlueprint,Items.DKIslesChunkyBlueprint,Items.JungleJapesDonkeyBlueprint,Items.JungleJapesDiddyBlueprint,Items.JungleJapesLankyBlueprint,Items.JungleJapesTinyBlueprint,Items.JungleJapesChunkyBlueprint,Items.AngryAztecDonkeyBlueprint,Items.AngryAztecDiddyBlueprint,Items.AngryAztecLankyBlueprint,Items.AngryAztecTinyBlueprint,Items.AngryAztecChunkyBlueprint,Items.FranticFactoryDonkeyBlueprint,Items.FranticFactoryDiddyBlueprint,Items.FranticFactoryLankyBlueprint,Items.FranticFactoryTinyBlueprint,Items.FranticFactoryChunkyBlueprint,Items.GloomyGalleonDonkeyBlueprint,Items.GloomyGalleonDiddyBlueprint,Items.GloomyGalleonLankyBlueprint,Items.GloomyGalleonTinyBlueprint,Items.GloomyGalleonChunkyBlueprint,Items.FungiForestDonkeyBlueprint,Items.FungiForestDiddyBlueprint,Items.FungiForestLankyBlueprint,Items.FungiForestTinyBlueprint,Items.FungiForestChunkyBlueprint,Items.CrystalCavesDonkeyBlueprint,Items.CrystalCavesDiddyBlueprint,Items.CrystalCavesLankyBlueprint,Items.CrystalCavesTinyBlueprint,Items.CrystalCavesChunkyBlueprint,Items.CreepyCastleDonkeyBlueprint,Items.CreepyCastleDiddyBlueprint,Items.CreepyCastleLankyBlueprint,Items.CreepyCastleTinyBlueprint,Items.CreepyCastleChunkyBlueprint];return A
def BlueprintAssumedItems(settings):'Items which are assumed to be owned while placing blueprints.';A=settings;return LowPriorityItems(A)+ExcessItems(A)
def Keys():'Return all key items.';A=[Items.JungleJapesKey,Items.AngryAztecKey,Items.FranticFactoryKey,Items.GloomyGalleonKey,Items.FungiForestKey,Items.CrystalCavesKey,Items.CreepyCastleKey,Items.HideoutHelmKey];return A
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
	if B.training_barrels=='shuffled':A.extend(TrainingBarrelAbilities())
	if not B.unlock_all_moves:
		A.extend(itertools.repeat(Items.ProgressiveSlam,3-1))
		if B.progressive_upgrades:A.extend(itertools.repeat(Items.ProgressiveDonkeyPotion,3));A.extend(itertools.repeat(Items.ProgressiveDiddyPotion,3));A.extend(itertools.repeat(Items.ProgressiveLankyPotion,3));A.extend(itertools.repeat(Items.ProgressiveTinyPotion,3));A.extend(itertools.repeat(Items.ProgressiveChunkyPotion,3))
		else:A.extend([Items.BaboonBlast,Items.StrongKong,Items.GorillaGrab,Items.ChimpyCharge,Items.RocketbarrelBoost,Items.SimianSpring,Items.Orangstand,Items.BaboonBalloon,Items.OrangstandSprint,Items.MiniMonkey,Items.PonyTailTwirl,Items.Monkeyport,Items.HunkyChunky,Items.PrimatePunch,Items.GorillaGone])
	if not B.unlock_fairy_shockwave:A.append(Items.CameraAndShockwave)
	return A
def HighPriorityItems(settings):'Get all items which are of high importance logically.\n\n    Placing these first prevents fill failures.\n    ';B=settings;A=[];A.extend(Kongs(B));A.extend(Guns(B));A.extend(Instruments(B));A.extend(Upgrades(B));return A
def HighPriorityAssumedItems(settings):'Items which are assumed to be owned while placing high priority items.';A=settings;return Blueprints(A)+LowPriorityItems(A)+ExcessItems(A)
def LowPriorityItems(settings):
	'While most of these items still have logical value they are not as important.';B=settings;A=[];A.extend(itertools.repeat(Items.GoldenBanana,100));A.extend(itertools.repeat(Items.BananaFairy,20));A.extend(itertools.repeat(Items.BananaMedal,15))
	if not B.crown_door_open:A.extend(itertools.repeat(Items.BattleCrown,4))
	if not B.coin_door_open:A.append(Items.NintendoCoin);A.append(Items.RarewareCoin)
	if not B.unlock_all_moves:
		A.append(Items.SniperSight)
		if not B.hard_shooting:A.append(Items.HomingAmmo)
	return A
def ExcessItems(settings):
	'Items which either have no logical value or are excess copies of those that do.';B=settings;A=[]
	if not B.unlock_all_moves:
		if B.hard_shooting:A.append(Items.HomingAmmo)
		A.extend(itertools.repeat(Items.ProgressiveAmmoBelt,2));A.extend(itertools.repeat(Items.ProgressiveInstrumentUpgrade,3))
	A.extend(itertools.repeat(Items.GoldenBanana,101));A.extend(itertools.repeat(Items.BananaMedal,25));A.extend(itertools.repeat(Items.BattleCrown,6))
	if B.crown_door_open:A.extend(itertools.repeat(Items.BattleCrown,4))
	if B.coin_door_open:A.append(Items.NintendoCoin);A.append(Items.RarewareCoin)
	return A
def GetMoveLocationsToRemove(sharedMoveShops):
	'Determine locations to remove from the move pool based on where shared moves got placed.';A=[]
	for B in sharedMoveShops:
		if B==Locations.SharedJapesPotion:A.append(Locations.BaboonBlast);A.append(Locations.ChimpyCharge);A.append(Locations.Orangstand);A.append(Locations.MiniMonkey);A.append(Locations.HunkyChunky)
		elif B==Locations.SharedJapesGun:A.append(Locations.CoconutGun);A.append(Locations.PeanutGun);A.append(Locations.GrapeGun);A.append(Locations.FeatherGun);A.append(Locations.PineappleGun)
		elif B==Locations.SharedAztecPotion:A.append(Locations.StrongKong);A.append(Locations.RocketbarrelBoost);A.append(Locations.LankyAztecPotion);A.append(Locations.TinyAztecPotion);A.append(Locations.ChunkyAztecPotion)
		elif B==Locations.SharedAztecGun:A.append(Locations.DonkeyAztecGun);A.append(Locations.DiddyAztecGun);A.append(Locations.LankyAztecGun);A.append(Locations.TinyAztecGun);A.append(Locations.ChunkyAztecGun)
		elif B==Locations.SharedAztecInstrument:A.append(Locations.Bongos);A.append(Locations.Guitar);A.append(Locations.Trombone);A.append(Locations.Saxophone);A.append(Locations.Triangle)
		elif B==Locations.SharedFactoryPotion:A.append(Locations.GorillaGrab);A.append(Locations.SimianSpring);A.append(Locations.BaboonBalloon);A.append(Locations.PonyTailTwirl);A.append(Locations.PrimatePunch)
		elif B==Locations.AmmoBelt1:A.append(Locations.DonkeyFactoryGun);A.append(Locations.DiddyFactoryGun);A.append(Locations.LankyFactoryGun);A.append(Locations.TinyFactoryGun);A.append(Locations.ChunkyFactoryGun)
		elif B==Locations.SharedFactoryInstrument:A.append(Locations.DonkeyFactoryInstrument);A.append(Locations.DiddyFactoryInstrument);A.append(Locations.LankyFactoryInstrument);A.append(Locations.TinyFactoryInstrument);A.append(Locations.ChunkyFactoryInstrument)
		elif B==Locations.SharedGalleonPotion:A.append(Locations.DonkeyGalleonPotion);A.append(Locations.DiddyGalleonPotion);A.append(Locations.LankyGalleonPotion);A.append(Locations.TinyGalleonPotion);A.append(Locations.ChunkyGalleonPotion)
		elif B==Locations.SharedGalleonGun:A.append(Locations.DonkeyGalleonGun);A.append(Locations.DiddyGalleonGun);A.append(Locations.LankyGalleonGun);A.append(Locations.TinyGalleonGun);A.append(Locations.ChunkyGalleonGun)
		elif B==Locations.MusicUpgrade1:A.append(Locations.DonkeyGalleonInstrument);A.append(Locations.DiddyGalleonInstrument);A.append(Locations.LankyGalleonInstrument);A.append(Locations.TinyGalleonInstrument);A.append(Locations.ChunkyGalleonInstrument)
		elif B==Locations.SuperSimianSlam:A.append(Locations.DonkeyForestPotion);A.append(Locations.DiddyForestPotion);A.append(Locations.LankyForestPotion);A.append(Locations.TinyForestPotion);A.append(Locations.ChunkyForestPotion)
		elif B==Locations.HomingAmmo:A.append(Locations.DonkeyForestGun);A.append(Locations.DiddyForestGun);A.append(Locations.LankyForestGun);A.append(Locations.TinyForestGun);A.append(Locations.ChunkyForestGun)
		elif B==Locations.SharedCavesPotion:A.append(Locations.DonkeyCavesPotion);A.append(Locations.DiddyCavesPotion);A.append(Locations.OrangstandSprint);A.append(Locations.Monkeyport);A.append(Locations.GorillaGone)
		elif B==Locations.AmmoBelt2:A.append(Locations.DonkeyCavesGun);A.append(Locations.DiddyCavesGun);A.append(Locations.LankyCavesGun);A.append(Locations.TinyCavesGun);A.append(Locations.ChunkyCavesGun)
		elif B==Locations.ThirdMelon:A.append(Locations.DonkeyCavesInstrument);A.append(Locations.DiddyCavesInstrument);A.append(Locations.LankyCavesInstrument);A.append(Locations.TinyCavesInstrument);A.append(Locations.ChunkyCavesInstrument)
		elif B==Locations.SuperDuperSimianSlam:A.append(Locations.DonkeyCastlePotion);A.append(Locations.DiddyCastlePotion);A.append(Locations.LankyCastlePotion);A.append(Locations.TinyCastlePotion);A.append(Locations.ChunkyCastlePotion)
		elif B==Locations.SniperSight:A.append(Locations.DonkeyCastleGun);A.append(Locations.DiddyCastleGun);A.append(Locations.LankyCastleGun);A.append(Locations.TinyCastleGun);A.append(Locations.ChunkyCastleGun)
		elif B==Locations.MusicUpgrade2:A.append(Locations.DonkeyCastleInstrument);A.append(Locations.DiddyCastleInstrument);A.append(Locations.LankyCastleInstrument);A.append(Locations.TinyCastleInstrument);A.append(Locations.ChunkyCastleInstrument)
		elif B==Locations.SimianSlam:A.append(Locations.DonkeyIslesPotion);A.append(Locations.DiddyIslesPotion);A.append(Locations.LankyIslesPotion);A.append(Locations.TinyIslesPotion);A.append(Locations.ChunkyIslesPotion)
	return set(A)
def GetKongMoveOccupiedShops():
	'Return shop locations that already contain a kong move and are therefore unable to hold a shared move.';D=None;B=[];C=[]
	for A in DonkeyMoveLocations:
		if LocationList[A].item is not D:C.append(A)
	for A in DiddyMoveLocations:
		if LocationList[A].item is not D:C.append(A)
	for A in LankyMoveLocations:
		if LocationList[A].item is not D:C.append(A)
	for A in TinyMoveLocations:
		if LocationList[A].item is not D:C.append(A)
	for A in ChunkyMoveLocations:
		if LocationList[A].item is not D:C.append(A)
	for A in C:
		if A in JapesCrankyMoveLocations:B.append(Locations.SharedJapesPotion)
		elif A in JapesFunkyMoveLocations:B.append(Locations.SharedJapesGun)
		elif A in AztecCrankyMoveLocations:B.append(Locations.SharedAztecPotion)
		elif A in AztecCandyMoveLocations:B.append(Locations.SharedAztecInstrument)
		elif A in AztecFunkyMoveLocations:B.append(Locations.SharedAztecGun)
		elif A in FactoryCrankyMoveLocations:B.append(Locations.SharedFactoryPotion)
		elif A in FactoryCandyMoveLocations:B.append(Locations.SharedFactoryInstrument)
		elif A in FactoryFunkyMoveLocations:B.append(Locations.AmmoBelt1)
		elif A in GalleonCrankyMoveLocations:B.append(Locations.SharedGalleonPotion)
		elif A in GalleonCandyMoveLocations:B.append(Locations.MusicUpgrade1)
		elif A in GalleonFunkyMoveLocations:B.append(Locations.SharedGalleonGun)
		elif A in ForestCrankyMoveLocations:B.append(Locations.SuperSimianSlam)
		elif A in ForestFunkyMoveLocations:B.append(Locations.HomingAmmo)
		elif A in CavesCrankyMoveLocations:B.append(Locations.SharedCavesPotion)
		elif A in CavesCandyMoveLocations:B.append(Locations.ThirdMelon)
		elif A in CavesFunkyMoveLocations:B.append(Locations.AmmoBelt2)
		elif A in CastleCrankyMoveLocations:B.append(Locations.SuperDuperSimianSlam)
		elif A in CastleCandyMoveLocations:B.append(Locations.MusicUpgrade2)
		elif A in CastleFunkyMoveLocations:B.append(Locations.SniperSight)
		elif A in IslesCrankyMoveLocations:B.append(Locations.SimianSlam)
	return list(set(B))
DonkeyMoveLocations={Locations.BaboonBlast,Locations.StrongKong,Locations.GorillaGrab,Locations.CoconutGun,Locations.Bongos,Locations.DonkeyGalleonPotion,Locations.DonkeyForestPotion,Locations.DonkeyCavesPotion,Locations.DonkeyCastlePotion,Locations.DonkeyAztecGun,Locations.DonkeyFactoryGun,Locations.DonkeyGalleonGun,Locations.DonkeyForestGun,Locations.DonkeyCavesGun,Locations.DonkeyCastleGun,Locations.DonkeyFactoryInstrument,Locations.DonkeyGalleonInstrument,Locations.DonkeyCavesInstrument,Locations.DonkeyCastleInstrument,Locations.DonkeyIslesPotion}
DiddyMoveLocations={Locations.ChimpyCharge,Locations.RocketbarrelBoost,Locations.SimianSpring,Locations.PeanutGun,Locations.Guitar,Locations.DiddyGalleonPotion,Locations.DiddyForestPotion,Locations.DiddyCavesPotion,Locations.DiddyCastlePotion,Locations.DiddyAztecGun,Locations.DiddyFactoryGun,Locations.DiddyGalleonGun,Locations.DiddyForestGun,Locations.DiddyCavesGun,Locations.DiddyCastleGun,Locations.DiddyFactoryInstrument,Locations.DiddyGalleonInstrument,Locations.DiddyCavesInstrument,Locations.DiddyCastleInstrument,Locations.DiddyIslesPotion}
LankyMoveLocations={Locations.Orangstand,Locations.BaboonBalloon,Locations.OrangstandSprint,Locations.GrapeGun,Locations.Trombone,Locations.LankyAztecPotion,Locations.LankyGalleonPotion,Locations.LankyForestPotion,Locations.LankyCastlePotion,Locations.LankyAztecGun,Locations.LankyFactoryGun,Locations.LankyGalleonGun,Locations.LankyForestGun,Locations.LankyCavesGun,Locations.LankyCastleGun,Locations.LankyFactoryInstrument,Locations.LankyGalleonInstrument,Locations.LankyCavesInstrument,Locations.LankyCastleInstrument,Locations.LankyIslesPotion}
TinyMoveLocations={Locations.MiniMonkey,Locations.PonyTailTwirl,Locations.Monkeyport,Locations.FeatherGun,Locations.Saxophone,Locations.TinyAztecPotion,Locations.TinyGalleonPotion,Locations.TinyForestPotion,Locations.TinyCastlePotion,Locations.TinyAztecGun,Locations.TinyFactoryGun,Locations.TinyGalleonGun,Locations.TinyForestGun,Locations.TinyCavesGun,Locations.TinyCastleGun,Locations.TinyFactoryInstrument,Locations.TinyGalleonInstrument,Locations.TinyCavesInstrument,Locations.TinyCastleInstrument,Locations.TinyIslesPotion}
ChunkyMoveLocations={Locations.HunkyChunky,Locations.PrimatePunch,Locations.GorillaGone,Locations.PineappleGun,Locations.Triangle,Locations.ChunkyAztecPotion,Locations.ChunkyGalleonPotion,Locations.ChunkyForestPotion,Locations.ChunkyCastlePotion,Locations.ChunkyAztecGun,Locations.ChunkyFactoryGun,Locations.ChunkyGalleonGun,Locations.ChunkyForestGun,Locations.ChunkyCavesGun,Locations.ChunkyCastleGun,Locations.ChunkyFactoryInstrument,Locations.ChunkyGalleonInstrument,Locations.ChunkyCavesInstrument,Locations.ChunkyCastleInstrument,Locations.ChunkyIslesPotion}
SharedMoveLocations={Locations.SimianSlam,Locations.SuperSimianSlam,Locations.SuperDuperSimianSlam,Locations.SniperSight,Locations.HomingAmmo,Locations.AmmoBelt1,Locations.AmmoBelt2,Locations.MusicUpgrade1,Locations.ThirdMelon,Locations.MusicUpgrade2,Locations.SharedJapesPotion,Locations.SharedJapesGun,Locations.SharedAztecPotion,Locations.SharedAztecGun,Locations.SharedAztecInstrument,Locations.SharedFactoryPotion,Locations.SharedFactoryInstrument,Locations.SharedGalleonPotion,Locations.SharedGalleonGun,Locations.SharedCavesPotion}
DonkeyMoves=[Items.Coconut,Items.Bongos,Items.BaboonBlast,Items.StrongKong,Items.GorillaGrab]
DiddyMoves=[Items.Peanut,Items.Guitar,Items.ChimpyCharge,Items.RocketbarrelBoost,Items.SimianSpring]
LankyMoves=[Items.Grape,Items.Trombone,Items.Orangstand,Items.BaboonBalloon,Items.OrangstandSprint]
TinyMoves=[Items.Feather,Items.Saxophone,Items.MiniMonkey,Items.PonyTailTwirl,Items.Monkeyport]
ChunkyMoves=[Items.Pineapple,Items.Triangle,Items.HunkyChunky,Items.PrimatePunch,Items.GorillaGone]
ImportantSharedMoves=[Items.ProgressiveSlam,Items.ProgressiveSlam,Items.SniperSight,Items.HomingAmmo]
JunkSharedMoves=[Items.ProgressiveAmmoBelt,Items.ProgressiveAmmoBelt,Items.ProgressiveInstrumentUpgrade,Items.ProgressiveInstrumentUpgrade,Items.ProgressiveInstrumentUpgrade]
JapesCrankyMoveLocations={Locations.BaboonBlast,Locations.ChimpyCharge,Locations.Orangstand,Locations.MiniMonkey,Locations.HunkyChunky,Locations.SharedJapesPotion}
JapesFunkyMoveLocations={Locations.CoconutGun,Locations.PeanutGun,Locations.GrapeGun,Locations.FeatherGun,Locations.PineappleGun,Locations.SharedJapesGun}
AztecCrankyMoveLocations={Locations.StrongKong,Locations.RocketbarrelBoost,Locations.LankyAztecPotion,Locations.TinyAztecPotion,Locations.ChunkyAztecPotion,Locations.SharedAztecPotion}
AztecCandyMoveLocations={Locations.Bongos,Locations.Guitar,Locations.Trombone,Locations.Saxophone,Locations.Triangle,Locations.SharedAztecInstrument}
AztecFunkyMoveLocations={Locations.DonkeyAztecGun,Locations.DiddyAztecGun,Locations.LankyAztecGun,Locations.TinyAztecGun,Locations.ChunkyAztecGun,Locations.SharedAztecGun}
FactoryCrankyMoveLocations={Locations.GorillaGrab,Locations.SimianSpring,Locations.BaboonBalloon,Locations.PonyTailTwirl,Locations.PrimatePunch,Locations.SharedFactoryPotion}
FactoryCandyMoveLocations={Locations.DonkeyFactoryInstrument,Locations.DiddyFactoryInstrument,Locations.LankyFactoryInstrument,Locations.TinyFactoryInstrument,Locations.ChunkyFactoryInstrument,Locations.SharedFactoryInstrument}
FactoryFunkyMoveLocations={Locations.DonkeyFactoryGun,Locations.DiddyFactoryGun,Locations.LankyFactoryGun,Locations.TinyFactoryGun,Locations.ChunkyFactoryGun,Locations.AmmoBelt1}
GalleonCrankyMoveLocations={Locations.DonkeyGalleonPotion,Locations.DiddyGalleonPotion,Locations.LankyGalleonPotion,Locations.TinyGalleonPotion,Locations.ChunkyGalleonPotion,Locations.SharedGalleonPotion}
GalleonCandyMoveLocations={Locations.DonkeyGalleonInstrument,Locations.DiddyGalleonInstrument,Locations.LankyGalleonInstrument,Locations.TinyGalleonInstrument,Locations.ChunkyGalleonInstrument,Locations.MusicUpgrade1}
GalleonFunkyMoveLocations={Locations.DonkeyGalleonGun,Locations.DiddyGalleonGun,Locations.LankyGalleonGun,Locations.TinyGalleonGun,Locations.ChunkyGalleonGun,Locations.SharedGalleonGun}
ForestCrankyMoveLocations={Locations.DonkeyForestPotion,Locations.DiddyForestPotion,Locations.LankyForestPotion,Locations.TinyForestPotion,Locations.ChunkyForestPotion,Locations.SuperSimianSlam}
ForestFunkyMoveLocations={Locations.DonkeyForestGun,Locations.DiddyForestGun,Locations.LankyForestGun,Locations.TinyForestGun,Locations.ChunkyForestGun,Locations.HomingAmmo}
CavesCrankyMoveLocations={Locations.DonkeyCavesPotion,Locations.DiddyCavesPotion,Locations.OrangstandSprint,Locations.Monkeyport,Locations.GorillaGone,Locations.SharedCavesPotion}
CavesCandyMoveLocations={Locations.DonkeyCavesInstrument,Locations.DiddyCavesInstrument,Locations.LankyCavesInstrument,Locations.TinyCavesInstrument,Locations.ChunkyCavesInstrument,Locations.ThirdMelon}
CavesFunkyMoveLocations={Locations.DonkeyCavesGun,Locations.DiddyCavesGun,Locations.LankyCavesGun,Locations.TinyCavesGun,Locations.ChunkyCavesGun,Locations.AmmoBelt2}
CastleCrankyMoveLocations={Locations.DonkeyCastlePotion,Locations.DiddyCastlePotion,Locations.LankyCastlePotion,Locations.TinyCastlePotion,Locations.ChunkyCastlePotion,Locations.SuperDuperSimianSlam}
CastleCandyMoveLocations={Locations.DonkeyCastleInstrument,Locations.DiddyCastleInstrument,Locations.LankyCastleInstrument,Locations.TinyCastleInstrument,Locations.ChunkyCastleInstrument,Locations.MusicUpgrade2}
CastleFunkyMoveLocations={Locations.DonkeyCastleGun,Locations.DiddyCastleGun,Locations.LankyCastleGun,Locations.TinyCastleGun,Locations.ChunkyCastleGun,Locations.SniperSight}
IslesCrankyMoveLocations={Locations.DonkeyIslesPotion,Locations.DiddyIslesPotion,Locations.LankyIslesPotion,Locations.TinyIslesPotion,Locations.ChunkyIslesPotion,Locations.SimianSlam}