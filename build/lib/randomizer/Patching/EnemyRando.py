'Apply Boss Locations.'
_C='medium'
_B='off'
_A=True
from email.policy import default
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def getBalancedCrownEnemyRando(crown_setting,damage_ohko_setting):
	'Get array of weighted enemies.';M=damage_ohko_setting;K=False;I=crown_setting;C={}
	if I!=_B:
		C={Maps.JapesCrown:[],Maps.AztecCrown:[],Maps.FactoryCrown:[],Maps.GalleonCrown:[],Maps.ForestCrown:[],Maps.CavesCrown:[],Maps.CastleCrown:[],Maps.HelmCrown:[],Maps.SnidesCrown:[],Maps.LobbyCrown:[]};N=[];J=[];L=[];G=[];O=[]
		for B in EnemyMetaData:
			if EnemyMetaData[B].crown_enabled and B is not Enemies.GetOut:
				N.append(B)
				if EnemyMetaData[B].disruptive<=1:J.append(B)
				if EnemyMetaData[B].kasplat is _A:L.append(B)
				elif EnemyMetaData[B].disruptive==0:L.append(B);G.append(B)
		R=2
		for B in EnemyMetaData.keys():
			if EnemyMetaData[B].crown_enabled:
				S=EnemyMetaData[B].crown_weight;T=abs(S-R);U=abs(10-T)
				if M is K or B is not Enemies.GetOut:
					for P in range(U):O.append(B)
		if I=='easy':
			for A in C:
				C[A].append(random.choice(J));C[A].append(random.choice(G));C[A].append(random.choice(G))
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:C[A].append(random.choice(G))
		elif I==_C:
			D=0
			for A in C:
				F=0;E=0;H=3;Q=K
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:H=4
				for P in range(H):
					if F==0:
						if E<2:D=random.choice(N)
						elif E==2:D=random.choice(J)
						elif E==3:D=random.choice(G)
					elif F==1:
						if E<2:D=random.choice(J)
						elif E==2:D=random.choice(G)
					elif F==2:
						if E==0:D=random.choice(L)
						elif E==1:D=random.choice(G)
					elif E>3 or E>2 and F>1 or E==2 and F==2:print('This is a mistake in the crown enemy algorithm. Report this to the devs.');D=Enemies.BeaverGold
					if M is K and F<2 and Q is K and random.randint(0,1000)>994:D=Enemies.GetOut;Q=_A
					if EnemyMetaData[D].kasplat is _A:E=E+1
					F=EnemyMetaData[D].disruptive+F;C[A].append(D)
		elif I=='hard':
			for A in C:
				H=3
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:H=4
				for P in range(H):C[A].append(random.choice(O))
		for A in C:
			if len(C[A])>0:random.shuffle(C[A])
	return C
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';s='kasplat_swaps';r='container_map';a='index';T='replace_with';S='vanilla_location';N='enemy_id';J='big';F=spoiler;D='offset';A7=[{r:7,s:[{S:0,T:1},{S:1,T:3},{S:2,T:0},{S:3,T:2}]}];t=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];u=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];b=[Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];c=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];d=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];O=[];U=b.copy();U.extend(c);U.extend(d);U.extend(O);X={'ground_simple':[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],'air':[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],'ground_beefyboys':[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],'water':[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};e={};f=[]
	for G in EnemyMetaData:
		if EnemyMetaData[G].crown_enabled is _A:f.append(G)
	if F.settings.enemy_rando or F.settings.kasplat_rando or F.settings.crown_enemy_rando!=_B:
		v=F.settings.damage_amount=='ohko';e=getBalancedCrownEnemyRando(F.settings.crown_enemy_rando,v);g=[];h=[];i=[];j=[]
		for G in EnemyMetaData:
			if EnemyMetaData[G].minigame_enabled:
				i.append(G)
				if EnemyMetaData[G].beaver:j.append(G)
				if EnemyMetaData[G].killable:
					h.append(G)
					if EnemyMetaData[G].simple:g.append(G)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];P=[];ROM().seek(C);k=int.from_bytes(ROM().readBytes(2),J);H=2
			if k>0:
				for l in range(k):ROM().seek(C+H);w=int.from_bytes(ROM().readBytes(2),J);H+=w*6+2;ROM().seek(C+H);x=int.from_bytes(ROM().readBytes(2),J);H+=x*10+6
			ROM().seek(C+H);m=int.from_bytes(ROM().readBytes(2),J);Y={}
			for Q in X:
				V=[]
				for l in range(m):V.append(random.choice(X[Q]))
				Y[Q]=V
			H+=2
			for l in range(m):ROM().seek(C+H);y=int.from_bytes(ROM().readBytes(1),J);ROM().seek(C+H+19);z=int.from_bytes(ROM().readBytes(1),J);A0=H;ROM().seek(C+H+17);A1=int.from_bytes(ROM().readBytes(1),J);H+=22+A1*2;P.append({N:y,D:A0,a:z})
			if F.settings.kasplat_rando and not F.settings.kasplat_location_rando:
				for n in F.enemy_replacements:
					if n[r]==E:
						for o in n[s]:
							A2=o[S]+Enemies.KasplatDK;A3=o[T]+Enemies.KasplatDK
							for B in P:
								if B[N]==A2:ROM().seek(C+B[D]);ROM().writeMultipleBytes(A3,1)
			if F.settings.enemy_rando and E in t:
				for Q in Y:
					V=Y[Q];A4=X[Q];p=0
					for B in P:
						if B[N]in A4:
							if E!=Maps.FranticFactory or B[a]<35 or B[a]>44:
								A=V[p];p+=1
								if E!=Maps.ForestSpider or EnemyMetaData[A].aggro!=4:
									if A!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
										if A!=Enemies.Kosha or E!=Maps.CavesDiddyLowerCabin:
											if A!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
												ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
												if A in EnemyMetaData.keys():
													ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
													if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
													ROM().seek(C+B[D]+15);R=int.from_bytes(ROM().readBytes(1),J)
													if EnemyMetaData[A].size_cap>0:
														if R>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
													if F.settings.enemy_speed_rando:
														I=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
														if I>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(I,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(I,L),1)
			if F.settings.enemy_rando and E in U:
				M=[]
				if E in b:M=g.copy()
				elif E in c:M=h.copy()
				elif E in d:M=i.copy()
				elif E in O:M=j.copy()
				for B in P:
					if B[N]in M:
						A=random.choice(M)
						if E in O:
							A5=random.choice(M)
							if A!=Enemies.BeaverGold or A5!=Enemies.BeaverGold:A=Enemies.BeaverBlue
						ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);R=int.from_bytes(ROM().readBytes(1),J)
							if EnemyMetaData[A].size_cap>0:
								if R>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if F.settings.enemy_speed_rando and E not in O:
								I=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
								if I>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(I,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(I,L),1)
							if A==Enemies.BeaverGold and E in O:
								for q in [12,13]:
									ROM().seek(C+B[D]+q);A6=int.from_bytes(ROM().readBytes(1),J);Z=int(A6*1.1)
									if Z>255:Z=255
									ROM().seek(C+B[D]+q);ROM().writeMultipleBytes(Z,1)
			if F.settings.crown_enemy_rando!=_B and E in u:
				for B in P:
					if B[N]in f:
						A=e[E].pop();ROM().seek(C+B[D]);ROM().writeMultipleBytes(A,1)
						if A in EnemyMetaData.keys():
							ROM().seek(C+B[D]+16);ROM().writeMultipleBytes(EnemyMetaData[A].aggro,1)
							if A==Enemies.RoboKremling:ROM().seek(C+B[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[A].air:ROM().seek(C+B[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+B[D]+15);R=int.from_bytes(ROM().readBytes(1),J)
							if EnemyMetaData[A].size_cap>0:
								if R>EnemyMetaData[A].size_cap:ROM().seek(C+B[D]+15);ROM().writeMultipleBytes(EnemyMetaData[A].size_cap,1)
							if F.settings.enemy_speed_rando:
								I=EnemyMetaData[A].min_speed;K=EnemyMetaData[A].max_speed
								if I>0 and K>0:ROM().seek(C+B[D]+13);L=random.randint(I,K);ROM().writeMultipleBytes(L,1);ROM().seek(C+B[D]+12);ROM().writeMultipleBytes(random.randint(I,L),1)
					elif B[N]==Enemies.BattleCrownController:
						ROM().seek(C+B[D]+11);W=5
						if F.settings.crown_enemy_rando=='easy':W=5
						elif F.settings.crown_enemy_rando==_C:W=15
						elif F.settings.crown_enemy_rando=='hard':W=30
						ROM().writeMultipleBytes(random.randint(W,60),1)