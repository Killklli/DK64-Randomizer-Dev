'Build the ROM.'
_n='do_not_delete_output'
_m='do_not_delete'
_l=') to ROM'
_k='use_zlib'
_j='.rgba32'
_i='assets/Non-Code/credits'
_h='decoded_filename'
_g='encoder'
_f=False
_e='ia4'
_d='compressed_size'
_c='.png'
_b='patcher'
_a='do_not_extract'
_Z='rb'
_Y='target_uncompressed_size'
_X='do_not_recompress'
_W='.bin'
_V='index'
_U='encoded_filename'
_T='do_not_delete_source'
_S='start'
_R='coins'
_Q='offset'
_P='map_folder'
_O='do_not_compress'
_N='rgba32'
_M='target_compressed_size'
_L='use_external_gzip'
_K='big'
_J='rgba5551'
_I='output_file'
_H='bps_file'
_G='is_diff_patch'
_F='texture_format'
_E=True
_D='file_index'
_C='pointer_table_index'
_B='name'
_A='source_file'
import gzip,os,shutil,subprocess,zlib,generate_watch_file,patch_text
from adjust_exits import adjustExits
from convertPortalImage import convertPortalImage
from convertSetup import convertSetup
from map_names import maps
from populateSongData import writeVanillaSongData
from recompute_overlays import isROMAddressOverlay,readOverlayOriginalData,replaceOverlayData,writeModifiedOverlaysToROM
from recompute_pointer_table import dumpPointerTableDetails,getFileInfo,make_safe_filename,parsePointerTables,pointer_tables,replaceROMFile,writeModifiedPointerTablesToROM
from replace_simslam_text import replaceSimSlam
from staticcode import patchStaticCode
from vanilla_move_data import writeVanillaMoveData
from image_converter import convertToRGBA32
from end_seq_writer import createTextFile,createSquishFile
ROMName='rom/dk64.z64'
newROMName='rom/dk64-randomizer-base.z64'
if os.path.exists(newROMName):os.remove(newROMName)
shutil.copyfile(ROMName,newROMName)
portal_images=[]
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_1.png'))
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_2.png'))
createTextFile(_i)
createSquishFile(_i)
file_dict=[{_B:'Static ASM Code',_S:70640,_d:726500,_A:'StaticCode.bin',_L:_E,_b:patchStaticCode},{_B:'Dolby Logo',_C:14,_D:176,_A:'assets/Non-Code/Dolby/DolbyThin.png',_F:_e},{_B:'Thumb Image',_C:14,_D:94,_A:'assets/Non-Code/Nintendo Logo/Nintendo.png',_F:_J},{_B:'DKTV Image',_C:14,_D:44,_A:'assets/Non-Code/DKTV/logo3.png',_F:_J},{_B:'Spin Transition Image',_C:14,_D:95,_A:'assets/Non-Code/transition/transition-body.png',_F:_e},{_B:'Moves Image',_C:14,_D:115,_A:'assets/Non-Code/file_screen/moves.png',_F:_J},{_B:'Blueprint Image',_C:14,_D:116,_A:'assets/Non-Code/file_screen/blueprint.png',_F:_J},{_B:'Isles Object Instance Scripts',_C:10,_D:34,_A:'assets/Non-Code/instance_scripts/isles.bin',_H:'assets/Non-Code/instance_scripts/isles.bps',_G:_E},{_B:'Helm Object Instance Scripts',_C:10,_D:17,_A:'assets/Non-Code/instance_scripts/helm.bin',_H:'assets/Non-Code/instance_scripts/helm.bps',_G:_E},{_B:'Galleon Object Instance Scripts',_C:10,_D:30,_A:'assets/Non-Code/instance_scripts/galleon.bin',_H:'assets/Non-Code/instance_scripts/galleon.bps',_G:_E},{_B:'Aztec Object Instance Scripts',_C:10,_D:38,_A:'assets/Non-Code/instance_scripts/aztec.bin',_H:'assets/Non-Code/instance_scripts/aztec.bps',_G:_E},{_B:'Fungi Object Instance Scripts',_C:10,_D:48,_A:'assets/Non-Code/instance_scripts/fungi.bin',_H:'assets/Non-Code/instance_scripts/fungi.bps',_G:_E},{_B:'Chunky Phase Object Instance Scripts',_C:10,_D:207,_A:'assets/Non-Code/instance_scripts/chunky_phase.bin',_H:'assets/Non-Code/instance_scripts/chunky_phase.bps',_G:_E},{_B:'Diddy 5DC Upper Object Instance Scripts',_C:10,_D:200,_A:'assets/Non-Code/instance_scripts/diddy_5dc_upper.bin',_H:'assets/Non-Code/instance_scripts/diddy_5dc_upper.bps',_G:_E},{_B:'Dungeon Object Instance Scripts',_C:10,_D:163,_A:'assets/Non-Code/instance_scripts/dungeon.bin',_H:'assets/Non-Code/instance_scripts/dungeon.bps',_G:_E},{_B:'Wind Tower Object Instance Scripts',_C:10,_D:105,_A:'assets/Non-Code/instance_scripts/wind_tower.bin',_H:'assets/Non-Code/instance_scripts/wind_tower.bps',_G:_E},{_B:'Ballroom Object Instance Scripts',_C:10,_D:88,_A:'assets/Non-Code/instance_scripts/ballroom.bin',_H:'assets/Non-Code/instance_scripts/ballroom.bps',_G:_E},{_B:'Museum Object Instance Scripts',_C:10,_D:113,_A:'assets/Non-Code/instance_scripts/museum.bin',_H:'assets/Non-Code/instance_scripts/museum.bps',_G:_E},{_B:'Llama Temple Instance Scripts',_C:10,_D:20,_A:'assets/Non-Code/instance_scripts/llama_temple.bin',_H:'assets/Non-Code/instance_scripts/llama_temple.bps',_G:_E},{_B:'Jungle Japes Instance Scripts',_C:10,_D:7,_A:'assets/Non-Code/instance_scripts/japes.bin',_H:'assets/Non-Code/instance_scripts/japes.bps',_G:_E},{_B:'Mountain Instance Scripts',_C:10,_D:4,_A:'assets/Non-Code/instance_scripts/japes_mountain.bin',_H:'assets/Non-Code/instance_scripts/japes_mountain.bps',_G:_E},{_B:'Frantic Factory Instance Scripts',_C:10,_D:26,_A:'assets/Non-Code/instance_scripts/factory.bin',_H:'assets/Non-Code/instance_scripts/factory.bps',_G:_E},{_B:'Mill Front Instance Scripts',_C:10,_D:61,_A:'assets/Non-Code/instance_scripts/mill_front.bin',_H:'assets/Non-Code/instance_scripts/mill_front.bps',_G:_E},{_B:'Mill Rear Instance Scripts',_C:10,_D:62,_A:'assets/Non-Code/instance_scripts/mill_rear.bin',_H:'assets/Non-Code/instance_scripts/mill_rear.bps',_G:_E},{_B:'Giant Mushroom Instance Scripts',_C:10,_D:64,_A:'assets/Non-Code/instance_scripts/giant_mushroom.bin',_H:'assets/Non-Code/instance_scripts/giant_mushroom.bps',_G:_E},{_B:'Crystal Caves Instance Scripts',_C:10,_D:72,_A:'assets/Non-Code/instance_scripts/caves.bin',_H:'assets/Non-Code/instance_scripts/caves.bps',_G:_E},{_B:'Training Grounds Instance Scripts',_C:10,_D:176,_A:'assets/Non-Code/instance_scripts/tgrounds.bin',_H:'assets/Non-Code/instance_scripts/tgrounds.bps',_G:_E},{_B:'Tiny Temple Instance Scripts',_C:10,_D:16,_A:'assets/Non-Code/instance_scripts/tiny_temple.bin',_H:'assets/Non-Code/instance_scripts/tiny_temple.bps',_G:_E},{_B:'Tag Barrel Shell Texture',_C:25,_D:4938,_A:'assets/Non-Code/tagbarrel/shell.png',_F:_J},{_B:'Gong Geometry',_C:4,_D:195,_A:'assets/Non-Code/Gong/gong_geometry.bin',_H:'assets/Non-Code/Gong/gong_geometry.bps',_G:_E},{_B:'No Face',_C:14,_D:33,_A:'assets/Non-Code/displays/none.png',_F:_N},{_B:'DK Face',_C:14,_D:34,_A:'assets/Non-Code/displays/dk_face.png',_F:_N},{_B:'Diddy Face',_C:14,_D:35,_A:'assets/Non-Code/displays/diddy_face.png',_F:_N},{_B:'Lanky Face',_C:14,_D:36,_A:'assets/Non-Code/displays/lanky_face.png',_F:_N},{_B:'Tiny Face',_C:14,_D:37,_A:'assets/Non-Code/displays/tiny_face.png',_F:_N},{_B:'Chunky Face',_C:14,_D:38,_A:'assets/Non-Code/displays/chunky_face.png',_F:_N},{_B:'Shared Face',_C:14,_D:39,_A:'assets/Non-Code/displays/shared.png',_F:_N},{_B:'Sold Out Face',_C:14,_D:40,_A:'assets/Non-Code/displays/soldout32.png',_F:_N},{_B:'End Sequence Credits',_C:19,_D:7,_A:'assets/Non-Code/credits/credits.bin',_T:_E},{_B:'WXY_Slash',_C:14,_D:12,_A:'assets/Non-Code/displays/wxys.png',_F:_J}]
map_replacements=[]
for x in range(175):
	if x>0:file_dict.append({_B:'Song '+str(x),_C:0,_D:x,_A:'song'+str(x)+_W,_M:11742})
for x in range(6):file_dict.append({_B:'DKTV Inputs '+str(x),_C:17,_D:x,_A:'dktv'+str(x)+_W,_M:1816})
for x in range(221):file_dict.append({_B:'Zones for map '+str(x),_C:18,_D:x,_A:'lz'+str(x)+_W,_M:2128,_X:_E})
for x in range(221):file_dict.append({_B:'Setup for map '+str(x),_C:9,_D:x,_A:'setup'+str(x)+_W,_M:32768,_Y:32768,_X:_E})
for x in range(221):file_dict.append({_B:'Character Spawners for map '+str(x),_C:16,_D:x,_A:'charspawners'+str(x)+_W,_M:4096,_Y:4096,_X:_E})
for x in range(8):file_dict.append({_B:'Key '+str(x+1)+' file screen',_C:14,_D:107+x,_A:'assets/Non-Code/file_screen/key'+str(x+1)+_c,_F:_J})
for x in range(43):
	if x!=13:
		if x!=32:file_dict.append({_B:'Text '+str(x),_C:12,_D:x,_A:'text'+str(x)+_W,_M:8192,_Y:8192,_X:_E})
for x in range(10):file_dict.append({_B:f"Tag Barrel Bottom Texture ({x+1})",_C:25,_D:4749+x,_A:'assets/Non-Code/tagbarrel/bottom.png',_F:_J})
barrel_faces=['Dk','Diddy','Lanky','Tiny','Chunky']
barrel_offsets=[4817,4815,4819,4769,4747]
for x in range(5):
	for y in range(2):file_dict.append({_B:f"{barrel_faces[x]} Transform Barrel Shell ({y+1})",_C:25,_D:barrel_offsets[x]+y,_A:f"assets/Non-Code/tagbarrel/{barrel_faces[x]} barrel {y}.png",_F:_J})
portal_image_order=[['SE','NE','SW','NW'],['NW','SW','NE','SE']]
for x in range(2):
	order=portal_image_order[x];image_series=portal_images[x]
	for y in range(4):
		segment=order[y];found_image=''
		for image in image_series:
			if segment in image:found_image=image
		if found_image!='':file_dict.append({_B:f"Portal Image {x+1} - {segment}",_C:7,_D:931+4*x+y,_A:found_image,_F:_J,_O:_E})
hash_icons=['bongos.png','crown.png','dkcoin.png','fairy.png','guitar.png','nin_coin.png','orange.png','rainbow_coin.png','rw_coin.png','sax.png']
hash_indexes=[48,49,50,51,55,62,63,64,65,76]
for x in range(len(hash_indexes)):idx=hash_indexes[x];file_dict.append({_B:f"Hash Icon {x+1}",_C:14,_D:idx,_A:f"assets/Non-Code/hash/{hash_icons[x]}",_F:_J})
file_dict.append({_B:'Dolby Text',_C:12,_D:13,_A:'dolby_text.bin',_O:_E,_T:_E})
file_dict.append({_B:'Custom Text',_C:12,_D:32,_A:'custom_text.bin',_O:_E,_T:_E})
print('DK64 Extractor')
with open(ROMName,_Z)as fh:
	print('[1 / 7] - Parsing pointer tables');parsePointerTables(fh);readOverlayOriginalData(fh)
	for x in map_replacements:
		print(' - Processing map replacement '+x[_B])
		if os.path.exists(x[_P]):
			found_geometry=_f;found_floors=_f;found_walls=_f;should_compress_walls=_E;should_compress_floors=_E
			for y in pointer_tables:
				if _U not in y:continue
				if _g in y and callable(y[_g]):
					if _h in y and os.path.exists(x[_P]+y[_h]):y[_g](x[_P]+y[_h],x[_P]+y[_U])
				if os.path.exists(x[_P]+y[_U]):
					if y[_V]==1:
						with open(x[_P]+y[_U],_Z)as fg:byte_read=fg.read(10);should_compress_walls=byte_read[9]&1!=0;should_compress_floors=byte_read[9]&2!=0
						found_geometry=_E
					elif y[_V]==2:found_walls=_E
					elif y[_V]==3:found_floors=_E
			walls_floors_geometry_valid=found_geometry==found_walls and found_geometry==found_floors
			if not walls_floors_geometry_valid:print('  - WARNING: In map replacement: '+x[_B]);print('    - Need all 3 files present to replace walls, floors, and geometry.');print('    - Only found 1 or 2 of them out of 3. Make sure all 3 exist on disk.');print('    - Will skip replacing walls, floors, and geometry to prevent crashes.')
			for y in pointer_tables:
				if _U not in y:continue
				if os.path.exists(x[_P]+y[_U]):
					if y[_V]in[1,2,3]and not walls_floors_geometry_valid:continue
					do_not_compress=_O in y and y[_O]
					if y[_V]==2:do_not_compress=not should_compress_walls
					elif y[_V]==3:do_not_compress=not should_compress_floors
					print('  - Found '+x[_P]+y[_U]);file_dict.append({_B:x[_B]+y[_B],_C:y[_V],_D:x['map_index'],_A:x[_P]+y[_U],_a:_E,_O:do_not_compress,_L:_L in y and y[_L]})
	print('[2 / 7] - Extracting files from ROM')
	for x in file_dict:
		if _F in x:x[_a]=_E;x[_I]=x[_A].replace(_c,'.'+x[_F])
		if _I not in x:x[_I]=x[_A]
		if _L in x and x[_L]:x[_I]=x[_I]+'.gz'
		if _a in x and x[_a]:x[_T]=_E
		if not(_a in x and x[_a]):
			byte_read=bytes()
			if _C in x and _D in x:
				file_info=getFileInfo(x[_C],x[_D])
				if file_info:x[_S]=file_info['new_absolute_address'];x[_d]=len(file_info['data'])
			if _S not in x:print(x)
			fh.seek(x[_S]);byte_read=fh.read(x[_d])
			if not(_T in x and x[_T]):
				if os.path.exists(x[_A]):os.remove(x[_A])
				with open(x[_A],'wb')as fg:dec=zlib.decompress(byte_read,15+32);fg.write(dec)
print('[3 / 7] - Patching Extracted Files')
for x in file_dict:
	if _b in x and callable(x[_b]):print(' - Running patcher for '+x[_A]);x[_b](x[_A])
with open(newROMName,'r+b')as fh:
	print('[4 / 7] - Writing patched files to ROM')
	for x in file_dict:
		if _M in x:
			x[_O]=_E
			if x[_A][:5]=='setup':convertSetup(x[_A])
			with open(x[_A],_Z)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			if _X in x and x[_X]:
				compress=bytearray(byte_read)
				if _Y in x:
					diff=x[_Y]-len(byte_read);byte_append=0
					if diff>0:byte_read+=byte_append.to_bytes(diff,_K)
					compress=bytearray(byte_read);uncompressed_size=x[_Y]
			else:
				precomp=gzip.compress(byte_read,compresslevel=9);byte_append=0;diff=x[_M]-len(precomp)
				if diff>0:precomp+=byte_append.to_bytes(diff,_K)
				compress=bytearray(precomp);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			with open(x[_A],'wb')as fg:fg.write(compress)
			x[_I]=x[_A]
		if _G in x and x[_G]:
			with open(x[_A],_Z)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			subprocess.Popen(['build\\flips.exe','--apply',x[_H],x[_A],x[_A]]).wait()
		if _F in x:
			if x[_F]in[_J,'i4',_e,'i8','ia8']:result=subprocess.check_output(['./build/n64tex.exe',x[_F],x[_A]])
			elif x[_F]==_N:convertToRGBA32(x[_A]);x[_A]=x[_A].replace(_c,_j)
			else:print(' - ERROR: Unsupported texture format '+x[_F])
		if _L in x and x[_L]:
			if os.path.exists(x[_A]):
				result=subprocess.check_output(['./build/gzip.exe','-f','-n','-k','-q','-9',x[_I].replace('.gz','')])
				if os.path.exists(x[_I]):
					with open(x[_I],'r+b')as outputFile:outputFile.truncate(len(outputFile.read())-8)
		if os.path.exists(x[_I]):
			byte_read=bytes()
			if _M not in x:uncompressed_size=0
			with open(x[_I],_Z)as fg:
				byte_read=fg.read()
				if _M not in x:uncompressed_size=len(byte_read)
			if _O in x and x[_O]:compress=bytearray(byte_read)
			elif _L in x and x[_L]:compress=bytearray(byte_read)
			elif _k in x and x[_k]:compressor=zlib.compressobj(zlib.Z_BEST_COMPRESSION,zlib.DEFLATED,25);compress=compressor.compress(byte_read);compress+=compressor.flush();compress=bytearray(compress);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			else:compress=bytearray(gzip.compress(byte_read,compresslevel=9));compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			print(' - Writing '+x[_I]+' ('+hex(len(compress))+_l)
			if _C in x and _D in x:replaceROMFile(x[_C],x[_D],compress,uncompressed_size)
			elif _S in x:
				if isROMAddressOverlay(x[_S]):replaceOverlayData(x[_S],compress)
				else:fh.seek(x[_S]);fh.write(compress)
			else:print("  - WARNING: Can't find address information in file_dict entry to write "+x[_I]+' ('+hex(len(compress))+_l)
		else:print(x[_I]+' does not exist')
		if not(_m in x and x[_m]):
			if not(_n in x and x[_n]):
				if os.path.exists(x[_I])and x[_I]!=x[_A]:os.remove(x[_I])
			if not(_T in x and x[_T]):
				if os.path.exists(x[_A]):os.remove(x[_A])
	print('[5 / 7] - Writing recomputed pointer tables to ROM');writeModifiedPointerTablesToROM(fh);writeModifiedOverlaysToROM(fh);print('[6 / 7] - Dumping details of all pointer tables to rom/build.log');dumpPointerTableDetails('rom/build.log',fh);fh.seek(33476640);arr=[]
	for x in range(512):arr.append(0)
	fh.write(bytearray(arr));writeVanillaMoveData(fh);adjustExits(fh);replaceSimSlam(fh);writeVanillaSongData(fh)
	for x in portal_images:
		for y in x:
			if os.path.exists(y):os.remove(y)
	fh.seek(33476640+321);fh.write((0).to_bytes(1,_K));fh.seek(33476640+322);fh.write((1).to_bytes(1,_K));fh.seek(33476640+323);fh.write((0).to_bytes(1,_K));fh.seek(33476640+324);fh.write((2).to_bytes(1,_K));fh.seek(33476640+325);fh.write((0).to_bytes(1,_K));fh.seek(33476640+326);fh.write((3).to_bytes(1,_K));fh.seek(33476640+327);fh.write((1).to_bytes(1,_K));fh.seek(33476640+328);fh.write((4).to_bytes(1,_K));fh.seek(33476640+329);fh.write((2).to_bytes(1,_K))
	with open('assets/Non-Code/credits/squish.bin',_Z)as squish:fh.seek(33552384);fh.write(squish.read())
	vanilla_coin_reqs=[{_Q:300,_R:50},{_Q:301,_R:50},{_Q:302,_R:10},{_Q:303,_R:10},{_Q:304,_R:10},{_Q:305,_R:50},{_Q:306,_R:50},{_Q:307,_R:25}]
	for coinreq in vanilla_coin_reqs:fh.seek(33476640+coinreq[_Q]);fh.write(coinreq[_R].to_bytes(1,_K))
	for x in hash_icons:
		pth=f"assets/Non-Code/hash/{x}"
		if os.path.exists(pth):os.remove(pth)
	other_remove=[];displays=['dk_face','diddy_face','lanky_face','tiny_face','chunky_face','none','shared','soldout32','wxys']
	for disp in displays:
		for ext in [_c,_j]:other_remove.append(f"displays/{disp}{ext}")
	for x in range(8):other_remove.append(f"file_screen/key{x+1}.png")
	for x in other_remove:
		pth=f"assets/Non-Code/{x}"
		if os.path.exists(pth):os.remove(pth)
	credits_bins=['credits','squish']
	for x in credits_bins:
		pth=f"assets/Non-Code/credits/{x}.bin"
		if os.path.exists(pth):os.remove(pth)
print('[7 / 7] - Generating BizHawk RAM watch')
exit()