'Convert file setup.'
_C='_.bin'
_B='.bin'
_A='big'
import os,shutil,struct
from getMoveSignLocations import getMoveSignData
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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';s=file_name;k=False;d='use_byte_stream';c=b'';X='rz';W='rx';U=True;S='stream';R='scale';Q='ry';P='type';N='base_byte_stream';M='id';L='z';K='y';J='x';F=map_index;global base_stream
	with open(s,'r+b')as A4:
		G=A4.read();A5=int.from_bytes(G[:4],_A);C=4;e=[];l=[];f=[];g=[];T=[];Y=544;t=k;u=k;v=k;w=k
		for A in range(A5):
			B=G[C:C+48];h=int.from_bytes(G[C+40:C+42],_A);H=int.from_bytes(G[C+42:C+44],_A)
			if h==684 and F!=42:
				if F==72 and not u and H==38:
					for i in range(2):x=50.167;g.append({N:B,P:[684,683][i],J:int(float_to_hex(120.997),16),K:[int(float_to_hex(x),16),int(float_to_hex(x-30),16)][i],L:int(float_to_hex(1182.974),16),W:0,Q:int(float_to_hex(75.146),16),X:0,M:[368,Y][i],R:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][i]})
					Y+=1;u=U
				base_stream=B;y=int.from_bytes(G[C+0:C+4],_A);m=int.from_bytes(G[C+4:C+8],_A);A6=int_to_float(m)-30;m=int(float_to_hex(A6),16);z=int.from_bytes(G[C+8:C+12],_A);AM=int.from_bytes(G[C+24:C+28],_A);Z=int.from_bytes(G[C+28:C+32],_A);AN=int.from_bytes(G[C+32:C+36],_A);H=int.from_bytes(G[C+42:C+44],_A)
				if F==7:
					if Y==544:y=int(float_to_hex(805.6618),16);z=int(float_to_hex(2226.797),16)
				g.append({N:B,P:683,J:y,K:m,L:z,W:0,Q:Z,X:0,M:Y,R:int(float_to_hex(0.35),16)});Y+=1
			if F==34 and not t and H==6:t=U;g.append({N:B,P:132,J:int(float_to_hex(2457.471),16),K:int(float_to_hex(1280),16),L:int(float_to_hex(3458.604),16),W:0,Q:int(float_to_hex(166),16),X:0,M:256,R:int(float_to_hex(1.18),16)})
			if F==7 and H==26 or F==176 and H==57:
				h=206;E=c
				for A in range(41):E+=B[A].to_bytes(1,_A)
				E+=h.to_bytes(1,_A)
				for A in range(48-42):E+=B[A+42].to_bytes(1,_A)
				B=E
			if F==26 and H==36:
				E=c;O=[0,0,0];n=[1455.853,6.5,522.716];O[0]=int(float_to_hex(n[0]),16);O[1]=int(float_to_hex(n[1]),16);O[2]=int(float_to_hex(n[2]),16);Z=int(float_to_hex(0),16)
				for A in O:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=B[A+12].to_bytes(1,_A)
				E+=Z.to_bytes(4,_A)
				for A in range(48-32):E+=B[A+32].to_bytes(1,_A)
				B=E
			if F==26 and H>=103 and H<=118:
				E=c;A0=H-103;A7=A0%4;A8=int(A0/4);A9=2606.114;AA=1767.899;A1=37.7;O=[0,0,0];O[0]=int(float_to_hex(A9+A1*A8),16);O[1]=int(float_to_hex(1002),16);O[2]=int(float_to_hex(AA+A1*A7),16)
				for A in O:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=B[A+12].to_bytes(1,_A)
				E+=Z.to_bytes(4,_A)
				for A in range(48-32):E+=B[A+32].to_bytes(1,_A)
				B=E;Z=int(float_to_hex(180),16)
			if F==72:
				if H==87 or H==207:
					E=c;AB=176.505;AC=1089.408;E+=int(float_to_hex(AB),16).to_bytes(4,_A)
					for A in range(4):E+=B[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(AC),16).to_bytes(4,_A)
					for A in range(48-12):E+=B[A+12].to_bytes(1,_A)
					B=E
			if F==7 and H==201:
				E=c;o=int(float_to_hex(400),16)
				for A in range(4):E+=B[A].to_bytes(1,_A)
				E+=o.to_bytes(4,_A)
				for A in range(48-8):E+=B[A+8].to_bytes(1,_A)
				B=E
			a={S:B,P:h};e.append(a);C+=48
		AD=getMoveSignData(F,base_stream)
		for AE in AD:T.append(AE)
		AF=int.from_bytes(G[C:C+4],_A);C+=4
		for A in range(AF):B=G[C:C+36];a={S:B};l.append(a);C+=36
		AG=int.from_bytes(G[C:C+4],_A);C+=4
		for A in range(AG):
			B=G[C:C+56];j=int.from_bytes(G[C+52:C+54],_A)
			if F==26 and j==13:
				b=[]
				for I in range(56):b.append(B[I])
				B=b.copy();p=1237.001;o=175;q=840.569;writedatatoarr(B,int(float_to_hex(p),16),4,0);writedatatoarr(B,int(float_to_hex(o),16),4,4);writedatatoarr(B,int(float_to_hex(q),16),4,8)
			elif F==64 and j==4:
				T.append({N:B,J:int(float_to_hex(517.993),16),K:int(float_to_hex(1070.614),16),L:int(float_to_hex(510.374),16),M:255,d:U});b=[]
				for I in range(56):b.append(B[I])
				B=b.copy();p=410.614;q=512.886;writedatatoarr(B,int(float_to_hex(p),16),4,0);writedatatoarr(B,int(float_to_hex(q),16),4,8)
			elif F==34 and j==4:T.append({N:B,J:int(float_to_hex(3178.968),16),K:int(float_to_hex(992.493),16),L:int(float_to_hex(1152.631),16),M:255,d:U})
			elif F==7 and j==26:T.append({N:B,J:int(float_to_hex(802.113),16),K:int(float_to_hex(632.5),16),L:int(float_to_hex(2258.593),16),M:255,d:U})
			elif F==17 and not v:
				AH=5423.538;A2=160;r=104.5;AI=[[575.763,A2],[494.518,A2],[606.161,r],[534.567,r],[463.642,r]]
				for (AJ,A3) in enumerate(AI):T.append({N:B,J:int(float_to_hex(A3[0]),16),K:int(float_to_hex(A3[1]),16),L:int(float_to_hex(AH),16),M:256+AJ,P:70-16,W:0,Q:0,X:0,R:int(float_to_hex(0.35),16)})
				v=U
			elif F==86 and not w:T.append({N:B,J:int(float_to_hex(118.011),16),K:int(float_to_hex(20),16),L:int(float_to_hex(462.749),16),M:32,P:57-16,W:0,Q:1024,X:0,R:int(float_to_hex(1),16)});w=U
			a={S:B};f.append(a);C+=56
		for A in T:
			D=[]
			for I in range(56):
				if d in A and A[d]and N in A:D.append(A[N][I])
				else:D.append(0)
			if J in A:writedatatoarr(D,A[J],4,0)
			if K in A:writedatatoarr(D,A[K],4,4)
			if L in A:writedatatoarr(D,A[L],4,8)
			if R in A:writedatatoarr(D,A[R],4,12)
			if Q in A:writedatatoarr(D,A[Q],2,48)
			if P in A:writedatatoarr(D,A[P],2,50)
			if M in A:writedatatoarr(D,A[M],2,52)
			f.append({S:D})
		for A in g:
			D=[]
			for I in range(16):D.append(0)
			AK=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in AK:D.append(I)
			for I in range(12):D.append(0)
			AL=[0,1,0,0]
			for I in AL:D.append(I)
			D=writedatatoarr(D,A[P],2,40);D=writedatatoarr(D,A[M],2,42);D=writedatatoarr(D,A[R],4,12);D=writedatatoarr(D,A[J],4,0);D=writedatatoarr(D,A[K],4,4);D=writedatatoarr(D,A[L],4,8);D=writedatatoarr(D,A[W],4,24);D=writedatatoarr(D,A[Q],4,28);D=writedatatoarr(D,A[X],4,32);e.append({S:D})
		with open(s.replace(_B,_C),'wb')as V:
			V.write(len(e).to_bytes(4,_A))
			for A in e:V.write(bytearray(A[S]))
			V.write(len(l).to_bytes(4,_A))
			for A in l:V.write(bytearray(A[S]))
			V.write(len(f).to_bytes(4,_A))
			for A in f:V.write(bytearray(A[S]))