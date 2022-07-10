'Convert RGB colors into a kong color palette.'
_I='overalls'
_H='checkered'
_G='zones'
_F='kong'
_E='image'
_D='zone'
_C='radial'
_B='colors'
_A='fill_type'
import gzip,math
color_palettes=[{_F:'dk',_G:[{_D:'base',_E:3724,_B:['#2da1ad'],_A:_C}]},{_F:'diddy',_G:[{_D:'cap_shirt',_E:3686,_B:['#00ff37'],_A:_C}]},{_F:'lanky',_G:[{_D:_I,_E:3689,_B:['#3e1c73'],_A:_C}]},{_F:'tiny',_G:[{_D:_I,_E:6014,_B:['#ff3beb'],_A:_C}]},{_F:'chunky',_G:[{_D:'shirt_back',_E:3769,_B:['#FF0000','#FFFFFF'],_A:_H},{_D:'shirt_front',_E:3687,_B:['#000000'],_A:_C}]},{_F:'rambi',_G:[{_D:'top',_E:3826,_B:['#070657'],_A:_C}]},{_F:'enguarde',_G:[{_D:'top',_E:3847,_B:['FF0000'],_A:_C}]}]
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors():
	'Convert color into RGBA5551 format.';X='big'
	for N in color_palettes:
		for D in N[_G]:
			F=[]
			if D[_A]==_H or D[_A]==_C:O=2
			else:O=1
			for H in range(O):
				P=[0,0,0,1]
				for A in range(3):
					if D[_A]==_C:
						B=int(int(f"0x{D[_B][0][2*A+1:2*A+3]}",16)*(1/8))
						if H==1:B=int(B*2)
					else:B=int(int(f"0x{D[_B][H][2*A+1:2*A+3]}",16)*(1/8))
					if B<0:B=0
					elif B>31:B=31
					P[A]=B
				F.append(P)
			E=[]
			if D[_A]=='block':
				C=convertRGBAToBytearray(F[0])
				for H in range(32*32):E.extend(C)
			elif D[_A]==_C:
				I=15.5;J=15.5;Y=I*I+J*J;Q=[0,0,0]
				for A in range(3):Q[A]=F[1][A]-F[0][A]
				for K in range(32):
					for H in range(32):
						R=I-H;S=J-K;Z=R*R+S*S;a=1-Z/Y;T=[0,0,0,1]
						for A in range(3):
							B=int(Q[A]*a+F[0][A])
							if B<0:B=0
							elif B>31:B=31
							T[A]=B
						C=convertRGBAToBytearray(T);E.extend(C)
			elif D[_A]==_H:
				for U in range(3):
					L=int(32/math.pow(2,U));V=int(L/8)
					for K in range(L):
						for H in range(L):
							W=0
							if U==1:W=1
							b=int(H/V)%2;c=int((K+W)/V)%2;d=(b+c)%2;C=convertRGBAToBytearray(F[d]);E.extend(C)
				for A in range(18):C=convertRGBAToBytearray(F[1]);E.extend(C)
				for A in range(4):C=convertRGBAToBytearray([0,0,0,0]);E.extend(C)
				for A in range(3):C=convertRGBAToBytearray(F[1]);E.extend(C)
				for A in range(3):C=convertRGBAToBytearray([0,0,0,0]);E.extend(C)
			with open(f"{N[_F]}{D[_D]}.bin",'wb')as G:G.write(bytearray(E))
			with open('rom/dk64-randomizer-base-dev.z64','r+b')as G:M=1055824;G.seek(M+25*4);e=M+int.from_bytes(G.read(4),X);G.seek(e+D[_E]*4);f=M+int.from_bytes(G.read(4),X);G.seek(f);g=gzip.compress(bytearray(E),compresslevel=9);G.write(g)
convertColors()