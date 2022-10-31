'Shuffle Crown picks, excluding helm.'
import random,randomizer.Logic as Logic
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Lists.CrownLocations import CrownLocations
from randomizer.LogicClasses import LocationLogic
def ShuffleCrowns(crown_selection,human_crowns):
	'Generate Crown Placement Assortment.';C=Locations.JapesBattleArena
	for A in CrownLocations:
		B=CrownLocations[A];I=list(range(len(B)));D=1
		if A==Levels.DKIsles:D=2
		E=random.sample(I,D);crown_selection[A]=E.copy()
		for (J,F) in enumerate(E):
			G=A.name
			if A==Levels.DKIsles:G=f"{A.name} ({J+1})"
			human_crowns[G]=B[F].name;H=B[F];K=Logic.Regions[H.region];K.locations.append(LocationLogic(Locations(C),H.logic));C+=1