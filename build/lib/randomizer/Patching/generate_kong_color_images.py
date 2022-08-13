'Convert RGB colors into a kong color palette.'
import gzip,math
from randomizer.Patching.Patcher import ROM
import js
def convertRGBAToBytearray(rgba_lst):'Convert RGBA list with 4 items (r,g,b,a) to a two-byte array in RGBA5551 format.';A=rgba_lst;B=A[0]<<11|A[1]<<6|A[2]<<1|A[3];C=B%256;D=int(B/256)%256;return[D,C]
def convertColors(color_palettes):
	'Convert color into RGBA5551 format.';X='colors';W='checkered';M='radial';H='fill_type'
	for Y in color_palettes:
		for D in Y['zones']:
			E=[]
			if D[H]==W or D[H]==M:N=2
			else:N=1
			for G in range(N):
				O=[0,0,0,1]
				for A in range(3):
					if D[H]==M:
						B=int(int(f"0x{D[X][0][2*A+1:2*A+3]}",16)*(1/8))
						if G==1:B=int(B*2)
					else:B=int(int(f"0x{D[X][G][2*A+1:2*A+3]}",16)*(1/8))
					if B<0:B=0
					elif B>31:B=31
					O[A]=B
				E.append(O)
			F=[]
			if D[H]=='block':
				C=convertRGBAToBytearray(E[0])
				for G in range(32*32):F.extend(C)
			elif D[H]==M:
				I=15.5;J=15.5;Z=I*I+J*J;P=[0,0,0]
				for A in range(3):P[A]=E[1][A]-E[0][A]
				for K in range(32):
					for G in range(32):
						Q=I-G;R=J-K;a=Q*Q+R*R;b=1-a/Z;S=[0,0,0,1]
						for A in range(3):
							B=int(P[A]*b+E[0][A])
							if B<0:B=0
							elif B>31:B=31
							S[A]=B
						C=convertRGBAToBytearray(S);F.extend(C)
			elif D[H]==W:
				for T in range(3):
					L=int(32/math.pow(2,T));U=int(L/8)
					for K in range(L):
						for G in range(L):
							V=0
							if T==1:V=1
							c=int(G/U)%2;d=int((K+V)/U)%2;e=(c+d)%2;C=convertRGBAToBytearray(E[e]);F.extend(C)
				for A in range(18):C=convertRGBAToBytearray(E[1]);F.extend(C)
				for A in range(4):C=convertRGBAToBytearray([0,0,0,0]);F.extend(C)
				for A in range(3):C=convertRGBAToBytearray(E[1]);F.extend(C)
				for A in range(3):C=convertRGBAToBytearray([0,0,0,0]);F.extend(C)
			f=js.pointer_addresses[25]['entries'][D['image']]['pointing_to'];ROM().seek(f);ROM().writeBytes(gzip.compress(bytearray(F),compresslevel=9))