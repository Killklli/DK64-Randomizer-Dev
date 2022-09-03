'Module used to distribute items randomly.'
_K='levels'
_J='Retrying fill. Tries: '
_I='Fill failed, out of retries.'
_H='Game unbeatable after placing all items.'
_G='assumed'
_F='random'
_E='cross_purchase'
_D='all'
_C=False
_B=True
_A=None
import json,random,js,randomizer.ItemPool as ItemPool,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic,randomizer.ShuffleExits as ShuffleExits
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
from randomizer.Lists.Location import LocationList
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Lists.ShufflableExit import GetLevelShuffledToIndex,GetShuffledLevelIndex
from randomizer.Lists.Warps import BananaportVanilla
from randomizer.Logic import STARTING_SLAM,LogicVarHolder,LogicVariables
from randomizer.LogicClasses import Sphere,TransitionFront
from randomizer.Prices import GetMaxForKong,GetPriceOfMoveItem
from randomizer.Settings import Settings
from randomizer.ShuffleBarrels import BarrelShuffle
from randomizer.ShuffleBosses import ShuffleBossesBasedOnOwnedItems
from randomizer.ShuffleKasplats import InitKasplatMap,KasplatShuffle
from randomizer.ShufflePatches import ShufflePatches
from randomizer.ShuffleShopLocations import ShuffleShopLocations
from randomizer.ShuffleWarps import ShuffleWarps
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
	'Search to find all reachable locations given owned items.';Z='skip';V=ownedItems;P=purchaseList;O=settings;D=searchType
	if O.no_logic and D in[SearchMode.CheckAllReachable,SearchMode.CheckBeatable,SearchMode.CheckSpecificItemReachable]:return _B
	if P is _A:P=[]
	G=[];H=[];Q=[];I=_B
	while len(H)>0 or I:
		E=Sphere()
		if Q:E.availableGBs=Q[-1].availableGBs
		for J in H:
			G.append(J);A=LocationList[J]
			if A.item is not _A:
				if A.type==Types.Shop and D==SearchMode.GetReachableWithControlledPurchases and J not in P:continue
				V.append(A.item)
				if D==SearchMode.GeneratePlaythrough and ItemList[A.item].playthrough:
					if A.item==Items.BananaHoard:E.locations=[J];break
					if A.item==Items.GoldenBanana:E.availableGBs+=1
					E.locations.append(J)
				if D==SearchMode.CheckBeatable and A.item==Items.BananaHoard:return _B
				if D==SearchMode.CheckSpecificItemReachable and A.item==targetItemId:return _B
		if len(E.locations)>0:
			Q.append(E)
			if LocationList[E.locations[0]].item==Items.BananaHoard:break
		I=_C;H=[];LogicVariables.Update(V)
		for R in LogicVariables.GetKongs():
			LogicVariables.SetKong(R);S=Logic.Regions[Regions.IslesMain];S.id=Regions.IslesMain;S.dayAccess=_B;S.nightAccess=Events.Night in LogicVariables.Events;K=[S];F=[Regions.IslesMain];W=[(A,B)for(A,B)in Logic.Regions.items()if B.HasAccess(R)and A not in F];F.extend([A[0]for A in W]);K.extend([A[1]for A in W])
			while len(K)>0:
				B=K.pop();B.UpdateAccess(R,LogicVariables);LogicVariables.UpdateCurrentRegionAccess(B)
				for L in B.events:
					if L.name not in LogicVariables.Events and L.logic(LogicVariables):I=_B;LogicVariables.Events.append(L.name)
					if L.name==Events.Night and L.logic(LogicVariables):B.nightAccess=_B
				if B.id in Logic.CollectibleRegions.keys():
					for M in Logic.CollectibleRegions[B.id]:
						if not M.added and M.kong in(R,Kongs.any)and M.logic(LogicVariables)and M.enabled:LogicVariables.AddCollectible(M,B.level)
				for A in B.locations:
					if A.logic(LogicVariables)and A.id not in H and A.id not in G:
						if A.bonusBarrel is MinigameType.BonusBarrel and O.bonus_barrels!=Z or A.bonusBarrel is MinigameType.HelmBarrel and O.helm_barrels!=Z:
							a=BarrelMetaData[A.id].minigame
							if not MinigameRequirements[a].logic(LogicVariables):continue
						elif LocationList[A.id].type==Types.Blueprint:
							if not LogicVariables.KasplatAccess(A.id):continue
						elif LocationList[A.id].type==Types.Shop:
							if D!=SearchMode.GetReachableWithControlledPurchases or A.id in P:LogicVariables.PurchaseShopItem(LocationList[A.id])
						elif A.id==Locations.NintendoCoin:LogicVariables.Coins[Kongs.donkey]-=2
						H.append(A.id)
				X=B.exits.copy()
				if O.shuffle_loading_zones and B.level!=Levels.DKIsles and B.level!=Levels.Shops:
					Y=GetExitLevelExit(B)
					if Y is not _A:b=ShuffleExits.ShufflableExits[Y].back.regionId;X.append(TransitionFront(b,lambda l:_B))
				for exit in X:
					C=exit.dest
					if exit.exitShuffleId is not _A and not exit.assumed:
						T=ShuffleExits.ShufflableExits[exit.exitShuffleId]
						if T.shuffled:C=ShuffleExits.ShufflableExits[T.shuffledId].back.regionId
						elif T.toBeShuffled and not exit.assumed:continue
					if C not in F and exit.logic(LogicVariables):
						U=_B
						if exit.time==Time.Night and not B.nightAccess:U=_C
						elif exit.time==Time.Day and not B.dayAccess:U=_C
						if U:F.append(C);N=Logic.Regions[C];N.id=C;K.append(N)
					if exit.logic(LogicVariables):
						if B.dayAccess and exit.time!=Time.Night and not Logic.Regions[C].dayAccess:Logic.Regions[C].dayAccess=_B;I=_B
						if B.nightAccess and exit.time!=Time.Day and not Logic.Regions[C].nightAccess:Logic.Regions[C].nightAccess=_B;I=_B
				if B.deathwarp is not _A:
					C=B.deathwarp.dest
					if C not in F and B.deathwarp.logic(LogicVariables):F.append(C);N=Logic.Regions[C];N.id=C;K.append(N)
	if D in(SearchMode.GetReachable,SearchMode.GetReachableWithControlledPurchases):return G
	elif D==SearchMode.CheckBeatable or D==SearchMode.CheckSpecificItemReachable:return _C
	elif D==SearchMode.GeneratePlaythrough:return Q
	elif D==SearchMode.CheckAllReachable:return len(G)==len(LocationList)
	elif D==SearchMode.GetUnreachable:return[A for A in LocationList if A not in G]
def VerifyWorld(settings):
	'Make sure all item locations are reachable on current world graph with constant items placed and all other items owned.';A=settings
	if A.no_logic:return _B
	ItemPool.PlaceConstants(A);B=GetAccessibleLocations(A,ItemPool.AllItems(A),SearchMode.GetUnreachable);C=len(B)==0;Reset();return C
def VerifyWorldWithWorstCoinUsage(settings):
	'Make sure the game is beatable without it being possible to run out of coins for required moves.';A=settings
	if A.no_logic:return _B
	D=[];H=[];N=[GetMaxForKong(A,Kongs.donkey),GetMaxForKong(A,Kongs.diddy),GetMaxForKong(A,Kongs.lanky),GetMaxForKong(A,Kongs.tiny),GetMaxForKong(A,Kongs.chunky)]
	while _B:
		Reset();H=GetAccessibleLocations(A,[],SearchMode.GetReachableWithControlledPurchases,D);O=[LocationList[A].item for A in D];P=GetMaxCoinsSpent(A,O);F=[N[A]-P[A]for A in range(0,5)];E=LogicVariables.Coins.copy()
		if E[Kongs.donkey]>=F[Kongs.donkey]and E[Kongs.diddy]>=F[Kongs.diddy]and E[Kongs.lanky]>=F[Kongs.lanky]and E[Kongs.tiny]>=F[Kongs.tiny]and E[Kongs.chunky]>=F[Kongs.chunky]:Reset();return _B
		if len([A for A in H if LocationList[A].item==Items.BananaHoard])>0:Reset();return _B
		K=[A for A in H if LocationList[A].type==Types.Shop and LocationList[A].item is not _A and LocationList[A].item!=Items.NoItem and A not in D and LogicVariables.CanBuy(A)];I={};G={}
		if len(K)==0:print('Seed is invalid, coin locked with purchase order: '+str([LocationList[A].name+': '+LocationList[A].item.name+', 'for A in D]));Reset();return _C
		C=_A
		for B in K:
			L=D.copy();L.append(B);Reset();Q=GetAccessibleLocations(A,[],SearchMode.GetReachableWithControlledPurchases,L);R=LogicVariables.Coins.copy();M=[0,0,0,0,0]
			for J in LogicVariables.GetKongs():M[J]=R[J]-E[J]
			I[B]=M;G[B]=[LocationList[A].item for A in Q if A not in H and LocationList[A].item is not _A]
			if C is _A:C=B;continue
			if len([A for A in I[B]if A<0])==0:continue
			S=len([A for A in G[C]if ItemList[A].type==Types.Kong]);T=len([A for A in G[B]if ItemList[A].type==Types.Kong])
			if T>S:continue
			U=len([A for A in G[C]if ItemList[A].type==Types.Key]);V=len([A for A in G[B]if ItemList[A].type==Types.Key])
			if V>U:continue
			W=sum(list(I[C]));X=sum(list(I[B]))
			if X<W:C=B
		D.append(C)
def Reset():'Reset logic variables and region info that should be reset before a search.';LogicVariables.Reset();Logic.ResetRegionAccess();Logic.ResetCollectibleRegions()
def ParePlaythrough(settings,PlaythroughLocations):
	'Pare playthrough down to only the essential elements.';C=PlaythroughLocations;A=settings;G=[];I=max([A.blocker_0,A.blocker_1,A.blocker_2,A.blocker_3,A.blocker_4,A.blocker_5,A.blocker_6,A.blocker_7])
	for D in range(len(C)-2,-1,-1):
		B=C[D]
		if D>0 and C[D-1].availableGBs>I:B.locations=[A for A in B.locations if LocationList[A].item!=Items.GoldenBanana]
		for E in B.locations.copy():
			F=LocationList[E]
			if F.item==Items.GoldenBanana:continue
			H=F.item;F.item=_A;Reset()
			if GetAccessibleLocations(A,[],SearchMode.CheckBeatable):B.locations.remove(E);F.SetDelayedItem(H);G.append(E)
			else:F.PlaceItem(H)
	for D in range(len(C)-2,-1,-1):
		B=C[D]
		if len(B.locations)==0:C.remove(B)
	for E in G:LocationList[E].PlaceDelayedItem()
def PareWoth(settings,PlaythroughLocations):
	'Pare playthrough to locations which are Way of the Hoard (hard required by logic).';A=[]
	for D in PlaythroughLocations:
		for E in [A for A in D.locations if not LocationList[A].constant]:A.append(E)
	for F in range(len(A)-1,-1,-1):
		C=A[F];B=LocationList[C];G=B.item;B.item=_A;Reset()
		if GetAccessibleLocations(settings,[],SearchMode.CheckBeatable):A.remove(C)
		B.PlaceItem(G)
	return A
def RandomFill(itemsToPlace,validLocations):
	'Randomly place given items in any location disregarding logic.';A=itemsToPlace;random.shuffle(A);B=[]
	for (id,F) in LocationList.items():
		if F.item is _A:B.append(id)
	while len(A)>0:
		D=A.pop();C=[A for A in B if A in GetItemValidLocations(validLocations,D)]
		if len(C)==0:return len(A)
		random.shuffle(C);E=C.pop();LocationList[E].PlaceItem(D);B.remove(E)
	return 0
def ForwardFill(settings,itemsToPlace,validLocations,ownedItems=_A):
	'Forward fill algorithm for item placement.';C=itemsToPlace;A=ownedItems
	if A is _A:A=[]
	random.shuffle(C);A=A.copy()
	while len(C)>0:
		B=GetAccessibleLocations(settings,A.copy());B=[A for A in B if LocationList[A].item is _A and A in validLocations]
		if len(B)==0:return len(C)
		random.shuffle(B);E=B.pop();D=C.pop();A.append(D);LocationList[E].PlaceItem(D)
	return 0
def GetItemValidLocations(validLocations,item):
	'Get the list of valid locations for this item.';A=validLocations;B=A
	if isinstance(A,dict):
		for C in A.keys():
			if item==C:B=A[C];break
			B=list(LocationList)
	return B
def AssumedFill(settings,itemsToPlace,validLocations,ownedItems=_A,isPriorityMove=_C):
	'Assumed fill algorithm for item placement.';a=' in location ';P=validLocations;O='Failed placing item ';K=ownedItems;G=itemsToPlace;A=settings
	if K is _A:K=[]
	Q=GetMaxCoinsSpent(A,G+K);random.shuffle(G)
	while len(G)>0:
		B=G.pop(0);R=_C;C=G.copy();C.extend(K);b=sum((1 for A in C if A==Items.ProgressiveSlam))+STARTING_SLAM;c=sum((1 for A in C if A==Items.ProgressiveAmmoBelt));d=sum((1 for A in C if A==Items.ProgressiveInstrumentUpgrade));e=GetItemValidLocations(P,B);Reset();N=GetAccessibleLocations(A,C);I=[A for A in N if LocationList[A].item is _A and A in e]
		if len(I)==0:
			print(O+ItemList[B].name+', no valid reachable locations without this item.');U=[ItemList[A].name for A in C if ItemList[A].type==Types.Kong];V=[]
			for f in A.starting_kong_list:V.append(f.name.capitalize())
			for (D,F) in enumerate(V):U.insert(D,F)
			g=[ItemList[A].name for A in C if ItemList[A].type==Types.Shop];h=len([A for A in C if ItemList[A].type==Types.Banana]);js.postMessage('Current Moves owned at failure: '+str(g)+' with GB count: '+str(h)+' and kongs freed: '+str(U));return len(G)+1
		random.shuffle(I)
		if ItemList[B].type==Types.Shop:
			S=ItemList[B].kong;L=GetPriceOfMoveItem(B,A,b,c,d);T=[0,0,0,0,0]
			if L is not _A:
				if S==Kongs.any:
					for W in range(5):Q[W]-=L;T[W]=L
				else:Q[S]-=L;T[S]=L
		elif ItemList[B].type==Types.Kong:
			J=[KongFromItem(A)for A in C if ItemList[A].type==Types.Kong]
			for (D,F) in enumerate(A.starting_kong_list):J.insert(D,F)
			X=KongFromItem(B)
			if X in J:J.remove(X)
			if A.kongs_for_progression:
				i=GetShuffledLevelIndex(Levels.JungleJapes);j=GetShuffledLevelIndex(Levels.AngryAztec);k=GetShuffledLevelIndex(Levels.FranticFactory);H={}
				for D in range(0,7):
					if D==i:
						if Locations.DiddyKong in A.kong_locations:H[Locations.DiddyKong]=D
						else:H[Locations.DiddyKong]=-1
					elif D==j:
						if Locations.LankyKong in A.kong_locations:H[Locations.LankyKong]=D
						else:H[Locations.LankyKong]=-1
						if Locations.TinyKong in A.kong_locations:H[Locations.TinyKong]=D
						else:H[Locations.TinyKong]=-1
					elif D==k:
						if Locations.ChunkyKong in A.kong_locations:H[Locations.ChunkyKong]=D
						else:H[Locations.ChunkyKong]=-1
				I.sort(key=lambda x:H[x],reverse=_B)
		for E in I:
			LocationList[E].PlaceItem(B)
			if ItemList[B].type==Types.Kong:
				if E not in A.kong_locations:LocationList[E].PlaceItem(Items.NoItem)
				if E==Locations.DiddyKong:A.diddy_freeing_kong=random.choice(J)
				elif E==Locations.LankyKong:A.lanky_freeing_kong=random.choice(J)
				elif E==Locations.TinyKong:
					Y=list(set(J).intersection([Kongs.diddy,Kongs.chunky]))
					if len(Y)==0:js.postMessage(O+ItemList[B].name+a+LocationList[E].name+', due to no kongs being able to free them');M=_C;break
					A.tiny_freeing_kong=random.choice(Y)
				elif E==Locations.ChunkyKong:A.chunky_freeing_kong=random.choice(J)
			C=G.copy();C.extend(K);Reset();N=GetAccessibleLocations(A,C);M=_B
			for l in G:
				m=GetItemValidLocations(P,l);I=[A for A in N if A in m and A!=E]
				if len(I)==0:js.postMessage(O+ItemList[B].name+a+LocationList[E].name+', due to too few remaining locations in play');M=_C;break
				N.remove(I[0])
			if M and ItemList[B].type==Types.Shop and not isPriorityMove:
				Z=[0,0,0,0,0]
				for F in range(5):Z[F]=LogicVariables.Coins[F]-Q[F]
				for F in range(5):
					if Z[F]<T[F]:M=_C
			if not M:LocationList[E].item=_A;R=_C;continue
			R=_B;break
		if not R:js.postMessage(O+ItemList[B].name+' in any of remaining '+str(len(P))+' possible locations');return len(G)+1
	return 0
def GetMaxCoinsSpent(settings,ownedItems):
	'Calculate the max number of coins each kong could have spent given the ownedItems and the price settings.';B=ownedItems;C=[0,0,0,0,0];E=sum((1 for A in B if A==Items.ProgressiveSlam))+STARTING_SLAM;F=sum((1 for A in B if A==Items.ProgressiveAmmoBelt));G=sum((1 for A in B if A==Items.ProgressiveInstrumentUpgrade))
	for A in B:
		if ItemList[A].type==Types.Shop:
			H=ItemList[A].kong
			if A==Items.ProgressiveSlam:E-=1
			elif A==Items.ProgressiveAmmoBelt:F-=1
			elif A==Items.ProgressiveInstrumentUpgrade:G-=1
			D=GetPriceOfMoveItem(A,settings,E,F,G)
			if D is not _A:
				if H==Kongs.any:
					for I in range(5):C[I]+=D
				else:C[H]+=D
	return C
def GetItemPrerequisites(spoiler,targetItemId,ownedKongs=[]):
	'Given the target item and the current world state, find a valid, minimal, unplaced set of items required to reach the location it is in.';D=ownedKongs;C=spoiler;B=targetItemId;Reset()
	if GetAccessibleLocations(C.settings,[],SearchMode.CheckSpecificItemReachable,targetItemId=B):return[]
	A=[]
	if D==[]:D=GetKongs()
	G=[A for A in ItemPool.OwnedKongMoves(D)if A!=B];random.shuffle(G);E=_A
	for H in G:
		A.append(H);Reset()
		if GetAccessibleLocations(C.settings,A.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=B):E=H;break
	if E is _A:
		F=_A
		for I in GetValidLocationsForMove(C,B):
			if LocationList[I].item==B:F=LocationList[I];break
		if F is _A:raise Ex.ItemPlacementException('Target item not placed??')
		raise Ex.ItemPlacementException('Item placed in an inaccessible location: '+str(F.name))
	while A!=[]and A[0]!=E:
		J=A.pop(0);Reset()
		if not GetAccessibleLocations(C.settings,A.copy(),SearchMode.CheckSpecificItemReachable,targetItemId=B):A.append(J)
	return A
def GetValidLocationsForMove(spoiler,move):
	'Return the valid locations for the given move. Currently only returns shop locations for moves.';C=move;B=spoiler;A=[]
	if B.settings.move_rando==_E or C in ItemPool.DonkeyMoves:A.extend(ItemPool.DonkeyMoveLocations.copy())
	if B.settings.move_rando==_E or C in ItemPool.DiddyMoves:A.extend(ItemPool.DiddyMoveLocations.copy())
	if B.settings.move_rando==_E or C in ItemPool.TinyMoves:A.extend(ItemPool.TinyMoveLocations.copy())
	if B.settings.move_rando==_E or C in ItemPool.ChunkyMoves:A.extend(ItemPool.ChunkyMoveLocations.copy())
	if B.settings.move_rando==_E or C in ItemPool.LankyMoves:A.extend(ItemPool.LankyMoveLocations.copy())
	return list(A)
def PlaceItems(settings,algorithm,itemsToPlace,ownedItems=_A,validLocations=_A,isPriorityMove=_C):
	'Places items using given algorithm.';E=itemsToPlace;D=settings;C=ownedItems;B=algorithm;A=validLocations
	if C is _A:C=[]
	if A is _A:A=[]
	if D.no_logic:B=_F
	if len(A)==0:A=list(LocationList)
	if B==_G:return AssumedFill(D,E,A,C,isPriorityMove)
	elif B=='forward':return ForwardFill(D,E,A,C)
	elif B==_F:return RandomFill(E,A)
def Fill(spoiler):
	'Fully randomizes and places all items. Currently theoretical.';A=spoiler;B=0
	while _B:
		try:
			ItemPool.PlaceConstants(A.settings);C=PlaceItems(A.settings,A.settings.algorithm,ItemPool.HighPriorityItems(A.settings),ItemPool.HighPriorityAssumedItems(A.settings))
			if C>0:raise Ex.ItemPlacementException(str(C)+' unplaced high priority items.')
			Reset();D=PlaceItems(A.settings,A.settings.algorithm,ItemPool.Blueprints(A.settings),ItemPool.BlueprintAssumedItems(A.settings))
			if D>0:raise Ex.ItemPlacementException(str(D)+' unplaced blueprints.')
			Reset();E=PlaceItems(A.settings,A.settings.algorithm,ItemPool.LowPriorityItems(A.settings),ItemPool.ExcessItems(A.settings))
			if E>0:raise Ex.ItemPlacementException(str(E)+' unplaced low priority items.')
			H=ItemPool.ExcessItems(A.settings);F=PlaceItems(A.settings,_F,ItemPool.ExcessItems(A.settings))
			if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced excess items.')
			Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_H)
			return
		except Ex.FillException as G:
			if B==4:js.postMessage(_I);raise G
			B+=1;js.postMessage(_J+str(B));Reset();Logic.ClearAllLocations()
def ShuffleSharedMoves(spoiler):
	'Shuffles shared kong moves and then returns the remaining ones and their valid locations.';A=spoiler;ItemPool.PlaceConstants(A.settings);B=[];B.extend(ItemPool.DonkeyMoves);B.extend(ItemPool.DiddyMoves);B.extend(ItemPool.LankyMoves);B.extend(ItemPool.TinyMoves);B.extend(ItemPool.ChunkyMoves);C=ItemPool.SharedMoveLocations.copy();M=ItemPool.GetKongMoveOccupiedShops()
	for N in M:C.remove(N)
	if len(C)<len(ItemPool.ImportantSharedMoves)+len(ItemPool.JunkSharedMoves):raise Ex.ItemPlacementException('Too many kong moves placed before shared moves. Only '+len(C)+' available for all shared moves.')
	F=PlaceItems(A.settings,_G,ItemPool.ImportantSharedMoves.copy(),[B for B in ItemPool.AllItems(A.settings)if B not in ItemPool.ImportantSharedMoves],C)
	if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced shared important items.')
	G=PlaceItems(A.settings,_F,ItemPool.JunkSharedMoves.copy(),[B for B in ItemPool.AllItems(A.settings)if B not in ItemPool.JunkSharedMoves],validLocations=C)
	if G>0:raise Ex.ItemPlacementException(str(G)+' unplaced shared junk items.')
	H=[]
	for I in C:
		if LocationList[I].item is not _A:H.append(I)
	J=ItemPool.GetMoveLocationsToRemove(H);E={};O=[ItemPool.DonkeyMoves,ItemPool.DiddyMoves,ItemPool.LankyMoves,ItemPool.TinyMoves,ItemPool.ChunkyMoves];P=[ItemPool.DonkeyMoveLocations,ItemPool.DiddyMoveLocations,ItemPool.LankyMoveLocations,ItemPool.TinyMoveLocations,ItemPool.ChunkyMoveLocations];D=ItemPool.DonkeyMoveLocations.copy();D.update(ItemPool.DiddyMoveLocations.copy());D.update(ItemPool.LankyMoveLocations.copy());D.update(ItemPool.TinyMoveLocations.copy());D.update(ItemPool.ChunkyMoveLocations.copy())
	for K in range(5):
		for L in O[K]:
			if A.settings.move_rando==_E:E[L]=D-J
			else:E[L]=P[K]-J
	return B,E
def FillKongsAndMovesGeneric(spoiler):
	'Facilitate shuffling individual pools of items in lieu of full item rando.';B=spoiler;A=0
	while _B:
		try:
			FillKongsAndMoves(B);Reset()
			if not VerifyWorldWithWorstCoinUsage(B.settings):raise Ex.GameNotBeatableException(_H)
			return
		except Ex.FillException as C:
			if A==20:js.postMessage(_I);raise C
			A+=1
			if A%5==0:B.settings.shuffle_prices()
			js.postMessage(_J+str(A));Reset();Logic.ClearAllLocations()
def GeneratePlaythrough(spoiler):'Generate playthrough and way of the hoard and update spoiler.';A=spoiler;Reset();B=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,B);C=PareWoth(A.settings,B);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,B);A.UpdateWoth(LocationList,C)
def GetLogicallyAccessibleKongLocations(spoiler,kongLocations,ownedKongs,latestLevel):
	'Find the logically accessible Kong Locations given the current state of Kong unlocking.';D=kongLocations;B=spoiler;A=ownedKongs;C=[]
	for E in range(1,latestLevel+1):
		if B.settings.level_order[E]==Levels.JungleJapes and Locations.DiddyKong in D:C.append(Locations.DiddyKong)
		if B.settings.level_order[E]==Levels.FranticFactory and Locations.ChunkyKong in D:C.append(Locations.ChunkyKong)
		if B.settings.level_order[E]==Levels.AngryAztec and Locations.TinyKong in D and(Kongs.diddy in A or Kongs.chunky in A):C.append(Locations.TinyKong)
		if B.settings.level_order[E]==Levels.AngryAztec and Locations.LankyKong in D and(Kongs.diddy in A or B.settings.open_levels or Kongs.donkey in A and B.settings.activate_all_bananaports==_D)and(Kongs.donkey in A or Kongs.lanky in A or Kongs.tiny in A):C.append(Locations.LankyKong)
	return C
def PlaceKongs(spoiler,kongItems,kongLocations):
	'For these settings, Kongs to place, and locations to place them in, place the Kongs in such a way the generation will never error here.';N=' SEND THIS TO THE DEVS!';E=kongLocations;D=kongItems;A=spoiler;B=[B for B in A.settings.starting_kong_list]
	if A.settings.shuffle_loading_zones==_D or A.settings.no_logic:
		random.shuffle(D)
		if Locations.ChunkyKong in E:C=D.pop();LocationList[Locations.ChunkyKong].PlaceItem(C);A.settings.chunky_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.DiddyKong in E:C=D.pop();LocationList[Locations.DiddyKong].PlaceItem(C);A.settings.diddy_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.LankyKong in E:C=D.pop();LocationList[Locations.LankyKong].PlaceItem(C);A.settings.lanky_freeing_kong=random.choice(B);B.append(ItemPool.GetKongForItem(C))
		if Locations.TinyKong in E:C=D.pop();LocationList[Locations.TinyKong].PlaceItem(C);J=list(set(B).intersection([Kongs.diddy,Kongs.chunky]));A.settings.tiny_freeing_kong=random.choice(J);B.append(ItemPool.GetKongForItem(C))
	elif A.settings.shuffle_loading_zones in(_K,'none'):
		H=len(B)+1;F=GetLogicallyAccessibleKongLocations(A,E,B,H)
		while len(B)!=5:
			if not any(F):raise Ex.EntrancePlacementException('Levels shuffled in a way that makes Kong unlocks impossible. SEND THIS TO THE DEVS! '+json.dumps(A.settings.__dict__)+N)
			G=random.choice(F);F.remove(G)
			if G==Locations.DiddyKong:A.settings.diddy_freeing_kong=random.choice(B)
			elif G==Locations.LankyKong:A.settings.lanky_freeing_kong=random.choice(B)
			elif G==Locations.TinyKong:J=list(set(B).intersection([Kongs.diddy,Kongs.chunky]));A.settings.tiny_freeing_kong=random.choice(J)
			elif G==Locations.ChunkyKong:A.settings.chunky_freeing_kong=random.choice(B)
			E.remove(G);I=random.choice(D);H+=1
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
def FillKongsAndMoves(spoiler):
	'Fill kongs, then progression moves, then shared moves, then rest of moves.';A=spoiler;M=[];Q={};G=[]
	if A.settings.kong_rando:
		U=[ItemPool.ItemFromKong(B)for B in A.settings.starting_kong_list];R=[B for B in ItemPool.Kongs(A.settings)if B not in U];V={};J=[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]
		if any(A.settings.kong_locations):
			W=[B for B in J if B not in A.settings.kong_locations]
			for S in W:LocationList[S].PlaceItem(Items.NoItem);J.remove(S)
		for H in R:V[H]=J
		Reset();PlaceKongs(A,R,[A for A in J])
		if A.settings.kongs_for_progression and A.settings.shuffle_loading_zones!=_D and A.settings.move_rando!='start_with':
			b={};E=[A for A in J];B=[B for B in A.settings.starting_kong_list];K=A.settings.starting_kongs_count+1;F=1;O=_C
			while len(B)!=5:
				K=len(B)+1;D={};I=_A
				if A.settings.level_order[F]==Levels.FranticFactory and Locations.ChunkyKong in E and A.settings.chunky_freeing_kong in B:E.remove(Locations.ChunkyKong);I=ItemPool.GetKongForItem(LocationList[Locations.ChunkyKong].item)
				if A.settings.level_order[F]==Levels.JungleJapes and Locations.DiddyKong in E and A.settings.diddy_freeing_kong in B:
					E.remove(Locations.DiddyKong);I=ItemPool.GetKongForItem(LocationList[Locations.DiddyKong].item);L=GetItemPrerequisites(A,LocationList[Locations.DiddyKong].item,B)
					for C in L:
						if C not in G:D[C]=GetValidLocationsForMove(A,C)
				if A.settings.level_order[F]==Levels.AngryAztec and Locations.TinyKong in E and A.settings.tiny_freeing_kong in B:
					E.remove(Locations.TinyKong);I=ItemPool.GetKongForItem(LocationList[Locations.TinyKong].item);L=GetItemPrerequisites(A,LocationList[Locations.TinyKong].item,B)
					for C in L:
						if C not in G:D[C]=GetValidLocationsForMove(A,C)
				elif A.settings.level_order[F]==Levels.AngryAztec and Locations.LankyKong in E and A.settings.lanky_freeing_kong in B and(Kongs.diddy in B or A.settings.open_levels or Kongs.donkey in B and A.settings.activate_all_bananaports==_D)and(Kongs.donkey in B or Kongs.lanky in B or Kongs.tiny in B):
					E.remove(Locations.LankyKong);I=ItemPool.GetKongForItem(LocationList[Locations.LankyKong].item);L=GetItemPrerequisites(A,LocationList[Locations.LankyKong].item,B)
					for C in L:
						if C not in G:D[C]=GetValidLocationsForMove(A,C)
				while any(D):
					BlockAccessToLevel(A.settings,K);Reset();X=list(D.keys());P=ItemPool.OwnedKongMoves(B).copy()
					for H in D.keys():P.remove(H)
					for H in G:P.remove(H)
					N=PlaceItems(A.settings,_G,X,ownedItems=P,validLocations=D,isPriorityMove=_B)
					if N>0:raise Ex.ItemPlacementException('Failed to place items that would unlock Kong number '+str(len(B)+1)+', '+I.name)
					G.extend(list(D.keys()));T={}
					for H in list(D.keys()):
						Y=GetItemPrerequisites(A,H,B)
						for C in Y:
							if C not in G:T[C]=GetValidLocationsForMove(A,C)
					D=T
				if I is not _A:B.append(I);O=_C
				else:
					if F==K and O:raise Ex.ItemPlacementException('Kongs logically locked behind themselves. Only '+str(len(B))+' kongs logically accessible.')
					elif F==K:O=_B
					F=F%K+1
				BlockAccessToLevel(A.settings,100)
	if A.settings.shuffle_items=='moves':Z,a=ShuffleSharedMoves(A);M.extend(Z);Q.update(a)
	Reset();M=[A for A in M if A not in G];N=PlaceItems(A.settings,_G,M,[],validLocations=Q)
	if N>0:raise Ex.ItemPlacementException(str(N)+' unplaced items.')
def FillKongsAndMovesForLevelOrder(spoiler):
	'Shuffle Kongs and Moves accounting for level order restrictions.';A=spoiler;B=0
	while _B:
		try:
			ItemPool.PlaceConstants(A.settings);WipeProgressionRequirements(A.settings);A.settings.kongs_for_progression=_B;FillKongsAndMoves(A);SetNewProgressionRequirements(A.settings);A.settings.kongs_for_progression=_C
			if not VerifyWorldWithWorstCoinUsage(A.settings):raise Ex.GameNotBeatableException(_H)
			return
		except Ex.FillException as C:
			Reset();Logic.ClearAllLocations();B+=1
			if B==20:js.postMessage(_I);raise C
			if B%5==0:
				js.postMessage('Retrying fill really hard. Tries: '+str(B));A.settings.shuffle_prices()
				if A.settings.shuffle_loading_zones==_K:ShuffleExits.ShuffleExits(A.settings);A.UpdateExits()
			else:js.postMessage(_J+str(B))
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
	'Set new progression requirements based on what is owned or accessible heading into each level.';A=settings;B=[];C=[];J={};H={}
	if A.unlock_all_moves:D=ItemPool.DonkeyMoves.copy();D.extend(ItemPool.DiddyMoves);D.extend(ItemPool.LankyMoves);D.extend(ItemPool.TinyMoves);D.extend(ItemPool.ChunkyMoves);D.extend(ItemPool.ImportantSharedMoves)
	for K in range(1,8):
		BlockAccessToLevel(A,K);Reset();L=GetAccessibleLocations(A,[]);I=GetLevelShuffledToIndex(K-1);B.append(LogicVariables.ColoredBananas[I]);C.append(LogicVariables.GoldenBananas);J[I]=LogicVariables.GetKongs()
		if A.unlock_all_moves:H[I]=D
		else:M=[LocationList[A].item for A in L if LocationList[A].type==Types.Shop and LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A];H[I]=M
	E=0.4;F=0.7;A.EntryGBs=[min(A.blocker_0,1),min(A.blocker_1,max(1,round(random.uniform(E,F)*C[0]))),min(A.blocker_2,max(1,round(random.uniform(E,F)*C[1]))),min(A.blocker_3,max(1,round(random.uniform(E,F)*C[2]))),min(A.blocker_4,max(1,round(random.uniform(E,F)*C[3]))),min(A.blocker_5,max(1,round(random.uniform(E,F)*C[4]))),min(A.blocker_6,max(1,round(random.uniform(E,F)*C[5]))),A.blocker_7]
	if A.randomize_blocker_required_amounts:
		for G in range(1,7):
			if A.EntryGBs[G]>A.EntryGBs[G+1]:N=A.EntryGBs[G];A.EntryGBs[G]=A.EntryGBs[G+1];A.EntryGBs[G+1]=N
	A.BossBananas=[min(A.troff_0,sum(B[0]),round(A.troff_0/(A.troff_max*A.troff_weight_0)*sum(B[0]))),min(A.troff_1,sum(B[1]),round(A.troff_1/(A.troff_max*A.troff_weight_1)*sum(B[1]))),min(A.troff_2,sum(B[2]),round(A.troff_2/(A.troff_max*A.troff_weight_2)*sum(B[2]))),min(A.troff_3,sum(B[3]),round(A.troff_3/(A.troff_max*A.troff_weight_3)*sum(B[3]))),min(A.troff_4,sum(B[4]),round(A.troff_4/(A.troff_max*A.troff_weight_4)*sum(B[4]))),min(A.troff_5,sum(B[5]),round(A.troff_5/(A.troff_max*A.troff_weight_5)*sum(B[5]))),min(A.troff_6,sum(B[6]),round(A.troff_6/(A.troff_max*A.troff_weight_6)*sum(B[6])))];ShuffleExits.UpdateLevelProgression(A);ShuffleBossesBasedOnOwnedItems(A,J,H);A.owned_kongs_by_level=J;A.owned_moves_by_level=H
def BlockAccessToLevel(settings,level):
	'Assume the level index passed in is the furthest level you have access to in the level order.';A=settings
	for B in range(0,7):
		if B>=level:A.EntryGBs[B]=1000;A.BossBananas[B]=1000
		else:A.EntryGBs[B]=0;A.BossBananas[B]=0
	ShuffleExits.UpdateLevelProgression(A)
def Generate_Spoiler(spoiler):
	'Generate a complete spoiler based on input settings.';A=spoiler;global LogicVariables;LogicVariables=LogicVarHolder(A.settings);InitKasplatMap(LogicVariables)
	if A.settings.kongs_for_progression:
		if A.settings.shuffle_loading_zones==_K:ShuffleExits.ShuffleExits(A.settings);A.UpdateExits()
		WipeProgressionRequirements(A.settings);ShuffleMisc(A);FillKongsAndMovesForLevelOrder(A)
	else:
		ShuffleMisc(A)
		if A.settings.shuffle_loading_zones!='none':ShuffleExits.ExitShuffle(A.settings);A.UpdateExits()
		if A.settings.shuffle_items==_D:Fill(A)
		elif A.settings.shuffle_items=='moves'or A.settings.kong_rando:FillKongsAndMovesGeneric(A)
		else:
			ItemPool.PlaceConstants(A.settings)
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.VanillaItemsGameNotBeatableException('Game unbeatable.')
	GeneratePlaythrough(A)
	if A.settings.wrinkly_hints in['standard','cryptic']:compileHints(A)
	Reset();ShuffleExits.Reset();return A
def ShuffleMisc(spoiler):
	'Shuffle miscellaneous objects outside of main fill algorithm, including Kasplats, Bonus barrels, and bananaport warps.';A=spoiler;KasplatShuffle(A,LogicVariables);A.human_kasplats={};A.UpdateKasplats(LogicVariables.kasplat_map)
	if A.settings.bonus_barrels in(_F,'selected'):BarrelShuffle(A.settings);A.UpdateBarrels()
	if A.settings.bananaport_rando:C=[];D={};ShuffleWarps(C,D);A.bananaport_replacements=C.copy();A.human_warp_locations=D
	if A.settings.random_patches:G=[];A.human_patches=ShufflePatches(A,G).copy()
	if A.settings.shuffle_shops:ShuffleShopLocations(A)
	if A.settings.activate_all_bananaports in[_D,'isles']:
		H=set([BananaportVanilla[A].map_id for A in Warps])
		for E in H:
			I=[BananaportVanilla[A]for A in Warps if BananaportVanilla[A].map_id==E]
			for B in I:
				F=[BananaportVanilla[A]for A in Warps if BananaportVanilla[A].map_id==E and BananaportVanilla[A].new_warp==B.new_warp and BananaportVanilla[A].name!=B.name][0]
				if B.region_id!=F.region_id and(A.settings.activate_all_bananaports==_D or B.map_id==Maps.Isles):J=Logic.Regions[B.region_id];K=TransitionFront(F.region_id,lambda l:_B);J.exits.append(K)