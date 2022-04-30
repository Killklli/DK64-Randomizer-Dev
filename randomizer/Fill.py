'Module used to distribute items randomly.'
_I='moves'
_H='Fill failed. Retrying. Tries: '
_G='Fill failed, out of retries.'
_F='Game unbeatable after placing all items.'
_E='random'
_D='assumed'
_C=False
_B=True
_A=None
import random,js,randomizer.ItemPool as ItemPool,randomizer.Lists.Exceptions as Ex
from randomizer.Lists.ShufflableExit import GetLevelShuffledToIndex,GetShuffledLevelIndex
import randomizer.Logic as Logic
from randomizer.Settings import Settings
import randomizer.ShuffleExits as ShuffleExits
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.Enums.SearchMode import SearchMode
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Lists.Item import ItemList,KongFromItem
from randomizer.Lists.Location import LocationList
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Logic import LogicVarHolder,LogicVariables,STARTING_SLAM
from randomizer.LogicClasses import TransitionFront
from randomizer.Prices import GetPriceOfMoveItem
from randomizer.ShuffleBarrels import BarrelShuffle
from randomizer.ShuffleKasplats import KasplatShuffle
from randomizer.ShuffleWarps import ShuffleWarps
from randomizer.ShuffleBosses import ShuffleBossesBasedOnOwnedItems
def GetExitLevelExit(region):
	'Get the exit that using the "Exit Level" button will take you to.';A=region.level
	if A==Levels.JungleJapes:return ShuffleExits.ShufflableExits[Transitions.JapesToIsles].shuffledId
	elif A==Levels.AngryAztec:return ShuffleExits.ShufflableExits[Transitions.AztecToIsles].shuffledId
	elif A==Levels.FranticFactory:return ShuffleExits.ShufflableExits[Transitions.FactoryToIsles].shuffledId
	elif A==Levels.GloomyGalleon:return ShuffleExits.ShufflableExits[Transitions.GalleonToIsles].shuffledId
	elif A==Levels.FungiForest:return ShuffleExits.ShufflableExits[Transitions.ForestToIsles].shuffledId
	elif A==Levels.CrystalCaves:return ShuffleExits.ShufflableExits[Transitions.CavesToIsles].shuffledId
	elif A==Levels.CreepyCastle:return ShuffleExits.ShufflableExits[Transitions.CastleToIsles].shuffledId
def GetAccessibleLocations(settings,ownedItems,searchType=SearchMode.GetReachable):
	'Search to find all reachable locations given owned items.';R=ownedItems;Q=settings;D=searchType;F=[];G=[];S=[];N=_B
	while len(G)>0 or N:
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
		N=_C;G=[];LogicVariables.Update(R)
		for M in LogicVariables.GetKongs():
			LogicVariables.SetKong(M);T=Logic.Regions[Regions.IslesMain];T.id=Regions.IslesMain;I=[T];E=[Regions.IslesMain];U=[(A,B)for(A,B)in Logic.Regions.items()if B.HasAccess(M)and A not in E];E.extend([A[0]for A in U]);I.extend([A[1]for A in U])
			while len(I)>0:
				B=I.pop();B.UpdateAccess(M,LogicVariables);LogicVariables.UpdateCurrentRegionAccess(B)
				for O in B.events:
					if O.name not in LogicVariables.Events and O.logic(LogicVariables):N=_B;LogicVariables.Events.append(O.name)
				if B.id in Logic.CollectibleRegions.keys():
					for J in Logic.CollectibleRegions[B.id]:
						if not J.added and(M==J.kong or J.kong==Kongs.any)and J.logic(LogicVariables):LogicVariables.AddCollectible(J,B.level)
				for A in B.locations:
					if A.logic(LogicVariables)and A.id not in G and A.id not in F:
						if A.bonusBarrel and Q.bonus_barrels!='skip':
							X=BarrelMetaData[A.id].minigame
							if not MinigameRequirements[X].logic(LogicVariables):continue
						elif LocationList[A.id].type==Types.Blueprint:
							if not LogicVariables.KasplatAccess(A.id):continue
						elif LocationList[A.id].type==Types.Shop and A.id!=Locations.SimianSlam:LogicVariables.PurchaseShopItem(LocationList[A.id])
						G.append(A.id)
				V=B.exits.copy()
				if Q.shuffle_loading_zones and B.level!=Levels.DKIsles and B.level!=Levels.Shops:
					W=GetExitLevelExit(B)
					if W is not _A:Y=ShuffleExits.ShufflableExits[W].back.regionId;V.append(TransitionFront(Y,lambda l:_B))
				for exit in V:
					C=exit.dest
					if exit.exitShuffleId is not _A and not exit.assumed:
						P=ShuffleExits.ShufflableExits[exit.exitShuffleId]
						if P.shuffled:C=ShuffleExits.ShufflableExits[P.shuffledId].back.regionId
						elif P.toBeShuffled and not exit.assumed:continue
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
	'Assumed fill algorithm for item placement.';a=', due to no kongs being able to free them';V=' in location ';Q=ownedItems;P=validLocations;N='Failed placing item ';D=itemsToPlace;C=settings;R=GetMaxCoinsSpent(C,D+Q);random.shuffle(D)
	while len(D)>0:
		A=D.pop(0);S=_C;B=D.copy();B.extend(Q);b=sum((1 for A in B if A==Items.ProgressiveSlam))+STARTING_SLAM;c=sum((1 for A in B if A==Items.ProgressiveAmmoBelt));d=sum((1 for A in B if A==Items.ProgressiveInstrumentUpgrade));e=GetItemValidLocations(P,A);Reset();O=GetAccessibleLocations(C,B);F=[A for A in O if LocationList[A].item is _A and A in e]
		if len(F)==0:print(N+ItemList[A].name+', no valid reachable locations without this item.');W=[ItemList[A].name for A in B if ItemList[A].type==Types.Kong];W.insert(0,C.starting_kong.name);f=[ItemList[A].name for A in B if ItemList[A].type==Types.Shop];g=len([A for A in B if ItemList[A].type==Types.Banana]);js.postMessage('Current Moves owned at failure: '+str(f)+' with GB count: '+str(g)+' and kongs freed: '+str(W));return len(D)+1
		random.shuffle(F)
		if ItemList[A].type==Types.Shop:
			T=ItemList[A].kong;K=GetPriceOfMoveItem(A,C,b,c,d);U=[0,0,0,0,0]
			if K is not _A:
				if T==Kongs.any:
					for X in range(5):R[X]-=K;U[X]=K
				else:R[T]-=K;U[T]=K
		elif ItemList[A].type==Types.Kong:
			G=[KongFromItem(A)for A in B if ItemList[A].type==Types.Kong];G.insert(0,C.starting_kong);Y=KongFromItem(A)
			if Y in G:G.remove(Y)
			if C.kongs_for_progression:
				h=GetShuffledLevelIndex(Levels.JungleJapes);i=GetShuffledLevelIndex(Levels.AngryAztec);j=GetShuffledLevelIndex(Levels.FranticFactory);L={}
				for H in range(0,5):
					if H==h:L[Locations.DiddyKong]=H
					elif H==i:L[Locations.LankyKong]=H;L[Locations.TinyKong]=H
					elif H==j:L[Locations.ChunkyKong]=H
				F.sort(key=lambda x:L[x],reverse=_B)
		for E in F:
			LocationList[E].PlaceItem(A)
			if ItemList[A].type==Types.Kong:
				if E==Locations.DiddyKong:C.diddy_freeing_kong=random.choice(G)
				elif E==Locations.LankyKong:
					M=list(set(G).intersection([Kongs.donkey,Kongs.lanky,Kongs.tiny]))
					if len(M)==0:js.postMessage(N+ItemList[A].name+V+LocationList[E].name+a);I=_C;break
					C.lanky_freeing_kong=random.choice(M)
				elif E==Locations.TinyKong:
					M=list(set(G).intersection([Kongs.diddy,Kongs.chunky]))
					if len(M)==0:js.postMessage(N+ItemList[A].name+V+LocationList[E].name+a);I=_C;break
					C.tiny_freeing_kong=random.choice(M)
				elif E==Locations.ChunkyKong:C.chunky_freeing_kong=random.choice(G)
			B=D.copy();B.extend(Q);Reset();O=GetAccessibleLocations(C,B);I=_B
			for k in D:
				l=GetItemValidLocations(P,k);F=[A for A in O if A in l]
				if len(F)==0:js.postMessage(N+ItemList[A].name+V+LocationList[E].name+', due to too few remaining locations in play');I=_C;break
				O.remove(F[0])
			if I and ItemList[A].type==Types.Shop:
				Z=[0,0,0,0,0]
				for J in range(5):Z[J]=LogicVariables.Coins[J]-R[J]
				for J in range(5):
					if Z[J]<U[J]:I=_C
			if not I:LocationList[E].item=_A;S=_C;continue
			else:S=_B;break
		if not S:js.postMessage(N+ItemList[A].name+' in any of remaining '+str(len(P))+' possible locations');return len(D)+1
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
			ItemPool.PlaceConstants(A.settings);D=PlaceItems(A.settings,A.settings.algorithm,ItemPool.HighPriorityItems(A.settings),ItemPool.HighPriorityAssumedItems(A.settings))
			if D>0:raise Ex.ItemPlacementException(str(D)+' unplaced high priority items.')
			Reset();E=PlaceItems(A.settings,A.settings.algorithm,ItemPool.Blueprints(A.settings),ItemPool.BlueprintAssumedItems(A.settings))
			if E>0:raise Ex.ItemPlacementException(str(E)+' unplaced blueprints.')
			Reset();F=PlaceItems(A.settings,A.settings.algorithm,ItemPool.LowPriorityItems(A.settings),ItemPool.ExcessItems(A.settings))
			if F>0:raise Ex.ItemPlacementException(str(F)+' unplaced low priority items.')
			J=ItemPool.ExcessItems(A.settings);G=PlaceItems(A.settings,_E,ItemPool.ExcessItems(A.settings))
			if G>0:raise Ex.ItemPlacementException(str(G)+' unplaced excess items.')
			Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_F)
			Reset();C=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,C);H=PareWoth(A.settings,C);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,C);A.UpdateWoth(LocationList,H);return A
		except Ex.FillException as I:
			if B==4:js.postMessage(_G);raise I
			else:B+=1;js.postMessage(_H+str(B));Reset();Logic.ClearAllLocations()
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
def ShuffleMisc(spoiler):
	'Facilitate shuffling individual pools of items in lieu of full item rando.';A=spoiler;B=0
	while _B:
		try:
			FillKongsAndMoves(A);Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_F)
			Reset();C=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,C);D=PareWoth(A.settings,C);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,C);A.UpdateWoth(LocationList,D);return A
		except Ex.FillException as E:
			if B==20:js.postMessage(_G);raise E
			else:B+=1;js.postMessage(_H+str(B));Reset();Logic.ClearAllLocations()
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
def ShuffleKongsAndLevels(spoiler):
	'Shuffle Kongs and Levels simultaneously accounting for restrictions.';A=spoiler;ShuffleExits.ShuffleLevelOrderWithRestrictions(A.settings);A.UpdateExits();print('Starting Kong: '+A.settings.starting_kong.name);ItemPool.PlaceConstants(A.settings);B=0
	while _B:
		try:
			WipeProgressionRequirements(A.settings);FillKongsAndMoves(A);SetNewProgressionRequirements(A.settings);Reset()
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.GameNotBeatableException(_F)
			Reset();C=GetAccessibleLocations(A.settings,[],SearchMode.GeneratePlaythrough);ParePlaythrough(A.settings,C);D=PareWoth(A.settings,C);A.UpdateLocations(LocationList);A.UpdatePlaythrough(LocationList,C);A.UpdateWoth(LocationList,D);return A
		except Ex.FillException as E:
			if B==20:js.postMessage(_G);raise E
			else:B+=1;js.postMessage(_H+str(B));Reset();Logic.ClearAllLocations()
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
	'Set new progression requirements based on what is owned or accessible heading into each level.';A=settings;B=[];C=[];G={};F={}
	if A.unlock_all_moves:D=ItemPool.DonkeyMoves.copy();D.extend(ItemPool.DiddyMoves);D.extend(ItemPool.LankyMoves);D.extend(ItemPool.TinyMoves);D.extend(ItemPool.ChunkyMoves);D.extend(ItemPool.ImportantSharedMoves)
	for H in range(1,8):
		BlockAccessToLevel(A,H);Reset();I=GetAccessibleLocations(A,[]);E=GetLevelShuffledToIndex(H-1);B.append(LogicVariables.ColoredBananas[E]);C.append(LogicVariables.GoldenBananas);G[E]=LogicVariables.GetKongs()
		if A.unlock_all_moves:F[E]=D
		else:J=[LocationList[A].item for A in I if LocationList[A].type==Types.Shop and LocationList[A].item!=Items.NoItem and LocationList[A].item is not _A];F[E]=J
	A.EntryGBs=[min(A.blocker_0,1),min(A.blocker_1,C[0]),min(A.blocker_2,C[1]),min(A.blocker_3,C[2]),min(A.blocker_4,C[3]),min(A.blocker_5,C[4]),min(A.blocker_6,C[5]),A.blocker_7];A.BossBananas=[min(A.troff_0,sum(B[0])),min(A.troff_1,sum(B[1])),min(A.troff_2,sum(B[2])),min(A.troff_3,sum(B[3])),min(A.troff_4,sum(B[4])),min(A.troff_5,sum(B[5])),min(A.troff_6,sum(B[6]))];ShuffleExits.UpdateLevelProgression(A);ShuffleBossesBasedOnOwnedItems(A,G,F)
def BlockAccessToLevel(settings,level):
	'Assume the level index passed in is the furthest level you have access to in the level order.';A=settings
	for B in range(0,7):
		if B>=level:A.EntryGBs[B]=1000;A.BossBananas[B]=1000
		else:A.EntryGBs[B]=0;A.BossBananas[B]=0
	ShuffleExits.UpdateLevelProgression(A)
def Generate_Spoiler(spoiler):
	'Generate a complete spoiler based on input settings.';A=spoiler;global LogicVariables;LogicVariables=LogicVarHolder(A.settings);KasplatShuffle(LogicVariables);A.human_kasplats={};A.UpdateKasplats(LogicVariables.kasplat_map)
	if A.settings.bonus_barrels==_E:BarrelShuffle(A.settings);A.UpdateBarrels()
	if A.settings.bananaport_rando:B=[];C={};ShuffleWarps(B,C);A.bananaport_replacements=B.copy();A.human_warp_locations=C
	if A.settings.shuffle_loading_zones=='levels'and A.settings.kong_rando:
		if not A.settings.unlock_all_moves:A.settings.shuffle_items=_I
		A.settings.boss_location_rando=_B;A.settings.boss_kong_rando=_B;ShuffleKongsAndLevels(A)
	else:
		if A.settings.shuffle_loading_zones!='none':ShuffleExits.ExitShuffle(A.settings);A.UpdateExits()
		if A.settings.shuffle_items=='all':Fill(A)
		elif A.settings.shuffle_items==_I or A.settings.kong_rando:ShuffleMisc(A)
		else:
			ItemPool.PlaceConstants(A.settings)
			if not GetAccessibleLocations(A.settings,[],SearchMode.CheckBeatable):raise Ex.VanillaItemsGameNotBeatableException('Game unbeatable.')
	Reset();ShuffleExits.Reset();return A