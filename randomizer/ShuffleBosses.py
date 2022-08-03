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
	'Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves.';I=ownedMoves;B=ownedKongs;A=settings
	try:
		F={0,1,2,3,4,5,6};J='Dogadon 2';M=[A for A in F if Kongs.chunky in B[A]and Items.HunkyChunky in I[A]]
		if not A.kong_rando and not A.boss_location_rando and 4 not in M:raise ItemPlacementException('Items not placed to allow vanilla Dogadon 2.')
		N=random.choice(M);O=Kongs.chunky;F.remove(N);J='Mad Jack'
		if A.hard_bosses:
			K=[A for A in F if Kongs.donkey in B[A]or Kongs.chunky in B[A]or Kongs.tiny in B[A]and Items.PonyTailTwirl in I[A]];G=random.choice(K);P=set(B[G]).intersection({Kongs.donkey,Kongs.chunky})
			if Kongs.tiny in B[G]and Items.PonyTailTwirl in I[G]:P.add(Kongs.tiny)
			L=random.choice(list(P))
		else:K=[A for A in F if Kongs.tiny in B[A]and Items.PonyTailTwirl in I[A]];G=random.choice(K);L=Kongs.tiny
		F.remove(G);J='the easy bosses to place (if this breaks here something REALLY strange happened)';H=list(F);random.shuffle(H);Q=H.pop();R=random.choice(B[Q]);S=H.pop();T=random.choice(B[S]);U=H.pop();V=random.choice(B[U]);W=H.pop();X=random.choice(B[W]);Y=H.pop();Z=random.choice(B[Y]);C=[];D=[]
		for E in range(0,7):
			if E==U:C.append(Maps.JapesBoss);D.append(V)
			elif E==W:C.append(Maps.AztecBoss);D.append(X)
			elif E==G:C.append(Maps.FactoryBoss);D.append(L)
			elif E==Q:C.append(Maps.GalleonBoss);D.append(R)
			elif E==N:C.append(Maps.FungiBoss);D.append(O)
			elif E==S:C.append(Maps.CavesBoss);D.append(T)
			elif E==Y:C.append(Maps.CastleBoss);D.append(Z)
		if len(C)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as a:
		if'index out of range'in a.args[0]:raise BossOutOfLocationsException('No valid locations to place '+J)
		raise FillException(a)
	if A.kong_rando or A.boss_location_rando:A.boss_maps=C
	else:A.boss_maps=BossMapList.copy()
	if A.kong_rando or A.boss_kong_rando:
		if not A.boss_location_rando:A.boss_kongs=[V,X,L,R,O,T,Z]
		else:A.boss_kongs=D
	else:A.boss_kongs=ShuffleBossKongs(A)
	A.kutout_kongs=ShuffleKutoutKongs(A.boss_maps,A.boss_kongs,A.boss_kong_rando)