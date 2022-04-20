'Rando write bananaport locations.'
from imp import source_from_cache
import js
from randomizer.Lists.Warps import BananaportVanilla
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_bananaport(spoiler):
	'Rando write bananaport locations.';W='idx';V='scale';U='_id';J=spoiler;I='pad_index';B='big';D=[532,531,529,530,528]
	if J.settings.bananaport_rando:
		for K in J.bananaport_replacements:
			E=[];L=int(K['containing_map']);F=js.pointer_addresses[9]['entries'][L]['pointing_to'];ROM().seek(F);X=int.from_bytes(ROM().readBytes(4),B)
			for M in range(X):
				A=F+4+M*48;ROM().seek(A+40);N=int.from_bytes(ROM().readBytes(2),B)
				if N in D:
					Y=D.index(N);ROM().seek(A+42);O=int.from_bytes(ROM().readBytes(2),B);ROM().seek(A+0);Z=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+4);a=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+8);b=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+12);c=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+24);d=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+28);e=int.from_bytes(ROM().readBytes(4),B);ROM().seek(A+32);f=int.from_bytes(ROM().readBytes(4),B);g=M;P=False
					for G in BananaportVanilla.values():
						if G.map_id==L and G.obj_id_vanilla==O and G.locked:P=True
					if not P:E.append({I:Y,U:O,'x':Z,'y':a,'z':b,V:c,'rx':d,'ry':e,'rz':f,W:g})
			for Q in K['pads']:
				h=Q['warp_index'];i=Q['warp_ids'];R=0
				for j in i:
					for H in E:
						if H[U]==j:
							k=H[W];A=F+48*k+4;C={};S=0
							for T in E:
								if T[I]==h:
									if S==R:C=T
									S+=1
							ROM().seek(A+40);ROM().writeMultipleBytes(D[H[I]],2);ROM().seek(A+0);ROM().writeMultipleBytes(C['x'],4);ROM().seek(A+4);ROM().writeMultipleBytes(C['y'],4);ROM().seek(A+8);ROM().writeMultipleBytes(C['z'],4);ROM().seek(A+12);ROM().writeMultipleBytes(C[V],4);ROM().seek(A+24);ROM().writeMultipleBytes(C['rx'],4);ROM().seek(A+28);ROM().writeMultipleBytes(C['ry'],4);ROM().seek(A+32);ROM().writeMultipleBytes(C['rz'],4)
					R+=1