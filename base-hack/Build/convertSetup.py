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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';x=False;o=file_name;n='use_byte_stream';m=True;f=b'';e='rz';d='rx';T='scale';S='ry';R='base_byte_stream';P='id';O='z';N='y';M='x';L='type';K='stream';G=map_index;global base_stream
	with open(o,'r+b')as y:
		F=y.read();z=int.from_bytes(F[:4],_A);B=4;Y=[];g=[];Z=[];a=[];h=[];U=544;p=x;q=x
		for A in range(z):
			D=F[B:B+48];b=int.from_bytes(F[B+40:B+42],_A);H=int.from_bytes(F[B+42:B+44],_A)
			if b==684 and G!=42:
				if G==72 and not q and H==38:
					for c in range(2):r=50.167;a.append({R:D,L:[684,683][c],M:int(float_to_hex(120.997),16),N:[int(float_to_hex(r),16),int(float_to_hex(r-30),16)][c],O:int(float_to_hex(1182.974),16),d:0,S:int(float_to_hex(75.146),16),e:0,P:[368,U][c],T:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][c]})
					U+=1;q=m
				base_stream=D;s=int.from_bytes(F[B+0:B+4],_A);i=int.from_bytes(F[B+4:B+8],_A);A0=int_to_float(i)-30;i=int(float_to_hex(A0),16);t=int.from_bytes(F[B+8:B+12],_A);AE=int.from_bytes(F[B+24:B+28],_A);V=int.from_bytes(F[B+28:B+32],_A);AF=int.from_bytes(F[B+32:B+36],_A);H=int.from_bytes(F[B+42:B+44],_A)
				if G==7:
					if U==544:s=int(float_to_hex(805.6618),16);t=int(float_to_hex(2226.797),16)
				a.append({R:D,L:683,M:s,N:i,O:t,d:0,S:V,e:0,P:U,T:int(float_to_hex(0.35),16)});U+=1
			if G==34 and not p and H==6:p=m;a.append({R:D,L:132,M:int(float_to_hex(2457.471),16),N:int(float_to_hex(1280),16),O:int(float_to_hex(3458.604),16),d:0,S:int(float_to_hex(166),16),e:0,P:256,T:int(float_to_hex(1.18),16)})
			if G==7 and H==26 or G==176 and H==57:
				b=206;E=f
				for A in range(41):E+=D[A].to_bytes(1,_A)
				E+=b.to_bytes(1,_A)
				for A in range(48-42):E+=D[A+42].to_bytes(1,_A)
				D=E
			if G==26 and H==36:
				E=f;J=[0,0,0];j=[1455.853,6.5,522.716];J[0]=int(float_to_hex(j[0]),16);J[1]=int(float_to_hex(j[1]),16);J[2]=int(float_to_hex(j[2]),16);V=int(float_to_hex(0),16)
				for A in J:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=V.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E
			if G==26 and H>=103 and H<=118:
				E=f;u=H-103;A1=u%4;A2=int(u/4);A3=2606.114;A4=1767.899;v=37.7;J=[0,0,0];J[0]=int(float_to_hex(A3+v*A2),16);J[1]=int(float_to_hex(1002),16);J[2]=int(float_to_hex(A4+v*A1),16)
				for A in J:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=V.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E;V=int(float_to_hex(180),16)
			if G==72:
				if H==87 or H==207:
					E=f;A5=176.505;A6=1089.408;E+=int(float_to_hex(A5),16).to_bytes(4,_A)
					for A in range(4):E+=D[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(A6),16).to_bytes(4,_A)
					for A in range(48-12):E+=D[A+12].to_bytes(1,_A)
					D=E
			W={K:D,L:b};Y.append(W);B+=48
		A7=getMoveSignData(G,base_stream)
		for A8 in A7:h.append(A8)
		A9=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(A9):D=F[B:B+36];W={K:D};g.append(W);B+=36
		AA=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(AA):
			D=F[B:B+56];w=int.from_bytes(F[B+52:B+54],_A)
			if G==26 and w==13:
				X=[]
				for I in range(56):X.append(D[I])
				D=X.copy();k=1237.001;AB=175;l=840.569;writedatatoarr(D,int(float_to_hex(k),16),4,0);writedatatoarr(D,int(float_to_hex(AB),16),4,4);writedatatoarr(D,int(float_to_hex(l),16),4,8)
			elif G==64 and w==4:
				h.append({R:D,M:int(float_to_hex(517.993),16),N:int(float_to_hex(1070.614),16),O:int(float_to_hex(510.374),16),P:255,n:m});X=[]
				for I in range(56):X.append(D[I])
				D=X.copy();k=410.614;l=512.886;writedatatoarr(D,int(float_to_hex(k),16),4,0);writedatatoarr(D,int(float_to_hex(l),16),4,8)
			W={K:D};Z.append(W);B+=56
		for A in h:
			C=[]
			for I in range(56):
				if n in A and A[n]and R in A:C.append(A[R][I])
				else:C.append(0)
			if M in A:writedatatoarr(C,A[M],4,0)
			if N in A:writedatatoarr(C,A[N],4,4)
			if O in A:writedatatoarr(C,A[O],4,8)
			if T in A:writedatatoarr(C,A[T],4,12)
			if S in A:writedatatoarr(C,A[S],2,48)
			if L in A:writedatatoarr(C,A[L],2,50)
			if P in A:writedatatoarr(C,A[P],2,52)
			Z.append({K:C})
		for A in a:
			C=[]
			for I in range(16):C.append(0)
			AC=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in AC:C.append(I)
			for I in range(12):C.append(0)
			AD=[0,1,0,0]
			for I in AD:C.append(I)
			C=writedatatoarr(C,A[L],2,40);C=writedatatoarr(C,A[P],2,42);C=writedatatoarr(C,A[T],4,12);C=writedatatoarr(C,A[M],4,0);C=writedatatoarr(C,A[N],4,4);C=writedatatoarr(C,A[O],4,8);C=writedatatoarr(C,A[d],4,24);C=writedatatoarr(C,A[S],4,28);C=writedatatoarr(C,A[e],4,32);Y.append({K:C})
		with open(o.replace(_B,_C),'wb')as Q:
			Q.write(len(Y).to_bytes(4,_A))
			for A in Y:Q.write(bytearray(A[K]))
			Q.write(len(g).to_bytes(4,_A))
			for A in g:Q.write(bytearray(A[K]))
			Q.write(len(Z).to_bytes(4,_A))
			for A in Z:Q.write(bytearray(A[K]))