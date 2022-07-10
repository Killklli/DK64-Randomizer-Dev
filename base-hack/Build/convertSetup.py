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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';l='base_byte_stream';f=file_name;e='rz';d='rx';W='scale';V='id';U='ry';T='z';S='y';R='x';M='type';I='stream';G=map_index;global base_stream
	with open(f,'r+b')as m:
		E=m.read();n=int.from_bytes(E[:4],_A);B=4;N=[];X=[];O=[];Y=[];g=[];Z=544;h=False
		for A in range(n):
			D=E[B:B+48];P=int.from_bytes(E[B+40:B+42],_A);K=int.from_bytes(E[B+42:B+44],_A)
			if P==684 and G!=42:
				base_stream=D;i=int.from_bytes(E[B+0:B+4],_A);a=int.from_bytes(E[B+4:B+8],_A);o=int_to_float(a)-30;a=int(float_to_hex(o),16);j=int.from_bytes(E[B+8:B+12],_A);y=int.from_bytes(E[B+24:B+28],_A);b=int.from_bytes(E[B+28:B+32],_A);z=int.from_bytes(E[B+32:B+36],_A);K=int.from_bytes(E[B+42:B+44],_A)
				if G==7:
					if Z==544:i=int(float_to_hex(805.6618),16);j=int(float_to_hex(2226.797),16)
				Y.append({l:D,M:683,R:i,S:a,T:j,d:0,U:b,e:0,V:Z,W:int(float_to_hex(0.35),16)});Z+=1
			if G==34 and not h and K==6:h=True;Y.append({l:D,M:132,R:int(float_to_hex(2457.471),16),S:int(float_to_hex(1280),16),T:int(float_to_hex(3458.604),16),d:0,U:int(float_to_hex(166),16),e:0,V:256,W:int(float_to_hex(1.18),16)})
			if G==7 and K==26 or G==176 and K==57:
				P=206;F=b''
				for A in range(41):F+=D[A].to_bytes(1,_A)
				F+=P.to_bytes(1,_A)
				for A in range(48-42):F+=D[A+42].to_bytes(1,_A)
				D=F
			if G==26 and K==36:
				F=b'';Q=[0,0,0];c=[1455.853,6.5,522.716];Q[0]=int(float_to_hex(c[0]),16);Q[1]=int(float_to_hex(c[1]),16);Q[2]=int(float_to_hex(c[2]),16);b=int(float_to_hex(0),16)
				for A in Q:F+=A.to_bytes(4,_A)
				for A in range(28-12):F+=D[A+12].to_bytes(1,_A)
				F+=b.to_bytes(4,_A)
				for A in range(48-32):F+=D[A+32].to_bytes(1,_A)
				D=F
			L={I:D,M:P};N.append(L);B+=48
		p=getMoveSignData(G,base_stream)
		for q in p:g.append(q)
		r=int.from_bytes(E[B:B+4],_A);B+=4
		for A in range(r):D=E[B:B+36];L={I:D};X.append(L);B+=36
		s=int.from_bytes(E[B:B+4],_A);B+=4
		for A in range(s):
			D=E[B:B+56];t=int.from_bytes(E[B+52:B+54],_A)
			if G==26 and t==13:
				k=[]
				for H in range(56):k.append(D[H])
				D=k.copy();u=1237.001;v=840.569;writedatatoarr(D,int(float_to_hex(u),16),4,0);writedatatoarr(D,int(float_to_hex(v),16),4,8)
			L={I:D};O.append(L);B+=56
		for A in g:
			C=[]
			for H in range(56):C.append(0)
			writedatatoarr(C,A[R],4,0);writedatatoarr(C,A[S],4,4);writedatatoarr(C,A[T],4,8);writedatatoarr(C,A[W],4,12);writedatatoarr(C,A[U],2,48);writedatatoarr(C,A[M],2,50);writedatatoarr(C,A[V],2,52);O.append({I:C})
		for A in Y:
			C=[]
			for H in range(16):C.append(0)
			w=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for H in w:C.append(H)
			for H in range(12):C.append(0)
			x=[0,1,0,0]
			for H in x:C.append(H)
			C=writedatatoarr(C,A[M],2,40);C=writedatatoarr(C,A[V],2,42);C=writedatatoarr(C,A[W],4,12);C=writedatatoarr(C,A[R],4,0);C=writedatatoarr(C,A[S],4,4);C=writedatatoarr(C,A[T],4,8);C=writedatatoarr(C,A[d],4,24);C=writedatatoarr(C,A[U],4,28);C=writedatatoarr(C,A[e],4,32);N.append({I:C})
		with open(f.replace(_B,_C),'wb')as J:
			J.write(len(N).to_bytes(4,_A))
			for A in N:J.write(bytearray(A[I]))
			J.write(len(X).to_bytes(4,_A))
			for A in X:J.write(bytearray(A[I]))
			J.write(len(O).to_bytes(4,_A))
			for A in O:J.write(bytearray(A[I]))