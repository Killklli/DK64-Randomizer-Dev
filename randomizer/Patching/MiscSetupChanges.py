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
	'Randomize setup.';A6='coords';A5='corner';v='offset';u='center';t='item_list';s='map';h='rotation';g='numbers';f='subtype';T='offsets';S='item';O='weight';N='type';J='positions';E='big';C=spoiler;B='rot';A='number';A7=[{S:'orange',N:86,O:3},{S:'film',N:152,O:1},{S:'crystals',N:142,O:4},{S:'standard_crate',N:143,O:4},{S:'homing_crate',N:17,O:2}];i=[]
	for w in A7:
		for AT in range(w[O]):i.append(w[N])
	A8=[C.settings.fast_gbs,C.settings.randomize_pickups,C.settings.random_patches,C.settings.puzzle_rando,C.settings.hard_bosses,C.settings.high_req];j=False
	for A9 in A8:j=j or A9
	AA=[{s:Maps.AztecLlamaTemple,t:[188,555,553,554]},{s:Maps.CastleMuseum,t:[23]}];AB=[{f:A5,g:[{A:12,B:0},{A:3,B:1},{A:5,B:2},{A:6,B:3}]},{f:'edge',g:[{A:8,B:0},{A:10,B:0},{A:7,B:1},{A:16,B:1},{A:14,B:2},{A:9,B:2},{A:4,B:3},{A:1,B:3}]},{f:u,g:[{A:13,B:0},{A:15,B:0},{A:11,B:0},{A:2,B:0}]}]
	if j:
		for F in range(216):
			P=js.pointer_addresses[9]['entries'][F]['pointing_to'];ROM().seek(P);U=int.from_bytes(ROM().readBytes(4),E);k=[];V=[]
			if F==Maps.FranticFactory:W={A5:{T:[],J:[]},'edge':{T:[],J:[]},u:{T:[],J:[]}}
			for AC in range(U):
				D=P+4+AC*48;ROM().seek(D+40);G=int.from_bytes(ROM().readBytes(2),E);x=False
				for y in AA:
					if y[s]==F and G in y[t]:x=True
				if G==406 and C.settings.fast_gbs and F==Maps.FactoryBaboonBlast:ROM().seek(D+40);ROM().writeMultipleBytes(116,2);ROM().seek(D+12);ROM().writeMultipleBytes(1056964608,4)
				elif G in i and C.settings.randomize_pickups:ROM().seek(D+40);ROM().writeMultipleBytes(random.choice(i),2)
				elif x:
					if C.settings.puzzle_rando:k.append(D);ROM().seek(D);Q=int.from_bytes(ROM().readBytes(4),E);l=int.from_bytes(ROM().readBytes(4),E);m=int.from_bytes(ROM().readBytes(4),E);V.append([Q,l,m])
				elif G==565 and(F==Maps.GalleonBoss and C.settings.hard_bosses or F==Maps.HideoutHelm and C.settings.puzzle_rando):
					if F==Maps.HideoutHelm:n=[1055.704,3446.966];X=[123.128,235.971];Y=[-131,500]
					elif F==Maps.GalleonBoss:n=[1216,1478];X=[200,460];Y=[]
					z=X[0]+math.sqrt(random.random())*(X[1]-X[0]);Z=random.uniform(0,math.pi*2);o=random.uniform(0,360)
					if Z==math.pi*2:Z=0
					if o==360:o=0
					AD=z*math.sin(Z);AE=z*math.cos(Z);AF=n[0]+AD;AG=n[1]+AE;ROM().seek(D);ROM().writeMultipleBytes(int(float_to_hex(AF),16),4);ROM().seek(D+8);ROM().writeMultipleBytes(int(float_to_hex(AG),16),4);ROM().seek(D+28);ROM().writeMultipleBytes(int(float_to_hex(o),16),4)
					if len(Y)>0:AH=random.uniform(Y[0],Y[1]);ROM().seek(D+4);ROM().writeMultipleBytes(int(float_to_hex(AH),16),4)
				elif G==116 and F==Maps.GalleonLighthouse and C.settings.high_req:
					AI=[407.107,720,501.02]
					for (AJ,K) in enumerate(AI):ROM().seek(D+AJ*4);ROM().writeMultipleBytes(int(float_to_hex(K),16),4)
				elif F==Maps.FranticFactory and C.settings.puzzle_rando and G>=244 and G<=259:
					for A0 in AB:
						for p in A0[g]:
							if p[A]==G-243:a=A0[f];ROM().seek(D);Q=int.from_bytes(ROM().readBytes(4),E);l=int.from_bytes(ROM().readBytes(4),E);m=int.from_bytes(ROM().readBytes(4),E);W[a][T].append({v:D,h:p[B],A:G-243});W[a][J].append({A6:[Q,l,m],h:p[B]})
			if C.settings.puzzle_rando:
				if len(V)>0 and len(k)>0:
					random.shuffle(V)
					for (b,R) in enumerate(k):
						ROM().seek(R)
						for K in range(3):ROM().writeMultipleBytes(V[b][K],4)
				if F==Maps.FranticFactory:
					AK=[_A,'0x42B40000','0x43340000','0x43870000']
					for I in W:
						a=I;I=W[I];random.shuffle(I[J])
						for (b,R) in enumerate(I[T]):
							ROM().seek(R[v]);AL=R[h]
							for K in range(3):
								A1=I[J][b][A6][K]
								if K==1:A1=int(float_to_hex(1002),16)
								ROM().writeMultipleBytes(A1,4)
							q=I[J][b][h];A2=(AL-q+4)%4
							if a==u:A2=random.randint(0,3)
							ROM().seek(R[v]+28);q=(2+A2)%4;ROM().writeMultipleBytes(int(AK[q],16),4)
			ROM().seek(P+4+U*48);A3=int.from_bytes(ROM().readBytes(4),E);A4=P+4+U*48+4+A3*36;ROM().seek(P+4+U*48+4+A3*36);AM=int.from_bytes(ROM().readBytes(4),E);c=[];d=[]
			for AN in range(AM):
				r=A4+4+AN*56;ROM().seek(r+50);AO=int.from_bytes(ROM().readBytes(2),E)+16
				if C.settings.random_patches:
					if not AO==139:
						e=[];ROM().seek(r+52);d.append(int.from_bytes(ROM().readBytes(2),E));ROM().seek(r)
						for Q in range(int(56/4)):e.append(int.from_bytes(ROM().readBytes(4),E))
						c.append(e.copy())
			if C.settings.random_patches:
				L=32
				for AP in C.dirt_patch_placement:
					for M in DirtPatchLocations:
						if M.map_id==F and M.name==AP:
							if L in d:
								while L in d:L+=1
							H=[];H.append(int(float_to_hex(M.x),16));H.append(int(float_to_hex(M.y),16));H.append(int(float_to_hex(M.z),16));H.append(int(float_to_hex(1),16))
							for Q in range(8):H.append(0)
							AQ=hex(M.rotation)+'007B';H.append(int(AQ,16));AR=hex(L)+'46D0';d.append(L);L+=1;H.append(int(AR,16));c.append(H)
					ROM().seek(A4);ROM().writeMultipleBytes(len(c),4)
					for AS in c:
						for e in AS:ROM().writeMultipleBytes(e,4)