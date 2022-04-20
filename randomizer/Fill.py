'Module used to distribute items randomly.'
_H='Fill failed. Retrying. Tries: '
_G='Fill failed, out of retries.'
_F='Game unbeatable after placing all items.'
_E='random'
_D='assumed'
_C=False
_B=True
_A=None
import random,js,randomizer.ItemPool as ItemPool,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic,randomizer.ShuffleExits as ShuffleExits
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.Enums.SearchMode import SearchMode
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Lists.Item import ItemList
from randomizer.Lists.Location import Location,LocationList
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Logic import LogicVarHolder,LogicVariables,STARTING_SLAM
from randomizer.LogicClasses import TransitionFront
from randomizer.Prices import GetPriceOfMoveItem
from randomizer.ShuffleBarrels import BarrelShuffle
from randomizer.ShuffleKasplats import KasplatShuffle
from randomizer.ShuffleWarps import ShuffleWarps
def GetExitLevelExit(settings,region):
	'Get the exit that using the "Exit Level" button will take you to.';A=region.level
	if A==Levels.JungleJapes:return ShuffleExits.ShufflableExits[Transitions.JapesToIsles].shuffledId
	elif A==Levels.AngryAztec:return ShuffleExits.ShufflableExits[Transitions.AztecToIsles].shuffledId
	elif A==Levels.FranticFactory:return ShuffleExits.ShufflableExits[Transitions.FactoryToIsles].shuffledId
	elif A==Levels.GloomyGalleon:return ShuffleExits.ShufflableExits[Transitions.GalleonToIsles].shuffledId
	elif A==Levels.FungiForest:return ShuffleExits.ShufflableExits[Transitions.ForestToIsles].shuffledId
	elif A==Levels.CrystalCaves:return ShuffleExits.ShufflableExits[Transitions.CavesToIsles].shuffledId
	elif A==Levels.CreepyCastle:return ShuffleExits.ShufflableExits[Transitions.CastleToIsles].shuffledId
def GetAccessibleLocations(settings,ownedItems,searchType=SearchMode.GetReachable):
	'Search to find all reachable locations given owned items.';R=ownedItems;N=settings;D=searchType;F=[];G=[];S=[];O=_B
	while len(G)>0 or O:
		H=[]
		for L in G:
			F.append(L);A=LocationList[L]
			if A.item is not _A:
				R.append(A.item)
				if D==SearchMode.GeneratePlaythrough and ItemList[A.item].playthrough:
					if A.item==Items.BananaHoard:H=[L];break
					H.append(L)
				if D==SearchMode.CheckBeatable and A.item==Items.BananaHoard:return _B
		if len(H)>0:
			S.append(H)
			if LocationList[H[0]].item==Items.BananaHoard:break
		O=_C;G=[];LogicVariables.Update(R)
		for M in LogicVariables.GetKongs():
			LogicVariables.SetKong(M);T=Logic.Regions[Regions.IslesMain];T.id=Regions.IslesMain;I=[T];E=[Regions.IslesMain];U=[(A,B)for(A,B)in Logic.Regions.items()if B.HasAccess(M)and A not in E];E.extend([A[0]for A in U]);I.extend([A[1]for A in U])
			while len(I)>0:
				B=I.pop();B.UpdateAccess(M,LogicVariables);LogicVariables.UpdateCurrentRegionAccess(B)
				for P in B.events:
					if P.name not in LogicVariables.Events and P.logic(LogicVariables):O=_B;LogicVariables.Events.append(P.name)
				if B.id in Logic.CollectibleRegions.keys():
					for J in Logic.CollectibleRegions[B.id]:
						if not J.added and(M==J.kong or J.kong==Kongs.any)and J.logic(LogicVariables):LogicVariables.AddCollectible(J,B.level)
				for A in B.locations:
					if A.logic(LogicVariables)and A.id not in G and A.id not in F:
						if A.bonusBarrel and N.bonus_barrels!='skip':
							X=BarrelMetaData[A.id].minigame
							if not MinigameRequirements[X].logic(LogicVariables):continue
						elif LocationList[A.id].type==Types.Blueprint:
							if not LogicVariables.KasplatAccess(A.id):continue
						elif LocationList[A.id].type==Types.Shop and A.id!=Locations.SimianSlam:LogicVariables.PurchaseShopItem(LocationList[A.id])
						G.append(A.id)
				V=B.exits.copy()
				if N.shuffle_loading_zones and B.level!=Levels.DKIsles and B.level!=Levels.Shops:
					W=GetExitLevelExit(N,B)
					if W is not _A:Y=ShuffleExits.ShufflableExits[W].back.regionId;V.append(TransitionFront(Y,lambda l:_B))
				for exit in V:
					C=exit.dest
					if exit.exitShuffleId is not _A and not exit.assumed:
						Q=ShuffleExits.ShufflableExits[exit.exitShuffleId]
						if Q.shuffled:C=ShuffleExits.ShufflableExits[Q.shuffledId].back.regionId
						elif Q.toBeShuffled and not exit.assumed:continue
					if C not in E and exit.logic(LogicVariables):E.append(C);K=Logic.Regions[C];K.id=C;I.append(K)
				if B.deathwarp is not _A:
					C=B.deathwarp.dest
					if C not in E and B.deathwarp.logic(LogicVariables):E.append(C);K=Logic.Regions[C];K.id=C;I.append(K)
	if D==SearchMode.GetReachable:return F
	elif D==SearchMode.CheckBeatable:return _C
	elif D==SearchMode.GeneratePlaythrough:return S
	elif D==SearchMode.CheckAllReachable:return len(F)==len(LocationList)
	elif D==SearchMode.GetUnreachable:return[A for A in LocationList if A not in F]
def VerifyWorld(settings):'Make sure all item locations are reachable on current world graph with constant items placed and all other items owned.';A=settings;ItemPool.PlaceConstants(A);B=GetAccessibleLocations(A,ItemPool.AllItems(A),SearchMode.GetUnreachable);C=len(B)==0;Reset();return C
def Reset():'Reset logic variables and region info that should be reset before a search.';LogicVariables.Reset();Logic.ResetRegionAccess();Logic.ResetCollectibleRegions()
def ParePlaythrough(settings,PlaythroughLocations):
	'Pares playthrough down to only the essential elements.';A=PlaythroughLocations;F=[]
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
def RandomFill(itemsToPlace,validLocations):
	'Randomly place given items in any location disregarding logic.';A=itemsToPlace;random.shuffle(A);B=[]
	for (id,C) in LocationList.items():
		if C.item is _A and id in validLocations:B.append(id)
	random.shuffle(B)
	while len(A)>0:
		if len(B)==0:return len(A)
		D=A.pop();E=B.pop();LocationList[E].PlaceItem(D)
	return 0
def ForwardFill(settings,itemsToPlace,validLocations,ownedItems=[]):
	'Forward fill algorithm for item placement.';C=ownedItems;B=itemsToPlace;random.shuffle(B);C=C.copy()
	while len(B)>0:
		A=GetAccessibleLocations(settings,C.copy());A=[B for B in A if LocationList[B].item is _A and B in validLocations]
		if len(A)==0:return len(B)
		random.shuffle(A);E=A.pop();D=B.pop();C.append(D);LocationList[E].PlaceItem(D)
	return 0
def GetItemValidLocations(validLocations,item):
	'Get the list of valid locations for this item.';A=validLocations;B=A
	if isinstance(A,dict):
		for C in A.keys():
			if item==C:B=A[C];break
			B=[A for A in LocationList]
	return B
def AssumedFill(settings,itemsToPlace,validLocations,ownedItems=[]):
	'Assumed fill algorithm for item placement.';Q='Failed placing item ';K=ownedItems;J=validLocations;F=settings;B=itemsToPlace;L=GetMaxCoinsSpent(F,B+K);random.shuffle(B)
	while len(B)>0:
		C=B.pop(0);M=_C;A=B.copy();A.extend(K);U=sum((1 for B in A if B==Items.ProgressiveSlam))+STARTING_SLAM;V=sum((1 for B in A if B==Items.ProgressiveAmmoBelt));W=sum((1 for B in A if B==Items.ProgressiveInstrumentUpgrade));X=GetItemValidLocations(J,C);Reset();H=GetAccessibleLocations(F,A);D=[A for A in H if LocationList[A].item is _A and A in X]
		if len(D)==0:print(Q+ItemList[C].name+', no valid reachable locations without this item.');R=[ItemList[B].name for B in A if ItemList[B].type==Types.Kong];R.insert(0,F.starting_kong.name);Y=[ItemList[B].name for B in A if ItemList[B].type==Types.Shop];Z=len([B for B in A if ItemList[B].type==Types.Banana]);js.postMessage('Current Moves owned at failure: '+str(Y)+' with GB count: '+str(Z)+' and kongs freed: '+str(R));return len(B)+1
		if ItemList[C].type==Types.Shop:
			N=ItemList[C].kong;G=GetPriceOfMoveItem(C,F,U,V,W);O=[0,0,0,0,0]
			if G is not _A:
				if N==Kongs.any:
					for S in range(5):L[S]-=G;O[S]=G
				else:L[N]-=G;O[N]=G
		random.shuffle(D)
		for P in D:
			LocationList[P].PlaceItem(C);A=B.copy();A.extend(K);Reset();H=GetAccessibleLocations(F,A);I=_B
			for a in B:
				b=GetItemValidLocations(J,a);D=[A for A in H if A in b]
				if len(D)==0:js.postMessage(Q+ItemList[C].name+' in location '+LocationList[P].name+', due to too few remaining locations in play');I=_C;break
				H.remove(D[0])
			if I and ItemList[C].type==Types.Shop:
				T=[0,0,0,0,0]
				for E in range(5):T[E]=LogicVariables.Coins[E]-L[E]
				for E in range(5):
					if T[E]<O[E]:I=_C
			if not I:LocationList[P].item=_A;M=_C;continue
			else:M=_B;break
		if not M:js.postMessage(Q+ItemList[C].name+' in any of remaining '+str(len(J))+' possible locations');return len(B)+1
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
def PlaceItems(settings,algorithm,itemsToPlace,ownedItems=[],validLocations=[]):
	'Places items using given algorithm.';E=ownedItems;D=settings;C=itemsToPlace;B=algorithm;A=validLocations
	if len(A)==0:A=[A for A in LocationList]
	if B==_D:return AssumedFill(D,C,A,E)
	elif B=='forward':return ForwardFill(D,C,A,E)
	elif B==_E:return RandomFill(C,A)
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
			I=ItemPool.ExcessItems(A.settings);F=PlaceItems(A.settings,_E,ItemPool.ExcessItems(A.settings))
			if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced excess items.')
			Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_F)
			Reset();G=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,G);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,G);return A
		except Ex.FillException as H:
			if B==4:js.postMessage(_G);raise H
			else:B+=1;js.postMessage(_H+str(B));Reset();Logic.ClearAllLocations()
def ShuffleMoves(spoiler):
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
def ShuffleMisc(spoiler):
	'Facilitate shuffling individual pools of items in lieu of full item rando.';A=spoiler;C=0
	while _B:
		try:
			D=[];E={}
			if A.settings.shuffle_items=='moves':I,J=ShuffleMoves(A);D.extend(I);E.update(J)
			if A.settings.kong_rando:
				F=ItemPool.Kongs(A.settings);G={};K=[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]
				for L in F:G[L]=K
				Reset();B=PlaceItems(A.settings,_D,F,ownedItems=D,validLocations=G)
				if B>0:raise Ex.ItemPlacementException(str(B)+' unplaced kongs.')
			Reset();B=PlaceItems(A.settings,_D,D,validLocations=E)
			if B>0:raise Ex.ItemPlacementException(str(B)+' unplaced items.')
			Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_F)
			Reset();H=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,H);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,H);return A
		except Ex.FillException as M:
			if C==20:js.postMessage(_G);raise M
			else:C+=1;js.postMessage(_H+str(C));Reset();Logic.ClearAllLocations()
def Generate_Spoiler(spoiler):
	'Generate a complete spoiler based on input settings.';A=spoiler;global LogicVariables;LogicVariables=LogicVarHolder(A.settings);KasplatShuffle(LogicVariables);A.human_kasplats={};A.UpdateKasplats(LogicVariables.kasplat_map)
	if A.settings.bonus_barrels==_E:BarrelShuffle(A.settings);A.UpdateBarrels()
	if A.settings.shuffle_loading_zones!='none':ShuffleExits.ExitShuffle(A.settings);A.UpdateExits()
	if A.settings.bananaport_rando:B=[];C={};ShuffleWarps(B,C);A.bananaport_replacements=B.copy();A.human_warp_locations=C
	if A.settings.shuffle_items=='all':Fill(A)
	elif A.settings.shuffle_items=='moves'or A.settings.kong_rando:ShuffleMisc(A)
	else:
		ItemPool.PlaceConstants(A.settings)
		if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.VanillaItemsGameNotBeatableException('Game unbeatable.')
	Reset();ShuffleExits.Reset();return A