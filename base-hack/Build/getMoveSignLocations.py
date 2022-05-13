'Get move sign data.'
_G='candy'
_F='funky'
_E='cranky'
_D='signs'
_C='map_index'
_B='sign_type'
_A='data'
import struct
sign_data=[{_C:7,_D:[{_B:_E,_A:[1693.203,280.964,3934.433,183.867,1]},{_B:_F,_A:[2048.232,522.388,2195.41,207.861,1]}]},{_C:38,_D:[{_B:_G,_A:[2365.486,120,494.248,358.418,1.12]},{_B:_E,_A:[2755.299,124.339,2522.297,110.654,1]},{_B:_F,_A:[2902.485,123.604,4490.055,163.125,1]}]},{_C:26,_D:[{_B:_G,_A:[235.468,225.5,620.636,37.002,1]},{_B:_F,_A:[1471.488,1132.888,516.591,43.066,1]},{_B:_E,_A:[229.027,228.203,850.685,147.832,1]}]},{_C:30,_D:[{_B:_E,_A:[3301.647,1792.776,2427.058,16.348,1]},{_B:_G,_A:[2904.595,1561.547,564.17,71.191,1.28]},{_B:_F,_A:[3742.295,1568.709,1268.402,64.863,1.12]}]},{_C:48,_D:[{_B:_E,_A:[984.411,251.25,342.849,342.42,1.28]},{_B:_F,_A:[3261.958,181.03,163.222,353.232,1.16]}]},{_C:72,_D:[{_B:_E,_A:[1172.329,282.911,1618.7,37.793,1]},{_B:_F,_A:[2780.684,283.12,1280.243,179.561,1.04]},{_B:_G,_A:[3239.475,112.833,2120.751,208.916,1.26]}]},{_C:87,_D:[{_B:_E,_A:[294.081,1138.622,1405.777,95.625,1]}]},{_C:183,_D:[{_B:_F,_A:[1463.363,203.18,310.011,359.561,1.06]}]},{_C:151,_D:[{_B:_G,_A:[1077.46,300,2140.457,271.67,1.7]}]},{_C:176,_D:[{_B:_E,_A:[651.318,77.255,1834.692,126.914,1]}]}]
def int_to_float(val):'Convert a hex int to a float.';return struct.unpack('!f',bytes.fromhex(hex(val).split('0x')[1]))[0]
def float_to_hex(f):'Convert float to hex.';return hex(struct.unpack('<I',struct.pack('<f',f))[0])
def convertCoord(f):'Convert a coord to an int.';return int(float_to_hex(f),16)
def convertAngle(f):'Convert an angle to DK64 Angle system.';return int(f/360*4096)
def getMoveSignData(map_index,base_stream):
	'Get current move sign data.';C=[]
	for D in sign_data:
		if D[_C]==map_index:
			for A in D[_D]:
				B=40;id=256
				if A[_B]==_E:B=40;id=256
				elif A[_B]==_F:B=40;id=257
				elif A[_B]==_G:B=40;id=258
				C.append({'base_byte_stream':base_stream,'type':70-16,'x':convertCoord(A[_A][0]),'y':convertCoord(A[_A][1]+B*A[_A][4]),'z':convertCoord(A[_A][2]),'rx':0,'ry':(convertAngle(A[_A][3])+2048)%4096,'rz':0,'scale':int(float_to_hex(0.25),16),'id':id})
	return C