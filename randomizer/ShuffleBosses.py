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
	'Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves.';d='No valid locations to place ';c='Dogadon 2';H=ownedMoves;B=ownedKongs;A=settings
	try:
		C={0,1,2,3,4,5,6};I=[A for A in C if Kongs.chunky in B[A]and Items.HunkyChunky in H[A]and Items.Barrels in H[A]]
		if not A.kong_rando and not A.boss_location_rando and 4 not in I:raise ItemPlacementException('Items not placed to allow vanilla Dogadon 2.')
		if A.hard_bosses:J=[A for A in C if Kongs.donkey in B[A]or Kongs.chunky in B[A]or Kongs.tiny in B[A]and Items.PonyTailTwirl in H[A]]
		else:J=[A for A in C if Kongs.tiny in B[A]and Items.PonyTailTwirl in H[A]]
		L=None;K=c
		if len(I)<len(J):
			M=random.choice(I);L=Kongs.chunky
			if M in J:J.remove(M)
		K='Mad Jack'
		if A.hard_bosses:
			E=random.choice(J);U=set(B[E]).intersection({Kongs.donkey,Kongs.chunky})
			if Kongs.tiny in B[E]and Items.PonyTailTwirl in H[E]:U.add(Kongs.tiny)
			P=random.choice(list(U))
		else:E=random.choice(J);P=Kongs.tiny
		if E in I:I.remove(E)
		if L is None:K=c;M=random.choice(I);L=Kongs.chunky
		C.remove(M);C.remove(E);K='barrels-locked bosses';O=[A for A in C if Items.Barrels in H[A]];random.shuffle(O);Q=O.pop();V=random.choice(B[Q]);C.remove(Q);R=O.pop();W=random.choice(B[R]);C.remove(R);S=O.pop();X=random.choice(B[S]);C.remove(S);K='the easy bosses to place (if this breaks here something REALLY strange happened)';T=list(C);random.shuffle(T);Y=T.pop();Z=random.choice(B[Y]);a=T.pop();b=random.choice(B[a]);D=[];F=[]
		for G in range(0,7):
			if G==R:D.append(Maps.JapesBoss);F.append(W)
			elif G==S:D.append(Maps.AztecBoss);F.append(X)
			elif G==E:D.append(Maps.FactoryBoss);F.append(P)
			elif G==Y:D.append(Maps.GalleonBoss);F.append(Z)
			elif G==M:D.append(Maps.FungiBoss);F.append(L)
			elif G==Q:D.append(Maps.CavesBoss);F.append(V)
			elif G==a:D.append(Maps.CastleBoss);F.append(b)
		if len(D)<7:raise FillException('Invalid boss order with fewer than the 7 required main levels.')
	except Exception as N:
		if isinstance(N.args[0],str)and'index out of range'in N.args[0]:print('Unlucky move placement fill :(');raise BossOutOfLocationsException(d+K)
		if isinstance(N.args[0],str)and'pop from empty list'in N.args[0]:print('Barrels bad.');raise BossOutOfLocationsException(d+K)
		raise N
	if A.kong_rando or A.boss_location_rando:A.boss_maps=D
	else:A.boss_maps=BossMapList.copy()
	if A.kong_rando or A.boss_kong_rando:
		if not A.boss_location_rando:A.boss_kongs=[W,X,P,Z,L,V,b]
		else:A.boss_kongs=F
	else:A.boss_kongs=ShuffleBossKongs(A)
	A.kutout_kongs=ShuffleKutoutKongs(A.boss_maps,A.boss_kongs,A.boss_kong_rando)