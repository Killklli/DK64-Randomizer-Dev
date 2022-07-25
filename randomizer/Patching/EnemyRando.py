'Apply Boss Locations.'
from email.policy import default
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
	'Write replaced enemies to ROM.';s='kasplat_swaps';r='container_map';c='index';T='replace_with';S='vanilla_location';N='enemy_id';I='big';F=spoiler;D='offset';A6=[{r:7,s:[{S:0,T:1},{S:1,T:3},{S:2,T:0},{S:3,T:2}]}];t=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];u=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];d=[Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];e=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];f=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];O=[Maps.BeaverBotherEasy,Maps.BeaverBotherNormal,Maps.BeaverBotherHard];U=d.copy();U.extend(e);U.extend(f);U.extend(O);W={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};X=[]
	if F.settings.enemy_rando or F.settings.kasplat_rando:
		X=getBalancedCrownEnemyRando();g=[];h=[];i=[];j=[]
		for J in EnemyMetaData:
			if EnemyMetaData[J].minigame_enabled:
				i.append(J)
				if EnemyMetaData[J].beaver:j.append(J)
				if EnemyMetaData[J].killable:
					h.append(J)
					if EnemyMetaData[J].simple:g.append(J)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];P=[];ROM().seek(C);k=int.from_bytes(ROM().readBytes(2),I);G=2
			if k>0:
				for Y in range(k):ROM().seek(C+G);v=int.from_bytes(ROM().readBytes(2),I);G+=v*6+2;ROM().seek(C+G);w=int.from_bytes(ROM().readBytes(2),I);G+=w*10+6
			ROM().seek(C+G);Z=int.from_bytes(ROM().readBytes(2),I);a={};l=[]
			for Q in W:
				V=[]
				for Y in range(Z):V.append(random.choice(W[Q]))
				a[Q]=V
			for Y in range(Z):l.append(random.choice(X))
			G+=2
			for Y in range(Z):ROM().seek(C+G);x=int.from_bytes(ROM().readBytes(1),I);ROM().seek(C+G+19);y=int.from_bytes(ROM().readBytes(1),I);z=G;ROM().seek(C+G+17);A0=int.from_bytes(ROM().readBytes(1),I);G+=22+A0*2;P.append({N:x,D:z,c:y})
			if F.settings.kasplat_rando and not F.settings.kasplat_location_rando:
				for m in F.enemy_replacements:
					if m[r]==E:
						for n in m[s]:
							A1=n[S]+Enemies.KasplatDK;A2=n[T]+Enemies.KasplatDK
							for A in P:
								if A[N]==A1:ROM().seek(C+A[D]);ROM().writeMultipleBytes(A2,1)
			if F.settings.enemy_rando and E in t:
				for Q in a:
					V=a[Q];A3=W[Q];o=0
					for A in P:
						if A[N]in A3:
							if E!=Maps.FranticFactory or A[c]<35 or A[c]>44:
								B=V[o];o+=1
								if B!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
									if B!=Enemies.Kosha or E!=Maps.CavesDiddyLowerCabin:
										if B!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
											ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
											if B in EnemyMetaData.keys():
												ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
												if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
												ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),I)
												if EnemyMetaData[B].size_cap>0:
													if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
												if F.settings.enemy_speed_rando:
													H=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
													if H>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
			if F.settings.enemy_rando and E in U:
				M=[]
				if E in d:M=g.copy()
				elif E in e:M=h.copy()
				elif E in f:M=i.copy()
				elif E in O:M=j.copy()
				for A in P:
					if A[N]in M:
						B=random.choice(M)
						if E in O:
							A4=random.choice(M)
							if B!=Enemies.BeaverGold or A4!=Enemies.BeaverGold:B=Enemies.BeaverBlue
						ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0:
								if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if F.settings.enemy_speed_rando and E not in O:
								H=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
								if H>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
							if B==Enemies.BeaverGold and E in O:
								for p in [12,13]:
									ROM().seek(C+A[D]+p);A5=int.from_bytes(ROM().readBytes(1),I);b=int(A5*1.1)
									if b>255:b=255
									ROM().seek(C+A[D]+p);ROM().writeMultipleBytes(b,1)
			if F.settings.crown_enemy_rando and E in u:
				q=0
				for A in P:
					if A[N]in X:
						B=l[q];ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1);q+=1
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0:
								if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if F.settings.enemy_speed_rando:
								H=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
								if H>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
					elif A[N]==Enemies.BattleCrownController:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(random.randint(5,60),1)