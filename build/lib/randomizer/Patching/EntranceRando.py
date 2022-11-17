'Randomize Entrances passed from Misc options.'
_C='pointing_to'
_B='entries'
_A='big'
import js
from randomizer.Enums.Transitions import Transitions
from randomizer.Lists.MapsAndExits import GetExitId,GetMapId,MapExitTable,Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
valid_lz_types=[9,12,13,16]
def intToArr(val,size):
	'Convert INT to an array.\n\n    Args:\n        val (int): Value to convert\n        size (int): Size to write as\n\n    Returns:\n        array: int array\n    ';A=val;C=[]
	for E in range(size):C.append(0)
	B=size-1
	while B>-1:
		D=A%256;C[B]=D;B-=1;A=int((A-D)/256)
		if B==-1:break
		elif A==0:break
	return C
def randomize_entrances(spoiler):
	'Randomize Entrances based on shuffled_exit_instructions.';I='From Minecart';B=spoiler
	if B.settings.shuffle_loading_zones=='all'and B.shuffled_exit_instructions is not None:
		for F in B.shuffled_exit_instructions:
			J=int(F['container_map']);C=js.pointer_addresses[18][_B][J][_C];ROM().seek(C);K=int.from_bytes(ROM().readBytes(2),_A)
			for L in range(K):
				D=L*56+2;ROM().seek(C+D+16);M=int.from_bytes(ROM().readBytes(2),_A)
				if M in valid_lz_types:
					ROM().seek(C+D+18);G=int.from_bytes(ROM().readBytes(2),_A);ROM().seek(C+D+20);N=int.from_bytes(ROM().readBytes(2),_A)
					for E in F['zones']:
						if G==E['vanilla_map']:
							if N==E['vanilla_exit']or G==Maps.FactoryCrusher:ROM().seek(C+D+18);O=intToArr(E['new_map'],2);ROM().writeBytes(bytearray(O));ROM().seek(C+D+20);P=intToArr(E['new_exit'],2);ROM().writeBytes(bytearray(P))
		H=B.settings.rom_data;Q=93;ROM().seek(H+Q);ROM().write(1);A=B.shuffled_exit_data[Transitions.AztecMainToRace];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.AztecRaceToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CavesRaceToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.GalleonSealToShipyard];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.FactoryRaceToRandD];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleRaceToMuseum];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.GalleonLighthouseAreaToSickBay];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		if Transitions.ForestMainToCarts in B.shuffled_exit_data:A=B.shuffled_exit_data[Transitions.ForestMainToCarts];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		else:ROM().write(Maps.ForestMinecarts);ROM().write(0)
		if Transitions.ForestCartsToMain in B.shuffled_exit_data:A=B.shuffled_exit_data[Transitions.ForestCartsToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		else:ROM().write(Maps.FungiForest);ROM().write(MapExitTable[Maps.FungiForest].index(I))
		if Transitions.JapesCartsToMain in B.shuffled_exit_data:A=B.shuffled_exit_data[Transitions.JapesCartsToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		else:ROM().write(Maps.JungleJapes);ROM().write(MapExitTable[Maps.JungleJapes].index(I))
		A=B.shuffled_exit_data[Transitions.CastleCartsToCrypt];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesMainToCastleLobby];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));ROM().write(Maps.Isles);ROM().write(12);A=B.shuffled_exit_data[Transitions.JapesToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.AztecToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.FactoryToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.GalleonToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.ForestToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CavesToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));ROM().write(Maps.HideoutHelmLobby);ROM().write(1);A=B.shuffled_exit_data[Transitions.IslesToJapes];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToAztec];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToFactory];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToGalleon];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToForest];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToCaves];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToCastle];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleBallroomToMuseum];ROM().seek(H+304);ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleMuseumToBallroom];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
def filterEntranceType():
	'Change LZ Type for some entrances so that warps from crown pads work correctly.'
	for C in range(216):
		A=js.pointer_addresses[18][_B][C][_C];ROM().seek(A);D=int.from_bytes(ROM().readBytes(2),_A)
		for E in range(D):
			B=E*56+2;ROM().seek(A+B+16);F=int.from_bytes(ROM().readBytes(2),_A);G=int.from_bytes(ROM().readBytes(2),_A)
			if F==16 and G not in(Maps.Cranky,Maps.Candy,Maps.Funky,Maps.Snide):ROM().seek(A+B+16);ROM().writeMultipleBytes(12,2);ROM().seek(A+B+22);ROM().writeMultipleBytes(0,2)