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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';s=False;i=file_name;h='base_byte_stream';d=b'';c='rz';b='rx';V='scale';U='id';T='ry';S='z';R='y';Q='x';M='type';K='stream';G=map_index;global base_stream
	with open(i,'r+b')as t:
		F=t.read();u=int.from_bytes(F[:4],_A);B=4;W=[];e=[];X=[];Y=[];j=[];N=544;k=s;l=s
		for A in range(u):
			D=F[B:B+48];Z=int.from_bytes(F[B+40:B+42],_A);H=int.from_bytes(F[B+42:B+44],_A)
			if Z==684 and G!=42:
				if G==72 and not l and H==38:
					for a in range(2):m=50.167;Y.append({h:D,M:[684,683][a],Q:int(float_to_hex(120.997),16),R:[int(float_to_hex(m),16),int(float_to_hex(m-30),16)][a],S:int(float_to_hex(1182.974),16),b:0,T:int(float_to_hex(75.146),16),c:0,U:[368,N][a],V:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][a]})
					N+=1;l=True
				base_stream=D;n=int.from_bytes(F[B+0:B+4],_A);f=int.from_bytes(F[B+4:B+8],_A);v=int_to_float(f)-30;f=int(float_to_hex(v),16);o=int.from_bytes(F[B+8:B+12],_A);AB=int.from_bytes(F[B+24:B+28],_A);O=int.from_bytes(F[B+28:B+32],_A);AC=int.from_bytes(F[B+32:B+36],_A);H=int.from_bytes(F[B+42:B+44],_A)
				if G==7:
					if N==544:n=int(float_to_hex(805.6618),16);o=int(float_to_hex(2226.797),16)
				Y.append({h:D,M:683,Q:n,R:f,S:o,b:0,T:O,c:0,U:N,V:int(float_to_hex(0.35),16)});N+=1
			if G==34 and not k and H==6:k=True;Y.append({h:D,M:132,Q:int(float_to_hex(2457.471),16),R:int(float_to_hex(1280),16),S:int(float_to_hex(3458.604),16),b:0,T:int(float_to_hex(166),16),c:0,U:256,V:int(float_to_hex(1.18),16)})
			if G==7 and H==26 or G==176 and H==57:
				Z=206;E=d
				for A in range(41):E+=D[A].to_bytes(1,_A)
				E+=Z.to_bytes(1,_A)
				for A in range(48-42):E+=D[A+42].to_bytes(1,_A)
				D=E
			if G==26 and H==36:
				E=d;I=[0,0,0];g=[1455.853,6.5,522.716];I[0]=int(float_to_hex(g[0]),16);I[1]=int(float_to_hex(g[1]),16);I[2]=int(float_to_hex(g[2]),16);O=int(float_to_hex(0),16)
				for A in I:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=O.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E
			if G==26 and H>=103 and H<=118:
				E=d;p=H-103;w=p%4;x=int(p/4);y=2606.114;z=1767.899;q=37.7;I=[0,0,0];I[0]=int(float_to_hex(y+q*x),16);I[1]=int(float_to_hex(1002),16);I[2]=int(float_to_hex(z+q*w),16)
				for A in I:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=O.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E;O=int(float_to_hex(180),16)
			if G==72:
				if H==87 or H==207:
					E=d;A0=176.505;A1=1089.408;E+=int(float_to_hex(A0),16).to_bytes(4,_A)
					for A in range(4):E+=D[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(A1),16).to_bytes(4,_A)
					for A in range(48-12):E+=D[A+12].to_bytes(1,_A)
					D=E
			P={K:D,M:Z};W.append(P);B+=48
		A2=getMoveSignData(G,base_stream)
		for A3 in A2:j.append(A3)
		A4=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(A4):D=F[B:B+36];P={K:D};e.append(P);B+=36
		A5=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(A5):
			D=F[B:B+56];A6=int.from_bytes(F[B+52:B+54],_A)
			if G==26 and A6==13:
				r=[]
				for J in range(56):r.append(D[J])
				D=r.copy();A7=1237.001;A8=840.569;writedatatoarr(D,int(float_to_hex(A7),16),4,0);writedatatoarr(D,int(float_to_hex(A8),16),4,8)
			P={K:D};X.append(P);B+=56
		for A in j:
			C=[]
			for J in range(56):C.append(0)
			writedatatoarr(C,A[Q],4,0);writedatatoarr(C,A[R],4,4);writedatatoarr(C,A[S],4,8);writedatatoarr(C,A[V],4,12);writedatatoarr(C,A[T],2,48);writedatatoarr(C,A[M],2,50);writedatatoarr(C,A[U],2,52);X.append({K:C})
		for A in Y:
			C=[]
			for J in range(16):C.append(0)
			A9=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for J in A9:C.append(J)
			for J in range(12):C.append(0)
			AA=[0,1,0,0]
			for J in AA:C.append(J)
			C=writedatatoarr(C,A[M],2,40);C=writedatatoarr(C,A[U],2,42);C=writedatatoarr(C,A[V],4,12);C=writedatatoarr(C,A[Q],4,0);C=writedatatoarr(C,A[R],4,4);C=writedatatoarr(C,A[S],4,8);C=writedatatoarr(C,A[b],4,24);C=writedatatoarr(C,A[T],4,28);C=writedatatoarr(C,A[c],4,32);W.append({K:C})
		with open(i.replace(_B,_C),'wb')as L:
			L.write(len(W).to_bytes(4,_A))
			for A in W:L.write(bytearray(A[K]))
			L.write(len(e).to_bytes(4,_A))
			for A in e:L.write(bytearray(A[K]))
			L.write(len(X).to_bytes(4,_A))
			for A in X:L.write(bytearray(A[K]))