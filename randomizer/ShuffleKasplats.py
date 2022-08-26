'Module used to handle setting and randomizing kasplats.'
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex,randomizer.Logic as Logic
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import GetKongs,Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Types import Types
from randomizer.Lists.KasplatLocations import KasplatLocationList
from randomizer.Lists.Location import Location
from randomizer.Lists.MapsAndExits import Maps
from randomizer.LogicClasses import LocationLogic
shufflable={Locations.IslesKasplatHelmLobby:Kongs.donkey,Locations.IslesKasplatCastleLobby:Kongs.diddy,Locations.IslesKasplatCavesLobby:Kongs.lanky,Locations.IslesKasplatFactoryLobby:Kongs.tiny,Locations.IslesKasplatGalleonLobby:Kongs.chunky,Locations.JapesKasplatLeftTunnelNear:Kongs.donkey,Locations.JapesKasplatNearPaintingRoom:Kongs.diddy,Locations.JapesKasplatNearLab:Kongs.lanky,Locations.JapesKasplatLeftTunnelFar:Kongs.tiny,Locations.AztecKasplatSandyBridge:Kongs.donkey,Locations.AztecKasplatLlamaTemple:Kongs.lanky,Locations.AztecKasplatNearLab:Kongs.tiny,Locations.FactoryKasplatProductionTop:Kongs.donkey,Locations.FactoryKasplatProductionBottom:Kongs.diddy,Locations.FactoryKasplatRandD:Kongs.lanky,Locations.FactoryKasplatStorage:Kongs.tiny,Locations.FactoryKasplatBlocks:Kongs.chunky,Locations.GalleonKasplatGoldTower:Kongs.donkey,Locations.GalleonKasplatLighthouseArea:Kongs.diddy,Locations.GalleonKasplatCannons:Kongs.lanky,Locations.GalleonKasplatNearLab:Kongs.tiny,Locations.GalleonKasplatNearSub:Kongs.chunky,Locations.ForestKasplatNearBarn:Kongs.donkey,Locations.ForestKasplatInsideMushroom:Kongs.diddy,Locations.ForestKasplatOwlTree:Kongs.lanky,Locations.ForestKasplatLowerMushroomExterior:Kongs.tiny,Locations.ForestKasplatUpperMushroomExterior:Kongs.chunky,Locations.CavesKasplatNearLab:Kongs.donkey,Locations.CavesKasplatPillar:Kongs.lanky,Locations.CavesKasplatNearCandy:Kongs.tiny,Locations.CavesKasplatOn5DI:Kongs.chunky,Locations.CastleKasplatCrypt:Kongs.diddy,Locations.CastleKasplatHalfway:Kongs.lanky,Locations.CastleKasplatLowerLedge:Kongs.tiny,Locations.CastleKasplatNearCandy:Kongs.chunky}
constants={Locations.JapesKasplatUnderground:Kongs.chunky,Locations.AztecKasplatOnTinyTemple:Kongs.diddy,Locations.AztecKasplatChunky5DT:Kongs.chunky,Locations.CavesKasplatNearFunky:Kongs.diddy,Locations.CastleKasplatTree:Kongs.donkey}
def FindLevel(location):
	'Find the level given a location.'
	for A in Logic.Regions.values():
		for B in A.locations:
			if B.id==location:return A.level
def GetBlueprintItemForKongAndLevel(level,kong):
	'For the Level and Kong enum values, return the Blueprint Item enum tied to it.';B=int(Items.JungleJapesDonkeyBlueprint);A=int(level)
	if A>7:A=7
	return Items(B+5*A+int(kong))
def GetBlueprintLocationForKongAndLevel(level,kong):
	'For the Level and Kong enum values, return the generic Blueprint Location enum tied to it.';B=int(Locations.JapesDonkeyKasplatRando);A=int(level)
	if A>7:A=7
	return Locations(B+5*A+int(kong))
def ShuffleKasplatsAndLocations(spoiler,LogicVariables):
	'Shuffle the location and kong assigned to each kasplat. This should replace ShuffleKasplats if all goes well.';G=LogicVariables;F=spoiler;F.shuffled_kasplat_map={};G.kasplat_map={}
	for B in shufflable:Logic.LocationList.pop(B,None)
	for B in constants:Logic.LocationList.pop(B,None)
	for D in KasplatLocationList:
		H=KasplatLocationList[D];I=GetKongs();random.shuffle(I)
		for C in I:
			J=[]
			for A in H:
				if not A.selected and C in A.kong_lst:J.append(A.name)
			K=random.choice(J)
			for A in H:
				if A.name==K:A.setKasplat();L=GetBlueprintItemForKongAndLevel(D,C);E=GetBlueprintLocationForKongAndLevel(D,C);B=Location(A.name,L,Types.Blueprint,[A.map,C]);B.PlaceDefaultItem();Logic.LocationList[E]=B;M=Logic.Regions[A.region_id];M.locations.append(LocationLogic(E,A.additional_logic));G.kasplat_map[E]=C;F.shuffled_kasplat_map[A.name]=int(C);break
def ResetShuffledKasplatLocations():
	'Reset all placed kasplat locations.'
	for C in KasplatLocationList:
		for A in KasplatLocationList[C]:
			if A.selected:A.setKasplat(state=False);B=Logic.Regions[A.region_id];B.locations=[A for A in B.locations if A.id<Locations.JapesDonkeyKasplatRando or A.id>Locations.IslesChunkyKasplatRando]
def ShuffleKasplats(LogicVariables):
	'Shuffles the kong assigned to each kasplat.';A=LogicVariables;B=[];C=GetKongs()
	for J in range(len(Levels)-1):B.append(C.copy())
	for (I,D) in constants.items():E=FindLevel(I);B[E].remove(D)
	A.kasplat_map={}
	for F in shufflable.keys():A.kasplat_map[F]=Kongs.any
	A.kasplat_map.update(constants);G=list(shufflable.keys());random.shuffle(G)
	while len(G)>0:
		F=G.pop();E=FindLevel(F);C=B[E];random.shuffle(C);H=False
		for D in C:A.kasplat_map[F]=D;B[E].remove(D);H=True;break
		if not H:raise Ex.KasplatOutOfKongs
def KasplatShuffle(spoiler,LogicVariables):
	'Facilitate the shuffling of kasplat types.';A=LogicVariables
	if A.settings.kasplat_rando:
		B=0
		while True:
			try:
				if A.settings.kasplat_location_rando:ShuffleKasplatsAndLocations(spoiler,A)
				else:ShuffleKasplats(A)
				if not Fill.VerifyWorld(A.settings):raise Ex.KasplatPlacementException
				return
			except Ex.KasplatPlacementException:
				if B==5:js.postMessage('Kasplat placement failed, out of retries.');raise Ex.KasplatAttemptCountExceeded
				B+=1;js.postMessage('Kasplat placement failed. Retrying. Tries: '+str(B))
				if A.settings.kasplat_location_rando:ResetShuffledKasplatLocations()
def InitKasplatMap(LogicVariables):'Initialize kasplat_map in logic variables with default values.';A=LogicVariables;A.kasplat_map={};A.kasplat_map.update(shufflable);A.kasplat_map.update(constants)