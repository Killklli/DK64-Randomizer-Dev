'Rando write bananaport locations.'
from imp import source_from_cache
import js
from randomizer.Lists.Warps import BananaportVanilla
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_bananaport(spoiler):
	'Rando write bananaport locations.';d='idx';c='scale';b='pointing_to';a='entries';J=spoiler;B='big';L=[532,531,529,530,528]
	if J.settings.bananaport_rando=='in_level':
		for S in J.bananaport_replacements:
			C={};E=int(S['containing_map']);F=js.pointer_addresses[9][a][E][b];ROM().seek(F);M=int.from_bytes(ROM().readBytes(4),B)
			for K in range(M):
				A=F+4+K*48;ROM().seek(A+40);T=int.from_bytes(ROM().readBytes(2),B)
				if T in L:
					p=L.index(T);ROM().seek(A+42);G=int.from_bytes(ROM().readBytes(2),B);ROM().seek(A+0);e=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+4);f=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+8);g=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+12);h=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+24);i=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+28);j=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+32);k=int.from_bytes(ROM().readBytes(4),B);U=False
					for N in BananaportVanilla.values():
						if N.map_id==E and N.obj_id_vanilla==G and N.locked:U=True
					if not U:C[G]={'x':e,'y':f,'z':g,c:h,'rx':i,'ry':j,'rz':k,d:K}
			for V in S['pads']:
				l=V['warp_index']
				for (W,D) in enumerate(V['warp_ids']):
					O=0;X=[];I=-1
					for H in BananaportVanilla.values():
						if H.map_id==E and H.vanilla_warp==l and I==-1:
							X.append(H.locked)
							if W==O and not H.locked or W==0 and O==1 and X[0]and not H.locked:I=H.obj_id_vanilla
							O+=1
					if I!=-1:
						if I in C and D in C:m=C[I][d];A=F+48*m+4;ROM().seek(A);ROM().writeMultipleBytes(C[D]['x'],4);ROM().writeMultipleBytes(C[D]['y'],4);ROM().writeMultipleBytes(C[D]['z'],4);ROM().writeMultipleBytes(C[D][c],4);ROM().seek(A+24);ROM().writeMultipleBytes(C[D]['rx'],4);ROM().writeMultipleBytes(C[D]['ry'],4);ROM().writeMultipleBytes(C[D]['rz'],4)
						else:print('ERROR: ID not found in pad location dump')
					else:print('ERROR: Vanilla ID not found')
	elif J.settings.bananaport_rando in('crossmap_coupled','crossmap_decoupled'):
		n=33488896;Y=[];P=[]
		for (o,Z) in enumerate(J.bananaport_replacements):
			ROM().seek(n+o*10);Q=int.from_bytes(ROM().readBytes(1),B);ROM().writeMultipleBytes(Z[0],1);G=int.from_bytes(ROM().readBytes(2),B)
			if Q not in P:P.append(Q)
			Y.append([Q,G,Z[1]])
		for E in P:
			F=js.pointer_addresses[9][a][E][b];ROM().seek(F);M=int.from_bytes(ROM().readBytes(4),B)
			for K in range(M):
				A=F+4+K*48;ROM().seek(A+42);G=int.from_bytes(ROM().readBytes(2),B)
				for R in Y:
					if R[0]==E and R[1]==G:ROM().seek(A+40);ROM().writeMultipleBytes(L[R[2]],2)