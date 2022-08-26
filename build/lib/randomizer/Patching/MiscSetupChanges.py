'Apply barrel changes.'
_E='0x00000000'
_D=True
_C='picked'
_B=False
_A='index'
import math,random,struct,js
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Patches import DirtPatchLocations
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def float_to_hex(f):
	'Convert float to hex.'
	if f==0:return _E
	return hex(struct.unpack('<I',struct.pack('<f',f))[0])
def pickRandomPositionCircle(center_x,center_z,min_radius,max_radius):
	'Pick a random position within a torus where the center and radius boundaries are specified.';B=min_radius;C=B+math.sqrt(random.random())*(max_radius-B);A=random.uniform(0,math.pi*2)
	if A==math.pi*2:A=0
	D=C*math.sin(A);E=C*math.cos(A);F=center_x+D;G=center_z+E;return[F,G]
def pickRandomPositionsMult(center_x,center_z,min_radius,max_radius,count,min_dist):
	"Pick multiple points within a torus where the center and radius boundaries are defined. There is a failsafe to make sure 2 points aren't within a certain specified distance away from each other.";B=[]
	for H in range(count):
		A=_B
		while not A:
			C=pickRandomPositionCircle(center_x,center_z,min_radius,max_radius)
			if len(B)==0:A=_D
			else:
				A=_D
				for D in B:
					E=D[0]-C[0];F=D[1]-C[1];G=math.sqrt(E*E+F*F)
					if G<min_dist:A=_B
			if A:B.append(C)
	return{_C:B.copy(),_A:0}
def pickChunkyCabinPadPositions():
	"Pick 3 points within a torus in Chunky's 5-door cabin where the center and radius boundaries are defined. There are failsafes to make sure 2 points are far enough apart and all points are easy enough to reach for casual game play purposes.";I=[];C=[[169.53,205.91],[435.219,483.118]];B=[294.594,337.22];N=70
	for R in range(3):
		D=_B
		while not D:
			A=pickRandomPositionCircle(B[0],B[1],70,180)
			for J in C:
				E=A[0]-J[0];F=A[1]-J[1];K=math.sqrt(E*E+F*F)
				if K<N:
					G=A[0]
					if J[0]<B[0]:G=G+70
					else:G=G-70
					H=A[1]
					if J[1]<B[1]:H=H+70
					else:H=H-70
					A=random.choice([[G,A[1]],[A[0],H]])
			O=C[0][0]<A[0]<B[0]and C[0][1]<A[1]<B[1];P=B[0]<A[0]<C[1][0]and B[1]<A[1]<C[1][1]
			if O or P:L=294.594;Q=A[0]-L;A[0]=L-Q
			if len(I)==0:D=_D
			else:
				D=_D
				for M in I:
					E=M[0]-A[0];F=M[1]-A[1];K=math.sqrt(E*E+F*F)
					if K<70:D=_B
			if D:I.append(A)
	return{_C:I.copy(),_A:0}
def randomize_setup(spoiler):
	'Randomize setup.';AE='coords';AD='corner';A5='offset';A4='center';m='rotation';l='numbers';k='subtype';b='offsets';a='item';V='item_list';U='map';T='weight';S='type';M='positions';G='big';D='rot';C='number';A=spoiler;AF=[{a:'orange',S:86,T:3},{a:'film',S:152,T:1},{a:'crystals',S:142,T:4},{a:'standard_crate',S:143,T:4},{a:'homing_crate',S:17,T:2}];n=[]
	for A6 in AF:
		for AX in range(A6[T]):n.append(A6[S])
	AG=[A.settings.fast_gbs,A.settings.randomize_pickups,A.settings.random_patches,A.settings.puzzle_rando,A.settings.hard_bosses,A.settings.high_req];o=_B
	for AH in AG:o=o or AH
	AI=[{U:Maps.AztecLlamaTemple,V:[188,555,553,554]},{U:Maps.CastleMuseum,V:[23]},{U:Maps.AztecTinyTemple,V:[167,166,165,164]},{U:Maps.FranticFactory,V:[333,332,331,330]},{U:Maps.CastleCrypt,V:[583,584,585,586]}];AJ=[{k:AD,l:[{C:12,D:0},{C:3,D:1},{C:5,D:2},{C:6,D:3}]},{k:'edge',l:[{C:8,D:0},{C:10,D:0},{C:7,D:1},{C:16,D:1},{C:14,D:2},{C:9,D:2},{C:4,D:3},{C:1,D:3}]},{k:A4,l:[{C:13,D:0},{C:15,D:0},{C:11,D:0},{C:2,D:0}]}];p=[[212.543,120.5,963.536],[100.017,120.5,569.51],[497.464,120.5,458.709],[401.557,138.167,754.136],[318.119,138.167,752.011],[311.555,138.167,666.162],[398.472,138.167,668.426]]
	if o:
		q=pickRandomPositionsMult(287.94,312.119,0,140,6,40);c=pickRandomPositionsMult(274.9,316.505,40,160,6,40);r=pickChunkyCabinPadPositions();random.shuffle(p);d=0
		for E in range(216):
			N=js.pointer_addresses[9]['entries'][E]['pointing_to'];ROM().seek(N);W=int.from_bytes(ROM().readBytes(4),G);s=[];X=[]
			if E==Maps.FranticFactory:e={AD:{b:[],M:[]},'edge':{b:[],M:[]},A4:{b:[],M:[]}}
			for AK in range(W):
				B=N+4+AK*48;ROM().seek(B+40);F=int.from_bytes(ROM().readBytes(2),G);A7=_B
				for A8 in AI:
					if A8[U]==E and F in A8[V]:A7=_D
				if F==406 and A.settings.fast_gbs and E==Maps.FactoryBaboonBlast:ROM().seek(B+40);ROM().writeMultipleBytes(116,2);ROM().seek(B+12);ROM().writeMultipleBytes(1056964608,4)
				elif F in n and A.settings.randomize_pickups:ROM().seek(B+40);ROM().writeMultipleBytes(random.choice(n),2)
				elif A7:
					if A.settings.puzzle_rando:s.append(B);ROM().seek(B);Y=int.from_bytes(ROM().readBytes(4),G);t=int.from_bytes(ROM().readBytes(4),G);u=int.from_bytes(ROM().readBytes(4),G);ROM().seek(B+28);AL=int.from_bytes(ROM().readBytes(4),G);X.append([Y,t,u,AL])
				elif F==565 and(E==Maps.GalleonBoss and A.settings.hard_bosses or E==Maps.HideoutHelm and A.settings.puzzle_rando):
					if E==Maps.HideoutHelm:v=[1055.704,3446.966];w=[123.128,235.971];f=[-131,500]
					elif E==Maps.GalleonBoss:v=[1216,1478];w=[200,460];f=[]
					A9=pickRandomPositionCircle(v[0],v[1],w[0],w[1]);x=random.uniform(0,360)
					if x==360:x=0
					AM=A9[0];AN=A9[1];ROM().seek(B);ROM().writeMultipleBytes(int(float_to_hex(AM),16),4);ROM().seek(B+8);ROM().writeMultipleBytes(int(float_to_hex(AN),16),4);ROM().seek(B+28);ROM().writeMultipleBytes(int(float_to_hex(x),16),4)
					if len(f)>0:AO=random.uniform(f[0],f[1]);ROM().seek(B+4);ROM().writeMultipleBytes(int(float_to_hex(AO),16),4)
				elif F==116 and E==Maps.GalleonLighthouse and A.settings.high_req:
					AP=[407.107,720,501.02]
					for (AQ,I) in enumerate(AP):ROM().seek(B+AQ*4);ROM().writeMultipleBytes(int(float_to_hex(I),16),4)
				elif E==Maps.FranticFactory and A.settings.puzzle_rando and F>=244 and F<=259:
					for AA in AJ:
						for y in AA[l]:
							if y[C]==F-243:g=AA[k];ROM().seek(B);Y=int.from_bytes(ROM().readBytes(4),G);t=int.from_bytes(ROM().readBytes(4),G);u=int.from_bytes(ROM().readBytes(4),G);e[g][b].append({A5:B,m:y[D],C:F-243});e[g][M].append({AE:[Y,t,u],m:y[D]})
				elif E==Maps.ForestLankyMushroomsRoom and A.settings.puzzle_rando:
					if F>=442 and F<=446:H=c[_C][c[_A]];ROM().seek(B);ROM().writeMultipleBytes(int(float_to_hex(H[0]),16),4);ROM().seek(B+8);ROM().writeMultipleBytes(int(float_to_hex(H[1]),16),4);c[_A]+=1
					elif F==517:H=c[_C][0];ROM().seek(B);ROM().writeMultipleBytes(int(float_to_hex(H[0]),16),4);ROM().seek(B+8);ROM().writeMultipleBytes(int(float_to_hex(H[1]),16),4)
				elif E==Maps.AngryAztec and A.settings.puzzle_rando and(F==289 or F>=550 and F<=552):
					ROM().seek(B)
					for I in range(3):ROM().writeMultipleBytes(int(float_to_hex(p[d][I]),16),4)
					d+=1
				elif E==Maps.CavesChunkyCabin and A.settings.puzzle_rando and F==515:H=r[_C][r[_A]];ROM().seek(B);ROM().writeMultipleBytes(int(float_to_hex(H[0]),16),4);ROM().seek(B+8);ROM().writeMultipleBytes(int(float_to_hex(H[1]),16),4);r[_A]+=1
			if A.settings.puzzle_rando:
				if len(X)>0 and len(s)>0:
					random.shuffle(X)
					for (Z,O) in enumerate(s):
						ROM().seek(O)
						for I in range(3):ROM().writeMultipleBytes(X[Z][I],4)
						ROM().seek(O+28);ROM().writeMultipleBytes(X[Z][3],4)
				if E==Maps.FranticFactory:
					AR=[_E,'0x42B40000','0x43340000','0x43870000']
					for L in e:
						g=L;L=e[L];random.shuffle(L[M])
						for (Z,O) in enumerate(L[b]):
							ROM().seek(O[A5]);AS=O[m]
							for I in range(3):
								AB=L[M][Z][AE][I]
								if I==1:AB=int(float_to_hex(1002),16)
								ROM().writeMultipleBytes(AB,4)
							z=L[M][Z][m];AC=(AS-z+4)%4
							if g==A4:AC=random.randint(0,3)
							ROM().seek(O[A5]+28);z=(2+AC)%4;ROM().writeMultipleBytes(int(AR[z],16),4)
			ROM().seek(N+4+W*48);A0=int.from_bytes(ROM().readBytes(4),G);A1=N+4+W*48+4+A0*36;ROM().seek(N+4+W*48+4+A0*36);A2=int.from_bytes(ROM().readBytes(4),G);h=[];i=[]
			for A3 in range(A2):
				J=A1+4+A3*56;ROM().seek(J+50);P=int.from_bytes(ROM().readBytes(2),G)+16
				if A.settings.random_patches:
					if not P==139:
						j=[];ROM().seek(J+52);i.append(int.from_bytes(ROM().readBytes(2),G));ROM().seek(J)
						for Y in range(int(56/4)):j.append(int.from_bytes(ROM().readBytes(4),G))
						h.append(j.copy())
			if A.settings.random_patches:
				Q=32
				for AT in A.dirt_patch_placement:
					for R in DirtPatchLocations:
						if R.map_id==E and R.name==AT:
							if Q in i:
								while Q in i:Q+=1
							K=[];K.append(int(float_to_hex(R.x),16));K.append(int(float_to_hex(R.y),16));K.append(int(float_to_hex(R.z),16));K.append(int(float_to_hex(1),16))
							for Y in range(8):K.append(0)
							AU=hex(R.rotation)+'007B';K.append(int(AU,16));AV=hex(Q)+'46D0';i.append(Q);Q+=1;K.append(int(AV,16));h.append(K)
					ROM().seek(A1);ROM().writeMultipleBytes(len(h),4)
					for AW in h:
						for j in AW:ROM().writeMultipleBytes(j,4)
			ROM().seek(N+4+W*48+4+A0*36);A2=int.from_bytes(ROM().readBytes(4),G);AY=[]
			for A3 in range(A2):
				J=A1+4+A3*56;ROM().seek(J+50);P=int.from_bytes(ROM().readBytes(2),G)+16
				if P>=100 and P<=105 and A.settings.puzzle_rando and E==Maps.CavesDiddyIgloo:H=q[_C][q[_A]];ROM().seek(J);ROM().writeMultipleBytes(int(float_to_hex(H[0]),16),4);ROM().seek(J+8);ROM().writeMultipleBytes(int(float_to_hex(H[1]),16),4);q[_A]+=1
				elif P>=64 and P<=66 and A.settings.puzzle_rando and E==Maps.AngryAztec:
					ROM().seek(J)
					for I in range(3):ROM().writeMultipleBytes(int(float_to_hex(p[d][I]),16),4)
					d+=1