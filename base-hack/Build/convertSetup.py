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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';q=file_name;p='use_byte_stream';i=b'';h=False;b=True;V='rz';U='rx';S='stream';R='scale';Q='ry';P='base_byte_stream';O='id';N='z';M='y';L='x';K='type';G=map_index;global base_stream
	with open(q,'r+b')as A3:
		F=A3.read();A4=int.from_bytes(F[:4],_A);B=4;c=[];j=[];d=[];e=[];W=[];X=544;r=h;s=h;t=h;u=h
		for A in range(A4):
			D=F[B:B+48];f=int.from_bytes(F[B+40:B+42],_A);H=int.from_bytes(F[B+42:B+44],_A)
			if f==684 and G!=42:
				if G==72 and not s and H==38:
					for g in range(2):v=50.167;e.append({P:D,K:[684,683][g],L:int(float_to_hex(120.997),16),M:[int(float_to_hex(v),16),int(float_to_hex(v-30),16)][g],N:int(float_to_hex(1182.974),16),U:0,Q:int(float_to_hex(75.146),16),V:0,O:[368,X][g],R:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][g]})
					X+=1;s=b
				base_stream=D;w=int.from_bytes(F[B+0:B+4],_A);k=int.from_bytes(F[B+4:B+8],_A);A5=int_to_float(k)-30;k=int(float_to_hex(A5),16);x=int.from_bytes(F[B+8:B+12],_A);AM=int.from_bytes(F[B+24:B+28],_A);Y=int.from_bytes(F[B+28:B+32],_A);AN=int.from_bytes(F[B+32:B+36],_A);H=int.from_bytes(F[B+42:B+44],_A)
				if G==7:
					if X==544:w=int(float_to_hex(805.6618),16);x=int(float_to_hex(2226.797),16)
				e.append({P:D,K:683,L:w,M:k,N:x,U:0,Q:Y,V:0,O:X,R:int(float_to_hex(0.35),16)});X+=1
			if G==34 and not r and H==6:r=b;e.append({P:D,K:132,L:int(float_to_hex(2457.471),16),M:int(float_to_hex(1280),16),N:int(float_to_hex(3458.604),16),U:0,Q:int(float_to_hex(166),16),V:0,O:256,R:int(float_to_hex(1.18),16)})
			if G==7 and H==26 or G==176 and H==57:
				f=206;E=i
				for A in range(41):E+=D[A].to_bytes(1,_A)
				E+=f.to_bytes(1,_A)
				for A in range(48-42):E+=D[A+42].to_bytes(1,_A)
				D=E
			if G==26 and H==36:
				E=i;J=[0,0,0];l=[1455.853,6.5,522.716];J[0]=int(float_to_hex(l[0]),16);J[1]=int(float_to_hex(l[1]),16);J[2]=int(float_to_hex(l[2]),16);Y=int(float_to_hex(0),16)
				for A in J:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=Y.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E
			if G==26 and H>=103 and H<=118:
				E=i;y=H-103;A6=y%4;A7=int(y/4);A8=2606.114;A9=1767.899;z=37.7;J=[0,0,0];J[0]=int(float_to_hex(A8+z*A7),16);J[1]=int(float_to_hex(1002),16);J[2]=int(float_to_hex(A9+z*A6),16)
				for A in J:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=Y.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E;Y=int(float_to_hex(180),16)
			if G==72:
				if H==87 or H==207:
					E=i;AA=176.505;AB=1089.408;E+=int(float_to_hex(AA),16).to_bytes(4,_A)
					for A in range(4):E+=D[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(AB),16).to_bytes(4,_A)
					for A in range(48-12):E+=D[A+12].to_bytes(1,_A)
					D=E
			Z={S:D,K:f};c.append(Z);B+=48
		AC=getMoveSignData(G,base_stream)
		for AD in AC:W.append(AD)
		AE=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(AE):D=F[B:B+36];Z={S:D};j.append(Z);B+=36
		AF=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(AF):
			D=F[B:B+56];A0=int.from_bytes(F[B+52:B+54],_A)
			if G==26 and A0==13:
				a=[]
				for I in range(56):a.append(D[I])
				D=a.copy();m=1237.001;AG=175;n=840.569;writedatatoarr(D,int(float_to_hex(m),16),4,0);writedatatoarr(D,int(float_to_hex(AG),16),4,4);writedatatoarr(D,int(float_to_hex(n),16),4,8)
			elif G==64 and A0==4:
				W.append({P:D,L:int(float_to_hex(517.993),16),M:int(float_to_hex(1070.614),16),N:int(float_to_hex(510.374),16),O:255,p:b});a=[]
				for I in range(56):a.append(D[I])
				D=a.copy();m=410.614;n=512.886;writedatatoarr(D,int(float_to_hex(m),16),4,0);writedatatoarr(D,int(float_to_hex(n),16),4,8)
			elif G==17 and not t:
				AH=5423.538;A1=160;o=104.5;AI=[[575.763,A1],[494.518,A1],[606.161,o],[534.567,o],[463.642,o]]
				for (AJ,A2) in enumerate(AI):W.append({P:D,L:int(float_to_hex(A2[0]),16),M:int(float_to_hex(A2[1]),16),N:int(float_to_hex(AH),16),O:256+AJ,K:70-16,U:0,Q:0,V:0,R:int(float_to_hex(0.35),16)})
				t=b
			elif G==86 and not u:W.append({P:D,L:int(float_to_hex(118.011),16),M:int(float_to_hex(20),16),N:int(float_to_hex(462.749),16),O:32,K:57-16,U:0,Q:1024,V:0,R:int(float_to_hex(1),16)});u=b
			Z={S:D};d.append(Z);B+=56
		for A in W:
			C=[]
			for I in range(56):
				if p in A and A[p]and P in A:C.append(A[P][I])
				else:C.append(0)
			if L in A:writedatatoarr(C,A[L],4,0)
			if M in A:writedatatoarr(C,A[M],4,4)
			if N in A:writedatatoarr(C,A[N],4,8)
			if R in A:writedatatoarr(C,A[R],4,12)
			if Q in A:writedatatoarr(C,A[Q],2,48)
			if K in A:writedatatoarr(C,A[K],2,50)
			if O in A:writedatatoarr(C,A[O],2,52)
			d.append({S:C})
		for A in e:
			C=[]
			for I in range(16):C.append(0)
			AK=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in AK:C.append(I)
			for I in range(12):C.append(0)
			AL=[0,1,0,0]
			for I in AL:C.append(I)
			C=writedatatoarr(C,A[K],2,40);C=writedatatoarr(C,A[O],2,42);C=writedatatoarr(C,A[R],4,12);C=writedatatoarr(C,A[L],4,0);C=writedatatoarr(C,A[M],4,4);C=writedatatoarr(C,A[N],4,8);C=writedatatoarr(C,A[U],4,24);C=writedatatoarr(C,A[Q],4,28);C=writedatatoarr(C,A[V],4,32);c.append({S:C})
		with open(q.replace(_B,_C),'wb')as T:
			T.write(len(c).to_bytes(4,_A))
			for A in c:T.write(bytearray(A[S]))
			T.write(len(j).to_bytes(4,_A))
			for A in j:T.write(bytearray(A[S]))
			T.write(len(d).to_bytes(4,_A))
			for A in d:T.write(bytearray(A[S]))