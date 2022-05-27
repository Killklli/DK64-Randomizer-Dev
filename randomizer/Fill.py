'Module used to distribute items randomly.'
_I='moves'
_H='Retrying fill. Tries: '
_G='Fill failed, out of retries.'
_F='Game unbeatable after placing all items.'
_E='random'
_D='assumed'
_C=False
_B=True
_A=None
import random,js
from randomizer.Enums.MinigameType import MinigameType
import randomizer.ItemPool as ItemPool,randomizer.Lists.Exceptions as Ex
from randomizer.Lists.ShufflableExit import GetLevelShuffledToIndex,GetShuffledLevelIndex
import randomizer.Logic as Logic
from randomizer.Settings import Settings
import randomizer.ShuffleExits as ShuffleExits
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.Enums.SearchMode import SearchMode
from randomizer.Enums.Time import Time
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Lists.Item import ItemList,KongFromItem
from randomizer.Lists.Location import LocationList
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Logic import LogicVarHolder,LogicVariables,STARTING_SLAM
from randomizer.LogicClasses import TransitionFront
from randomizer.Prices import GetMaxForKong,GetPriceOfMoveItem
from randomizer.ShuffleBarrels import BarrelShuffle
from randomizer.ShuffleKasplats import InitKasplatMap,KasplatShuffle
from randomizer.ShuffleWarps import ShuffleWarps
from randomizer.ShuffleBosses import ShuffleBossesBasedOnOwnedItems
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
def GetAccessibleLocations(settings,ownedItems,searchType=SearchMode.GetReachable,purchaseList=_A):
	'Search to find all reachable locations given owned items.';Z='skip';U=ownedItems;R=settings;N=purchaseList;D=searchType
	if N is _A:N=[]
	G=[];H=[];V=[];I=_B
	while len(H)>0 or I:
		J=[]
		for E in H:
			G.append(E);A=LocationList[E]
			if A.item is not _A:
				if A.type==Types.Shop and E!=Locations.SimianSlam and D==SearchMode.GetReachableWithControlledPurchases and E not in N:continue
				U.append(A.item)
				if D==SearchMode.GeneratePlaythrough and ItemList[A.item].playthrough:
					if A.item==Items.BananaHoard:J=[E];break
					J.append(E)
				if D==SearchMode.CheckBeatable and A.item==Items.BananaHoard:return _B
		if len(J)>0:
			V.append(J)
			if LocationList[J[0]].item==Items.BananaHoard:break
		I=_C;H=[];LogicVariables.Update(U)
		for O in LogicVariables.GetKongs():
			LogicVariables.SetKong(O);P=Logic.Regions[Regions.IslesMain];P.id=Regions.IslesMain;P.dayAccess=_B;P.nightAccess=Events.Night in LogicVariables.Events;K=[P];F=[Regions.IslesMain];W=[(A,B)for(A,B)in Logic.Regions.items()if B.HasAccess(O)and A not in F];F.extend([A[0]for A in W]);K.extend([A[1]for A in W])
			while len(K)>0:
				B=K.pop();B.UpdateAccess(O,LogicVariables);LogicVariables.UpdateCurrentRegionAccess(B)
				for L in B.events:
					if L.name not in LogicVariables.Events and L.logic(LogicVariables):I=_B;LogicVariables.Events.append(L.name)
					if L.name==Events.Night and L.logic(LogicVariables):B.nightAccess=_B
				if B.id in Logic.CollectibleRegions.keys():
					for Q in Logic.CollectibleRegions[B.id]:
						if not Q.added and Q.kong in(O,Kongs.any)and Q.logic(LogicVariables):LogicVariables.AddCollectible(Q,B.level)
				for A in B.locations:
					if A.logic(LogicVariables)and A.id not in H and A.id not in G:
						if A.bonusBarrel is MinigameType.BonusBarrel and R.bonus_barrels!=Z or A.bonusBarrel is MinigameType.HelmBarrel and R.helm_barrels!=Z:
							a=BarrelMetaData[A.id].minigame
							if not MinigameRequirements[a].logic(LogicVariables):continue
						elif LocationList[A.id].type==Types.Blueprint:
							if not LogicVariables.KasplatAccess(A.id):continue
						elif LocationList[A.id].type==Types.Shop and A.id!=Locations.SimianSlam:
							if D!=SearchMode.GetReachableWithControlledPurchases or A.id in N:LogicVariables.PurchaseShopItem(LocationList[A.id])
						elif A.id==Locations.NintendoCoin:LogicVariables.Coins[Kongs.donkey]-=2
						H.append(A.id)
				X=B.exits.copy()
				if R.shuffle_loading_zones and B.level!=Levels.DKIsles and B.level!=Levels.Shops:
					Y=GetExitLevelExit(B)
					if Y is not _A:b=ShuffleExits.ShufflableExits[Y].back.regionId;X.append(TransitionFront(b,lambda l:_B))
				for exit in X:
					C=exit.dest
					if exit.exitShuffleId is not _A and not exit.assumed:
						S=ShuffleExits.ShufflableExits[exit.exitShuffleId]
						if S.shuffled:C=ShuffleExits.ShufflableExits[S.shuffledId].back.regionId
						elif S.toBeShuffled and not exit.assumed:continue
					if C not in F and exit.logic(LogicVariables):
						T=_B
						if exit.time==Time.Night and not B.nightAccess:T=_C
						elif exit.time==Time.Day and not B.dayAccess:T=_C
						if T:F.append(C);M=Logic.Regions[C];M.id=C;K.append(M)
					if exit.logic(LogicVariables):
						if B.dayAccess and exit.time!=Time.Night and not Logic.Regions[C].dayAccess:Logic.Regions[C].dayAccess=_B;I=_B
						if B.nightAccess and exit.time!=Time.Day and not Logic.Regions[C].nightAccess:Logic.Regions[C].nightAccess=_B;I=_B
				if B.deathwarp is not _A:
					C=B.deathwarp.dest
					if C not in F and B.deathwarp.logic(LogicVariables):F.append(C);M=Logic.Regions[C];M.id=C;K.append(M)
	if D in(SearchMode.GetReachable,SearchMode.GetReachableWithControlledPurchases):return G
	elif D==SearchMode.CheckBeatable:return _C
	elif D==SearchMode.GeneratePlaythrough:return V
	elif D==SearchMode.CheckAllReachable:return len(G)==len(LocationList)
	elif D==SearchMode.GetUnreachable:return[A for A in LocationList if A not in G]
def VerifyWorld(settings):'Make sure all item locations are reachable on current world graph with constant items placed and all other items owned.';A=settings;ItemPool.PlaceConstants(A);B=GetAccessibleLocations(A,ItemPool.AllItems(A),SearchMode.GetUnreachable);C=len(B)==0;Reset();return C
def VerifyWorldWithWorstCoinUsage(settings):
	'Make sure the game is beatable without it being possible to run out of coins for required moves.';B=settings;D=[];H=[];N=[GetMaxForKong(B,Kongs.donkey),GetMaxForKong(B,Kongs.diddy),GetMaxForKong(B,Kongs.lanky),GetMaxForKong(B,Kongs.tiny),GetMaxForKong(B,Kongs.chunky)]
	while _B:
		Reset();H=GetAccessibleLocations(B,[],SearchMode.GetReachableWithControlledPurchases,D);O=[LocationList[A].item for A in D];P=GetMaxCoinsSpent(B,O);F=[N[A]-P[A]for A in range(0,5)];E=LogicVariables.Coins.copy()
		if E[Kongs.donkey]>=F[Kongs.donkey]and E[Kongs.diddy]>=F[Kongs.diddy]and E[Kongs.lanky]>=F[Kongs.lanky]and E[Kongs.tiny]>=F[Kongs.tiny]and E[Kongs.chunky]>=F[Kongs.chunky]:Reset();return _B
		if len([A for A in H if LocationList[A].item==Items.BananaHoard])>0:Reset();return _B
		K=[A for A in H if LocationList[A].type==Types.Shop and LocationList[A].item is not _A and LocationList[A].item!=Items.NoItem and A not in D and LogicVariables.CanBuy(A)];I={};G={}
		if len(K)==0:print('Seed is invalid, coin locked with purchase order: '+str([LocationList[A].name+': '+LocationList[A].item.name+', 'for A in D]));Reset();return _C
		C=_A
		for A in K:
			L=D.copy();L.append(A);Reset();Q=GetAccessibleLocations(B,[],SearchMode.GetReachableWithControlledPurchases,L);R=LogicVariables.Coins.copy();M=[0,0,0,0,0]
			for J in LogicVariables.GetKongs():M[J]=R[J]-E[J]
			I[A]=M;G[A]=[LocationList[A].item for A in Q if A not in H and LocationList[A].item is not _A]
			if C is _A:C=A;continue
			if len([B for B in I[A]if B<0])==0:continue
			S=len([A for A in G[C]if ItemList[A].type==Types.Kong]);T=len([B for B in G[A]if ItemList[B].type==Types.Kong])
			if T>S:continue
			U=len([A for A in G[C]if ItemList[A].type==Types.Key]);V=len([B for B in G[A]if ItemList[B].type==Types.Key])
			if V>U:continue
			W=sum(list(I[C]));X=sum(list(I[A]))
			if X<W:C=A
		D.append(C)
def Reset():'Reset logic variables and region info that should be reset before a search.';LogicVariables.Reset();Logic.ResetRegionAccess();Logic.ResetCollectibleRegions()
def ParePlaythrough(settings,PlaythroughLocations):
	'Pare playthrough down to only the essential elements.';A=PlaythroughLocations;F=[]
	for E in range(len(A)-2,-1,-1):
		B=A[E]
		for C in B.copy():
			D=LocationList[C];G=D.item;D.item=_A;Reset()
			if GetAccessibleLocations(settings,[],SearchMode.CheckBeatable):B.remove(C);D.SetDelayedItem(G);F.append(C)
			else:D.PlaceItem(G)
	for E in range(len(A)-2,-1,-1):
		B=A[E]
		if len(B)==0:A.remove(B)
	for C in F:LocationList[C].PlaceDelayedItem()
def PareWoth(settings,PlaythroughLocations):
	'Pare playthrough to locations which are Way of the Hoard (hard required by logic).';A=[]
	for D in PlaythroughLocations:
		for E in [A for A in D if not LocationList[A].constant]:A.append(E)
	for F in range(len(A)-2,-1,-1):
		C=A[F];B=LocationList[C];G=B.item;B.item=_A;Reset()
		if GetAccessibleLocations(settings,[],SearchMode.CheckBeatable):A.remove(C)
		B.PlaceItem(G)
	return A
def RandomFill(itemsToPlace,validLocations):
	'Randomly place given items in any location disregarding logic.';A=itemsToPlace;random.shuffle(A);B=[]
	for (id,C) in LocationList.items():
		if C.item is _A and id in validLocations:B.append(id)
	random.shuffle(B)
	while len(A)>0:
		if len(B)==0:return len(A)
		D=A.pop();E=B.pop();LocationList[E].PlaceItem(D)
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
def AssumedFill(settings,itemsToPlace,validLocations,ownedItems=_A):
	'Assumed fill algorithm for item placement.';a=' in location ';P=validLocations;O='Failed placing item ';J=ownedItems;F=itemsToPlace;C=settings
	if J is _A:J=[]
	Q=GetMaxCoinsSpent(C,F+J);random.shuffle(F)
	while len(F)>0:
		A=F.pop(0);R=_C;B=F.copy();B.extend(J);b=sum((1 for A in B if A==Items.ProgressiveSlam))+STARTING_SLAM;c=sum((1 for A in B if A==Items.ProgressiveAmmoBelt));d=sum((1 for A in B if A==Items.ProgressiveInstrumentUpgrade));e=GetItemValidLocations(P,A);Reset();N=GetAccessibleLocations(C,B);H=[A for A in N if LocationList[A].item is _A and A in e]
		if len(H)==0:
			print(O+ItemList[A].name+', no valid reachable locations without this item.');U=[ItemList[A].name for A in B if ItemList[A].type==Types.Kong];V=[]
			for f in C.starting_kong_list:V.append(f.name.capitalize())
			for (D,E) in enumerate(V):U.insert(D,E)
			g=[ItemList[A].name for A in B if ItemList[A].type==Types.Shop];h=len([A for A in B if ItemList[A].type==Types.Banana]);js.postMessage('Current Moves owned at failure: '+str(g)+' with GB count: '+str(h)+' and kongs freed: '+str(U));return len(F)+1
		random.shuffle(H)
		if ItemList[A].type==Types.Shop:
			S=ItemList[A].kong;K=GetPriceOfMoveItem(A,C,b,c,d);T=[0,0,0,0,0]
			if K is not _A:
				if S==Kongs.any:
					for W in range(5):Q[W]-=K;T[W]=K
				else:Q[S]-=K;T[S]=K
		elif ItemList[A].type==Types.Kong:
			I=[KongFromItem(A)for A in B if ItemList[A].type==Types.Kong]
			for (D,E) in enumerate(C.starting_kong_list):I.insert(D,E)
			X=KongFromItem(A)
			if X in I:I.remove(X)
			if C.kongs_for_progression:
				i=GetShuffledLevelIndex(Levels.JungleJapes);j=GetShuffledLevelIndex(Levels.AngryAztec);k=GetShuffledLevelIndex(Levels.FranticFactory);L={}
				for D in range(0,5):
					if D==i:L[Locations.DiddyKong]=D
					elif D==j:L[Locations.LankyKong]=D;L[Locations.TinyKong]=D
					elif D==k:L[Locations.ChunkyKong]=D
				H.sort(key=lambda x:L[x],reverse=_B)
		for G in H:
			LocationList[G].PlaceItem(A)
			if ItemList[A].type==Types.Kong:
				if G==Locations.DiddyKong:C.diddy_freeing_kong=random.choice(I)
				elif G==Locations.LankyKong:C.lanky_freeing_kong=random.choice(I)
				elif G==Locations.TinyKong:
					Y=list(set(I).intersection([Kongs.diddy,Kongs.chunky]))
					if len(Y)==0:js.postMessage(O+ItemList[A].name+a+LocationList[G].name+', due to no kongs being able to free them');M=_C;break
					C.tiny_freeing_kong=random.choice(Y)
				elif G==Locations.ChunkyKong:C.chunky_freeing_kong=random.choice(I)
			B=F.copy();B.extend(J);Reset();N=GetAccessibleLocations(C,B);M=_B
			for l in F:
				m=GetItemValidLocations(P,l);H=[A for A in N if A in m]
				if len(H)==0:js.postMessage(O+ItemList[A].name+a+LocationList[G].name+', due to too few remaining locations in play');M=_C;break
				N.remove(H[0])
			if M and ItemList[A].type==Types.Shop:
				Z=[0,0,0,0,0]
				for E in range(5):Z[E]=LogicVariables.Coins[E]-Q[E]
				for E in range(5):
					if Z[E]<T[E]:M=_C
			if not M:LocationList[G].item=_A;R=_C;continue
			R=_B;break
		if not R:js.postMessage(O+ItemList[A].name+' in any of remaining '+str(len(P))+' possible locations');return len(F)+1
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
def PlaceItems(settings,algorithm,itemsToPlace,ownedItems=_A,validLocations=_A):
	'Places items using given algorithm.';E=settings;D=itemsToPlace;C=algorithm;B=ownedItems;A=validLocations
	if B is _A:B=[]
	if A is _A:A=[]
	if len(A)==0:A=list(LocationList)
	if C==_D:return AssumedFill(E,D,A,B)
	elif C=='forward':return ForwardFill(E,D,A,B)
	elif C==_E:return RandomFill(D,A)
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
			H=ItemPool.ExcessItems(A.settings);F=PlaceItems(A.settings,_E,ItemPool.ExcessItems(A.settings))
			if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced excess items.')
			Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_F)
			return
		except Ex.FillException as G:
			if B==4:js.postMessage(_G);raise G
			B+=1;js.postMessage(_H+str(B));Reset();Logic.ClearAllLocations()
def ShuffleSharedMoves(spoiler):
	'Shuffles shared kong moves and then returns the remaining ones and their valid locations.';B=spoiler;ItemPool.PlaceConstants(B.settings);A=[];A.extend(ItemPool.DonkeyMoves);A.extend(ItemPool.DiddyMoves);A.extend(ItemPool.LankyMoves);A.extend(ItemPool.TinyMoves);A.extend(ItemPool.ChunkyMoves);C=PlaceItems(B.settings,_D,ItemPool.ImportantSharedMoves.copy(),[A for A in ItemPool.AllItems(B.settings)if A not in ItemPool.ImportantSharedMoves],ItemPool.SharedMoveLocations)
	if C>0:raise Ex.ItemPlacementException(str(C)+' unplaced shared important items.')
	D=PlaceItems(B.settings,_E,ItemPool.JunkSharedMoves.copy(),validLocations=ItemPool.SharedMoveLocations)
	if D>0:raise Ex.ItemPlacementException(str(D)+' unplaced shared junk items.')
	E=[]
	for F in ItemPool.SharedMoveLocations:
		if LocationList[F].item is not _A:E.append(F)
	I=ItemPool.GetMoveLocationsToRemove(E);G={};J=[ItemPool.DonkeyMoves,ItemPool.DiddyMoves,ItemPool.LankyMoves,ItemPool.TinyMoves,ItemPool.ChunkyMoves];K=[ItemPool.DonkeyMoveLocations,ItemPool.DiddyMoveLocations,ItemPool.LankyMoveLocations,ItemPool.TinyMoveLocations,ItemPool.ChunkyMoveLocations]
	for H in range(5):
		for L in J[H]:G[L]=K[H]-I
	return A,G
def FillKongsAndMovesGeneric(spoiler):
	'Facilitate shuffling individual pools of items in lieu of full item rando.';B=spoiler;A=0
	while _B:
		try:
			FillKongsAndMoves(B);Reset()
			if not VerifyWorldWithWorstCoinUsage(B.settings):raise Ex.GameNotBeatableException(_F)
			return
		except Ex.FillException as C:
			if A==20:js.postMessage(_G);raise C
			A+=1;js.postMessage(_H+str(A));Reset();Logic.ClearAllLocations()
def GeneratePlaythrough(spoiler):'Generate playthrough and way of the hoard and update spoiler.';A=spoiler;Reset();B=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,B);C=PareWoth(A.settings,B);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,B);A.UpdateWoth(LocationList,C)
def FillKongsAndMoves(spoiler):
	'Fill shared moves, then kongs, then rest of moves.';A=spoiler;C=[];D={}
	if A.settings.shuffle_items==_I:G,H=ShuffleSharedMoves(A);C.extend(G);D.update(H)
	if A.settings.kong_rando:
		E=ItemPool.Kongs(A.settings);F={};I=[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]
		for J in E:F[J]=I
		Reset();B=PlaceItems(A.settings,_D,E,ownedItems=C,validLocations=F)
		if B>0:raise Ex.ItemPlacementException(str(B)+' unplaced kongs.')
	Reset();B=PlaceItems(A.settings,_D,C,validLocations=D)
	if B>0:raise Ex.ItemPlacementException(str(B)+' unplaced items.')
def FillKongsAndMovesForLevelOrder(spoiler):
	'Shuffle Kongs and Moves accounting for level order restrictions.';A=spoiler;ItemPool.PlaceConstants(A.settings);B=0
	while _B:
		try:
			WipeProgressionRequirements(A.settings);A.settings.kongs_for_progression=_B;FillKongsAndMoves(A);SetNewProgressionRequirements(A.settings);A.settings.kongs_for_progression=_C
			if not VerifyWorldWithWorstCoinUsage(A.settings):raise Ex.GameNotBeatableException(_F)
			return
		except Ex.FillException as C:
			if B==20:js.postMessage(_G);raise C
			B+=1;js.postMessage(_H+str(B));Reset();Logic.ClearAllLocations()
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
	A.diddy_freeing_kong=Kongs.any;A.lanky_freeing_kong=Kongs.any;A.tiny_freeing_kong=Kongs.any;A.chunky_freeing_kong=Kongs.any
def SetNewProgressionRequirements(settings):
	'Set new progression requirements based on what is owned or accessible heading into each level.';A=settings;B=[];C=[];I={};H={}
	if A.unlock_all_moves:D=ItemPool.DonkeyMoves.copy();D.extend(ItemPool.DiddyMoves);D.extend(ItemPool.LankyMoves);D.extend(ItemPool.TinyMoves);D.extend(ItemPool.ChunkyMoves);D.extend(ItemPool.ImportantSharedMoves)
	for J in range(1,8):
		BlockAccessToLevel(A,J);Reset();K=GetAccessibleLocations(A,[]);G=GetLevelShuffledToIndex(J-1);B.append(LogicVariables.ColoredBananas[G]);C.append(LogicVariables.GoldenBananas);I[G]=LogicVariables.GetKongs()
		if A.unlock_all_moves:H[G]=D
		else:L=[LocationList[A].item for A in K if LocationList[A].type==Types.Shop and LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A];H[G]=L
	E=0.4;F=0.7;A.EntryGBs=[min(A.blocker_0,1),min(A.blocker_1,max(1,round(random.uniform(E,F)*C[0]))),min(A.blocker_2,max(1,round(random.uniform(E,F)*C[1]))),min(A.blocker_3,max(1,round(random.uniform(E,F)*C[2]))),min(A.blocker_4,max(1,round(random.uniform(E,F)*C[3]))),min(A.blocker_5,max(1,round(random.uniform(E,F)*C[4]))),min(A.blocker_6,max(1,round(random.uniform(E,F)*C[5]))),A.blocker_7];A.BossBananas=[min(A.troff_0,round(A.troff_0/(A.troff_max*A.troff_weight_0)*sum(B[0]))),min(A.troff_1,round(A.troff_1/(A.troff_max*A.troff_weight_1)*sum(B[1]))),min(A.troff_2,round(A.troff_2/(A.troff_max*A.troff_weight_2)*sum(B[2]))),min(A.troff_3,round(A.troff_3/(A.troff_max*A.troff_weight_3)*sum(B[3]))),min(A.troff_4,round(A.troff_4/(A.troff_max*A.troff_weight_4)*sum(B[4]))),min(A.troff_5,round(A.troff_5/(A.troff_max*A.troff_weight_5)*sum(B[5]))),min(A.troff_6,round(A.troff_6/(A.troff_max*A.troff_weight_6)*sum(B[6])))];ShuffleExits.UpdateLevelProgression(A);ShuffleBossesBasedOnOwnedItems(A,I,H)
def BlockAccessToLevel(settings,level):
	'Assume the level index passed in is the furthest level you have access to in the level order.';A=settings
	for B in range(0,7):
		if B>=level:A.EntryGBs[B]=1000;A.BossBananas[B]=1000
		else:A.EntryGBs[B]=0;A.BossBananas[B]=0
	ShuffleExits.UpdateLevelProgression(A)
def Generate_Spoiler(spoiler):
	'Generate a complete spoiler based on input settings.';A=spoiler;global LogicVariables;LogicVariables=LogicVarHolder(A.settings);InitKasplatMap(LogicVariables)
	if A.settings.kongs_for_progression:
		if not A.settings.unlock_all_moves:A.settings.shuffle_items=_I
		A.settings.boss_location_rando=_B;A.settings.boss_kong_rando=_B
		if A.settings.shuffle_loading_zones=='levels':ShuffleExits.ShuffleLevelOrderWithRestrictions(A.settings);A.UpdateExits()
		WipeProgressionRequirements(A.settings);ShuffleMisc(A);FillKongsAndMovesForLevelOrder(A)
	else:
		if A.settings.shuffle_loading_zones!='none':ShuffleExits.ExitShuffle(A.settings);A.UpdateExits()
		ShuffleMisc(A)
		if A.settings.shuffle_items=='all':Fill(A)
		elif A.settings.shuffle_items==_I or A.settings.kong_rando:FillKongsAndMovesGeneric(A)
		else:
			ItemPool.PlaceConstants(A.settings)
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.VanillaItemsGameNotBeatableException('Game unbeatable.')
	GeneratePlaythrough(A);Reset();ShuffleExits.Reset();return A
def ShuffleMisc(spoiler):
	'Shuffle miscellaneous objects outside of main fill algorithm, including Kasplats, Bonus barrels, and bananaport warps.';A=spoiler;KasplatShuffle(LogicVariables);A.human_kasplats={};A.UpdateKasplats(LogicVariables.kasplat_map)
	if A.settings.bonus_barrels in(_E,'all_beaver_bother'):BarrelShuffle(A.settings);A.UpdateBarrels()
	if A.settings.bananaport_rando:B=[];C={};ShuffleWarps(B,C);A.bananaport_replacements=B.copy();A.human_warp_locations=C