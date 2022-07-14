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
	'Write replaced enemies to ROM.';n='kasplat_swaps';m='container_map';b='index';S='replace_with';R='vanilla_location';M='enemy_id';I='big';H=spoiler;D='offset';A0=[{m:7,n:[{R:0,S:1},{R:1,S:3},{R:2,S:0},{R:3,S:2}]}];o=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];p=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];c=[Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];d=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];q=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];U=c.copy();U.extend(d);U.extend(q);V={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};W=[]
	if H.settings.enemy_rando or H.settings.kasplat_rando:
		W=getBalancedCrownEnemyRando();e=[];f=[];X=[]
		for L in EnemyMetaData:
			if EnemyMetaData[L].minigame_enabled:
				X.append(L)
				if EnemyMetaData[L].killable:
					f.append(L)
					if EnemyMetaData[L].simple:e.append(L)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];N=[];ROM().seek(C);g=int.from_bytes(ROM().readBytes(2),I);F=2
			if g>0:
				for Y in range(g):ROM().seek(C+F);r=int.from_bytes(ROM().readBytes(2),I);F+=r*6+2;ROM().seek(C+F);s=int.from_bytes(ROM().readBytes(2),I);F+=s*10+6
			ROM().seek(C+F);Z=int.from_bytes(ROM().readBytes(2),I);a={};h=[]
			for O in V:
				T=[]
				for Y in range(Z):T.append(random.choice(V[O]))
				a[O]=T
			for Y in range(Z):h.append(random.choice(W))
			F+=2
			for Y in range(Z):ROM().seek(C+F);t=int.from_bytes(ROM().readBytes(1),I);ROM().seek(C+F+19);u=int.from_bytes(ROM().readBytes(1),I);v=F;ROM().seek(C+F+17);w=int.from_bytes(ROM().readBytes(1),I);F+=22+w*2;N.append({M:t,D:v,b:u})
			if H.settings.kasplat_rando:
				for i in H.enemy_replacements:
					if i[m]==E:
						for j in i[n]:
							x=j[R]+Enemies.KasplatDK;y=j[S]+Enemies.KasplatDK
							for A in N:
								if A[M]==x:ROM().seek(C+A[D]);ROM().writeMultipleBytes(y,1)
			if H.settings.enemy_rando and E in o:
				for O in a:
					T=a[O];z=V[O];k=0
					for A in N:
						if A[M]in z:
							if E!=Maps.FranticFactory or A[b]<35 or A[b]>44:
								B=T[k];k+=1
								if B!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
									if B!=Enemies.Kosha or E!=Maps.CavesDiddyLowerCabin:
										ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
										if B in EnemyMetaData.keys():
											ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
											if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
											ROM().seek(C+A[D]+15);P=int.from_bytes(ROM().readBytes(1),I)
											if EnemyMetaData[B].size_cap>0:
												if P>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
											if H.settings.enemy_speed_rando:
												G=EnemyMetaData[B].min_speed;J=EnemyMetaData[B].max_speed
												if G>0 and J>0:ROM().seek(C+A[D]+13);K=random.randint(G,J);ROM().writeMultipleBytes(K,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(G,K),1)
			if H.settings.enemy_rando and E in U:
				Q=[]
				if E in c:Q=e.copy()
				elif E in d:Q=f.copy()
				elif E in X:Q=X.copy()
				for A in N:
					if A[M]in Q:
						B=random.choice(Q);ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);P=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0:
								if P>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if H.settings.enemy_speed_rando:
								G=EnemyMetaData[B].min_speed;J=EnemyMetaData[B].max_speed
								if G>0 and J>0:ROM().seek(C+A[D]+13);K=random.randint(G,J);ROM().writeMultipleBytes(K,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(G,K),1)
			if H.settings.crown_enemy_rando and E in p:
				l=0
				for A in N:
					if A[M]in W:
						B=h[l];ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1);l+=1
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);P=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0:
								if P>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if H.settings.enemy_speed_rando:
								G=EnemyMetaData[B].min_speed;J=EnemyMetaData[B].max_speed
								if G>0 and J>0:ROM().seek(C+A[D]+13);K=random.randint(G,J);ROM().writeMultipleBytes(K,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(G,K),1)
					elif A[M]==Enemies.BattleCrownController:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(random.randint(5,60),1)