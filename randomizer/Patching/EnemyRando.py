'Apply Boss Locations.'
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';f='kasplat_swaps';e='container_map';O='enemy_id';N='replace_with';M='vanilla_location';I=spoiler;F='big';D='offset';q=[{e:7,f:[{M:0,N:1},{M:1,N:3},{M:2,N:0},{M:3,N:2}]}];g=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestSpider,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];h=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];R={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};S=[]
	if I.settings.enemy_rando or I.settings.kasplat_rando:
		for X in EnemyMetaData.keys():
			if EnemyMetaData[X].crown_enabled:S.append(X)
		for G in range(216):
			A=js.pointer_addresses[16]['entries'][G]['pointing_to'];P=[];ROM().seek(A);Y=int.from_bytes(ROM().readBytes(2),F);E=2
			if Y>0:
				for T in range(Y):ROM().seek(A+E);i=int.from_bytes(ROM().readBytes(2),F);E+=i*6+2;ROM().seek(A+E);j=int.from_bytes(ROM().readBytes(2),F);E+=j*10+6
			ROM().seek(A+E);U=int.from_bytes(ROM().readBytes(2),F);V={};Z=[]
			for J in R:
				Q=[]
				for T in range(U):Q.append(random.choice(R[J]))
				V[J]=Q
			for T in range(U):Z.append(random.choice(S))
			E+=2
			for T in range(U):ROM().seek(A+E);k=int.from_bytes(ROM().readBytes(1),F);l=E;ROM().seek(A+E+17);m=int.from_bytes(ROM().readBytes(1),F);E+=22+m*2;P.append({O:k,D:l})
			if I.settings.kasplat_rando:
				for a in I.enemy_replacements:
					if a[e]==G:
						for b in a[f]:
							n=b[M]+Enemies.KasplatDK;o=b[N]+Enemies.KasplatDK
							for B in P:
								if B[O]==n:ROM().seek(A+B[D]);ROM().writeMultipleBytes(o,1)
			if I.settings.enemy_rando and G in g:
				for J in V:
					Q=V[J];p=R[J];c=0
					for B in P:
						if B[O]in p:
							C=Q[c];c+=1
							if C!=Enemies.Book or G!=Maps.CavesDonkeyCabin and G!=Maps.JapesLankyCave and G!=Maps.AngryAztecLobby:
								ROM().seek(A+B[D]);ROM().writeMultipleBytes(C,1)
								if C in EnemyMetaData.keys():
									ROM().seek(A+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[C].aggro,1)
									if C==Enemies.RoboKremling:ROM().seek(A+B[D]+11);ROM().writeMultipleBytes(200,1)
									ROM().seek(A+B[D]+15);W=int.from_bytes(ROM().readBytes(1),F)
									if EnemyMetaData[C].size_cap>0:
										if W>EnemyMetaData[C].size_cap:ROM().seek(A+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[C].size_cap,1)
									H=EnemyMetaData[C].min_speed;K=EnemyMetaData[C].max_speed
									if H>0 and K>0:ROM().seek(A+B[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(A+B[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
			if I.settings.enemy_rando and G in h:
				d=0
				for B in P:
					if B[O]in S:
						C=Z[d];ROM().seek(A+B[D]);ROM().writeMultipleBytes(C,1);d+=1
						if C in EnemyMetaData.keys():
							ROM().seek(A+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[C].aggro,1)
							if C==Enemies.RoboKremling:ROM().seek(A+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[C].air:ROM().seek(A+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(A+B[D]+15);W=int.from_bytes(ROM().readBytes(1),F)
							if EnemyMetaData[C].size_cap>0:
								if W>EnemyMetaData[C].size_cap:ROM().seek(A+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[C].size_cap,1)
							H=EnemyMetaData[C].min_speed;K=EnemyMetaData[C].max_speed
							if H>0 and K>0:ROM().seek(A+B[D]+13);L=random.randint(H,K);ROM().writeMultipleBytes(L,1);ROM().seek(A+B[D]+12);ROM().writeMultipleBytes(random.randint(H,L),1)
					elif B[O]==Enemies.BattleCrownController:ROM().seek(A+B[D]+11);ROM().writeMultipleBytes(random.randint(5,60),1)