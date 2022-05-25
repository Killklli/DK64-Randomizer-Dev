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
	'Shuffle the kongs required for the bosses.';D={Maps.JapesBoss:Kongs.donkey,Maps.AztecBoss:Kongs.diddy,Maps.FactoryBoss:Kongs.tiny,Maps.GalleonBoss:Kongs.lanky,Maps.FungiBoss:Kongs.chunky,Maps.CavesBoss:Kongs.donkey,Maps.CastleBoss:Kongs.lanky};A=[]
	for E in range(7):
		B=boss_maps[E]
		if boss_kong_rando:C=SelectRandomKongForBoss(B)
		else:C=D[B]
		A.append(C)
	return A
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
		C={0,1,2,3,4,5,6};Q=[B for B in C if Kongs.chunky in A[B]and Items.HunkyChunky in I[B]];L=random.choice(Q);R=Kongs.chunky;C.remove(L);S=[B for B in C if Kongs.donkey in A[B]or Kongs.chunky in A[B]or Kongs.tiny in A[B]and Items.PonyTailTwirl in I[B]];G=random.choice(S);M=set(A[G]).intersection({Kongs.donkey,Kongs.chunky})
		if Kongs.tiny in A[G]and Items.PonyTailTwirl in I[G]:M.add(Kongs.tiny)
		T=random.choice(list(M));C.remove(G);U=[B for B in C if Kongs.diddy in A[B]or Kongs.lanky in A[B]or Kongs.tiny in A[B]or Kongs.chunky in A[B]];J=random.choice(U);V=set(A[J]).intersection({Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky});W=random.choice(list(V));C.remove(J);X=[B for B in C if Kongs.donkey in A[B]or Kongs.diddy in A[B]or Kongs.lanky in A[B]or Kongs.chunky in A[B]];K=random.choice(X);Y=set(A[K]).intersection({Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.chunky});Z=random.choice(list(Y));C.remove(K);H=list(C);random.shuffle(H);N=H.pop();a=random.choice(A[N]);O=H.pop();b=random.choice(A[O]);P=H.pop();c=random.choice(A[P]);B=[];D=[]
		for E in range(0,7):
			if E==N:B.append(Maps.JapesBoss);D.append(a)
			elif E==O:B.append(Maps.AztecBoss);D.append(b)
			elif E==G:B.append(Maps.FactoryBoss);D.append(T)
			elif E==J:B.append(Maps.GalleonBoss);D.append(W)
			elif E==L:B.append(Maps.FungiBoss);D.append(R)
			elif E==K:B.append(Maps.CavesBoss);D.append(Z)
			elif E==P:B.append(Maps.CastleBoss);D.append(c)
		print('New Boss Order: '+str(B));print('New Boss Kongs: '+str(D))
		if len(B)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as d:raise FillException(d)
	F.boss_maps=B;F.boss_kongs=D;F.kutout_kongs=ShuffleKutoutKongs(F.boss_maps,F.boss_kongs,True)