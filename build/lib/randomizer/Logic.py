'Contains the class which holds logic variables, and the master copy of regions.'
_C=None
_B=True
_A=False
import randomizer.CollectibleLogicFiles.AngryAztec,randomizer.CollectibleLogicFiles.CreepyCastle,randomizer.CollectibleLogicFiles.CrystalCaves,randomizer.CollectibleLogicFiles.DKIsles,randomizer.CollectibleLogicFiles.FranticFactory,randomizer.CollectibleLogicFiles.FungiForest,randomizer.CollectibleLogicFiles.GloomyGalleon,randomizer.CollectibleLogicFiles.JungleJapes,randomizer.LogicFiles.AngryAztec,randomizer.LogicFiles.CreepyCastle,randomizer.LogicFiles.CrystalCaves,randomizer.LogicFiles.DKIsles,randomizer.LogicFiles.FranticFactory,randomizer.LogicFiles.FungiForest,randomizer.LogicFiles.GloomyGalleon,randomizer.LogicFiles.HideoutHelm,randomizer.LogicFiles.JungleJapes,randomizer.LogicFiles.Shops
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Time import Time
from randomizer.Lists.Location import Location,LocationList
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.ShufflableExit import GetShuffledLevelIndex
from randomizer.Prices import CanBuy,GetPriceOfMoveItem
STARTING_SLAM=1
class LogicVarHolder:
	'Used to store variables when checking logic conditions.'
	def __init__(A,settings=_C):
		'Initialize with given parameters.';B=settings
		if B is _C:return
		A.settings=B;A.startkong=A.settings.starting_kong;A.Reset()
	def Reset(A):
		'Reset all logic variables.\n\n        Done between reachability searches and upon initialization.\n        ';A.donkey=Kongs.donkey in A.settings.starting_kong_list;A.diddy=Kongs.diddy in A.settings.starting_kong_list;A.lanky=Kongs.lanky in A.settings.starting_kong_list;A.tiny=Kongs.tiny in A.settings.starting_kong_list;A.chunky=Kongs.chunky in A.settings.starting_kong_list;A.vines=_B;A.swim=_B;A.oranges=_B;A.barrels=_B;A.progDonkey=3 if A.settings.unlock_all_moves else 0;A.blast=A.settings.unlock_all_moves;A.strongKong=A.settings.unlock_all_moves;A.grab=A.settings.unlock_all_moves;A.progDiddy=3 if A.settings.unlock_all_moves else 0;A.charge=A.settings.unlock_all_moves;A.jetpack=A.settings.unlock_all_moves;A.spring=A.settings.unlock_all_moves;A.progLanky=3 if A.settings.unlock_all_moves else 0;A.handstand=A.settings.unlock_all_moves;A.balloon=A.settings.unlock_all_moves;A.sprint=A.settings.unlock_all_moves;A.progTiny=3 if A.settings.unlock_all_moves else 0;A.mini=A.settings.unlock_all_moves;A.twirl=A.settings.unlock_all_moves;A.monkeyport=A.settings.unlock_all_moves;A.progChunky=3 if A.settings.unlock_all_moves else 0;A.hunkyChunky=A.settings.unlock_all_moves;A.punch=A.settings.unlock_all_moves;A.gorillaGone=A.settings.unlock_all_moves;A.coconut=A.settings.unlock_all_moves;A.peanut=A.settings.unlock_all_moves;A.grape=A.settings.unlock_all_moves;A.feather=A.settings.unlock_all_moves;A.pineapple=A.settings.unlock_all_moves;A.bongos=A.settings.unlock_all_moves;A.guitar=A.settings.unlock_all_moves;A.trombone=A.settings.unlock_all_moves;A.saxophone=A.settings.unlock_all_moves;A.triangle=A.settings.unlock_all_moves;A.nintendoCoin=_A;A.rarewareCoin=_A;A.camera=A.settings.unlock_fairy_shockwave;A.shockwave=A.settings.unlock_fairy_shockwave;A.scope=A.settings.unlock_all_moves;A.homing=A.settings.unlock_all_moves;A.JapesKey=_A;A.AztecKey=_A;A.FactoryKey=_A;A.GalleonKey=_A;A.ForestKey=_A;A.CavesKey=_A;A.CastleKey=_A;A.HelmKey=_A;A.HelmDonkey1=_A;A.HelmDonkey2=_A;A.HelmDiddy1=_A;A.HelmDiddy2=_A;A.HelmLanky1=_A;A.HelmLanky2=_A;A.HelmTiny1=_A;A.HelmTiny2=_A;A.HelmChunky1=_A;A.HelmChunky2=_A;A.Slam=3 if A.settings.unlock_all_moves else STARTING_SLAM;A.AmmoBelts=2 if A.settings.unlock_all_moves else 0;A.InstUpgrades=3 if A.settings.unlock_all_moves else 0;A.GoldenBananas=0;A.BananaFairies=0;A.BananaMedals=0;A.BattleCrowns=0;A.superSlam=A.settings.unlock_all_moves;A.superDuperSlam=A.settings.unlock_all_moves;A.Blueprints=[];A.Events=[];C=[Events.JapesKeyTurnedIn,Events.AztecKeyTurnedIn,Events.FactoryKeyTurnedIn,Events.GalleonKeyTurnedIn,Events.ForestKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn,Events.HelmKeyTurnedIn]
		for B in C:
			if B not in A.settings.krool_keys_required:A.Events.append(B)
		A.ColoredBananas=[]
		for D in range(7):A.ColoredBananas.append([0]*5)
		A.Coins=[0]*5;A.donkeyAccess=_A;A.diddyAccess=_A;A.lankyAccess=_A;A.tinyAccess=_A;A.chunkyAccess=_A;A.kong=A.startkong;A.UpdateKongs()
	def Update(A,ownedItems):'Update logic variables based on owned items.';B=ownedItems;A.donkey=A.donkey or Items.Donkey in B or A.startkong==Kongs.donkey;A.diddy=A.diddy or Items.Diddy in B or A.startkong==Kongs.diddy;A.lanky=A.lanky or Items.Lanky in B or A.startkong==Kongs.lanky;A.tiny=A.tiny or Items.Tiny in B or A.startkong==Kongs.tiny;A.chunky=A.chunky or Items.Chunky in B or A.startkong==Kongs.chunky;A.vines=A.vines or Items.Vines in B;A.swim=A.swim or Items.Swim in B;A.oranges=A.oranges or Items.Oranges in B;A.barrels=A.barrels or Items.Barrels in B;A.progDonkey=sum((1 for A in B if A==Items.ProgressiveDonkeyPotion));A.blast=A.blast or(Items.BaboonBlast in B or A.progDonkey>=1)and A.donkey;A.strongKong=A.strongKong or(Items.StrongKong in B or A.progDonkey>=2)and A.donkey;A.grab=A.grab or(Items.GorillaGrab in B or A.progDonkey>=3)and A.donkey;A.progDiddy=sum((1 for A in B if A==Items.ProgressiveDiddyPotion));A.charge=A.charge or(Items.ChimpyCharge in B or A.progDiddy>=1)and A.diddy;A.jetpack=A.jetpack or(Items.RocketbarrelBoost in B or A.progDiddy>=2)and A.diddy;A.spring=A.spring or(Items.SimianSpring in B or A.progDiddy>=3)and A.diddy;A.progLanky=sum((1 for A in B if A==Items.ProgressiveLankyPotion));A.handstand=A.handstand or(Items.Orangstand in B or A.progLanky>=1)and A.lanky;A.balloon=A.balloon or(Items.BaboonBalloon in B or A.progLanky>=2)and A.lanky;A.sprint=A.sprint or(Items.OrangstandSprint in B or A.progLanky>=3)and A.lanky;A.progTiny=sum((1 for A in B if A==Items.ProgressiveTinyPotion));A.mini=A.mini or(Items.MiniMonkey in B or A.progTiny>=1)and A.tiny;A.twirl=A.twirl or(Items.PonyTailTwirl in B or A.progTiny>=2)and A.tiny;A.monkeyport=A.monkeyport or(Items.Monkeyport in B or A.progTiny>=3)and A.tiny;A.progChunky=sum((1 for A in B if A==Items.ProgressiveChunkyPotion));A.hunkyChunky=A.hunkyChunky or(Items.HunkyChunky in B or A.progChunky>=1)and A.chunky;A.punch=A.punch or(Items.PrimatePunch in B or A.progChunky>=2)and A.chunky;A.gorillaGone=A.gorillaGone or(Items.GorillaGone in B or A.progChunky>=3)and A.chunky;A.coconut=A.coconut or Items.Coconut in B and A.donkey;A.peanut=A.peanut or Items.Peanut in B and A.diddy;A.grape=A.grape or Items.Grape in B and A.lanky;A.feather=A.feather or Items.Feather in B and A.tiny;A.pineapple=A.pineapple or Items.Pineapple in B and A.chunky;A.bongos=A.bongos or Items.Bongos in B and A.donkey;A.guitar=A.guitar or Items.Guitar in B and A.diddy;A.trombone=A.trombone or Items.Trombone in B and A.lanky;A.saxophone=A.saxophone or Items.Saxophone in B and A.tiny;A.triangle=A.triangle or Items.Triangle in B and A.chunky;A.nintendoCoin=A.nintendoCoin or Items.NintendoCoin in B;A.rarewareCoin=A.rarewareCoin or Items.RarewareCoin in B;A.JapesKey=A.JapesKey or Items.JungleJapesKey in B;A.AztecKey=A.AztecKey or Items.AngryAztecKey in B;A.FactoryKey=A.FactoryKey or Items.FranticFactoryKey in B;A.GalleonKey=A.GalleonKey or Items.GloomyGalleonKey in B;A.ForestKey=A.ForestKey or Items.FungiForestKey in B;A.CavesKey=A.CavesKey or Items.CrystalCavesKey in B;A.CastleKey=A.CastleKey or Items.CreepyCastleKey in B;A.HelmKey=A.HelmKey or Items.HideoutHelmKey in B;A.HelmDonkey1=A.HelmDonkey1 or Items.HelmDonkey1 in B;A.HelmDonkey2=A.HelmDonkey2 or Items.HelmDonkey2 in B;A.HelmDiddy1=A.HelmDiddy1 or Items.HelmDiddy1 in B;A.HelmDiddy2=A.HelmDiddy2 or Items.HelmDiddy2 in B;A.HelmLanky1=A.HelmLanky1 or Items.HelmLanky1 in B;A.HelmLanky2=A.HelmLanky2 or Items.HelmLanky2 in B;A.HelmTiny1=A.HelmTiny1 or Items.HelmTiny1 in B;A.HelmTiny2=A.HelmTiny2 or Items.HelmTiny2 in B;A.HelmChunky1=A.HelmChunky1 or Items.HelmChunky1 in B;A.HelmChunky2=A.HelmChunky2 or Items.HelmChunky2 in B;A.Slam=3 if A.settings.unlock_all_moves else sum((1 for A in B if A==Items.ProgressiveSlam))+STARTING_SLAM;A.AmmoBelts=2 if A.settings.unlock_all_moves else sum((1 for A in B if A==Items.ProgressiveAmmoBelt));A.InstUpgrades=3 if A.settings.unlock_all_moves else sum((1 for A in B if A==Items.ProgressiveInstrumentUpgrade));A.GoldenBananas=sum((1 for A in B if A==Items.GoldenBanana));A.BananaFairies=sum((1 for A in B if A==Items.BananaFairy));A.BananaMedals=sum((1 for A in B if A==Items.BananaMedal));A.BattleCrowns=sum((1 for A in B if A==Items.BattleCrown));A.camera=A.camera or Items.CameraAndShockwave in B;A.shockwave=A.shockwave or Items.CameraAndShockwave in B;A.scope=A.scope or Items.SniperSight in B;A.homing=A.homing or Items.HomingAmmo in B;A.superSlam=A.Slam>=2;A.superDuperSlam=A.Slam>=3;A.Blueprints=[A for A in B if A>=Items.JungleJapesDonkeyBlueprint]
	def AddEvent(A,event):'Add an event to events list so it can be checked for logically.';A.Events.append(event)
	def SetKong(A,kong):'Set current kong for logic.';A.kong=kong;A.UpdateKongs()
	def GetKongs(B):
		'Return all owned kongs.';A=[]
		if B.donkey:A.append(Kongs.donkey)
		if B.diddy:A.append(Kongs.diddy)
		if B.lanky:A.append(Kongs.lanky)
		if B.tiny:A.append(Kongs.tiny)
		if B.chunky:A.append(Kongs.chunky)
		return A
	def UpdateKongs(A):'Set variables for current kong based on self.kong.';A.isdonkey=A.kong==Kongs.donkey;A.isdiddy=A.kong==Kongs.diddy;A.islanky=A.kong==Kongs.lanky;A.istiny=A.kong==Kongs.tiny;A.ischunky=A.kong==Kongs.chunky
	def IsKong(B,kong):
		'Check if logic is currently a specific kong.';A=kong
		if A==Kongs.donkey:return B.isdonkey
		if A==Kongs.diddy:return B.isdiddy
		if A==Kongs.lanky:return B.islanky
		if A==Kongs.tiny:return B.istiny
		if A==Kongs.chunky:return B.ischunky
		if A==Kongs.any:return _B
	def HasKong(B,kong):
		'Check if logic currently owns a specific kong.';A=kong
		if A==Kongs.donkey:return B.donkey
		if A==Kongs.diddy:return B.diddy
		if A==Kongs.lanky:return B.lanky
		if A==Kongs.tiny:return B.tiny
		if A==Kongs.chunky:return B.chunky
		if A==Kongs.any:return _B
	def HasGun(A,kong):
		'Check if logic currently is currently the specified kong and owns a gun for them.';B=kong
		if B==Kongs.donkey:return A.coconut and A.isdonkey
		if B==Kongs.diddy:return A.peanut and A.isdiddy
		if B==Kongs.lanky:return A.grape and A.islanky
		if B==Kongs.tiny:return A.feather and A.istiny
		if B==Kongs.chunky:return A.pineapple and A.ischunky
		if B==Kongs.any:return A.coconut and A.isdonkey or A.peanut and A.isdiddy or A.grape and A.islanky or A.feather and A.istiny or A.pineapple and A.ischunky
	def HasInstrument(A,kong):
		'Check if logic currently is currently the specified kong and owns an instrument for them.';B=kong
		if B==Kongs.donkey:return A.bongos and A.isdonkey
		if B==Kongs.diddy:return A.guitar and A.isdiddy
		if B==Kongs.lanky:return A.trombone and A.islanky
		if B==Kongs.tiny:return A.saxophone and A.istiny
		if B==Kongs.chunky:return A.triangle and A.ischunky
		if B==Kongs.any:return A.bongos and A.isdonkey or A.guitar and A.isdiddy or A.trombone and A.islanky or A.saxophone and A.istiny or A.triangle and A.ischunky
	def CanFreeDiddy(A):'Check if kong at Diddy location can be freed.';return A.HasGun(A.settings.diddy_freeing_kong)
	def CanFreeTiny(A):
		'Check if kong at Tiny location can be freed,r equires either chimpy charge or primate punch.'
		if A.settings.tiny_freeing_kong==Kongs.diddy:return A.charge and A.isdiddy
		elif A.settings.tiny_freeing_kong==Kongs.chunky:return A.punch and A.ischunky
		elif A.settings.tiny_freeing_kong==Kongs.any:return _B
	def CanFreeLanky(A):'Check if kong at Lanky location can be freed, requires freeing kong to have its gun and instrument.';return A.HasGun(A.settings.lanky_freeing_kong)and A.HasInstrument(A.settings.lanky_freeing_kong)
	def CanFreeChunky(A):'Check if kong at Chunky location can be freed.';return A.Slam and A.IsKong(A.settings.chunky_freeing_kong)
	def UpdateCurrentRegionAccess(A,region):'Set access of current region.';B=region;A.donkeyAccess=B.donkeyAccess;A.diddyAccess=B.diddyAccess;A.lankyAccess=B.lankyAccess;A.tinyAccess=B.tinyAccess;A.chunkyAccess=B.chunkyAccess
	def LevelEntered(A,level):
		'Check whether a level, or any level above it, has been entered.';B=level
		if Events.CastleEntered in A.Events:return _B
		elif Events.CavesEntered in A.Events and B<=Levels.CrystalCaves:return _B
		elif Events.ForestEntered in A.Events and B<=Levels.FungiForest:return _B
		elif Events.GalleonEntered in A.Events and B<=Levels.GloomyGalleon:return _B
		elif Events.FactoryEntered in A.Events and B<=Levels.FranticFactory:return _B
		elif Events.AztecEntered in A.Events and B<=Levels.AngryAztec:return _B
		elif Events.JapesEntered in A.Events and B<=Levels.JungleJapes:return _B
		return _A
	def AddCollectible(B,collectible,level):
		'Add a collectible.';C=level;A=collectible
		if A.enabled:
			if A.type==Collectibles.coin:
				if A.kong==Kongs.any:
					for D in range(5):B.Coins[D]+=A.amount*5
				else:B.Coins[A.kong]+=A.amount
			elif A.type==Collectibles.banana:B.ColoredBananas[C][A.kong]+=A.amount
			elif A.type==Collectibles.bunch:B.ColoredBananas[C][A.kong]+=A.amount*5
			elif A.type==Collectibles.balloon:B.ColoredBananas[C][A.kong]+=A.amount*10
			A.added=_B
	def PurchaseShopItem(A,location):
		'Purchase items from shops and subtract price from logical coin counts.';B=location
		if B.item is not _C and B.item is not Items.NoItem:
			C=GetPriceOfMoveItem(B.item,A.settings,A.Slam,A.AmmoBelts,A.InstUpgrades)
			if B.kong==Kongs.any:
				for D in range(0,5):A.Coins[D]-=C
			else:A.Coins[B.kong]-=C
	@staticmethod
	def HasAccess(region,kong):"Check if a certain kong has access to a certain region.\n\n        Usually the region's own HasAccess function is used, but this is necessary for checking access for other regions in logic files.\n        ";return Regions[region].HasAccess(kong)
	@staticmethod
	def TimeAccess(region,time):
		'Check if a certain region has the given time of day access.';A=region
		if time==Time.Day:return Regions[A].dayAccess
		elif time==Time.Night:return Regions[A].nightAccess
		else:return Regions[A].dayAccess or Regions[A].nightAccess
	def KasplatAccess(A,location):'Use the kasplat map to check kasplat logic for blueprint locations.';B=A.kasplat_map[location];return A.IsKong(B)
	def CanBuy(A,location):'Check if there are enough coins to purchase this location.';return CanBuy(location,A)
	def CanAccessKRool(A):'Make sure that each required key has been turned in.';return all((not B not in A.Events for B in A.settings.krool_keys_required))
	def IsBossReachable(A,level):'Check if the boss banana requirement is met.';B=level;return A.HasEnoughKongs(B)and sum(A.ColoredBananas[B])>=A.settings.BossBananas[B]
	def HasEnoughKongs(B,level,forPreviousLevel=_A):
		'Check if kongs are required for progression, do we have enough to reach the given level.';C=level
		if B.settings.kongs_for_progression and C!=Levels.HideoutHelm:
			A=GetShuffledLevelIndex(C)
			if forPreviousLevel:A=A-1
			if A<5:return len(B.GetKongs())>A
			else:return len(B.GetKongs())==5
		else:return _B
	def IsBossBeatable(A,level):
		'Return true if the boss for a given level is beatable according to boss location rando and boss kong rando.';C=level;D=A.settings.boss_kongs[C];E=A.settings.boss_maps[C];B=_B
		if E==Maps.FactoryBoss and D==Kongs.tiny:B=A.twirl
		elif E==Maps.FungiBoss:B=A.hunkyChunky
		return A.IsKong(D)and B
	def IsLevelEnterable(A,level):'Check if level entry requirement is met.';B=level;return A.HasEnoughKongs(B,forPreviousLevel=_B)and A.GoldenBananas>=A.settings.EntryGBs[B]
LogicVariables=LogicVarHolder()
Regions={}
Regions.update(randomizer.LogicFiles.DKIsles.LogicRegions)
Regions.update(randomizer.LogicFiles.JungleJapes.LogicRegions)
Regions.update(randomizer.LogicFiles.AngryAztec.LogicRegions)
Regions.update(randomizer.LogicFiles.FranticFactory.LogicRegions)
Regions.update(randomizer.LogicFiles.GloomyGalleon.LogicRegions)
Regions.update(randomizer.LogicFiles.FungiForest.LogicRegions)
Regions.update(randomizer.LogicFiles.CrystalCaves.LogicRegions)
Regions.update(randomizer.LogicFiles.CreepyCastle.LogicRegions)
Regions.update(randomizer.LogicFiles.HideoutHelm.LogicRegions)
Regions.update(randomizer.LogicFiles.Shops.LogicRegions)
CollectibleRegions={}
CollectibleRegions.update(randomizer.CollectibleLogicFiles.DKIsles.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.JungleJapes.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.AngryAztec.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.FranticFactory.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.GloomyGalleon.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.FungiForest.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.CrystalCaves.LogicRegions)
CollectibleRegions.update(randomizer.CollectibleLogicFiles.CreepyCastle.LogicRegions)
def ResetRegionAccess():
	'Reset kong access for all regions.'
	for A in Regions.values():A.ResetAccess()
def ResetCollectibleRegions():
	'Reset if each collectible has been added.'
	for A in CollectibleRegions.values():
		for B in A:B.added=_A
def ClearAllLocations():
	'Clear item from every location.'
	for A in LocationList.values():A.item=_C