'Build the ROM.'
_A4='num_9_unlit'
_A3='num_9_lit'
_A2='num_6_unlit'
_A1='num_6_lit'
_A0='do_not_delete_output'
_z='do_not_delete'
_y=') to ROM'
_x='use_zlib'
_w='.rgba32'
_v='homing_crate'
_u='standard_crate'
_t='Chunky'
_s='assets/Non-Code/hash/tiny_palette.png'
_r='Tiny Overalls Palette'
_q='assets/Non-Code/credits'
_p='helm.bin'
_o='decoded_filename'
_n='encoder'
_m='assets/Non-Code/Gong/hint_door.bin'
_l='bps_file'
_k='ia4'
_j='compressed_size'
_i=False
_h='is_diff_patch'
_g='patcher'
_f='.png'
_e='texture'
_d='rgba32'
_c='target_uncompressed_size'
_b='do_not_recompress'
_a='.bin'
_Z='state'
_Y='number'
_X='rb'
_W='encoded_filename'
_V='start'
_U='coins'
_T='offset'
_S='map_folder'
_R='model_index'
_Q='model_file'
_P='bps'
_O='do_not_extract'
_N='use_external_gzip'
_M='do_not_compress'
_L='do_not_delete_source'
_K='target_compressed_size'
_J='output_file'
_I='index'
_H='rgba5551'
_G='big'
_F='texture_format'
_E=True
_D='file_index'
_C='pointer_table_index'
_B='name'
_A='source_file'
import gzip,json,os,shutil,subprocess,sys,zlib,create_helm_geo,generate_watch_file,shop_instance_script,instance_script_maker,model_fix,patch_text
from adjust_exits import adjustExits
from convertPortalImage import convertPortalImage
from convertSetup import convertSetup
from end_seq_writer import createSquishFile,createTextFile
from generate_yellow_wrinkly import generateYellowWrinkly
from image_converter import convertToRGBA32
from map_names import maps
from populateSongData import writeVanillaSongData
from recompute_overlays import isROMAddressOverlay,readOverlayOriginalData,replaceOverlayData,writeModifiedOverlaysToROM
from recompute_pointer_table import dumpPointerTableDetails,getFileInfo,make_safe_filename,parsePointerTables,pointer_tables,replaceROMFile,writeModifiedPointerTablesToROM
from replace_simslam_text import replaceSimSlam
from staticcode import patchStaticCode
from vanilla_move_data import writeVanillaMoveData
ROMName='rom/dk64.z64'
newROMName='rom/dk64-randomizer-base.z64'
if os.path.exists(newROMName):os.remove(newROMName)
shutil.copyfile(ROMName,newROMName)
portal_images=[]
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_1.png'))
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_2.png'))
createTextFile(_q)
createSquishFile(_q)
generateYellowWrinkly()
file_dict=[{_B:'Static ASM Code',_V:70640,_j:726500,_A:'StaticCode.bin',_N:_E,_g:patchStaticCode},{_B:'Dolby Logo',_C:14,_D:176,_A:'assets/Non-Code/Dolby/DolbyThin.png',_F:_k},{_B:'Thumb Image',_C:14,_D:94,_A:'assets/Non-Code/Nintendo Logo/Nintendo4.png',_F:_H},{_B:'DKTV Image',_C:14,_D:44,_A:'assets/Non-Code/DKTV/logo3.png',_F:_H},{_B:'Spin Transition Image',_C:14,_D:95,_A:'assets/Non-Code/transition/transition-body.png',_F:_k},{_B:'Moves Image',_C:14,_D:115,_A:'assets/Non-Code/file_screen/moves.png',_F:_H},{_B:'Blueprint Image',_C:14,_D:116,_A:'assets/Non-Code/file_screen/blueprint.png',_F:_H},{_B:'Tag Barrel Shell Texture',_C:25,_D:4938,_A:'assets/Non-Code/tagbarrel/shell.png',_F:_H},{_B:'Gong Geometry',_C:4,_D:195,_A:'assets/Non-Code/Gong/gong_geometry.bin',_l:'assets/Non-Code/Gong/gong_geometry.bps',_h:_E},{_B:'No Face',_C:14,_D:33,_A:'assets/Non-Code/displays/none.png',_F:_d},{_B:'Shared Face',_C:14,_D:39,_A:'assets/Non-Code/displays/shared.png',_F:_d},{_B:'Sold Out Face',_C:14,_D:40,_A:'assets/Non-Code/displays/soldout32.png',_F:_d},{_B:'End Sequence Credits',_C:19,_D:7,_A:'assets/Non-Code/credits/credits.bin',_L:_E},{_B:'DK Wrinkly Door',_C:4,_D:240,_A:_m,_L:_E},{_B:'WXY_Slash',_C:14,_D:12,_A:'assets/Non-Code/displays/wxys.png',_F:_H},{_B:'DK Tie Palette',_C:25,_D:6013,_A:'assets/Non-Code/hash/dk_tie_palette.png',_O:_E,_F:_H,_K:32*32*2},{_B:_r,_C:25,_D:6014,_A:_s,_O:_E,_F:_H,_K:32*32*2},{_B:_r,_C:25,_D:6014,_A:_s,_O:_E,_F:_H,_K:32*32*2},{_B:'DPad Image',_C:14,_D:187,_A:'assets/Non-Code/displays/dpad.png',_F:_H}]
number_game_changes=[{_Y:6,_Z:'unlit',_e:520},{_Y:6,_Z:'lit',_e:521},{_Y:9,_Z:'unlit',_e:526},{_Y:9,_Z:'lit',_e:527}]
for num in number_game_changes:file_dict.append({_B:f"Number Game ({num[_Y]}, {num[_Z]})",_C:7,_D:num[_e],_A:f"assets/Non-Code/displays/num_{num[_Y]}_{num[_Z]}.png",_F:_H,_M:_E})
kong_names=['DK','Diddy','Lanky','Tiny',_t]
ammo_names=[_u,_v]
for (ammo_index,ammo) in enumerate(ammo_names):file_dict.append({_B:f"{ammo.replace('_',' ')} Image",_C:14,_D:188+ammo_index,_A:f"assets/Non-Code/displays/{ammo}.png",_F:_H})
for (kong_index,kong) in enumerate(kong_names):
	for (x_i,x) in enumerate([_d,_H]):file_dict.append({_B:f"{kong} Face ({x})",_C:14,_D:[34+kong_index,190+kong_index][x_i],_A:f"assets/Non-Code/displays/{kong.lower()}_face.png",_F:x})
base_coin_sfx='assets/Non-Code/music/Win95_startup.dk64song'
new_coin_sfx='assets/Non-Code/music/coin_sfx.bin'
if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
shutil.copyfile(base_coin_sfx,new_coin_sfx)
map_replacements=[]
song_replacements=[{_B:'baboon_balloon',_I:107,_P:_E},{_B:'bonus_minigames',_I:8,_P:_E},{_B:'dk_rap',_I:75,_P:_E},{_B:'failure_races_try_again',_I:87,_P:_E},{_B:'move_get',_I:114,_P:_E},{_B:'nintendo_logo',_I:174,_P:_E},{_B:'success_races',_I:86,_P:_E},{_B:'klumsy_celebration',_I:125,_P:_E},{_B:'coin_sfx',_I:7,_P:_i}]
changed_song_indexes=[]
for song in song_replacements:
	item={_B:song[_B].replace('_',' '),_C:0,_D:song[_I],_A:f"assets/Non-Code/music/{song[_B]}.bin",_K:11742}
	if song[_P]:item[_h]=_E;item[_l]=f"assets/Non-Code/music/{song[_B]}.bps"
	else:item[_L]=_E;item[_O]=_E
	file_dict.append(item);changed_song_indexes.append(song[_I])
with open('./instance_scripts_data.json','r')as json_f:instance_script_maps=json.load(json_f)
for x in instance_script_maps:file_dict.append({_B:f"{x[_B].replace('_',' ')} Instance Scripts",_C:10,_D:x['map'],_A:f"{x[_B]}.raw",_L:_E})
for x in range(175):
	if x>0:
		if x not in changed_song_indexes:file_dict.append({_B:'Song '+str(x),_C:0,_D:x,_A:'song'+str(x)+_a,_K:11742})
for x in range(6):file_dict.append({_B:'DKTV Inputs '+str(x),_C:17,_D:x,_A:'dktv'+str(x)+_a,_K:1816})
for x in range(221):file_dict.append({_B:'Zones for map '+str(x),_C:18,_D:x,_A:'lz'+str(x)+_a,_K:2128,_b:_E})
for x in range(221):file_dict.append({_B:'Setup for map '+str(x),_C:9,_D:x,_A:'setup'+str(x)+_a,_K:32768,_c:32768,_b:_E})
for x in range(221):file_dict.append({_B:'Character Spawners for map '+str(x),_C:16,_D:x,_A:'charspawners'+str(x)+_a,_K:5120,_c:5120,_b:_E})
for x in range(8):file_dict.append({_B:'Key '+str(x+1)+' file screen',_C:14,_D:107+x,_A:'assets/Non-Code/file_screen/key'+str(x+1)+_f,_F:_H})
for x in range(43):
	if x!=13:
		if x!=32:
			if x!=24:file_dict.append({_B:'Text '+str(x),_C:12,_D:x,_A:'text'+str(x)+_a,_K:8192,_c:8192,_b:_E})
for x in range(10):file_dict.append({_B:f"Tag Barrel Bottom Texture ({x+1})",_C:25,_D:4749+x,_A:'assets/Non-Code/tagbarrel/bottom.png',_F:_H})
for x in range(4761,4768):
	sz='44'
	if x==4761:sz='3264'
	file_dict.append({_B:f"Portal Ripple Texture ({x})",_C:25,_D:x,_A:f"assets/Non-Code/displays/empty{sz}.png",_F:_H})
barrel_faces=['Dk','Diddy','Lanky','Tiny',_t]
barrel_offsets=[4817,4815,4819,4769,4747]
for x in range(5):
	for y in range(2):file_dict.append({_B:f"{barrel_faces[x]} Transform Barrel Shell ({y+1})",_C:25,_D:barrel_offsets[x]+y,_A:f"assets/Non-Code/tagbarrel/{barrel_faces[x]} barrel {y}a.png",_F:_H})
kong_palettes=[3724,3686,3689,3769,3687,3826,3847,3734]
for x in kong_palettes:
	x_s=32*32*2
	if x==3769 or x==3734:x_s=43*32*2
	file_dict.append({_B:f"Palette Expansion ({hex(x)})",_C:25,_D:x,_A:f"palette_{x}.bin",_K:x_s})
model_changes=[{_R:0,_Q:'diddy_base.bin'},{_R:1,_Q:'diddy_ins.bin'},{_R:5,_Q:'lanky_base.bin'},{_R:6,_Q:'lanky_ins.bin'},{_R:3,_Q:'dk_base.bin'},{_R:8,_Q:'tiny_base.bin'},{_R:9,_Q:'tiny_ins.bin'}]
for x in model_changes:file_dict.append({_B:f"Model {x[_R]}",_C:5,_D:x[_R],_A:x[_Q],_L:_E})
portal_image_order=[['SE','NE','SW','NW'],['NW','SW','NE','SE']]
for x in range(2):
	order=portal_image_order[x];image_series=portal_images[x]
	for y in range(4):
		segment=order[y];found_image=''
		for image in image_series:
			if segment in image:found_image=image
		if found_image!='':file_dict.append({_B:f"Portal Image {x+1} - {segment}",_C:7,_D:931+4*x+y,_A:found_image,_F:_H,_M:_E})
hash_icons=['bongos.png','crown.png','dkcoin.png','fairy.png','guitar.png','nin_coin.png','orange.png','rainbow_coin.png','rw_coin.png','sax.png']
hash_indexes=[48,49,50,51,55,62,63,64,65,76]
for x in range(len(hash_indexes)):idx=hash_indexes[x];file_dict.append({_B:f"Hash Icon {x+1}",_C:14,_D:idx,_A:f"assets/Non-Code/hash/{hash_icons[x]}",_F:_H})
file_dict.append({_B:'Dolby Text',_C:12,_D:13,_A:'dolby_text.bin',_M:_E,_L:_E})
file_dict.append({_B:'Custom Text',_C:12,_D:32,_A:'custom_text.bin',_M:_E,_L:_E})
file_dict.append({_B:'DK Text',_C:12,_D:24,_A:'dk_text.bin',_M:_E,_L:_E})
print('\nDK64 Extractor\nBuilt by Isotarge')
with open(ROMName,_X)as fh:
	print('[1 / 7] - Parsing pointer tables');parsePointerTables(fh);readOverlayOriginalData(fh)
	for x in map_replacements:
		print(' - Processing map replacement '+x[_B])
		if os.path.exists(x[_S]):
			found_geometry=_i;found_floors=_i;found_walls=_i;should_compress_walls=_E;should_compress_floors=_E
			for y in pointer_tables:
				if _W not in y:continue
				if _n in y and callable(y[_n]):
					if _o in y and os.path.exists(x[_S]+y[_o]):y[_n](x[_S]+y[_o],x[_S]+y[_W])
				if os.path.exists(x[_S]+y[_W]):
					if y[_I]==1:
						with open(x[_S]+y[_W],_X)as fg:byte_read=fg.read(10);should_compress_walls=byte_read[9]&1!=0;should_compress_floors=byte_read[9]&2!=0
						found_geometry=_E
					elif y[_I]==2:found_walls=_E
					elif y[_I]==3:found_floors=_E
			walls_floors_geometry_valid=found_geometry==found_walls and found_geometry==found_floors
			if not walls_floors_geometry_valid:print('  - WARNING: In map replacement: '+x[_B]);print('    - Need all 3 files present to replace walls, floors, and geometry.');print('    - Only found 1 or 2 of them out of 3. Make sure all 3 exist on disk.');print('    - Will skip replacing walls, floors, and geometry to prevent crashes.')
			for y in pointer_tables:
				if _W not in y:continue
				if os.path.exists(x[_S]+y[_W]):
					if y[_I]in[1,2,3]and not walls_floors_geometry_valid:continue
					do_not_compress=_M in y and y[_M]
					if y[_I]==2:do_not_compress=not should_compress_walls
					elif y[_I]==3:do_not_compress=not should_compress_floors
					print('  - Found '+x[_S]+y[_W]);file_dict.append({_B:x[_B]+y[_B],_C:y[_I],_D:x['map_index'],_A:x[_S]+y[_W],_O:_E,_M:do_not_compress,_N:_N in y and y[_N]})
	print('[2 / 7] - Extracting files from ROM')
	for x in file_dict:
		if _F in x:x[_O]=_E;x[_J]=x[_A].replace(_f,'.'+x[_F])
		if _J not in x:x[_J]=x[_A]
		if _N in x and x[_N]:x[_J]=x[_J]+'.gz'
		if _O in x and x[_O]:x[_L]=_E
		if not(_O in x and x[_O]):
			byte_read=bytes()
			if _C in x and _D in x:
				file_info=getFileInfo(x[_C],x[_D])
				if file_info:x[_V]=file_info['new_absolute_address'];x[_j]=len(file_info['data'])
			if _V not in x:print(x)
			fh.seek(x[_V]);byte_read=fh.read(x[_j])
			if not(_L in x and x[_L]):
				if os.path.exists(x[_A]):os.remove(x[_A])
				with open(x[_A],'wb')as fg:dec=zlib.decompress(byte_read,15+32);fg.write(dec)
print('[3 / 7] - Patching Extracted Files')
for x in file_dict:
	if _g in x and callable(x[_g]):print(' - Running patcher for '+x[_A]);x[_g](x[_A])
with open(newROMName,'r+b')as fh:
	print('[4 / 7] - Writing patched files to ROM')
	for x in file_dict:
		if _h in x and x[_h]:
			with open(x[_A],_X)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			subprocess.Popen(['build\\flips.exe','--apply',x[_l],x[_A],x[_A]]).wait()
		if _F in x:
			if x[_F]in[_H,'i4',_k,'i8','ia8']:
				result=subprocess.check_output(['./build/n64tex.exe',x[_F],x[_A]])
				if _K in x:x[_A]=x[_A].replace(_f,f".{x[_F]}")
			elif x[_F]==_d:convertToRGBA32(x[_A]);x[_A]=x[_A].replace(_f,_w)
			else:print(' - ERROR: Unsupported texture format '+x[_F])
		if _K in x:
			x[_M]=_E
			if x[_A][:5]=='setup':convertSetup(x[_A])
			with open(x[_A],_X)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			if _b in x and x[_b]:
				compress=bytearray(byte_read)
				if _c in x:
					diff=x[_c]-len(byte_read);byte_append=0
					if diff>0:byte_read+=byte_append.to_bytes(diff,_G)
					compress=bytearray(byte_read);uncompressed_size=x[_c]
			else:
				precomp=gzip.compress(byte_read,compresslevel=9);byte_append=0;diff=x[_K]-len(precomp)
				if diff>0:precomp+=byte_append.to_bytes(diff,_G)
				compress=bytearray(precomp);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			with open(x[_A],'wb')as fg:fg.write(compress)
			x[_J]=x[_A]
		if _N in x and x[_N]:
			if os.path.exists(x[_A]):
				result=subprocess.check_output(['./build/gzip.exe','-f','-n','-k','-q','-9',x[_J].replace('.gz','')])
				if os.path.exists(x[_J]):
					with open(x[_J],'r+b')as outputFile:outputFile.truncate(len(outputFile.read())-8)
		if os.path.exists(x[_J]):
			byte_read=bytes()
			if _K not in x:uncompressed_size=0
			with open(x[_J],_X)as fg:
				byte_read=fg.read()
				if _K not in x:uncompressed_size=len(byte_read)
			if _M in x and x[_M]:compress=bytearray(byte_read)
			elif _N in x and x[_N]:compress=bytearray(byte_read)
			elif _x in x and x[_x]:compressor=zlib.compressobj(zlib.Z_BEST_COMPRESSION,zlib.DEFLATED,25);compress=compressor.compress(byte_read);compress+=compressor.flush();compress=bytearray(compress);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			else:compress=bytearray(gzip.compress(byte_read,compresslevel=9));compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			print(' - Writing '+x[_J]+' ('+hex(len(compress))+_y)
			if _C in x and _D in x:replaceROMFile(fh,x[_C],x[_D],compress,uncompressed_size)
			elif _V in x:
				if isROMAddressOverlay(x[_V]):replaceOverlayData(x[_V],compress)
				else:fh.seek(x[_V]);fh.write(compress)
			else:print("  - WARNING: Can't find address information in file_dict entry to write "+x[_J]+' ('+hex(len(compress))+_y)
		else:print(x[_J]+' does not exist')
		if not(_z in x and x[_z]):
			if not(_A0 in x and x[_A0]):
				if os.path.exists(x[_J])and x[_J]!=x[_A]:os.remove(x[_J])
			if not(_L in x and x[_L]):
				if os.path.exists(x[_A]):os.remove(x[_A])
	print('[5 / 7] - Writing recomputed pointer tables to ROM');writeModifiedPointerTablesToROM(fh);writeModifiedOverlaysToROM(fh);print('[6 / 7] - Dumping details of all pointer tables to rom/build.log');dumpPointerTableDetails('rom/build.log',fh);main_pointer_table_offset=1055824;fh.seek(main_pointer_table_offset+4);geo_table=main_pointer_table_offset+int.from_bytes(fh.read(4),_G);fh.seek(geo_table+17*4);helm_geo=main_pointer_table_offset+int.from_bytes(fh.read(4),_G);helm_geo_end=main_pointer_table_offset+int.from_bytes(fh.read(4),_G);helm_geo_size=helm_geo_end-helm_geo;fh.seek(helm_geo)
	for by_i in range(helm_geo_size):fh.write((0).to_bytes(1,_G))
	fh.seek(helm_geo)
	with open(_p,_X)as helm_geo:fh.write(gzip.compress(helm_geo.read(),compresslevel=9))
	main_pointer_table_offset=1055824;fh.seek(main_pointer_table_offset+12*4);text_table=main_pointer_table_offset+int.from_bytes(fh.read(4),_G);fh.seek(text_table+19*4);misc_text=main_pointer_table_offset+int.from_bytes(fh.read(4),_G);fh.seek(misc_text+1872);fh.write('?'.encode('ascii'))
	for i in range(21):fh.write('\x00'.encode('ascii'))
	fh.seek(33476640);arr=[]
	for x in range(512):arr.append(0)
	fh.write(bytearray(arr));writeVanillaMoveData(fh);adjustExits(fh);replaceSimSlam(fh);writeVanillaSongData(fh)
	for x in portal_images:
		for y in x:
			if os.path.exists(y):os.remove(y)
	fh.seek(33476640+337);fh.write((0).to_bytes(1,_G));fh.seek(33476640+338);fh.write((1).to_bytes(1,_G));fh.seek(33476640+339);fh.write((0).to_bytes(1,_G));fh.seek(33476640+340);fh.write((2).to_bytes(1,_G));fh.seek(33476640+341);fh.write((0).to_bytes(1,_G));fh.seek(33476640+342);fh.write((3).to_bytes(1,_G));fh.seek(33476640+343);fh.write((1).to_bytes(1,_G));fh.seek(33476640+344);fh.write((4).to_bytes(1,_G));fh.seek(33476640+345);fh.write((2).to_bytes(1,_G));fh.seek(33476640+331);fh.write((1).to_bytes(1,_G));piano_vanilla=[2,1,2,3,4,2,0]
	for (piano_index,piano_key) in enumerate(piano_vanilla):fh.seek(33476640+364+piano_index);fh.write(piano_key.to_bytes(1,_G))
	dk_face_puzzle_vanilla=[0,3,2,0,1,2,3,2,1];chunky_face_puzzle_vanilla=[0,1,3,1,2,1,3,0,1]
	for face_index in range(9):fh.seek(33476640+382+face_index);fh.write(dk_face_puzzle_vanilla[face_index].to_bytes(1,_G));fh.seek(33476640+391+face_index);fh.write(chunky_face_puzzle_vanilla[face_index].to_bytes(1,_G))
	with open('assets/Non-Code/credits/squish.bin',_X)as squish:fh.seek(33552384);fh.write(squish.read())
	vanilla_coin_reqs=[{_T:316,_U:50},{_T:317,_U:50},{_T:318,_U:10},{_T:319,_U:10},{_T:320,_U:10},{_T:321,_U:50},{_T:322,_U:50},{_T:323,_U:25}]
	for coinreq in vanilla_coin_reqs:fh.seek(33476640+coinreq[_T]);fh.write(coinreq[_U].to_bytes(1,_G))
	for x in range(5):fh.seek(33476640+x);fh.write(x.to_bytes(1,_G))
	for x in hash_icons:
		pth=f"assets/Non-Code/hash/{x}"
		if os.path.exists(pth):os.remove(pth)
	other_remove=[];displays=['dk_face','diddy_face','lanky_face','tiny_face','chunky_face','none','shared','soldout32','wxys','yellow_qmark_0','yellow_qmark_1','empty44','empty3264',_v,_A1,_A2,_A3,_A4,_u]
	for disp in displays:
		for ext in [_f,_w]:other_remove.append(f"displays/{disp}{ext}")
	for x in range(8):other_remove.append(f"file_screen/key{x+1}.png")
	for x in other_remove:
		pth=f"assets/Non-Code/{x}"
		if os.path.exists(pth):os.remove(pth)
	hash_items=['dk_tie_palette','homing_crate_0','homing_crate_1','num_1_lit','num_1_unlit',_A1,_A2,'num_7_lit','num_7_unlit',_A3,_A4,'standard_crate_0','standard_crate_1','tiny_palette'];script_files=[A[0]for A in os.walk('assets/Non-Code/instance_scripts/')];shop_files=['snide.script','cranky.script','funky.script','candy.script']
	for folder in script_files:
		for file in os.listdir(folder):
			file=f"{folder}/{file}"
			for shop in shop_files:
				if shop in file:
					if os.path.exists(file):os.remove(file)
	for hash_item in hash_items:
		for f_t in [_H,'png']:
			pth=f"assets/Non-Code/hash/{hash_item}.{f_t}"
			if os.path.exists(pth):os.remove(pth)
	credits_bins=['credits','squish']
	for x in credits_bins:
		pth=f"assets/Non-Code/credits/{x}.bin"
		if os.path.exists(pth):os.remove(pth)
	if os.path.exists(_m):os.remove(_m)
	for x in model_changes:
		if os.path.exists(x[_Q]):os.remove(x[_Q])
	if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
	if os.path.exists(_p):os.remove(_p)
print('[7 / 7] - Generating BizHawk RAM watch')
sys.exit()