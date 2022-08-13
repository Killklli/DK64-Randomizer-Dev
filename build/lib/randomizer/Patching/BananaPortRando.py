'Rando write bananaport locations.'
from imp import source_from_cache
import js
from randomizer.Lists.Warps import BananaportVanilla
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_bananaport(spoiler):
	'Rando write bananaport locations.';V='idx';U='scale';K=spoiler;C='big';L=[532,531,529,530,528]
	if K.settings.bananaport_rando:
		for M in K.bananaport_replacements:
			B={};G=int(M['containing_map']);H=js.pointer_addresses[9]['entries'][G]['pointing_to'];ROM().seek(H);W=int.from_bytes(ROM().readBytes(4),C)
			for N in range(W):
				A=H+4+N*48;ROM().seek(A+40);O=int.from_bytes(ROM().readBytes(2),C)
				if O in L:
					g=L.index(O);ROM().seek(A+42);P=int.from_bytes(ROM().readBytes(2),C);ROM().seek(A+0);X=int.from_bytes(ROM().readBytes(4),C);ROM().seek(A+4);Y=int.from_bytes(ROM().readBytes(4),C);ROM().seek(A+8);Z=int.from_bytes(ROM().readBytes(4),C);ROM().seek(A+12);a=int.from_bytes(ROM().readBytes(4),C);ROM().seek(A+24);b=int.from_bytes(ROM().readBytes(4),C);ROM().seek(A+28);c=int.from_bytes(ROM().readBytes(4),C);ROM().seek(A+32);d=int.from_bytes(ROM().readBytes(4),C);Q=False
					for I in BananaportVanilla.values():
						if I.map_id==G and I.obj_id_vanilla==P and I.locked:Q=True
					if not Q:B[P]={'x':X,'y':Y,'z':Z,U:a,'rx':b,'ry':c,'rz':d,V:N}
			for R in M['pads']:
				e=R['warp_index']
				for (S,D) in enumerate(R['warp_ids']):
					J=0;T=[];F=-1
					for E in BananaportVanilla.values():
						if E.map_id==G and E.vanilla_warp==e and F==-1:
							T.append(E.locked)
							if S==J and not E.locked or S==0 and J==1 and T[0]and not E.locked:F=E.obj_id_vanilla
							J+=1
					if F!=-1:
						if F in B and D in B:f=B[F][V];A=H+48*f+4;ROM().seek(A);ROM().writeMultipleBytes(B[D]['x'],4);ROM().writeMultipleBytes(B[D]['y'],4);ROM().writeMultipleBytes(B[D]['z'],4);ROM().writeMultipleBytes(B[D][U],4);ROM().seek(A+24);ROM().writeMultipleBytes(B[D]['rx'],4);ROM().writeMultipleBytes(B[D]['ry'],4);ROM().writeMultipleBytes(B[D]['rz'],4)
						else:print('ERROR: ID not found in pad location dump')
					else:print('ERROR: Vanilla ID not found')