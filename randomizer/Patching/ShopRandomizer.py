'Place Shuffled Shops.'
from randomizer.Spoiler import Spoiler
import js,struct,math
from randomizer.ShuffleShopLocations import available_shops
from randomizer.Enums.Regions import Regions
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
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
	'Write shop locations to ROM.';u='scale_factor';t='replace_zone';s='zone_index';r='model_index';q='pointing_to';p='entries';f=spoiler;e='angle_change';K='replace_model';B='big'
	if f.settings.shuffle_shops:
		v=f.shuffled_shop_locations;W=[]
		for T in available_shops:
			X=available_shops[T]
			for C in X:
				if C.map not in W:W.append(C.map)
		for map in W:
			Y=js.pointer_addresses[9][p][map][q];Z=js.pointer_addresses[18][p][map][q];g=[];h=0
			for T in available_shops:
				X=available_shops[T]
				for C in X:
					if C.map==map and not C.locked:g.append(C.shop);h=T
			i=[]
			for C in g:
				D={};w=v[h][C];H=-1;I=-1;L=-1;E=-1;F=-1;J=-1;M=-1;N=-1;x=[C,w]
				for (U,V) in enumerate(x):
					if V==Regions.CrankyGeneric:
						if U==0:F=115;J=Maps.Cranky;M=180;N=1
						else:H=115;I=Maps.Cranky;L=180;E=1
					elif V==Regions.CandyGeneric:
						if U==0:F=292;J=Maps.Candy;M=0;N=1
						else:H=292;I=Maps.Candy;L=0;E=1
					elif V==Regions.FunkyGeneric:
						if U==0:F=122;J=Maps.Funky;M=90;N=1.1
						else:H=122;I=Maps.Funky;L=90;E=1.1
					elif V==Regions.Snide:
						if U==0:F=121;J=Maps.Snide;M=270;N=3
						else:H=121;I=Maps.Snide;L=270;E=3
				if H>-1 and I>-1 and F>-1 and J>-1:
					O=-1;P=-1;ROM().seek(Y);y=int.from_bytes(ROM().readBytes(4),B)
					for j in range(y):
						if O==-1:
							z=Y+4+j*48;ROM().seek(z+40);A0=int.from_bytes(ROM().readBytes(2),B)
							if A0==F:O=j
					ROM().seek(Z);A1=int.from_bytes(ROM().readBytes(2),B)
					for k in range(A1):
						if P==-1:
							l=Z+2+k*56;ROM().seek(l+16);A2=int.from_bytes(ROM().readBytes(2),B)
							if A2==16:
								ROM().seek(l+18);A3=int.from_bytes(ROM().readBytes(2),B)
								if A3==J:P=k
					if O>-1 and P>-1:D[r]=O;D[s]=P;D[K]=H;D['original_model']=F;D[t]=I;D[e]=M-L;D[u]=N/E;i.append(D)
					else:print(f"ERROR: Couldn't find LZ or Model attributed to shop ({O} | {P})")
				else:print("ERROR: Couldn't find shop in assortment")
			for A in i:
				G=Y+4+A[r]*48;Q=Z+2+A[s]*56;ROM().seek(G+40);ROM().writeMultipleBytes(A[K],2)
				if A[e]!=0:
					ROM().seek(G+28);A4=intf_to_float(int.from_bytes(ROM().readBytes(4),B));R=A4+A[e]
					if R<0:R+=360
					elif R>=360:R-=360
					ROM().seek(G+28);ROM().writeMultipleBytes(int(float_to_hex(R),16),4)
				ROM().seek(G+12);A5=intf_to_float(int.from_bytes(ROM().readBytes(4),B));E=A5*A[u];ROM().seek(G+12);ROM().writeMultipleBytes(int(float_to_hex(E),16),4);ROM().seek(G);m=intf_to_float(int.from_bytes(ROM().readBytes(4),B));ROM().seek(G+8);n=intf_to_float(int.from_bytes(ROM().readBytes(4),B));ROM().seek(Q);A6=ushort_to_short(int.from_bytes(ROM().readBytes(2),B));ROM().seek(Q+4);A7=ushort_to_short(int.from_bytes(ROM().readBytes(2),B));a=A6-m;b=A7-n;A8=math.sqrt(a*a+b*b);S=1
				if A[K]==115:S=35
				elif A[K]==122:S=43
				elif A[K]==292:S=35
				elif A[K]==121:S=50
				A9=S*E;o=A9/A8;AA=a*o;AB=b*o;c=m+AA;d=n+AB
				if c<0:c+=65536
				if d<0:d+=65536
				ROM().seek(Q+0);ROM().writeMultipleBytes(c,2);ROM().seek(Q+4);ROM().writeMultipleBytes(d,2);ROM().seek(Q+18);ROM().writeMultipleBytes(A[t],2)