'Apply Boss Locations.'
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';g='kasplat_swaps';f='container_map';X='index';O='enemy_id';N='replace_with';M='vanilla_location';I=spoiler;G='big';D='offset';s=[{f:7,g:[{M:0,N:1},{M:1,N:3},{M:2,N:0},{M:3,N:2}]}];h=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];i=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];R={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};S=[]
	if I.settings.enemy_rando or I.settings.kasplat_rando:
		for Y in EnemyMetaData.keys():
			if EnemyMetaData[Y].crown_enabled:S.append(Y)
		for F in range(216):
			B=js.pointer_addresses[16]['entries'][F]['pointing_to'];P=[];ROM().seek(B);Z=int.from_bytes(ROM().readBytes(2),G);E=2
			if Z>0:
				for T in range(Z):ROM().seek(B+E);j=int.from_bytes(ROM().readBytes(2),G);E+=j*6+2;ROM().seek(B+E);k=int.from_bytes(ROM().readBytes(2),G);E+=k*10+6
			ROM().seek(B+E);U=int.from_bytes(ROM().readBytes(2),G);V={};a=[]
			for J in R:
				Q=[]
				for T in range(U):Q.append(random.choice(R[J]))
				V[J]=Q
			for T in range(U):a.append(random.choice(S))
			E+=2
			for T in range(U):ROM().seek(B+E);l=int.from_bytes(ROM().readBytes(1),G);ROM().seek(B+E+19);m=int.from_bytes(ROM().readBytes(1),G);n=E;ROM().seek(B+E+17);o=int.from_bytes(ROM().readBytes(1),G);E+=22+o*2;P.append({O:l,D:n,X:m})
			if I.settings.kasplat_rando:
				for b in I.enemy_replacements:
					if b[f]==F:
						for c in b[g]:
							p=c[M]+Enemies.KasplatDK;q=c[N]+Enemies.KasplatDK
							for A in P:
								if A[O]==p:ROM().seek(B+A[D]);ROM().writeMultipleBytes(q,1)
			if I.settings.enemy_rando and F in h:
				for J in V:
					Q=V[J];r=R[J];d=0
					for A in P:
						if A[O]in r:
							if F!=Maps.FranticFactory or A[X]<35 or A[X]>44:
								C=Q[d];d+=1
								if C!=Enemies.Book or F!=Maps.CavesDonkeyCabin and F!=Maps.JapesLankyCave and F!=Maps.AngryAztecLobby:
									if C!=Enemies.Bug or F!=Maps.CavesDiddyLowerCabin:
										ROM().seek(B+A[D]);ROM().writeMultipleBytes(C,1)
										if C in EnemyMetaData.keys():
											ROM().seek(B+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[C].aggro,1)
											if C==Enemies.RoboKremling:ROM().seek(B+A[D]+11);ROM().writeMultipleBytes(200,1)
											ROM().seek(B+A[D]+15);W=int.from_bytes(ROM().readBytes(1),G)
											if EnemyMetaData[C].size_cap>0:
												if W>EnemyMetaData[C].size_cap:ROM().seek(B+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[C].size_cap,1)
											H=EnemyMetaData[C].min_speed;K=EnemyMetaData[C].max_speed
											if H>0 and K>0:ROM().seek(B+A[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(B+A[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
			if I.settings.enemy_rando and F in i:
				e=0
				for A in P:
					if A[O]in S:
						C=a[e];ROM().seek(B+A[D]);ROM().writeMultipleBytes(C,1);e+=1
						if C in EnemyMetaData.keys():
							ROM().seek(B+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[C].aggro,1)
							if C==Enemies.RoboKremling:ROM().seek(B+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[C].air:ROM().seek(B+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(B+A[D]+15);W=int.from_bytes(ROM().readBytes(1),G)
							if EnemyMetaData[C].size_cap>0:
								if W>EnemyMetaData[C].size_cap:ROM().seek(B+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[C].size_cap,1)
							H=EnemyMetaData[C].min_speed;K=EnemyMetaData[C].max_speed
							if H>0 and K>0:ROM().seek(B+A[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(B+A[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
					elif A[O]==Enemies.BattleCrownController:ROM().seek(B+A[D]+11);ROM().writeMultipleBytes(random.randint(5,60),1)