'Convert RGB colors into a kong color palette.'
_I='overalls'
_H='checkered'
_G='block'
_F='zones'
_E='kong'
_D='image'
_C='zone'
_B='colors'
_A='fill_type'
import gzip,math
color_palettes=[{_E:'dk',_F:[{_C:'base',_D:3724,_B:['#2da1ad'],_A:_G}]},{_E:'diddy',_F:[{_C:'cap_shirt',_D:3686,_B:['#00ff37'],_A:_G}]},{_E:'lanky',_F:[{_C:_I,_D:3689,_B:['#3e1c73'],_A:_G}]},{_E:'tiny',_F:[{_C:_I,_D:6014,_B:['#ff3beb'],_A:_G}]},{_E:'chunky',_F:[{_C:'shirt_back',_D:3769,_B:['#FF0000','#FFFFFF'],_A:_H},{_C:'shirt_front',_D:3687,_B:['#000000'],_A:_G}]},{_E:'rambi',_F:[{_C:'top',_D:3826,_B:['#070657'],_A:_G}]},{_E:'enguarde',_F:[{_C:'top',_D:3847,_B:['FF0000'],_A:_G}]}]
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors():
	'Convert color into RGBA5551 format.';Y='big';N='radial'
	for O in color_palettes:
		for D in O[_F]:
			F=[]
			if D[_A]==_H or D[_A]==N:P=2
			else:P=1
			for H in range(P):
				Q=[0,0,0,1]
				for A in range(3):
					if D[_A]==N:
						B=int(int(f"0x{D[_B][0][2*A+1:2*A+3]}",16)*(1/8))
						if H==1:B=int(B*2)
					else:B=int(int(f"0x{D[_B][H][2*A+1:2*A+3]}",16)*(1/8))
					if B<0:B=0
					elif B>31:B=31
					Q[A]=B
				F.append(Q)
			E=[]
			if D[_A]==_G:
				C=convertRGBAToBytearray(F[0])
				for H in range(32*32):E.extend(C)
			elif D[_A]==N:
				I=15.5;J=15.5;Z=I*I+J*J;R=[0,0,0]
				for A in range(3):R[A]=F[1][A]-F[0][A]
				for K in range(32):
					for H in range(32):
						S=I-H;T=J-K;a=S*S+T*T;b=1-a/Z;U=[0,0,0,1]
						for A in range(3):
							B=int(R[A]*b+F[0][A])
							if B<0:B=0
							elif B>31:B=31
							U[A]=B
						C=convertRGBAToBytearray(U);E.extend(C)
			elif D[_A]==_H:
				for V in range(3):
					L=int(32/math.pow(2,V));W=int(L/8)
					for K in range(L):
						for H in range(L):
							X=0
							if V==1:X=1
							c=int(H/W)%2;d=int((K+X)/W)%2;e=(c+d)%2;C=convertRGBAToBytearray(F[e]);E.extend(C)
				for A in range(18):C=convertRGBAToBytearray(F[1]);E.extend(C)
				for A in range(4):C=convertRGBAToBytearray([0,0,0,0]);E.extend(C)
				for A in range(3):C=convertRGBAToBytearray(F[1]);E.extend(C)
				for A in range(3):C=convertRGBAToBytearray([0,0,0,0]);E.extend(C)
			with open(f"{O[_E]}{D[_C]}.bin",'wb')as G:G.write(bytearray(E))
			with open('rom/dk64-randomizer-base-dev.z64','r+b')as G:M=1055824;G.seek(M+25*4);f=M+int.from_bytes(G.read(4),Y);G.seek(f+D[_D]*4);g=M+int.from_bytes(G.read(4),Y);G.seek(g);h=gzip.compress(bytearray(E),compresslevel=9);G.write(h)
convertColors()