'Apply Kasplat Locations.'
import js
from randomizer.Lists.EnemyTypes import Enemies
from randomizer.Lists.KasplatLocations import KasplatLocationList
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_kasplat_locations(spoiler):
	'Write replaced enemies to ROM.';K=spoiler;G='big';Q=[Enemies.KasplatDK,Enemies.KasplatDiddy,Enemies.KasplatLanky,Enemies.KasplatTiny,Enemies.KasplatChunky];o=[Maps.JungleJapes,Maps.JapesUnderGround,Maps.AngryAztec,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.GloomyGalleon,Maps.FungiForest,Maps.ForestGiantMushroom,Maps.CrystalCaves,Maps.CreepyCastle,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTree,Maps.HideoutHelmLobby,Maps.CreepyCastleLobby,Maps.CrystalCavesLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby]
	if K.settings.kasplat_location_rando:
		c=[A for A in K.shuffled_kasplat_map.keys()]
		for L in range(216):
			E=js.pointer_addresses[16]['entries'][L]['pointing_to'];ROM().seek(E);d=int.from_bytes(ROM().readBytes(2),G);D=2;M=[];N=[]
			if d>0:
				for A in range(d):
					e=[];f=E+D;ROM().seek(E+D);p=int.from_bytes(ROM().readBytes(2),G);D+=p*6+2;ROM().seek(E+D);q=int.from_bytes(ROM().readBytes(2),G);D+=q*10+6;R=E+D;r=R-f;ROM().seek(R-4);N.append(int.from_bytes(ROM().readBytes(2),G));ROM().seek(f)
					for F in range(int(r/2)):e.append(int.from_bytes(ROM().readBytes(2),G))
					M.append(e);ROM().seek(R)
			s=E+D;ROM().seek(s);t=int.from_bytes(ROM().readBytes(2),G);D+=2;O=[];P=[]
			for A in range(t):
				ROM().seek(E+D);u=int.from_bytes(ROM().readBytes(1),G);ROM().seek(E+D+4);g=[]
				for F in range(3):
					S=int.from_bytes(ROM().readBytes(2),G)
					if S>32767:S-=65536
					g.append(S)
				ROM().seek(E+D+19);v=int.from_bytes(ROM().readBytes(1),G);P.append(v);T=D;ROM().seek(E+D+17);w=int.from_bytes(ROM().readBytes(1),G);D+=22+w*2;x=D;U=False;h=0
				for V in KasplatLocationList:
					W=KasplatLocationList[V]
					for C in W:
						if C.vanilla and C.name in c and C.map==L:
							i=0
							for F in range(3):
								if g[F]==C.coords[F]:i+=1
							if i==3:U=True;X=K.shuffled_kasplat_map[C.name];h=Q[X]
				if u not in Q or U or L not in o:
					B=[];y=x-T;ROM().seek(E+T)
					for A in range(y):
						if A==0 and U:B.append(h);ROM().seek(E+T+1)
						else:B.append(int.from_bytes(ROM().readBytes(1),G))
					O.append(B)
			J=1;H=1
			for V in KasplatLocationList:
				W=KasplatLocationList[V]
				for C in W:
					if L==C.map and C.name in c and not C.vanilla:
						if J in P:
							while J in P:J+=1
							P.append(J)
						if H in N:
							while H in N:H+=1
							N.append(H)
						B=[];X=K.shuffled_kasplat_map[C.name];B.append(Q[X]);B.append(122)
						for A in range(2):B.append(0)
						for A in C.coords:
							if A<0:A+=65536
							B.append(int(A/256));B.append(int(A%256))
						for A in range(2):B.append(0)
						B.append(35);B.append(60);B.append(H);B.append(50);B.append(1);B.append(0);B.append(2);B.append(J);B.append(30);B.append(0);O.append(B);I=[];Y=[C.bounds[0],0,C.bounds[2]];Z=[C.bounds[1],0,C.bounds[2]];a=[C.bounds[1],0,C.bounds[3]];b=[C.bounds[0],0,C.bounds[3]];j=[];k=[];l=[];m=[]
						for A in range(3):j.append(int((Y[A]+Z[A])/2));k.append(int((Z[A]+a[A])/2));l.append(int((a[A]+b[A])/2));m.append(int((b[A]+Y[A])/2))
						n=[Y,j,Z,k,a,l,b,m];I.append(len(n))
						for A in n:
							for F in A:
								if F<0:F+=65536
								I.append(F)
						I.append(0);I.append(H);I.append(1);M.append(I)
			ROM().seek(E);ROM().writeMultipleBytes(len(M),2)
			for A in M:
				for F in A:ROM().writeMultipleBytes(F,2)
			ROM().writeMultipleBytes(len(O),2)
			for A in O:
				for F in A:ROM().writeMultipleBytes(F,1)