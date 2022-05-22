'Module used to handle setting and randomizing bonus barrels.'
_A='all_beaver_bother'
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex
from randomizer.Settings import Settings
from randomizer.Enums.Minigames import Minigames
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Lists.MapsAndExits import Maps
def Reset(barrelLocations):
	'Reset bonus barrel associations.'
	for A in barrelLocations:BarrelMetaData[A].minigame=Minigames.NoGame
def ShuffleBarrels(settings,barrelLocations,minigamePool):
	'Shuffle minigames to different barrels.';H='skip';E=barrelLocations;C=settings;A=minigamePool;random.shuffle(E);random.shuffle(A)
	while len(E)>0:
		D=E.pop()
		if BarrelMetaData[D].map==Maps.HideoutHelm and C.helm_barrels==H:continue
		elif BarrelMetaData[D].map!=Maps.HideoutHelm and C.bonus_barrels==H:continue
		F=False
		for B in A:
			BarrelMetaData[D].minigame=B
			if C.bonus_barrels!=_A:
				if not MinigameRequirements[B].helm_enabled and BarrelMetaData[D].map==Maps.HideoutHelm:continue
			if C.bonus_barrels!=_A:
				if Fill.VerifyWorld(C):
					A.remove(B)
					if MinigameRequirements[B].repeat:
						G=random.randint(20,len(A))
						if G>=len(A):A.append(B)
						else:A.insert(G,B)
					F=True;break
				else:BarrelMetaData[D].minigame=Minigames.NoGame
			else:random.shuffle(A);F=True;break
		if not F:raise Ex.BarrelOutOfMinigames
def BarrelShuffle(settings):
	'Facilitate shuffling of barrels.';E='random';A=settings
	if A.bonus_barrels==E or A.bonus_barrels==_A or A.helm_barrels==E or A.helm_barrels==_A:
		C=[A for A in BarrelMetaData.keys()];D=[A for A in MinigameRequirements.keys()if A!=Minigames.NoGame]
		if A.bonus_barrels==_A or A.helm_barrels==_A:D=[A for A in MinigameRequirements.keys()if A==Minigames.BeaverBotherEasy or A==Minigames.BeaverBotherNormal or A==Minigames.BeaverBotherHard]
		B=0
		while True:
			try:
				Reset(C);ShuffleBarrels(A,C.copy(),D.copy())
				if not Fill.VerifyWorld(A):raise Ex.BarrelPlacementException
				return
			except Ex.BarrelPlacementException:
				if B==5:js.postMessage('Minigame placement failed, out of retries.');raise Ex.BarrelAttemptCountExceeded
				else:B+=1;js.postMessage('Minigame placement failed. Retrying. Tries: '+str(B))