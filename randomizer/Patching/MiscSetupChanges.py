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
	'Randomize setup.';A9='coords';A8='corner';z='offset';y='center';x='item_list';w='map';v=False;h='rotation';g='numbers';f='subtype';T='offsets';S='item';Q='weight';P='type';K='positions';D='big';C=spoiler;B='rot';A='number';AA=[{S:'orange',P:86,Q:3},{S:'film',P:152,Q:1},{S:'crystals',P:142,Q:4},{S:'standard_crate',P:143,Q:4},{S:'homing_crate',P:17,Q:2}];i=[]
	for A0 in AA:
		for AT in range(A0[Q]):i.append(A0[P])
	if C.settings.random_patches:
		j=[]
		for G in DirtPatchLocations:G.setPatch(v);j.append(G.name)
		for G in range(16):
			k=random.choice(j)
			for L in DirtPatchLocations:
				if L.name==k:L.setPatch(True);print(k);j.remove(k)
	AB=[C.settings.skip_arcader1,C.settings.randomize_pickups,C.settings.random_patches,C.settings.puzzle_rando];l=v
	for AC in AB:l=l or AC
	AD=[{w:Maps.AztecLlamaTemple,x:[188,555,553,554]},{w:Maps.CastleMuseum,x:[23]}];AE=[{f:A8,g:[{A:12,B:0},{A:3,B:1},{A:5,B:2},{A:6,B:3}]},{f:'edge',g:[{A:8,B:0},{A:10,B:0},{A:7,B:1},{A:16,B:1},{A:14,B:2},{A:9,B:2},{A:4,B:3},{A:1,B:3}]},{f:y,g:[{A:13,B:0},{A:15,B:0},{A:11,B:0},{A:2,B:0}]}]
	if l:
		for F in range(216):
			R=js.pointer_addresses[9]['entries'][F]['pointing_to'];ROM().seek(R);U=int.from_bytes(ROM().readBytes(4),D);m=[];V=[]
			if F==Maps.FranticFactory:W={A8:{T:[],K:[]},'edge':{T:[],K:[]},y:{T:[],K:[]}}
			for AF in range(U):
				E=R+4+AF*48;ROM().seek(E+40);H=int.from_bytes(ROM().readBytes(2),D);A1=v
				for A2 in AD:
					if A2[w]==F and H in A2[x]:A1=True
				if H==406 and C.settings.skip_arcader1 and F==Maps.FactoryBaboonBlast:ROM().seek(E+40);ROM().writeMultipleBytes(116,2);ROM().seek(E+12);ROM().writeMultipleBytes(1056964608,4)
				elif H in i and C.settings.randomize_pickups:ROM().seek(E+40);ROM().writeMultipleBytes(random.choice(i),2)
				elif A1:
					if C.settings.puzzle_rando:m.append(E);ROM().seek(E);G=int.from_bytes(ROM().readBytes(4),D);L=int.from_bytes(ROM().readBytes(4),D);n=int.from_bytes(ROM().readBytes(4),D);V.append([G,L,n])
				elif(F==Maps.GalleonBoss or F==Maps.HideoutHelm)and H==565 and C.settings.puzzle_rando:
					if F==Maps.HideoutHelm:o=[1055.704,3446.966];p=[123.128,235.971];X=[-131,500]
					elif F==Maps.GalleonBoss:o=[1216,1478];p=[188,460];X=[]
					A3=random.uniform(p[0],p[1]);Y=random.uniform(0,math.pi*2);q=random.uniform(0,360)
					if Y==math.pi*2:Y=0
					if q==360:q=0
					AG=A3*math.sin(Y);AH=A3*math.cos(Y);AI=o[0]+AG;AJ=o[1]+AH;ROM().seek(E);ROM().writeMultipleBytes(int(float_to_hex(AI),16),4);ROM().seek(E+8);ROM().writeMultipleBytes(int(float_to_hex(AJ),16),4);ROM().seek(E+28);ROM().writeMultipleBytes(int(float_to_hex(q),16),4)
					if len(X)>0:AK=random.uniform(X[0],X[1]);ROM().seek(E+4);ROM().writeMultipleBytes(int(float_to_hex(AK),16),4)
				elif F==Maps.FranticFactory and C.settings.puzzle_rando and H>=244 and H<=259:
					for A4 in AE:
						for r in A4[g]:
							if r[A]==H-243:Z=A4[f];ROM().seek(E);G=int.from_bytes(ROM().readBytes(4),D);L=int.from_bytes(ROM().readBytes(4),D);n=int.from_bytes(ROM().readBytes(4),D);W[Z][T].append({z:E,h:r[B],A:H-243});W[Z][K].append({A9:[G,L,n],h:r[B]})
			if C.settings.puzzle_rando:
				if len(V)>0 and len(m)>0:
					random.shuffle(V)
					for (a,M) in enumerate(m):
						ROM().seek(M)
						for b in range(3):ROM().writeMultipleBytes(V[a][b],4)
				if F==Maps.FranticFactory:
					AL=[_A,'0x42B40000','0x43340000','0x43870000']
					for J in W:
						Z=J;J=W[J];random.shuffle(J[K])
						for (a,M) in enumerate(J[T]):
							ROM().seek(M[z]);AM=M[h]
							for b in range(3):
								A5=J[K][a][A9][b]
								if b==1:A5=int(float_to_hex(1002),16)
								ROM().writeMultipleBytes(A5,4)
							s=J[K][a][h];t=(AM-s+4)%4;print(f"Number {M[A]} - Rotation Diff: {t}")
							if Z==y:t=random.randint(0,3)
							ROM().seek(M[z]+28);s=(2+t)%4;ROM().writeMultipleBytes(int(AL[s],16),4)
			ROM().seek(R+4+U*48);A6=int.from_bytes(ROM().readBytes(4),D);A7=R+4+U*48+4+A6*36;ROM().seek(R+4+U*48+4+A6*36);AN=int.from_bytes(ROM().readBytes(4),D);c=[];d=[]
			for AO in range(AN):
				u=A7+4+AO*56;ROM().seek(u+50);AP=int.from_bytes(ROM().readBytes(2),D)+16
				if C.settings.random_patches:
					if not AP==139:
						e=[];ROM().seek(u+52);d.append(int.from_bytes(ROM().readBytes(2),D));ROM().seek(u)
						for G in range(int(56/4)):e.append(int.from_bytes(ROM().readBytes(4),D))
						c.append(e.copy())
			if C.settings.random_patches:
				N=32
				for O in DirtPatchLocations:
					if N in d:
						while N in d:N+=1
					if O.map_id==F and O.selected:
						I=[];I.append(int(float_to_hex(O.x),16));I.append(int(float_to_hex(O.y),16));I.append(int(float_to_hex(O.z),16));I.append(int(float_to_hex(1),16))
						for G in range(8):I.append(0)
						AQ=hex(O.rotation)+'007B';I.append(int(AQ,16));AR=hex(N)+'46D0';d.append(N);N+=1;I.append(int(AR,16));c.append(I)
				ROM().seek(A7);ROM().writeMultipleBytes(len(c),4)
				for AS in c:
					for e in AS:ROM().writeMultipleBytes(e,4)