'Apply CB Rando changes.'
_B='balloons'
_A='cb'
import js
from randomizer.Patching.Patcher import ROM
from randomizer.Enums.Levels import Levels
from randomizer.Spoiler import Spoiler
from randomizer.Patching.Lib import float_to_hex,short_to_ushort
import randomizer.Lists.CBLocations.JungleJapesCBLocations,randomizer.Lists.CBLocations.AngryAztecCBLocations,randomizer.Lists.CBLocations.FranticFactoryCBLocations,randomizer.Lists.CBLocations.GloomyGalleonCBLocations,randomizer.Lists.CBLocations.FungiForestCBLocations,randomizer.Lists.CBLocations.CrystalCavesCBLocations,randomizer.Lists.CBLocations.CreepyCastleCBLocations
level_data={Levels.JungleJapes:{_A:randomizer.Lists.CBLocations.JungleJapesCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.JungleJapesCBLocations.BalloonList},Levels.AngryAztec:{_A:randomizer.Lists.CBLocations.AngryAztecCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.AngryAztecCBLocations.BalloonList},Levels.FranticFactory:{_A:randomizer.Lists.CBLocations.FranticFactoryCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.FranticFactoryCBLocations.BalloonList},Levels.GloomyGalleon:{_A:randomizer.Lists.CBLocations.GloomyGalleonCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.GloomyGalleonCBLocations.BalloonList},Levels.FungiForest:{_A:randomizer.Lists.CBLocations.FungiForestCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.FungiForestCBLocations.BalloonList},Levels.CrystalCaves:{_A:randomizer.Lists.CBLocations.CrystalCavesCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.CrystalCavesCBLocations.BalloonList},Levels.CreepyCastle:{_A:randomizer.Lists.CBLocations.CreepyCastleCBLocations.ColoredBananaGroupList,_B:randomizer.Lists.CBLocations.CreepyCastleCBLocations.BalloonList}}
def randomize_cbs(spoiler):
	'Place Colored Bananas into ROM.';u='pointing_to';t='entries';k=spoiler;j=True;i=False;h='kong';B='big'
	if k.settings.cb_rando:
		for W in range(216):
			v=[10,13,22,30,31,43,517,518,519,520];w=[91,111,112,113,114];G=js.pointer_addresses[9][t][W][u];ROM().seek(G);N=int.from_bytes(ROM().readBytes(4),B);O=[];X=[]
			for J in range(N):
				Y=G+4+J*48;ROM().seek(Y+40);x=int.from_bytes(ROM().readBytes(2),B)
				if x not in v:
					ROM().seek(Y+42);X.append(int.from_bytes(ROM().readBytes(2),B));ROM().seek(Y);A=[]
					for C in range(int(48/4)):A.append(int.from_bytes(ROM().readBytes(4),B))
					O.append(A)
			ROM().seek(G+4+48*N);l=int.from_bytes(ROM().readBytes(4),B);Z=[]
			for J in range(l):
				ROM().seek(G+4+N*48+4+J*36);A=[]
				for C in range(int(36/4)):A.append(int.from_bytes(ROM().readBytes(4),B))
				Z.append(A)
			m=G+4+48*N+4+36*l;ROM().seek(m);y=int.from_bytes(ROM().readBytes(4),B);P=[];a=[];b=[]
			for J in range(y):
				Q=m+4+J*56;ROM().seek(Q+50);z=int.from_bytes(ROM().readBytes(2),B)+16
				if z not in w:
					ROM().seek(Q+52);a.append(int.from_bytes(ROM().readBytes(2),B));ROM().seek(Q);A=[]
					for C in range(int(56/4)):A.append(int.from_bytes(ROM().readBytes(4),B))
					P.append(A)
				else:
					ROM().seek(Q+18);K=int.from_bytes(ROM().readBytes(2),B)
					if K not in b:b.append(K)
			R=js.pointer_addresses[15][t][W][u];ROM().seek(R);A0=int.from_bytes(ROM().readBytes(2),B);H=[];c=[];d=2
			for A7 in range(A0):
				ROM().seek(R+d);K=int.from_bytes(ROM().readBytes(2),B);n=int.from_bytes(ROM().readBytes(2),B)
				if K not in b:
					A1=6+n*10;A=[];ROM().seek(R+d)
					for C in range(int(A1/2)):A.append(int.from_bytes(ROM().readBytes(2),B))
					H.append(A);c.append(K)
				d+=6+10*n
			S=0;T=0;U=0
			for D in k.cb_placements:
				if D['map']==W:
					e=D['type'];A2=level_data[D['level']][e]
					if e==_A:
						A3=[13,10,30,22,31];A4=[43,520,517,519,518]
						for L in D['locations']:
							A=[];A.extend([int(float_to_hex(L[2]),16),int(float_to_hex(L[3]),16),int(float_to_hex(L[4]),16),int(float_to_hex(L[1]),16)]);A.append(2);A.append(29884415)
							for C in range(int((36-24)/4)):A.append(0)
							A.append(1077936128);f=0
							if L[0]==5:f=A4[D[h]]
							else:f=A3[D[h]]
							o=i;p=0
							while not o:
								if S not in X:X.append(S);p=S;o=j
								S+=1
							A.append((f<<16)+p);A.append((2<<16)+1);O.append(A)
					for I in A2:
						if e==_B and I.id==D['id']:
							A5=[114,91,113,112,111];A=[]
							for A6 in I.setSpawnPoint(I.points):A.append(int(float_to_hex(A6),16))
							A.append(int(float_to_hex(1),16));q=i;E=0;r=i;s=0
							while not q:
								if U not in c:c.append(U);E=U;q=j
								U+=1
							while not r:
								if T not in a:a.append(T);s=T;r=j
								T+=1
							if E<26:A.append(E)
							else:A.append(65535)
							A.append(I.speed)
							for C in range(int((48-24)/4)):A.append(0)
							A.append(A5[D[h]]-16);A.append((s<<16)+28168);P.append(A)
							if E<26:
								A=[];A.append(E);A.append(len(I.points));A.append(0)
								for g in I.points:A.append(20);A.append(short_to_ushort(g[0]));A.append(short_to_ushort(g[1]));A.append(short_to_ushort(g[2]));A.append((1<<8)+0)
								V=[]
								for M in H:
									if M[0]<E:V.append(M)
								V.append(A)
								for M in H:
									if M[0]>E:V.append(M)
								H=V.copy()
			ROM().seek(G);ROM().writeMultipleBytes(len(O),4)
			for C in O:
				for F in C:ROM().writeMultipleBytes(F,4)
			ROM().writeMultipleBytes(len(Z),4)
			for C in Z:
				for F in C:ROM().writeMultipleBytes(F,4)
			ROM().writeMultipleBytes(len(P),4)
			for C in P:
				for F in C:ROM().writeMultipleBytes(F,4)
			ROM().seek(R);ROM().writeMultipleBytes(len(H),2)
			for C in H:
				for F in C:ROM().writeMultipleBytes(F,2)