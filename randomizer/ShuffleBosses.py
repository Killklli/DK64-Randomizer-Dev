'Randomize Boss Locations.'
import random
from array import array
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.Exceptions import BossOutOfLocationsException,FillException
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
	'Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves.';I=ownedMoves;F=settings;A=ownedKongs
	try:
		B={0,1,2,3,4,5,6};H='Dogadon 2';U=[C for C in B if Kongs.chunky in A[C]and Items.HunkyChunky in I[C]];N=random.choice(U);V=Kongs.chunky;B.remove(N);H='Mad Jack'
		if F.hard_mad_jack:
			K=[C for C in B if Kongs.donkey in A[C]or Kongs.chunky in A[C]or Kongs.tiny in A[C]and Items.PonyTailTwirl in I[C]];G=random.choice(K);O=set(A[G]).intersection({Kongs.donkey,Kongs.chunky})
			if Kongs.tiny in A[G]and Items.PonyTailTwirl in I[G]:O.add(Kongs.tiny)
			P=random.choice(list(O))
		else:K=[C for C in B if Kongs.tiny in A[C]and Items.PonyTailTwirl in I[C]];G=random.choice(K);P=Kongs.tiny
		B.remove(G);H='Pufftoss';W=[C for C in B if Kongs.diddy in A[C]or Kongs.lanky in A[C]or Kongs.tiny in A[C]or Kongs.chunky in A[C]];L=random.choice(W);X=set(A[L]).intersection({Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky});Y=random.choice(list(X));B.remove(L);H='Armydillo 2';Z=[C for C in B if Kongs.donkey in A[C]or Kongs.diddy in A[C]or Kongs.lanky in A[C]or Kongs.chunky in A[C]];M=random.choice(Z);a=set(A[M]).intersection({Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.chunky});b=random.choice(list(a));B.remove(M);H='the easy bosses to place (if this breaks here something REALLY strange happened)';J=list(B);random.shuffle(J);Q=J.pop();c=random.choice(A[Q]);R=J.pop();d=random.choice(A[R]);S=J.pop();e=random.choice(A[S]);C=[];D=[]
		for E in range(0,7):
			if E==Q:C.append(Maps.JapesBoss);D.append(c)
			elif E==R:C.append(Maps.AztecBoss);D.append(d)
			elif E==G:C.append(Maps.FactoryBoss);D.append(P)
			elif E==L:C.append(Maps.GalleonBoss);D.append(Y)
			elif E==N:C.append(Maps.FungiBoss);D.append(V)
			elif E==M:C.append(Maps.CavesBoss);D.append(b)
			elif E==S:C.append(Maps.CastleBoss);D.append(e)
		if len(C)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as T:
		if'index out of range'in T.args[0]:raise BossOutOfLocationsException('No valid locations to place '+H)
		raise FillException(T)
	F.boss_maps=C;F.boss_kongs=D;F.kutout_kongs=ShuffleKutoutKongs(F.boss_maps,F.boss_kongs,True)