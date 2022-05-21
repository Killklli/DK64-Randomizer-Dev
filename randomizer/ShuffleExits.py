'File that shuffles loading zone exits.'
_D='levels'
_C=False
_B=True
_A=None
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Kongs import Kongs
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
	'Shuffle exits within a specific pool.';O='Failed to connect to ';K=settings;B=backpool;A=frontpool;C=[A for A in B if not Logic.Regions[ShufflableExits[A].back.regionId].tagbarrel];D=[A for A in C if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(D);H=[A for A in C if A not in D];random.shuffle(H);I=[A for A in B if A not in C];E=[A for A in I if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(E);J=[A for A in I if A not in E];random.shuffle(J);B=D;B.extend(H);B.extend(E);B.extend(J)
	if not K.decoupled_loading_zones:C=[B for B in A if not Logic.Regions[ShufflableExits[B].back.regionId].tagbarrel];D=[A for A in C if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(D);H=[A for A in C if A not in D];random.shuffle(H);I=[B for B in A if B not in C];E=[A for A in I if len(Logic.Regions[ShufflableExits[A].back.regionId].exits)==1];random.shuffle(E);J=[A for A in I if A not in E];random.shuffle(J);A=D;A.extend(H);A.extend(E);A.extend(J)
	else:random.shuffle(A)
	while len(B)>0:
		N=B.pop(0);F=ShufflableExits[N];G=[B for B in A if ShufflableExits[B].entryKongs.issuperset(F.regionKongs)]
		if not K.decoupled_loading_zones and F.category is _A:G=[A for A in G if ShufflableExits[ShufflableExits[A].back.reverse].category is not _A];G=[A for A in G if ShufflableExits[F.back.reverse].entryKongs.issuperset(ShufflableExits[ShufflableExits[A].back.reverse].regionKongs)]
		if len(G)==0:print(O+F.name+', found no suitable origins!');raise Ex.EntranceOutOfDestinations
		for L in G:
			M=ShufflableExits[L]
			if AttemptConnect(K,M,L,F,N):
				A.remove(L)
				if not K.decoupled_loading_zones:A.remove(F.back.reverse);B.remove(M.back.reverse)
				break
		if not M.shuffled:print(O+F.name+' from any of the remaining '+str(len(G))+' origins!');raise Ex.EntranceOutOfDestinations
		if len(A)!=len(B):print('Length of frontpool '+len(A)+' and length of backpool '+len(B)+' do not match!');raise Ex.EntranceOutOfDestinations
def AssumeExits(settings,frontpool,backpool,newpool):
	'Split exit pool into front and back pools, and assumes exits reachable from root.';B=newpool
	for C in range(len(B)):
		A=B[C];exit=ShufflableExits[A]
		if not settings.decoupled_loading_zones and exit.back.reverse is _A:continue
		frontpool.append(A);backpool.append(A);exit.shuffledId=_A;exit.toBeShuffled=_B;D=TransitionFront(exit.back.regionId,lambda l:_B,A,_B);AddRootExit(D)
def ShuffleExits(settings):
	'Shuffle exit pools depending on settings.';A=settings
	if A.shuffle_loading_zones==_D:ShuffleLevelExits()
	elif A.shuffle_loading_zones=='all':B=[];C=[];AssumeExits(A,B,C,[A for A in ShufflableExits.keys()]);ShuffleExitsInPool(A,B,C)
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
			else:A+=1;js.postMessage('Entrance placement failed. Retrying. Tries: '+str(A));Reset()
def UpdateLevelProgression(settings):
	'Update level progression.';A=settings;D=A.EntryGBs.copy();E=A.BossBananas.copy();F=[Regions.JungleJapesLobby,Regions.AngryAztecLobby,Regions.FranticFactoryLobby,Regions.GloomyGalleonLobby,Regions.FungiForestLobby,Regions.CrystalCavesLobby,Regions.CreepyCastleLobby]
	for B in range(len(F)):
		C=B
		if A.shuffle_loading_zones==_D:G=ShufflableExits[LobbyEntrancePool[B]].shuffledId;H=ShufflableExits[G].back.regionId;C=F.index(H)
		D[C]=A.EntryGBs[B];E[C]=A.BossBananas[B]
	A.EntryGBs=D;A.BossBananas=E
def ShuffleLevelExits(newLevelOrder=_A):
	'Shuffle level exits according to new level order if provided, otherwise shuffle randomly.';C=newLevelOrder;D=LobbyEntrancePool.copy();A=LobbyEntrancePool.copy()
	if C is not _A:
		for (G,H) in C.items():A[G-1]=LobbyEntrancePool[H]
	else:random.shuffle(D)
	while len(A)>0:E=A.pop();I=ShufflableExits[E];J=D.pop();B=ShufflableExits[J];B.shuffled=_B;B.shuffledId=E;F=ShufflableExits[I.back.reverse];F.shuffled=_B;F.shuffledId=B.back.reverse
def ShuffleLevelOrderWithRestrictions(settings):
	'Determine level order given starting kong and the need to find more kongs along the way.';M='free';B=settings;A={1,2,3,4,5,6,7}
	if B.starting_kong==Kongs.diddy:D=random.randint(1,4)
	else:D=random.randint(2,4)
	A.remove(D);F=[]
	if D==4:
		if B.starting_kong==Kongs.tiny and B.random_prices!=M:F=list(A.intersection({2,3}))
		else:F=list(A.intersection({1,3}))
	elif B.starting_kong==Kongs.tiny and B.random_prices!=M:F=list(A.intersection({2,3,4,5}))
	else:F=list(A.intersection({1,2,3,4,5}))
	E=random.choice(F);A.remove(E);C=[]
	if D==4:C=list(A.intersection({1,2,3}))
	elif D==3:
		if E<3:C=list(A.intersection({1,2,3,4,5}))
		else:C=list(A.intersection({1,2}))
	elif D==2 and B.starting_kong!=Kongs.diddy and B.starting_kong!=Kongs.chunky:
		if E==1:C=list(A.intersection({3,4,5}))
		else:C=list(A.intersection({1}))
	elif D==2 and B.starting_kong==Kongs.chunky:
		if E==1 or E==3:C=list(A.intersection({3,4,5}))
		else:C=list(A.intersection({1,2,3}))
	elif E<5:C=list(A.intersection({1,2,3,4,5}))
	else:C=list(A.intersection({1,2,3,4}))
	J=random.choice(C);A.remove(J);H=[]
	if B.starting_kong==Kongs.tiny or B.starting_kong==Kongs.donkey:H=list(A.intersection({2,7}))
	else:H=list(A.intersection({1,7}))
	K=random.choice(H);A.remove(K);G=list(A);random.shuffle(G);N=G.pop();O=G.pop();P=G.pop();I={E:Levels.JungleJapes,D:Levels.AngryAztec,J:Levels.FranticFactory,N:Levels.GloomyGalleon,O:Levels.FungiForest,K:Levels.CrystalCaves,P:Levels.CreepyCastle};print('New Level Order:')
	for L in range(1,8):print(str(L)+': '+I[L].name)
	if len(I)<7:raise Ex.EntrancePlacementException('Invalid level order with fewer than the 7 required main levels.')
	ShuffleLevelExits(I)