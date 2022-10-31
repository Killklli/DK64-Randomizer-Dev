'Library functions for patching.'
_C='pointing_to'
_B='entries'
_A='big'
import struct,js
from randomizer.Patching.Patcher import ROM
from randomizer.Enums.ScriptTypes import ScriptTypes
def float_to_hex(f):
	'Convert float to hex.'
	if f==0:return'0x00000000'
	return hex(struct.unpack('<I',struct.pack('<f',f))[0])
def short_to_ushort(short):
	'Convert short to unsigned short format.';A=short
	if A<0:return A+65536
	return A
def intf_to_float(intf):
	'Convert float as int format to float.'
	if intf==0:return 0
	else:return struct.unpack('!f',bytes.fromhex('{:08X}'.format(intf)))[0]
def ushort_to_short(ushort):
	'Convert unsigned short to signed short.';A=ushort
	if A>32767:return A-65536
	return A
def getNextFreeID(cont_map_id,ignore=[]):
	'Get next available Model 2 ID.';B=js.pointer_addresses[9][_B][cont_map_id][_C];ROM().seek(B);D=int.from_bytes(ROM().readBytes(4),_A);A=list(range(0,600))
	for E in range(D):
		F=B+4+E*48;ROM().seek(F+42);C=int.from_bytes(ROM().readBytes(2),_A)
		if C in A:A.remove(C)
	for id in range(544,549):
		if id in A:A.remove(id)
	for id in ignore:
		if id in A:A.remove(id)
	if len(A)>0:return min(A)
	return 0
def addNewScript(cont_map_id,item_ids,type):
	'Append a new script to the script database. Has to be just 1 execution and 1 endblock.';E=item_ids;B=js.pointer_addresses[10][_B][cont_map_id][_C];ROM().seek(B);J=int.from_bytes(ROM().readBytes(2),_A);D=[];A=2
	for R in range(J):
		ROM().seek(B+A);F=B+A;K=int.from_bytes(ROM().readBytes(2),_A);L=int.from_bytes(ROM().readBytes(2),_A);A+=6
		for S in range(L):ROM().seek(B+A);M=int.from_bytes(ROM().readBytes(2),_A);A+=2+8*M;ROM().seek(B+A);N=int.from_bytes(ROM().readBytes(2),_A);A+=2+8*N
		O=B+A
		if K not in E:
			G=[];ROM().seek(F)
			for H in range(int((O-F)/2)):G.append(int.from_bytes(ROM().readBytes(2),_A))
			D.append(G)
	C=-100
	if type==ScriptTypes.Bananaport:C=-1
	elif type==ScriptTypes.Wrinkly:C=-2
	elif type==ScriptTypes.TnsPortal:C=-3
	elif type==ScriptTypes.TnsIndicator:C=-4
	elif type==ScriptTypes.CrownMain:C=-5
	elif type==ScriptTypes.CrownIsles2:C=-6
	for I in E:P=[I,1,0,0,1,7,125,short_to_ushort(C),I];D.append(P)
	ROM().seek(B);ROM().writeMultipleBytes(len(D),2)
	for Q in D:
		for H in Q:ROM().writeMultipleBytes(H,2)