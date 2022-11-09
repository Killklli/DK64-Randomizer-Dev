'Apply Door Locations.'
import random,js
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.DoorLocations import door_locations
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.Lib import float_to_hex,getNextFreeID,addNewScript
from randomizer.Enums.ScriptTypes import ScriptTypes
def place_door_locations(spoiler):
	'Place Wrinkly Doors, and eventually T&S Doors.';T='remove_wrinkly_puzzles';K=False;G='big';B=spoiler
	if B.settings.wrinkly_location_rando or B.settings.tns_location_rando or(T in B.settings.misc_changes_selected or len(B.settings.misc_changes_selected)==0):
		U=[240,242,239,103,241]
		for D in range(216):
			L=js.pointer_addresses[9]['entries'][D]['pointing_to'];ROM().seek(L);V=int.from_bytes(ROM().readBytes(4),G);H=[]
			for P in range(V):
				W=L+4+P*48;ROM().seek(W+40);I=int.from_bytes(ROM().readBytes(2),G);F=True
				if B.settings.wrinkly_location_rando or(T in B.settings.misc_changes_selected or len(B.settings.misc_changes_selected)==0):
					if I in U:F=K
					if D==Maps.AngryAztecLobby and I in(572,24):F=K
					if D==Maps.FungiForestLobby and I in(573,40):F=K
					if D==Maps.CrystalCavesLobby and I in(53,206):F=K
				if B.settings.tns_location_rando:
					if D!=42:
						if I in(683,684):F=K
				if F:
					ROM().seek(W);A=[]
					for b in range(int(48/4)):A.append(int.from_bytes(ROM().readBytes(4),G))
					H.append(A)
			M=L+4+V*48;ROM().seek(M);c=int.from_bytes(ROM().readBytes(4),G);X=M+4+c*36;ROM().seek(X);d=int.from_bytes(ROM().readBytes(4),G);e=X+4+d*56;Y=[];ROM().seek(M)
			for b in range(int((e-M)/4)):Y.append(int.from_bytes(ROM().readBytes(4),G))
			N=[];Q=[];f=[];R=[];S=[]
			for Z in B.shuffled_door_data:
				for E in B.shuffled_door_data[Z]:
					C=door_locations[Z][E[0]];a=E[1]
					if C.map==D:
						if a=='wrinkly'and(B.settings.wrinkly_location_rando or(T in B.settings.misc_changes_selected or len(B.settings.misc_changes_selected)==0)):
							g=E[2];A=[]
							for J in range(3):A.append(int(float_to_hex(C.location[J]),16))
							A.append(int(float_to_hex(C.scale),16));A.append(1520);A.append(2148670208);A.append(int(float_to_hex(C.rx),16));A.append(int(float_to_hex(C.location[3]),16));A.append(int(float_to_hex(C.rz),16));A.append(0);id=getNextFreeID(D,N);Q.append(id);N.append(id);A.append(U[g]<<16|id);A.append(1<<16);H.append(A)
						elif a=='tns'and B.settings.tns_location_rando:
							for O in range(2):
								A=[]
								for J in range(3):
									if O==1 and J==1:A.append(int(float_to_hex(C.location[J]-30),16))
									else:A.append(int(float_to_hex(C.location[J]),16))
								A.append(int(float_to_hex([C.scale,0.35][O]),16));A.append(4294901503);A.append(1834977);A.append(int(float_to_hex(C.rx),16));A.append(int(float_to_hex(C.location[3]),16));A.append(int(float_to_hex(C.rz),16));A.append(0);id=getNextFreeID(D,N);f.append(id);N.append(id)
								if O==0:R.append(id)
								else:S.append(id)
								A.append([684,683][O]<<16|id);A.append(1<<16);H.append(A)
			if len(Q)>0:addNewScript(D,Q,ScriptTypes.Wrinkly)
			if len(R)>0:addNewScript(D,R,ScriptTypes.TnsPortal)
			if len(S)>0:addNewScript(D,S,ScriptTypes.TnsIndicator)
			ROM().seek(L);ROM().writeMultipleBytes(len(H),4)
			for P in H:
				for E in P:ROM().writeMultipleBytes(E,4)
			for E in Y:ROM().writeMultipleBytes(E,4)