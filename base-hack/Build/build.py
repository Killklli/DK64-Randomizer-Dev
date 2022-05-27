'Build the ROM.'
_o='do_not_delete_output'
_n='do_not_delete'
_m=') to ROM'
_l='use_zlib'
_k='.rgba32'
_j='assets/Non-Code/credits'
_i='decoded_filename'
_h='encoder'
_g=False
_f='assets/Non-Code/Gong/hint_door.bin'
_e='bps_file'
_d='ia4'
_c='compressed_size'
_b='.png'
_a='is_diff_patch'
_Z='patcher'
_Y='do_not_extract'
_X='rb'
_W='target_uncompressed_size'
_V='do_not_recompress'
_U='.bin'
_T='encoded_filename'
_S='start'
_R='coins'
_Q='offset'
_P='map_folder'
_O='rgba32'
_N='do_not_compress'
_M='target_compressed_size'
_L='do_not_delete_source'
_K='use_external_gzip'
_J='rgba5551'
_I='index'
_H='big'
_G='output_file'
_F=True
_E='texture_format'
_D='file_index'
_C='pointer_table_index'
_B='name'
_A='source_file'
import gzip,os,shutil,subprocess,sys,zlib,generate_watch_file,patch_text
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
from instance_script_maps import instance_script_maps
from generate_yellow_wrinkly import generateYellowWrinkly
ROMName='rom/dk64.z64'
newROMName='rom/dk64-randomizer-base.z64'
if os.path.exists(newROMName):os.remove(newROMName)
shutil.copyfile(ROMName,newROMName)
portal_images=[]
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_1.png'))
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_2.png'))
createTextFile(_j)
createSquishFile(_j)
generateYellowWrinkly()
file_dict=[{_B:'Static ASM Code',_S:70640,_c:726500,_A:'StaticCode.bin',_K:_F,_Z:patchStaticCode},{_B:'Dolby Logo',_C:14,_D:176,_A:'assets/Non-Code/Dolby/DolbyThin.png',_E:_d},{_B:'Thumb Image',_C:14,_D:94,_A:'assets/Non-Code/Nintendo Logo/Nintendo.png',_E:_J},{_B:'DKTV Image',_C:14,_D:44,_A:'assets/Non-Code/DKTV/logo3.png',_E:_J},{_B:'Spin Transition Image',_C:14,_D:95,_A:'assets/Non-Code/transition/transition-body.png',_E:_d},{_B:'Moves Image',_C:14,_D:115,_A:'assets/Non-Code/file_screen/moves.png',_E:_J},{_B:'Blueprint Image',_C:14,_D:116,_A:'assets/Non-Code/file_screen/blueprint.png',_E:_J},{_B:'Tag Barrel Shell Texture',_C:25,_D:4938,_A:'assets/Non-Code/tagbarrel/shell.png',_E:_J},{_B:'Gong Geometry',_C:4,_D:195,_A:'assets/Non-Code/Gong/gong_geometry.bin',_e:'assets/Non-Code/Gong/gong_geometry.bps',_a:_F},{_B:'No Face',_C:14,_D:33,_A:'assets/Non-Code/displays/none.png',_E:_O},{_B:'DK Face',_C:14,_D:34,_A:'assets/Non-Code/displays/dk_face.png',_E:_O},{_B:'Diddy Face',_C:14,_D:35,_A:'assets/Non-Code/displays/diddy_face.png',_E:_O},{_B:'Lanky Face',_C:14,_D:36,_A:'assets/Non-Code/displays/lanky_face.png',_E:_O},{_B:'Tiny Face',_C:14,_D:37,_A:'assets/Non-Code/displays/tiny_face.png',_E:_O},{_B:'Chunky Face',_C:14,_D:38,_A:'assets/Non-Code/displays/chunky_face.png',_E:_O},{_B:'Shared Face',_C:14,_D:39,_A:'assets/Non-Code/displays/shared.png',_E:_O},{_B:'Sold Out Face',_C:14,_D:40,_A:'assets/Non-Code/displays/soldout32.png',_E:_O},{_B:'End Sequence Credits',_C:19,_D:7,_A:'assets/Non-Code/credits/credits.bin',_L:_F},{_B:'DK Wrinkly Door',_C:4,_D:240,_A:_f,_L:_F},{_B:'WXY_Slash',_C:14,_D:12,_A:'assets/Non-Code/displays/wxys.png',_E:_J}]
map_replacements=[]
song_replacements=[{_B:'baboon_balloon',_I:107},{_B:'bonus_minigames',_I:8},{_B:'dk_rap',_I:75},{_B:'failure_races_try_again',_I:87},{_B:'move_get',_I:114},{_B:'nintendo_logo',_I:174},{_B:'success_races',_I:86}]
changed_song_indexes=[]
for x in instance_script_maps:file_dict.append({_B:f"{x[_B].replace('_',' ')} Instance Scripts",_C:10,_D:x['map'],_A:f"assets/Non-Code/instance_scripts/{x[_B]}.bin",_e:f"assets/Non-Code/instance_scripts/{x[_B]}.bps",_a:_F})
for x in range(175):
	if x>0:
		if x not in changed_song_indexes:file_dict.append({_B:'Song '+str(x),_C:0,_D:x,_A:'song'+str(x)+_U,_M:11742})
for x in range(6):file_dict.append({_B:'DKTV Inputs '+str(x),_C:17,_D:x,_A:'dktv'+str(x)+_U,_M:1816})
for x in range(221):file_dict.append({_B:'Zones for map '+str(x),_C:18,_D:x,_A:'lz'+str(x)+_U,_M:2128,_V:_F})
for x in range(221):file_dict.append({_B:'Setup for map '+str(x),_C:9,_D:x,_A:'setup'+str(x)+_U,_M:32768,_W:32768,_V:_F})
for x in range(221):file_dict.append({_B:'Character Spawners for map '+str(x),_C:16,_D:x,_A:'charspawners'+str(x)+_U,_M:4096,_W:4096,_V:_F})
for x in range(8):file_dict.append({_B:'Key '+str(x+1)+' file screen',_C:14,_D:107+x,_A:'assets/Non-Code/file_screen/key'+str(x+1)+_b,_E:_J})
for x in range(43):
	if x!=13:
		if x!=32:
			if x!=24:file_dict.append({_B:'Text '+str(x),_C:12,_D:x,_A:'text'+str(x)+_U,_M:8192,_W:8192,_V:_F})
for x in range(10):file_dict.append({_B:f"Tag Barrel Bottom Texture ({x+1})",_C:25,_D:4749+x,_A:'assets/Non-Code/tagbarrel/bottom.png',_E:_J})
barrel_faces=['Dk','Diddy','Lanky','Tiny','Chunky']
barrel_offsets=[4817,4815,4819,4769,4747]
for x in range(5):
	for y in range(2):file_dict.append({_B:f"{barrel_faces[x]} Transform Barrel Shell ({y+1})",_C:25,_D:barrel_offsets[x]+y,_A:f"assets/Non-Code/tagbarrel/{barrel_faces[x]} barrel {y}a.png",_E:_J})
portal_image_order=[['SE','NE','SW','NW'],['NW','SW','NE','SE']]
for x in range(2):
	order=portal_image_order[x];image_series=portal_images[x]
	for y in range(4):
		segment=order[y];found_image=''
		for image in image_series:
			if segment in image:found_image=image
		if found_image!='':file_dict.append({_B:f"Portal Image {x+1} - {segment}",_C:7,_D:931+4*x+y,_A:found_image,_E:_J,_N:_F})
hash_icons=['bongos.png','crown.png','dkcoin.png','fairy.png','guitar.png','nin_coin.png','orange.png','rainbow_coin.png','rw_coin.png','sax.png']
hash_indexes=[48,49,50,51,55,62,63,64,65,76]
for x in range(len(hash_indexes)):idx=hash_indexes[x];file_dict.append({_B:f"Hash Icon {x+1}",_C:14,_D:idx,_A:f"assets/Non-Code/hash/{hash_icons[x]}",_E:_J})
file_dict.append({_B:'Dolby Text',_C:12,_D:13,_A:'dolby_text.bin',_N:_F,_L:_F})
file_dict.append({_B:'Custom Text',_C:12,_D:32,_A:'custom_text.bin',_N:_F,_L:_F})
file_dict.append({_B:'DK Text',_C:12,_D:24,_A:'dk_text.bin',_N:_F,_L:_F})
print('DK64 Extractor')
with open(ROMName,_X)as fh:
	print('[1 / 7] - Parsing pointer tables');parsePointerTables(fh);readOverlayOriginalData(fh)
	for x in map_replacements:
		print(' - Processing map replacement '+x[_B])
		if os.path.exists(x[_P]):
			found_geometry=_g;found_floors=_g;found_walls=_g;should_compress_walls=_F;should_compress_floors=_F
			for y in pointer_tables:
				if _T not in y:continue
				if _h in y and callable(y[_h]):
					if _i in y and os.path.exists(x[_P]+y[_i]):y[_h](x[_P]+y[_i],x[_P]+y[_T])
				if os.path.exists(x[_P]+y[_T]):
					if y[_I]==1:
						with open(x[_P]+y[_T],_X)as fg:byte_read=fg.read(10);should_compress_walls=byte_read[9]&1!=0;should_compress_floors=byte_read[9]&2!=0
						found_geometry=_F
					elif y[_I]==2:found_walls=_F
					elif y[_I]==3:found_floors=_F
			walls_floors_geometry_valid=found_geometry==found_walls and found_geometry==found_floors
			if not walls_floors_geometry_valid:print('  - WARNING: In map replacement: '+x[_B]);print('    - Need all 3 files present to replace walls, floors, and geometry.');print('    - Only found 1 or 2 of them out of 3. Make sure all 3 exist on disk.');print('    - Will skip replacing walls, floors, and geometry to prevent crashes.')
			for y in pointer_tables:
				if _T not in y:continue
				if os.path.exists(x[_P]+y[_T]):
					if y[_I]in[1,2,3]and not walls_floors_geometry_valid:continue
					do_not_compress=_N in y and y[_N]
					if y[_I]==2:do_not_compress=not should_compress_walls
					elif y[_I]==3:do_not_compress=not should_compress_floors
					print('  - Found '+x[_P]+y[_T]);file_dict.append({_B:x[_B]+y[_B],_C:y[_I],_D:x['map_index'],_A:x[_P]+y[_T],_Y:_F,_N:do_not_compress,_K:_K in y and y[_K]})
	print('[2 / 7] - Extracting files from ROM')
	for x in file_dict:
		if _E in x:x[_Y]=_F;x[_G]=x[_A].replace(_b,'.'+x[_E])
		if _G not in x:x[_G]=x[_A]
		if _K in x and x[_K]:x[_G]=x[_G]+'.gz'
		if _Y in x and x[_Y]:x[_L]=_F
		if not(_Y in x and x[_Y]):
			byte_read=bytes()
			if _C in x and _D in x:
				file_info=getFileInfo(x[_C],x[_D])
				if file_info:x[_S]=file_info['new_absolute_address'];x[_c]=len(file_info['data'])
			if _S not in x:print(x)
			fh.seek(x[_S]);byte_read=fh.read(x[_c])
			if not(_L in x and x[_L]):
				if os.path.exists(x[_A]):os.remove(x[_A])
				with open(x[_A],'wb')as fg:dec=zlib.decompress(byte_read,15+32);fg.write(dec)
print('[3 / 7] - Patching Extracted Files')
for x in file_dict:
	if _Z in x and callable(x[_Z]):print(' - Running patcher for '+x[_A]);x[_Z](x[_A])
with open(newROMName,'r+b')as fh:
	print('[4 / 7] - Writing patched files to ROM')
	for x in file_dict:
		if _a in x and x[_a]:
			with open(x[_A],_X)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			subprocess.Popen(['build\\flips.exe','--apply',x[_e],x[_A],x[_A]]).wait()
		if _M in x:
			x[_N]=_F
			if x[_A][:5]=='setup':convertSetup(x[_A])
			with open(x[_A],_X)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			if _V in x and x[_V]:
				compress=bytearray(byte_read)
				if _W in x:
					diff=x[_W]-len(byte_read);byte_append=0
					if diff>0:byte_read+=byte_append.to_bytes(diff,_H)
					compress=bytearray(byte_read);uncompressed_size=x[_W]
			else:
				precomp=gzip.compress(byte_read,compresslevel=9);byte_append=0;diff=x[_M]-len(precomp)
				if diff>0:precomp+=byte_append.to_bytes(diff,_H)
				compress=bytearray(precomp);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			with open(x[_A],'wb')as fg:fg.write(compress)
			x[_G]=x[_A]
		if _E in x:
			if x[_E]in[_J,'i4',_d,'i8','ia8']:result=subprocess.check_output(['./build/n64tex.exe',x[_E],x[_A]])
			elif x[_E]==_O:convertToRGBA32(x[_A]);x[_A]=x[_A].replace(_b,_k)
			else:print(' - ERROR: Unsupported texture format '+x[_E])
		if _K in x and x[_K]:
			if os.path.exists(x[_A]):
				result=subprocess.check_output(['./build/gzip.exe','-f','-n','-k','-q','-9',x[_G].replace('.gz','')])
				if os.path.exists(x[_G]):
					with open(x[_G],'r+b')as outputFile:outputFile.truncate(len(outputFile.read())-8)
		if os.path.exists(x[_G]):
			byte_read=bytes()
			if _M not in x:uncompressed_size=0
			with open(x[_G],_X)as fg:
				byte_read=fg.read()
				if _M not in x:uncompressed_size=len(byte_read)
			if _N in x and x[_N]:compress=bytearray(byte_read)
			elif _K in x and x[_K]:compress=bytearray(byte_read)
			elif _l in x and x[_l]:compressor=zlib.compressobj(zlib.Z_BEST_COMPRESSION,zlib.DEFLATED,25);compress=compressor.compress(byte_read);compress+=compressor.flush();compress=bytearray(compress);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			else:compress=bytearray(gzip.compress(byte_read,compresslevel=9));compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			print(' - Writing '+x[_G]+' ('+hex(len(compress))+_m)
			if _C in x and _D in x:replaceROMFile(x[_C],x[_D],compress,uncompressed_size)
			elif _S in x:
				if isROMAddressOverlay(x[_S]):replaceOverlayData(x[_S],compress)
				else:fh.seek(x[_S]);fh.write(compress)
			else:print("  - WARNING: Can't find address information in file_dict entry to write "+x[_G]+' ('+hex(len(compress))+_m)
		else:print(x[_G]+' does not exist')
		if not(_n in x and x[_n]):
			if not(_o in x and x[_o]):
				if os.path.exists(x[_G])and x[_G]!=x[_A]:os.remove(x[_G])
			if not(_L in x and x[_L]):
				if os.path.exists(x[_A]):os.remove(x[_A])
	print('[5 / 7] - Writing recomputed pointer tables to ROM');writeModifiedPointerTablesToROM(fh);writeModifiedOverlaysToROM(fh);print('[6 / 7] - Dumping details of all pointer tables to rom/build.log');dumpPointerTableDetails('rom/build.log',fh);main_pointer_table_offset=1055824;fh.seek(main_pointer_table_offset+12*4);text_table=main_pointer_table_offset+int.from_bytes(fh.read(4),_H);fh.seek(text_table+19*4);misc_text=main_pointer_table_offset+int.from_bytes(fh.read(4),_H);fh.seek(misc_text+1872);fh.write('?'.encode('ascii'))
	for i in range(21):fh.write('\x00'.encode('ascii'))
	fh.seek(33476640);arr=[]
	for x in range(512):arr.append(0)
	fh.write(bytearray(arr));writeVanillaMoveData(fh);adjustExits(fh);replaceSimSlam(fh);writeVanillaSongData(fh)
	for x in portal_images:
		for y in x:
			if os.path.exists(y):os.remove(y)
	fh.seek(33476640+321);fh.write((0).to_bytes(1,_H));fh.seek(33476640+322);fh.write((1).to_bytes(1,_H));fh.seek(33476640+323);fh.write((0).to_bytes(1,_H));fh.seek(33476640+324);fh.write((2).to_bytes(1,_H));fh.seek(33476640+325);fh.write((0).to_bytes(1,_H));fh.seek(33476640+326);fh.write((3).to_bytes(1,_H));fh.seek(33476640+327);fh.write((1).to_bytes(1,_H));fh.seek(33476640+328);fh.write((4).to_bytes(1,_H));fh.seek(33476640+329);fh.write((2).to_bytes(1,_H));fh.seek(33476640+315);fh.write((1).to_bytes(1,_H))
	with open('assets/Non-Code/credits/squish.bin',_X)as squish:fh.seek(33552384);fh.write(squish.read())
	vanilla_coin_reqs=[{_Q:300,_R:50},{_Q:301,_R:50},{_Q:302,_R:10},{_Q:303,_R:10},{_Q:304,_R:10},{_Q:305,_R:50},{_Q:306,_R:50},{_Q:307,_R:25}]
	for coinreq in vanilla_coin_reqs:fh.seek(33476640+coinreq[_Q]);fh.write(coinreq[_R].to_bytes(1,_H))
	for x in hash_icons:
		pth=f"assets/Non-Code/hash/{x}"
		if os.path.exists(pth):os.remove(pth)
	other_remove=[];displays=['dk_face','diddy_face','lanky_face','tiny_face','chunky_face','none','shared','soldout32','wxys','yellow_qmark_0','yellow_qmark_1']
	for disp in displays:
		for ext in [_b,_k]:other_remove.append(f"displays/{disp}{ext}")
	for x in range(8):other_remove.append(f"file_screen/key{x+1}.png")
	for x in other_remove:
		pth=f"assets/Non-Code/{x}"
		if os.path.exists(pth):os.remove(pth)
	credits_bins=['credits','squish']
	for x in credits_bins:
		pth=f"assets/Non-Code/credits/{x}.bin"
		if os.path.exists(pth):os.remove(pth)
	if os.path.exists(_f):os.remove(_f)
print('[7 / 7] - Generating BizHawk RAM watch')
sys.exit()