'Module used to handle setting and randomizing bonus barrels.'
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex
from randomizer.Enums.Minigames import Minigames
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Lists.MapsAndExits import Maps
def Reset(barrelLocations):
	'Reset bonus barrel associations.'
	for A in barrelLocations:BarrelMetaData[A].minigame=Minigames.NoGame
def ShuffleBarrels(settings,barrelLocations,minigamePool):
	'Shuffle minigames to different barrels.';C=barrelLocations;A=minigamePool;random.shuffle(C);random.shuffle(A)
	while len(C)>0:
		D=C.pop();E=False
		for B in A:
			BarrelMetaData[D].minigame=B
			if not MinigameRequirements[B].helm_enabled and BarrelMetaData[D].map==Maps.HideoutHelm:continue
			if Fill.VerifyWorld(settings):
				A.remove(B)
				if MinigameRequirements[B].repeat:
					F=random.randint(20,len(A))
					if F>=len(A):A.append(B)
					else:A.insert(F,B)
				E=True;break
			else:BarrelMetaData[D].minigame=Minigames.NoGame
		if not E:raise Ex.BarrelOutOfMinigames
def BarrelShuffle(settings):
	'Facilitate shuffling of barrels.';B=settings;C=[A for A in BarrelMetaData.keys()];D=[A for A in MinigameRequirements.keys()if A!=Minigames.NoGame];A=0
	while True:
		try:
			Reset(C);ShuffleBarrels(B,C.copy(),D.copy())
			if not Fill.VerifyWorld(B):raise Ex.BarrelPlacementException
			return
		except Ex.BarrelPlacementException:
			if A==5:js.postMessage('Minigame placement failed, out of retries.');raise Ex.BarrelAttemptCountExceeded
			else:A+=1;js.postMessage('Minigame placement failed. Retrying. Tries: '+str(A))