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
	'Randomize setup.';A5='coords';A4='corner';v='offset';u='center';t='item_list';s='map';r=False;e='rotation';d='numbers';c='subtype';Q='offsets';K='positions';D='big';C=spoiler;B='rot';A='number';w=[86,152,142,143,17]
	if C.settings.random_patches:
		f=[]
		for G in DirtPatchLocations:G.setPatch(r);f.append(G.name)
		for G in range(16):
			g=random.choice(f)
			for L in DirtPatchLocations:
				if L.name==g:L.setPatch(True);print(g);f.remove(g)
	A6=[C.settings.skip_arcader1,C.settings.randomize_pickups,C.settings.random_patches,C.settings.puzzle_rando];h=r
	for A7 in A6:h=h or A7
	A8=[{s:Maps.AztecLlamaTemple,t:[188,555,553,554]},{s:Maps.CastleMuseum,t:[23]}];A9=[{c:A4,d:[{A:12,B:0},{A:3,B:1},{A:5,B:2},{A:6,B:3}]},{c:'edge',d:[{A:8,B:0},{A:10,B:0},{A:7,B:1},{A:16,B:1},{A:14,B:2},{A:9,B:2},{A:4,B:3},{A:1,B:3}]},{c:u,d:[{A:13,B:0},{A:15,B:0},{A:11,B:0},{A:2,B:0}]}]
	if h:
		for F in range(216):
			P=js.pointer_addresses[9]['entries'][F]['pointing_to'];ROM().seek(P);R=int.from_bytes(ROM().readBytes(4),D);i=[];S=[]
			if F==Maps.FranticFactory:T={A4:{Q:[],K:[]},'edge':{Q:[],K:[]},u:{Q:[],K:[]}}
			for AA in range(R):
				E=P+4+AA*48;ROM().seek(E+40);H=int.from_bytes(ROM().readBytes(2),D);x=r
				for y in A8:
					if y[s]==F and H in y[t]:x=True
				if H==406 and C.settings.skip_arcader1 and F==Maps.FactoryBaboonBlast:ROM().seek(E+40);ROM().writeMultipleBytes(116,2);ROM().seek(E+12);ROM().writeMultipleBytes(1056964608,4)
				elif H in w and C.settings.randomize_pickups:ROM().seek(E+40);ROM().writeMultipleBytes(random.choice(w),2)
				elif x:
					if C.settings.puzzle_rando:i.append(E);ROM().seek(E);G=int.from_bytes(ROM().readBytes(4),D);L=int.from_bytes(ROM().readBytes(4),D);j=int.from_bytes(ROM().readBytes(4),D);S.append([G,L,j])
				elif(F==Maps.GalleonBoss or F==Maps.HideoutHelm)and H==565 and C.settings.puzzle_rando:
					if F==Maps.HideoutHelm:k=[1055.704,3446.966];l=[123.128,235.971];U=[-131,500]
					elif F==Maps.GalleonBoss:k=[1216,1478];l=[188,460];U=[]
					z=random.uniform(l[0],l[1]);V=random.uniform(0,math.pi*2);m=random.uniform(0,360)
					if V==math.pi*2:V=0
					if m==360:m=0
					AB=z*math.sin(V);AC=z*math.cos(V);AD=k[0]+AB;AE=k[1]+AC;ROM().seek(E);ROM().writeMultipleBytes(int(float_to_hex(AD),16),4);ROM().seek(E+8);ROM().writeMultipleBytes(int(float_to_hex(AE),16),4);ROM().seek(E+28);ROM().writeMultipleBytes(int(float_to_hex(m),16),4)
					if len(U)>0:AF=random.uniform(U[0],U[1]);ROM().seek(E+4);ROM().writeMultipleBytes(int(float_to_hex(AF),16),4)
				elif F==Maps.FranticFactory and C.settings.puzzle_rando and H>=244 and H<=259:
					for A0 in A9:
						for n in A0[d]:
							if n[A]==H-243:W=A0[c];ROM().seek(E);G=int.from_bytes(ROM().readBytes(4),D);L=int.from_bytes(ROM().readBytes(4),D);j=int.from_bytes(ROM().readBytes(4),D);T[W][Q].append({v:E,e:n[B],A:H-243});T[W][K].append({A5:[G,L,j],e:n[B]})
			if C.settings.puzzle_rando:
				if len(S)>0 and len(i)>0:
					random.shuffle(S)
					for (X,M) in enumerate(i):
						ROM().seek(M)
						for Y in range(3):ROM().writeMultipleBytes(S[X][Y],4)
				if F==Maps.FranticFactory:
					AG=[_A,'0x42B40000','0x43340000','0x43870000']
					for J in T:
						W=J;J=T[J];random.shuffle(J[K])
						for (X,M) in enumerate(J[Q]):
							ROM().seek(M[v]);AH=M[e]
							for Y in range(3):
								A1=J[K][X][A5][Y]
								if Y==1:A1=int(float_to_hex(1002),16)
								ROM().writeMultipleBytes(A1,4)
							o=J[K][X][e];p=(AH-o+4)%4;print(f"Number {M[A]} - Rotation Diff: {p}")
							if W==u:p=random.randint(0,3)
							ROM().seek(M[v]+28);o=(2+p)%4;ROM().writeMultipleBytes(int(AG[o],16),4)
			ROM().seek(P+4+R*48);A2=int.from_bytes(ROM().readBytes(4),D);A3=P+4+R*48+4+A2*36;ROM().seek(P+4+R*48+4+A2*36);AI=int.from_bytes(ROM().readBytes(4),D);Z=[];a=[]
			for AJ in range(AI):
				q=A3+4+AJ*56;ROM().seek(q+50);AK=int.from_bytes(ROM().readBytes(2),D)+16
				if C.settings.random_patches:
					if not AK==139:
						b=[];ROM().seek(q+52);a.append(int.from_bytes(ROM().readBytes(2),D));ROM().seek(q)
						for G in range(int(56/4)):b.append(int.from_bytes(ROM().readBytes(4),D))
						Z.append(b.copy())
			if C.settings.random_patches:
				N=32
				for O in DirtPatchLocations:
					if N in a:
						while N in a:N+=1
					if O.map_id==F and O.selected:
						I=[];I.append(int(float_to_hex(O.x),16));I.append(int(float_to_hex(O.y),16));I.append(int(float_to_hex(O.z),16));I.append(int(float_to_hex(1),16))
						for G in range(8):I.append(0)
						AL=hex(O.rotation)+'007B';I.append(int(AL,16));AM=hex(N)+'46D0';a.append(N);N+=1;I.append(int(AM,16));Z.append(I)
				ROM().seek(A3);ROM().writeMultipleBytes(len(Z),4)
				for AN in Z:
					for b in AN:ROM().writeMultipleBytes(b,4)