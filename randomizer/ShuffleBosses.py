'Randomize Boss Locations.'
import random
from array import array
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.Exceptions import FillException
from randomizer.Lists.MapsAndExits import Maps
BossMapList=[Maps.JapesBoss,Maps.AztecBoss,Maps.FactoryBoss,Maps.GalleonBoss,Maps.FungiBoss,Maps.CavesBoss,Maps.CastleBoss]
def ShuffleBosses(boss_location_rando):
	'Shuffle boss locations.';A=BossMapList.copy()
	if boss_location_rando:random.shuffle(A)
	return A
def ShuffleBossKongs(boss_maps,boss_kong_rando):
	'Shuffle the kongs required for the bosses.';A={};A[Maps.JapesBoss]=Kongs.donkey;A[Maps.AztecBoss]=Kongs.diddy;A[Maps.FactoryBoss]=Kongs.tiny;A[Maps.GalleonBoss]=Kongs.lanky;A[Maps.FungiBoss]=Kongs.chunky;A[Maps.CavesBoss]=Kongs.donkey;A[Maps.CastleBoss]=Kongs.lanky;B=[]
	for E in range(7):
		C=boss_maps[E]
		if boss_kong_rando:D=SelectRandomKongForBoss(C)
		else:D=A[C]
		B.append(D)
	return B
def SelectRandomKongForBoss(boss_map):
	'Randomly choses from the allowed list for the boss.';A=boss_map
	if A==Maps.JapesBoss:B=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif A==Maps.AztecBoss:B=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif A==Maps.FactoryBoss:B=[Kongs.donkey,Kongs.tiny,Kongs.chunky]
	elif A==Maps.GalleonBoss:B=[Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif A==Maps.FungiBoss:B=[Kongs.chunky]
	elif A==Maps.CavesBoss:B=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.chunky]
	elif A==Maps.CastleBoss:B=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	return random.choice(B)
def ShuffleKutoutKongs(boss_maps,boss_kongs,boss_kong_rando):
	'Shuffle the Kutout kong order.';C=[Kongs.lanky,Kongs.tiny,Kongs.chunky,Kongs.donkey,Kongs.diddy];A=[]
	if boss_kong_rando:E=boss_maps.index(Maps.CastleBoss);D=boss_kongs[E];B=C.copy();B.remove(D);random.shuffle(B);A.append(D);A.extend(B)
	else:A=C
	return A
def ShuffleBossesBasedOnOwnedItems(settings,ownedKongs,ownedMoves):
	'Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves.';I=ownedMoves;F=settings;A=ownedKongs
	try:
		D={0,1,2,3,4,5,6};Q=[B for B in D if Kongs.chunky in A[B]and Items.HunkyChunky in I[B]];K=random.choice(Q);R=Kongs.chunky;D.remove(K);S=[B for B in D if Kongs.donkey in A[B]or Kongs.chunky in A[B]or Kongs.tiny in A[B]and Items.PonyTailTwirl in I[B]];G=random.choice(S);L=set(A[G]).intersection({Kongs.donkey,Kongs.chunky})
		if Kongs.tiny in A[G]and Items.PonyTailTwirl in I[G]:L.add(Kongs.tiny)
		T=random.choice(list(L));D.remove(G);U=[B for B in D if Kongs.diddy in A[B]or Kongs.lanky in A[B]or Kongs.tiny in A[B]or Kongs.chunky in A[B]];J=random.choice(U);V=set(A[J]).intersection({Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky});W=random.choice(list(V));D.remove(J);H=list(D);random.shuffle(H);M=H.pop();X=random.choice(A[M]);N=H.pop();Y=random.choice(A[N]);O=H.pop();Z=random.choice(A[O]);P=H.pop();a=random.choice(A[P]);B=[];C=[]
		for E in range(0,7):
			if E==M:B.append(Maps.JapesBoss);C.append(X)
			elif E==N:B.append(Maps.AztecBoss);C.append(Y)
			elif E==G:B.append(Maps.FactoryBoss);C.append(T)
			elif E==J:B.append(Maps.GalleonBoss);C.append(W)
			elif E==K:B.append(Maps.FungiBoss);C.append(R)
			elif E==O:B.append(Maps.CavesBoss);C.append(Z)
			elif E==P:B.append(Maps.CastleBoss);C.append(a)
		print('New Boss Order: '+str(B));print('New Boss Kongs: '+str(C))
		if len(B)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as b:raise FillException(b)
	F.boss_maps=B;F.boss_kongs=C;F.kutout_kongs=ShuffleKutoutKongs(F.boss_maps,F.boss_kongs,True)