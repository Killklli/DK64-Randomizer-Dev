'Apply Boss Locations.'
_C='medium'
_B='off'
_A=True
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def getBalancedCrownEnemyRando(crown_setting,damage_ohko_setting):
	'Get array of weighted enemies.';N=damage_ohko_setting;J=crown_setting;I=False;C={}
	if J!=_B:
		C={Maps.JapesCrown:[],Maps.AztecCrown:[],Maps.FactoryCrown:[],Maps.GalleonCrown:[],Maps.ForestCrown:[],Maps.CavesCrown:[],Maps.CastleCrown:[],Maps.HelmCrown:[],Maps.SnidesCrown:[],Maps.LobbyCrown:[]};O=[];K=[];L=[];G=[];M=[]
		for B in EnemyMetaData:
			if EnemyMetaData[B].crown_enabled and B is not Enemies.GetOut:
				O.append(B)
				if EnemyMetaData[B].disruptive<=1:K.append(B)
				if EnemyMetaData[B].kasplat is _A:L.append(B)
				elif EnemyMetaData[B].disruptive==0:L.append(B);G.append(B)
		T=2
		for B in EnemyMetaData.keys():
			if EnemyMetaData[B].crown_enabled:
				U=EnemyMetaData[B].crown_weight;V=abs(U-T);P=abs(10-V)
				if B==Enemies.GetOut:P=1
				if N is I or B is not Enemies.GetOut:
					for Q in range(P):M.append(B)
		if J=='easy':
			for A in C:
				C[A].append(random.choice(K));C[A].append(random.choice(G));C[A].append(random.choice(G))
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:C[A].append(random.choice(G))
		elif J==_C:
			D=0
			for A in C:
				F=0;E=0;H=3;R=I
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:H=4
				for Q in range(H):
					if F==0:
						if E<2:D=random.choice(O)
						elif E==2:D=random.choice(K)
						elif E==3:D=random.choice(G)
					elif F==1:
						if E<2:D=random.choice(K)
						elif E==2:D=random.choice(G)
					elif F==2:
						if E==0:D=random.choice(L)
						elif E==1:D=random.choice(G)
					elif E>3 or E>2 and F>1 or E==2 and F==2:print('This is a mistake in the crown enemy algorithm. Report this to the devs.');D=Enemies.BeaverGold
					if N is I and F<2 and R is I and random.randint(0,1000)>994:D=Enemies.GetOut;R=_A
					if EnemyMetaData[D].kasplat is _A:E=E+1
					F=EnemyMetaData[D].disruptive+F;C[A].append(D)
		elif J=='hard':
			W=I
			for A in C:
				H=3
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:H=4
				for Q in range(H):
					if W:S=random.choice([A for A in M if A!=Enemies.GetOut])
					else:S=random.choice(M)
					C[A].append(S)
		for A in C:
			if len(C[A])>0:random.shuffle(C[A])
	return C
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';y='ohko';x='kasplat_swaps';w='container_map';d='index';T='replace_with';S='vanilla_location';N='enemy_id';G='big';F=spoiler;D='offset';AD=[{w:7,x:[{S:0,T:1},{S:1,T:3},{S:2,T:0},{S:3,T:2}]}];z=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];A0=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];e=[Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageHard,Maps.BusyBarrelBarrageNormal,Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];f=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];g=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];O=[Maps.BeaverBotherEasy,Maps.BeaverBotherNormal,Maps.BeaverBotherHard];U=e.copy();U.extend(f);U.extend(g);U.extend(O);Z=Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageNormal,Maps.BusyBarrelBarrageHard;a={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};h={};i=[]
	for H in EnemyMetaData:
		if EnemyMetaData[H].crown_enabled is _A:i.append(H)
	if F.settings.enemy_rando or F.settings.kasplat_rando or F.settings.crown_enemy_rando!=_B:
		A1=F.settings.damage_amount==y;h=getBalancedCrownEnemyRando(F.settings.crown_enemy_rando,A1);j=[];k=[];l=[];m=[]
		for H in EnemyMetaData:
			if EnemyMetaData[H].minigame_enabled:
				l.append(H)
				if EnemyMetaData[H].beaver:m.append(H)
				if EnemyMetaData[H].killable:
					k.append(H)
					if EnemyMetaData[H].simple:j.append(H)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];P=[];ROM().seek(C);n=int.from_bytes(ROM().readBytes(2),G);I=2
			if n>0:
				for o in range(n):ROM().seek(C+I);A2=int.from_bytes(ROM().readBytes(2),G);I+=A2*6+2;ROM().seek(C+I);A3=int.from_bytes(ROM().readBytes(2),G);I+=A3*10+6
			ROM().seek(C+I);p=int.from_bytes(ROM().readBytes(2),G);b={}
			for Q in a:
				V=[]
				for o in range(p):V.append(random.choice(a[Q]))
				b[Q]=V
			I+=2
			for o in range(p):ROM().seek(C+I);A4=int.from_bytes(ROM().readBytes(1),G);ROM().seek(C+I+19);A5=int.from_bytes(ROM().readBytes(1),G);A6=I;ROM().seek(C+I+17);A7=int.from_bytes(ROM().readBytes(1),G);I+=22+A7*2;P.append({N:A4,D:A6,d:A5})
			if F.settings.kasplat_rando and not F.settings.kasplat_location_rando:
				for q in F.enemy_replacements:
					if q[w]==E:
						for r in q[x]:
							A8=r[S]+Enemies.KasplatDK;A9=r[T]+Enemies.KasplatDK
							for A in P:
								if A[N]==A8:ROM().seek(C+A[D]);ROM().writeMultipleBytes(A9,1)
			if F.settings.enemy_rando and E in z:
				for Q in b:
					V=b[Q];AA=a[Q];s=0
					for A in P:
						if A[N]in AA:
							if E!=Maps.FranticFactory or A[d]<35 or A[d]>44:
								B=V[s];s+=1
								if E!=Maps.ForestSpider or EnemyMetaData[B].aggro!=4:
									if B!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
										if B!=Enemies.Kosha or E!=Maps.CavesDiddyLowerCabin:
											if B!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
												ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
												if B in EnemyMetaData.keys():
													ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
													if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
													ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),G)
													if EnemyMetaData[B].size_cap>0:
														if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
													if F.settings.enemy_speed_rando:
														J=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
														if J>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(J,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(J,L),1)
			if F.settings.enemy_rando and E in U:
				M=[]
				if E in e:
					M=j.copy()
					if E in Z:
						if Enemies.KlaptrapGreen in M:M.remove(Enemies.KlaptrapGreen)
				elif E in f:M=k.copy()
				elif E in g:M=l.copy()
				elif E in O:M=m.copy()
				for A in P:
					if A[N]in M:
						B=random.choice(M)
						if E in O:B=random.choice([Enemies.BeaverBlue,Enemies.BeaverBlue,Enemies.BeaverGold])
						ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),G)
							if EnemyMetaData[B].size_cap>0:
								if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							ROM().seek(C+A[D]+15);AB=int.from_bytes(ROM().readBytes(1),G)
							if AB<EnemyMetaData[B].bbbarrage_min_scale and E in Z:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].bbbarrage_min_scale,1)
							if F.settings.enemy_speed_rando and E not in O and E not in Z:
								J=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
								if J>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(J,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(J,L),1)
							if B==Enemies.BeaverGold and E in O:
								for t in [12,13]:
									ROM().seek(C+A[D]+t);AC=int.from_bytes(ROM().readBytes(1),G);c=int(AC*1.1)
									if c>255:c=255
									ROM().seek(C+A[D]+t);ROM().writeMultipleBytes(c,1)
			if F.settings.crown_enemy_rando!=_B and E in A0:
				W=5
				if F.settings.crown_enemy_rando=='easy':W=5
				elif F.settings.crown_enemy_rando==_C:W=15
				elif F.settings.crown_enemy_rando=='hard':W=30
				X=random.randint(W,60)
				for A in P:
					if A[N]in i:
						B=h[E].pop();ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							if B==Enemies.GetOut:
								ROM().seek(C+A[D]+10);Y=20
								if X>20:
									u=1;v={'double':2,'quad':4,y:12}
									if F.settings.damage_amount in v:u=v[F.settings.damage_amount]
									Y=random.randint(int(X/(12/u))+1,X-1)
								if Y==0:Y=1
								ROM().writeMultipleBytes(Y,1)
							ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),G)
							if EnemyMetaData[B].size_cap>0:
								if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if F.settings.enemy_speed_rando:
								J=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
								if J>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(J,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(J,L),1)
					elif A[N]==Enemies.BattleCrownController:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(X,1)