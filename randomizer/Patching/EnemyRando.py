'Apply Boss Locations.'
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def getBalancedCrownEnemyRando():
	'Get array of weighted enemies.';B=[]
	for A in EnemyMetaData.keys():
		if EnemyMetaData[A].crown_enabled:
			for C in range(EnemyMetaData[A].crown_weight):B.append(A)
	return B
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';b='index';T='replace_with';S='vanilla_location';P='enemy_id';I=spoiler;H='big';D='offset';u=[{'container_map':7,'kasplat_swaps':[{S:0,T:1},{S:1,T:3},{S:2,T:0},{S:3,T:2}]}];k=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];l=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];c=[Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];d=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];m=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];U=c.copy();U.extend(d);U.extend(m);V={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};W=[]
	if I.settings.enemy_rando or I.settings.kasplat_rando:
		W=getBalancedCrownEnemyRando();e=[];f=[];X=[]
		for L in EnemyMetaData:
			if EnemyMetaData[L].minigame_enabled:
				X.append(L)
				if EnemyMetaData[L].killable:
					f.append(L)
					if EnemyMetaData[L].simple:e.append(L)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];Q=[];ROM().seek(C);g=int.from_bytes(ROM().readBytes(2),H);F=2
			if g>0:
				for Y in range(g):ROM().seek(C+F);n=int.from_bytes(ROM().readBytes(2),H);F+=n*6+2;ROM().seek(C+F);o=int.from_bytes(ROM().readBytes(2),H);F+=o*10+6
			ROM().seek(C+F);Z=int.from_bytes(ROM().readBytes(2),H);a={};h=[]
			for M in V:
				R=[]
				for Y in range(Z):R.append(random.choice(V[M]))
				a[M]=R
			for Y in range(Z):h.append(random.choice(W))
			F+=2
			for Y in range(Z):ROM().seek(C+F);p=int.from_bytes(ROM().readBytes(1),H);ROM().seek(C+F+19);q=int.from_bytes(ROM().readBytes(1),H);r=F;ROM().seek(C+F+17);s=int.from_bytes(ROM().readBytes(1),H);F+=22+s*2;Q.append({P:p,D:r,b:q})
			if I.settings.enemy_rando and E in k:
				for M in a:
					R=a[M];t=V[M];i=0
					for B in Q:
						if B[P]in t:
							if E!=Maps.FranticFactory or B[b]<35 or B[b]>44:
								A=R[i];i+=1
								if A!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
									if A!=Enemies.Kosha or E!=Maps.CavesDiddyLowerCabin:
										if A!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
											ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
											if A in EnemyMetaData.keys():
												ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
												if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
												ROM().seek(C+B[D]+15);N=int.from_bytes(ROM().readBytes(1),H)
												if EnemyMetaData[A].size_cap>0:
													if N>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
												if I.settings.enemy_speed_rando:
													G=EnemyMetaData[A].min_speed;J=EnemyMetaData[A].max_speed
													if G>0 and J>0:ROM().seek(C+B[D]+13);K=random.randint(G,J);ROM().writeMultipleBytes(K,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(G,K),1)
			if I.settings.enemy_rando and E in U:
				O=[]
				if E in c:O=e.copy()
				elif E in d:O=f.copy()
				elif E in X:O=X.copy()
				for B in Q:
					if B[P]in O:
						A=random.choice(O);ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);N=int.from_bytes(ROM().readBytes(1),H)
							if EnemyMetaData[A].size_cap>0:
								if N>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if I.settings.enemy_speed_rando:
								G=EnemyMetaData[A].min_speed;J=EnemyMetaData[A].max_speed
								if G>0 and J>0:ROM().seek(C+B[D]+13);K=random.randint(G,J);ROM().writeMultipleBytes(K,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(G,K),1)
			if I.settings.crown_enemy_rando and E in l:
				j=0
				for B in Q:
					if B[P]in W:
						A=h[j];ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1);j+=1
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);N=int.from_bytes(ROM().readBytes(1),H)
							if EnemyMetaData[A].size_cap>0:
								if N>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if I.settings.enemy_speed_rando:
								G=EnemyMetaData[A].min_speed;J=EnemyMetaData[A].max_speed
								if G>0 and J>0:ROM().seek(C+B[D]+13);K=random.randint(G,J);ROM().writeMultipleBytes(K,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(G,K),1)
					elif B[P]==Enemies.BattleCrownController:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(random.randint(5,60),1)