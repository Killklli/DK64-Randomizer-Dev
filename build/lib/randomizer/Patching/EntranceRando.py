'Randomize Entrances passed from Misc options.'
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
	'Randomize Entrances based on shuffled_exit_instructions.';J='From Minecart';F='big';B=spoiler
	if B.settings.shuffle_loading_zones=='all'and B.shuffled_exit_instructions is not None:
		for G in B.shuffled_exit_instructions:
			K=int(G['container_map']);C=js.pointer_addresses[18]['entries'][K]['pointing_to'];ROM().seek(C);L=int.from_bytes(ROM().readBytes(2),F)
			for M in range(L):
				D=M*56+2;ROM().seek(C+D+16);N=int.from_bytes(ROM().readBytes(2),F)
				if N in valid_lz_types:
					ROM().seek(C+D+18);H=int.from_bytes(ROM().readBytes(2),F);ROM().seek(C+D+20);O=int.from_bytes(ROM().readBytes(2),F)
					for E in G['zones']:
						if H==E['vanilla_map']:
							if O==E['vanilla_exit']or H==Maps.FactoryCrusher:ROM().seek(C+D+18);P=intToArr(E['new_map'],2);ROM().writeBytes(bytearray(P));ROM().seek(C+D+20);Q=intToArr(E['new_exit'],2);ROM().writeBytes(bytearray(Q))
		I=B.settings.rom_data;R=93;ROM().seek(I+R);ROM().write(1);A=B.shuffled_exit_data[Transitions.AztecMainToRace];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.AztecRaceToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CavesRaceToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.GalleonSealToShipyard];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.FactoryRaceToRandD];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleRaceToMuseum];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.GalleonLighthouseAreaToSickBay];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		if Transitions.ForestMainToCarts in B.shuffled_exit_data:A=B.shuffled_exit_data[Transitions.ForestMainToCarts];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		else:ROM().write(Maps.ForestMinecarts);ROM().write(0)
		if Transitions.ForestCartsToMain in B.shuffled_exit_data:A=B.shuffled_exit_data[Transitions.ForestCartsToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		else:ROM().write(Maps.FungiForest);ROM().write(MapExitTable[Maps.FungiForest].index(J))
		if Transitions.JapesCartsToMain in B.shuffled_exit_data:A=B.shuffled_exit_data[Transitions.JapesCartsToMain];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))
		else:ROM().write(Maps.JungleJapes);ROM().write(MapExitTable[Maps.JungleJapes].index(J))
		A=B.shuffled_exit_data[Transitions.CastleCartsToCrypt];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesMainToCastleLobby];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));ROM().write(Maps.Isles);ROM().write(12);A=B.shuffled_exit_data[Transitions.JapesToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.AztecToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.FactoryToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.GalleonToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.ForestToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CavesToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleToIsles];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));ROM().write(Maps.HideoutHelmLobby);ROM().write(1);A=B.shuffled_exit_data[Transitions.IslesToJapes];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToAztec];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToFactory];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToGalleon];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToForest];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToCaves];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.IslesToCastle];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleBallroomToMuseum];ROM().seek(I+304);ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A));A=B.shuffled_exit_data[Transitions.CastleMuseumToBallroom];ROM().write(GetMapId(A.regionId));ROM().write(GetExitId(A))