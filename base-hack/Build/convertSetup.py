'Convert file setup.'
_C='_.bin'
_B='.bin'
_A='big'
import os,shutil,struct
from getMoveSignLocations import getMoveSignData
from place_vines import generateVineSeries
def convertSetup(file_name):
	'Convert file type setup.\n\n    Args:\n        file_name (str): File name to convert.\n    ';B='_';A=file_name
	with open(A,'rb')as C:
		with open(B+A,'wb')as D:D.write(C.read())
	E=int(A.split('setup')[1].split(_B)[0]);modify(B+A,E)
	if os.path.exists(A):os.remove(A)
	shutil.copyfile(B+A.replace(_B,_C),A)
	if os.path.exists(B+A):os.remove(B+A)
	if os.path.exists(B+A.replace(_B,_C)):os.remove(B+A.replace(_B,_C))
def writedatatoarr(stream,value,size,location):
	'Write data to an array.';A=stream
	for B in range(size):A[location+B]=bytearray(value.to_bytes(size,_A))[B]
	return A
def int_to_float(val):'Convert a hex int to a float.';return struct.unpack('!f',bytes.fromhex(hex(val).split('0x')[1]))[0]
def float_to_hex(f):
	'Convert float to hex.'
	if f==0:return'0x00000000'
	return hex(struct.unpack('<I',struct.pack('<f',f))[0])
base_stream=0
def modify(file_name,map_index):
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';A5='change';t=file_name;s='use_byte_stream';l=False;d=b'';c=True;V='rz';U='rx';S='stream';R='scale';Q='ry';P='base_byte_stream';O='type';M='id';L='z';K='y';J='x';G=map_index;global base_stream
	with open(t,'r+b')as A6:
		F=A6.read();A7=int.from_bytes(F[:4],_A);C=4;e=[];m=[];f=[];g=[];W=[];X=544;u=l;v=l;w=l;x=l
		for A in range(A7):
			B=F[C:C+48];h=int.from_bytes(F[C+40:C+42],_A);H=int.from_bytes(F[C+42:C+44],_A)
			if h==684 and G!=42:
				if G==72 and not v and H==38:
					for i in range(2):y=50.167;g.append({P:B,O:[684,683][i],J:int(float_to_hex(120.997),16),K:[int(float_to_hex(y),16),int(float_to_hex(y-30),16)][i],L:int(float_to_hex(1182.974),16),U:0,Q:int(float_to_hex(75.146),16),V:0,M:[368,X][i],R:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][i]})
					X+=1;v=c
				base_stream=B;z=int.from_bytes(F[C+0:C+4],_A);n=int.from_bytes(F[C+4:C+8],_A);A8=int_to_float(n)-30;n=int(float_to_hex(A8),16);A0=int.from_bytes(F[C+8:C+12],_A);AQ=int.from_bytes(F[C+24:C+28],_A);Y=int.from_bytes(F[C+28:C+32],_A);AR=int.from_bytes(F[C+32:C+36],_A);H=int.from_bytes(F[C+42:C+44],_A)
				if G==7:
					if X==544:z=int(float_to_hex(805.6618),16);A0=int(float_to_hex(2226.797),16)
				g.append({P:B,O:683,J:z,K:n,L:A0,U:0,Q:Y,V:0,M:X,R:int(float_to_hex(0.35),16)});X+=1
			if G==34 and not u and H==6:u=c;g.append({P:B,O:132,J:int(float_to_hex(2457.471),16),K:int(float_to_hex(1280),16),L:int(float_to_hex(3458.604),16),U:0,Q:int(float_to_hex(166),16),V:0,M:256,R:int(float_to_hex(1.18),16)})
			if G==7 and H==26 or G==176 and H==57:
				h=206;E=d
				for A in range(41):E+=B[A].to_bytes(1,_A)
				E+=h.to_bytes(1,_A)
				for A in range(48-42):E+=B[A+42].to_bytes(1,_A)
				B=E
			if G==26 and H==36:
				E=d;N=[0,0,0];o=[1455.853,6.5,522.716];N[0]=int(float_to_hex(o[0]),16);N[1]=int(float_to_hex(o[1]),16);N[2]=int(float_to_hex(o[2]),16);Y=int(float_to_hex(0),16)
				for A in N:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=B[A+12].to_bytes(1,_A)
				E+=Y.to_bytes(4,_A)
				for A in range(48-32):E+=B[A+32].to_bytes(1,_A)
				B=E
			if G==26 and H>=103 and H<=118:
				E=d;A1=H-103;A9=A1%4;AA=int(A1/4);AB=2606.114;AC=1767.899;A2=37.7;N=[0,0,0];N[0]=int(float_to_hex(AB+A2*AA),16);N[1]=int(float_to_hex(1002),16);N[2]=int(float_to_hex(AC+A2*A9),16)
				for A in N:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=B[A+12].to_bytes(1,_A)
				E+=Y.to_bytes(4,_A)
				for A in range(48-32):E+=B[A+32].to_bytes(1,_A)
				B=E;Y=int(float_to_hex(180),16)
			if G==72:
				if H==87 or H==207:
					E=d;AD=176.505;AE=1089.408;E+=int(float_to_hex(AD),16).to_bytes(4,_A)
					for A in range(4):E+=B[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(AE),16).to_bytes(4,_A)
					for A in range(48-12):E+=B[A+12].to_bytes(1,_A)
					B=E
			if G==7 and H==201:
				E=d;p=int(float_to_hex(400),16)
				for A in range(4):E+=B[A].to_bytes(1,_A)
				E+=p.to_bytes(4,_A)
				for A in range(48-8):E+=B[A+8].to_bytes(1,_A)
				B=E
			Z={S:B,O:h};e.append(Z);C+=48
		AF=getMoveSignData(G,base_stream);j=generateVineSeries(G)
		for AG in AF:W.append(AG)
		AH=int.from_bytes(F[C:C+4],_A);C+=4
		for A in range(AH):B=F[C:C+36];Z={S:B};m.append(Z);C+=36
		AI=int.from_bytes(F[C:C+4],_A);C+=4
		for A in range(AI):
			B=F[C:C+56];q=int.from_bytes(F[C+52:C+54],_A)
			if G==26 and q==13:
				a=[]
				for I in range(56):a.append(B[I])
				B=a.copy();AJ=1237.001;p=175;AK=840.569;writedatatoarr(B,int(float_to_hex(AJ),16),4,0);writedatatoarr(B,int(float_to_hex(p),16),4,4);writedatatoarr(B,int(float_to_hex(AK),16),4,8)
			elif G==17 and not w:
				AL=5423.538;A3=160;r=104.5;AM=[[575.763,A3],[494.518,A3],[606.161,r],[534.567,r],[463.642,r]]
				for (AN,A4) in enumerate(AM):W.append({P:B,J:int(float_to_hex(A4[0]),16),K:int(float_to_hex(A4[1]),16),L:int(float_to_hex(AL),16),M:256+AN,O:70-16,U:0,Q:0,V:0,R:int(float_to_hex(0.35),16)})
				w=c
			elif G==86 and not x:W.append({P:B,J:int(float_to_hex(118.011),16),K:int(float_to_hex(20),16),L:int(float_to_hex(462.749),16),M:32,O:57-16,U:0,Q:1024,V:0,R:int(float_to_hex(1),16)});x=c
			if len(j['add'])>0:
				for b in j['add']:
					if q==b['id_base']:W.append({P:B,J:int(float_to_hex(b[J]),16),K:int(float_to_hex(b[K]),16),L:int(float_to_hex(b[L]),16),M:b[M],s:c})
			if len(j[A5])>0:
				for k in j[A5]:
					if q==k[M]:
						a=[]
						for I in range(56):a.append(B[I])
						B=a.copy();writedatatoarr(B,int(float_to_hex(k[J]),16),4,0);writedatatoarr(B,int(float_to_hex(k[K]),16),4,4);writedatatoarr(B,int(float_to_hex(k[L]),16),4,8)
			Z={S:B};f.append(Z);C+=56
		for A in W:
			D=[]
			for I in range(56):
				if s in A and A[s]and P in A:D.append(A[P][I])
				else:D.append(0)
			if J in A:writedatatoarr(D,A[J],4,0)
			if K in A:writedatatoarr(D,A[K],4,4)
			if L in A:writedatatoarr(D,A[L],4,8)
			if R in A:writedatatoarr(D,A[R],4,12)
			if Q in A:writedatatoarr(D,A[Q],2,48)
			if O in A:writedatatoarr(D,A[O],2,50)
			if M in A:writedatatoarr(D,A[M],2,52)
			f.append({S:D})
		for A in g:
			D=[]
			for I in range(16):D.append(0)
			AO=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in AO:D.append(I)
			for I in range(12):D.append(0)
			AP=[0,1,0,0]
			for I in AP:D.append(I)
			D=writedatatoarr(D,A[O],2,40);D=writedatatoarr(D,A[M],2,42);D=writedatatoarr(D,A[R],4,12);D=writedatatoarr(D,A[J],4,0);D=writedatatoarr(D,A[K],4,4);D=writedatatoarr(D,A[L],4,8);D=writedatatoarr(D,A[U],4,24);D=writedatatoarr(D,A[Q],4,28);D=writedatatoarr(D,A[V],4,32);e.append({S:D})
		with open(t.replace(_B,_C),'wb')as T:
			T.write(len(e).to_bytes(4,_A))
			for A in e:T.write(bytearray(A[S]))
			T.write(len(m).to_bytes(4,_A))
			for A in m:T.write(bytearray(A[S]))
			T.write(len(f).to_bytes(4,_A))
			for A in f:T.write(bytearray(A[S]))