'Apply barrel changes.'
_A='0x00000000'
import js,random,struct,math
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Lists.Patches import DirtPatchLocations
from randomizer.Lists.MapsAndExits import Maps
def float_to_hex(f):
	'Convert float to hex.'
	if f==0:return _A
	return hex(struct.unpack('<I',struct.pack('<f',f))[0])
def randomize_setup(spoiler):
	'Randomize setup.';A6='coords';A5='corner';w='offset';v='center';u='item_list';t='map';h='rotation';g='numbers';f='subtype';S='offsets';R='item';O='weight';N='type';J='positions';D='big';C=spoiler;B='rot';A='number';A7=[{R:'orange',N:86,O:3},{R:'film',N:152,O:1},{R:'crystals',N:142,O:4},{R:'standard_crate',N:143,O:4},{R:'homing_crate',N:17,O:2}];i=[]
	for x in A7:
		for AR in range(x[O]):i.append(x[N])
	A8=[C.settings.fast_gbs,C.settings.randomize_pickups,C.settings.random_patches,C.settings.puzzle_rando];j=False
	for A9 in A8:j=j or A9
	AA=[{t:Maps.AztecLlamaTemple,u:[188,555,553,554]},{t:Maps.CastleMuseum,u:[23]}];AB=[{f:A5,g:[{A:12,B:0},{A:3,B:1},{A:5,B:2},{A:6,B:3}]},{f:'edge',g:[{A:8,B:0},{A:10,B:0},{A:7,B:1},{A:16,B:1},{A:14,B:2},{A:9,B:2},{A:4,B:3},{A:1,B:3}]},{f:v,g:[{A:13,B:0},{A:15,B:0},{A:11,B:0},{A:2,B:0}]}]
	if j:
		for F in range(216):
			P=js.pointer_addresses[9]['entries'][F]['pointing_to'];ROM().seek(P);T=int.from_bytes(ROM().readBytes(4),D);k=[];U=[]
			if F==Maps.FranticFactory:V={A5:{S:[],J:[]},'edge':{S:[],J:[]},v:{S:[],J:[]}}
			for AC in range(T):
				E=P+4+AC*48;ROM().seek(E+40);G=int.from_bytes(ROM().readBytes(2),D);y=False
				for z in AA:
					if z[t]==F and G in z[u]:y=True
				if G==406 and C.settings.fast_gbs and F==Maps.FactoryBaboonBlast:ROM().seek(E+40);ROM().writeMultipleBytes(116,2);ROM().seek(E+12);ROM().writeMultipleBytes(1056964608,4)
				elif G in i and C.settings.randomize_pickups:ROM().seek(E+40);ROM().writeMultipleBytes(random.choice(i),2)
				elif y:
					if C.settings.puzzle_rando:k.append(E);ROM().seek(E);Q=int.from_bytes(ROM().readBytes(4),D);l=int.from_bytes(ROM().readBytes(4),D);m=int.from_bytes(ROM().readBytes(4),D);U.append([Q,l,m])
				elif(F==Maps.GalleonBoss or F==Maps.HideoutHelm)and G==565 and C.settings.puzzle_rando:
					if F==Maps.HideoutHelm:n=[1055.704,3446.966];W=[123.128,235.971];X=[-131,500]
					elif F==Maps.GalleonBoss:n=[1216,1478];W=[200,460];X=[]
					A0=W[0]+math.sqrt(random.random())*(W[1]-W[0]);Y=random.uniform(0,math.pi*2);o=random.uniform(0,360)
					if Y==math.pi*2:Y=0
					if o==360:o=0
					AD=A0*math.sin(Y);AE=A0*math.cos(Y);AF=n[0]+AD;AG=n[1]+AE;ROM().seek(E);ROM().writeMultipleBytes(int(float_to_hex(AF),16),4);ROM().seek(E+8);ROM().writeMultipleBytes(int(float_to_hex(AG),16),4);ROM().seek(E+28);ROM().writeMultipleBytes(int(float_to_hex(o),16),4)
					if len(X)>0:AH=random.uniform(X[0],X[1]);ROM().seek(E+4);ROM().writeMultipleBytes(int(float_to_hex(AH),16),4)
				elif F==Maps.FranticFactory and C.settings.puzzle_rando and G>=244 and G<=259:
					for A1 in AB:
						for p in A1[g]:
							if p[A]==G-243:Z=A1[f];ROM().seek(E);Q=int.from_bytes(ROM().readBytes(4),D);l=int.from_bytes(ROM().readBytes(4),D);m=int.from_bytes(ROM().readBytes(4),D);V[Z][S].append({w:E,h:p[B],A:G-243});V[Z][J].append({A6:[Q,l,m],h:p[B]})
			if C.settings.puzzle_rando:
				if len(U)>0 and len(k)>0:
					random.shuffle(U)
					for (a,K) in enumerate(k):
						ROM().seek(K)
						for b in range(3):ROM().writeMultipleBytes(U[a][b],4)
				if F==Maps.FranticFactory:
					AI=[_A,'0x42B40000','0x43340000','0x43870000']
					for I in V:
						Z=I;I=V[I];random.shuffle(I[J])
						for (a,K) in enumerate(I[S]):
							ROM().seek(K[w]);AJ=K[h]
							for b in range(3):
								A2=I[J][a][A6][b]
								if b==1:A2=int(float_to_hex(1002),16)
								ROM().writeMultipleBytes(A2,4)
							q=I[J][a][h];r=(AJ-q+4)%4;print(f"Number {K[A]} - Rotation Diff: {r}")
							if Z==v:r=random.randint(0,3)
							ROM().seek(K[w]+28);q=(2+r)%4;ROM().writeMultipleBytes(int(AI[q],16),4)
			ROM().seek(P+4+T*48);A3=int.from_bytes(ROM().readBytes(4),D);A4=P+4+T*48+4+A3*36;ROM().seek(P+4+T*48+4+A3*36);AK=int.from_bytes(ROM().readBytes(4),D);c=[];d=[]
			for AL in range(AK):
				s=A4+4+AL*56;ROM().seek(s+50);AM=int.from_bytes(ROM().readBytes(2),D)+16
				if C.settings.random_patches:
					if not AM==139:
						e=[];ROM().seek(s+52);d.append(int.from_bytes(ROM().readBytes(2),D));ROM().seek(s)
						for Q in range(int(56/4)):e.append(int.from_bytes(ROM().readBytes(4),D))
						c.append(e.copy())
			if C.settings.random_patches:
				L=32
				for AN in C.dirt_patch_placement:
					for M in DirtPatchLocations:
						if M.map_id==F and M.name==AN:
							if L in d:
								while L in d:L+=1
							H=[];H.append(int(float_to_hex(M.x),16));H.append(int(float_to_hex(M.y),16));H.append(int(float_to_hex(M.z),16));H.append(int(float_to_hex(1),16))
							for Q in range(8):H.append(0)
							AO=hex(M.rotation)+'007B';H.append(int(AO,16));AP=hex(L)+'46D0';d.append(L);L+=1;H.append(int(AP,16));c.append(H)
					ROM().seek(A4);ROM().writeMultipleBytes(len(c),4)
					for AQ in c:
						for e in AQ:ROM().writeMultipleBytes(e,4)