'Module used to handle setting and randomizing kasplats.'
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic
from randomizer.Enums.Kongs import Kongs,GetKongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
shufflable={Locations.IslesKasplatHelmLobby:Kongs.donkey,Locations.IslesKasplatCastleLobby:Kongs.diddy,Locations.IslesKasplatCavesLobby:Kongs.lanky,Locations.IslesKasplatFactoryLobby:Kongs.tiny,Locations.IslesKasplatGalleonLobby:Kongs.chunky,Locations.JapesKasplatLeftTunnelNear:Kongs.donkey,Locations.JapesKasplatNearPaintingRoom:Kongs.diddy,Locations.JapesKasplatNearLab:Kongs.lanky,Locations.JapesKasplatLeftTunnelFar:Kongs.tiny,Locations.AztecKasplatSandyBridge:Kongs.donkey,Locations.AztecKasplatLlamaTemple:Kongs.lanky,Locations.AztecKasplatNearLab:Kongs.tiny,Locations.FactoryKasplatProductionTop:Kongs.donkey,Locations.FactoryKasplatProductionBottom:Kongs.diddy,Locations.FactoryKasplatRandD:Kongs.lanky,Locations.FactoryKasplatStorage:Kongs.tiny,Locations.FactoryKasplatBlocks:Kongs.chunky,Locations.GalleonKasplatGoldTower:Kongs.donkey,Locations.GalleonKasplatLighthouseArea:Kongs.diddy,Locations.GalleonKasplatCannons:Kongs.lanky,Locations.GalleonKasplatNearLab:Kongs.tiny,Locations.GalleonKasplatNearSub:Kongs.chunky,Locations.ForestKasplatNearBarn:Kongs.donkey,Locations.ForestKasplatInsideMushroom:Kongs.diddy,Locations.ForestKasplatOwlTree:Kongs.lanky,Locations.ForestKasplatLowerMushroomExterior:Kongs.tiny,Locations.ForestKasplatUpperMushroomExterior:Kongs.chunky,Locations.CavesKasplatNearLab:Kongs.donkey,Locations.CavesKasplatPillar:Kongs.lanky,Locations.CavesKasplatNearCandy:Kongs.tiny,Locations.CavesKasplatOn5DI:Kongs.chunky,Locations.CastleKasplatCrypt:Kongs.diddy,Locations.CastleKasplatHalfway:Kongs.lanky,Locations.CastleKasplatLowerLedge:Kongs.tiny,Locations.CastleKasplatNearCandy:Kongs.chunky}
constants={Locations.JapesKasplatUnderground:Kongs.chunky,Locations.AztecKasplatOnTinyTemple:Kongs.diddy,Locations.AztecKasplatChunky5DT:Kongs.chunky,Locations.CavesKasplatNearFunky:Kongs.diddy,Locations.CastleKasplatTree:Kongs.donkey}
def FindLevel(location):
	'Find the level given a location.'
	for A in Logic.Regions.values():
		for B in A.locations:
			if B.id==location:return A.level
def ShuffleKasplats(LogicVariables):
	'Shuffles the kong assigned to each kasplat.';A=LogicVariables;global kasplat_map;B=[];C=GetKongs()
	for J in range(len(Levels)-1):B.append(C.copy())
	for (I,D) in constants.items():E=FindLevel(I);B[E].remove(D)
	A.kasplat_map={}
	for F in shufflable.keys():A.kasplat_map[F]=Kongs.any
	A.kasplat_map.update(constants);G=[A for A in shufflable.keys()];random.shuffle(G)
	while len(G)>0:
		F=G.pop();E=FindLevel(F);C=B[E];random.shuffle(C);H=False
		for D in C:A.kasplat_map[F]=D;B[E].remove(D);H=True;break
		if not H:raise Ex.KasplatOutOfKongs
def KasplatShuffle(LogicVariables):
	'Facilitate the shuffling of kasplat types.';A=LogicVariables
	if A.settings.kasplat_rando:
		B=0
		while True:
			try:
				ShuffleKasplats(A)
				if not Fill.VerifyWorld(A.settings):raise Ex.KasplatPlacementException
				return
			except Ex.KasplatPlacementException:
				if B==5:js.postMessage('Kasplat placement failed, out of retries.');raise Ex.KasplatAttemptCountExceeded
				else:B+=1;js.postMessage('Kasplat placement failed. Retrying. Tries: '+str(B))
def InitKasplatMap(LogicVariables):'Initialize kasplat_map in logic variables with default values.';A=LogicVariables;A.kasplat_map={};A.kasplat_map.update(shufflable);A.kasplat_map.update(constants)