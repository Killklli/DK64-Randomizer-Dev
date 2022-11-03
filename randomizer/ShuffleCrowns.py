'Shuffle Crown picks, excluding helm.'
import random,randomizer.Logic as Logic
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Lists.CrownLocations import CrownLocations
from randomizer.LogicClasses import LocationLogic
def ShuffleCrowns(crown_selection,human_crowns):
	'Generate Crown Placement Assortment.';M=False;H=True;I=Locations.JapesBattleArena
	for C in CrownLocations:
		D=CrownLocations[C];N=list(range(len(D)));J=1
		if C==Levels.DKIsles:J=2
		E=random.sample(N,J);F={}
		for B in E:F[B]=0
		if C==Levels.DKIsles:
			G=[M,M]
			for B in E:
				A=D[B];A.placement_subindex=A.default_index
				if A.is_vanilla:G[A.placement_subindex]=H
			for B in E:
				A=D[B]
				if not A.is_vanilla:
					if G[0]:A.placement_subindex=1;F[B]=1;G[1]=H
					else:A.placement_index=0;F[B]=0;G[0]=H
		crown_selection[C]=F
		for (B,A) in enumerate(E):
			K=C.name
			if C==Levels.DKIsles:K=f"{C.name} ({2-D[A].placement_subindex})"
			human_crowns[K]=D[A].name;L=D[A];O=Logic.Regions[L.region];O.locations.append(LocationLogic(Locations(I),L.logic));I+=1