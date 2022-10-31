'Crown Randomizer Placement Code.'
import js
from randomizer.Patching.Patcher import ROM
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Spoiler import Spoiler
from randomizer.Patching.Lib import float_to_hex,getNextFreeID,addNewScript
from randomizer.Enums.ScriptTypes import ScriptTypes
from randomizer.Lists.CrownLocations import CrownLocations
class CrownPlacementShortData:
	'Class to store small parts of information relevant to the placement algorithm.'
	def __init__(A,map,coords,scale,default,vanilla):'Initialize with provided data.';A.map=map;A.coords=coords;A.scale=scale;A.default=default;A.vanilla=vanilla
def randomize_crown_pads(spoiler):
	'Place Crown Pads.';E=spoiler;D='big'
	if E.settings.crown_placement_rando:
		M=[];N=[Maps.JungleJapes,Maps.AztecTinyTemple,Maps.FranticFactory,Maps.GloomyGalleon,Maps.FungiForest,Maps.CavesRotatingCabin,Maps.CastleGreenhouse,Maps.IslesSnideRoom,Maps.FungiForestLobby,Maps.HideoutHelm];F=[];K=N.copy()
		for O in E.crown_locations:
			for B in E.crown_locations[O]:
				A=CrownLocations[O][B];M.append(CrownPlacementShortData(A.map,A.coords,A.scale,A.default_index,A.is_vanilla))
				if A.is_vanilla and A.map in F:F.append(A.map)
				if not A.is_vanilla:
					if A.map not in K:K.append(A.map)
		for C in K:
			if C==Maps.CavesRotatingCabin:
				if C not in F:X=E.settings.rom_data;ROM().seek(X+405);ROM().write(1)
			else:
				G=js.pointer_addresses[9]['entries'][C]['pointing_to'];ROM().seek(G);P=int.from_bytes(ROM().readBytes(4),D);H=[]
				for Y in range(P):
					Q=True;R=G+4+Y*48;ROM().seek(R+40);Z=int.from_bytes(ROM().readBytes(2),D)
					if C in N and C not in F and Z==454:Q=False
					if Q:
						ROM().seek(R);S=[]
						for T in range(int(48/4)):S.append(int.from_bytes(ROM().readBytes(4),D))
						H.append(S)
				for B in M:
					U=[]
					if B.map==C and not B.vanilla:
						I=getNextFreeID(C,U);U.append(I);H.append([int(float_to_hex(B.coords[0]),16),int(float_to_hex(B.coords[1]),16),int(float_to_hex(B.coords[2]),16),int(float_to_hex(B.scale),16),1795943986,2605527663,0,0,0,0,454<<16|I,1<<16])
						if B.default==0:addNewScript(C,[I],ScriptTypes.CrownMain)
						elif B.default==1:addNewScript(C,[I],ScriptTypes.CrownIsles2)
				ROM().seek(G+4+P*48);V=int.from_bytes(ROM().readBytes(4),D);J=[V]
				for b in range(V):
					for T in range(int(36/4)):J.append(int.from_bytes(ROM().readBytes(4),D))
				W=int.from_bytes(ROM().readBytes(4),D);J.append(W)
				for c in range(W):
					for T in range(int(56/4)):J.append(int.from_bytes(ROM().readBytes(4),D))
				ROM().seek(G);ROM().writeMultipleBytes(len(H),4)
				for a in H:
					for L in a:ROM().writeMultipleBytes(L,4)
				for L in J:ROM().writeMultipleBytes(L,4)