'Test file used for checking all kongs have 100 colored bananas per level.'
import randomizer.CollectibleLogicFiles.AngryAztec as AngryAztec,randomizer.CollectibleLogicFiles.CreepyCastle as CreepyCastle,randomizer.CollectibleLogicFiles.CrystalCaves as CrystalCaves,randomizer.CollectibleLogicFiles.FranticFactory as FranticFactory,randomizer.CollectibleLogicFiles.FungiForest as FungiForest,randomizer.CollectibleLogicFiles.GloomyGalleon as GloomyGalleon,randomizer.CollectibleLogicFiles.JungleJapes as JungleJapes
from randomizer.Enums.Collectibles import Collectibles
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.LogicClasses import Collectible
def __CountBananasForLevel(bananaTotals,collectibles,level):
	for A in collectibles:
		B=0
		if A.type==Collectibles.balloon:B=10
		elif A.type==Collectibles.bunch:B=5
		elif A.type==Collectibles.banana:B=1
		bananaTotals[level][A.kong]+=A.amount*B
bananaTotals=[]
for i in range(7):bananaTotals.append({Kongs.donkey:0,Kongs.diddy:0,Kongs.lanky:0,Kongs.tiny:0,Kongs.chunky:0})
for (region,collectibles) in JungleJapes.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.JungleJapes)
for (region,collectibles) in AngryAztec.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.AngryAztec)
for (region,collectibles) in FranticFactory.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.FranticFactory)
for (region,collectibles) in GloomyGalleon.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.GloomyGalleon)
for (region,collectibles) in FungiForest.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.FungiForest)
for (region,collectibles) in CrystalCaves.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.CrystalCaves)
for (region,collectibles) in CreepyCastle.LogicRegions.items():__CountBananasForLevel(bananaTotals,collectibles,Levels.CreepyCastle)
for level in range(7):
	print(Levels(level).name+' Totals:');levelTotals=bananaTotals[level]
	for (kong,total) in levelTotals.items():print(kong.name+': '+str(total))
print('Done.')