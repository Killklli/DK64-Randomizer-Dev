'Adjust exits to prevent logical problems with LZR.'
_F='exits'
_E='containing_map'
_D='z'
_C='y'
_B='x'
_A='exit_index'
from typing import BinaryIO
import zlib,struct,os
pointer_table_address=1055824
setup_index=9
pointer_table_index=23
new_caves_portal_coords=[120.997,50,1182.974]
def int_to_float(val):
	'Convert a hex int to a float.'
	if val==0:return 0
	return struct.unpack('!f',bytes.fromhex(hex(val).split('0x')[1]))[0]
exit_adjustments=[{_E:48,_F:[{_A:3,_B:3429,_C:462,_D:4494},{_A:6,_B:4153,_C:163,_D:3721},{_A:4,_B:3982,_C:115,_D:2026},{_A:5,_B:4550,_C:162,_D:3646}]},{_E:30,_F:[{_A:10,_B:1524,_C:1754,_D:3964},{_A:19,_B:3380,_C:1640,_D:120}]},{_E:112,_F:[{_A:1,_B:1515,_C:80,_D:2506}]},{_E:34,_F:[{_A:3,_B:3464,_C:1040,_D:1716}]},{_E:26,_F:[{_A:8,_B:814,_C:8,_D:1334}]},{_E:87,_F:[{_A:15,_B:1293,_C:472,_D:238},{_A:11,_B:1808,_C:1406,_D:1270}]},{_E:72,_F:[{_A:11,_B:int(new_caves_portal_coords[0]-25),_C:int(new_caves_portal_coords[1]),_D:int(new_caves_portal_coords[2]-12)}]}]
exit_additions=[]
temp_file='temp.bin'
def shortToUshort(short):
	'Convert Short to Unsigned Short.';A=short
	if A<0:return A+65536
	return A
def adjustExits(fh):
	'Write new exits.';C=fh;B='big';print('Adjusting Exits');C.seek(pointer_table_address+4*setup_index);O=pointer_table_address+int.from_bytes(C.read(4),B)
	for D in range(216):
		K=[]
		if D not in(97,170,17):
			C.seek(O+4*D);I=pointer_table_address+int.from_bytes(C.read(4),B);P=pointer_table_address+int.from_bytes(C.read(4),B);Q=P-I;C.seek(I);R=int.from_bytes(C.read(2),B);L=False
			if R==8075:L=True
			C.seek(I);E=C.read(Q)
			if L:E=zlib.decompress(E,15+32)
			with open(temp_file,'wb')as A:A.write(E)
			with open(temp_file,'rb')as A:
				S=int.from_bytes(A.read(4),B)
				for T in range(S):
					J=4+T*48;A.seek(J+40);M=int.from_bytes(A.read(2),B);U=int.from_bytes(A.read(2),B)
					if M>=528 and M<=532:
						if U==87 and D==72:A.seek(J+4);G=[int(176.505),int(int_to_float(int.from_bytes(A.read(4),B)))+5,int(1089.408)]
						else:
							A.seek(J);G=[]
							for a in range(3):G.append(int(int_to_float(int.from_bytes(A.read(4),B))))
							G[1]+=5
						K.append(G.copy())
			if os.path.exists(temp_file):os.remove(temp_file)
		exit_additions.append(K.copy())
	C.seek(pointer_table_address+4*pointer_table_index);V=pointer_table_address+int.from_bytes(C.read(4),B)
	for D in range(216):
		C.seek(V+4*D);H=pointer_table_address+int.from_bytes(C.read(4),B);W=pointer_table_address+int.from_bytes(C.read(4),B);X=W-H;C.seek(H);E=C.read(X);F=f"exit{D}.bin"
		with open(F,'wb')as A:
			A.write(E)
			for Y in exit_additions[D]:
				for Z in Y:A.write(shortToUshort(Z).to_bytes(2,B))
				A.write((0).to_bytes(4,B))
		with open(F,'r+b')as A:
			for N in exit_adjustments:
				if D==N[_E]:
					for exit in N[_F]:H=exit[_A]*10;A.seek(H);A.write(shortToUshort(exit[_B]).to_bytes(2,B));A.write(shortToUshort(exit[_C]).to_bytes(2,B));A.write(shortToUshort(exit[_D]).to_bytes(2,B))
		if os.path.exists(F)and os.path.getsize(F)==0:os.remove(F)