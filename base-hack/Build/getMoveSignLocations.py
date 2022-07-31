'Get move sign data.'
_H='candy'
_G='funky'
_F='snide'
_E='cranky'
_D='signs'
_C='map_index'
_B='data'
_A='sign_type'
import struct
sign_data=[{_C:7,_D:[{_A:_E,_B:[1695.127,280,3998.528,3]},{_A:_G,_B:[2074.149,520,2248.571,119]},{_A:_F,_B:[2174.763,680,2581.554,288]}]},{_C:38,_D:[{_A:_H,_B:[2364.392,120.5,414.73,0]},{_A:_E,_B:[2697.736,120.5,2538.648,290]},{_A:_G,_B:[2888.978,121.051,4546.7,77]},{_A:_F,_B:[4217.064,120,4468.096,334]}]},{_C:26,_D:[{_A:_H,_B:[192.108,225.5,567.249,38]},{_A:_G,_B:[1426.279,1131.833,468.852,315]},{_A:_E,_B:[202.208,225.5,902.929,335]},{_A:_F,_B:[1753.705,826,2074.416,34]}]},{_C:30,_D:[{_A:_E,_B:[3288.249,1790,2370.118,196]},{_A:_H,_B:[2816.421,1564.253,553.305,82]},{_A:_G,_B:[3676.859,1560.177,1235.449,337]},{_A:_F,_B:[2091.915,1610,4726.344,307]}]},{_C:48,_D:[{_A:_E,_B:[1005.894,247,263.491,164]},{_A:_G,_B:[3271.472,178.69,93.169,264]},{_A:_F,_B:[3090.001,267.011,3588.082,194]}]},{_C:72,_D:[{_A:_E,_B:[1127.643,281.527,1574.504,225]},{_A:_G,_B:[2777.721,280,1340.63,86]},{_A:_H,_B:[3285.967,112.833,2187.781,214]},{_A:_F,_B:[1210.936,64.5,411.259,110]}]},{_C:87,_D:[{_A:_E,_B:[235.221,1135.469,1412.605,278]},{_A:_F,_B:[784.377,1794.167,1362.74,180]}]},{_C:183,_D:[{_A:_G,_B:[1456.806,200,246.614,274]}]},{_C:151,_D:[{_A:_H,_B:[1191.144,300,2142.678,269]}]},{_C:176,_D:[{_A:_E,_B:[602.935,75,1870.478,309]}]},{_C:195,_D:[{_A:_F,_B:[449.519,0,468.524,268]}]}]
def int_to_float(val):'Convert a hex int to a float.';return struct.unpack('!f',bytes.fromhex(hex(val).split('0x')[1]))[0]
def float_to_hex(f):'Convert float to hex.';return hex(struct.unpack('<I',struct.pack('<f',f))[0])
def convertCoord(f):'Convert a coord to an int.';return int(float_to_hex(f),16)
def convertAngle(f):'Convert an angle to DK64 Angle system.';return int(f/360*4096)
def getMoveSignData(map_index,base_stream):
	'Get current move sign data.';C=[]
	for D in sign_data:
		if D[_C]==map_index:
			for A in D[_D]:
				id=256;B=0
				if A[_A]==_E:id=256;B=180
				elif A[_A]==_G:id=257;B=90
				elif A[_A]==_H:id=258;B=0
				elif A[_A]==_F:id=259;B=270
				C.append({'base_byte_stream':base_stream,'type':70-16,'x':convertCoord(A[_B][0]),'y':convertCoord(A[_B][1]),'z':convertCoord(A[_B][2]),'rx':0,'ry':convertAngle(A[_B][3]+B)%4096,'rz':0,'scale':int(float_to_hex(0.25),16),'id':id})
	return C