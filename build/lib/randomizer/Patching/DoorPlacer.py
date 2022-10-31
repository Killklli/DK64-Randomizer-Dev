'Apply Door Locations.'
import random,js
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.DoorLocations import door_locations
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.Lib import float_to_hex,getNextFreeID,addNewScript
from randomizer.Enums.ScriptTypes import ScriptTypes
def place_door_locations(spoiler):
	'Place Wrinkly Doors, and eventually T&S Doors.';O=False;F='big';D=spoiler
	if D.settings.wrinkly_location_rando or D.settings.tns_location_rando:
		T=[240,242,239,103,241]
		for C in range(216):
			J=js.pointer_addresses[9]['entries'][C]['pointing_to'];ROM().seek(J);U=int.from_bytes(ROM().readBytes(4),F);G=[]
			for P in range(U):
				V=J+4+P*48;ROM().seek(V+40);K=int.from_bytes(ROM().readBytes(2),F);H=True
				if D.settings.wrinkly_location_rando:
					if K in T:H=O
					if C==Maps.AngryAztecLobby and K in(572,24):H=O
					if C==Maps.FungiForestLobby and K in(573,40):H=O
				if D.settings.tns_location_rando:
					if C!=42:
						if K in(683,684):H=O
				if H:
					ROM().seek(V);A=[]
					for a in range(int(48/4)):A.append(int.from_bytes(ROM().readBytes(4),F))
					G.append(A)
			L=J+4+U*48;ROM().seek(L);b=int.from_bytes(ROM().readBytes(4),F);W=L+4+b*36;ROM().seek(W);c=int.from_bytes(ROM().readBytes(4),F);d=W+4+c*56;X=[];ROM().seek(L)
			for a in range(int((d-L)/4)):X.append(int.from_bytes(ROM().readBytes(4),F))
			M=[];Q=[];e=[];R=[];S=[]
			for Y in D.shuffled_door_data:
				for E in D.shuffled_door_data[Y]:
					B=door_locations[Y][E[0]];Z=E[1]
					if B.map==C:
						if Z=='wrinkly'and D.settings.wrinkly_location_rando:
							f=E[2];A=[]
							for I in range(3):A.append(int(float_to_hex(B.location[I]),16))
							A.append(int(float_to_hex(B.scale),16));A.append(1520);A.append(2148670208);A.append(int(float_to_hex(B.rx),16));A.append(int(float_to_hex(B.location[3]),16));A.append(int(float_to_hex(B.rz),16));A.append(0);id=getNextFreeID(C,M);Q.append(id);M.append(id);A.append(T[f]<<16|id);A.append(1<<16);G.append(A)
						elif Z=='tns'and D.settings.tns_location_rando:
							for N in range(2):
								A=[]
								for I in range(3):
									if N==1 and I==1:A.append(int(float_to_hex(B.location[I]-30),16))
									else:A.append(int(float_to_hex(B.location[I]),16))
								A.append(int(float_to_hex([B.scale,0.35][N]),16));A.append(4294901503);A.append(1834977);A.append(int(float_to_hex(B.rx),16));A.append(int(float_to_hex(B.location[3]),16));A.append(int(float_to_hex(B.rz),16));A.append(0);id=getNextFreeID(C,M);e.append(id);M.append(id)
								if N==0:R.append(id)
								else:S.append(id)
								A.append([684,683][N]<<16|id);A.append(1<<16);G.append(A)
			if len(Q)>0:addNewScript(C,Q,ScriptTypes.Wrinkly)
			if len(R)>0:addNewScript(C,R,ScriptTypes.TnsPortal)
			if len(S)>0:addNewScript(C,S,ScriptTypes.TnsIndicator)
			ROM().seek(J);ROM().writeMultipleBytes(len(G),4)
			for P in G:
				for E in P:ROM().writeMultipleBytes(E,4)
			for E in X:ROM().writeMultipleBytes(E,4)