'File that shuffles loading zone exits.'
_C=False
_B=True
_A=None
import random
from ast import And
import js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic
from randomizer.Enums.Regions import Regions
from randomizer.Enums.SearchMode import SearchMode
from randomizer.Enums.Transitions import Transitions
from randomizer.ItemPool import AllItems,PlaceConstants
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.LogicClasses import TransitionFront
from randomizer.Settings import Settings
LobbyEntrancePool=[Transitions.IslesMainToJapesLobby,Transitions.IslesMainToAztecLobby,Transitions.IslesMainToFactoryLobby,Transitions.IslesMainToGalleonLobby,Transitions.IslesMainToForestLobby,Transitions.IslesMainToCavesLobby,Transitions.IslesMainToCastleLobby]
LobbyExitPool=[Transitions.IslesJapesLobbyToMain,Transitions.IslesAztecLobbyToMain,Transitions.IslesFactoryLobbyToMain,Transitions.IslesGalleonLobbyToMain,Transitions.IslesForestLobbyToMain,Transitions.IslesCavesLobbyToMain,Transitions.IslesCastleLobbyToMain]
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
	'Shuffle exit pools depending on settings.';D='levels';A=settings;B=[];C=[]
	if A.shuffle_loading_zones==D:ShuffleLevelExits(A,LobbyEntrancePool.copy(),LobbyEntrancePool.copy())
	elif A.shuffle_loading_zones=='all':AssumeExits(A,B,C,[A for A in ShufflableExits.keys()]);ShuffleExitsInPool(A,B,C)
	if A.shuffle_loading_zones==D:UpdateLevelProgression(A)
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
	'Update level progression.';A=settings;C=A.EntryGBs.copy();D=A.BossBananas.copy();E=[Regions.JungleJapesLobby,Regions.AngryAztecLobby,Regions.FranticFactoryLobby,Regions.GloomyGalleonLobby,Regions.FungiForestLobby,Regions.CrystalCavesLobby,Regions.CreepyCastleLobby]
	for B in range(len(E)):G=ShufflableExits[LobbyEntrancePool[B]].shuffledId;H=ShufflableExits[G].back.regionId;F=E.index(H);C[F]=A.EntryGBs[B];D[F]=A.BossBananas[B]
	A.EntryGBs=C;A.BossBananas=D
def ShuffleLevelExits(settings,frontpool,backpool):
	'Shuffle exits within a  pool.';C=backpool;B=frontpool;random.shuffle(B)
	while len(C)>0:D=C.pop(0);F=ShufflableExits[D];G=B.pop();A=ShufflableExits[G];A.shuffled=_B;A.shuffledId=D;E=ShufflableExits[F.back.reverse];E.shuffled=_B;E.shuffledId=A.back.reverse