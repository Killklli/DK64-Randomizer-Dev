'Module used to handle setting and randomizing bonus barrels.'
_B='selected'
_A=True
import random,js,randomizer.Fill as Fill,randomizer.Lists.Exceptions as Ex
from randomizer.Enums.Minigames import Minigames
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Settings import Settings
def Reset(barrelLocations):
	'Reset bonus barrel associations.'
	for A in barrelLocations:BarrelMetaData[A].minigame=Minigames.NoGame
def ShuffleBarrels(settings,barrelLocations,minigamePool):
	'Shuffle minigames to different barrels.';J=False;I='skip';F=barrelLocations;D=settings;A=minigamePool;random.shuffle(F);random.shuffle(A)
	while len(F)>0:
		C=F.pop()
		if BarrelMetaData[C].map==Maps.HideoutHelm and D.helm_barrels==I:continue
		elif BarrelMetaData[C].map!=Maps.HideoutHelm and D.bonus_barrels==I:continue
		G=J;H=J
		for B in A:
			if MinigameRequirements[B].helm_enabled:H=_A
		for B in A:
			BarrelMetaData[C].minigame=B
			if not MinigameRequirements[B].helm_enabled and BarrelMetaData[C].map==Maps.HideoutHelm and H is _A:continue
			if D.bonus_barrels!=_B:
				if Fill.VerifyWorld(D):
					A.remove(B)
					if MinigameRequirements[B].repeat:
						E=random.randint(20,len(A))
						if E>=len(A):A.append(B)
						else:A.insert(E,B)
					G=_A;break
				else:BarrelMetaData[C].minigame=Minigames.NoGame
			elif Fill.VerifyWorld(D):
				A.remove(B)
				if MinigameRequirements[B].repeat:
					E=random.randint(int(len(A)/2),len(A))
					if E>=len(A):A.append(B)
					else:A.insert(E,B)
				G=_A;break
			else:BarrelMetaData[C].minigame=Minigames.NoGame
		if not G:raise Ex.BarrelOutOfMinigames
def BarrelShuffle(settings):
	'Facilitate shuffling of barrels.';A=settings;D=list(BarrelMetaData.keys())
	if A.bonus_barrels==_B:E={'batty_barrel_bandit':[Minigames.BattyBarrelBanditVEasy,Minigames.BattyBarrelBanditEasy,Minigames.BattyBarrelBanditNormal,Minigames.BattyBarrelBanditHard],'big_bug_bash':[Minigames.BigBugBashVEasy,Minigames.BigBugBashEasy,Minigames.BigBugBashNormal,Minigames.BigBugBashHard],'busy_barrel_barrage':[Minigames.BusyBarrelBarrageEasy,Minigames.BusyBarrelBarrageNormal,Minigames.BusyBarrelBarrageHard],'mad_maze_maul':[Minigames.MadMazeMaulEasy,Minigames.MadMazeMaulNormal,Minigames.MadMazeMaulHard,Minigames.MadMazeMaulInsane],'minecart_mayhem':[Minigames.MinecartMayhemEasy,Minigames.MinecartMayhemNormal,Minigames.MinecartMayhemHard],'beaver_bother':[Minigames.BeaverBotherEasy,Minigames.BeaverBotherNormal,Minigames.BeaverBotherHard],'teetering_turtle_trouble':[Minigames.TeeteringTurtleTroubleVEasy,Minigames.TeeteringTurtleTroubleEasy,Minigames.TeeteringTurtleTroubleNormal,Minigames.TeeteringTurtleTroubleHard],'stealthy_snoop':[Minigames.StealthySnoopVEasy,Minigames.StealthySnoopEasy,Minigames.StealthySnoopNormal,Minigames.StealthySnoopHard],'stash_snatch':[Minigames.StashSnatchEasy,Minigames.StashSnatchNormal,Minigames.StashSnatchHard,Minigames.StashSnatchInsane],'splish_splash_salvage':[Minigames.SplishSplashSalvageEasy,Minigames.SplishSplashSalvageNormal,Minigames.SplishSplashSalvageHard],'speedy_swing_sortie':[Minigames.SpeedySwingSortieEasy,Minigames.SpeedySwingSortieNormal,Minigames.SpeedySwingSortieHard],'krazy_kong_klamour':[Minigames.KrazyKongKlamourEasy,Minigames.KrazyKongKlamourNormal,Minigames.KrazyKongKlamourHard,Minigames.KrazyKongKlamourInsane],'searchlight_seek':[Minigames.SearchlightSeekVEasy,Minigames.SearchlightSeekEasy,Minigames.SearchlightSeekNormal,Minigames.SearchlightSeekHard],'kremling_kosh':[Minigames.KremlingKoshVEasy,Minigames.KremlingKoshEasy,Minigames.KremlingKoshNormal,Minigames.KremlingKoshHard],'peril_path_panic':[Minigames.PerilPathPanicVEasy,Minigames.PerilPathPanicEasy,Minigames.PerilPathPanicNormal,Minigames.PerilPathPanicHard],'helm_minigames':[Minigames.DonkeyRambi,Minigames.DonkeyTarget,Minigames.DiddyKremling,Minigames.DiddyRocketbarrel,Minigames.LankyMaze,Minigames.LankyShooting,Minigames.TinyMushroom,Minigames.TinyPonyTailTwirl,Minigames.ChunkyHiddenKremling,Minigames.ChunkyShooting]};B=[]
	else:B=[A for A in MinigameRequirements.keys()if A!=Minigames.NoGame]
	if A.bonus_barrels==_B:
		for (F,G) in E.items():
			if F in A.minigames_list_selected:B.extend([A for A in MinigameRequirements.keys()if A in G])
	C=0
	while _A:
		try:
			Reset(D);ShuffleBarrels(A,D.copy(),B.copy())
			if not Fill.VerifyWorld(A):raise Ex.BarrelPlacementException
			return
		except Ex.BarrelPlacementException:
			if C==5:js.postMessage('Minigame placement failed, out of retries.');raise Ex.BarrelAttemptCountExceeded
			C+=1;js.postMessage('Minigame placement failed. Retrying. Tries: '+str(C))