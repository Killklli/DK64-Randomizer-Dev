'Module used to distribute items randomly.'
_R='Retrying fill. Tries: '
_Q='Retrying fill really hard. Tries: '
_P='Fill failed, out of retries.'
_O='Game potentially unbeatable after placing all items.'
_N='shuffled_decoupled'
_M='all_blueprints'
_L='all_medals'
_K='levels'
_J='vanilla'
_I='shuffled'
_H='assumed'
_G='normal'
_F='off'
_E='random'
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
from randomizer.Lists.Location import LocationList,TrainingBarrelLocations,DonkeyMoveLocations,DiddyMoveLocations,LankyMoveLocations,TinyMoveLocations,ChunkyMoveLocations,SharedMoveLocations
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Lists.ShufflableExit import GetLevelShuffledToIndex,GetShuffledLevelIndex
from randomizer.Lists.Warps import BananaportVanilla
from randomizer.Logic import LogicVarHolder,LogicVariables
from randomizer.Logic import Regions as RegionList
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
def GetAccessibleLocations(settings,startingOwnedItems,searchType=SearchMode.GetReachable,purchaseList=_A,targetItemId=_A):
	'Search to find all reachable locations given owned items.';b='skip';Q=purchaseList;F=settings;D=searchType
	if F.no_logic and D in[SearchMode.CheckAllReachable,SearchMode.CheckBeatable,SearchMode.CheckSpecificItemReachable]:return _B
	if Q is _A:Q=[]
	G=[];J=[];W=startingOwnedItems.copy();X=[];R=[];K=_B
	while len(J)>0 or K:
		E=Sphere()
		if R:E.availableGBs=R[-1].availableGBs
		for L in J:
			G.append(L);A=LocationList[L]
			if A.item is not _A:
				if A.type==Types.Shop and D==SearchMode.GetReachableWithControlledPurchases and L not in Q:continue
				W.append(A.item);X.append(A.item)
				if D==SearchMode.GeneratePlaythrough and ItemList[A.item].playthrough:
					if A.item==Items.BananaHoard:E.locations=[L];break
					if A.item==Items.GoldenBanana:E.availableGBs+=1
					E.locations.append(L)
				if D==SearchMode.CheckSpecificItemReachable and A.item==targetItemId:return _B
		K=_C;J=[];LogicVariables.Update(W);X=[]
		if len(E.locations)>0:
			if D==SearchMode.GeneratePlaythrough:E.seedBeaten=LogicVariables.bananaHoard
			R.append(E)
		if D==SearchMode.CheckBeatable and LogicVariables.bananaHoard:return _B
		for S in LogicVariables.GetKongs():
			LogicVariables.SetKong(S);T=Logic.Regions[Regions.GameStart];T.id=Regions.GameStart;T.dayAccess=_B;T.nightAccess=Events.Night in LogicVariables.Events;M=[T];H=[Regions.GameStart];Y=[(A,B)for(A,B)in Logic.Regions.items()if B.HasAccess(S)and A not in H];H.extend([A[0]for A in Y]);M.extend([A[1]for A in Y])
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
						if A.bonusBarrel is MinigameType.BonusBarrel and F.bonus_barrels!=b or A.bonusBarrel is MinigameType.HelmBarrel and F.helm_barrels!=b:
							c=BarrelMetaData[A.id].minigame
							if not MinigameRequirements[c].logic(LogicVariables):continue
						elif I.item is not _A and ItemList[LocationList[A.id].item].type==Types.Blueprint:
							if not LogicVariables.BlueprintAccess(ItemList[LocationList[A.id].item]):continue
						elif I.type==Types.Blueprint:
							if not LogicVariables.IsKong(I.kong)and not F.free_trade_items:continue
						elif I.type==Types.Shop and I.item is not _A and I.item!=Items.NoItem:
							if D!=SearchMode.GetReachableWithControlledPurchases or A.id in Q:LogicVariables.PurchaseShopItem(A.id)
						elif A.id==Locations.NintendoCoin:LogicVariables.Coins[Kongs.donkey]-=2
						J.append(A.id)
				Z=B.exits.copy()
				if F.shuffle_loading_zones and B.level!=Levels.DKIsles and B.level!=Levels.Shops:
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
	elif D==SearchMode.CheckBeatable or D==SearchMode.CheckSpecificItemReachable:F.debug_accessible=G;return _C
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
		if LogicVariables.bananaHoard:Reset();return _B
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
				if A.win_condition!=_L:B.locations.remove(F)
				continue
			if D.item is not _A and ItemList[D.item].type==Types.Blueprint:
				if A.win_condition!=_M:B.locations.remove(F)
				continue
			H=D.item;D.item=_A;Reset()
			if GetAccessibleLocations(A,[],SearchMode.CheckBeatable):B.locations.remove(F);D.SetDelayedItem(H);G.append(F)
			else:D.PlaceItem(H)
	for E in range(len(C)-1,-1,-1):
		B=C[E]
		if len(B.locations)==0:C.remove(B)
	for F in G:LocationList[F].PlaceDelayedItem()
def PareWoth(spoiler,PlaythroughLocations):
	'Pare playthrough to locations which are Way of the Hoard (hard required by logic).';B=spoiler;A=[]
	for E in PlaythroughLocations:
		for F in [A for A in E.locations if not LocationList[A].constant and ItemList[LocationList[A].item].type not in(Types.Banana,Types.BlueprintBanana,Types.Crown,Types.Medal,Types.Blueprint)]:A.append(F)
	A.append(Locations.BananaHoard)
	for G in range(len(A)-1,-1,-1):
		D=A[G];C=LocationList[D];H=C.item;C.item=_A;Reset()
		if GetAccessibleLocations(B.settings,[],SearchMode.CheckBeatable):A.remove(D)
		C.PlaceItem(H)
	if B.settings.shuffle_items:CalculateWothPaths(B,A);CalculateFoolish(B,A)
	return A
def CalculateWothPaths(spoiler,WothLocations):
	'Calculate the Paths (dependencies) for each Way of the Hoard item.';C=WothLocations;B=spoiler;G=[]
	for A in C:B.woth_paths[A]=[A]
	for A in C:
		D=LocationList[A];E=D.item;D.item=_A;F=ItemPool.Keys()+ItemPool.Kongs(B.settings);F.extend([Items.Vines,Items.Swim]);Reset();LogicVariables.GainInfiniteCoins();J=GetAccessibleLocations(B.settings,F,SearchMode.GetReachable);H=_C
		for I in C:
			if I not in J:B.woth_paths[I].append(A);H=_B
		D.PlaceItem(E)
		if E not in F and E!=Items.BananaHoard and not H:G.append(A)
	for A in G:C.remove(A);del B.woth_paths[A]
def CalculateFoolish(spoiler,WothLocations):
	'Calculate the items and regions that are foolish (blocking no major items).';G='need_both';A=spoiler;H=[LocationList[A].item for A in WothLocations];C=[];B=ItemPool.AllKongMoves()
	if A.settings.training_barrels!=_G:B.extend([Items.Vines,Items.Swim,Items.Barrels])
	if A.settings.shockwave_status==_I:B.append(Items.CameraAndShockwave)
	if A.settings.shockwave_status==_N:B.append(Items.Camera);B.append(Items.Shockwave)
	for D in B:
		if D in H:continue
		Reset();LogicVariables.BanItem(D);GetAccessibleLocations(A.settings,[],SearchMode.GetReachable)
		if LogicVariables.HasAllItems():C.append(D)
	A.foolish_moves=C;B=[A for A in B if A not in C];B.extend(ItemPool.Keys());B.extend(ItemPool.Kongs(A.settings));B.append(Items.Oranges)
	if Types.Coin in A.settings.shuffled_location_types and A.settings.coin_door_open in[G,'need_rw']:B.append(Items.RarewareCoin)
	if Types.Coin in A.settings.shuffled_location_types and A.settings.coin_door_open in[G,'need_nin']:B.append(Items.NintendoCoin)
	if Types.Blueprint in A.settings.shuffled_location_types and A.settings.win_condition==_M:B.extend(ItemPool.Blueprints(A.settings))
	if Types.Medal in A.settings.shuffled_location_types and A.settings.win_condition==_L:B.append(Items.BananaMedal)
	if Types.Crown in A.settings.shuffled_location_types and not A.settings.crown_door_open:B.append(Items.BattleCrown)
	E={'K. Rool Arena','Snide','Candy Generic','Funky Generic','Credits'}
	if Types.Coin not in A.settings.shuffled_location_types:E.add('Jetpac Game')
	for (id,F) in RegionList.items():
		I=[A for A in F.locations if A.id in LocationList.keys()]
		if any([A for A in I if LocationList[A.id].item in B]):E.add(F.hint_name)
	A.foolish_region_names=list(set([A.hint_name for(id,A)in RegionList.items()if any(A.locations)and A.hint_name not in E]))
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
	'Calculate the max number of coins each kong could have spent given the ownedItems and the price settings.';B=settings;D=[0,0,0,0,0,0];E=0;F=0;G=0
	for H in purchasedShops:
		A=LocationList[H]
		if A.item==Items.ProgressiveSlam:C=B.prices[A.item][E];E+=1
		elif A.item==Items.ProgressiveAmmoBelt:C=B.prices[A.item][F];F+=1
		elif A.item==Items.ProgressiveInstrumentUpgrade:C=B.prices[A.item][G];G+=1
		elif B.random_prices==_J:C=B.prices[A.item]
		else:C=B.prices[H]
		if C is not _A:D[A.kong]+=C
	for I in range(5):D[I]+=D[int(Kongs.any)]
	D.pop();return D
def GetUnplacedItemPrerequisites(spoiler,targetItemId,placedMoves,ownedKongs=[]):
	'Given the target item and the current world state, find a valid, minimal, unplaced set of items required to reach the location it is in.';M='Item placed in an inaccessible location: ';L=ownedKongs;K=placedMoves;C=targetItemId;A=spoiler;E=[]
	if Types.Key in A.settings.shuffled_location_types:E=ItemPool.BlueprintAssumedItems().copy()
	Reset()
	if GetAccessibleLocations(A.settings,E.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=C):return[]
	B=[]
	if L==[]:L=GetKongs()
	D=[A for A in ItemPool.AllMovesForOwnedKongs(L)]
	if A.settings.shockwave_status!=_J:D.append(Items.Shockwave)
	if A.settings.training_barrels!=_G:D.extend(ItemPool.TrainingBarrelAbilities())
	for F in K:D.remove(F)
	if C in D:D.remove(C)
	if Items.ProgressiveSlam in K:
		while Items.ProgressiveSlam in D:D.remove(Items.ProgressiveSlam)
	random.shuffle(D);G=_A
	for F in D:
		B.append(F);Reset()
		if GetAccessibleLocations(A.settings,E.copy()+B.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=C):G=F;break
	if G is _A and K.count(Items.ProgressiveSlam)==1:
		B.append(Items.ProgressiveSlam);Reset()
		if GetAccessibleLocations(A.settings,E.copy()+B.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=C):G=F
	if G is _A:
		H=_A;J=ItemList[C]
		if type(A.settings.valid_locations[J.type])is dict:
			for I in A.settings.valid_locations[J.type][J.kong]:
				if LocationList[I].item==C:H=LocationList[I];break
		else:
			for I in A.settings.valid_locations[J.type]:
				if LocationList[I].item==C:H=LocationList[I];break
		if H is _A:raise Ex.ItemPlacementException('Target item not placed??')
		print(M+str(H.name));raise Ex.ItemPlacementException(M+str(H.name))
	while B!=[]and B[0]!=G:
		N=B.pop(0);Reset()
		if not GetAccessibleLocations(A.settings,E.copy()+B.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=C):B.append(N)
	A.settings.debug_prerequisites[C]=B;return B
def PlaceItems(settings,algorithm,itemsToPlace,ownedItems=_A,inOrder=_C):
	'Places items using given algorithm.';E=inOrder;D=itemsToPlace;C=ownedItems;B=algorithm;A=settings
	if C is _A:C=[]
	if A.no_logic:B=_E
	if B==_H:return AssumedFill(A,D,C,E)
	elif B=='forward':return ForwardFill(A,D,C,E)
	elif B==_E:return RandomFill(A,D,E)
def FillShuffledKeys(spoiler):
	'Fill Keys in shuffled locations based on the settings.';E=' unplaced keys.';A=spoiler;C=ItemPool.Keys().copy()
	if A.settings.key_8_helm:C.remove(Items.HideoutHelmKey)
	if A.settings.no_logic or A.settings.shuffle_loading_zones==_D or A.settings.hard_level_progression:
		random.shuffle(C)
		if Items.FranticFactoryKey in C:C.remove(Items.FranticFactoryKey);C.append(Items.FranticFactoryKey)
		if Items.HideoutHelmKey in C:C.remove(Items.HideoutHelmKey);C.append(Items.HideoutHelmKey)
		B=PlaceItems(A.settings,A.settings.algorithm,C,ItemPool.KeyAssumedItems(),inOrder=_B)
		if B>0:raise Ex.ItemPlacementException(str(B)+E)
	elif A.settings.kongs_for_progression:
		D=ItemPool.KeyAssumedItems();BlockAccessToLevel(A.settings,2);B=PlaceItems(A.settings,A.settings.algorithm,[Items.JungleJapesKey],D);BlockAccessToLevel(A.settings,3);B+=PlaceItems(A.settings,A.settings.algorithm,[Items.AngryAztecKey],D);BlockAccessToLevel(A.settings,5);B+=PlaceItems(A.settings,A.settings.algorithm,[Items.FranticFactoryKey,Items.GloomyGalleonKey],D);BlockAccessToLevel(A.settings,6);B+=PlaceItems(A.settings,A.settings.algorithm,[Items.FungiForestKey],D);BlockAccessToLevel(A.settings,8);B+=PlaceItems(A.settings,A.settings.algorithm,[Items.CrystalCavesKey,Items.CreepyCastleKey],D);BlockAccessToLevel(A.settings,100)
		if Items.HideoutHelmKey in C:B+=PlaceItems(A.settings,A.settings.algorithm,[Items.HideoutHelmKey],D)
		if B>0:raise Ex.ItemPlacementException(str(B)+E)
	else:
		B=PlaceItems(A.settings,A.settings.algorithm,C,ItemPool.KeyAssumedItems(),inOrder=_B)
		if B>0:raise Ex.ItemPlacementException(str(B)+E)
def Fill(spoiler):
	'Fully randomizes and places all items.';A=spoiler;A.settings.debug_fill={};A.settings.debug_prerequisites={};A.settings.debug_fill_blueprints={};ItemPool.PlaceConstants(A.settings);FillKongsAndMoves(A)
	if Types.Blueprint in A.settings.shuffled_location_types:
		Reset();C=PlaceItems(A.settings,_E,ItemPool.Blueprints(A.settings).copy(),ItemPool.BlueprintAssumedItems())
		if C>0:raise Ex.ItemPlacementException(str(C)+' unplaced blueprints.')
	if Types.Key in A.settings.shuffled_location_types:FillShuffledKeys(A)
	if Types.Coin in A.settings.shuffled_location_types:
		Reset();D=PlaceItems(A.settings,A.settings.algorithm,ItemPool.CompanyCoinItems(),ItemPool.CoinAssumedItems())
		if D>0:raise Ex.ItemPlacementException(str(D)+' unplaced company coins.')
	if Types.Crown in A.settings.shuffled_location_types:
		Reset();B=_E
		if not A.settings.crown_door_open:B=A.settings.algorithm
		E=PlaceItems(A.settings,B,ItemPool.BattleCrownItems(),ItemPool.CrownAssumedItems())
		if E>0:raise Ex.ItemPlacementException(str(E)+' unplaced crowns.')
	if Types.Medal in A.settings.shuffled_location_types:
		Reset();B=_E
		if Types.Coin in A.settings.shuffled_location_types or A.settings.medal_requirement>39:B=A.settings.algorithm
		F=PlaceItems(A.settings,B,ItemPool.BananaMedalItems(),ItemPool.MedalAssumedItems())
		if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced medals.')
	if Types.Banana in A.settings.shuffled_location_types:
		Reset();G=PlaceItems(A.settings,_E,ItemPool.GoldenBananaItems(),[])
		if G>0:raise Ex.ItemPlacementException(str(G)+' unplaced GBs.')
	if LocationList[Locations.JapesDonkeyFreeDiddy].item is _A:LocationList[Locations.JapesDonkeyFreeDiddy].PlaceItem(Items.NoItem)
	Reset()
	if not GetAccessibleLocations(A.settings,[],SearchMode.CheckAllReachable):raise Ex.GameNotBeatableException('Game not able to complete 101% after placing all items.')
	return
def ShuffleSharedMoves(spoiler,placedMoves):
	'Shuffles shared kong moves into shops and then returns the remaining ones and their valid locations.';B=placedMoves;A=spoiler;ItemPool.PlaceConstants(A.settings);F=[A for A in SharedMoveLocations if LocationList[A].item is _A];G=[A for A in B if A in ItemPool.ImportantSharedMoves or A in ItemPool.JunkSharedMoves]
	if len(F)<len(ItemPool.ImportantSharedMoves)+len(ItemPool.JunkSharedMoves)-len(G):raise Ex.ItemPlacementException('Too many kong moves placed before shared moves. Only '+len(F)+' available for '+len(ItemPool.ImportantSharedMoves)+len(ItemPool.JunkSharedMoves)-len(G)+' remaining shared moves.')
	if A.settings.training_barrels!=_G and Items.Oranges not in B:
		J=PlaceItems(A.settings,_H,[Items.Oranges],[C for C in ItemPool.AllItems(A.settings)if C!=Items.Oranges and C not in B])
		if J>0:raise Ex.ItemPlacementException('Failed to place Orange training barrel move.')
	C=ItemPool.ImportantSharedMoves.copy()
	if A.settings.shockwave_status==_I and Items.CameraAndShockwave not in B:C.append(Items.CameraAndShockwave)
	elif A.settings.shockwave_status==_N and(Items.Camera not in B or Items.Shockwave not in B):C.append(Items.Camera);C.append(Items.Shockwave)
	for D in B:
		if D in C:C.remove(D)
	H=PlaceItems(A.settings,_H,C,[D for D in ItemPool.AllItems(A.settings)if D not in C and D not in B])
	if H>0:raise Ex.ItemPlacementException(str(H)+' unplaced shared important items.')
	E=ItemPool.JunkSharedMoves.copy()
	for D in B:
		if D in E:E.remove(D)
	I=PlaceItems(A.settings,_E,E,[B for B in ItemPool.AllItems(A.settings)if B not in E])
	if I>0:raise Ex.ItemPlacementException(str(I)+' unplaced shared junk items.')
def FillKongsAndMovesGeneric(spoiler):
	'Facilitate shuffling individual pools of items in lieu of full item rando.';B=spoiler;A=0
	while _B:
		try:
			Fill(B);Reset()
			if not VerifyWorldWithWorstCoinUsage(B.settings):raise Ex.GameNotBeatableException(_O)
			return
		except Ex.FillException as C:
			if A==20:js.postMessage(_P);raise C
			A+=1
			if A%5==0:js.postMessage(_Q+str(A));B.settings.shuffle_prices()
			else:js.postMessage(_R+str(A))
			Reset();Logic.ClearAllLocations()
def GeneratePlaythrough(spoiler):
	'Generate playthrough and way of the hoard and update spoiler.';A=spoiler;js.postMessage('Seed generated! Finalizing spoiler...');Reset();B=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,B);C=PareWoth(A,B);A.UpdateLocations(LocationList)
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
def PlacePriorityItems(spoiler,itemsToPlace,beforePlacedItems,levelBlock=_A):
	'Place the given items with priority, also placing all dependencies depending on where they got placed. Returns a list of all items newly placed by this function.';H=itemsToPlace;G=levelBlock;D=spoiler
	if H==[]:return[]
	B=H.copy();E=beforePlacedItems.copy();I=[]
	if G is not _A:I=[A for A in ItemPool.Keys()if ItemList[A].index>=G]
	C=ItemPool.AllKongMoves().copy()
	if Types.Key in D.settings.shuffled_location_types:
		C.extend(ItemPool.BlueprintAssumedItems().copy())
		for K in I:C.remove(K)
	if D.settings.training_barrels!=_G:C.extend(ItemPool.TrainingBarrelAbilities())
	if D.settings.shockwave_status!=_J:C.append(Items.Shockwave)
	for A in B:C.remove(A)
	for A in E:C.remove(A)
	L=PlaceItems(D.settings,_H,B.copy(),ownedItems=C)
	if L>0:M=', '.join([ItemList[A].name for A in B]);raise Ex.ItemPlacementException(f"Failed to priority place {M}")
	N=LogicVariables.GetKongs();E.extend(B);P=E.count(Items.ProgressiveSlam);F=[]
	for A in B:
		J=GetUnplacedItemPrerequisites(D,A,E,N);O=J.count(Items.ProgressiveSlam)
		for A in J:
			if A not in F or A==Items.ProgressiveSlam and O>1 and F.count(Items.ProgressiveSlam)<2:F.append(A)
	B.extend(PlacePriorityItems(D,F,E,G));return B
def PlaceKongsInKongLocations(spoiler,kongItems,kongLocations):
	'For these settings, Kongs to place, and locations to place them in, place the Kongs in such a way the generation will never error here.';N=' SEND THIS TO THE DEVS!';E=kongLocations;D=kongItems;A=spoiler;B=[B for B in A.settings.starting_kong_list]
	if A.settings.shuffle_loading_zones==_D or A.settings.no_logic:
		random.shuffle(D)
		if Locations.ChunkyKong in E:C=D.pop();LocationList[Locations.ChunkyKong].PlaceItem(C);A.settings.chunky_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.DiddyKong in E:C=D.pop();LocationList[Locations.DiddyKong].PlaceItem(C);A.settings.diddy_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.LankyKong in E:C=D.pop();LocationList[Locations.LankyKong].PlaceItem(C);A.settings.lanky_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.TinyKong in E:C=D.pop();LocationList[Locations.TinyKong].PlaceItem(C);J=list(set(B).intersection([Kongs.diddy,Kongs.chunky]));A.settings.tiny_freeing_kong=random.choice(J);B.append(ItemPool.GetKongForItem(C))
	elif A.settings.shuffle_loading_zones in(_K,'none'):
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
	'Fill kongs, then progression moves, then shared moves, then rest of moves.';A=spoiler;J=[];C=[]
	if A.settings.kong_rando:FillKongs(A)
	if not A.settings.unlock_all_moves and A.settings.move_rando!=_F and A.settings.training_barrels==_I:
		S=_A
		if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression:S=2;BlockAccessToLevel(A.settings,S)
		b=PlacePriorityItems(A,[Items.Barrels],C,levelBlock=S);C.extend(b)
		if Items.Vines not in C:
			N=_A
			if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression:
				N=2
				for V in range(1,8):
					if A.settings.level_order[V]==Levels.AngryAztec:N=V;break
				if A.settings.activate_all_bananaports==_F:N=min(2,N)
				BlockAccessToLevel(A.settings,N)
			c=PlacePriorityItems(A,[Items.Vines],C,levelBlock=N);C.extend(c)
		if Items.Swim not in C:
			T=_A
			if not A.settings.no_logic and A.settings.shuffle_loading_zones!=_D and not A.settings.hard_level_progression:T=4;BlockAccessToLevel(A.settings,T)
			d=PlacePriorityItems(A,[Items.Swim],C,levelBlock=T);C.extend(d)
	if A.settings.kong_rando:
		if A.settings.kongs_for_progression and A.settings.shuffle_loading_zones!=_D and A.settings.move_rando!='start_with':
			j={};K=A.settings.kong_locations.copy();D=[B for B in A.settings.starting_kong_list];L=A.settings.starting_kongs_count+1
			if A.settings.hard_level_progression:L=100
			H=1;R=_C
			while len(D)!=5:
				L=len(D)+1
				if A.settings.hard_level_progression:L=100
				E=[];O=_A
				if A.settings.level_order[H]==Levels.FranticFactory and Locations.ChunkyKong in K and A.settings.chunky_freeing_kong in D:K.remove(Locations.ChunkyKong);O=ItemPool.GetKongForItem(LocationList[Locations.ChunkyKong].item)
				if A.settings.level_order[H]==Levels.JungleJapes and Locations.DiddyKong in K and A.settings.diddy_freeing_kong in D:
					K.remove(Locations.DiddyKong);O=ItemPool.GetKongForItem(LocationList[Locations.DiddyKong].item);M=GetUnplacedItemPrerequisites(A,LocationList[Locations.DiddyKong].item,C,D);P=M.count(Items.ProgressiveSlam)
					for F in M:
						if F not in E:E.append(F)
						elif F==Items.ProgressiveSlam and P>1 and E.count(Items.ProgressiveSlam)<2:E.append(F)
				if A.settings.level_order[H]==Levels.AngryAztec and Locations.TinyKong in K and A.settings.tiny_freeing_kong in D:
					K.remove(Locations.TinyKong);O=ItemPool.GetKongForItem(LocationList[Locations.TinyKong].item);M=GetUnplacedItemPrerequisites(A,LocationList[Locations.TinyKong].item,C,D);P=M.count(Items.ProgressiveSlam)
					for F in M:
						if F not in E:E.append(F)
						elif F==Items.ProgressiveSlam and P>1 and E.count(Items.ProgressiveSlam)<2:E.append(F)
				elif A.settings.level_order[H]==Levels.AngryAztec and Locations.LankyKong in K and A.settings.lanky_freeing_kong in D and(Kongs.diddy in D or A.settings.open_levels or Kongs.donkey in D and A.settings.activate_all_bananaports==_D)and(Kongs.donkey in D or Kongs.lanky in D or Kongs.tiny in D):
					K.remove(Locations.LankyKong);O=ItemPool.GetKongForItem(LocationList[Locations.LankyKong].item);M=GetUnplacedItemPrerequisites(A,LocationList[Locations.LankyKong].item,C,D);P=E.count(Items.ProgressiveSlam)
					for F in M:
						if F not in E:E.append(F)
						elif F==Items.ProgressiveSlam and P>1 and E.count(Items.ProgressiveSlam)<2:E.append(F)
				if any(E):BlockAccessToLevel(A.settings,L);e=PlacePriorityItems(A,E,C,levelBlock=L);C.extend(e)
				if O is not _A:D.append(O);R=_C
				else:
					if H==L and R:raise Ex.ItemPlacementException('Kongs logically locked behind themselves. Only '+str(len(D))+' kongs logically accessible.')
					elif H==L:R=_B
					if A.settings.hard_level_progression:H=H%7+1;R=H==1
					else:H=H%L+1
				BlockAccessToLevel(A.settings,100)
	if not A.settings.unlock_all_moves and A.settings.move_rando!=_F:ShuffleSharedMoves(A,C.copy());J.extend(ItemPool.DonkeyMoves);J.extend(ItemPool.DiddyMoves);J.extend(ItemPool.LankyMoves);J.extend(ItemPool.TinyMoves);J.extend(ItemPool.ChunkyMoves)
	Reset();J=[A for A in J if A not in C];W=[]
	if Types.Key in A.settings.shuffled_location_types:W=ItemPool.BlueprintAssumedItems().copy()
	X=PlaceItems(A.settings,_H,J,W)
	if X>0:
		f={};g=[];h=[]
		for U in LocationList:
			B=LocationList[U]
			if B.item is not _A and B.item!=Items.NoItem and B.item<=Items.CameraAndShockwave:f[U]=B.item
			if B.type==Types.Shop and B.item is _A:
				g.append(B)
				if U in SharedMoveLocations:h.append(B)
		raise Ex.ItemPlacementException(str(X)+' unplaced items.')
	if not A.settings.unlock_all_moves and A.settings.move_rando!=_F:
		if A.settings.training_barrels==_I:
			Y=[A for A in TrainingBarrelLocations if LocationList[A].item is _A]
			if len(Y)>0:
				I=[]
				for B in DonkeyMoveLocations:
					G=LocationList[B].item
					if G is not _A and G!=Items.NoItem:I.append(B)
				for B in DiddyMoveLocations:
					G=LocationList[B].item
					if G is not _A and G!=Items.NoItem:I.append(B)
				for B in LankyMoveLocations:
					G=LocationList[B].item
					if G is not _A and G!=Items.NoItem:I.append(B)
				for B in TinyMoveLocations:
					G=LocationList[B].item
					if G is not _A and G!=Items.NoItem:I.append(B)
				for B in ChunkyMoveLocations:
					G=LocationList[B].item
					if G is not _A and G!=Items.NoItem:I.append(B)
				if len(I)==0:
					for (i,B) in LocationList.items():
						if B.item in ItemPool.AllKongMoves():I.append(i)
				for Z in Y:
					Q=random.choice(I);a=LocationList[Q].item;LocationList[Z].PlaceItem(a);LocationList[Q].PlaceItem(Items.NoItem);I.remove(Q)
					if Q in A.settings.debug_fill.keys():del A.settings.debug_fill[Q];A.settings.debug_fill[Z]=a
	A.settings.debug_preplaced_priority_moves=C
	if C.count(Items.ProgressiveSlam)>2:raise Ex.FillException("Somehow managed to place 3 slams? This shouldn't happen.")
def FillKongsAndMovesForLevelOrder(spoiler):
	'Shuffle Kongs and Moves accounting for level order restrictions.';A=spoiler;B=0
	while _B:
		try:
			ItemPool.PlaceConstants(A.settings);WipeProgressionRequirements(A.settings);A.settings.kongs_for_progression=_B;Fill(A)
			if A.settings.hard_level_progression:SetNewProgressionRequirementsUnordered(A.settings)
			else:SetNewProgressionRequirements(A.settings)
			A.settings.kongs_for_progression=_C
			if not VerifyWorldWithWorstCoinUsage(A.settings):raise Ex.GameNotBeatableException(_O)
			return
		except Ex.FillException as C:
			Reset();Logic.ClearAllLocations();B+=1
			if B==20:js.postMessage(_P);raise C
			if B%5==0:
				js.postMessage(_Q+str(B));A.settings.shuffle_prices()
				if A.settings.shuffle_loading_zones==_K:ShuffleExits.ShuffleExits(A.settings);A.UpdateExits()
			else:js.postMessage(_R+str(B))
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
	for B in range(0,7):A.EntryGBs[B]=0;A.BossBananas[B]=0;A.boss_kongs[B]=A.starting_kong;A.boss_maps[B]=Maps.JapesBoss
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
	'Set level progression requirements based on a random path of accessible levels.';A=settings;Z=A.shuffle_items and Types.Key in A.shuffled_location_types;K={};G={};I=ItemPool.DonkeyMoves.copy();I.extend(ItemPool.DiddyMoves);I.extend(ItemPool.LankyMoves);I.extend(ItemPool.TinyMoves);I.extend(ItemPool.ChunkyMoves);I.extend(ItemPool.ImportantSharedMoves);I.extend(ItemPool.TrainingBarrelAbilities());j=[Events.JapesKeyTurnedIn,Events.AztecKeyTurnedIn,Events.FactoryKeyTurnedIn,Events.GalleonKeyTurnedIn,Events.ForestKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn,Events.HelmKeyTurnedIn];BlockAccessToLevel(A,0);Reset();J=GetAccessibleLocations(A,[]);O=LogicVariables.GoldenBananas;P=0;A.EntryGBs=[A.blocker_0,A.blocker_1,A.blocker_2,A.blocker_3,A.blocker_4,A.blocker_5,A.blocker_6,A.blocker_7];A.BossBananas=[A.troff_0,A.troff_1,A.troff_2,A.troff_3,A.troff_4,A.troff_5,A.troff_6];L=[A.troff_0,A.troff_1,A.troff_2,A.troff_3,A.troff_4,A.troff_5,A.troff_6];f=0.4;U=0.7
	if A.hard_blockers:f=0.6;U=0.95
	H=[];V=[]
	while len(H)<7:
		Q=GetAccessibleOpenLevels(A,J);W=[B for B in Q if B not in H and A.EntryGBs[B]<=round(O*U)]
		if len(W)==0:
			g=[A for A in Q if A not in H]
			if len(g)==0:raise Ex.FillException('E1: Hard level order shuffler failed to progress through levels.')
			E=random.choice(g)
			if A.randomize_blocker_required_amounts:
				X=E
				for a in range(0,len(A.EntryGBs)):
					if a not in H and A.EntryGBs[a]<A.EntryGBs[X]:X=a
				k=A.EntryGBs[X];A.EntryGBs[X]=A.EntryGBs[E];A.EntryGBs[E]=k
			if A.EntryGBs[E]>round(O*U):
				b=round(O*U);c=max(P,round(O*f))
				if c>b:print("this shouldn't happen but here we are");c=b
				A.EntryGBs[E]=random.randint(c,b)
			W=[E]
		else:
			E=random.choice(W)
			if A.randomize_blocker_required_amounts and O>A.blocker_max and A.EntryGBs[E]<P:A.EntryGBs[E]=random.randint(P,A.blocker_max)
		P=A.EntryGBs[E];H.append(E)
		if not Z:BlockCompletionOfLevelSet(A,W)
		Reset();J=GetAccessibleLocations(A,[]);O=LogicVariables.GoldenBananas
		if Z:
			while _B:
				Q=GetAccessibleOpenLevels(A,J)
				if len(Q)<7 and len(Q)==len(H):
					Y=[A for(id,A)in LocationList.items()if A.type==Types.Key and A.level in H];random.shuffle(Y);C=_A;D=-1
					for B in Y:
						if B.item is _A or B.item==Items.NoItem:continue
						M=sum(LogicVariables.ColoredBananas[B.level])
						if M<A.BossBananas[B.level]:
							if B.item==Items.Barrels:C=B;D=1000
							d=ItemList[B.item]
							if d.type==Types.Key and D<100:C=B;D=100
							if B.item==Items.Swim and D<99:C=B;D=99
							if B.item==Items.Vines and D<98:C=B;D=98
							if B.item in ItemPool.Guns(A)or B.item in ItemPool.Instruments(A):C=B;D=50
							elif d.type==Types.Shop and D<10:C=B;D=10
							elif d.type in(Types.TrainingBarrel,Types.Shockwave)and D<9:C=B;D=9
							elif D<0:C=B;D=0
					if C is _A:raise Ex.FillException('E2: Hard level order shuffler failed to progress through levels.')
					R=L[C.level]/A.troff_max;A.BossBananas[C.level]=round(M*R);N=[LocationList[A].item for A in J if LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A and ItemList[LocationList[A].item].type in(Types.TrainingBarrel,Types.Shop,Types.Shockwave)]
					if C.item in N:N.remove(C.item)
					G[C.level]=N;K[C.level]=LogicVariables.GetKongs();Reset();J=GetAccessibleLocations(A,[])
				else:break
		else:
			if not A.open_lobbies:
				h=-1
				for i in A.level_order.keys():
					if A.level_order[i]==E:h=i-1;break
				e=j[h]
				if e in A.krool_keys_required and e not in[Events.FactoryKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn]:V.append(e)
			if len(Q)==len(H)and any(V):
				S=random.choice(V);V.remove(S)
				if S==Events.JapesKeyTurnedIn:LogicVariables.Events.append(Events.JapesKeyTurnedIn);F=A.level_order[1]
				elif S==Events.AztecKeyTurnedIn:LogicVariables.Events.append(Events.AztecKeyTurnedIn);F=A.level_order[2]
				elif S==Events.GalleonKeyTurnedIn:LogicVariables.Events.append(Events.GalleonKeyTurnedIn);F=A.level_order[4]
				elif S==Events.ForestKeyTurnedIn:LogicVariables.Events.append(Events.ForestKeyTurnedIn);F=A.level_order[5]
				M=sum(LogicVariables.ColoredBananas[F])
				if M<L[F]:R=L[F]/A.troff_max;A.BossBananas[F]=round(M*R)
				else:A.BossBananas[F]=L[F]
				K[F]=LogicVariables.GetKongs()
				if A.unlock_all_moves:G[F]=I
				else:N=[LocationList[A].item for A in J if LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A and ItemList[LocationList[A].item].type in(Types.TrainingBarrel,Types.Shop,Types.Shockwave)];G[F]=N
	Y=[B for(id,B)in LocationList.items()if B.type==Types.Key and B.level in H and A.BossBananas[B.level]>=L[B.level]]
	for B in Y:
		if A.BossBananas[B.level]>500:A.BossBananas[B.level]=L[B.level]
		if B.level not in K.keys():K[B.level]=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky];G[B.level]=I
		if Z:
			T=B.item
			if T is _A or ItemList[T].type not in(Types.TrainingBarrel,Types.Shop,Types.Shockwave,Types.Key):continue
			if T in G[B.level]:G[B.level].remove(T)
			B.PlaceItem(Items.TestItem);Reset();J=GetAccessibleLocations(A,[])
			if not LogicVariables.found_test_item:R=L[B.level]/A.troff_max;M=sum(LogicVariables.ColoredBananas[B.level]);A.BossBananas[B.level]=round(M*R);N=[LocationList[A].item for A in J if LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A and ItemList[LocationList[A].item].type in(Types.TrainingBarrel,Types.Shop,Types.Shockwave)];G[B.level]=N;K[B.level]=LogicVariables.GetKongs()
			B.PlaceItem(T)
	if A.randomize_blocker_required_amounts and not A.maximize_helm_blocker and A.EntryGBs[7]<P:A.EntryGBs[7]=random.randint(P,A.blocker_max)
	ShuffleBossesBasedOnOwnedItems(A,K,G);A.owned_kongs_by_level=K;A.owned_moves_by_level=G;Reset()
	if not GetAccessibleLocations(A,[],SearchMode.CheckAllReachable):raise Ex.GameNotBeatableException('Complex progression generation prevented 101%.')
def GetAccessibleOpenLevels(settings,accessible):
	'Return the list of levels (not lobbies) you have access to after running GetAccessibleLocations().';B=settings;E=[Events.JapesKeyTurnedIn,Events.AztecKeyTurnedIn,Events.FactoryKeyTurnedIn,Events.GalleonKeyTurnedIn,Events.ForestKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn,Events.HelmKeyTurnedIn];F=[A for A in LogicVariables.Events if A in E];A=[1]
	if not B.open_lobbies:
		for C in F:
			if C==Events.JapesKeyTurnedIn:A.append(2)
			elif C==Events.AztecKeyTurnedIn:A.append(3);A.append(4)
			elif C==Events.GalleonKeyTurnedIn:A.append(5)
			elif C==Events.ForestKeyTurnedIn:A.append(6);A.append(7)
	else:A=[1,2,3,4,5,6,7]
	if 6 in A and not LogicVariables.donkey and not LogicVariables.chunky and not(LogicVariables.tiny and LogicVariables.twirl):A.remove(6)
	if B.training_barrels!=_G:
		if B.activate_all_bananaports==_F and not LogicVariables.vines:
			if 2 in A:A.remove(2)
			if 6 in A:A.remove(6)
		if 4 in A and not LogicVariables.swim:A.remove(4)
	D=[B.level_order[C]for C in A]
	if Levels.AngryAztec in D:
		if not LogicVariables.vines and not(LogicVariables.tiny and LogicVariables.twirl):D.remove(Levels.AngryAztec)
	return D
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
		if A.settings.shuffle_loading_zones==_K:ShuffleExits.ShuffleExits(A.settings);A.UpdateExits()
		WipeProgressionRequirements(A.settings);ShuffleMisc(A);FillKongsAndMovesForLevelOrder(A)
	else:
		ShuffleMisc(A)
		if A.settings.shuffle_loading_zones!='none':ShuffleExits.ExitShuffle(A.settings);A.UpdateExits()
		if A.settings.move_rando!=_F and not A.settings.unlock_all_moves or A.settings.kong_rando or any(A.settings.shuffled_location_types):FillKongsAndMovesGeneric(A)
		else:
			ItemPool.PlaceConstants(A.settings)
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.VanillaItemsGameNotBeatableException('Game unbeatable.')
	GeneratePlaythrough(A)
	if A.settings.wrinkly_hints in['standard','cryptic']:compileHints(A)
	Reset();ShuffleExits.Reset();A.createJson();js.postMessage('Patching ROM...');return A
def ShuffleMisc(spoiler):
	'Shuffle miscellaneous objects outside of main fill algorithm, including Kasplats, Bonus barrels, and bananaport warps.';N='isles';M='crossmap_coupled';L='in_level';A=spoiler
	if A.settings.wrinkly_location_rando or A.settings.tns_location_rando or('remove_wrinkly_puzzles'in A.settings.misc_changes_selected or len(A.settings.misc_changes_selected)==0):ShuffleDoors(A)
	if A.settings.crown_placement_rando:H={};I={};ShuffleCrowns(H,I);A.crown_locations=H;A.human_crowns=dict(sorted(I.items()))
	KasplatShuffle(A,LogicVariables);A.human_kasplats={};A.UpdateKasplats(LogicVariables.kasplat_map)
	if A.settings.bonus_barrels in(_E,'selected'):BarrelShuffle(A.settings);A.UpdateBarrels()
	if A.settings.cb_rando:ShuffleCBs(A)
	if A.settings.bananaport_rando==L:B=[];C={};ShuffleWarps(B,C);A.bananaport_replacements=B.copy();A.human_warp_locations=C
	elif A.settings.bananaport_rando in(M,'crossmap_decoupled'):B=[];C={};ShuffleWarpsCrossMap(B,C,A.settings.bananaport_rando==M);A.bananaport_replacements=B.copy();A.human_warp_locations=C
	if A.settings.random_patches:O=[];A.human_patches=ShufflePatches(A,O).copy()
	if A.settings.shuffle_shops:ShuffleShopLocations(A)
	A.human_item_assignment={}
	if A.settings.activate_all_bananaports in[_D,N]:
		if A.settings.bananaport_rando in(L,_F):
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