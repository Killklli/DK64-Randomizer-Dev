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
	'Write replaced enemies to ROM.';x='ohko';w='kasplat_swaps';v='container_map';c='index';T='replace_with';S='vanilla_location';N='enemy_id';G='big';F=spoiler;D='offset';AC=[{v:7,w:[{S:0,T:1},{S:1,T:3},{S:2,T:0},{S:3,T:2}]}];y=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];z=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];d=[Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageHard,Maps.BusyBarrelBarrageNormal,Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];e=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];f=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];O=[Maps.BeaverBotherEasy,Maps.BeaverBotherNormal,Maps.BeaverBotherHard];U=d.copy();U.extend(e);U.extend(f);U.extend(O);Z={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};g={};h=[]
	for H in EnemyMetaData:
		if EnemyMetaData[H].crown_enabled is _A:h.append(H)
	if F.settings.enemy_rando or F.settings.kasplat_rando or F.settings.crown_enemy_rando!=_B:
		A0=F.settings.damage_amount==x;g=getBalancedCrownEnemyRando(F.settings.crown_enemy_rando,A0);i=[];j=[];k=[];l=[]
		for H in EnemyMetaData:
			if EnemyMetaData[H].minigame_enabled:
				k.append(H)
				if EnemyMetaData[H].beaver:l.append(H)
				if EnemyMetaData[H].killable:
					j.append(H)
					if EnemyMetaData[H].simple:i.append(H)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];P=[];ROM().seek(C);m=int.from_bytes(ROM().readBytes(2),G);I=2
			if m>0:
				for n in range(m):ROM().seek(C+I);A1=int.from_bytes(ROM().readBytes(2),G);I+=A1*6+2;ROM().seek(C+I);A2=int.from_bytes(ROM().readBytes(2),G);I+=A2*10+6
			ROM().seek(C+I);o=int.from_bytes(ROM().readBytes(2),G);a={}
			for Q in Z:
				V=[]
				for n in range(o):V.append(random.choice(Z[Q]))
				a[Q]=V
			I+=2
			for n in range(o):ROM().seek(C+I);A3=int.from_bytes(ROM().readBytes(1),G);ROM().seek(C+I+19);A4=int.from_bytes(ROM().readBytes(1),G);A5=I;ROM().seek(C+I+17);A6=int.from_bytes(ROM().readBytes(1),G);I+=22+A6*2;P.append({N:A3,D:A5,c:A4})
			if F.settings.kasplat_rando and not F.settings.kasplat_location_rando:
				for p in F.enemy_replacements:
					if p[v]==E:
						for q in p[w]:
							A7=q[S]+Enemies.KasplatDK;A8=q[T]+Enemies.KasplatDK
							for A in P:
								if A[N]==A7:ROM().seek(C+A[D]);ROM().writeMultipleBytes(A8,1)
			if F.settings.enemy_rando and E in y:
				for Q in a:
					V=a[Q];A9=Z[Q];r=0
					for A in P:
						if A[N]in A9:
							if E!=Maps.FranticFactory or A[c]<35 or A[c]>44:
								B=V[r];r+=1
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
				if E in d:
					M=i.copy()
					if E in(Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageNormal,Maps.BusyBarrelBarrageHard):
						if Enemies.KlaptrapGreen in M:M.remove(Enemies.KlaptrapGreen)
				elif E in e:M=j.copy()
				elif E in f:M=k.copy()
				elif E in O:M=l.copy()
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
							ROM().seek(C+A[D]+15);AA=int.from_bytes(ROM().readBytes(1),G)
							if AA<EnemyMetaData[B].bbbarrage_min_scale:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].bbbarrage_min_scale,1)
							if F.settings.enemy_speed_rando and E not in O and E not in(Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageNormal,Maps.BusyBarrelBarrageHard):
								J=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
								if J>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(J,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(J,L),1)
							if B==Enemies.BeaverGold and E in O:
								for s in [12,13]:
									ROM().seek(C+A[D]+s);AB=int.from_bytes(ROM().readBytes(1),G);b=int(AB*1.1)
									if b>255:b=255
									ROM().seek(C+A[D]+s);ROM().writeMultipleBytes(b,1)
			if F.settings.crown_enemy_rando!=_B and E in z:
				W=5
				if F.settings.crown_enemy_rando=='easy':W=5
				elif F.settings.crown_enemy_rando==_C:W=15
				elif F.settings.crown_enemy_rando=='hard':W=30
				X=random.randint(W,60)
				for A in P:
					if A[N]in h:
						B=g[E].pop();ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							if B==Enemies.GetOut:
								ROM().seek(C+A[D]+10);Y=20
								if X>20:
									t=1;u={'double':2,'quad':4,x:12}
									if F.settings.damage_amount in u:t=u[F.settings.damage_amount]
									Y=random.randint(int(X/(12/t))+1,X-1)
								if Y==0:Y=1
								ROM().writeMultipleBytes(Y,1)
							ROM().seek(C+A[D]+15);R=int.from_bytes(ROM().readBytes(1),G)
							if EnemyMetaData[B].size_cap>0:
								if R>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if F.settings.enemy_speed_rando:
								J=EnemyMetaData[B].min_speed;K=EnemyMetaData[B].max_speed
								if J>0 and K>0:ROM().seek(C+A[D]+13);L=random.randint(J,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(J,L),1)
					elif A[N]==Enemies.BattleCrownController:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(X,1)