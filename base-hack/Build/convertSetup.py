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
	'Modify the file to be updated.\n\n    Args:\n        file_name (str): File name.\n        map_index (int): Map index.\n    ';A7='change';v=file_name;u='use_byte_stream';n=False;f=True;Z=b'';Y='rz';X='rx';T='stream';S='scale';R='ry';Q='base_byte_stream';P='type';N='id';M='z';L='y';K='x';F=map_index;global base_stream
	with open(v,'r+b')as A8:
		G=A8.read();A9=int.from_bytes(G[:4],_A);C=4;g=[];o=[];h=[];i=[];a=[];b=544;w=n;x=n;y=n;z=n
		for A in range(A9):
			B=G[C:C+48];j=int.from_bytes(G[C+40:C+42],_A);I=int.from_bytes(G[C+42:C+44],_A)
			if j==684 and F!=42:
				if F==72 and not x and I==38:
					for k in range(2):A0=50.167;i.append({Q:B,P:[684,683][k],K:int(float_to_hex(120.997),16),L:[int(float_to_hex(A0),16),int(float_to_hex(A0-30),16)][k],M:int(float_to_hex(1182.974),16),X:0,R:int(float_to_hex(75.146),16),Y:0,N:[368,b][k],S:[int(float_to_hex(1),16),int(float_to_hex(0.35),16)][k]})
					b+=1;x=f
				base_stream=B;A1=int.from_bytes(G[C+0:C+4],_A);p=int.from_bytes(G[C+4:C+8],_A);AA=int_to_float(p)-30;p=int(float_to_hex(AA),16);A2=int.from_bytes(G[C+8:C+12],_A);AR=int.from_bytes(G[C+24:C+28],_A);c=int.from_bytes(G[C+28:C+32],_A);AS=int.from_bytes(G[C+32:C+36],_A);I=int.from_bytes(G[C+42:C+44],_A)
				if F==7:
					if b==544:A1=int(float_to_hex(805.6618),16);A2=int(float_to_hex(2226.797),16)
				i.append({Q:B,P:683,K:A1,L:p,M:A2,X:0,R:c,Y:0,N:b,S:int(float_to_hex(0.35),16)});b+=1
			if F==34 and not w and I==6:w=f;i.append({Q:B,P:132,K:int(float_to_hex(2457.471),16),L:int(float_to_hex(1280),16),M:int(float_to_hex(3458.604),16),X:0,R:int(float_to_hex(166),16),Y:0,N:256,S:int(float_to_hex(1.18),16)})
			if F==7 and I==26 or F==176 and I==57:
				j=206;E=Z
				for A in range(41):E+=B[A].to_bytes(1,_A)
				E+=j.to_bytes(1,_A)
				for A in range(48-42):E+=B[A+42].to_bytes(1,_A)
				B=E
			elif F==26 and I==318 or F==5 and I==2:
				E=Z;AB=int(float_to_hex(0.2),16)
				for A in range(12):E+=B[A].to_bytes(1,_A)
				E+=AB.to_bytes(4,_A)
				for A in range(48-16):E+=B[A+16].to_bytes(1,_A)
				B=E
			if F==26 and I==36:
				E=Z;O=[0,0,0];q=[1455.853,6.5,522.716];O[0]=int(float_to_hex(q[0]),16);O[1]=int(float_to_hex(q[1]),16);O[2]=int(float_to_hex(q[2]),16);c=int(float_to_hex(0),16)
				for A in O:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=B[A+12].to_bytes(1,_A)
				E+=c.to_bytes(4,_A)
				for A in range(48-32):E+=B[A+32].to_bytes(1,_A)
				B=E
			if F==26 and I>=103 and I<=118:
				E=Z;A3=I-103;AC=A3%4;AD=int(A3/4);AE=2606.114;AF=1767.899;A4=37.7;O=[0,0,0];O[0]=int(float_to_hex(AE+A4*AD),16);O[1]=int(float_to_hex(1002),16);O[2]=int(float_to_hex(AF+A4*AC),16)
				for A in O:E+=A.to_bytes(4,_A)
				for A in range(28-12):E+=B[A+12].to_bytes(1,_A)
				E+=c.to_bytes(4,_A)
				for A in range(48-32):E+=B[A+32].to_bytes(1,_A)
				B=E;c=int(float_to_hex(180),16)
			if F==72:
				if I==87 or I==207:
					E=Z;AG=176.505;AH=1089.408;E+=int(float_to_hex(AG),16).to_bytes(4,_A)
					for A in range(4):E+=B[A+4].to_bytes(1,_A)
					E+=int(float_to_hex(AH),16).to_bytes(4,_A)
					for A in range(48-12):E+=B[A+12].to_bytes(1,_A)
					B=E
			if F==7 and I==201:
				E=Z;U=int(float_to_hex(400),16)
				for A in range(4):E+=B[A].to_bytes(1,_A)
				E+=U.to_bytes(4,_A)
				for A in range(48-8):E+=B[A+8].to_bytes(1,_A)
				B=E
			d={T:B,P:j};g.append(d);C+=48
		AI=getMoveSignData(F,base_stream);l=generateVineSeries(F)
		for AJ in AI:a.append(AJ)
		AK=int.from_bytes(G[C:C+4],_A);C+=4
		for A in range(AK):B=G[C:C+36];d={T:B};o.append(d);C+=36
		AL=int.from_bytes(G[C:C+4],_A);C+=4
		for A in range(AL):
			B=G[C:C+56];V=int.from_bytes(G[C+52:C+54],_A)
			if F==26 and V==13:
				J=[]
				for H in range(56):J.append(B[H])
				B=J.copy();r=1237.001;U=175;s=840.569;writedatatoarr(B,int(float_to_hex(r),16),4,0);writedatatoarr(B,int(float_to_hex(U),16),4,4);writedatatoarr(B,int(float_to_hex(s),16),4,8)
			elif F==30 and V==36:
				J=[]
				for H in range(56):J.append(B[H])
				B=J.copy();U=383.8333;writedatatoarr(B,int(float_to_hex(U),16),4,4)
			elif F==30 and V in(23,25):
				J=[]
				for H in range(56):J.append(B[H])
				B=J.copy();r=1296;U=1600;s=2028
				if V==23:writedatatoarr(B,int(float_to_hex(r),16),4,0);writedatatoarr(B,int(float_to_hex(s),16),4,8)
				writedatatoarr(B,int(float_to_hex(U),16),4,4)
			elif F==17 and not y:
				AM=5423.538;A5=160;t=104.5;AN=[[575.763,A5],[494.518,A5],[606.161,t],[534.567,t],[463.642,t]]
				for (AO,A6) in enumerate(AN):a.append({Q:B,K:int(float_to_hex(A6[0]),16),L:int(float_to_hex(A6[1]),16),M:int(float_to_hex(AM),16),N:256+AO,P:70-16,X:0,R:0,Y:0,S:int(float_to_hex(0.35),16)})
				y=f
			elif F==86 and not z:a.append({Q:B,K:int(float_to_hex(118.011),16),L:int(float_to_hex(20),16),M:int(float_to_hex(462.749),16),N:32,P:57-16,X:0,R:1024,Y:0,S:int(float_to_hex(1),16)});z=f
			if len(l['add'])>0:
				for e in l['add']:
					if V==e['id_base']:a.append({Q:B,K:int(float_to_hex(e[K]),16),L:int(float_to_hex(e[L]),16),M:int(float_to_hex(e[M]),16),N:e[N],u:f})
			if len(l[A7])>0:
				for m in l[A7]:
					if V==m[N]:
						J=[]
						for H in range(56):J.append(B[H])
						B=J.copy();writedatatoarr(B,int(float_to_hex(m[K]),16),4,0);writedatatoarr(B,int(float_to_hex(m[L]),16),4,4);writedatatoarr(B,int(float_to_hex(m[M]),16),4,8)
			d={T:B};h.append(d);C+=56
		for A in a:
			D=[]
			for H in range(56):
				if u in A and A[u]and Q in A:D.append(A[Q][H])
				else:D.append(0)
			if K in A:writedatatoarr(D,A[K],4,0)
			if L in A:writedatatoarr(D,A[L],4,4)
			if M in A:writedatatoarr(D,A[M],4,8)
			if S in A:writedatatoarr(D,A[S],4,12)
			if R in A:writedatatoarr(D,A[R],2,48)
			if P in A:writedatatoarr(D,A[P],2,50)
			if N in A:writedatatoarr(D,A[N],2,52)
			h.append({T:D})
		for A in i:
			D=[]
			for H in range(16):D.append(0)
			AP=[255,251,0,0,21,0,0,0,64,192,0,0,67,179,0,0]
			for H in AP:D.append(H)
			for H in range(12):D.append(0)
			AQ=[0,1,0,0]
			for H in AQ:D.append(H)
			D=writedatatoarr(D,A[P],2,40);D=writedatatoarr(D,A[N],2,42);D=writedatatoarr(D,A[S],4,12);D=writedatatoarr(D,A[K],4,0);D=writedatatoarr(D,A[L],4,4);D=writedatatoarr(D,A[M],4,8);D=writedatatoarr(D,A[X],4,24);D=writedatatoarr(D,A[R],4,28);D=writedatatoarr(D,A[Y],4,32);g.append({T:D})
		with open(v.replace(_B,_C),'wb')as W:
			W.write(len(g).to_bytes(4,_A))
			for A in g:W.write(bytearray(A[T]))
			W.write(len(o).to_bytes(4,_A))
			for A in o:W.write(bytearray(A[T]))
			W.write(len(h).to_bytes(4,_A))
			for A in h:W.write(bytearray(A[T]))