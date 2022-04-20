'Encoders for updating file data.'
_k='behaviour'
_j='unkFooter'
_i='Unknown field type in readStruct(): '
_h='unk10'
_g='scale'
_f='mapping'
_e='unk4'
_d='unk18'
_c='index_offset'
_b=False
_a='actors'
_Z='conveyor_data'
_Y='model2Index'
_X='extra_data_count'
_W='points'
_V='character_spawners'
_U='points_0xA'
_T='points_0x6'
_S='fences'
_R=True
_Q='model2'
_P='extra_data'
_O='uint'
_N='w+b'
_M='w'
_L='rb'
_K='index_of'
_J='z_pos'
_I='y_pos'
_H='x_pos'
_G='ushort'
_F='byte'
_E='size'
_D='short'
_C='big'
_B='name'
_A='type'
import json,math,struct
from typing import BinaryIO
from actor_names import actor_names
from character_spawner_names import character_spawner_names
from map_names import maps
from model2_names import model2_names
from model_names import cutscene_model_names
valueSamples={}
def sampleValue(tag,value):
	'Sample the value.';E='max';D='min';C='all';B=value;A=tag
	if A not in valueSamples:valueSamples[A]={D:math.inf,E:-math.inf,C:{}}
	if type(B)==int or type(B)==float:valueSamples[A][D]=min(B,valueSamples[A][D]);valueSamples[A][E]=max(B,valueSamples[A][E])
	if B not in valueSamples[A][C]:valueSamples[A][C][B]=0
	valueSamples[A][C][B]+=1;return B
dump_struct_debug_info=_b
def ScriptHawkSetPosition(x,y,z):'Set Scripthawk position.';return'Game.setPosition('+str(x)+','+str(y)+','+str(z)+');'
def getStructSize(struct_fields):
	'Get Struct size.';B=0
	for A in struct_fields:
		if A[_A]==_F:A[_E]=1
		elif A[_A]==_D:A[_E]=2
		elif A[_A]==_G:A[_E]=2
		elif A[_A]==float:A[_E]=4
		B+=A[_E]
	return B
def readStructArray(byte_read,offset,length,struct_fields):
	'Read Struct Array.';A=struct_fields;B=[];C=offset;D=getStructSize(A)
	for E in range(length):B.append(readStruct(byte_read,C,A));C+=D
	return B
def readStruct(byte_read,offset,struct_fields):
	'Read a particular struct.';H='_name';G=offset;F='sample';D=byte_read;C=G;B={}
	for A in struct_fields:
		if A[_A]==_F:A[_A]=_O;A[_E]=1
		if A[_A]==_D:A[_A]=int;A[_E]=2
		elif A[_A]==_G:A[_A]=_O;A[_E]=2
		if A[_A]==int:B[A[_B]]=int.from_bytes(D[C:C+A[_E]],byteorder=_C,signed=_R)
		elif A[_A]==_O:B[A[_B]]=int.from_bytes(D[C:C+A[_E]],byteorder=_C)
		elif A[_A]==float:A[_E]=4;B[A[_B]]=struct.unpack('>f',D[C:C+4])[0]
		elif A[_A]==bool:B[A[_B]]=_R if int.from_bytes(D[C:C+A[_E]],byteorder=_C)else _b
		elif A[_A]==bytes:B[A[_B]]=D[C:C+A[_E]].hex(' ').upper()
		else:print(_i+A[_A])
		if _K in A:
			E=0
			if _c in A:E=A[_c]
			if B[A[_B]]+E<len(A[_K]):B[A[_B]+H]=A[_K][B[A[_B]]+E]
			else:B[A[_B]+H]='Unknown '+hex(B[A[_B]]+E)
		if F in A:I=A[F]if type(A[F])==str else A[_B];sampleValue(I,B[A[_B]])
		C+=A[_E]
	if dump_struct_debug_info:
		B['DEBUG_File_Address']=hex(G)
		if _H in B and _I in B and _J in B:B['DEBUG_Set_Position']=ScriptHawkSetPosition(B[_H],B[_I],B[_J])
	return B
def writeStructArray(fh,struct_array,struct_fields,include_count=_b,count_bytes=0):
	'Write the struct Array.';A=struct_array
	if include_count:fh.write(len(A).to_bytes(count_bytes,byteorder=_C))
	for B in A:writeStruct(fh,B,struct_fields)
def writeStruct(fh,struct_data,struct_fields):
	'Write a particular struct.';C=struct_data;B=fh
	for A in struct_fields:
		if A[_A]==_F:A[_A]=_O;A[_E]=1
		elif A[_A]==_D:A[_A]=int;A[_E]=2
		elif A[_A]==_G:A[_A]=_O;A[_E]=2
		if A[_A]==int:B.write(int(C[A[_B]]).to_bytes(A[_E],byteorder=_C,signed=_R))
		elif A[_A]==_O:B.write(int(C[A[_B]]).to_bytes(A[_E],byteorder=_C))
		elif A[_A]==float:B.write(struct.pack('>f',C[A[_B]]))
		elif A[_A]==bool:B.write(bytes([1 if C[A[_B]]else 0]))
		elif A[_A]==bytes:B.write(bytes.fromhex(C[A[_B]]))
		else:print(_i+A[_A])
lz_object_types=['Unknown 0x0','Unused 0x1','Unknown 0x2','Boss Door Trigger 0x3','Unknown 0x4','Cutscene Trigger 0x5','Unknown 0x6','Unknown 0x7','Unknown 0x8','Loading Zone 0x9','Cutscene Trigger 0xA','Unknown 0xB','Loading Zone + Objects 0xC','Loading Zone 0xD','Unused 0xE','Warp Trigger 0xF','Loading Zone 0x10','Loading Zone 0x11','Unused 0x12','Unknown 0x13','Boss Loading Zone 0x14','Cutscene Trigger 0x15','Unknown 0x16','Cutscene Trigger 0x17','Unknown 0x18','Trigger 0x19','Unknown 0x1A','Slide Trigger 0x1B','Unknown 0x1C','Unused 0x1D','Unused 0x1E','Unused 0x1F','Cutscene Trigger 0x20','Unused 0x21','Unused 0x22','Unused 0x23','Unknown 0x24','Unknown 0x25','Unknown 0x26']
lz_struct=[{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'radius',_A:_D},{_B:'height',_A:_D},{_B:'unkA',_A:_G},{_B:'activation_type',_A:_F},{_B:'boolD',_A:bool,_E:1},{_B:'unkE',_A:_F},{_B:'unkF',_A:_F},{_B:'object_type',_A:_D,_K:lz_object_types},{_B:'destination_map',_A:_G,_K:maps},{_B:'destination_exit',_A:_G},{_B:'transition_type',_A:_G},{_B:_d,_A:_G},{_B:'cutscene_is_tied',_A:_G},{_B:'cutscene_index',_A:_G},{_B:'shift_camera_to_kong',_A:_G},{_B:'unk20',_A:bytes,_E:56-32}]
def decodeLoadingZones(decoded_filename,encoded_filename):
	'Decode loading zones.'
	with open(encoded_filename,_L)as D:
		A=D.read();E=int.from_bytes(A[0:2],byteorder=_C);B=readStructArray(A,2,E,lz_struct)
		for C in B:
			if'Loading Zone'not in C['object_type_name']:del C['destination_map_name']
		with open(decoded_filename,_M)as F:json.dump(B,F,indent=4,default=str)
def encodeLoadingZones(decoded_filename,encoded_filename):
	'Encode loading zones.'
	with open(decoded_filename)as A:
		B=json.load(A)
		with open(encoded_filename,_N)as C:writeStructArray(C,B,lz_struct,include_count=_R,count_bytes=2)
exit_struct=[{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'angle',_A:_D},{_B:'has_autowalk',_A:_F},{_B:_E,_A:_F}]
def decodeExits(decoded_filename,encoded_filename):
	'Decode exits.'
	with open(encoded_filename,_L)as B:
		A=B.read();C=math.floor(len(A)/10);D=readStructArray(A,0,C,exit_struct)
		with open(decoded_filename,_M)as E:json.dump(D,E,indent=4,default=str)
def encodeExits(decoded_filename,encoded_filename):
	'Encode exits.'
	with open(decoded_filename)as A:
		B=json.load(A)
		with open(encoded_filename,_N)as C:writeStructArray(C,B,exit_struct)
autowalk_point_struct=[{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'unk6',_A:bytes,_E:18-6}]
def decodeAutowalk(decoded_filename,encoded_filename):
	'Decode autowalk.'
	with open(encoded_filename,_L)as E:
		B=E.read();A=0;C=[];F=int.from_bytes(B[0:2],byteorder=_C);A+=2
		for I in range(F):D=int.from_bytes(B[A:A+2],byteorder=_C);A+=2;G=readStructArray(B,A,D,autowalk_point_struct);A+=D*18;C.append(G)
		with open(decoded_filename,_M)as H:json.dump(C,H,indent=4,default=str)
def encodeAutowalk(decoded_filename,encoded_filename):
	'Encode autowalk.'
	with open(decoded_filename)as C:
		A=json.load(C)
		with open(encoded_filename,_N)as B:
			B.write(len(A).to_bytes(2,byteorder=_C))
			for D in A:writeStructArray(B,D,autowalk_point_struct,include_count=_R,count_bytes=2)
path_point_struct=[{_B:'unk0',_A:_D},{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'speed',_A:_F},{_B:'unk9',_A:_F}]
def decodePaths(decoded_filename,encoded_filename):
	'Decode paths.'
	with open(encoded_filename,_L)as G:
		B=G.read();E=[];H=int.from_bytes(B[0:2],byteorder=_C);A=2
		for J in range(H):
			C=B[A:A+6];D=int.from_bytes(C[2:4],byteorder=_C);F={'id':int.from_bytes(C[0:2],byteorder=_C),_e:int.from_bytes(C[4:6],byteorder=_C)};A+=6
			if D>0:F[_W]=readStructArray(B,A,D,path_point_struct);A+=D*10
			E.append(F)
		with open(decoded_filename,_M)as I:json.dump(E,I,indent=4,default=str)
def encodePaths(decoded_filename,encoded_filename):
	'Encode Paths.'
	with open(decoded_filename)as E:
		C=json.load(E)
		with open(encoded_filename,_N)as A:
			A.write(len(C).to_bytes(2,byteorder=_C))
			for B in C:
				D=len(B[_W])if _W in B else 0;A.write(int(B['id']).to_bytes(2,byteorder=_C));A.write(D.to_bytes(2,byteorder=_C));A.write(int(B[_e]).to_bytes(2,byteorder=_C))
				if D>0:writeStructArray(A,B[_W],path_point_struct)
checkpoint_struct=[{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'angle',_A:_D},{_B:'unk8',_A:float},{_B:'unkC',_A:float},{_B:'visibility',_A:_F},{_B:'unk11',_A:_F},{_B:'unk12',_A:_G},{_B:'unk14',_A:float},{_B:_d,_A:_G},{_B:'unk1A',_A:_G}]
def decodeCheckpoints(decoded_filename,encoded_filename):
	'Decode Checkpoints.'
	with open(encoded_filename,_L)as I:
		A=I.read();C=[];D=int.from_bytes(A[1:3],byteorder=_C);E=int.from_bytes(A[3:5],byteorder=_C)
		if D!=E:print(' - Error: Number of checkpoints does not match number of checkpoint mappings.');return 0
		F=5+E*2
		for B in range(D):
			G=int.from_bytes(A[5+B*2:7+B*2],byteorder=_C);H=readStruct(A,F,checkpoint_struct)
			if G!=B:H[_f]=G
			C.append(H);F+=28
		with open(decoded_filename,_M)as J:json.dump(C,J,indent=4,default=str)
def encodeCheckpoints(decoded_filename,encoded_filename):
	'Encode Checkpoints.'
	with open(decoded_filename)as D:
		B=json.load(D)
		with open(encoded_filename,_N)as A:
			A.write(bytes([1]));A.write(len(B).to_bytes(2,byteorder=_C));A.write(len(B).to_bytes(2,byteorder=_C))
			for (E,C) in enumerate(B):
				if _f in C:A.write(int(C[_f]).to_bytes(2,byteorder=_C))
				else:A.write(E.to_bytes(2,byteorder=_C))
			writeStructArray(A,B,checkpoint_struct)
character_spawner_point_0x6_struct=[{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D}]
character_spawner_point_0xA_struct=[{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'unk6',_A:bytes,_E:10-6}]
character_spawner_struct=[{_B:'enemy_val',_A:_F,_K:character_spawner_names},{_B:'unk1',_A:_F},{_B:'y_rot',_A:_G},{_B:_H,_A:_D},{_B:_I,_A:_D},{_B:_J,_A:_D},{_B:'cutscene_model',_A:_F,_K:cutscene_model_names},{_B:'unkB',_A:_F},{_B:'max_idle_speed',_A:_F},{_B:'max_aggro_speed',_A:_F},{_B:'unkE',_A:_F},{_B:_g,_A:_F},{_B:'aggro',_A:_F},{_B:_X,_A:_F},{_B:'initial_spawn_state',_A:_F},{_B:'spawn_trigger',_A:_F},{_B:'initial_respawn_timer',_A:_F},{_B:'unk15',_A:_F}]
def decodeCharacterSpawners(decoded_filename,encoded_filename):
	'Decode character Spawners.'
	with open(encoded_filename,_L)as K:
		B=K.read();A=0;D={};H=int.from_bytes(B[0:2],byteorder=_C);A+=2
		if H>0:
			D[_S]=[]
			for L in range(H):
				E={};F=int.from_bytes(B[A:A+2],byteorder=_C);A+=2
				if F>0:E[_T]=readStructArray(B,A,F,character_spawner_point_0x6_struct);A+=F*6
				G=int.from_bytes(B[A:A+2],byteorder=_C);A+=2
				if G>0:E[_U]=readStructArray(B,A,G,character_spawner_point_0xA_struct);A+=G*10
				E[_j]=B[A:A+4].hex(' ').upper();A+=4;D[_S].append(E)
		I=int.from_bytes(B[A:A+2],byteorder=_C);A+=2
		if I>0:
			D[_V]=[]
			for L in range(I):
				C=readStruct(B,A,character_spawner_struct);J=C[_X];del C[_X];A+=22
				if C['enemy_val_name']!='Cutscene Object':del C['cutscene_model_name']
				if J>0:
					C[_P]=[]
					for N in range(J):C[_P].append(int.from_bytes(B[A:A+2],byteorder=_C));A+=2
				D[_V].append(C)
		with open(decoded_filename,_M)as M:json.dump(D,M,indent=4,default=str)
def encodeCharacterSpawners(decoded_filename,encoded_filename):
	'Encode Character Spawners.'
	with open(decoded_filename)as G:
		C=json.load(G)
		with open(encoded_filename,_N)as A:
			E=len(C[_S])if _S in C else 0;A.write(E.to_bytes(2,byteorder=_C))
			if E>0:
				for B in C[_S]:
					H=len(B[_T])if _T in B else 0;A.write(H.to_bytes(2,byteorder=_C))
					if _T in B:writeStructArray(A,B[_T],character_spawner_point_0x6_struct)
					I=len(B[_U])if _U in B else 0;A.write(I.to_bytes(2,byteorder=_C))
					if _U in B:writeStructArray(A,B[_U],character_spawner_point_0xA_struct)
					A.write(bytes.fromhex(B[_j]))
			F=len(C[_V])if _V in C else 0;A.write(F.to_bytes(2,byteorder=_C))
			if F>0:
				for D in C[_V]:
					D[_X]=len(D[_P])if _P in D else 0;writeStruct(A,D,character_spawner_struct)
					if _P in D:
						for J in D[_P]:A.write(int(J).to_bytes(2,byteorder=_C))
setup_model2_struct=[{_B:_H,_A:float},{_B:_I,_A:float},{_B:_J,_A:float},{_B:_g,_A:float},{_B:_h,_A:bytes,_E:24-16},{_B:'angle18',_A:float},{_B:'angle1C',_A:float},{_B:'angle20',_A:float},{_B:'unk24',_A:float},{_B:_k,_A:_D,_K:model2_names},{_B:'unk2A',_A:bytes,_E:48-42}]
setup_conveyor_data_struct=[{_B:_Y,_A:int,_E:4},{_B:_e,_A:float},{_B:'unk8',_A:float},{_B:'unkC',_A:float},{_B:_h,_A:float},{_B:'unk14',_A:float},{_B:_d,_A:float},{_B:'unk1C',_A:float},{_B:'unk20',_A:float}]
setup_actor_spawner_struct=[{_B:_H,_A:float},{_B:_I,_A:float},{_B:_J,_A:float},{_B:_g,_A:float},{_B:_h,_A:bytes,_E:50-16},{_B:_k,_A:_G,_K:actor_names,_c:16},{_B:'unk34',_A:bytes,_E:56-52}]
def decodeSetup(decoded_filename,encoded_filename):
	'Decode Setup.'
	with open(encoded_filename,_L)as H:
		B=H.read();A=0;C={};D=int.from_bytes(B[A:A+4],byteorder=_C);A+=4
		if D>0:C[_Q]=readStructArray(B,A,D,setup_model2_struct);A+=D*48
		G=int.from_bytes(B[A:A+4],byteorder=_C);A+=4
		if G>0:
			for K in range(G):E=readStruct(B,A,setup_conveyor_data_struct);I=E[_Y];del E[_Y];C[_Q][I][_Z]=E;A+=36
		F=int.from_bytes(B[A:A+4],byteorder=_C);A+=4
		if F>0:C[_a]=readStructArray(B,A,F,setup_actor_spawner_struct);A+=F*56
		with open(decoded_filename,_M)as J:json.dump(C,J,indent=4,default=str)
def encodeSetup(decoded_filename,encoded_filename):
	'Encode Setup.'
	with open(decoded_filename)as I:
		A=json.load(I)
		with open(encoded_filename,_N)as B:
			D=0;E=len(A[_Q])if _Q in A else 0;F=len(A[_a])if _a in A else 0;B.write(E.to_bytes(4,byteorder=_C))
			if E>0:
				for (G,C) in enumerate(A[_Q]):
					writeStruct(B,C,setup_model2_struct)
					if _Z in C:D+=1
			B.write(D.to_bytes(4,byteorder=_C))
			if D>0:
				for (G,C) in enumerate(A[_Q]):
					if _Z in C:H=C[_Z];H[_Y]=G;writeStruct(B,H,setup_conveyor_data_struct)
			B.write(F.to_bytes(4,byteorder=_C))
			if F>0:writeStructArray(B,A[_a],setup_actor_spawner_struct)