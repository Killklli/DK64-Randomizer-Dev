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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';Y=file_name;X='scale';W='ry';V='z';U='y';T='x';O='type';I=map_index;F='stream';global base_stream
	with open(Y,'r+b')as d:
		D=d.read();e=int.from_bytes(D[:4],_A);A=4;K=[];P=[];L=[];Z=[];a=[];Q=544
		for C in range(e):
			E=D[A:A+48];M=int.from_bytes(D[A+40:A+42],_A);R=int.from_bytes(D[A+42:A+44],_A)
			if M==684 and I!=42:
				base_stream=E;b=int.from_bytes(D[A+0:A+4],_A);S=int.from_bytes(D[A+4:A+8],_A);f=int_to_float(S)-30;S=int(float_to_hex(f),16);c=int.from_bytes(D[A+8:A+12],_A);n=int.from_bytes(D[A+24:A+28],_A);g=int.from_bytes(D[A+28:A+32],_A);o=int.from_bytes(D[A+32:A+36],_A);R=int.from_bytes(D[A+42:A+44],_A)
				if I==7:
					if Q==544:b=int(float_to_hex(805.6618),16);c=int(float_to_hex(2226.797),16)
				Z.append({'base_byte_stream':E,O:683,T:b,U:S,V:c,'rx':0,W:g,'rz':0,'id':Q,X:int(float_to_hex(0.35),16)});Q+=1
			if I==7 and R==26 or I==176 and R==57:
				M=206;N=b''
				for C in range(41):N+=E[C].to_bytes(1,_A)
				N+=M.to_bytes(1,_A)
				for C in range(48-42):N+=E[C+42].to_bytes(1,_A)
				E=N
			J={F:E,O:M};K.append(J);A+=48
		h=getMoveSignData(I,base_stream)
		for i in h:a.append(i)
		j=int.from_bytes(D[A:A+4],_A);A+=4
		for C in range(j):E=D[A:A+36];J={F:E};P.append(J);A+=36
		k=int.from_bytes(D[A:A+4],_A);A+=4
		for C in range(k):E=D[A:A+56];J={F:E};L.append(J);A+=56
		for C in a:
			B=[]
			for G in range(56):B.append(0)
			writedatatoarr(B,C[T],4,0);writedatatoarr(B,C[U],4,4);writedatatoarr(B,C[V],4,8);writedatatoarr(B,C[X],4,12);writedatatoarr(B,C[W],2,48);writedatatoarr(B,C[O],2,50);L.append({F:B})
		for C in Z:
			B=[]
			for G in range(16):B.append(0)
			l=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for G in l:B.append(G)
			for G in range(12):B.append(0)
			m=[0,1,0,0]
			for G in m:B.append(G)
			B=writedatatoarr(B,C[O],2,40);B=writedatatoarr(B,C['id'],2,42);B=writedatatoarr(B,C[X],4,12);B=writedatatoarr(B,C[T],4,0);B=writedatatoarr(B,C[U],4,4);B=writedatatoarr(B,C[V],4,8);B=writedatatoarr(B,C['rx'],4,24);B=writedatatoarr(B,C[W],4,28);B=writedatatoarr(B,C['rz'],4,32);K.append({F:B})
		with open(Y.replace(_B,_C),'wb')as H:
			H.write(len(K).to_bytes(4,_A))
			for C in K:H.write(bytearray(C[F]))
			H.write(len(P).to_bytes(4,_A))
			for C in P:H.write(bytearray(C[F]))
			H.write(len(L).to_bytes(4,_A))
			for C in L:H.write(bytearray(C[F]))