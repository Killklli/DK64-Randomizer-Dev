'Convert RGB colors into a kong color palette.'
import gzip,math,js
from randomizer.Patching.Patcher import ROM
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors(color_palettes):
	'Convert color into RGBA5551 format.';g='colors';f='checkered';V='radial';N=True;J='fill_type'
	for h in color_palettes:
		for G in h['zones']:
			E=[]
			if G[J]==f or G[J]==V:W=2
			else:W=1
			for F in range(W):
				X=[0,0,0,1]
				for B in range(3):
					if G[J]==V:
						C=int(int(f"0x{G[g][0][2*B+1:2*B+3]}",16)*(1/8))
						if F==1:C=int(C*2)
					else:C=int(int(f"0x{G[g][F][2*B+1:2*B+3]}",16)*(1/8))
					if C<0:C=0
					elif C>31:C=31
					X[B]=C
				E.append(X)
			D=[]
			if G[J]=='block':
				A=convertRGBAToBytearray(E[0])
				for F in range(32*32):D.extend(A)
			elif G[J]==V:
				O=15.5;P=15.5;i=O*O+P*P;Y=[0,0,0]
				for B in range(3):Y[B]=E[1][B]-E[0][B]
				for H in range(32):
					for F in range(32):
						Z=O-F;a=P-H;j=Z*Z+a*a;k=1-j/i;b=[0,0,0,1]
						for B in range(3):
							C=int(Y[B]*k+E[0][B])
							if C<0:C=0
							elif C>31:C=31
							b[B]=C
						A=convertRGBAToBytearray(b);D.extend(A)
			elif G[J]==f:
				for I in range(3):
					K=int(32/math.pow(2,I));c=int(K/8)
					for H in range(K):
						for F in range(K):
							d=0
							if I==1:d=1
							Q=int(F/c)%2;R=int((H+d)/c)%2;S=(Q+R)%2;A=convertRGBAToBytearray(E[S]);D.extend(A)
				for B in range(18):A=convertRGBAToBytearray(E[1]);D.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray(E[1]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
			elif G[J]=='patch':
				for I in range(3):
					T=int(6/math.pow(2,I));U=int(8/math.pow(2,I));L=3-I
					if L==3:L=5
					K=int(32/math.pow(2,I))
					for H in range(K):
						for F in range(K):
							M=N
							if F<T:M=N
							elif F>=T+4*L:M=N
							elif H<U:M=N
							elif H>=U+3*L:M=N
							if M:A=convertRGBAToBytearray(E[0])
							else:
								l=F-T;m=H-U;Q=int(l/L)%2;R=int(m/L)%2;S=(Q+R)%2;e=[31,31,31,1]
								if S==1:e=[31,0,0,1]
								A=convertRGBAToBytearray(e)
							D.extend(A)
				for B in range(18):A=convertRGBAToBytearray(E[0]);D.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray(E[0]);D.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);D.extend(A)
			n=js.pointer_addresses[25]['entries'][G['image']]['pointing_to'];ROM().seek(n);ROM().writeBytes(gzip.compress(bytearray(D),compresslevel=9))