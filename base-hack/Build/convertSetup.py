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
def float_to_hex(f):'Convert float to hex.';return hex(struct.unpack('<I',struct.pack('<f',f))[0])
base_stream=0
def modify(file_name,map_index):
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';c=file_name;b='scale';a='id';Z='ry';Y='z';X='y';W='x';Q='type';H=map_index;G='stream';global base_stream
	with open(c,'r+b')as h:
		D=h.read();i=int.from_bytes(D[:4],_A);B=4;L=[];R=[];M=[];d=[];e=[];S=544
		for A in range(i):
			E=D[B:B+48];N=int.from_bytes(D[B+40:B+42],_A);O=int.from_bytes(D[B+42:B+44],_A)
			if N==684 and H!=42:
				base_stream=E;f=int.from_bytes(D[B+0:B+4],_A);T=int.from_bytes(D[B+4:B+8],_A);j=int_to_float(T)-30;T=int(float_to_hex(j),16);g=int.from_bytes(D[B+8:B+12],_A);q=int.from_bytes(D[B+24:B+28],_A);U=int.from_bytes(D[B+28:B+32],_A);r=int.from_bytes(D[B+32:B+36],_A);O=int.from_bytes(D[B+42:B+44],_A)
				if H==7:
					if S==544:f=int(float_to_hex(805.6618),16);g=int(float_to_hex(2226.797),16)
				d.append({'base_byte_stream':E,Q:683,W:f,X:T,Y:g,'rx':0,Z:U,'rz':0,a:S,b:int(float_to_hex(0.35),16)});S+=1
			if H==7 and O==26 or H==176 and O==57:
				N=206;F=b''
				for A in range(41):F+=E[A].to_bytes(1,_A)
				F+=N.to_bytes(1,_A)
				for A in range(48-42):F+=E[A+42].to_bytes(1,_A)
				E=F
			if H==26 and O==36:
				F=b'';P=[0,0,0];V=[1455.853,6.5,522.716];P[0]=int(float_to_hex(V[0]),16);P[1]=int(float_to_hex(V[1]),16);P[2]=int(float_to_hex(V[2]),16);U=int(float_to_hex(0),16)
				for A in P:F+=A.to_bytes(4,_A)
				for A in range(28-12):F+=E[A+12].to_bytes(1,_A)
				F+=U.to_bytes(4,_A)
				for A in range(48-32):F+=E[A+32].to_bytes(1,_A)
				E=F
			K={G:E,Q:N};L.append(K);B+=48
		k=getMoveSignData(H,base_stream)
		for l in k:e.append(l)
		m=int.from_bytes(D[B:B+4],_A);B+=4
		for A in range(m):E=D[B:B+36];K={G:E};R.append(K);B+=36
		n=int.from_bytes(D[B:B+4],_A);B+=4
		for A in range(n):E=D[B:B+56];K={G:E};M.append(K);B+=56
		for A in e:
			C=[]
			for I in range(56):C.append(0)
			writedatatoarr(C,A[W],4,0);writedatatoarr(C,A[X],4,4);writedatatoarr(C,A[Y],4,8);writedatatoarr(C,A[b],4,12);writedatatoarr(C,A[Z],2,48);writedatatoarr(C,A[Q],2,50);writedatatoarr(C,A[a],2,52);M.append({G:C})
		for A in d:
			C=[]
			for I in range(16):C.append(0)
			o=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in o:C.append(I)
			for I in range(12):C.append(0)
			p=[0,1,0,0]
			for I in p:C.append(I)
			C=writedatatoarr(C,A[Q],2,40);C=writedatatoarr(C,A[a],2,42);C=writedatatoarr(C,A[b],4,12);C=writedatatoarr(C,A[W],4,0);C=writedatatoarr(C,A[X],4,4);C=writedatatoarr(C,A[Y],4,8);C=writedatatoarr(C,A['rx'],4,24);C=writedatatoarr(C,A[Z],4,28);C=writedatatoarr(C,A['rz'],4,32);L.append({G:C})
		with open(c.replace(_B,_C),'wb')as J:
			J.write(len(L).to_bytes(4,_A))
			for A in L:J.write(bytearray(A[G]))
			J.write(len(R).to_bytes(4,_A))
			for A in R:J.write(bytearray(A[G]))
			J.write(len(M).to_bytes(4,_A))
			for A in M:J.write(bytearray(A[G]))