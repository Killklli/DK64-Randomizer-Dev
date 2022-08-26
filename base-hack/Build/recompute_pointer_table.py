'Recompute all the pointers within the rom.'
_X='Textures'
_W='do_not_compress'
_V='filename'
_U=False
_T='uncompressed_size'
_S='sha1'
_R='original_compressed_size'
_Q='original_sha1'
_P='bit_set'
_O='decoder'
_N='encoder'
_M='data'
_L='absolute_address'
_K='new_sha1'
_J='num_entries'
_I='dont_overwrite_uncompressed_sizes'
_H='decoded_filename'
_G='encoded_filename'
_F=True
_E='new_absolute_address'
_D='big'
_C='entries'
_B='name'
_A='index'
import hashlib,json
from typing import BinaryIO
import encoders
from map_names import maps
pointer_tables=[{_A:0,_B:'Music MIDI'},{_A:1,_B:'Map Geometry',_G:'geometry.bin',_H:'geometry.todo'},{_A:2,_B:'Map Walls',_G:'walls.bin',_H:'walls.obj',_I:_F},{_A:3,_B:'Map Floors',_G:'floors.bin',_H:'floors.obj',_I:_F},{_A:4,_B:'Object Model 2 Geometry'},{_A:5,_B:'Actor Geometry'},{_A:6,_B:'Unknown 6',_I:_F},{_A:7,_B:'Textures (Uncompressed)',_I:_F},{_A:8,_B:'Map Cutscenes',_G:'cutscenes.bin',_H:'cutscenes.todo'},{_A:9,_B:'Map Object Setups',_G:'setup.bin',_H:'setup.json',_N:encoders.encodeSetup,_O:encoders.decodeSetup},{_A:10,_B:'Map Object Model 2 Behaviour Scripts',_G:'object_behaviour_scripts.bin',_H:'object_behaviour_scripts.todo'},{_A:11,_B:'Animations',_I:_F},{_A:12,_B:'Text'},{_A:13,_B:'Unknown 13'},{_A:14,_B:_X},{_A:15,_B:'Map Paths',_G:'paths.bin',_H:'paths.json',_N:encoders.encodePaths,_O:encoders.decodePaths,_W:_F,_I:_F},{_A:16,_B:'Map Character Spawners',_G:'character_spawners.bin',_H:'character_spawners.json',_N:encoders.encodeCharacterSpawners,_O:encoders.decodeCharacterSpawners},{_A:17,_B:'DKTV Inputs'},{_A:18,_B:'Map Loading Zones',_G:'loading_zones.bin',_H:'loading_zones.json',_N:encoders.encodeLoadingZones,_O:encoders.decodeLoadingZones},{_A:19,_B:'Unknown 19'},{_A:20,_B:'Unknown 20',_I:_F},{_A:21,_B:'Map Autowalk Data',_G:'autowalk.bin',_H:'autowalk.json',_N:encoders.encodeAutowalk,_O:encoders.decodeAutowalk,_W:_F,_I:_F},{_A:22,_B:'Unknown 22'},{_A:23,_B:'Map Exits',_G:'exits.bin',_H:'exits.json',_W:_F,_I:_F,_N:encoders.encodeExits,_O:encoders.decodeExits},{_A:24,_B:'Map Race Checkpoints',_G:'race_checkpoints.bin',_H:'race_checkpoints.json',_N:encoders.encodeCheckpoints,_O:encoders.decodeCheckpoints},{_A:25,_B:_X},{_A:26,_B:'Uncompressed File Sizes',_I:_F},{_A:27,_B:'Unknown 27'},{_A:28,_B:'Unknown 28'},{_A:29,_B:'Unknown 29'},{_A:30,_B:'Unknown 30'},{_A:31,_B:'Unknown 31'}]
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
	if _I in pointer_tables[A]:return 0
	B=pointer_tables[26][_C][A][_L]+file_index*4;fh.seek(B);return int.from_bytes(fh.read(4),_D)
def writeUncompressedSize(fh,pointer_table_index,file_index,uncompressed_size):
	'Write to the uncompressed size.';D=file_index;C=pointer_table_index;B=uncompressed_size;A=fh
	if _I in pointer_tables[C]:return 0
	A.seek(main_pointer_table_offset+26*4);F=main_pointer_table_offset+int.from_bytes(A.read(4),_D);A.seek(F+C*4);E=main_pointer_table_offset+int.from_bytes(A.read(4),_D)+D*4
	if B%2==1:B+=1
	print(' - Writing new uncompressed size '+hex(B)+' for file '+str(C)+'->'+str(D)+' to ROM address '+hex(E));A.seek(E);A.write(int.to_bytes(B,4,_D))
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
	for A in pointer_tables:D=int.from_bytes(B.read(4),_D)+main_pointer_table_offset;A[_L]=D;A[_E]=D
	B.seek(main_pointer_table_offset+num_tables*4)
	for A in pointer_tables:A[_J]=int.from_bytes(B.read(4),_D);A[_R]=0;A[_C]=[]
	for A in pointer_tables:
		if A[_J]>0:
			for F in range(A[_J]):B.seek(A[_L]+F*4);H=int.from_bytes(B.read(4),_D);D=(H&2147483647)+main_pointer_table_offset;J=(int.from_bytes(B.read(4),_D)&2147483647)+main_pointer_table_offset;A[_C].append({_A:F,'pointer_address':hex(A[_L]+F*4),_L:D,_E:D,I:J,_P:H&2147483648>0,_Q:'',_K:''})
	for A in pointer_tables:
		if A[_J]>0:
			for C in A[_C]:
				if not C[_P]:
					G=C[I]-C[_L]
					if G>0:E=addFileToDatabase(B,C[_L],G,A[_A],C[_A]);A[_R]+=G
	for A in pointer_tables:
		if A[_J]>0:
			for C in A[_C]:
				if C[_P]:
					B.seek(C[_L]);K=int.from_bytes(B.read(2),_D);E=getFileInfo(A[_A],K)
					if E:C[_Q]=E[_S];C[_K]=E[_S]
def addFileToDatabase(fh,absolute_address,absolute_size,pointer_table_index,file_index):
	'Add the files to the database.';D=file_index;C=absolute_address;A=pointer_table_index
	for E in pointer_tables:
		if E[_L]==C:print('WARNING: POINTER TABLE '+str(E[_A])+' BEING USED AS FILE!');return
	fh.seek(C);F=fh.read(absolute_size);B=hashlib.sha1(F).hexdigest();pointer_tables[A][_C][D][_Q]=B;pointer_tables[A][_C][D][_K]=B;pointer_table_files[A][B]={_E:C,_M:F,_S:B,_T:getOriginalUncompressedSize(fh,A,D)};return pointer_table_files[A][B]
def getFileInfo(pointer_table_index,file_index):
	'Get the files info.';B=file_index;A=pointer_table_index
	if A not in range(len(pointer_tables)):return
	if B not in range(len(pointer_tables[A][_C])):return
	if not pointer_tables[A][_C][B][_K]in pointer_table_files[A]:return
	return pointer_table_files[A][pointer_tables[A][_C][B][_K]]
def replaceROMFile(rom,pointer_table_index,file_index,data,uncompressed_size,filename=''):
	'Replace the ROM file.';H=filename;D=data;C=rom;B=file_index;A=pointer_table_index
	if A==8 and B==0:print(' - WARNING: Tried to replace Test Map cutscenes. This will replace global cutscenes, so it has been disabled for now to prevent crashes.');return
	if len(D)%2==1:I=bytearray(D);I.append(0);D=bytes(I)
	F=hashlib.sha1(D).hexdigest();pointer_table_files[A][F]={_M:D,_S:F,_T:uncompressed_size}
	if B>=len(pointer_tables[A][_C]):
		G=B-len(pointer_tables[A][_C])+1;print(f" - Appending {G} extra entries to {pointer_tables[A][_B]} ({B+1-G}->{B+1})")
		for L in range(G):pointer_tables[A][_C].append({_A:B,_P:_U,_Q:''})
		C.seek(main_pointer_table_offset+4*len(pointer_tables)+4*A);C.write((B+1).to_bytes(4,_D));pointer_tables[A][_J]=B+1;C.seek(main_pointer_table_offset+4*26);M=main_pointer_table_offset+int.from_bytes(C.read(4),_D);C.seek(M+4*A);J=main_pointer_table_offset+int.from_bytes(C.read(4),_D);N=main_pointer_table_offset+int.from_bytes(C.read(4),_D);E=N-J
		if E>0:
			print(f" - Expanding pointer table {A} from {E} bytes to {4*(B+1)} bytes");C.seek(J);K=bytearray(C.read(E))
			for L in range(4*(B+1)-E):K.append(0)
			replaceROMFile(C,26,A,bytes(K),4*(B+1))
	pointer_tables[A][_C][B][_K]=F
	if len(H)>0:pointer_tables[A][_C][B][_V]=H
def shouldWritePointerTable(index):
	'Write to the pointer table.';A=index
	if A==6:return _U
	if pointer_tables[A][_J]==0:return _U
	if A in force_table_rewrite:return _F
	if pointer_tables[A]:
		for B in pointer_tables[A][_C]:
			if B[_Q]!=B[_K]:return _F
	return _U
def shouldRelocatePointerTable(index):
	'Relocate the pointer table.';A=index
	if A in[1,2,3,10]:return _F
	return getPointerTableCompressedSize(A)>pointer_tables[A][_R]
def writeModifiedPointerTablesToROM(fh):
	'Write the modified pointer tables to the rom file.';C=fh;global next_available_free_space
	for A in pointer_tables:
		if not shouldWritePointerTable(A[_A]):continue
		I=A[_J]*4+4;J=shouldRelocatePointerTable(A[_A])
		if J:A[_E]=next_available_free_space
		F=A[_E]+I;H=F
		for B in A[_C]:
			D=getFileInfo(A[_A],B[_A]);B[_E]=F
			if D:
				if len(D[_M])>0:F+=len(D[_M]);C.seek(B[_E]);C.write(D[_M])
		if J:next_available_free_space+=I;next_available_free_space+=F-H
	for A in reversed(pointer_tables):
		C.seek(main_pointer_table_offset+26*4);print(f"Pointer Table {A[_A]}. New Location: {hex(main_pointer_table_offset+int.from_bytes(C.read(4),_D))}. Write Location:")
		if not shouldWritePointerTable(A[_A]):continue
		E=0;G=0
		for B in A[_C]:
			D=getFileInfo(A[_A],B[_A])
			if D:
				E=B[_E]-main_pointer_table_offset;G=B[_E]+len(D[_M])-main_pointer_table_offset
				if B[_Q]!=B[_K]:writeUncompressedSize(C,A[_A],B[_A],D[_T])
			else:E=G
			if E==0:E=H-main_pointer_table_offset;G=H-main_pointer_table_offset
			C.seek(A[_E]+B[_A]*4);C.write(E.to_bytes(4,_D));C.write(G.to_bytes(4,_D))
		C.seek(main_pointer_table_offset+A[_A]*4);C.write((A[_E]-main_pointer_table_offset).to_bytes(4,_D))
dataset=[]
def dumpPointerTableDetails(filename,fr):
	'Dump the pointer table info into a JSON readable pointer table.';C=None;print('Dumping Pointer Table Details to '+filename)
	for A in pointer_tables:
		D=[]
		for B in A[_C]:fr.seek(A[_E]+B[_A]*4);G=(int.from_bytes(fr.read(4),_D)&2147483647)+main_pointer_table_offset;E=getFileInfo(A[_A],B[_A]);F=getOriginalUncompressedSize(fr,A[_A],B[_A]);H={_A:int(len(D)),'new_address':int(A[_E]+B[_A]*4),'pointing_to':int(G),'compressed_size':int(len(E[_M]))if E else C,_T:int(F)if F>0 else C,_P:B[_P],'map_index':maps[B[_A]]if A[_J]==221 else C,'file_name':B.get(_V,C),'sha':B[_K]};D.insert(B[_A],H)
		I={_B:A[_B],'address':int(A[_E]),'total_entries':int(A[_J]),'starting_byte':int(A[_R]),'ending_byte':int(getPointerTableCompressedSize(A[_A])),_C:D};dataset.insert(A[_A],I)
	with open('../static/patches/pointer_addresses.json','w')as J:J.write(json.dumps(dataset))
def dumpPointerTableDetailsLegacy(filename,fr):
	'Dump the table details in the legacy log format.';I=' -> ';F=': ';E=')';D=' ('
	with open(filename,'w')as A:
		for B in pointer_tables:
			A.write(str(B[_A])+F+B[_B]+F+hex(B[_E])+D+str(B[_J])+' entries, '+hex(B[_R])+I+hex(getPointerTableCompressedSize(B[_A]))+' bytes)');A.write('\n')
			for C in B[_C]:
				A.write(' - '+str(C[_A])+F);A.write(hex(B[_E]+C[_A]*4)+I);fr.seek(B[_E]+C[_A]*4);J=(int.from_bytes(fr.read(4),_D)&2147483647)+main_pointer_table_offset;A.write(hex(J));G=getFileInfo(B[_A],C[_A])
				if G:A.write(D+hex(len(G[_M]))+E)
				else:A.write(' WARNING: File info not found')
				H=getOriginalUncompressedSize(fr,B[_A],C[_A])
				if H>0:A.write(D+hex(H)+E)
				A.write(D+str(C[_P])+E)
				if B[_J]==221:A.write(D+maps[C[_A]]+E)
				A.write(D+str(C[_K])+E)
				if _V in C:A.write(D+str(C[_V])+E)
				A.write('\n')