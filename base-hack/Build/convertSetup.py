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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';q=file_name;p='use_byte_stream';o=False;h=b'';g=True;Z='rz';Y='rx';S='scale';R='ry';Q='base_byte_stream';P='stream';O='id';N='z';M='y';L='x';K='type';G=map_index;global base_stream
	with open(q,'r+b')as A2:
		F=A2.read();A3=int.from_bytes(F[:4],_A);B=4;a=[];i=[];b=[];c=[];d=[];U=544;r=o;s=o;t=o
		for A in range(A3):
			D=F[B:B+48];e=int.from_bytes(F[B+40:B+42],_A);H=int.from_bytes(F[B+42:B+44],_A)
			if e==684 and G!=42:
				if G==72 and not s and H==38:
					for f in range(2):u=50.167;c.append({Q:D,K:[684,683][f],L:int(float_to_hex(120.997),16),M:[int(float_to_hex(u),16),int(float_to_hex(u-30),16)][f],N:int(float_to_hex(1182.974),16),Y:0,R:int(float_to_hex(75.146),16),Z:0,O:[368,U][f],S:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][f]})
					U+=1;s=g
				base_stream=D;v=int.from_bytes(F[B+0:B+4],_A);j=int.from_bytes(F[B+4:B+8],_A);A4=int_to_float(j)-30;j=int(float_to_hex(A4),16);w=int.from_bytes(F[B+8:B+12],_A);AL=int.from_bytes(F[B+24:B+28],_A);V=int.from_bytes(F[B+28:B+32],_A);AM=int.from_bytes(F[B+32:B+36],_A);H=int.from_bytes(F[B+42:B+44],_A)
				if G==7:
					if U==544:v=int(float_to_hex(805.6618),16);w=int(float_to_hex(2226.797),16)
				c.append({Q:D,K:683,L:v,M:j,N:w,Y:0,R:V,Z:0,O:U,S:int(float_to_hex(0.35),16)});U+=1
			if G==34 and not r and H==6:r=g;c.append({Q:D,K:132,L:int(float_to_hex(2457.471),16),M:int(float_to_hex(1280),16),N:int(float_to_hex(3458.604),16),Y:0,R:int(float_to_hex(166),16),Z:0,O:256,S:int(float_to_hex(1.18),16)})
			if G==7 and H==26 or G==176 and H==57:
				e=206;E=h
				for A in range(41):E+=D[A].to_bytes(1,_A)
				E+=e.to_bytes(1,_A)
				for A in range(48-42):E+=D[A+42].to_bytes(1,_A)
				D=E
			if G==26 and H==36:
				E=h;J=[0,0,0];k=[1455.853,6.5,522.716];J[0]=int(float_to_hex(k[0]),16);J[1]=int(float_to_hex(k[1]),16);J[2]=int(float_to_hex(k[2]),16);V=int(float_to_hex(0),16)
				for A in J:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=V.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E
			if G==26 and H>=103 and H<=118:
				E=h;x=H-103;A5=x%4;A6=int(x/4);A7=2606.114;A8=1767.899;y=37.7;J=[0,0,0];J[0]=int(float_to_hex(A7+y*A6),16);J[1]=int(float_to_hex(1002),16);J[2]=int(float_to_hex(A8+y*A5),16)
				for A in J:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=D[A+12].to_bytes(1,_A)
				E+=V.to_bytes(4,_A)
				for A in range(48-32):E+=D[A+32].to_bytes(1,_A)
				D=E;V=int(float_to_hex(180),16)
			if G==72:
				if H==87 or H==207:
					E=h;A9=176.505;AA=1089.408;E+=int(float_to_hex(A9),16).to_bytes(4,_A)
					for A in range(4):E+=D[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(AA),16).to_bytes(4,_A)
					for A in range(48-12):E+=D[A+12].to_bytes(1,_A)
					D=E
			W={P:D,K:e};a.append(W);B+=48
		AB=getMoveSignData(G,base_stream)
		for AC in AB:d.append(AC)
		AD=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(AD):D=F[B:B+36];W={P:D};i.append(W);B+=36
		AE=int.from_bytes(F[B:B+4],_A);B+=4
		for A in range(AE):
			D=F[B:B+56];z=int.from_bytes(F[B+52:B+54],_A)
			if G==26 and z==13:
				X=[]
				for I in range(56):X.append(D[I])
				D=X.copy();l=1237.001;AF=175;m=840.569;writedatatoarr(D,int(float_to_hex(l),16),4,0);writedatatoarr(D,int(float_to_hex(AF),16),4,4);writedatatoarr(D,int(float_to_hex(m),16),4,8)
			elif G==64 and z==4:
				d.append({Q:D,L:int(float_to_hex(517.993),16),M:int(float_to_hex(1070.614),16),N:int(float_to_hex(510.374),16),O:255,p:g});X=[]
				for I in range(56):X.append(D[I])
				D=X.copy();l=410.614;m=512.886;writedatatoarr(D,int(float_to_hex(l),16),4,0);writedatatoarr(D,int(float_to_hex(m),16),4,8)
			elif G==17 and not t:
				AG=5423.538;A0=160;n=104.5;AH=[[575.763,A0],[494.518,A0],[606.161,n],[534.567,n],[463.642,n]]
				for (AI,A1) in enumerate(AH):d.append({Q:D,L:int(float_to_hex(A1[0]),16),M:int(float_to_hex(A1[1]),16),N:int(float_to_hex(AG),16),O:256+AI,K:70-16,Y:0,R:0,Z:0,S:int(float_to_hex(0.35),16)})
				t=g
			W={P:D};b.append(W);B+=56
		for A in d:
			C=[]
			for I in range(56):
				if p in A and A[p]and Q in A:C.append(A[Q][I])
				else:C.append(0)
			if L in A:writedatatoarr(C,A[L],4,0)
			if M in A:writedatatoarr(C,A[M],4,4)
			if N in A:writedatatoarr(C,A[N],4,8)
			if S in A:writedatatoarr(C,A[S],4,12)
			if R in A:writedatatoarr(C,A[R],2,48)
			if K in A:writedatatoarr(C,A[K],2,50)
			if O in A:writedatatoarr(C,A[O],2,52)
			b.append({P:C})
		for A in c:
			C=[]
			for I in range(16):C.append(0)
			AJ=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in AJ:C.append(I)
			for I in range(12):C.append(0)
			AK=[0,1,0,0]
			for I in AK:C.append(I)
			C=writedatatoarr(C,A[K],2,40);C=writedatatoarr(C,A[O],2,42);C=writedatatoarr(C,A[S],4,12);C=writedatatoarr(C,A[L],4,0);C=writedatatoarr(C,A[M],4,4);C=writedatatoarr(C,A[N],4,8);C=writedatatoarr(C,A[Y],4,24);C=writedatatoarr(C,A[R],4,28);C=writedatatoarr(C,A[Z],4,32);a.append({P:C})
		with open(q.replace(_B,_C),'wb')as T:
			T.write(len(a).to_bytes(4,_A))
			for A in a:T.write(bytearray(A[P]))
			T.write(len(i).to_bytes(4,_A))
			for A in i:T.write(bytearray(A[P]))
			T.write(len(b).to_bytes(4,_A))
			for A in b:T.write(bytearray(A[P]))