'Convert RGB colors into a kong color palette.'
_K='#3e1c73'
_J='overalls'
_I='checkered'
_H='patch'
_G='block'
_F='zones'
_E='kong'
_D='image'
_C='zone'
_B='colors'
_A='fill_type'
import gzip,math
color_palettes=[{_E:'dk',_F:[{_C:'base',_D:3724,_B:['#2da1ad'],_A:_G}]},{_E:'diddy',_F:[{_C:'cap_shirt',_D:3686,_B:['#00ff37'],_A:_G}]},{_E:'lanky',_F:[{_C:_J,_D:3689,_B:[_K],_A:_G},{_C:_H,_D:3734,_B:[_K],_A:_H}]},{_E:'tiny',_F:[{_C:_J,_D:6014,_B:['#ff3beb'],_A:_G}]},{_E:'chunky',_F:[{_C:'shirt_back',_D:3769,_B:['#FF0000','#FFFFFF'],_A:_I},{_C:'shirt_front',_D:3687,_B:['#000000'],_A:_G}]},{_E:'rambi',_F:[{_C:'top',_D:3826,_B:['#070657'],_A:_G}]},{_E:'enguarde',_F:[{_C:'top',_D:3847,_B:['FF0000'],_A:_G}]}]
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors():
	'Convert color into RGBA5551 format.';h='big';W='radial';N=True
	for X in color_palettes:
		for E in X[_F]:
			F=[]
			if E[_A]==_I or E[_A]==W:Y=2
			else:Y=1
			for G in range(Y):
				Z=[0,0,0,1]
				for B in range(3):
					if E[_A]==W:
						C=int(int(f"0x{E[_B][0][2*B+1:2*B+3]}",16)*(1/8))
						if G==1:C=int(C*2)
					else:C=int(int(f"0x{E[_B][G][2*B+1:2*B+3]}",16)*(1/8))
					if C<0:C=0
					elif C>31:C=31
					Z[B]=C
				F.append(Z)
			D=[]
			if E[_A]==_G:
				A=convertRGBAToBytearray(F[0])
				for G in range(32*32):D.extend(A)
			elif E[_A]==W:
				O=15.5;P=15.5;i=O*O+P*P;a=[0,0,0]
				for B in range(3):a[B]=F[1][B]-F[0][B]
				for I in range(32):
					for G in range(32):
						b=O-G;c=P-I;j=b*b+c*c;k=1-j/i;d=[0,0,0,1]
						for B in range(3):
							C=int(a[B]*k+F[0][B])
							if C<0:C=0
							elif C>31:C=31
							d[B]=C
						A=convertRGBAToBytearray(d);D.extend(A)
			elif E[_A]==_I:
				for J in range(3):
					K=int(32/math.pow(2,J));e=int(K/8)
					for I in range(K):
						for G in range(K):
							f=0
							if J==1:f=1
							Q=int(G/e)%2;R=int((I+f)/e)%2;S=(Q+R)%2;A=convertRGBAToBytearray(F[S]);D.extend(A)
				for B in range(18):A=convertRGBAToBytearray(F[1]);D.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray(F[1]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
			elif E[_A]==_H:
				for J in range(3):
					T=int(6/math.pow(2,J));U=int(8/math.pow(2,J));L=3-J
					if L==3:L=5
					K=int(32/math.pow(2,J))
					for I in range(K):
						for G in range(K):
							M=N
							if G<T:M=N
							elif G>=T+4*L:M=N
							elif I<U:M=N
							elif I>=U+3*L:M=N
							if M:A=convertRGBAToBytearray(F[0])
							else:
								l=G-T;m=I-U;Q=int(l/L)%2;R=int(m/L)%2;S=(Q+R)%2;g=[31,31,31,1]
								if S==1:g=[31,0,0,1]
								A=convertRGBAToBytearray(g)
							D.extend(A)
				for B in range(18):A=convertRGBAToBytearray(F[0]);D.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray(F[0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
			with open(f"{X[_E]}{E[_C]}.bin",'wb')as H:H.write(bytearray(D))
			with open('rom/dk64-randomizer-base-dev.z64','r+b')as H:V=1055824;H.seek(V+25*4);n=V+int.from_bytes(H.read(4),h);H.seek(n+E[_D]*4);o=V+int.from_bytes(H.read(4),h);H.seek(o);p=gzip.compress(bytearray(D),compresslevel=9);H.write(p)
convertColors()