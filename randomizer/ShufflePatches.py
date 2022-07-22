'Shuffle Dirt Patch Locations.'
_A=False
import randomizer.CollectibleLogicFiles.AngryAztec,randomizer.CollectibleLogicFiles.CreepyCastle,randomizer.CollectibleLogicFiles.CrystalCaves,randomizer.CollectibleLogicFiles.DKIsles,randomizer.CollectibleLogicFiles.FranticFactory,randomizer.CollectibleLogicFiles.FungiForest,randomizer.CollectibleLogicFiles.GloomyGalleon,randomizer.CollectibleLogicFiles.JungleJapes
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Levels import Levels
from randomizer.LogicClasses import Collectible
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.Patches import DirtPatchLocations
import random
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
	'Shuffle Dirt Patch Locations.';E=human_spoiler;D=spoiler;removePatches();B=[];D.dirt_patch_placement=[]
	for C in DirtPatchLocations:C.setPatch(_A);B.append(C.name)
	for C in range(16):
		F=random.choice(B)
		for A in DirtPatchLocations:
			if A.name==F:A.setPatch(True);addPatch(A);E.append(A.name);D.dirt_patch_placement.append(A.name);B.remove(F)
	return E.copy()