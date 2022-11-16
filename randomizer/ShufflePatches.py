'Shuffle Dirt Patch Locations.'
_A=False
import random,randomizer.CollectibleLogicFiles.AngryAztec,randomizer.CollectibleLogicFiles.CreepyCastle,randomizer.CollectibleLogicFiles.CrystalCaves,randomizer.CollectibleLogicFiles.DKIsles,randomizer.CollectibleLogicFiles.FranticFactory,randomizer.CollectibleLogicFiles.FungiForest,randomizer.CollectibleLogicFiles.GloomyGalleon,randomizer.CollectibleLogicFiles.JungleJapes
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Lists.Patches import DirtPatchLocations
from randomizer.LogicClasses import Collectible
from randomizer.Spoiler import Spoiler
def addPatch(patch):
	'Add patch to relevant Logic Region.';A=patch;C={Levels.DKIsles:randomizer.CollectibleLogicFiles.DKIsles.LogicRegions,Levels.JungleJapes:randomizer.CollectibleLogicFiles.JungleJapes.LogicRegions,Levels.AngryAztec:randomizer.CollectibleLogicFiles.AngryAztec.LogicRegions,Levels.FranticFactory:randomizer.CollectibleLogicFiles.FranticFactory.LogicRegions,Levels.GloomyGalleon:randomizer.CollectibleLogicFiles.GloomyGalleon.LogicRegions,Levels.FungiForest:randomizer.CollectibleLogicFiles.FungiForest.LogicRegions,Levels.CrystalCaves:randomizer.CollectibleLogicFiles.CrystalCaves.LogicRegions,Levels.CreepyCastle:randomizer.CollectibleLogicFiles.CreepyCastle.LogicRegions};B=C[A.level_name]
	if A.logicregion in B:B[A.logicregion].append(Collectible(Collectibles.coin,Kongs.any,A.logic,None,1,True,_A))
	else:B[A.logicregion]=[Collectible(Collectibles.coin,Kongs.any,A.logic,None,1,True,_A)]
def removePatches():
	'Remove all patches from Logic regions.';C=[randomizer.CollectibleLogicFiles.DKIsles.LogicRegions,randomizer.CollectibleLogicFiles.JungleJapes.LogicRegions,randomizer.CollectibleLogicFiles.AngryAztec.LogicRegions,randomizer.CollectibleLogicFiles.FranticFactory.LogicRegions,randomizer.CollectibleLogicFiles.GloomyGalleon.LogicRegions,randomizer.CollectibleLogicFiles.FungiForest.LogicRegions,randomizer.CollectibleLogicFiles.CrystalCaves.LogicRegions,randomizer.CollectibleLogicFiles.CreepyCastle.LogicRegions]
	for B in C:
		for D in B:
			E=B[D]
			for A in E:
				if A.type==Collectibles.coin and A.kong==Kongs.any:A.enabled=_A
def ShufflePatches(spoiler,human_spoiler):
	'Shuffle Dirt Patch Locations.';C=human_spoiler;B=spoiler;removePatches();B.dirt_patch_placement=[];A={Levels.DKIsles:[],Levels.JungleJapes:[],Levels.AngryAztec:[],Levels.FranticFactory:[],Levels.GloomyGalleon:[],Levels.FungiForest:[],Levels.CrystalCaves:[],Levels.CreepyCastle:[]}
	for D in DirtPatchLocations:D.setPatch(_A);A[D.level_name].append(D)
	select_random_dirt_from_area(A[Levels.DKIsles],4,B,C);del A[Levels.DKIsles]
	for D in range(5):E=random.choice(list(A.keys()));F=A[E];select_random_dirt_from_area(F,2,B,C);del A[E]
	for E in A.keys():F=A[E];select_random_dirt_from_area(F,1,B,C)
	return C.copy()
def select_random_dirt_from_area(area_dirt,amount,spoiler,human_spoiler):
	'Select <amount> random dirt patches from <area_dirt>, which is a list of dirt patches. Makes sure max 1 dirt patch per group is selected.';D=amount;B=area_dirt
	for E in range(D):
		C=random.choice(B)
		for A in DirtPatchLocations:
			if A.name==C.name:A.setPatch(True);addPatch(A);human_spoiler.append(A.name);spoiler.dirt_patch_placement.append(A.name);B.remove(C);break
		if D>1:B=[A for A in B if A.group!=C.group]