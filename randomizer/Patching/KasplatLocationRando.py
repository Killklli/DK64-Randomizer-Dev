'Apply Boss Locations.'
import random,js
from randomizer.Lists.EnemyTypes import Enemies,EnemyMetaData
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Lists.KasplatLocations import KasplatLocationList
from randomizer.Enums.Kongs import GetKongs
def randomize_kasplat_locations(spoiler):
	'Write replaced enemies to ROM.';o=False;G='big';R=[Enemies.KasplatDK,Enemies.KasplatDiddy,Enemies.KasplatLanky,Enemies.KasplatTiny,Enemies.KasplatChunky];p=[Maps.JungleJapes,Maps.JapesUnderGround,Maps.AngryAztec,Maps.AztecChunky5DTemple,Maps.AztecLlamaTemple,Maps.FranticFactory,Maps.GloomyGalleon,Maps.FungiForest,Maps.ForestGiantMushroom,Maps.CrystalCaves,Maps.CreepyCastle,Maps.CastleUpperCave,Maps.CastleLowerCave,Maps.CastleTree,Maps.HideoutHelmLobby,Maps.CreepyCastleLobby,Maps.CrystalCavesLobby,Maps.FranticFactoryLobby,Maps.GloomyGalleonLobby]
	if spoiler.settings.kasplat_rando:
		for I in KasplatLocationList:
			print(I);H=KasplatLocationList[I]
			for A in H:A.setKasplat(state=o)
			q=GetKongs()
			for (r,a) in enumerate(q):
				b=[]
				for A in H:
					if not A.selected and a in A.kong_lst:b.append(A.name)
				c=random.choice(b)
				for A in H:
					if A.name==c:A.setKasplat();A.selected_kong_idx=r;A.selected_kong=a;print(c)
		for M in range(216):
			E=js.pointer_addresses[16]['entries'][M]['pointing_to'];ROM().seek(E);d=int.from_bytes(ROM().readBytes(2),G);D=2;N=[];O=[]
			if d>0:
				for B in range(d):
					e=[];f=E+D;ROM().seek(E+D);s=int.from_bytes(ROM().readBytes(2),G);D+=s*6+2;ROM().seek(E+D);t=int.from_bytes(ROM().readBytes(2),G);D+=t*10+6;S=E+D;u=S-f;ROM().seek(S-4);O.append(int.from_bytes(ROM().readBytes(2),G));ROM().seek(f)
					for F in range(int(u/2)):e.append(int.from_bytes(ROM().readBytes(2),G))
					N.append(e);ROM().seek(S)
			v=E+D;ROM().seek(v);w=int.from_bytes(ROM().readBytes(2),G);D+=2;P=[];Q=[]
			for B in range(w):
				ROM().seek(E+D);x=int.from_bytes(ROM().readBytes(1),G);ROM().seek(E+D+4);g=[]
				for F in range(3):
					T=int.from_bytes(ROM().readBytes(2),G)
					if T>32767:T-=65536
					g.append(T)
				ROM().seek(E+D+19);y=int.from_bytes(ROM().readBytes(1),G);Q.append(y);U=D;ROM().seek(E+D+17);z=int.from_bytes(ROM().readBytes(1),G);D+=22+z*2;A0=D;V=o;h=0
				for I in KasplatLocationList:
					H=KasplatLocationList[I]
					for A in H:
						if A.vanilla and A.selected and A.map==M:
							i=0
							for F in range(3):
								if g[F]==A.coords[F]:i+=1
							if i==3:V=True;h=R[A.selected_kong_idx]
				if x not in R or V or M not in p:
					C=[];A1=A0-U;ROM().seek(E+U)
					for B in range(A1):
						if B==0 and V:C.append(h);ROM().seek(E+U+1)
						else:C.append(int.from_bytes(ROM().readBytes(1),G))
					P.append(C)
			L=1;J=1
			for I in KasplatLocationList:
				H=KasplatLocationList[I]
				for A in H:
					if M==A.map and A.selected and not A.vanilla:
						if L in Q:
							while L in Q:L+=1
							Q.append(L)
						if J in O:
							while J in O:J+=1
							O.append(J)
						C=[];C.append(R[A.selected_kong_idx]);C.append(122)
						for B in range(2):C.append(0)
						for B in A.coords:
							if B<0:B+=65536
							C.append(int(B/256));C.append(int(B%256))
						for B in range(2):C.append(0)
						C.append(35);C.append(60);C.append(J);C.append(50);C.append(1);C.append(0);C.append(2);C.append(L);C.append(30);C.append(0);P.append(C);K=[];W=[A.bounds[0],0,A.bounds[2]];X=[A.bounds[1],0,A.bounds[2]];Y=[A.bounds[1],0,A.bounds[3]];Z=[A.bounds[0],0,A.bounds[3]];j=[];k=[];l=[];m=[]
						for B in range(3):j.append(int((W[B]+X[B])/2));k.append(int((X[B]+Y[B])/2));l.append(int((Y[B]+Z[B])/2));m.append(int((Z[B]+W[B])/2))
						n=[W,j,X,k,Y,l,Z,m];K.append(len(n))
						for B in n:
							for F in B:
								if F<0:F+=65536
								K.append(F)
						K.append(0);K.append(J);K.append(1);N.append(K)
			ROM().seek(E);ROM().writeMultipleBytes(len(N),2)
			for B in N:
				for F in B:ROM().writeMultipleBytes(F,2)
			ROM().writeMultipleBytes(len(P),2)
			for B in P:
				for F in B:ROM().writeMultipleBytes(F,1)