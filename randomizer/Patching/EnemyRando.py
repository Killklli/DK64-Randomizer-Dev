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
	'Write replaced enemies to ROM.';c='index';V='replace_with';U='vanilla_location';Q='enemy_id';I=spoiler;H='big';D='offset';A0=[{'container_map':7,'kasplat_swaps':[{U:0,V:1},{U:1,V:3},{U:2,V:0},{U:3,V:2}]}];p=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];q=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];d=[Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];e=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];f=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];N=[Maps.BeaverBotherEasy,Maps.BeaverBotherNormal,Maps.BeaverBotherHard];R=d.copy();R.extend(e);R.extend(f);R.extend(N);W={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};X=[]
	if I.settings.enemy_rando or I.settings.kasplat_rando:
		X=getBalancedCrownEnemyRando();g=[];h=[];i=[];j=[]
		for J in EnemyMetaData:
			if EnemyMetaData[J].minigame_enabled:
				i.append(J)
				if EnemyMetaData[J].beaver:j.append(J)
				if EnemyMetaData[J].killable:
					h.append(J)
					if EnemyMetaData[J].simple:g.append(J)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];S=[];ROM().seek(C);k=int.from_bytes(ROM().readBytes(2),H);F=2
			if k>0:
				for Y in range(k):ROM().seek(C+F);r=int.from_bytes(ROM().readBytes(2),H);F+=r*6+2;ROM().seek(C+F);s=int.from_bytes(ROM().readBytes(2),H);F+=s*10+6
			ROM().seek(C+F);Z=int.from_bytes(ROM().readBytes(2),H);a={};l=[]
			for O in W:
				T=[]
				for Y in range(Z):T.append(random.choice(W[O]))
				a[O]=T
			for Y in range(Z):l.append(random.choice(X))
			F+=2
			for Y in range(Z):ROM().seek(C+F);t=int.from_bytes(ROM().readBytes(1),H);ROM().seek(C+F+19);u=int.from_bytes(ROM().readBytes(1),H);v=F;ROM().seek(C+F+17);w=int.from_bytes(ROM().readBytes(1),H);F+=22+w*2;S.append({Q:t,D:v,c:u})
			if I.settings.enemy_rando and E in p:
				for O in a:
					T=a[O];x=W[O];m=0
					for B in S:
						if B[Q]in x:
							if E!=Maps.FranticFactory or B[c]<35 or B[c]>44:
								A=T[m];m+=1
								if A!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
									if A!=Enemies.Kosha or E!=Maps.CavesDiddyLowerCabin:
										if A!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
											ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
											if A in EnemyMetaData.keys():
												ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
												if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
												ROM().seek(C+B[D]+15);P=int.from_bytes(ROM().readBytes(1),H)
												if EnemyMetaData[A].size_cap>0:
													if P>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
												if I.settings.enemy_speed_rando:
													G=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
													if G>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(G,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(G,L),1)
			if I.settings.enemy_rando and E in R:
				M=[]
				if E in d:M=g.copy()
				elif E in e:M=h.copy()
				elif E in f:M=i.copy()
				elif E in N:M=j.copy()
				for B in S:
					if B[Q]in M:
						A=random.choice(M)
						if E in N:
							y=random.choice(M)
							if A!=Enemies.BeaverGold or y!=Enemies.BeaverGold:A=Enemies.BeaverBlue
						ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);P=int.from_bytes(ROM().readBytes(1),H)
							if EnemyMetaData[A].size_cap>0:
								if P>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if I.settings.enemy_speed_rando and E not in N:
								G=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
								if G>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(G,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(G,L),1)
							if A==Enemies.BeaverGold and E in N:
								for n in [12,13]:
									ROM().seek(C+B[D]+n);z=int.from_bytes(ROM().readBytes(1),H);b=int(z*1.1)
									if b>255:b=255
									ROM().seek(C+B[D]+n);ROM().writeMultipleBytes(b,1)
			if I.settings.crown_enemy_rando and E in q:
				o=0
				for B in S:
					if B[Q]in X:
						A=l[o];ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1);o+=1
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);P=int.from_bytes(ROM().readBytes(1),H)
							if EnemyMetaData[A].size_cap>0:
								if P>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if I.settings.enemy_speed_rando:
								G=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
								if G>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(G,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(G,L),1)
					elif B[Q]==Enemies.BattleCrownController:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(random.randint(5,60),1)