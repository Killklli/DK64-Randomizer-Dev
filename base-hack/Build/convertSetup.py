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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';AC='change';x=file_name;w='use_byte_stream';o=False;g=True;Z='rz';Y='rx';V=b'';T='stream';S='scale';R='ry';Q='base_byte_stream';P='type';N='id';M='z';L='y';K='x';F=map_index;global base_stream
	with open(x,'r+b')as AD:
		H=AD.read();AE=int.from_bytes(H[:4],_A);D=4;h=[];p=[];i=[];j=[];a=[];b=544;y=o;z=o;A0=o;A1=o
		for A in range(AE):
			B=H[D:D+48];k=int.from_bytes(H[D+40:D+42],_A);G=int.from_bytes(H[D+42:D+44],_A)
			if k==684 and F!=42:
				if F==72 and not z and G==38:
					for l in range(2):A2=50.167;j.append({Q:B,P:[684,683][l],K:int(float_to_hex(120.997),16),L:[int(float_to_hex(A2),16),int(float_to_hex(A2-30),16)][l],M:int(float_to_hex(1182.974),16),Y:0,R:int(float_to_hex(75.146),16),Z:0,N:[368,b][l],S:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][l]})
					b+=1;z=g
				base_stream=B;A3=int.from_bytes(H[D+0:D+4],_A);q=int.from_bytes(H[D+4:D+8],_A);AF=int_to_float(q)-30;q=int(float_to_hex(AF),16);A4=int.from_bytes(H[D+8:D+12],_A);AX=int.from_bytes(H[D+24:D+28],_A);c=int.from_bytes(H[D+28:D+32],_A);AY=int.from_bytes(H[D+32:D+36],_A);G=int.from_bytes(H[D+42:D+44],_A)
				if F==7 and b==544:A3=int(float_to_hex(805.6618),16);A4=int(float_to_hex(2226.797),16)
				j.append({Q:B,P:683,K:A3,L:q,M:A4,Y:0,R:c,Z:0,N:b,S:int(float_to_hex(0.35),16)});b+=1
			if F==34 and not y and G==6:y=g;j.append({Q:B,P:132,K:int(float_to_hex(2457.471),16),L:int(float_to_hex(1280),16),M:int(float_to_hex(3458.604),16),Y:0,R:int(float_to_hex(166),16),Z:0,N:256,S:int(float_to_hex(1.18),16)})
			if F==7 and G==26 or F==176 and G==57:
				k=206;C=V
				for A in range(41):C+=B[A].to_bytes(1,_A)
				C+=k.to_bytes(1,_A)
				for A in range(48-42):C+=B[A+42].to_bytes(1,_A)
				B=C
			elif F==26 and G==318 or F==5 and G==2:
				C=V;AG=int(float_to_hex(0.2),16)
				for A in range(12):C+=B[A].to_bytes(1,_A)
				C+=AG.to_bytes(4,_A)
				for A in range(48-16):C+=B[A+16].to_bytes(1,_A)
				B=C
			if F==26 and G==36:
				C=V;O=[0,0,0];r=[1455.853,6.5,522.716];O[0]=int(float_to_hex(r[0]),16);O[1]=int(float_to_hex(r[1]),16);O[2]=int(float_to_hex(r[2]),16);c=int(float_to_hex(0),16)
				for A in O:C+=A.to_bytes(4,_A)
				for A in range(28-12):C+=B[A+12].to_bytes(1,_A)
				C+=c.to_bytes(4,_A)
				for A in range(48-32):C+=B[A+32].to_bytes(1,_A)
				B=C
			if F==26 and G>=103 and G<=118:
				C=V;A5=G-103;AH=A5%4;AI=int(A5/4);AJ=2606.114;AK=1767.899;A6=37.7;O=[0,0,0];O[0]=int(float_to_hex(AJ+A6*AI),16);O[1]=int(float_to_hex(1002),16);O[2]=int(float_to_hex(AK+A6*AH),16)
				for A in O:C+=A.to_bytes(4,_A)
				for A in range(28-12):C+=B[A+12].to_bytes(1,_A)
				C+=c.to_bytes(4,_A)
				for A in range(48-32):C+=B[A+32].to_bytes(1,_A)
				B=C;c=int(float_to_hex(180),16)
			if F==72 and G in(87,207):
				C=V;AL=176.505;AM=1089.408;C+=int(float_to_hex(AL),16).to_bytes(4,_A)
				for A in range(4):C+=B[A+4].to_bytes(1,_A)
				C+=int(float_to_hex(AM),16).to_bytes(4,_A)
				for A in range(48-12):C+=B[A+12].to_bytes(1,_A)
				B=C
			if F==205:
				A7=14,15,16,17;AN=13,19,20,18;A8=(780,419.629),(1135.232,780),(780,1116.334),(438.904,780);A9=(778.365,396.901),(1158.427,778.632),(780.283,1138.851),(416.092,778.456)
				if G>=13 and G<=20:
					A=0;s=0
					if G in A7:d=A7.index(G);A=A8[d][0];s=A8[d][1]
					else:d=AN.index(G);A=A9[d][0];s=A9[d][1]
					C=V;C+=int(float_to_hex(A),16).to_bytes(4,_A)
					for A in range(4):C+=B[A+4].to_bytes(1,_A)
					C+=int(float_to_hex(s),16).to_bytes(4,_A)
					for A in range(48-12):C+=B[A+12].to_bytes(1,_A)
					B=C
			if F==7 and G==201:
				C=V;U=int(float_to_hex(400),16)
				for A in range(4):C+=B[A].to_bytes(1,_A)
				C+=U.to_bytes(4,_A)
				for A in range(48-8):C+=B[A+8].to_bytes(1,_A)
				B=C
			e={T:B,P:k};h.append(e);D+=48
		AO=getMoveSignData(F,base_stream);m=generateVineSeries(F)
		for AP in AO:a.append(AP)
		AQ=int.from_bytes(H[D:D+4],_A);D+=4
		for A in range(AQ):B=H[D:D+36];e={T:B};p.append(e);D+=36
		AR=int.from_bytes(H[D:D+4],_A);D+=4
		for A in range(AR):
			B=H[D:D+56];W=int.from_bytes(H[D+52:D+54],_A)
			if F==26 and W==13:
				J=[]
				for I in range(56):J.append(B[I])
				B=J.copy();t=1237.001;U=175;u=840.569;writedatatoarr(B,int(float_to_hex(t),16),4,0);writedatatoarr(B,int(float_to_hex(U),16),4,4);writedatatoarr(B,int(float_to_hex(u),16),4,8)
			elif F==30 and W==36:
				J=[]
				for I in range(56):J.append(B[I])
				B=J.copy();U=383.8333;writedatatoarr(B,int(float_to_hex(U),16),4,4)
			elif F==30 and W in(23,25):
				J=[]
				for I in range(56):J.append(B[I])
				B=J.copy();t=1296;U=1600;u=2028
				if W==23:writedatatoarr(B,int(float_to_hex(t),16),4,0);writedatatoarr(B,int(float_to_hex(u),16),4,8)
				writedatatoarr(B,int(float_to_hex(U),16),4,4)
			elif F==17 and not A0:
				AS=5423.538;AA=160;v=104.5;AT=[[575.763,AA],[494.518,AA],[606.161,v],[534.567,v],[463.642,v]]
				for (AU,AB) in enumerate(AT):a.append({Q:B,K:int(float_to_hex(AB[0]),16),L:int(float_to_hex(AB[1]),16),M:int(float_to_hex(AS),16),N:256+AU,P:70-16,Y:0,R:0,Z:0,S:int(float_to_hex(0.35),16)})
				A0=g
			elif F==86 and not A1:a.append({Q:B,K:int(float_to_hex(118.011),16),L:int(float_to_hex(20),16),M:int(float_to_hex(462.749),16),N:32,P:57-16,Y:0,R:1024,Z:0,S:int(float_to_hex(1),16)});A1=g
			if len(m['add'])>0:
				for f in m['add']:
					if W==f['id_base']:a.append({Q:B,K:int(float_to_hex(f[K]),16),L:int(float_to_hex(f[L]),16),M:int(float_to_hex(f[M]),16),N:f[N],w:g})
			if len(m[AC])>0:
				for n in m[AC]:
					if W==n[N]:
						J=[]
						for I in range(56):J.append(B[I])
						B=J.copy();writedatatoarr(B,int(float_to_hex(n[K]),16),4,0);writedatatoarr(B,int(float_to_hex(n[L]),16),4,4);writedatatoarr(B,int(float_to_hex(n[M]),16),4,8)
			e={T:B};i.append(e);D+=56
		for A in a:
			E=[]
			for I in range(56):
				if w in A and A[w]and Q in A:E.append(A[Q][I])
				else:E.append(0)
			if K in A:writedatatoarr(E,A[K],4,0)
			if L in A:writedatatoarr(E,A[L],4,4)
			if M in A:writedatatoarr(E,A[M],4,8)
			if S in A:writedatatoarr(E,A[S],4,12)
			if R in A:writedatatoarr(E,A[R],2,48)
			if P in A:writedatatoarr(E,A[P],2,50)
			if N in A:writedatatoarr(E,A[N],2,52)
			i.append({T:E})
		for A in j:
			E=[]
			for I in range(16):E.append(0)
			AV=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for I in AV:E.append(I)
			for I in range(12):E.append(0)
			AW=[0,1,0,0]
			for I in AW:E.append(I)
			E=writedatatoarr(E,A[P],2,40);E=writedatatoarr(E,A[N],2,42);E=writedatatoarr(E,A[S],4,12);E=writedatatoarr(E,A[K],4,0);E=writedatatoarr(E,A[L],4,4);E=writedatatoarr(E,A[M],4,8);E=writedatatoarr(E,A[Y],4,24);E=writedatatoarr(E,A[R],4,28);E=writedatatoarr(E,A[Z],4,32);h.append({T:E})
		with open(x.replace(_B,_C),'wb')as X:
			X.write(len(h).to_bytes(4,_A))
			for A in h:X.write(bytearray(A[T]))
			X.write(len(p).to_bytes(4,_A))
			for A in p:X.write(bytearray(A[T]))
			X.write(len(i).to_bytes(4,_A))
			for A in i:X.write(bytearray(A[T]))