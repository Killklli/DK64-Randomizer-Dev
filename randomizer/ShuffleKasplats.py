'Module used to handle setting and randomizing kasplats.'
import random,js
from randomizer.Enums.Items import Items
from randomizer.Enums.Types import Types
import randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex
from randomizer.Lists.KasplatLocations import KasplatLocationList
from randomizer.Lists.Location import Location
from randomizer.Lists.MapsAndExits import Maps
import randomizer.Logic as Logic
from randomizer.Enums.Kongs import Kongs,GetKongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
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
	'Shuffle the location and kong assigned to each kasplat. This should replace ShuffleKasplats if all goes well.';H=LogicVariables;G=spoiler;G.shuffled_kasplat_map={};H.kasplat_map={}
	for B in shufflable:Logic.LocationList.pop(B,None)
	for B in constants:Logic.LocationList.pop(B,None)
	for D in KasplatLocationList:
		E=KasplatLocationList[D]
		for A in E:A.setKasplat(state=False)
		J=GetKongs()
		for (K,C) in enumerate(J):
			I=[]
			for A in E:
				if not A.selected and C in A.kong_lst:I.append(A.name)
			L=random.choice(I)
			for A in E:
				if A.name==L:A.setKasplat();M=GetBlueprintItemForKongAndLevel(D,C);F=GetBlueprintLocationForKongAndLevel(D,C);B=Location(A.name,M,Types.Blueprint,[A.map,C]);B.PlaceDefaultItem();Logic.LocationList[F]=B;N=Logic.Regions[A.region_id];N.locations.append(LocationLogic(F,lambda l:A.additional_logic(l)));H.kasplat_map[F]=C;G.shuffled_kasplat_map[A.name]=K;break
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
				ShuffleKasplatsAndLocations(spoiler,A)
				if not Fill.VerifyWorld(A.settings):raise Ex.KasplatPlacementException
				return
			except Ex.KasplatPlacementException:
				if B==5:js.postMessage('Kasplat placement failed, out of retries.');raise Ex.KasplatAttemptCountExceeded
				B+=1;js.postMessage('Kasplat placement failed. Retrying. Tries: '+str(B))
def InitKasplatMap(LogicVariables):'Initialize kasplat_map in logic variables with default values.';A=LogicVariables;A.kasplat_map={};A.kasplat_map.update(shufflable);A.kasplat_map.update(constants)