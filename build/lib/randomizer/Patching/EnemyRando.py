'Apply Boss Locations.'
_D='medium'
_C='off'
_B=False
_A=True
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData,convertEnemyName
from randomizer.Enums.EnemySubtypes import EnemySubtype
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
class PkmnSnapEnemy:
	'Class which determines if an enemy is available for the pkmn snap goal.'
	def __init__(A,enemy):
		'Initialize with given parameters.';B=enemy;A.enemy=B
		if B in(Enemies.KasplatDK,Enemies.KasplatDiddy,Enemies.KasplatLanky,Enemies.KasplatTiny,Enemies.KasplatChunky,Enemies.Book,Enemies.EvilTomato):A.spawned=_A
		else:A.spawned=_B
		A.default=A.spawned
	def addEnemy(A):'Add enemy as spawned.';A.spawned=_A
	def reset(A):'Reset enemy to default state.';A.spawned=A.default
pkmn_snap_enemies=[PkmnSnapEnemy(Enemies.Kaboom),PkmnSnapEnemy(Enemies.BeaverBlue),PkmnSnapEnemy(Enemies.Book),PkmnSnapEnemy(Enemies.Klobber),PkmnSnapEnemy(Enemies.ZingerCharger),PkmnSnapEnemy(Enemies.Klump),PkmnSnapEnemy(Enemies.KlaptrapGreen),PkmnSnapEnemy(Enemies.ZingerLime),PkmnSnapEnemy(Enemies.KlaptrapPurple),PkmnSnapEnemy(Enemies.KlaptrapRed),PkmnSnapEnemy(Enemies.BeaverGold),PkmnSnapEnemy(Enemies.MushroomMan),PkmnSnapEnemy(Enemies.Ruler),PkmnSnapEnemy(Enemies.RoboKremling),PkmnSnapEnemy(Enemies.Kremling),PkmnSnapEnemy(Enemies.KasplatDK),PkmnSnapEnemy(Enemies.KasplatDiddy),PkmnSnapEnemy(Enemies.KasplatLanky),PkmnSnapEnemy(Enemies.KasplatTiny),PkmnSnapEnemy(Enemies.KasplatChunky),PkmnSnapEnemy(Enemies.Guard),PkmnSnapEnemy(Enemies.ZingerRobo),PkmnSnapEnemy(Enemies.Krossbones),PkmnSnapEnemy(Enemies.Shuri),PkmnSnapEnemy(Enemies.Gimpfish),PkmnSnapEnemy(Enemies.MrDice0),PkmnSnapEnemy(Enemies.SirDomino),PkmnSnapEnemy(Enemies.MrDice1),PkmnSnapEnemy(Enemies.FireballGlasses),PkmnSnapEnemy(Enemies.SpiderSmall),PkmnSnapEnemy(Enemies.Bat),PkmnSnapEnemy(Enemies.EvilTomato),PkmnSnapEnemy(Enemies.Ghost),PkmnSnapEnemy(Enemies.Pufftup),PkmnSnapEnemy(Enemies.Kosha)]
def resetPkmnSnap():
	'Reset Pokemon Snap Listing.'
	for A in pkmn_snap_enemies:A.reset()
def setPkmnSnapEnemy(focused_enemy):
	'Set enemy to being spawned.'
	for A in pkmn_snap_enemies:
		if A.enemy==focused_enemy:A.addEnemy()
def getBalancedCrownEnemyRando(spoiler,crown_setting,damage_ohko_setting):
	'Get array of weighted enemies.';N=damage_ohko_setting;M=spoiler;I=crown_setting;C={}
	if I!=_C:
		C={Maps.JapesCrown:[],Maps.AztecCrown:[],Maps.FactoryCrown:[],Maps.GalleonCrown:[],Maps.ForestCrown:[],Maps.CavesCrown:[],Maps.CastleCrown:[],Maps.HelmCrown:[],Maps.SnidesCrown:[],Maps.LobbyCrown:[]};O=[];J=[];K=[];G=[];L=[]
		for B in EnemyMetaData:
			if EnemyMetaData[B].crown_enabled and B is not Enemies.GetOut:
				if convertEnemyName(EnemyMetaData[B].name)in M.settings.enemies_selected:
					O.append(B)
					if EnemyMetaData[B].disruptive<=1:J.append(B)
					if EnemyMetaData[B].kasplat is _A:K.append(B)
					elif EnemyMetaData[B].disruptive==0:K.append(B);G.append(B)
		T=2
		for B in EnemyMetaData.keys():
			if EnemyMetaData[B].crown_enabled:
				if convertEnemyName(EnemyMetaData[B].name)in M.settings.enemies_selected:
					U=EnemyMetaData[B].crown_weight;V=abs(U-T);P=abs(10-V)
					if B==Enemies.GetOut:P=1
					if N is _B or B is not Enemies.GetOut:
						for Q in range(P):L.append(B)
		if I=='easy':
			for A in C:
				C[A].append(random.choice(J));C[A].append(random.choice(G));C[A].append(random.choice(G))
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:C[A].append(random.choice(G))
		elif I==_D:
			D=0
			for A in C:
				F=0;E=0;H=3;R=_B
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:H=4
				for Q in range(H):
					if F==0:
						if E<2:D=random.choice(O)
						elif E==2:D=random.choice(J)
						elif E==3:D=random.choice(G)
					elif F==1:
						if E<2:D=random.choice(J)
						elif E==2:D=random.choice(G)
					elif F==2:
						if E==0:D=random.choice(K)
						elif E==1:D=random.choice(G)
					elif E>3 or E>2 and F>1 or E==2 and F==2:print('This is a mistake in the crown enemy algorithm. Report this to the devs.');D=Enemies.BeaverGold
					if N is _B and F<2 and R is _B and random.randint(0,1000)>994:D=Enemies.GetOut;R=_A
					if EnemyMetaData[D].kasplat is _A:E=E+1
					F=EnemyMetaData[D].disruptive+F;C[A].append(D)
		elif I=='hard':
			W=_B
			for A in C:
				H=3
				if A==Maps.GalleonCrown or A==Maps.LobbyCrown or A==Maps.HelmCrown:H=4
				for Q in range(H):
					if W:S=random.choice([A for A in L if A!=Enemies.GetOut])
					else:S=random.choice(L)
					C[A].append(S)
		for A in C:
			if len(C[A])>0:random.shuffle(C[A])
	return C
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';c='index';b='replace_with';a='vanilla_location';U='enemy_id';I='big';F=spoiler;D='offset';AF=[{'container_map':7,'kasplat_swaps':[{a:0,b:1},{a:1,b:3},{a:2,b:0},{a:3,b:2}]}];resetPkmnSnap();g=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];A1=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];h=[Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageHard,Maps.BusyBarrelBarrageNormal,Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];i=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];j=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];Q=[Maps.BeaverBotherEasy,Maps.BeaverBotherNormal,Maps.BeaverBotherHard];V=h.copy();V.extend(i);V.extend(j);V.extend(Q);d=Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageNormal,Maps.BusyBarrelBarrageHard;O={EnemySubtype.GroundSimple:[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],EnemySubtype.Air:[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],EnemySubtype.GroundBeefy:[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],EnemySubtype.Water:[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};A2={EnemySubtype.GroundSimple:[EnemySubtype.GroundBeefy,EnemySubtype.Water,EnemySubtype.Air],EnemySubtype.GroundBeefy:[EnemySubtype.GroundSimple,EnemySubtype.Water,EnemySubtype.Air],EnemySubtype.Water:[EnemySubtype.Air,EnemySubtype.GroundSimple,EnemySubtype.GroundBeefy],EnemySubtype.Air:[EnemySubtype.GroundSimple,EnemySubtype.GroundBeefy,EnemySubtype.Water]};k={};l=[]
	for J in O:
		P=[]
		for G in O[J]:
			if convertEnemyName(EnemyMetaData[G].name)in F.settings.enemies_selected:P.append(G)
		if len(P)==0:
			for A3 in A2[J]:
				if len(P)==0:
					for G in O[A3]:
						if convertEnemyName(EnemyMetaData[G].name)in F.settings.enemies_selected:P.append(G)
		if len(P)>0:k[J]=P.copy()
		else:l.append(J)
	for J in l:del O[J]
	m={};n=[]
	for G in EnemyMetaData:
		if EnemyMetaData[G].crown_enabled is _A:n.append(G)
	if F.settings.enemy_rando or F.settings.crown_enemy_rando!=_C:
		A4=F.settings.damage_amount=='ohko';m=getBalancedCrownEnemyRando(F,F.settings.crown_enemy_rando,A4);o=[];p=[];q=[];r=[]
		for G in EnemyMetaData:
			if EnemyMetaData[G].minigame_enabled:
				q.append(G)
				if EnemyMetaData[G].beaver:r.append(G)
				if EnemyMetaData[G].killable:
					p.append(G)
					if EnemyMetaData[G].simple:o.append(G)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];R=[];ROM().seek(C);s=int.from_bytes(ROM().readBytes(2),I);H=2
			if s>0:
				for t in range(s):ROM().seek(C+H);A5=int.from_bytes(ROM().readBytes(2),I);H+=A5*6+2;ROM().seek(C+H);A6=int.from_bytes(ROM().readBytes(2),I);H+=A6*10+6
			ROM().seek(C+H);u=int.from_bytes(ROM().readBytes(2),I);e={}
			for J in O:
				W=[]
				for t in range(u):W.append(random.choice(k[J]))
				e[J]=W
			H+=2
			for t in range(u):ROM().seek(C+H);A7=int.from_bytes(ROM().readBytes(1),I);ROM().seek(C+H+19);X=int.from_bytes(ROM().readBytes(1),I);A8=H;ROM().seek(C+H+17);A9=int.from_bytes(ROM().readBytes(1),I);H+=22+A9*2;R.append({U:A7,D:A8,c:X})
			if F.settings.enemy_rando and E in g:
				for J in e:
					W=e[J];AA=O[J];v=0
					for A in R:
						if A[U]in AA:
							if E!=Maps.FranticFactory or A[c]<35 or A[c]>44:
								B=W[v];v+=1
								if E!=Maps.ForestSpider or EnemyMetaData[B].aggro!=4:
									if B!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby):
										if B!=Enemies.Kosha or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyCabin):
											if B!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
												ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
												if B in EnemyMetaData.keys():
													ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
													if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
													ROM().seek(C+A[D]+15);S=int.from_bytes(ROM().readBytes(1),I)
													if EnemyMetaData[B].size_cap>0:
														if S>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
													if F.settings.enemy_speed_rando:
														K=EnemyMetaData[B].min_speed;L=EnemyMetaData[B].max_speed
														if K>0 and L>0:ROM().seek(C+A[D]+13);M=random.randint(K,L);ROM().writeMultipleBytes(M,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(K,M),1)
			if F.settings.enemy_rando and E in V:
				N=[]
				if E in h:
					N=o.copy()
					if E in d:
						if Enemies.KlaptrapGreen in N:N.remove(Enemies.KlaptrapGreen)
				elif E in i:N=p.copy()
				elif E in j:N=q.copy()
				elif E in Q:N=r.copy()
				for A in R:
					if A[U]in N:
						B=random.choice(N)
						if E in Q:B=random.choice([Enemies.BeaverBlue,Enemies.BeaverBlue,Enemies.BeaverGold])
						ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);S=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0:
								if S>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							ROM().seek(C+A[D]+15);AB=int.from_bytes(ROM().readBytes(1),I)
							if AB<EnemyMetaData[B].bbbarrage_min_scale and E in d:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].bbbarrage_min_scale,1)
							if F.settings.enemy_speed_rando and E not in Q and E not in d:
								K=EnemyMetaData[B].min_speed;L=EnemyMetaData[B].max_speed
								if K>0 and L>0:ROM().seek(C+A[D]+13);M=random.randint(K,L);ROM().writeMultipleBytes(M,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(K,M),1)
							if B==Enemies.BeaverGold and E in Q:
								for w in [12,13]:
									ROM().seek(C+A[D]+w);AC=int.from_bytes(ROM().readBytes(1),I);f=int(AC*1.1)
									if f>255:f=255
									ROM().seek(C+A[D]+w);ROM().writeMultipleBytes(f,1)
			if F.settings.crown_enemy_rando!=_C and E in A1:
				Y=5
				if F.settings.crown_enemy_rando=='easy':Y=5
				elif F.settings.crown_enemy_rando==_D:Y=15
				elif F.settings.crown_enemy_rando=='hard':Y=30
				Z=random.randint(Y,60)
				for A in R:
					if A[U]in n:
						B=m[E].pop();ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData.keys():
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							if B==Enemies.GetOut:
								ROM().seek(C+A[D]+10);T=20
								if Z>20:
									x=1;y={'double':2,'quad':4,'ohko':12}
									if F.settings.damage_amount in y:x=y[F.settings.damage_amount]
									T=random.randint(int(Z/(12/x))+1,Z-1)
								if T==0:T=1
								ROM().writeMultipleBytes(T,1);ROM().writeMultipleBytes(T,1)
							ROM().seek(C+A[D]+15);S=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0:
								if S>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if F.settings.enemy_speed_rando:
								K=EnemyMetaData[B].min_speed;L=EnemyMetaData[B].max_speed
								if K>0 and L>0:ROM().seek(C+A[D]+13);M=random.randint(K,L);ROM().writeMultipleBytes(M,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(K,M),1)
					elif A[U]==Enemies.BattleCrownController:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(Z,1)
			if E in g and E!=Maps.CastleBoss:
				for A in R:
					z=_A
					if E==Maps.CrystalCaves and A[c]<10:z=_B
					if z:ROM().seek(C+A[D]);setPkmnSnapEnemy(int.from_bytes(ROM().readBytes(1),I))
			A0=[0,0,0,0,0]
			for (X,G) in enumerate(pkmn_snap_enemies):
				if G.spawned:H=X>>3;AD=X&7;A0[H]|=1<<AD
			ROM().seek(F.settings.rom_data+279)
			for AE in A0:ROM().writeMultipleBytes(AE,1)