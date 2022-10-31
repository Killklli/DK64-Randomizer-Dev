'Module used to distribute items randomly.'
_L='Retrying fill. Tries: '
_K='Fill failed, out of retries.'
_J='normal'
_I='levels'
_H='shuffled'
_G='off'
_F='random'
_E='assumed'
_D='all'
_C=False
_B=True
_A=None
import json,random,js,randomizer.ItemPool as ItemPool,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic
from randomizer.ShuffleDoors import ShuffleDoors
import randomizer.ShuffleExits as ShuffleExits,randomizer.LogicFiles.DKIsles as IslesLogic
from randomizer.CompileHints import compileHints
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import GetKongs,Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MinigameType import MinigameType
from randomizer.Enums.Regions import Regions
from randomizer.Enums.SearchMode import SearchMode
from randomizer.Enums.Time import Time
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Enums.Warps import Warps
from randomizer.Lists.Item import ItemList,KongFromItem
from randomizer.Lists.Location import LocationList,SharedShopLocations,TrainingBarrelLocations,DonkeyMoveLocations,DiddyMoveLocations,LankyMoveLocations,TinyMoveLocations,ChunkyMoveLocations,SharedMoveLocations
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Lists.ShufflableExit import GetLevelShuffledToIndex,GetShuffledLevelIndex
from randomizer.Lists.Warps import BananaportVanilla
from randomizer.Logic import STARTING_SLAM,LogicVarHolder,LogicVariables
from randomizer.LogicClasses import Sphere,TransitionFront
from randomizer.Prices import GetMaxForKong
from randomizer.Settings import Settings
from randomizer.ShuffleBarrels import BarrelShuffle
from randomizer.ShuffleBosses import ShuffleBossesBasedOnOwnedItems
from randomizer.ShuffleKasplats import InitKasplatMap,KasplatShuffle
from randomizer.ShufflePatches import ShufflePatches
from randomizer.ShuffleShopLocations import ShuffleShopLocations
from randomizer.ShuffleWarps import ShuffleWarps,ShuffleWarpsCrossMap
from randomizer.ShuffleCBs import ShuffleCBs
from randomizer.ShuffleCrowns import ShuffleCrowns
from randomizer.ShuffleItems import ShuffleItems
def GetExitLevelExit(region):
	'Get the exit that using the "Exit Level" button will take you to.';B=region;A=B.level
	if B.restart is not _A:return _A
	if A==Levels.JungleJapes:return ShuffleExits.ShufflableExits[Transitions.JapesToIsles].shuffledId
	elif A==Levels.AngryAztec:return ShuffleExits.ShufflableExits[Transitions.AztecToIsles].shuffledId
	elif A==Levels.FranticFactory:return ShuffleExits.ShufflableExits[Transitions.FactoryToIsles].shuffledId
	elif A==Levels.GloomyGalleon:return ShuffleExits.ShufflableExits[Transitions.GalleonToIsles].shuffledId
	elif A==Levels.FungiForest:return ShuffleExits.ShufflableExits[Transitions.ForestToIsles].shuffledId
	elif A==Levels.CrystalCaves:return ShuffleExits.ShufflableExits[Transitions.CavesToIsles].shuffledId
	elif A==Levels.CreepyCastle:return ShuffleExits.ShufflableExits[Transitions.CastleToIsles].shuffledId
def GetAccessibleLocations(settings,ownedItems,searchType=SearchMode.GetReachable,purchaseList=_A,targetItemId=_A):
	'Search to find all reachable locations given owned items.';b='skip';W=ownedItems;Q=purchaseList;E=settings;D=searchType
	if E.no_logic and D in[SearchMode.CheckAllReachable,SearchMode.CheckBeatable,SearchMode.CheckSpecificItemReachable]:return _B
	if Q is _A:Q=[]
	G=[];J=[];X=[];R=[];K=_B
	while len(J)>0 or K:
		F=Sphere()
		if R:F.availableGBs=R[-1].availableGBs
		for L in J:
			G.append(L);A=LocationList[L]
			if A.item is not _A:
				if A.type==Types.Shop and D==SearchMode.GetReachableWithControlledPurchases and L not in Q:continue
				W.append(A.item);X.append(A.item)
				if D==SearchMode.GeneratePlaythrough and ItemList[A.item].playthrough:
					if E.win_condition=='beat_krool'and A.item==Items.BananaHoard:F.locations=[L];break
					if A.item==Items.GoldenBanana:F.availableGBs+=1
					F.locations.append(L)
				if D==SearchMode.CheckSpecificItemReachable and A.item==targetItemId:return _B
		K=_C;J=[];LogicVariables.Update(W);X=[]
		if len(F.locations)>0:
			if D==SearchMode.GeneratePlaythrough:F.seedBeaten=LogicVariables.WinConditionMet()
			R.append(F)
		if D==SearchMode.CheckBeatable and LogicVariables.WinConditionMet():return _B
		for S in LogicVariables.GetKongs():
			LogicVariables.SetKong(S);T=Logic.Regions[Regions.IslesMain];T.id=Regions.IslesMain;T.dayAccess=_B;T.nightAccess=Events.Night in LogicVariables.Events;M=[T];H=[Regions.IslesMain];Y=[(A,B)for(A,B)in Logic.Regions.items()if B.HasAccess(S)and A not in H];H.extend([A[0]for A in Y]);M.extend([A[1]for A in Y])
			while len(M)>0:
				B=M.pop();B.UpdateAccess(S,LogicVariables);LogicVariables.UpdateCurrentRegionAccess(B)
				for N in B.events:
					if N.name not in LogicVariables.Events and N.logic(LogicVariables):K=_B;LogicVariables.Events.append(N.name)
					if N.name==Events.Night and N.logic(LogicVariables):B.nightAccess=_B
				if B.id in Logic.CollectibleRegions.keys():
					for O in Logic.CollectibleRegions[B.id]:
						if not O.added and O.kong in(S,Kongs.any)and O.logic(LogicVariables)and O.enabled:LogicVariables.AddCollectible(O,B.level)
				for A in B.locations:
					if A.logic(LogicVariables)and A.id not in J and A.id not in G:
						I=LocationList[A.id]
						if A.bonusBarrel is MinigameType.BonusBarrel and E.bonus_barrels!=b or A.bonusBarrel is MinigameType.HelmBarrel and E.helm_barrels!=b:
							c=BarrelMetaData[A.id].minigame
							if not MinigameRequirements[c].logic(LogicVariables):continue
						elif I.item is not _A and ItemList[LocationList[A.id].item].type==Types.Blueprint:
							if not LogicVariables.BlueprintAccess(ItemList[LocationList[A.id].item]):continue
						elif I.type==Types.Blueprint:
							if not LogicVariables.IsKong(I.kong)and not E.free_trade_items:continue
						elif I.type==Types.Shop and I.item is not _A and I.item!=Items.NoItem:
							if D!=SearchMode.GetReachableWithControlledPurchases or A.id in Q:LogicVariables.PurchaseShopItem(A.id)
						elif A.id==Locations.NintendoCoin:LogicVariables.Coins[Kongs.donkey]-=2
						J.append(A.id)
				Z=B.exits.copy()
				if E.shuffle_loading_zones and B.level!=Levels.DKIsles and B.level!=Levels.Shops:
					a=GetExitLevelExit(B)
					if a is not _A:d=ShuffleExits.ShufflableExits[a].back.regionId;Z.append(TransitionFront(d,lambda l:_B))
				for exit in Z:
					C=exit.dest
					if exit.exitShuffleId is not _A and not exit.assumed:
						U=ShuffleExits.ShufflableExits[exit.exitShuffleId]
						if U.shuffled:C=ShuffleExits.ShufflableExits[U.shuffledId].back.regionId
						elif U.toBeShuffled and not exit.assumed:continue
					if C not in H and exit.logic(LogicVariables):
						V=_B
						if exit.time==Time.Night and not B.nightAccess:V=_C
						elif exit.time==Time.Day and not B.dayAccess:V=_C
						if V:H.append(C);P=Logic.Regions[C];P.id=C;M.append(P)
					if exit.logic(LogicVariables):
						if B.dayAccess and exit.time!=Time.Night and not Logic.Regions[C].dayAccess:Logic.Regions[C].dayAccess=_B;K=_B
						if B.nightAccess and exit.time!=Time.Day and not Logic.Regions[C].nightAccess:Logic.Regions[C].nightAccess=_B;K=_B
				if B.deathwarp is not _A:
					C=B.deathwarp.dest
					if C not in H and B.deathwarp.logic(LogicVariables):H.append(C);P=Logic.Regions[C];P.id=C;M.append(P)
	if D in(SearchMode.GetReachable,SearchMode.GetReachableWithControlledPurchases):return G
	elif D==SearchMode.CheckBeatable or D==SearchMode.CheckSpecificItemReachable:E.debug_accessible=G;return _C
	elif D==SearchMode.GeneratePlaythrough:return R
	elif D==SearchMode.CheckAllReachable:return len(G)==len(LocationList)
	elif D==SearchMode.GetUnreachable:return[A for A in LocationList if A not in G]
def VerifyWorld(settings):
	'Make sure all item locations are reachable on current world graph with constant items placed and all other items owned.';A=settings
	if A.no_logic:return _B
	ItemPool.PlaceConstants(A);B=GetAccessibleLocations(A,ItemPool.AllItems(A),SearchMode.GetUnreachable);C=len(B)==0;Reset();return C
def VerifyWorldWithWorstCoinUsage(settings):
	'Make sure the game is beatable without it being possible to run out of coins for required moves.';A=settings
	if A.no_logic:return _B
	C=[];I=[];N=[GetMaxForKong(A,Kongs.donkey),GetMaxForKong(A,Kongs.diddy),GetMaxForKong(A,Kongs.lanky),GetMaxForKong(A,Kongs.tiny),GetMaxForKong(A,Kongs.chunky)]
	while _B:
		Reset();I=GetAccessibleLocations(A,[],SearchMode.GetReachableWithControlledPurchases,C);X=[LocationList[A].item for A in C];O=GetMaxCoinsSpent(A,C);F=[N[A]-O[A]for A in range(0,5)];E=LogicVariables.Coins.copy()
		if E[Kongs.donkey]>=F[Kongs.donkey]and E[Kongs.diddy]>=F[Kongs.diddy]and E[Kongs.lanky]>=F[Kongs.lanky]and E[Kongs.tiny]>=F[Kongs.tiny]and E[Kongs.chunky]>=F[Kongs.chunky]:Reset();return _B
		if LogicVariables.WinConditionMet():Reset();return _B
		K=[A for A in I if LocationList[A].type==Types.Shop and LocationList[A].item is not _A and LocationList[A].item!=Items.NoItem and A not in C and LogicVariables.CanBuy(A)];H={};G={}
		if len(K)==0:print('Seed is invalid, coin locked with purchase order: '+str([LocationList[A].name+': '+LocationList[A].item.name+', 'for A in C]));Reset();return _C
		D=_A
		for B in K:
			L=C.copy();L.append(B);Reset();P=GetAccessibleLocations(A,[],SearchMode.GetReachableWithControlledPurchases,L);Q=LogicVariables.Coins.copy();M=[0,0,0,0,0]
			for J in LogicVariables.GetKongs():M[J]=Q[J]-E[J]
			H[B]=M;G[B]=[LocationList[A].item for A in P if A not in I and LocationList[A].item is not _A]
			if D is _A:D=B;continue
			if len([A for A in H[B]if A<0])==0:continue
			R=len([A for A in G[D]if ItemList[A].type==Types.Kong]);S=len([A for A in G[B]if ItemList[A].type==Types.Kong])
			if S>R:continue
			T=len([A for A in G[D]if ItemList[A].type==Types.Key]);U=len([A for A in G[B]if ItemList[A].type==Types.Key])
			if U>T:continue
			V=sum(list(H[D]));W=sum(list(H[B]))
			if W<V:D=B
		C.append(D)
def Reset():'Reset logic variables and region info that should be reset before a search.';LogicVariables.Reset();Logic.ResetRegionAccess();Logic.ResetCollectibleRegions()
def ParePlaythrough(settings,PlaythroughLocations):
	'Pare playthrough down to only the essential elements.';C=PlaythroughLocations;A=settings;G=[];I=max([A.blocker_0,A.blocker_1,A.blocker_2,A.blocker_3,A.blocker_4,A.blocker_5,A.blocker_6,A.blocker_7])
	for E in range(len(C)-1,-1,-1):
		if E>0 and C[E-1].seedBeaten:C.remove(C[E]);continue
		B=C[E]
		if E>0 and C[E-1].availableGBs>I:B.locations=[A for A in B.locations if LocationList[A].item!=Items.GoldenBanana]
		for F in B.locations.copy():
			D=LocationList[F]
			if D.item==Items.GoldenBanana:continue
			if D.item==Items.BananaFairy:
				if A.win_condition!='all_fairies':B.locations.remove(F)
				continue
			if D.item==Items.BananaMedal:
				if A.win_condition!='all_medals':B.locations.remove(F)
				continue
			if D.item is not _A and ItemList[D.item].type==Types.Blueprint:
				if A.win_condition!='all_blueprints':B.locations.remove(F)
				continue
			H=D.item;D.item=_A;Reset()
			if GetAccessibleLocations(A,[],SearchMode.CheckBeatable):B.locations.remove(F);D.SetDelayedItem(H);G.append(F)
			else:D.PlaceItem(H)
	for E in range(len(C)-1,-1,-1):
		B=C[E]
		if len(B.locations)==0:C.remove(B)
	for F in G:LocationList[F].PlaceDelayedItem()
def PareWoth(settings,PlaythroughLocations):
	'Pare playthrough to locations which are Way of the Hoard (hard required by logic).';A=[]
	for E in PlaythroughLocations:
		for F in [A for A in E.locations if not LocationList[A].constant]:A.append(F)
	A=[B for B in A if ItemList[LocationList[B].item].type not in(Types.Banana,Types.BlueprintBanana,Types.Crown,Types.Medal,Types.Blueprint)]
	for G in range(len(A)-1,-1,-1):
		C=A[G];B=LocationList[C];D=B.item
		if D==Items.ProgressiveSlam:continue
		B.item=_A;Reset()
		if GetAccessibleLocations(settings,[],SearchMode.CheckBeatable):A.remove(C)
		B.PlaceItem(D)
	return A
def RandomFill(settings,itemsToPlace,inOrder=_C):
	'Randomly place given items in any location disregarding logic.';A=itemsToPlace
	if not inOrder:random.shuffle(A)
	B=[]
	for (id,F) in LocationList.items():
		if F.item is _A:B.append(id)
	while len(A)>0:
		D=A.pop();G=settings.GetValidLocationsForItem(D);C=[A for A in B if A in G]
		if len(C)==0:return len(A)
		random.shuffle(C);E=C.pop();LocationList[E].PlaceItem(D);B.remove(E)
	return 0
def ForwardFill(settings,itemsToPlace,ownedItems=_A,inOrder=_C):
	'Forward fill algorithm for item placement.';E=itemsToPlace;C=settings;B=ownedItems
	if B is _A:B=[]
	if not inOrder:random.shuffle(E)
	B=B.copy()
	while len(E)>0:
		A=E.pop(0);Reset();D=GetAccessibleLocations(C,B.copy());G=C.GetValidLocationsForItem(A);D=[A for A in D if LocationList[A].item is _A and A in G]
		if len(D)==0:return len(E)
		random.shuffle(D);F=D.pop();B.append(A);LocationList[F].PlaceItem(A)
		if A in ItemPool.HighPriorityItems(C):C.debug_fill[F]=A
		if A in ItemPool.Keys():C.debug_fill[F]=A
	return 0
def GetItemValidLocations(validLocations,item):
	'Get the list of valid locations for this item.';A=validLocations;B=A
	if isinstance(A,dict):
		for C in A.keys():
			if item==C:B=A[C];break
			B=list(LocationList)
	return B
def AssumedFill(settings,itemsToPlace,ownedItems=_A,inOrder=_C):
	'Assumed fill algorithm for item placement.';T=' in location ';L='Failed placing item ';J=ownedItems;G=itemsToPlace;A=settings
	if J is _A:J=[]
	if not inOrder:random.shuffle(G)
	while len(G)>0:
		B=G.pop(0);M=_C;E=G.copy();E.extend(J);U=A.GetValidLocationsForItem(B);Reset();K=GetAccessibleLocations(A,E);H=[A for A in K if LocationList[A].item is _A and A in U]
		if len(H)==0:
			print(L+ItemList[B].name+', no valid reachable locations without this item.');P=[ItemList[A].name for A in E if ItemList[A].type==Types.Kong];Q=[]
			for V in A.starting_kong_list:Q.append(V.name.capitalize())
			for (D,N) in enumerate(Q):P.insert(D,N)
			W=[ItemList[A].name for A in E if ItemList[A].type==Types.Shop];X=len([A for A in E if ItemList[A].type==Types.Banana]);js.postMessage('Current Moves owned at failure: '+str(W)+' with GB count: '+str(X)+' and kongs freed: '+str(P));return len(G)+1
		random.shuffle(H)
		if ItemList[B].type==Types.Kong:
			I=[KongFromItem(A)for A in E if ItemList[A].type==Types.Kong]
			for (D,N) in enumerate(A.starting_kong_list):I.insert(D,N)
			R=KongFromItem(B)
			if R in I:I.remove(R)
			if A.kongs_for_progression:
				Y=GetShuffledLevelIndex(Levels.JungleJapes);Z=GetShuffledLevelIndex(Levels.AngryAztec);a=GetShuffledLevelIndex(Levels.FranticFactory);F={}
				for D in range(0,7):
					if D==Y:
						if Locations.DiddyKong in A.kong_locations:F[Locations.DiddyKong]=D
						else:F[Locations.DiddyKong]=-1
					elif D==Z:
						if Locations.LankyKong in A.kong_locations:F[Locations.LankyKong]=D
						else:F[Locations.LankyKong]=-1
						if Locations.TinyKong in A.kong_locations:F[Locations.TinyKong]=D
						else:F[Locations.TinyKong]=-1
					elif D==a:
						if Locations.ChunkyKong in A.kong_locations:F[Locations.ChunkyKong]=D
						else:F[Locations.ChunkyKong]=-1
				H.sort(key=lambda x:F[x],reverse=_B)
		for C in H:
			LocationList[C].PlaceItem(B)
			if ItemList[B].type==Types.Kong:
				if C not in A.kong_locations:LocationList[C].PlaceItem(Items.NoItem)
				if C==Locations.DiddyKong:A.diddy_freeing_kong=random.choice(I)
				elif C==Locations.LankyKong:A.lanky_freeing_kong=random.choice(I)
				elif C==Locations.TinyKong:
					S=list(set(I).intersection([Kongs.diddy,Kongs.chunky]))
					if len(S)==0:js.postMessage(L+ItemList[B].name+T+LocationList[C].name+', due to no kongs being able to free them');O=_C;break
					A.tiny_freeing_kong=random.choice(S)
				elif C==Locations.ChunkyKong:A.chunky_freeing_kong=random.choice(I)
			E=G.copy();E.extend(J);Reset();K=GetAccessibleLocations(A,E);O=_B
			for b in G:
				c=A.GetValidLocationsForItem(b);H=[A for A in K if A in c and A!=C]
				if len(H)==0:js.postMessage(L+ItemList[B].name+T+LocationList[C].name+', due to too few remaining locations in play');O=_C;break
				K.remove(H[0])
			if not O:LocationList[C].item=_A;M=_C;continue
			if B in ItemPool.HighPriorityItems(A):A.debug_fill[C]=B
			if B in ItemPool.Keys():A.debug_fill[C]=B
			M=_B;break
		if not M:js.postMessage(L+ItemList[B].name+' in any of remaining '+str(ItemList[B].type)+' type possible locations');return len(G)+1
	return 0
def GetMaxCoinsSpent(settings,purchasedShops):
	'Calculate the max number of coins each kong could have spent given the ownedItems and the price settings.';D=settings;B=[0,0,0,0,0,0];E=0;F=0;G=0
	for H in purchasedShops:
		A=LocationList[H]
		if A.item==Items.ProgressiveSlam:C=D.prices[A.item][E];E+=1
		elif A.item==Items.ProgressiveAmmoBelt:C=D.prices[A.item][F];F+=1
		elif A.item==Items.ProgressiveInstrumentUpgrade:C=D.prices[A.item][G];G+=1
		else:C=D.prices[H]
		if C is not _A:B[A.kong]+=C
	for I in range(5):B[I]+=B[int(Kongs.any)]
	B.pop();return B
def GetItemPrerequisites(spoiler,targetItemId,ownedKongs=[]):
	'Given the target item and the current world state, find a valid, minimal, unplaced set of items required to reach the location it is in.';G=ownedKongs;C=targetItemId;A=spoiler;Reset()
	if GetAccessibleLocations(A.settings,[],SearchMode.CheckSpecificItemReachable,targetItemId=C):return[]
	H=[]
	if Types.Key in A.settings.shuffled_location_types:H=ItemPool.BlueprintAssumedItems().copy()
	B=[]
	if G==[]:G=GetKongs()
	I=[A for A in ItemPool.AllMovesForOwnedKongs(G)if A!=C]
	if Types.Shockwave in A.settings.shuffled_location_types:I.append(Items.Shockwave)
	random.shuffle(I);J=_A
	for K in I:
		B.append(K);Reset()
		if GetAccessibleLocations(A.settings,H.copy()+B.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=C):J=K;break
	if J is _A:
		E=_A;F=ItemList[C]
		if type(A.settings.valid_locations[F.type])is dict:
			for D in A.settings.valid_locations[F.type][F.kong]:
				if LocationList[D].item==C:E=LocationList[D];break
		else:
			for D in A.settings.valid_locations[F.type]:
				if LocationList[D].item==C:E=LocationList[D];break
		if E is _A:raise Ex.ItemPlacementException('Target item not placed??')
		raise Ex.ItemPlacementException('Item placed in an inaccessible location: '+str(E.name))
	while B!=[]and B[0]!=J:
		L=B.pop(0);Reset()
		if not GetAccessibleLocations(A.settings,H.copy()+B.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=C):B.append(L)
	return B
def PlaceItems(settings,algorithm,itemsToPlace,ownedItems=_A,inOrder=_C):
	'Places items using given algorithm.';E=inOrder;D=itemsToPlace;C=ownedItems;B=algorithm;A=settings
	if C is _A:C=[]
	if A.no_logic:B=_F
	if B==_E:return AssumedFill(A,D,C,E)
	elif B=='forward':return ForwardFill(A,D,C,E)
	elif B==_F:return RandomFill(A,D,E)
def Fill(spoiler):
	'Fully randomizes and places all items.';A=spoiler;A.settings.debug_fill={};A.settings.debug_prerequisites={};A.settings.debug_fill_blueprints={};ItemPool.PlaceConstants(A.settings);FillKongsAndMoves(A)
	if Types.Blueprint in A.settings.shuffled_location_types:
		Reset();C=PlaceItems(A.settings,_F,ItemPool.Blueprints(A.settings).copy(),ItemPool.BlueprintAssumedItems())
		if C>0:raise Ex.ItemPlacementException(str(C)+' unplaced blueprints.')
	if Types.Key in A.settings.shuffled_location_types:
		Reset();D=PlaceItems(A.settings,A.settings.algorithm,ItemPool.Keys().copy(),ItemPool.KeyAssumedItems(),inOrder=_B)
		if D>0:raise Ex.ItemPlacementException(str(D)+' unplaced keys.')
	if Types.Coin in A.settings.shuffled_location_types:
		Reset();E=PlaceItems(A.settings,A.settings.algorithm,ItemPool.CompanyCoinItems(),ItemPool.CoinAssumedItems())
		if E>0:raise Ex.ItemPlacementException(str(E)+' unplaced company coins.')
	if Types.Crown in A.settings.shuffled_location_types:
		Reset();B=_F
		if not A.settings.crown_door_open:B=A.settings.algorithm
		F=PlaceItems(A.settings,B,ItemPool.BattleCrownItems(),ItemPool.CrownAssumedItems())
		if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced crowns.')
	if Types.Medal in A.settings.shuffled_location_types:
		Reset();B=_F
		if Types.Coin in A.settings.shuffled_location_types or A.settings.medal_requirement>39:B=A.settings.algorithm
		G=PlaceItems(A.settings,B,ItemPool.BananaMedalItems(),ItemPool.MedalAssumedItems())
		if G>0:raise Ex.ItemPlacementException(str(G)+' unplaced medals.')
	if Types.Banana in A.settings.shuffled_location_types:
		Reset();H=PlaceItems(A.settings,_F,ItemPool.GoldenBananaItems(),[])
		if H>0:raise Ex.ItemPlacementException(str(H)+' unplaced GBs.')
	Reset()
	if not GetAccessibleLocations(A.settings,[],SearchMode.CheckAllReachable):raise Ex.GameNotBeatableException('Game not able to complete 101% after placing all items.')
	return
def ShuffleSharedMoves(spoiler,placedMoves):
	'Shuffles shared kong moves into shops and then returns the remaining ones and their valid locations.';B=placedMoves;A=spoiler;ItemPool.PlaceConstants(A.settings);F=[A for A in SharedMoveLocations if LocationList[A].item is _A];G=[A for A in B if A in ItemPool.ImportantSharedMoves or A in ItemPool.JunkSharedMoves]
	if len(F)<len(ItemPool.ImportantSharedMoves)+len(ItemPool.JunkSharedMoves)-len(G):raise Ex.ItemPlacementException('Too many kong moves placed before shared moves. Only '+len(F)+' available for '+len(ItemPool.ImportantSharedMoves)+len(ItemPool.JunkSharedMoves)-len(G)+' remaining shared moves.')
	if A.settings.training_barrels!=_J and Items.Oranges not in B:
		J=PlaceItems(A.settings,_E,[Items.Oranges],[B for B in ItemPool.AllItems(A.settings)if B!=Items.Oranges])
		if J>0:raise Ex.ItemPlacementException('Failed to place Orange training barrel move.')
	C=ItemPool.ImportantSharedMoves.copy()
	if A.settings.shockwave_status==_H and Items.CameraAndShockwave not in B:C.append(Items.CameraAndShockwave)
	elif A.settings.shockwave_status=='shuffled_decoupled'and(Items.Camera not in B or Items.Shockwave not in B):C.append(Items.Camera);C.append(Items.Shockwave)
	for D in B:
		if D in C:C.remove(D)
	H=PlaceItems(A.settings,_E,C,[B for B in ItemPool.AllItems(A.settings)if B not in C])
	if H>0:raise Ex.ItemPlacementException(str(H)+' unplaced shared important items.')
	E=ItemPool.JunkSharedMoves.copy()
	for D in B:
		if D in E:E.remove(D)
	I=PlaceItems(A.settings,_F,E,[B for B in ItemPool.AllItems(A.settings)if B not in E])
	if I>0:raise Ex.ItemPlacementException(str(I)+' unplaced shared junk items.')
def FillKongsAndMovesGeneric(spoiler):
	'Facilitate shuffling individual pools of items in lieu of full item rando.';B=spoiler;A=0
	while _B:
		try:
			Fill(B);Reset()
			if not VerifyWorldWithWorstCoinUsage(B.settings):raise Ex.GameNotBeatableException('Game unbeatable after placing all items.')
			return
		except Ex.FillException as C:
			if A==20:js.postMessage(_K);raise C
			A+=1
			if A%5==0:B.settings.shuffle_prices()
			js.postMessage(_L+str(A));Reset();Logic.ClearAllLocations()
def GeneratePlaythrough(spoiler):
	'Generate playthrough and way of the hoard and update spoiler.';A=spoiler;js.postMessage('Seed generated! Finalizing spoiler...');Reset();B=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,B);C=PareWoth(A.settings,B);A.UpdateLocations(LocationList)
	if any(A.settings.shuffled_location_types):ShuffleItems(A)
	A.UpdatePlaythrough(LocationList,B);A.UpdateWoth(LocationList,C)
def GetLogicallyAccessibleKongLocations(spoiler,kongLocations,ownedKongs,latestLevel):
	'Find the logically accessible Kong Locations given the current state of Kong unlocking.';D=kongLocations;B=spoiler;A=ownedKongs;C=[]
	for E in range(1,latestLevel+1):
		if B.settings.level_order[E]==Levels.JungleJapes and Locations.DiddyKong in D:C.append(Locations.DiddyKong)
		if B.settings.level_order[E]==Levels.FranticFactory and Locations.ChunkyKong in D:C.append(Locations.ChunkyKong)
		if B.settings.level_order[E]==Levels.AngryAztec and Locations.TinyKong in D and(Kongs.diddy in A or Kongs.chunky in A):C.append(Locations.TinyKong)
		if B.settings.level_order[E]==Levels.AngryAztec and Locations.LankyKong in D and(Kongs.diddy in A or B.settings.open_levels or Kongs.donkey in A and B.settings.activate_all_bananaports==_D)and(Kongs.donkey in A or Kongs.lanky in A or Kongs.tiny in A):C.append(Locations.LankyKong)
	return C
def PlaceKongsInKongLocations(spoiler,kongItems,kongLocations):
	'For these settings, Kongs to place, and locations to place them in, place the Kongs in such a way the generation will never error here.';N=' SEND THIS TO THE DEVS!';E=kongLocations;D=kongItems;A=spoiler;B=[B for B in A.settings.starting_kong_list]
	if A.settings.shuffle_loading_zones==_D or A.settings.no_logic:
		random.shuffle(D)
		if Locations.ChunkyKong in E:C=D.pop();LocationList[Locations.ChunkyKong].PlaceItem(C);A.settings.chunky_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.DiddyKong in E:C=D.pop();LocationList[Locations.DiddyKong].PlaceItem(C);A.settings.diddy_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.LankyKong in E:C=D.pop();LocationList[Locations.LankyKong].PlaceItem(C);A.settings.lanky_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.TinyKong in E:C=D.pop();LocationList[Locations.TinyKong].PlaceItem(C);J=list(set(B).intersection([Kongs.diddy,Kongs.chunky]));A.settings.tiny_freeing_kong=random.choice(J);B.append(ItemPool.GetKongForItem(C))
	elif A.settings.shuffle_loading_zones in(_I,'none'):
		H=len(B)+1
		if A.settings.hard_level_progression:H=7
		F=GetLogicallyAccessibleKongLocations(A,E,B,H)
		while len(B)!=5:
			if not any(F):raise Ex.EntrancePlacementException('Levels shuffled in a way that makes Kong unlocks impossible. SEND THIS TO THE DEVS! '+json.dumps(A.settings.__dict__)+N)
			G=random.choice(F);F.remove(G)
			if G==Locations.DiddyKong:A.settings.diddy_freeing_kong=random.choice(B)
			elif G==Locations.LankyKong:A.settings.lanky_freeing_kong=random.choice(B)
			elif G==Locations.TinyKong:J=list(set(B).intersection([Kongs.diddy,Kongs.chunky]));A.settings.tiny_freeing_kong=random.choice(J)
			elif G==Locations.ChunkyKong:A.settings.chunky_freeing_kong=random.choice(B)
			E.remove(G);I=random.choice(D)
			if not A.settings.hard_level_progression:H+=1
			if len(F)==0 and len(D)>1:
				F=GetLogicallyAccessibleKongLocations(A,E,B,H)
				if not any(F):
					K=[]
					for L in D:
						M=[A for A in B];M.append(ItemPool.GetKongForItem(L));O=GetLogicallyAccessibleKongLocations(A,E,M,H)
						if any(O):K.append(L)
					if len(K)==0:raise Ex.FillException('Kongs placed in a way that is impossible to unlock everyone. SEND THIS TO THE DEVS! '+json.dumps(A.settings.__dict__)+N)
					I=random.choice(K)
			LocationList[G].PlaceItem(I);D.remove(I);B.append(ItemPool.GetKongForItem(I));F=GetLogicallyAccessibleKongLocations(A,E,B,H)
	if A.settings.diddy_freeing_kong==Kongs.any:A.settings.diddy_freeing_kong=random.choice(GetKongs())
	if A.settings.lanky_freeing_kong==Kongs.any:A.settings.lanky_freeing_kong=random.choice(GetKongs())
	if A.settings.tiny_freeing_kong==Kongs.any:A.settings.tiny_freeing_kong=random.choice([Kongs.diddy,Kongs.chunky])
	if A.settings.chunky_freeing_kong==Kongs.any:A.settings.chunky_freeing_kong=random.choice(GetKongs())
	LocationList[Locations.JapesDonkeyFrontofCage].kong=A.settings.diddy_freeing_kong;LocationList[Locations.JapesDonkeyFreeDiddy].kong=A.settings.diddy_freeing_kong;LocationList[Locations.AztecDonkeyFreeLanky].kong=A.settings.lanky_freeing_kong;LocationList[Locations.AztecDiddyFreeTiny].kong=A.settings.tiny_freeing_kong;LocationList[Locations.FactoryLankyFreeChunky].kong=A.settings.chunky_freeing_kong;A.settings.update_valid_locations()
def FillKongs(spoiler):
	'Place Kongs in valid locations.';A=spoiler;C=[ItemPool.ItemFromKong(B)for B in A.settings.starting_kong_list];B=[B for B in ItemPool.Kongs(A.settings)if B not in C]
	if any(A.settings.kong_locations):
		D=[B for B in[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]if B not in A.settings.kong_locations]
		for E in D:LocationList[E].PlaceItem(Items.NoItem)
	Reset();PlaceKongsInKongLocations(A,B,A.settings.kong_locations.copy())
def FillKongsAndMoves(spoiler):
	'Fill kongs, then progression moves, then shared moves, then rest of moves.';A=spoiler;I=[];J=[]
	if A.settings.kong_rando:FillKongs(A)
	if not A.settings.unlock_all_moves and A.settings.move_rando!=_G and A.settings.training_barrels==_H:
		if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression:f=2;BlockAccessToLevel(A.settings,f)
		Reset();V=ItemPool.AllKongMoves().copy();V.append(Items.Vines);g=PlaceItems(A.settings,_E,[Items.Barrels],ownedItems=V)
		if g>0:raise Ex.ItemPlacementException('Failed to place barrel training somehow.')
		if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression:
			R=2
			for W in range(1,8):
				if A.settings.level_order[W]==Levels.AngryAztec:R=W;break
			if A.settings.activate_all_bananaports==_G:R=min(2,R)
			BlockAccessToLevel(A.settings,R)
		Reset();X=ItemPool.AllKongMoves().copy();X.append(Items.Swim);h=PlaceItems(A.settings,_E,[Items.Vines],ownedItems=X)
		if h>0:raise Ex.ItemPlacementException('Failed to place vine training somehow.')
		if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression:i=4;BlockAccessToLevel(A.settings,i)
		Reset();j=PlaceItems(A.settings,_E,[Items.Swim],ownedItems=ItemPool.AllKongMoves().copy())
		if j>0:raise Ex.ItemPlacementException('Failed to place swimming training somehow.')
		if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression and LocationList[Locations.CameraAndShockwave].item in(Items.Vines,Items.Swim):
			BlockAccessToLevel(A.settings,100);Y=ItemPool.AllKongMoves().copy();Y.remove(Items.MiniMonkey);k=PlaceItems(A.settings,_E,[Items.MiniMonkey],ownedItems=Y)
			if k>0:raise Ex.ItemPlacementException('Failed to place Mini Monkey as a dependency for a training move somehow.')
		l=[]
		for Z in SharedMoveLocations:
			if LocationList[Z].item is not _A:l.append(Z)
	if A.settings.kong_rando:
		if A.settings.kongs_for_progression and A.settings.shuffle_loading_zones!=_D and A.settings.move_rando!='start_with':
			r={};K=A.settings.kong_locations.copy();C=[B for B in A.settings.starting_kong_list];L=A.settings.starting_kongs_count+1
			if A.settings.hard_level_progression:L=100
			E=1;S=_C
			while len(C)!=5:
				L=len(C)+1
				if A.settings.hard_level_progression:L=100
				G=set();M=_A
				if A.settings.level_order[E]==Levels.FranticFactory and Locations.ChunkyKong in K and A.settings.chunky_freeing_kong in C:K.remove(Locations.ChunkyKong);M=ItemPool.GetKongForItem(LocationList[Locations.ChunkyKong].item)
				if A.settings.level_order[E]==Levels.JungleJapes and Locations.DiddyKong in K and A.settings.diddy_freeing_kong in C:
					K.remove(Locations.DiddyKong);M=ItemPool.GetKongForItem(LocationList[Locations.DiddyKong].item);N=GetItemPrerequisites(A,LocationList[Locations.DiddyKong].item,C)
					for F in N:
						if F not in J:G.add(F)
				if A.settings.level_order[E]==Levels.AngryAztec and Locations.TinyKong in K and A.settings.tiny_freeing_kong in C:
					K.remove(Locations.TinyKong);M=ItemPool.GetKongForItem(LocationList[Locations.TinyKong].item);N=GetItemPrerequisites(A,LocationList[Locations.TinyKong].item,C)
					for F in N:
						if F not in J:G.add(F)
				elif A.settings.level_order[E]==Levels.AngryAztec and Locations.LankyKong in K and A.settings.lanky_freeing_kong in C and(Kongs.diddy in C or A.settings.open_levels or Kongs.donkey in C and A.settings.activate_all_bananaports==_D)and(Kongs.donkey in C or Kongs.lanky in C or Kongs.tiny in C):
					K.remove(Locations.LankyKong);M=ItemPool.GetKongForItem(LocationList[Locations.LankyKong].item);N=GetItemPrerequisites(A,LocationList[Locations.LankyKong].item,C)
					for F in N:
						if F not in J:G.add(F)
				while any(G):
					BlockAccessToLevel(A.settings,L);Reset();O=ItemPool.AllMovesForOwnedKongs(C).copy()
					if Types.Key in A.settings.shuffled_location_types:O.extend(ItemPool.BlueprintAssumedItems().copy())
					if Types.Shockwave in A.settings.shuffled_location_types:O.append(Items.Shockwave)
					for P in G:O.remove(P)
					for P in J:O.remove(P)
					T=PlaceItems(A.settings,_E,list(G),ownedItems=O)
					if T>0:raise Ex.ItemPlacementException('Failed to place items that would unlock Kong number '+str(len(C)+1)+', '+M.name)
					J.extend(list(G));a=[]
					for P in G:
						m=GetItemPrerequisites(A,P,C)
						for F in m:
							if F not in J:a.append(F)
					G=set(a)
				if M is not _A:C.append(M);S=_C
				else:
					if E==L and S:raise Ex.ItemPlacementException('Kongs logically locked behind themselves. Only '+str(len(C))+' kongs logically accessible.')
					elif E==L:S=_B
					if A.settings.hard_level_progression:E=E%7+1;S=E==1
					else:E=E%L+1
				BlockAccessToLevel(A.settings,100)
	if not A.settings.unlock_all_moves and A.settings.move_rando!=_G:ShuffleSharedMoves(A,J.copy());I.extend(ItemPool.DonkeyMoves);I.extend(ItemPool.DiddyMoves);I.extend(ItemPool.LankyMoves);I.extend(ItemPool.TinyMoves);I.extend(ItemPool.ChunkyMoves)
	Reset();I=[A for A in I if A not in J];b=[]
	if Types.Key in A.settings.shuffled_location_types:b=ItemPool.BlueprintAssumedItems().copy()
	T=PlaceItems(A.settings,_E,I,b)
	if T>0:
		n={};o=[];p=[]
		for U in LocationList:
			B=LocationList[U]
			if B.item is not _A and B.item!=Items.NoItem and B.item<=Items.CameraAndShockwave:n[U]=B.item
			if B.type==Types.Shop and B.item is _A:
				o.append(B)
				if U in SharedMoveLocations:p.append(B)
		raise Ex.ItemPlacementException(str(T)+' unplaced items.')
	if not A.settings.unlock_all_moves and A.settings.move_rando!=_G:
		if A.settings.training_barrels==_H:
			c=[A for A in TrainingBarrelLocations if LocationList[A].item is _A]
			if len(c)>0:
				H=[]
				for B in DonkeyMoveLocations:
					D=LocationList[B].item
					if D is not _A and D!=Items.NoItem:H.append(B)
				for B in DiddyMoveLocations:
					D=LocationList[B].item
					if D is not _A and D!=Items.NoItem:H.append(B)
				for B in LankyMoveLocations:
					D=LocationList[B].item
					if D is not _A and D!=Items.NoItem:H.append(B)
				for B in TinyMoveLocations:
					D=LocationList[B].item
					if D is not _A and D!=Items.NoItem:H.append(B)
				for B in ChunkyMoveLocations:
					D=LocationList[B].item
					if D is not _A and D!=Items.NoItem:H.append(B)
				if len(H)==0:
					for (q,B) in LocationList.items():
						if B.item in ItemPool.AllKongMoves():H.append(q)
				for d in c:
					Q=random.choice(H);e=LocationList[Q].item;LocationList[d].PlaceItem(e);LocationList[Q].PlaceItem(Items.NoItem);H.remove(Q)
					if Q in A.settings.debug_fill.keys():del A.settings.debug_fill[Q];A.settings.debug_fill[d]=e
def FillKongsAndMovesForLevelOrder(spoiler):
	'Shuffle Kongs and Moves accounting for level order restrictions.';A=spoiler;B=0
	while _B:
		try:
			ItemPool.PlaceConstants(A.settings);WipeProgressionRequirements(A.settings);A.settings.kongs_for_progression=_B;Fill(A)
			if A.settings.hard_level_progression:SetNewProgressionRequirementsUnordered(A.settings)
			else:SetNewProgressionRequirements(A.settings)
			A.settings.kongs_for_progression=_C
			if not VerifyWorldWithWorstCoinUsage(A.settings):raise Ex.GameNotBeatableException('Game potentially unbeatable after placing all items.')
			return
		except Ex.FillException as C:
			Reset();Logic.ClearAllLocations();B+=1
			if B==20:js.postMessage(_K);raise C
			if B%5==0:
				js.postMessage('Retrying fill really hard. Tries: '+str(B));A.settings.shuffle_prices()
				if A.settings.shuffle_loading_zones==_I:ShuffleExits.ShuffleExits(A.settings);A.UpdateExits()
			else:js.postMessage(_L+str(B))
def GetAccessibleKongLocations(levels,ownedKongs):
	'Get all kong locations within the provided levels which are reachable by owned kongs.';A=ownedKongs;B=[]
	for C in levels:
		if C==Levels.JungleJapes:B.append(Locations.DiddyKong)
		elif C==Levels.AngryAztec:
			if Kongs.donkey in A or Kongs.lanky in A or Kongs.tiny in A:B.append(Locations.LankyKong)
			if Kongs.diddy in A:B.append(Locations.TinyKong)
		elif C==Levels.FranticFactory:
			if Kongs.lanky in A or Kongs.tiny in A:B.append(Locations.ChunkyKong)
	return B
def WipeProgressionRequirements(settings):
	'Wipe out progression requirements to assume access through main 7 levels.';A=settings
	for B in range(0,7):A.EntryGBs[B]=0;A.BossBananas[B]=0;A.boss_kongs[B]=A.starting_kong;A.boss_maps[B]=Maps.CastleBoss
	if A.kong_rando:A.diddy_freeing_kong=Kongs.any;A.lanky_freeing_kong=Kongs.any;A.tiny_freeing_kong=Kongs.any;A.chunky_freeing_kong=Kongs.any
def SetNewProgressionRequirements(settings):
	'Set new progression requirements based on what is owned or accessible heading into each level.';A=settings;B=[];C=[];K={};I={}
	if A.unlock_all_moves:G=ItemPool.DonkeyMoves.copy();G.extend(ItemPool.DiddyMoves);G.extend(ItemPool.LankyMoves);G.extend(ItemPool.TinyMoves);G.extend(ItemPool.ChunkyMoves);G.extend(ItemPool.ImportantSharedMoves)
	BlockAccessToLevel(A,0);Reset();L=GetAccessibleLocations(A,[]);C.append(LogicVariables.GoldenBananas)
	for M in range(1,8):
		BlockAccessToLevel(A,M);Reset();L=GetAccessibleLocations(A,[]);J=GetLevelShuffledToIndex(M-1);B.append(LogicVariables.ColoredBananas[J]);C.append(LogicVariables.GoldenBananas);K[J]=LogicVariables.GetKongs()
		if A.unlock_all_moves:I[J]=G
		else:N=[LocationList[A].item for A in L if LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A and ItemList[LocationList[A].item].type in(Types.TrainingBarrel,Types.Shop,Types.Shockwave)];I[J]=N
	D=0.4;E=0.7
	if A.hard_blockers:D=0.6;E=0.95
	F=min(A.blocker_0,1,C[0]);A.EntryGBs=[F,min(A.blocker_1,max(F,round(random.uniform(D,E)*C[1]))),min(A.blocker_2,max(F,round(random.uniform(D,E)*C[2]))),min(A.blocker_3,max(F,round(random.uniform(D,E)*C[3]))),min(A.blocker_4,max(F,round(random.uniform(D,E)*C[4]))),min(A.blocker_5,max(F,round(random.uniform(D,E)*C[5]))),min(A.blocker_6,max(F,round(random.uniform(D,E)*C[6]))),A.blocker_7]
	if A.randomize_blocker_required_amounts:
		for H in range(1,7):
			if A.EntryGBs[H]>A.EntryGBs[H+1]:O=A.EntryGBs[H];A.EntryGBs[H]=A.EntryGBs[H+1];A.EntryGBs[H+1]=O
	A.BossBananas=[min(A.troff_0,sum(B[0]),round(A.troff_0/(A.troff_max*A.troff_weight_0)*sum(B[0]))),min(A.troff_1,sum(B[1]),round(A.troff_1/(A.troff_max*A.troff_weight_1)*sum(B[1]))),min(A.troff_2,sum(B[2]),round(A.troff_2/(A.troff_max*A.troff_weight_2)*sum(B[2]))),min(A.troff_3,sum(B[3]),round(A.troff_3/(A.troff_max*A.troff_weight_3)*sum(B[3]))),min(A.troff_4,sum(B[4]),round(A.troff_4/(A.troff_max*A.troff_weight_4)*sum(B[4]))),min(A.troff_5,sum(B[5]),round(A.troff_5/(A.troff_max*A.troff_weight_5)*sum(B[5]))),min(A.troff_6,sum(B[6]),round(A.troff_6/(A.troff_max*A.troff_weight_6)*sum(B[6])))];ShuffleExits.UpdateLevelProgression(A);ShuffleBossesBasedOnOwnedItems(A,K,I);A.owned_kongs_by_level=K;A.owned_moves_by_level=I
def SetNewProgressionRequirementsUnordered(settings):
	'Set level progression requirements based on a random path of accessible levels.';A=settings;R={};N={};G=ItemPool.DonkeyMoves.copy();G.extend(ItemPool.DiddyMoves);G.extend(ItemPool.LankyMoves);G.extend(ItemPool.TinyMoves);G.extend(ItemPool.ChunkyMoves);G.extend(ItemPool.ImportantSharedMoves);G.extend(ItemPool.TrainingBarrelAbilities());f=[Events.JapesKeyTurnedIn,Events.AztecKeyTurnedIn,Events.FactoryKeyTurnedIn,Events.GalleonKeyTurnedIn,Events.ForestKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn,Events.HelmKeyTurnedIn];BlockAccessToLevel(A,0);Reset();I=GetAccessibleLocations(A,[]);J=LogicVariables.GoldenBananas;K=0;A.EntryGBs=[A.blocker_0,A.blocker_1,A.blocker_2,A.blocker_3,A.blocker_4,A.blocker_5,A.blocker_6,A.blocker_7];A.BossBananas=[A.troff_0,A.troff_1,A.troff_2,A.troff_3,A.troff_4,A.troff_5,A.troff_6];S=[A.troff_0,A.troff_1,A.troff_2,A.troff_3,A.troff_4,A.troff_5,A.troff_6];b=0.4;T=0.7
	if A.hard_blockers:b=0.6;T=0.95
	L=[];B=[1,2,3,4,5,6,7]
	if not A.open_lobbies:
		for H in A.krool_keys_required:
			if H==Events.JapesKeyTurnedIn:B.remove(2)
			elif H==Events.AztecKeyTurnedIn:B.remove(3);B.remove(4)
			elif H==Events.GalleonKeyTurnedIn:B.remove(5)
			elif H==Events.ForestKeyTurnedIn:B.remove(6);B.remove(7)
	O=_C
	if 6 in B and Kongs.donkey not in A.starting_kong_list and Kongs.chunky not in A.starting_kong_list:B.remove(6);O=_B
	M=_C;P=_C;U=_C
	if A.training_barrels!=_J:
		c=[LocationList[A].item for A in TrainingBarrelLocations]
		if A.activate_all_bananaports==_G and Items.Vines not in c:
			if 2 in B:B.remove(2);P=_B
			if 6 in B:B.remove(6);M=_B
		if 4 in B and Items.Swim not in c:B.remove(4);U=_B
	E=[A.level_order[C]for C in B];V=[]
	while len(L)<7:
		W=[B for B in E if B not in L and A.EntryGBs[B]<=round(J*T)]
		if len(W)==0:
			X=[A for A in E if A not in L]
			if Levels.AngryAztec in X:
				if Items.Vines not in[LocationList[A].item for A in I]:X.remove(Levels.AngryAztec)
			if len(X)==0:raise Ex.FillException('Hard level order shuffler failed to progress through levels.')
			C=random.choice(X)
			if A.randomize_blocker_required_amounts:
				Y=C
				for F in range(0,len(A.EntryGBs)):
					if F not in L and A.EntryGBs[F]<A.EntryGBs[Y]:Y=F
				g=A.EntryGBs[Y];A.EntryGBs[Y]=A.EntryGBs[C];A.EntryGBs[C]=g
			if A.EntryGBs[C]>round(J*T):A.EntryGBs[C]=random.randint(max(K,round(J*b)),round(J*T))
			W=[C]
		else:
			C=random.choice(W)
			if A.randomize_blocker_required_amounts and J>A.blocker_max and A.EntryGBs[C]<K:A.EntryGBs[C]=random.randint(K,A.blocker_max)
		K=A.EntryGBs[C];L.append(C)
		if not A.open_lobbies:
			d=-1
			for H in A.level_order.keys():
				if A.level_order[H]==C:d=H-1;break
			Z=f[d]
			if Z in A.krool_keys_required and Z not in[Events.FactoryKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn]:V.append(Z)
		BlockCompletionOfLevelSet(A,W);Reset();I=GetAccessibleLocations(A,[]);J=LogicVariables.GoldenBananas
		if len(E)==len(L)and any(V):
			Q=random.choice(V);V.remove(Q)
			if Q==Events.JapesKeyTurnedIn:P=_B;D=A.level_order[1]
			elif Q==Events.AztecKeyTurnedIn:E.append(A.level_order[3]);U=_B;D=A.level_order[2]
			elif Q==Events.GalleonKeyTurnedIn:E.append(A.level_order[5]);D=A.level_order[4]
			elif Q==Events.ForestKeyTurnedIn:O=_B;M=_B;E.append(A.level_order[7]);D=A.level_order[5]
			e=sum(LogicVariables.ColoredBananas[D])
			if e<S[D]:h=S[D]/A.troff_max;A.BossBananas[D]=round(e*h)
			else:A.BossBananas[D]=S[D]
			R[D]=LogicVariables.GetKongs()
			if A.unlock_all_moves:N[D]=G
			else:i=[LocationList[A].item for A in I if LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A and ItemList[LocationList[A].item].type in(Types.TrainingBarrel,Types.Shop,Types.Shockwave)];N[D]=i
		if O:
			a=LogicVariables.GetKongs()
			if Kongs.donkey in a or Kongs.chunky in a or Kongs.tiny in a and Items.PonyTailTwirl in[LocationList[A].item for A in I]:
				O=_C
				if not M:E.append(A.level_order[6])
		if P or M:
			if A.activate_all_bananaports!=_G or Items.Vines in[LocationList[A].item for A in I]:
				if P:P=_C;E.append(A.level_order[2])
				if M:
					M=_C
					if not O:E.append(A.level_order[6])
		if U:
			if Items.Swim in[LocationList[A].item for A in I]:U=_C;E.append(A.level_order[4])
	for F in range(len(A.BossBananas)):
		if A.BossBananas[F]>500:R[Levels(F)]=LogicVariables.GetKongs();N[Levels(F)]=G;A.BossBananas[F]=S[F]
	if A.randomize_blocker_required_amounts and not A.maximize_helm_blocker and A.EntryGBs[7]<K:A.EntryGBs[7]=random.randint(K,A.blocker_max)
	ShuffleBossesBasedOnOwnedItems(A,R,N);A.owned_kongs_by_level=R;A.owned_moves_by_level=N
def BlockAccessToLevel(settings,level):
	'Assume the level index passed in is the furthest level you have access to in the level order.';B=settings
	for A in range(0,8):
		if A>=level:
			B.EntryGBs[A]=1000
			if A<7:B.BossBananas[A]=1000
		else:
			B.EntryGBs[A]=0
			if A<7:B.BossBananas[A]=0
	ShuffleExits.UpdateLevelProgression(B)
def BlockCompletionOfLevelSet(settings,lockedLevels):
	'Prevent acquiring the keys of the levels provided.'
	for A in range(0,7):
		if A in lockedLevels:settings.BossBananas[A]=1000
def Generate_Spoiler(spoiler):
	'Generate a complete spoiler based on input settings.';A=spoiler;global LogicVariables;LogicVariables=LogicVarHolder(A.settings);InitKasplatMap(LogicVariables)
	if A.settings.kongs_for_progression:
		if A.settings.shuffle_loading_zones==_I:ShuffleExits.ShuffleExits(A.settings);A.UpdateExits()
		WipeProgressionRequirements(A.settings);ShuffleMisc(A);FillKongsAndMovesForLevelOrder(A)
	else:
		ShuffleMisc(A)
		if A.settings.shuffle_loading_zones!='none':ShuffleExits.ExitShuffle(A.settings);A.UpdateExits()
		if A.settings.move_rando!=_G and not A.settings.unlock_all_moves or A.settings.kong_rando or any(A.settings.shuffled_location_types):FillKongsAndMovesGeneric(A)
		else:
			ItemPool.PlaceConstants(A.settings)
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.VanillaItemsGameNotBeatableException('Game unbeatable.')
	GeneratePlaythrough(A)
	if A.settings.wrinkly_hints in['standard','cryptic']:compileHints(A)
	Reset();ShuffleExits.Reset();A.createJson();js.postMessage('Patching ROM...');return A
def ShuffleMisc(spoiler):
	'Shuffle miscellaneous objects outside of main fill algorithm, including Kasplats, Bonus barrels, and bananaport warps.';N='isles';M='crossmap_coupled';L='in_level';A=spoiler
	if A.settings.wrinkly_location_rando or A.settings.tns_location_rando:ShuffleDoors(A)
	if A.settings.crown_placement_rando:H={};I={};ShuffleCrowns(H,I);A.crown_locations=H;A.human_crowns=I
	KasplatShuffle(A,LogicVariables);A.human_kasplats={};A.UpdateKasplats(LogicVariables.kasplat_map)
	if A.settings.bonus_barrels in(_F,'selected'):BarrelShuffle(A.settings);A.UpdateBarrels()
	if A.settings.cb_rando:ShuffleCBs(A)
	if A.settings.bananaport_rando==L:B=[];C={};ShuffleWarps(B,C);A.bananaport_replacements=B.copy();A.human_warp_locations=C
	elif A.settings.bananaport_rando in(M,'crossmap_decoupled'):B=[];C={};ShuffleWarpsCrossMap(B,C,A.settings.bananaport_rando==M);A.bananaport_replacements=B.copy();A.human_warp_locations=C
	if A.settings.random_patches:O=[];A.human_patches=ShufflePatches(A,O).copy()
	if A.settings.shuffle_shops:ShuffleShopLocations(A)
	A.human_item_assignment={}
	if A.settings.activate_all_bananaports in[_D,N]:
		if A.settings.bananaport_rando in(L,_G):
			P=set([BananaportVanilla[A].map_id for A in Warps])
			for J in P:
				Q=[BananaportVanilla[A]for A in Warps if BananaportVanilla[A].map_id==J]
				for D in Q:
					K=[BananaportVanilla[A]for A in Warps if BananaportVanilla[A].map_id==J and BananaportVanilla[A].new_warp==D.new_warp and BananaportVanilla[A].name!=D.name][0]
					if D.region_id!=K.region_id and(A.settings.activate_all_bananaports==_D or D.map_id==Maps.Isles):F=Logic.Regions[D.region_id];G=TransitionFront(K.region_id,lambda l:_B);F.exits.append(G)
		else:
			for E in BananaportVanilla.values():
				F=Logic.Regions[E.region_id]
				if A.settings.activate_all_bananaports!=N or E.region_id in IslesLogic.LogicRegions.keys()and E.destination_region_id in IslesLogic.LogicRegions.keys():G=TransitionFront(E.destination_region_id,lambda l:_B);F.exits.append(G)
	A.settings.update_valid_locations()