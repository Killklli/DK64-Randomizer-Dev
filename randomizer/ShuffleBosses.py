'Randomize Boss Locations.'
import random
from array import array
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.MapsAndExits import Maps
def ShuffleBosses(boss_location_rando):
	'Shuffle boss locations.';A=[Maps.JapesBoss,Maps.AztecBoss,Maps.FactoryBoss,Maps.GalleonBoss,Maps.FungiBoss,Maps.CavesBoss,Maps.CastleBoss]
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