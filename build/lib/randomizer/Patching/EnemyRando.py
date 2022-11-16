'Apply Boss Locations.'
_D='medium'
_C='off'
_B=True
_A=False
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
		if B in(Enemies.KasplatDK,Enemies.KasplatDiddy,Enemies.KasplatLanky,Enemies.KasplatTiny,Enemies.KasplatChunky,Enemies.Book,Enemies.EvilTomato):A.spawned=_B
		else:A.spawned=_A
		A.default=A.spawned
	def addEnemy(A):'Add enemy as spawned.';A.spawned=_B
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
	'Get array of weighted enemies.';L=spoiler;K=crown_setting;B={}
	if K!=_C:
		B={Maps.JapesCrown:[],Maps.AztecCrown:[],Maps.FactoryCrown:[],Maps.GalleonCrown:[],Maps.ForestCrown:[],Maps.CavesCrown:[],Maps.CastleCrown:[],Maps.HelmCrown:[],Maps.SnidesCrown:[],Maps.LobbyCrown:[]};M=[];G=[];I=[];F=[];N=[];O=_A
		for A in EnemyMetaData:
			if convertEnemyName(EnemyMetaData[A].name)in L.settings.enemies_selected and EnemyMetaData[A].crown_enabled is _B:O=_B;break
		for A in EnemyMetaData:
			if EnemyMetaData[A].crown_enabled and A is not Enemies.GetOut and convertEnemyName(EnemyMetaData[A].name)in L.settings.enemies_selected or O is _A:
				M.append(A)
				if EnemyMetaData[A].disruptive<=1:G.append(A)
				if EnemyMetaData[A].kasplat is _B:I.append(A)
				elif EnemyMetaData[A].disruptive==0:I.append(A);F.append(A)
		if len(G)==0:
			G.append(M.copy())
			for A in EnemyMetaData:
				if EnemyMetaData[A].disruptive>1:EnemyMetaData[A].disruptive=1
		if len(I)==0:I.append(G.copy())
		if len(F)==0:
			F.append(I)
			for A in EnemyMetaData:
				if EnemyMetaData[A].disruptive>0:EnemyMetaData[A].disruptive=0
		T=2
		for A in EnemyMetaData:
			if EnemyMetaData[A].crown_enabled and convertEnemyName(EnemyMetaData[A].name)in L.settings.enemies_selected or O is _A:
				U=EnemyMetaData[A].crown_weight;V=abs(U-T);Q=abs(10-V)
				if A==Enemies.GetOut:Q=1
				if damage_ohko_setting is _A or A is not Enemies.GetOut:
					for R in range(Q):N.append(A)
		if K=='easy':
			for C in B:
				B[C].append(random.choice(G));B[C].append(random.choice(F));B[C].append(random.choice(F))
				if C in(Maps.GalleonCrown,Maps.LobbyCrown,Maps.HelmCrown):B[C].append(random.choice(F))
		elif K==_D:
			E=0
			for C in B:
				H=0;D=0;J=3
				if C in(Maps.GalleonCrown,Maps.LobbyCrown,Maps.HelmCrown):J=4
				for R in range(J):
					if H==0:
						if D<2:E=random.choice(M)
						elif D==2:E=random.choice(G)
						elif D==3:E=random.choice(F)
					elif H==1:
						if D<2:E=random.choice(G)
						elif D==2:E=random.choice(F)
					elif H==2:
						if D==0:E=random.choice(I)
						elif D==1:E=random.choice(F)
					if D>3 or D>2 and H>1 or D==2 and H==2:print('This is a mistake in the crown enemy algorithm. Report this to the devs.');E=Enemies.BeaverGold
					if EnemyMetaData[E].kasplat is _B:D=D+1
					H=EnemyMetaData[E].disruptive+H;B[C].append(E)
		elif K=='hard':
			for C in B:
				J=3
				if C in(Maps.GalleonCrown,Maps.LobbyCrown,Maps.HelmCrown):J=4
				S=_A
				for R in range(J):
					if S:P=random.choice([A for A in N if A!=Enemies.GetOut])
					else:
						P=random.choice(N)
						if P==Enemies.GetOut:S=_B
					B[C].append(P)
		for C in B:
			if len(B[C])>0:random.shuffle(B[C])
	return B
def randomize_enemies(spoiler):
	'Write replaced enemies to ROM.';d='replace_with';c='vanilla_location';W='enemy_id';L='index';I='big';F=spoiler;D='offset';AG=[{'container_map':7,'kasplat_swaps':[{c:0,d:1},{c:1,d:3},{c:2,d:0},{c:3,d:2}]}];resetPkmnSnap();h=[Maps.JapesMountain,Maps.JungleJapes,Maps.JapesTinyHive,Maps.JapesLankyCave,Maps.AztecTinyTemple,Maps.HideoutHelm,Maps.AztecDonkey5DTemple,Maps.AztecDiddy5DTemple,Maps.AztecLanky5DTemple,Maps.AztecTiny5DTemple,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.FactoryPowerHut,Maps.GloomyGalleon,Maps.GalleonSickBay,Maps.JapesUnderGround,Maps.Isles,Maps.FactoryCrusher,Maps.AngryAztec,Maps.GalleonSealRace,Maps.JapesBaboonBlast,Maps.AztecBaboonBlast,Maps.Galleon2DShip,Maps.Galleon5DShipDiddyLankyChunky,Maps.Galleon5DShipDKTiny,Maps.GalleonTreasureChest,Maps.GalleonMermaidRoom,Maps.FungiForest,Maps.GalleonLighthouse,Maps.GalleonMechafish,Maps.ForestAnthill,Maps.GalleonBaboonBlast,Maps.ForestMinecarts,Maps.ForestMillAttic,Maps.ForestRafters,Maps.ForestMillAttic,Maps.ForestThornvineBarn,Maps.ForestMillFront,Maps.ForestMillBack,Maps.ForestLankyMushroomsRoom,Maps.CrystalCaves,Maps.CavesDonkeyIgloo,Maps.CavesDiddyIgloo,Maps.CavesLankyIgloo,Maps.CavesTinyIgloo,Maps.CavesDonkeyCabin,Maps.CavesDiddyLowerCabin,Maps.CavesDiddyUpperCabin,Maps.CavesLankyCabin,Maps.CavesTinyCabin,Maps.CavesChunkyCabin,Maps.CreepyCastle,Maps.CastleBallroom,Maps.CavesRotatingCabin,Maps.CavesFrozenCastle,Maps.CastleCrypt,Maps.CastleMausoleum,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTower,Maps.CastleMinecarts,Maps.FactoryBaboonBlast,Maps.CastleMuseum,Maps.CastleLibrary,Maps.CastleDungeon,Maps.CastleTree,Maps.CastleShed,Maps.CastleTrashCan,Maps.JungleJapesLobby,Maps.AngryAztecLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby,Maps.FungiForestLobby,Maps.CrystalCavesLobby,Maps.CreepyCastleLobby,Maps.HideoutHelmLobby,Maps.GalleonSubmarine,Maps.CavesBaboonBlast,Maps.CastleBaboonBlast,Maps.ForestBaboonBlast,Maps.IslesSnideRoom,Maps.ForestGiantMushroom,Maps.ForestLankyZingersRoom,Maps.CastleBoss];A1=[Maps.JapesCrown,Maps.AztecCrown,Maps.FactoryCrown,Maps.GalleonCrown,Maps.ForestCrown,Maps.CavesCrown,Maps.CastleCrown,Maps.HelmCrown,Maps.SnidesCrown,Maps.LobbyCrown];i=[Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageHard,Maps.BusyBarrelBarrageNormal,Maps.HelmBarrelChunkyHidden,Maps.HelmBarrelChunkyShooting];j=[Maps.MadMazeMaulEasy,Maps.MadMazeMaulNormal,Maps.MadMazeMaulHard,Maps.MadMazeMaulInsane];k=[Maps.HelmBarrelLankyMaze,Maps.StashSnatchEasy,Maps.StashSnatchNormal,Maps.StashSnatchHard,Maps.StashSnatchInsane];R=[Maps.BeaverBotherEasy,Maps.BeaverBotherNormal,Maps.BeaverBotherHard];X=i.copy();X.extend(j);X.extend(k);X.extend(R);e=Maps.BusyBarrelBarrageEasy,Maps.BusyBarrelBarrageNormal,Maps.BusyBarrelBarrageHard;P={EnemySubtype.GroundSimple:[Enemies.BeaverBlue,Enemies.KlaptrapGreen,Enemies.BeaverGold,Enemies.MushroomMan,Enemies.Ruler,Enemies.Kremling,Enemies.Krossbones,Enemies.MrDice0,Enemies.MrDice1,Enemies.SirDomino,Enemies.FireballGlasses,Enemies.SpiderSmall,Enemies.Ghost],EnemySubtype.Air:[Enemies.ZingerCharger,Enemies.ZingerLime,Enemies.ZingerRobo,Enemies.Bat],EnemySubtype.GroundBeefy:[Enemies.Klump,Enemies.RoboKremling,Enemies.Kosha,Enemies.Klobber,Enemies.Kaboom,Enemies.KlaptrapPurple,Enemies.KlaptrapRed,Enemies.Guard],EnemySubtype.Water:[Enemies.Shuri,Enemies.Gimpfish,Enemies.Pufftup]};A2={EnemySubtype.GroundSimple:[EnemySubtype.GroundBeefy,EnemySubtype.Water,EnemySubtype.Air],EnemySubtype.GroundBeefy:[EnemySubtype.GroundSimple,EnemySubtype.Water,EnemySubtype.Air],EnemySubtype.Water:[EnemySubtype.Air,EnemySubtype.GroundSimple,EnemySubtype.GroundBeefy],EnemySubtype.Air:[EnemySubtype.GroundSimple,EnemySubtype.GroundBeefy,EnemySubtype.Water]};l={};m=[]
	for J in P:
		Q=[]
		for G in P[J]:
			if convertEnemyName(EnemyMetaData[G].name)in F.settings.enemies_selected:Q.append(G)
		if len(Q)==0:
			for A3 in A2[J]:
				if len(Q)==0:
					for G in P[A3]:
						if convertEnemyName(EnemyMetaData[G].name)in F.settings.enemies_selected:Q.append(G)
		if len(Q)>0:l[J]=Q.copy()
		else:m.append(J)
	for J in m:del P[J]
	n={};o=[]
	for G in EnemyMetaData:
		if EnemyMetaData[G].crown_enabled is _B:o.append(G)
	if F.settings.enemy_rando or F.settings.crown_enemy_rando!=_C:
		A4=F.settings.damage_amount=='ohko';n=getBalancedCrownEnemyRando(F,F.settings.crown_enemy_rando,A4);p=[];q=[];r=[];s=[]
		for G in EnemyMetaData:
			if EnemyMetaData[G].minigame_enabled:
				r.append(G)
				if EnemyMetaData[G].beaver:s.append(G)
				if EnemyMetaData[G].killable:
					q.append(G)
					if EnemyMetaData[G].simple:p.append(G)
		for E in range(216):
			C=js.pointer_addresses[16]['entries'][E]['pointing_to'];S=[];ROM().seek(C);t=int.from_bytes(ROM().readBytes(2),I);H=2
			if t>0:
				for u in range(t):ROM().seek(C+H);A5=int.from_bytes(ROM().readBytes(2),I);H+=A5*6+2;ROM().seek(C+H);A6=int.from_bytes(ROM().readBytes(2),I);H+=A6*10+6
			ROM().seek(C+H);v=int.from_bytes(ROM().readBytes(2),I);f={}
			for J in P:
				Y=[]
				for u in range(v):Y.append(random.choice(l[J]))
				f[J]=Y
			H+=2
			for u in range(v):ROM().seek(C+H);A7=int.from_bytes(ROM().readBytes(1),I);ROM().seek(C+H+19);Z=int.from_bytes(ROM().readBytes(1),I);A8=H;ROM().seek(C+H+17);A9=int.from_bytes(ROM().readBytes(1),I);H+=22+A9*2;S.append({W:A7,D:A8,L:Z})
			if F.settings.enemy_rando and E in h:
				for J in f:
					Y=f[J];AA=P[J];w=0
					for A in S:
						if A[W]in AA and E!=Maps.FranticFactory or A[L]<35 or A[L]>44 and E!=Maps.AztecTinyTemple or A[L]<20 or A[L]>23:
							B=Y[w];w+=1
							if E!=Maps.ForestSpider or EnemyMetaData[B].aggro!=4 and B!=Enemies.Book or E not in(Maps.CavesDonkeyCabin,Maps.JapesLankyCave,Maps.AngryAztecLobby)and B!=Enemies.Kosha or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyCabin)and B!=Enemies.Guard or E not in(Maps.CavesDiddyLowerCabin,Maps.CavesTinyIgloo,Maps.CavesTinyCabin):
								ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
								if B in EnemyMetaData:
									ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
									if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
									ROM().seek(C+A[D]+15);T=int.from_bytes(ROM().readBytes(1),I)
									if EnemyMetaData[B].size_cap>0 and T>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
									if F.settings.enemy_speed_rando:
										K=EnemyMetaData[B].min_speed;M=EnemyMetaData[B].max_speed
										if K>0 and M>0:ROM().seek(C+A[D]+13);N=random.randint(K,M);ROM().writeMultipleBytes(N,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(K,N),1)
			if F.settings.enemy_rando and E in X:
				O=[]
				if E in i:
					O=p.copy()
					if E in e and Enemies.KlaptrapGreen in O:O.remove(Enemies.KlaptrapGreen)
				elif E in j:O=q.copy()
				elif E in k:O=r.copy()
				elif E in R:O=s.copy()
				for A in S:
					if A[W]in O:
						B=random.choice(O)
						if E in R:B=random.choice([Enemies.BeaverBlue,Enemies.BeaverBlue,Enemies.BeaverGold])
						ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData:
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							ROM().seek(C+A[D]+15);T=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0 and T>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							ROM().seek(C+A[D]+15);AB=int.from_bytes(ROM().readBytes(1),I)
							if AB<EnemyMetaData[B].bbbarrage_min_scale and E in e:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].bbbarrage_min_scale,1)
							if F.settings.enemy_speed_rando and E not in R and E not in e:
								K=EnemyMetaData[B].min_speed;M=EnemyMetaData[B].max_speed
								if K>0 and M>0:ROM().seek(C+A[D]+13);N=random.randint(K,M);ROM().writeMultipleBytes(N,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(K,N),1)
							if B==Enemies.BeaverGold and E in R:
								for x in [12,13]:
									ROM().seek(C+A[D]+x);AC=int.from_bytes(ROM().readBytes(1),I);g=int(AC*1.1)
									if g>255:g=255
									ROM().seek(C+A[D]+x);ROM().writeMultipleBytes(g,1)
			if F.settings.crown_enemy_rando!=_C and E in A1:
				a=5
				if F.settings.crown_enemy_rando=='easy':a=5
				elif F.settings.crown_enemy_rando==_D:a=15
				elif F.settings.crown_enemy_rando=='hard':a=30
				b=random.randint(a,60)
				for A in S:
					if A[W]in o:
						B=n[E].pop();ROM().seek(C+A[D]);ROM().writeMultipleBytes(B,1)
						if B in EnemyMetaData:
							ROM().seek(C+A[D]+16);ROM().writeMultipleBytes(EnemyMetaData[B].aggro,1)
							if B==Enemies.RoboKremling:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(200,1)
							if EnemyMetaData[B].air:ROM().seek(C+A[D]+6);ROM().writeMultipleBytes(300,2)
							if B==Enemies.GetOut:
								ROM().seek(C+A[D]+10);U=20
								if b>20:
									y=1;z={'double':2,'quad':4,'ohko':12}
									if F.settings.damage_amount in z:y=z[F.settings.damage_amount]
									U=random.randint(int(b/(12/y))+1,b-1)
								if U==0:U=1
								ROM().writeMultipleBytes(U,1);ROM().writeMultipleBytes(U,1)
							ROM().seek(C+A[D]+15);T=int.from_bytes(ROM().readBytes(1),I)
							if EnemyMetaData[B].size_cap>0 and T>EnemyMetaData[B].size_cap:ROM().seek(C+A[D]+15);ROM().writeMultipleBytes(EnemyMetaData[B].size_cap,1)
							if F.settings.enemy_speed_rando:
								K=EnemyMetaData[B].min_speed;M=EnemyMetaData[B].max_speed
								if K>0 and M>0:ROM().seek(C+A[D]+13);N=random.randint(K,M);ROM().writeMultipleBytes(N,1);ROM().seek(C+A[D]+12);ROM().writeMultipleBytes(random.randint(K,N),1)
					elif A[W]==Enemies.BattleCrownController:ROM().seek(C+A[D]+11);ROM().writeMultipleBytes(b,1)
			AD=[Maps.ForestSpider,Maps.CavesDiddyLowerCabin,Maps.CavesTinyCabin,Maps.CastleBoss]
			if E in h and E not in AD:
				for A in S:
					V=_B
					if E==Maps.AztecTinyTemple and A[L]<17:V=_A
					if E==Maps.AztecTinyTemple and A[L]>19 and A[L]<24:V=_A
					if E==Maps.FranticFactory and A[L]>34 and A[L]<45:V=_A
					if E==Maps.CrystalCaves and A[L]<10:V=_A
					if V:ROM().seek(C+A[D]);setPkmnSnapEnemy(int.from_bytes(ROM().readBytes(1),I))
			A0=[0,0,0,0,0]
			for (Z,G) in enumerate(pkmn_snap_enemies):
				if G.spawned:H=Z>>3;AE=Z&7;A0[H]|=1<<AE
			ROM().seek(F.settings.rom_data+279)
			for AF in A0:ROM().writeMultipleBytes(AF,1)