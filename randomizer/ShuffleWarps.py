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
def getWarpFromSwapIndex(index):
	'Acquire warp name from index.'
	for A in BananaportVanilla.values():
		if A.swap_index==index:return A
def ShuffleWarpsCrossMap(bananaport_replacements,human_ports,is_coupled):
	'Shuffles warps with the cross-map setting.';K=is_coupled;J=human_ports;I=True;H=bananaport_replacements;G=False
	for A in BananaportVanilla.values():A.cross_map_placed=G;H.append(0)
	L=[]
	for (P,A) in enumerate(BananaportVanilla.values()):
		if not A.cross_map_placed or not K:
			M=[];N=[]
			for B in BananaportVanilla.values():
				E=I
				if B.swap_index==A.swap_index:E=G
				if B.cross_map_placed:E=G
				else:N.append(B.swap_index)
				if A.restricted and B.restricted:E=G
				if E:M.append(B.swap_index)
			C=random.choice(M);F=random.randint(0,4);A.tied_index=C
			for B in BananaportVanilla.values():
				if B.swap_index==C:B.cross_map_placed=I
			A.new_warp=F;D=getWarpFromSwapIndex(C);J[A.name]=D.name;H[A.swap_index]=[C,F];A.destination_region_id=D.region_id;O=[C];L.append(C)
			if K:
				A.cross_map_placed=I
				for B in BananaportVanilla.values():
					if B.swap_index==C:B.tied_index=A.swap_index;O.append(A.swap_index);B.new_warp=F;D=getWarpFromSwapIndex(A.swap_index);J[B.name]=D.name;H[B.swap_index]=[A.swap_index,F];B.destination_region_id=D.region_id;L.append(A.swap_index)