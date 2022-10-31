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
	'Shuffles warps with the cross-map setting.';M=is_coupled;L=human_ports;K=True;I=bananaport_replacements;H=False
	for A in BananaportVanilla.values():A.cross_map_placed=H;I.append(0)
	E=[]
	for (P,A) in enumerate(BananaportVanilla.values()):
		if not A.cross_map_placed or not M:
			J=[];N=[]
			for B in BananaportVanilla.values():
				F=K
				if B.swap_index==A.swap_index:F=H
				if B.cross_map_placed:F=H
				else:N.append(B.swap_index)
				if A.restricted and B.restricted:F=H
				if F:J.append(B.swap_index)
			print(f"{P} ({len(J)} | {len(N)})");C=random.choice(J);G=random.randint(0,4);A.tied_index=C
			for B in BananaportVanilla.values():
				if B.swap_index==C:B.cross_map_placed=K
			A.new_warp=G;D=getWarpFromSwapIndex(C);L[A.name]=D.name;I[A.swap_index]=[C,G];A.destination_region_id=D.region_id;O=[C]
			if C in E:print(f"Selected {C} which is a duplicate")
			E.append(C)
			if M:
				A.cross_map_placed=K
				for B in BananaportVanilla.values():
					if B.swap_index==C:
						B.tied_index=A.swap_index;O.append(A.swap_index);B.new_warp=G;D=getWarpFromSwapIndex(A.swap_index);L[B.name]=D.name;I[B.swap_index]=[A.swap_index,G];A.destination_region_id=D.region_id
						if A.swap_index in E:print(f"Selected {A.swap_index} which is a duplicate")
						E.append(A.swap_index)
			print(f"Selected {O}")