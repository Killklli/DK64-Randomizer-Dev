'File that shuffles loading zone exits.'
_D='levels'
_C=False
_B=True
_A=None
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.LogicClasses import TransitionFront
from randomizer.Settings import Settings
LobbyEntrancePool=[Transitions.IslesMainToJapesLobby,Transitions.IslesMainToAztecLobby,Transitions.IslesMainToFactoryLobby,Transitions.IslesMainToGalleonLobby,Transitions.IslesMainToForestLobby,Transitions.IslesMainToCavesLobby,Transitions.IslesMainToCastleLobby]
root=Regions.IslesMain
def GetRootExit(exitId):'Query the world root to return an exit with a matching exit id.';return[A for A in Logic.Regions[root].exits if A.assumed and A.exitShuffleId is not _A and A.exitShuffleId==exitId][0]
def RemoveRootExit(exit):'Remove an exit from the world root.';Logic.Regions[root].exits.remove(exit)
def AddRootExit(exit):'Add an exit to the world root.';Logic.Regions[root].exits.append(exit)
def Reset():
	'Reset shufflable exit properties set during shuffling.'
	for exit in ShufflableExits.values():exit.shuffledId=_A;exit.shuffled=_C
	A=[]
	for exit in [A for A in Logic.Regions[root].exits if A.assumed]:A.append(exit)
	for exit in A:RemoveRootExit(exit)
def AttemptConnect(settings,frontExit,frontId,backExit,backId):
	'Attempt to connect two exits, checking if the world is valid if they are connected.';D=backId;B=settings;A=frontExit;E=_A
	if not B.decoupled_loading_zones:
		if A.back.reverse==D:return _C
		E=GetRootExit(A.back.reverse);RemoveRootExit(E)
	F=GetRootExit(D);RemoveRootExit(F);A.shuffled=_B;A.shuffledId=D
	if not B.decoupled_loading_zones:C=ShufflableExits[backExit.back.reverse];C.shuffled=_B;C.shuffledId=A.back.reverse
	G=Fill.VerifyWorld(B)
	if not G:
		AddRootExit(F);A.shuffled=_C;A.shuffledId=_A
		if not B.decoupled_loading_zones:AddRootExit(E);C.shuffled=_C;C.shuffledId=_A
	return G
def ShuffleExitsInPool(settings,frontpool,backpool):
	'Shuffle exits within a specific pool.';O='Failed to connect to ';H=settings;B=backpool;A=frontpool;E=[A for A in B if not Logic.Regions[ShufflableExits[A].back.regionId].tagbarrel];F=[A for A in E if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(F);I=[A for A in E if A not in F];random.shuffle(I);J=[A for A in B if A not in E];G=[A for A in J if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(G);K=[A for A in J if A not in G];random.shuffle(K);B=F;B.extend(I);B.extend(G);B.extend(K)
	if not H.decoupled_loading_zones:E=[B for B in A if not Logic.Regions[ShufflableExits[B].back.regionId].tagbarrel];F=[A for A in E if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(F);I=[A for A in E if A not in F];random.shuffle(I);J=[B for B in A if B not in E];G=[A for A in J if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(G);K=[A for A in J if A not in G];random.shuffle(K);A=F;A.extend(I);A.extend(G);A.extend(K)
	else:random.shuffle(A)
	while len(B)>0:
		N=B.pop(0);D=ShufflableExits[N];C=[B for B in A if ShufflableExits[B].entryKongs.issuperset(D.regionKongs)]
		if not H.decoupled_loading_zones and D.category is _A:C=[A for A in C if ShufflableExits[ShufflableExits[A].back.reverse].category is not _A];C=[A for A in C if ShufflableExits[D.back.reverse].entryKongs.issuperset(ShufflableExits[ShufflableExits[A].back.reverse].regionKongs)]
		elif H.decoupled_loading_zones and D.back.regionId in[Regions.JapesMinecarts,Regions.ForestMinecarts]:
			if Transitions.JapesCartsToMain in C:C.remove(Transitions.JapesCartsToMain)
			if Transitions.ForestCartsToMain in C:C.remove(Transitions.ForestCartsToMain)
		if len(C)==0:print(O+D.name+', found no suitable origins!');raise Ex.EntranceOutOfDestinations
		for L in C:
			M=ShufflableExits[L]
			if AttemptConnect(H,M,L,D,N):
				A.remove(L)
				if not H.decoupled_loading_zones:A.remove(D.back.reverse);B.remove(M.back.reverse)
				break
		if not M.shuffled:print(O+D.name+' from any of the remaining '+str(len(C))+' origins!');raise Ex.EntranceOutOfDestinations
		if len(A)!=len(B):print('Length of frontpool '+len(A)+' and length of backpool '+len(B)+' do not match!');raise Ex.EntranceOutOfDestinations
def AssumeExits(settings,frontpool,backpool,newpool):
	'Split exit pool into front and back pools, and assumes exits reachable from root.';B=newpool
	for C in range(len(B)):
		A=B[C];exit=ShufflableExits[A]
		if not settings.decoupled_loading_zones and exit.back.reverse is _A:continue
		frontpool.append(A);backpool.append(A);exit.shuffledId=_A;exit.toBeShuffled=_B;D=TransitionFront(exit.back.regionId,lambda l:_B,A,_B);AddRootExit(D)
def ShuffleExits(settings):
	'Shuffle exit pools depending on settings.';A=settings
	if A.shuffle_loading_zones==_D:
		if A.kongs_for_progression:ShuffleLevelOrderWithRestrictions(A)
		else:ShuffleLevelExits(A)
	elif A.shuffle_loading_zones=='all':B=[];C=[];AssumeExits(A,B,C,list(ShufflableExits.keys()));ShuffleExitsInPool(A,B,C)
	if A.shuffle_loading_zones==_D:UpdateLevelProgression(A)
def ExitShuffle(settings):
	'Facilitate shuffling of exits.';B=settings;A=0
	while _B:
		try:
			ShuffleExits(B)
			if not Fill.VerifyWorld(B):raise Ex.EntrancePlacementException
			return
		except Ex.EntrancePlacementException:
			if A==20:js.postMessage('Entrance placement failed, out of retries.');raise Ex.EntranceAttemptCountExceeded
			A+=1;js.postMessage('Entrance placement failed. Retrying. Tries: '+str(A));Reset()
def UpdateLevelProgression(settings):
	'Update level progression.';A=settings;D=A.EntryGBs.copy();E=A.BossBananas.copy();F=[Regions.JungleJapesLobby,Regions.AngryAztecLobby,Regions.FranticFactoryLobby,Regions.GloomyGalleonLobby,Regions.FungiForestLobby,Regions.CrystalCavesLobby,Regions.CreepyCastleLobby]
	for B in range(len(F)):
		C=B
		if A.shuffle_loading_zones==_D:G=ShufflableExits[LobbyEntrancePool[B]].shuffledId;H=ShufflableExits[G].back.regionId;C=F.index(H)
		D[C]=A.EntryGBs[B];E[C]=A.BossBananas[B]
	A.EntryGBs=D;A.BossBananas=E
def ShuffleLevelExits(settings,newLevelOrder=_A):
	'Shuffle level exits according to new level order if provided, otherwise shuffle randomly.';D=newLevelOrder;E=LobbyEntrancePool.copy();A=LobbyEntrancePool.copy()
	if D is not _A:
		for (J,K) in D.items():A[J-1]=LobbyEntrancePool[K]
	else:random.shuffle(E)
	F={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};G={1:_A,2:_A,3:_A,4:_A,5:_A,6:_A,7:_A}
	while len(A)>0:B=A.pop();L=ShufflableExits[B];H=E.pop();C=ShufflableExits[H];C.shuffled=_B;C.shuffledId=B;I=ShufflableExits[L.back.reverse];I.shuffled=_B;I.shuffledId=C.back.reverse;G[F[H]+1]=F[B]
	settings.level_order=G
def ShuffleLevelOrderWithRestrictions(settings):
	'Determine level order given starting kong and the need to find more kongs along the way.';A=settings
	if A.starting_kongs_count==1:B=ShuffleLevelOrderForOneStartingKong(A)
	else:B=ShuffleLevelOrderForMultipleStartingKongs(A)
	if _A in B.values():raise Ex.EntrancePlacementException('Invalid level order with fewer than the 7 required main levels.')
	ShuffleLevelExits(A,B)
def ShuffleLevelOrderForOneStartingKong(settings):
	'Determine level order given only starting with one kong and the need to find more kongs along the way.';J='free';C=settings;A={1,2,3,4,5,6,7}
	if C.starting_kong==Kongs.diddy:D=random.randint(1,4)
	else:D=random.randint(2,4)
	A.remove(D);F=[]
	if D==4:
		if C.starting_kong==Kongs.tiny and C.random_prices!=J:F=list(A.intersection({2,3}))
		else:F=list(A.intersection({1,3}))
	elif C.starting_kong==Kongs.tiny and C.random_prices!=J:F=list(A.intersection({2,3,4,5}))
	else:F=list(A.intersection({1,2,3,4,5}))
	E=random.choice(F);A.remove(E);B=[]
	if D==4:B=list(A.intersection({1,2,3}))
	elif D==3:
		if E<3:B=list(A.intersection({1,2,3,4,5}))
		else:B=list(A.intersection({1,2}))
	elif D==2 and C.starting_kong!=Kongs.diddy and C.starting_kong!=Kongs.chunky:
		if E==1:B=list(A.intersection({3,4,5}))
		else:B=list(A.intersection({1}))
	elif D==2 and C.starting_kong==Kongs.chunky:
		if E in(1,3):B=list(A.intersection({3,4,5}))
		else:B=list(A.intersection({1,2,3}))
	elif E<5:B=list(A.intersection({1,2,3,4,5}))
	else:B=list(A.intersection({1,2,3,4}))
	H=random.choice(B);A.remove(H);G=list(A);random.shuffle(G);K=G.pop();L=G.pop();M=G.pop();N=G.pop();I={E:Levels.JungleJapes,D:Levels.AngryAztec,H:Levels.FranticFactory,L:Levels.GloomyGalleon,M:Levels.FungiForest,K:Levels.CrystalCaves,N:Levels.CreepyCastle};C.level_order=I;return I
def ShuffleLevelOrderForMultipleStartingKongs(settings):
	'Determine level order given starting with 2 to 4 kongs and the need to find more kongs along the way.';A=settings;J={1,2,3,4,5,6,7};B={1:_A,2:_A,3:_A,4:_A,5:_A,6:_A,7:_A};D={Levels.JungleJapes:1 if Locations.DiddyKong in A.kong_locations else 0,Levels.AngryAztec:len([B for B in[Locations.LankyKong,Locations.TinyKong]if B in A.kong_locations]),Levels.FranticFactory:1 if Locations.ChunkyKong in A.kong_locations else 0,Levels.GloomyGalleon:0,Levels.FungiForest:0,Levels.CrystalCaves:0,Levels.CreepyCastle:0};O=[A[0]for A in sorted(D.items(),key=lambda x:x[1],reverse=_B)];F=sum(D.values())
	for K in O:
		F=F-D[K];G=A.starting_kongs_count;E=A.starting_kongs_count+F;L=[]
		for C in range(1,8):
			if E<5 and C>E+1:break
			if G==A.starting_kongs_count:
				if B[C]==Levels.AngryAztec and(Locations.TinyKong in A.kong_locations or Locations.LankyKong in A.kong_locations):
					H=Locations.TinyKong in A.kong_locations;I=Locations.LankyKong in A.kong_locations
					if H:
						if Kongs.diddy not in A.starting_kong_list and Kongs.chunky not in A.starting_kong_list:H=_C
					if I:
						P=Kongs.diddy in A.starting_kong_list or A.open_levels or Kongs.donkey in A.starting_kong_list and A.activate_all_bananaports=='all'
						if not P or Kongs.donkey not in A.starting_kong_list and Kongs.lanky not in A.starting_kong_list and Kongs.tiny not in A.starting_kong_list:I=_C
					if not H and not I:break
			L.append(C)
			if B[C]is not _A:G=G+D[B[C]];E=E+D[B[C]]
		M=list(J.intersection(L))
		if M==[]:return ShuffleLevelOrderForMultipleStartingKongs(A)
		N=random.choice(M);J.remove(N);B[N]=K
	return B