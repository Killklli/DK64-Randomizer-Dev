'Place Shuffled Shops.'
import math,struct,js
from randomizer.Enums.Regions import Regions
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.ShuffleShopLocations import available_shops
from randomizer.Spoiler import Spoiler
def intf_to_float(intf):
	'Convert float as int format to float.'
	if intf==0:return 0
	else:return struct.unpack('!f',bytes.fromhex(hex(intf)[2:]))[0]
def float_to_hex(f):
	'Convert float to hex.'
	if f==0:return'0x00000000'
	return hex(struct.unpack('<I',struct.pack('<f',f))[0])
def ushort_to_short(ushort):
	'Convert unsigned short to signed short.';A=ushort
	if A>32767:return A-65536
	return A
def ApplyShopRandomizer(spoiler):
	'Write shop locations to ROM.';q='scale_factor';p='replace_zone';o='zone_index';n='model_index';m='pointing_to';l='entries';e=spoiler;d='angle_change';M='replace_model';C='big'
	if e.settings.shuffle_shops:
		f=e.shuffled_shop_locations;Y=[]
		for U in available_shops:
			Z=available_shops[U]
			for B in Z:
				if B.map not in Y:Y.append(B.map)
		for map in Y:
			a=js.pointer_addresses[9][l][map][m];b=js.pointer_addresses[18][l][map][m];g=[];c=0
			for U in available_shops:
				Z=available_shops[U]
				for B in Z:
					if B.map==map and not B.locked:g.append(B.shop);c=U
			h=[]
			for B in g:
				if c not in f.keys():continue
				D={};r=f[c][B];H=-1;I=-1;N=-1;E=-1;F=-1;J=-1;O=-1;P=-1;s=[B,r]
				for (V,W) in enumerate(s):
					if W==Regions.CrankyGeneric:
						if V==0:F=115;J=Maps.Cranky;O=180;P=0.95
						else:H=115;I=Maps.Cranky;N=180;E=0.95
					elif W==Regions.CandyGeneric:
						if V==0:F=292;J=Maps.Candy;O=0;P=0.95
						else:H=292;I=Maps.Candy;N=0;E=0.95
					elif W==Regions.FunkyGeneric:
						if V==0:F=122;J=Maps.Funky;O=90;P=1.045
						else:H=122;I=Maps.Funky;N=90;E=1.045
					elif W==Regions.Snide:
						if V==0:F=121;J=Maps.Snide;O=270;P=3
						else:H=121;I=Maps.Snide;N=270;E=3
				if H>-1 and I>-1 and F>-1 and J>-1:
					Q=-1;R=-1;ROM().seek(a);t=int.from_bytes(ROM().readBytes(4),C)
					for i in range(t):
						if Q==-1:
							u=a+4+i*48;ROM().seek(u+40);v=int.from_bytes(ROM().readBytes(2),C)
							if v==F:Q=i
					ROM().seek(b);w=int.from_bytes(ROM().readBytes(2),C)
					for j in range(w):
						if R==-1:
							k=b+2+j*56;ROM().seek(k+16);x=int.from_bytes(ROM().readBytes(2),C)
							if x==16:
								ROM().seek(k+18);y=int.from_bytes(ROM().readBytes(2),C)
								if y==J:R=j
					if Q>-1 and R>-1:D[n]=Q;D[o]=R;D[M]=H;D['original_model']=F;D[p]=I;D[d]=O-N;D[q]=P/E;h.append(D)
					else:print(f"ERROR: Couldn't find LZ or Model attributed to shop ({Q} | {R})")
				else:print("ERROR: Couldn't find shop in assortment")
			for A in h:
				G=a+4+A[n]*48;X=b+2+A[o]*56;ROM().seek(G+40);ROM().writeMultipleBytes(A[M],2)
				if A[d]!=0:
					ROM().seek(G+28);z=intf_to_float(int.from_bytes(ROM().readBytes(4),C));S=z+A[d]
					if S<0:S+=360
					elif S>=360:S-=360
					ROM().seek(G+28);ROM().writeMultipleBytes(int(float_to_hex(S),16),4)
				ROM().seek(G+12);A0=intf_to_float(int.from_bytes(ROM().readBytes(4),C));E=A0*A[q];ROM().seek(G+12);ROM().writeMultipleBytes(int(float_to_hex(E),16),4);ROM().seek(G);K=intf_to_float(int.from_bytes(ROM().readBytes(4),C));ROM().seek(G+8);L=intf_to_float(int.from_bytes(ROM().readBytes(4),C))
				if K<0:K=int(K)+65536
				else:K=int(K)
				if L<0:L=int(L)+65536
				else:L=int(L)
				ROM().seek(X);ROM().writeMultipleBytes(K,2);ROM().seek(X+4);ROM().writeMultipleBytes(L,2);T=88
				if A[M]==115:T=50
				elif A[M]==122:T=55
				elif A[M]==292:T=40.1
				elif A[M]==121:T=87.5
				ROM().seek(X+6);ROM().writeMultipleBytes(int(T*E),2);ROM().seek(X+18);ROM().writeMultipleBytes(A[p],2)