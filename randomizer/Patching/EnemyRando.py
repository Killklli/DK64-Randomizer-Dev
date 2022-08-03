'Apply Boss Locations.'
_B='medium'
_A='off'
from email.policy import default
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def getBalancedCrownEnemyRando(crown_setting):
	'Get array of weighted enemies.';G=False;B=crown_setting;E=[]
	if B!=_A:
		C=10;F=G;H=G
		if B=='easy':C=10;F=True
		elif B==_B:C=6
		elif B=='hard':C=2
		for A in EnemyMetaData.keys():
			if EnemyMetaData[A].crown_enabled:
				if not F or A!=Enemies.GetOut:
					I=EnemyMetaData[A].crown_weight;J=abs(I-C);D=abs(10-J)
					if H:D=10
					if A==Enemies.GetOut:D=1
					for K in range(D):E.append(A)
	return E
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';t='kasplat_swaps';s='container_map';d='index';T='replace_with';S='vanilla_location';N='enemy_id';I='big';E=spoiler;D='offset';A7=[{s:7,t:[{S:0,T:1},{S:1,T:3},{S:2,T:0},{S:3,T:2}]}];u=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];v=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];e=[Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];f=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];g=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];O=[];U=e.copy();U.extend(f);U.extend(g);U.extend(O);X={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};Y=[]
	if E.settings.enemy_rando or E.settings.kasplat_rando or E.settings.crown_enemy_rando!=_A:
		Y=getBalancedCrownEnemyRando(E.settings.crown_enemy_rando);h=[];i=[];j=[];k=[]
		for J in EnemyMetaData:
			if EnemyMetaData[J].minigame_enabled:
				j.append(J)
				if EnemyMetaData[J].beaver:k.append(J)
				if EnemyMetaData[J].killable:
					i.append(J)
					if EnemyMetaData[J].simple:h.append(J)
		for F in range(216):
			C=js.pointer_addresses[16]['entries'][F]['pointing_to'];P=[];ROM().seek(C);l=int.from_bytes(ROM().readBytes(2),I);G=2
			if l>0:
				for Z in range(l):ROM().seek(C+G);w=int.from_bytes(ROM().readBytes(2),I);G+=w*6+2;ROM().seek(C+G);x=int.from_bytes(ROM().readBytes(2),I);G+=x*10+6
			ROM().seek(C+G);a=int.from_bytes(ROM().readBytes(2),I);b={}
			for Q in X:
				V=[]
				for Z in range(a):V.append(random.choice(X[Q]))
				b[Q]=V
			if E.settings.crown_enemy_rando!=_A:
				m=[]
				for Z in range(a):m.append(random.choice(Y))
			G+=2
			for Z in range(a):ROM().seek(C+G);y=int.from_bytes(ROM().readBytes(1),I);ROM().seek(C+G+19);z=int.from_bytes(ROM().readBytes(1),I);A0=G;ROM().seek(C+G+17);A1=int.from_bytes(ROM().readBytes(1),I);G+=22+A1*2;P.append({N:y,D:A0,d:z})
			if E.settings.kasplat_rando and not E.settings.kasplat_location_rando:
				for n in E.enemy_replacements:
					if n[s]==F:
						for o in n[t]:
							A2=o[S]+Enemies.KasplatDK;A3=o[T]+Enemies.KasplatDK
							for B in P:
								if B[N]==A2:ROM().seek(C+B[D]);ROM().writeMultipleBytes(A3,1)
			if E.settings.enemy_rando and F in u:
				for Q in b:
					V=b[Q];A4=X[Q];p=0
					for B in P:
						if B[N]in A4:
							if F!=Maps.FranticFactory or B[d]<35 or B[d]>44:
								A=V[p];p+=1
								if F!=Maps.ForestSpider or EnemyMetaData[A].aggro!=4:
									if A!=Enemies.Book or F not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
										if A!=Enemies.Kosha or F!=Maps.CavesDiddyLowerCabin:
											if A!=Enemies.Guard or F not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
												ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
												if A in EnemyMetaData.keys():
													ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
													if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
													ROM().seek(C+B[D]+15);R=int.from_bytes(ROM().readBytes(1),I)
													if EnemyMetaData[A].size_cap>0:
														if R>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
													if E.settings.enemy_speed_rando:
														H=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
														if H>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
			if E.settings.enemy_rando and F in U:
				M=[]
				if F in e:M=h.copy()
				elif F in f:M=i.copy()
				elif F in g:M=j.copy()
				elif F in O:M=k.copy()
				for B in P:
					if B[N]in M:
						A=random.choice(M)
						if F in O:
							A5=random.choice(M)
							if A!=Enemies.BeaverGold or A5!=Enemies.BeaverGold:A=Enemies.BeaverBlue
						ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);R=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[A].size_cap>0:
								if R>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if E.settings.enemy_speed_rando and F not in O:
								H=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
								if H>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
							if A==Enemies.BeaverGold and F in O:
								for q in [12,13]:
									ROM().seek(C+B[D]+q);A6=int.from_bytes(ROM().readBytes(1),I);c=int(A6*1.1)
									if c>255:c=255
									ROM().seek(C+B[D]+q);ROM().writeMultipleBytes(c,1)
			if E.settings.crown_enemy_rando!=_A and F in v:
				r=0
				for B in P:
					if B[N]in Y:
						A=m[r];ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1);r+=1
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);R=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[A].size_cap>0:
								if R>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if E.settings.enemy_speed_rando:
								H=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
								if H>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
					elif B[N]==Enemies.BattleCrownController:
						ROM().seek(C+B[D]+11);W=5
						if E.settings.crown_enemy_rando=='easy':W=5
						elif E.settings.crown_enemy_rando==_B:W=15
						elif E.settings.crown_enemy_rando=='hard':W=30
						ROM().writeMultipleBytes(random.randint(W,60),1)