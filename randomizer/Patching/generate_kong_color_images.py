'Convert RGB colors into a kong color palette.'
import gzip,math,js
from randomizer.Patching.Patcher import ROM
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors(color_palettes):
	'Convert color into RGBA5551 format.';l='colors';k='checkered';Z='radial';P=True;I='fill_type'
	for m in color_palettes:
		for G in m['zones']:
			D=[]
			if G[I]==k or G[I]==Z:a=2
			else:a=1
			for C in range(a):
				b=[0,0,0,1]
				for B in range(3):
					if G[I]==Z:
						E=int(int(f"0x{G[l][0][2*B+1:2*B+3]}",16)*(1/8))
						if C==1:E=int(E*2)
					else:E=int(int(f"0x{G[l][C][2*B+1:2*B+3]}",16)*(1/8))
					if E<0:E=0
					elif E>31:E=31
					b[B]=E
				D.append(b)
			F=[]
			if G[I]in('block','kong'):
				A=convertRGBAToBytearray(D[0])
				for C in range(32*32):F.extend(A)
			elif G[I]==Z:
				S=15.5;T=15.5;n=S*S+T*T;c=[0,0,0]
				for B in range(3):c[B]=D[1][B]-D[0][B]
				for H in range(32):
					for C in range(32):
						d=S-C;e=T-H;o=d*d+e*e;p=1-o/n;f=[0,0,0,1]
						for B in range(3):
							E=int(c[B]*p+D[0][B])
							if E<0:E=0
							elif E>31:E=31
							f[B]=E
						A=convertRGBAToBytearray(f);F.extend(A)
			elif G[I]==k:
				for J in range(3):
					K=int(32/math.pow(2,J));g=int(K/8)
					for H in range(K):
						for C in range(K):
							h=0
							if J==1:h=1
							U=int(C/g)%2;V=int((H+h)/g)%2;W=(U+V)%2;A=convertRGBAToBytearray(D[W]);F.extend(A)
				for B in range(18):A=convertRGBAToBytearray(D[1]);F.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);F.extend(A)
				for B in range(3):A=convertRGBAToBytearray(D[1]);F.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);F.extend(A)
			elif G[I]=='patch':
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
							if O:A=convertRGBAToBytearray(D[0])
							else:
								q=C-X;r=H-Y;U=int(q/L)%2;V=int(r/L)%2;W=(U+V)%2;i=[31,31,31,1]
								if W==1:i=[31,0,0,1]
								A=convertRGBAToBytearray(i)
							F.extend(A)
				for B in range(18):A=convertRGBAToBytearray(D[0]);F.extend(A)
				for B in range(4):A=convertRGBAToBytearray([0,0,0,0]);F.extend(A)
				for B in range(3):A=convertRGBAToBytearray(D[0]);F.extend(A)
				for B in range(3):A=convertRGBAToBytearray([0,0,0,0]);F.extend(A)
			elif G[I]=='sparkle':
				Q=[]
				for (M,s) in enumerate(D[0]):
					if M==3:Q.append(1)
					else:t=0.8*s;Q.append(int(t))
				for H in range(32):
					for C in range(32):
						R=[]
						if C==31:R=D[0].copy()
						else:
							for M in range(4):
								if M==3:N=1
								else:
									u=D[0][M]-Q[M];v=int(u*(C/31));N=Q[M]+v
									if N<0:N=0
									if N>31:N=31
								R.append(N)
						w=[[28,5],[27,10],[21,11],[25,14],[23,15],[23,16],[26,18],[20,19],[25,25]]
						for j in w:
							if j[0]==C and j[1]==H:R=[255,255,255,1]
						F.extend(convertRGBAToBytearray(R))
			x=js.pointer_addresses[25]['entries'][G['image']]['pointing_to'];ROM().seek(x);ROM().writeBytes(gzip.compress(bytearray(F),compresslevel=9))