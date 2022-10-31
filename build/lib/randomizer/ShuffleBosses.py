'Randomize Boss Locations.'
import random
from array import array
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.Exceptions import BossOutOfLocationsException,FillException,ItemPlacementException
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
		if A.boss_kong_rando:D=SelectRandomKongForBoss(C,A.hard_bosses)
		else:D=E[C]
		B.append(D)
	return B
def SelectRandomKongForBoss(boss_map,hard_bosses):
	'Randomly choses from the allowed list for the boss.';B=boss_map;A=[]
	if B==Maps.JapesBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.AztecBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.FactoryBoss:
		if hard_bosses:A=[Kongs.donkey,Kongs.tiny,Kongs.chunky]
		else:A=[Kongs.tiny]
	elif B==Maps.GalleonBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.FungiBoss:A=[Kongs.chunky]
	elif B==Maps.CavesBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	elif B==Maps.CastleBoss:A=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
	return random.choice(A)
def ShuffleKutoutKongs(boss_maps,boss_kongs,boss_kong_rando):
	'Shuffle the Kutout kong order.';C=[Kongs.lanky,Kongs.tiny,Kongs.chunky,Kongs.donkey,Kongs.diddy];A=[]
	if boss_kong_rando:E=boss_maps.index(Maps.CastleBoss);D=boss_kongs[E];B=C.copy();B.remove(D);random.shuffle(B);A.append(D);A.extend(B)
	else:A=C
	return A
def ShuffleKKOPhaseOrder(settings):
	'Shuffle the phase order in King Kut Out.';A=[0,1,2,3];random.shuffle(A);B=[]
	for C in range(3):B.append(A[C])
	return B.copy()
def ShuffleBossesBasedOnOwnedItems(settings,ownedKongs,ownedMoves):
	'Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves.';b='Dogadon 2';M=ownedMoves;B=ownedKongs;A=settings
	try:
		G={0,1,2,3,4,5,6};H=[A for A in G if Kongs.chunky in B[A]and Items.HunkyChunky in M[A]]
		if not A.kong_rando and not A.boss_location_rando and 4 not in H:raise ItemPlacementException('Items not placed to allow vanilla Dogadon 2.')
		if A.hard_bosses:I=[A for A in G if Kongs.donkey in B[A]or Kongs.chunky in B[A]or Kongs.tiny in B[A]and Items.PonyTailTwirl in M[A]]
		else:I=[A for A in G if Kongs.tiny in B[A]and Items.PonyTailTwirl in M[A]]
		K=None;N=b
		if len(H)<len(I):
			L=random.choice(H);K=Kongs.chunky
			if L in I:I.remove(L)
		N='Mad Jack'
		if A.hard_bosses:
			D=random.choice(I);Q=set(B[D]).intersection({Kongs.donkey,Kongs.chunky})
			if Kongs.tiny in B[D]and Items.PonyTailTwirl in M[D]:Q.add(Kongs.tiny)
			O=random.choice(list(Q))
		else:D=random.choice(I);O=Kongs.tiny
		if D in H:H.remove(D)
		if K is None:N=b;L=random.choice(H);K=Kongs.chunky
		G.remove(L);G.remove(D);N='the easy bosses to place (if this breaks here something REALLY strange happened)';J=list(G);random.shuffle(J);R=J.pop();S=random.choice(B[R]);T=J.pop();U=random.choice(B[T]);V=J.pop();W=random.choice(B[V]);X=J.pop();Y=random.choice(B[X]);Z=J.pop();a=random.choice(B[Z]);C=[];E=[]
		for F in range(0,7):
			if F==V:C.append(Maps.JapesBoss);E.append(W)
			elif F==X:C.append(Maps.AztecBoss);E.append(Y)
			elif F==D:C.append(Maps.FactoryBoss);E.append(O)
			elif F==R:C.append(Maps.GalleonBoss);E.append(S)
			elif F==L:C.append(Maps.FungiBoss);E.append(K)
			elif F==T:C.append(Maps.CavesBoss);E.append(U)
			elif F==Z:C.append(Maps.CastleBoss);E.append(a)
		if len(C)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as P:
		if isinstance(P.args[0],str)and'index out of range'in P.args[0]:raise BossOutOfLocationsException('No valid locations to place '+N)
		raise FillException(P)
	if A.kong_rando or A.boss_location_rando:A.boss_maps=C
	else:A.boss_maps=BossMapList.copy()
	if A.kong_rando or A.boss_kong_rando:
		if not A.boss_location_rando:A.boss_kongs=[W,Y,O,S,K,U,a]
		else:A.boss_kongs=E
	else:A.boss_kongs=ShuffleBossKongs(A)
	A.kutout_kongs=ShuffleKutoutKongs(A.boss_maps,A.boss_kongs,A.boss_kong_rando)