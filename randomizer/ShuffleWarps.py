'Randomizes Bananaports.'
import random,js
from randomizer.Enums.Warps import Warps
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Warps import BananaportVanilla
def getShuffleMaps():
	'Produce list of maps which contain a bananaport swap.';A=[]
	for B in BananaportVanilla.values():
		if B.map_id not in A:A.append(B.map_id)
	return A
def ShuffleWarps(bananaport_replacements,human_ports):
	'Shuffles warps between themselves.';H=getShuffleMaps()
	for B in H:
		D=[]
		for A in BananaportVanilla.values():
			if A.map_id==B and not A.locked:D.append(A.vanilla_warp)
		random.shuffle(D);F=0
		for A in BananaportVanilla.keys():
			if BananaportVanilla[A].map_id==B and not BananaportVanilla[A].locked:BananaportVanilla[A].setNewWarp(D[F]);F+=1
		G=[];C=[[],[],[],[],[]]
		for A in BananaportVanilla.values():
			if A.map_id==B:
				human_ports[A.name]='Warp '+str(A.new_warp+1)
				if not A.locked:C[A.new_warp].append(A.obj_id_vanilla)
		for E in range(len(C)):
			if len(C[E])>0:G.append({'warp_index':E,'warp_ids':C[E].copy()})
		bananaport_replacements.append({'containing_map':B,'pads':G.copy()})