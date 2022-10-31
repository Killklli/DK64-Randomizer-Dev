'Convert RGB colors into a kong color palette.'
_M='#FFFFFF'
_L='#3e1c73'
_K='overalls'
_J='sparkle'
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
color_palettes=[{_E:'dk',_F:[{_C:'base',_D:3724,_B:['#2da1ad'],_A:_G}]},{_E:'diddy',_F:[{_C:'cap_shirt',_D:3686,_B:['#00ff37'],_A:_G}]},{_E:'lanky',_F:[{_C:_K,_D:3689,_B:[_L],_A:_G},{_C:_H,_D:3734,_B:[_L],_A:_H}]},{_E:'tiny',_F:[{_C:_K,_D:6014,_B:['#ff3beb'],_A:_G}]},{_E:'chunky',_F:[{_C:'shirt_back',_D:3769,_B:['#FF0000',_M],_A:_I},{_C:'shirt_front',_D:3687,_B:['#000000'],_A:_G}]},{_E:'discochunky',_F:[{_C:'shirt',_D:3777,_B:['#00237D'],_A:_J},{_C:'gloves',_D:3778,_B:[_M],_A:_J}]},{_E:'krusha',_F:[{_C:'skin',_D:4971,_B:['#003631'],_A:_G},{_C:'belt',_D:4966,_B:['#FFD700'],_A:_G}]},{_E:'rambi',_F:[{_C:'top',_D:3826,_B:['#070657'],_A:_G}]},{_E:'enguarde',_F:[{_C:'top',_D:3847,_B:['FF0000'],_A:_G}]}]
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors():
	'Convert color into RGBA5551 format.';m='big';a='radial';P=True
	for b in color_palettes:
		for G in b[_F]:
			E=[]
			if G[_A]==_I or G[_A]==a:c=2
			else:c=1
			for C in range(c):
				d=[0,0,0,1]
				for B in range(3):
					if G[_A]==a:
						F=int(int(f"0x{G[_B][0][2*B+1:2*B+3]}",16)*(1/8))
						if C==1:F=int(F*2)
					else:F=int(int(f"0x{G[_B][C][2*B+1:2*B+3]}",16)*(1/8))
					if F<0:F=0
					elif F>31:F=31
					d[B]=F
				E.append(d)
			D=[]
			if G[_A]in(_G,_E):
				A=convertRGBAToBytearray(E[0])
				for C in range(32*32):D.extend(A)
			elif G[_A]==a:
				S=15.5;T=15.5;n=S*S+T*T;e=[0,0,0]
				for B in range(3):e[B]=E[1][B]-E[0][B]
				for H in range(32):
					for C in range(32):
						f=S-C;g=T-H;o=f*f+g*g;p=1-o/n;h=[0,0,0,1]
						for B in range(3):
							F=int(e[B]*p+E[0][B])
							if F<0:F=0
							elif F>31:F=31
							h[B]=F
						A=convertRGBAToBytearray(h);D.extend(A)
			elif G[_A]==_I:
				for J in range(3):
					K=int(32/math.pow(2,J));i=int(K/8)
					for H in range(K):
						for C in range(K):
							j=0
							if J==1:j=1
							U=int(C/i)%2;V=int((H+j)/i)%2;W=(U+V)%2;A=convertRGBAToBytearray(E[W]);D.extend(A)
				for B in range(18):A=convertRGBAToBytearray(E[1]);D.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray(E[1]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
			elif G[_A]==_H:
				for J in range(3):
					X=int(6/math.pow(2,J));Y=int(8/math.pow(2,J));L=3-J
					if L==3:L=5
					K=int(32/math.pow(2,J))
					for H in range(K):
						for C in range(K):
							O=P
							if C<X:O=P
							elif C>=X+4*L:O=P
							elif H<Y:O=P
							elif H>=Y+3*L:O=P
							if O:A=convertRGBAToBytearray(E[0])
							else:
								q=C-X;r=H-Y;U=int(q/L)%2;V=int(r/L)%2;W=(U+V)%2;k=[31,31,31,1]
								if W==1:k=[31,0,0,1]
								A=convertRGBAToBytearray(k)
							D.extend(A)
				for B in range(18):A=convertRGBAToBytearray(E[0]);D.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray(E[0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
			elif G[_A]==_J:
				Q=[]
				for (M,s) in enumerate(E[0]):
					if M==3:Q.append(1)
					else:t=0.8*s;Q.append(int(t))
				for H in range(32):
					for C in range(32):
						R=[]
						if C==31:R=E[0].copy()
						else:
							for M in range(4):
								if M==3:N=1
								else:
									u=E[0][M]-Q[M];v=int(u*(C/31));N=Q[M]+v
									if N<0:N=0
									if N>31:N=31
								R.append(N)
						w=[[28,5],[27,10],[21,11],[25,14],[23,15],[23,16],[26,18],[20,19],[25,25]]
						for l in w:
							if l[0]==C and l[1]==H:R=[255,255,255,1]
						D.extend(convertRGBAToBytearray(R))
			with open(f"{b[_E]}{G[_C]}.bin",'wb')as I:I.write(bytearray(D))
			with open('rom/dk64-randomizer-base-dev.z64','r+b')as I:Z=1055824;I.seek(Z+25*4);x=Z+int.from_bytes(I.read(4),m);I.seek(x+G[_D]*4);y=Z+int.from_bytes(I.read(4),m);I.seek(y);z=gzip.compress(bytearray(D),compresslevel=9);I.write(z)
convertColors()