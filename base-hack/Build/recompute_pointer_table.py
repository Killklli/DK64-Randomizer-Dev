'Recompute all the pointers within the rom.'
_W='Textures'
_V='do_not_compress'
_U='filename'
_T='uncompressed_size'
_S='sha1'
_R='original_sha1'
_Q='original_compressed_size'
_P='bit_set'
_O='decoder'
_N='encoder'
_M='data'
_L='new_sha1'
_K='absolute_address'
_J='num_entries'
_I='big'
_H='dont_overwrite_uncompressed_sizes'
_G='decoded_filename'
_F='encoded_filename'
_E=True
_D='new_absolute_address'
_C='entries'
_B='name'
_A='index'
import hashlib,json
from typing import BinaryIO
import encoders
from map_names import maps
pointer_tables=[{_A:0,_B:'Music MIDI'},{_A:1,_B:'Map Geometry',_F:'geometry.bin',_G:'geometry.todo'},{_A:2,_B:'Map Walls',_F:'walls.bin',_G:'walls.obj',_H:_E},{_A:3,_B:'Map Floors',_F:'floors.bin',_G:'floors.obj',_H:_E},{_A:4,_B:'Object Model 2 Geometry'},{_A:5,_B:'Actor Geometry'},{_A:6,_B:'Unknown 6',_H:_E},{_A:7,_B:'Textures (Uncompressed)',_H:_E},{_A:8,_B:'Map Cutscenes',_F:'cutscenes.bin',_G:'cutscenes.todo'},{_A:9,_B:'Map Object Setups',_F:'setup.bin',_G:'setup.json',_N:encoders.encodeSetup,_O:encoders.decodeSetup},{_A:10,_B:'Map Object Model 2 Behaviour Scripts',_F:'object_behaviour_scripts.bin',_G:'object_behaviour_scripts.todo'},{_A:11,_B:'Animations',_H:_E},{_A:12,_B:'Text'},{_A:13,_B:'Unknown 13'},{_A:14,_B:_W},{_A:15,_B:'Map Paths',_F:'paths.bin',_G:'paths.json',_N:encoders.encodePaths,_O:encoders.decodePaths,_V:_E,_H:_E},{_A:16,_B:'Map Character Spawners',_F:'character_spawners.bin',_G:'character_spawners.json',_N:encoders.encodeCharacterSpawners,_O:encoders.decodeCharacterSpawners},{_A:17,_B:'DKTV Inputs'},{_A:18,_B:'Map Loading Zones',_F:'loading_zones.bin',_G:'loading_zones.json',_N:encoders.encodeLoadingZones,_O:encoders.decodeLoadingZones},{_A:19,_B:'Unknown 19'},{_A:20,_B:'Unknown 20',_H:_E},{_A:21,_B:'Map Autowalk Data',_F:'autowalk.bin',_G:'autowalk.json',_N:encoders.encodeAutowalk,_O:encoders.decodeAutowalk,_V:_E,_H:_E},{_A:22,_B:'Unknown 22'},{_A:23,_B:'Map Exits',_F:'exits.bin',_G:'exits.json',_V:_E,_H:_E,_N:encoders.encodeExits,_O:encoders.decodeExits},{_A:24,_B:'Map Race Checkpoints',_F:'race_checkpoints.bin',_G:'race_checkpoints.json',_N:encoders.encodeCheckpoints,_O:encoders.decodeCheckpoints},{_A:25,_B:_W},{_A:26,_B:'Uncompressed File Sizes',_H:_E},{_A:27,_B:'Unknown 27'},{_A:28,_B:'Unknown 28'},{_A:29,_B:'Unknown 29'},{_A:30,_B:'Unknown 30'},{_A:31,_B:'Unknown 31'}]
num_tables=len(pointer_tables)
main_pointer_table_offset=1055824
next_available_free_space=33751040
pointer_table_files=[]
for x in pointer_tables:pointer_table_files.append({})
force_table_rewrite=[]
def make_safe_filename(s):
	'Make the file name safe without _.'
	def A(c):
		if c.isalnum():return c
		else:return'_'
	return ''.join((A(B)for B in s)).rstrip('_')
def getOriginalUncompressedSize(fh,pointer_table_index,file_index):
	'Get the orignal uncompressed size.';A=pointer_table_index
	if _H in pointer_tables[A]:return 0
	B=pointer_tables[26][_C][A][_K]+file_index*4;fh.seek(B);return int.from_bytes(fh.read(4),_I)
def writeUncompressedSize(fh,pointer_table_index,file_index,uncompressed_size):
	'Write to the uncompressed size.';C=file_index;B=pointer_table_index;A=uncompressed_size
	if _H in pointer_tables[B]:return 0
	D=pointer_tables[26][_C][B][_K]+C*4
	if A%2==1:A+=1
	print(' - Writing new uncompressed size '+hex(A)+' for file '+str(B)+'->'+str(C)+' to ROM address '+hex(D));fh.seek(D);fh.write(int.to_bytes(A,4,_I))
def getPointerTableCompressedSize(pointer_table_index):
	'Get the tables compressed size.';A=pointer_table_index;B=0
	if A<len(pointer_tables):
		D=pointer_tables[A]
		for E in D[_C]:
			C=getFileInfo(A,E[_A])
			if C:B+=len(C[_M])
	return B
def parsePointerTables(fh):
	'Parse the pointer tables.';I='next_absolute_address';B=fh;B.seek(main_pointer_table_offset)
	for A in pointer_tables:D=int.from_bytes(B.read(4),_I)+main_pointer_table_offset;A[_K]=D;A[_D]=D
	B.seek(main_pointer_table_offset+num_tables*4)
	for A in pointer_tables:A[_J]=int.from_bytes(B.read(4),_I);A[_Q]=0;A[_C]=[]
	for A in pointer_tables:
		if A[_J]>0:
			for F in range(A[_J]):B.seek(A[_K]+F*4);H=int.from_bytes(B.read(4),_I);D=(H&2147483647)+main_pointer_table_offset;J=(int.from_bytes(B.read(4),_I)&2147483647)+main_pointer_table_offset;A[_C].append({_A:F,'pointer_address':hex(A[_K]+F*4),_K:D,_D:D,I:J,_P:H&2147483648>0,_R:'',_L:''})
	for A in pointer_tables:
		if A[_J]>0:
			for C in A[_C]:
				if not C[_P]:
					G=C[I]-C[_K]
					if G>0:E=addFileToDatabase(B,C[_K],G,A[_A],C[_A]);A[_Q]+=G
	for A in pointer_tables:
		if A[_J]>0:
			for C in A[_C]:
				if C[_P]:
					B.seek(C[_K]);K=int.from_bytes(B.read(2),_I);E=getFileInfo(A[_A],K)
					if E:C[_R]=E[_S];C[_L]=E[_S]
def addFileToDatabase(fh,absolute_address,absolute_size,pointer_table_index,file_index):
	'Add the files to the database.';D=file_index;C=absolute_address;A=pointer_table_index
	for E in pointer_tables:
		if E[_K]==C:print('WARNING: POINTER TABLE '+str(E[_A])+' BEING USED AS FILE!');return
	fh.seek(C);F=fh.read(absolute_size);B=hashlib.sha1(F).hexdigest();pointer_tables[A][_C][D][_R]=B;pointer_tables[A][_C][D][_L]=B;pointer_table_files[A][B]={_D:C,_M:F,_S:B,_T:getOriginalUncompressedSize(fh,A,D)};return pointer_table_files[A][B]
def getFileInfo(pointer_table_index,file_index):
	'Get the files info.';B=file_index;A=pointer_table_index
	if A not in range(len(pointer_tables)):return
	if B not in range(len(pointer_tables[A][_C])):return
	if not pointer_tables[A][_C][B][_L]in pointer_table_files[A]:return
	return pointer_table_files[A][pointer_tables[A][_C][B][_L]]
def replaceROMFile(pointer_table_index,file_index,data,uncompressed_size,filename=''):
	'Replace the ROM file.';E=filename;C=file_index;B=pointer_table_index;A=data
	if B==8 and C==0:print(' - WARNING: Tried to replace Test Map cutscenes. This will replace global cutscenes, so it has been disabled for now to prevent crashes.');return
	if len(A)%2==1:F=bytearray(A);F.append(0);A=bytes(F)
	D=hashlib.sha1(A).hexdigest();pointer_table_files[B][D]={_M:A,_S:D,_T:uncompressed_size};pointer_tables[B][_C][C][_L]=D
	if len(E)>0:pointer_tables[B][_C][C][_U]=E
def shouldWritePointerTable(index):
	'Write to the pointer table.';B=False;A=index
	if A in[6,26]:return B
	if pointer_tables[A][_J]==0:return B
	if A in force_table_rewrite:return _E
	if pointer_tables[A]:
		for C in pointer_tables[A][_C]:
			if C[_R]!=C[_L]:return _E
	return B
def shouldRelocatePointerTable(index):
	'Relocate the pointer table.';A=index
	if A in[1,2,3,10]:return _E
	return getPointerTableCompressedSize(A)>pointer_tables[A][_Q]
def writeModifiedPointerTablesToROM(fh):
	'Write the modified pointer tables to the rom file.';C=fh;global next_available_free_space
	for A in pointer_tables:
		if not shouldWritePointerTable(A[_A]):continue
		I=A[_J]*4+4;J=shouldRelocatePointerTable(A[_A])
		if J:A[_D]=next_available_free_space
		F=A[_D]+I;H=F
		for B in A[_C]:
			D=getFileInfo(A[_A],B[_A]);B[_D]=F
			if D:
				if len(D[_M])>0:F+=len(D[_M]);C.seek(B[_D]);C.write(D[_M])
		if J:next_available_free_space+=I;next_available_free_space+=F-H
	for A in pointer_tables:
		if not shouldWritePointerTable(A[_A]):continue
		E=0;G=0
		for B in A[_C]:
			D=getFileInfo(A[_A],B[_A])
			if D:
				E=B[_D]-main_pointer_table_offset;G=B[_D]+len(D[_M])-main_pointer_table_offset
				if B[_R]!=B[_L]:writeUncompressedSize(C,A[_A],B[_A],D[_T])
			else:E=G
			if E==0:E=H-main_pointer_table_offset;G=H-main_pointer_table_offset
			C.seek(A[_D]+B[_A]*4);C.write(E.to_bytes(4,_I));C.write(G.to_bytes(4,_I))
		C.seek(main_pointer_table_offset+A[_A]*4);C.write((A[_D]-main_pointer_table_offset).to_bytes(4,_I))
dataset=[]
def dumpPointerTableDetails(filename,fr):
	'Dump the pointer table info into a JSON readable pointer table.';C=None;print('Dumping Pointer Table Details to '+filename)
	for A in pointer_tables:
		D=[]
		for B in A[_C]:fr.seek(A[_D]+B[_A]*4);G=(int.from_bytes(fr.read(4),_I)&2147483647)+main_pointer_table_offset;E=getFileInfo(A[_A],B[_A]);F=getOriginalUncompressedSize(fr,A[_A],B[_A]);H={_A:int(len(D)),'new_address':int(A[_D]+B[_A]*4),'pointing_to':int(G),'compressed_size':int(len(E[_M]))if E else C,_T:int(F)if F>0 else C,_P:B[_P],'map_index':maps[B[_A]]if A[_J]==221 else C,'file_name':B.get(_U,C),'sha':B[_L]};D.insert(B[_A],H)
		I={_B:A[_B],'address':int(A[_D]),'total_entries':int(A[_J]),'starting_byte':int(A[_Q]),'ending_byte':int(getPointerTableCompressedSize(A[_A])),_C:D};dataset.insert(A[_A],I)
	with open('../static/patches/pointer_addresses.json','w')as J:J.write(json.dumps(dataset))
def dumpPointerTableDetailsLegacy(filename,fr):
	'Dump the table details in the legacy log format.';I=' -> ';F=': ';E=')';D=' ('
	with open(filename,'w')as A:
		for B in pointer_tables:
			A.write(str(B[_A])+F+B[_B]+F+hex(B[_D])+D+str(B[_J])+' entries, '+hex(B[_Q])+I+hex(getPointerTableCompressedSize(B[_A]))+' bytes)');A.write('\n')
			for C in B[_C]:
				A.write(' - '+str(C[_A])+F);A.write(hex(B[_D]+C[_A]*4)+I);fr.seek(B[_D]+C[_A]*4);J=(int.from_bytes(fr.read(4),_I)&2147483647)+main_pointer_table_offset;A.write(hex(J));G=getFileInfo(B[_A],C[_A])
				if G:A.write(D+hex(len(G[_M]))+E)
				else:A.write(' WARNING: File info not found')
				H=getOriginalUncompressedSize(fr,B[_A],C[_A])
				if H>0:A.write(D+hex(H)+E)
				A.write(D+str(C[_P])+E)
				if B[_J]==221:A.write(D+maps[C[_A]]+E)
				A.write(D+str(C[_L])+E)
				if _U in C:A.write(D+str(C[_U])+E)
				A.write('\n')