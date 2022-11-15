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
		N=[];O=[Maps.JungleJapes,Maps.AztecTinyTemple,Maps.FranticFactory,Maps.GloomyGalleon,Maps.FungiForest,Maps.CavesRotatingCabin,Maps.CastleGreenhouse,Maps.IslesSnideRoom,Maps.FungiForestLobby,Maps.HideoutHelm];J=[];K=O.copy()
		for L in E.crown_locations:
			for A in E.crown_locations[L]:
				B=CrownLocations[L][A];X=E.crown_locations[L][A];N.append(CrownPlacementShortData(B.map,B.coords,B.scale,X,B.is_vanilla))
				if B.is_vanilla:J.append(B.map)
				if not B.is_vanilla:
					if B.map not in K:K.append(B.map)
		for C in K:
			if C==Maps.CavesRotatingCabin:
				if C not in J:Y=E.settings.rom_data;ROM().seek(Y+405);ROM().write(1)
			else:
				F=js.pointer_addresses[9]['entries'][C]['pointing_to'];ROM().seek(F);P=int.from_bytes(ROM().readBytes(4),D);G=[]
				for Z in range(P):
					Q=True;R=F+4+Z*48;ROM().seek(R+40);a=int.from_bytes(ROM().readBytes(2),D)
					if C in O and C not in J and a==454:Q=False
					if Q:
						ROM().seek(R);S=[]
						for T in range(int(48/4)):S.append(int.from_bytes(ROM().readBytes(4),D))
						G.append(S)
				U=[]
				for A in N:
					if A.map==C and not A.vanilla:
						H=getNextFreeID(C,U);U.append(H);G.append([int(float_to_hex(A.coords[0]),16),int(float_to_hex(A.coords[1]),16),int(float_to_hex(A.coords[2]),16),int(float_to_hex(A.scale),16),1795943986,2605527663,0,0,0,0,454<<16|H,1<<16])
						if A.default==0:addNewScript(C,[H],ScriptTypes.CrownMain)
						elif A.default==1:addNewScript(C,[H],ScriptTypes.CrownIsles2)
				ROM().seek(F+4+P*48);V=int.from_bytes(ROM().readBytes(4),D);I=[V]
				for c in range(V):
					for T in range(int(36/4)):I.append(int.from_bytes(ROM().readBytes(4),D))
				W=int.from_bytes(ROM().readBytes(4),D);I.append(W)
				for d in range(W):
					for T in range(int(56/4)):I.append(int.from_bytes(ROM().readBytes(4),D))
				ROM().seek(F);ROM().writeMultipleBytes(len(G),4)
				for b in G:
					for M in b:ROM().writeMultipleBytes(M,4)
				for M in I:ROM().writeMultipleBytes(M,4)