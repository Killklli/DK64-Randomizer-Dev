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
def ShuffleBossKongs(settings):
	'Shuffle the kongs required for the bosses.';A=settings;E={Maps.JapesBoss:Kongs.donkey,Maps.AztecBoss:Kongs.diddy,Maps.FactoryBoss:Kongs.tiny,Maps.GalleonBoss:Kongs.lanky,Maps.FungiBoss:Kongs.chunky,Maps.CavesBoss:Kongs.donkey,Maps.CastleBoss:Kongs.lanky};B=[]
	for F in range(7):
		C=A.boss_maps[F]
		if A.boss_kong_rando:D=SelectRandomKongForBoss(C,A.hard_mad_jack)
		else:D=E[C]
		B.append(D)
	return B
def SelectRandomKongForBoss(boss_map,hard_mad_jack):
	'Randomly choses from the allowed list for the boss.';B=boss_map;A=[]
	if B==Maps.JapesBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.AztecBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.FactoryBoss:
		if hard_mad_jack:A=[Kongs.donkey,Kongs.tiny,Kongs.chunky]
		else:A=[Kongs.tiny]
	elif B==Maps.GalleonBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.FungiBoss:A=[Kongs.chunky]
	elif B==Maps.CavesBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.chunky]
	elif B==Maps.CastleBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	return random.choice(A)
def ShuffleKutoutKongs(boss_maps,boss_kongs,boss_kong_rando):
	'Shuffle the Kutout kong order.';C=[Kongs.lanky,Kongs.tiny,Kongs.chunky,Kongs.donkey,Kongs.diddy];A=[]
	if boss_kong_rando:E=boss_maps.index(Maps.CastleBoss);D=boss_kongs[E];B=C.copy();B.remove(D);random.shuffle(B);A.append(D);A.extend(B)
	else:A=C
	return A
def ShuffleBossesBasedOnOwnedItems(settings,ownedKongs,ownedMoves):
	'Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves.';H=ownedMoves;F=settings;A=ownedKongs
	try:
		B={0,1,2,3,4,5,6};S=[C for C in B if Kongs.chunky in A[C]and Items.HunkyChunky in H[C]];M=random.choice(S);T=Kongs.chunky;B.remove(M)
		if F.hard_mad_jack:
			J=[C for C in B if Kongs.donkey in A[C]or Kongs.chunky in A[C]or Kongs.tiny in A[C]and Items.PonyTailTwirl in H[C]];G=random.choice(J);N=set(A[G]).intersection({Kongs.donkey,Kongs.chunky})
			if Kongs.tiny in A[G]and Items.PonyTailTwirl in H[G]:N.add(Kongs.tiny)
			O=random.choice(list(N))
		else:J=[C for C in B if Kongs.tiny in A[C]and Items.PonyTailTwirl in H[C]];G=random.choice(J);O=Kongs.tiny
		B.remove(G);U=[C for C in B if Kongs.diddy in A[C]or Kongs.lanky in A[C]or Kongs.tiny in A[C]or Kongs.chunky in A[C]];K=random.choice(U);V=set(A[K]).intersection({Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky});W=random.choice(list(V));B.remove(K);X=[C for C in B if Kongs.donkey in A[C]or Kongs.diddy in A[C]or Kongs.lanky in A[C]or Kongs.chunky in A[C]];L=random.choice(X);Y=set(A[L]).intersection({Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.chunky});Z=random.choice(list(Y));B.remove(L);I=list(B);random.shuffle(I);P=I.pop();a=random.choice(A[P]);Q=I.pop();b=random.choice(A[Q]);R=I.pop();c=random.choice(A[R]);C=[];D=[]
		for E in range(0,7):
			if E==P:C.append(Maps.JapesBoss);D.append(a)
			elif E==Q:C.append(Maps.AztecBoss);D.append(b)
			elif E==G:C.append(Maps.FactoryBoss);D.append(O)
			elif E==K:C.append(Maps.GalleonBoss);D.append(W)
			elif E==M:C.append(Maps.FungiBoss);D.append(T)
			elif E==L:C.append(Maps.CavesBoss);D.append(Z)
			elif E==R:C.append(Maps.CastleBoss);D.append(c)
		if len(C)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as d:raise FillException(d)
	F.boss_maps=C;F.boss_kongs=D;F.kutout_kongs=ShuffleKutoutKongs(F.boss_maps,F.boss_kongs,True)