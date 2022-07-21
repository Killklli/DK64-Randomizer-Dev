'Build the ROM.'
_A3='num_9_unlit'
_A2='num_9_lit'
_A1='num_6_unlit'
_A0='num_6_lit'
_z='do_not_delete_output'
_y='do_not_delete'
_x=') to ROM'
_w='use_zlib'
_v='.rgba32'
_u='homing_crate'
_t='standard_crate'
_s='Chunky'
_r='assets/Non-Code/hash/tiny_palette.png'
_q='Tiny Overalls Palette'
_p='assets/Non-Code/credits'
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
_c='rb'
_b='target_uncompressed_size'
_a='do_not_recompress'
_Z='.bin'
_Y='state'
_X='number'
_W='encoded_filename'
_V='start'
_U='coins'
_T='offset'
_S='map_folder'
_R='model_index'
_Q='bps'
_P='model_file'
_O='do_not_extract'
_N='use_external_gzip'
_M='do_not_compress'
_L='do_not_delete_source'
_K='big'
_J='target_compressed_size'
_I='output_file'
_H='index'
_G='rgba5551'
_F='texture_format'
_E=True
_D='file_index'
_C='pointer_table_index'
_B='name'
_A='source_file'
import gzip,os,shutil,subprocess,sys,zlib,json,generate_watch_file,patch_text
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
from generate_yellow_wrinkly import generateYellowWrinkly
import model_fix,instance_script_maker
ROMName='rom/dk64.z64'
newROMName='rom/dk64-randomizer-base.z64'
if os.path.exists(newROMName):os.remove(newROMName)
shutil.copyfile(ROMName,newROMName)
portal_images=[]
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_1.png'))
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_2.png'))
createTextFile(_p)
createSquishFile(_p)
generateYellowWrinkly()
file_dict=[{_B:'Static ASM Code',_V:70640,_j:726500,_A:'StaticCode.bin',_N:_E,_g:patchStaticCode},{_B:'Dolby Logo',_C:14,_D:176,_A:'assets/Non-Code/Dolby/DolbyThin.png',_F:_k},{_B:'Thumb Image',_C:14,_D:94,_A:'assets/Non-Code/Nintendo Logo/Nintendo4.png',_F:_G},{_B:'DKTV Image',_C:14,_D:44,_A:'assets/Non-Code/DKTV/logo3.png',_F:_G},{_B:'Spin Transition Image',_C:14,_D:95,_A:'assets/Non-Code/transition/transition-body.png',_F:_k},{_B:'Moves Image',_C:14,_D:115,_A:'assets/Non-Code/file_screen/moves.png',_F:_G},{_B:'Blueprint Image',_C:14,_D:116,_A:'assets/Non-Code/file_screen/blueprint.png',_F:_G},{_B:'Tag Barrel Shell Texture',_C:25,_D:4938,_A:'assets/Non-Code/tagbarrel/shell.png',_F:_G},{_B:'Gong Geometry',_C:4,_D:195,_A:'assets/Non-Code/Gong/gong_geometry.bin',_l:'assets/Non-Code/Gong/gong_geometry.bps',_h:_E},{_B:'No Face',_C:14,_D:33,_A:'assets/Non-Code/displays/none.png',_F:_d},{_B:'Shared Face',_C:14,_D:39,_A:'assets/Non-Code/displays/shared.png',_F:_d},{_B:'Sold Out Face',_C:14,_D:40,_A:'assets/Non-Code/displays/soldout32.png',_F:_d},{_B:'End Sequence Credits',_C:19,_D:7,_A:'assets/Non-Code/credits/credits.bin',_L:_E},{_B:'DK Wrinkly Door',_C:4,_D:240,_A:_m,_L:_E},{_B:'WXY_Slash',_C:14,_D:12,_A:'assets/Non-Code/displays/wxys.png',_F:_G},{_B:'DK Tie Palette',_C:25,_D:6013,_A:'assets/Non-Code/hash/dk_tie_palette.png',_O:_E,_F:_G,_J:32*32*2},{_B:_q,_C:25,_D:6014,_A:_r,_O:_E,_F:_G,_J:32*32*2},{_B:_q,_C:25,_D:6014,_A:_r,_O:_E,_F:_G,_J:32*32*2},{_B:'DPad Image',_C:14,_D:187,_A:'assets/Non-Code/displays/dpad.png',_F:_G}]
number_game_changes=[{_X:6,_Y:'unlit',_e:520},{_X:6,_Y:'lit',_e:521},{_X:9,_Y:'unlit',_e:526},{_X:9,_Y:'lit',_e:527}]
for num in number_game_changes:file_dict.append({_B:f"Number Game ({num[_X]}, {num[_Y]})",_C:7,_D:num[_e],_A:f"assets/Non-Code/displays/num_{num[_X]}_{num[_Y]}.png",_F:_G,_M:_E})
kong_names=['DK','Diddy','Lanky','Tiny',_s]
ammo_names=[_t,_u]
for (ammo_index,ammo) in enumerate(ammo_names):file_dict.append({_B:f"{ammo.replace('_',' ')} Image",_C:14,_D:188+ammo_index,_A:f"assets/Non-Code/displays/{ammo}.png",_F:_G})
for (kong_index,kong) in enumerate(kong_names):
	for (x_i,x) in enumerate([_d,_G]):file_dict.append({_B:f"{kong} Face ({x})",_C:14,_D:[34+kong_index,190+kong_index][x_i],_A:f"assets/Non-Code/displays/{kong.lower()}_face.png",_F:x})
base_coin_sfx='assets/Non-Code/music/Win95_startup.dk64song'
new_coin_sfx='assets/Non-Code/music/coin_sfx.bin'
if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
shutil.copyfile(base_coin_sfx,new_coin_sfx)
map_replacements=[]
song_replacements=[{_B:'baboon_balloon',_H:107,_Q:_E},{_B:'bonus_minigames',_H:8,_Q:_E},{_B:'dk_rap',_H:75,_Q:_E},{_B:'failure_races_try_again',_H:87,_Q:_E},{_B:'move_get',_H:114,_Q:_E},{_B:'nintendo_logo',_H:174,_Q:_E},{_B:'success_races',_H:86,_Q:_E},{_B:'coin_sfx',_H:7,_Q:_i}]
changed_song_indexes=[]
for song in song_replacements:
	item={_B:song[_B].replace('_',' '),_C:0,_D:song[_H],_A:f"assets/Non-Code/music/{song[_B]}.bin",_J:11742}
	if song[_Q]:item[_h]=_E;item[_l]=f"assets/Non-Code/music/{song[_B]}.bps"
	else:item[_L]=_E;item[_O]=_E
	file_dict.append(item);changed_song_indexes.append(song[_H])
with open('./instance_scripts_data.json','r')as json_f:instance_script_maps=json.load(json_f)
for x in instance_script_maps:file_dict.append({_B:f"{x[_B].replace('_',' ')} Instance Scripts",_C:10,_D:x['map'],_A:f"{x[_B]}.raw",_L:_E})
for x in range(175):
	if x>0:
		if x not in changed_song_indexes:file_dict.append({_B:'Song '+str(x),_C:0,_D:x,_A:'song'+str(x)+_Z,_J:11742})
for x in range(6):file_dict.append({_B:'DKTV Inputs '+str(x),_C:17,_D:x,_A:'dktv'+str(x)+_Z,_J:1816})
for x in range(221):file_dict.append({_B:'Zones for map '+str(x),_C:18,_D:x,_A:'lz'+str(x)+_Z,_J:2128,_a:_E})
for x in range(221):file_dict.append({_B:'Setup for map '+str(x),_C:9,_D:x,_A:'setup'+str(x)+_Z,_J:32768,_b:32768,_a:_E})
for x in range(221):file_dict.append({_B:'Character Spawners for map '+str(x),_C:16,_D:x,_A:'charspawners'+str(x)+_Z,_J:5120,_b:5120,_a:_E})
for x in range(8):file_dict.append({_B:'Key '+str(x+1)+' file screen',_C:14,_D:107+x,_A:'assets/Non-Code/file_screen/key'+str(x+1)+_f,_F:_G})
for x in range(43):
	if x!=13:
		if x!=32:
			if x!=24:file_dict.append({_B:'Text '+str(x),_C:12,_D:x,_A:'text'+str(x)+_Z,_J:8192,_b:8192,_a:_E})
for x in range(10):file_dict.append({_B:f"Tag Barrel Bottom Texture ({x+1})",_C:25,_D:4749+x,_A:'assets/Non-Code/tagbarrel/bottom.png',_F:_G})
for x in range(4761,4768):file_dict.append({_B:f"Portal Ripple Texture ({x})",_C:25,_D:x,_A:'assets/Non-Code/displays/empty44.png',_F:_G})
barrel_faces=['Dk','Diddy','Lanky','Tiny',_s]
barrel_offsets=[4817,4815,4819,4769,4747]
for x in range(5):
	for y in range(2):file_dict.append({_B:f"{barrel_faces[x]} Transform Barrel Shell ({y+1})",_C:25,_D:barrel_offsets[x]+y,_A:f"assets/Non-Code/tagbarrel/{barrel_faces[x]} barrel {y}a.png",_F:_G})
kong_palettes=[3724,3686,3689,3769,3687,3826,3847]
for x in kong_palettes:
	x_s=32*32*2
	if x==3769:x_s=43*32*2
	file_dict.append({_B:f"Palette Expansion ({hex(x)})",_C:25,_D:x,_A:f"palette_{x}.bin",_J:x_s})
model_changes=[{_R:0,_P:'diddy_base.bin'},{_R:1,_P:'diddy_ins.bin'},{_R:5,_P:'lanky_base.bin'},{_R:6,_P:'lanky_ins.bin'},{_R:3,_P:'dk_base.bin'},{_R:8,_P:'tiny_base.bin'},{_R:9,_P:'tiny_ins.bin'}]
for x in model_changes:file_dict.append({_B:f"Model {x[_R]}",_C:5,_D:x[_R],_A:x[_P],_L:_E})
portal_image_order=[['SE','NE','SW','NW'],['NW','SW','NE','SE']]
for x in range(2):
	order=portal_image_order[x];image_series=portal_images[x]
	for y in range(4):
		segment=order[y];found_image=''
		for image in image_series:
			if segment in image:found_image=image
		if found_image!='':file_dict.append({_B:f"Portal Image {x+1} - {segment}",_C:7,_D:931+4*x+y,_A:found_image,_F:_G,_M:_E})
hash_icons=['bongos.png','crown.png','dkcoin.png','fairy.png','guitar.png','nin_coin.png','orange.png','rainbow_coin.png','rw_coin.png','sax.png']
hash_indexes=[48,49,50,51,55,62,63,64,65,76]
for x in range(len(hash_indexes)):idx=hash_indexes[x];file_dict.append({_B:f"Hash Icon {x+1}",_C:14,_D:idx,_A:f"assets/Non-Code/hash/{hash_icons[x]}",_F:_G})
file_dict.append({_B:'Dolby Text',_C:12,_D:13,_A:'dolby_text.bin',_M:_E,_L:_E})
file_dict.append({_B:'Custom Text',_C:12,_D:32,_A:'custom_text.bin',_M:_E,_L:_E})
file_dict.append({_B:'DK Text',_C:12,_D:24,_A:'dk_text.bin',_M:_E,_L:_E})
print('DK64 Extractor')
with open(ROMName,_c)as fh:
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
					if y[_H]==1:
						with open(x[_S]+y[_W],_c)as fg:byte_read=fg.read(10);should_compress_walls=byte_read[9]&1!=0;should_compress_floors=byte_read[9]&2!=0
						found_geometry=_E
					elif y[_H]==2:found_walls=_E
					elif y[_H]==3:found_floors=_E
			walls_floors_geometry_valid=found_geometry==found_walls and found_geometry==found_floors
			if not walls_floors_geometry_valid:print('  - WARNING: In map replacement: '+x[_B]);print('    - Need all 3 files present to replace walls, floors, and geometry.');print('    - Only found 1 or 2 of them out of 3. Make sure all 3 exist on disk.');print('    - Will skip replacing walls, floors, and geometry to prevent crashes.')
			for y in pointer_tables:
				if _W not in y:continue
				if os.path.exists(x[_S]+y[_W]):
					if y[_H]in[1,2,3]and not walls_floors_geometry_valid:continue
					do_not_compress=_M in y and y[_M]
					if y[_H]==2:do_not_compress=not should_compress_walls
					elif y[_H]==3:do_not_compress=not should_compress_floors
					print('  - Found '+x[_S]+y[_W]);file_dict.append({_B:x[_B]+y[_B],_C:y[_H],_D:x['map_index'],_A:x[_S]+y[_W],_O:_E,_M:do_not_compress,_N:_N in y and y[_N]})
	print('[2 / 7] - Extracting files from ROM')
	for x in file_dict:
		if _F in x:x[_O]=_E;x[_I]=x[_A].replace(_f,'.'+x[_F])
		if _I not in x:x[_I]=x[_A]
		if _N in x and x[_N]:x[_I]=x[_I]+'.gz'
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
			with open(x[_A],_c)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			subprocess.Popen(['build\\flips.exe','--apply',x[_l],x[_A],x[_A]]).wait()
		if _F in x:
			if x[_F]in[_G,'i4',_k,'i8','ia8']:
				result=subprocess.check_output(['./build/n64tex.exe',x[_F],x[_A]])
				if _J in x:x[_A]=x[_A].replace(_f,f".{x[_F]}")
			elif x[_F]==_d:convertToRGBA32(x[_A]);x[_A]=x[_A].replace(_f,_v)
			else:print(' - ERROR: Unsupported texture format '+x[_F])
		if _J in x:
			x[_M]=_E
			if x[_A][:5]=='setup':convertSetup(x[_A])
			with open(x[_A],_c)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			if _a in x and x[_a]:
				compress=bytearray(byte_read)
				if _b in x:
					diff=x[_b]-len(byte_read);byte_append=0
					if diff>0:byte_read+=byte_append.to_bytes(diff,_K)
					compress=bytearray(byte_read);uncompressed_size=x[_b]
			else:
				precomp=gzip.compress(byte_read,compresslevel=9);byte_append=0;diff=x[_J]-len(precomp)
				if diff>0:precomp+=byte_append.to_bytes(diff,_K)
				compress=bytearray(precomp);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			with open(x[_A],'wb')as fg:fg.write(compress)
			x[_I]=x[_A]
		if _N in x and x[_N]:
			if os.path.exists(x[_A]):
				result=subprocess.check_output(['./build/gzip.exe','-f','-n','-k','-q','-9',x[_I].replace('.gz','')])
				if os.path.exists(x[_I]):
					with open(x[_I],'r+b')as outputFile:outputFile.truncate(len(outputFile.read())-8)
		if os.path.exists(x[_I]):
			byte_read=bytes()
			if _J not in x:uncompressed_size=0
			with open(x[_I],_c)as fg:
				byte_read=fg.read()
				if _J not in x:uncompressed_size=len(byte_read)
			if _M in x and x[_M]:compress=bytearray(byte_read)
			elif _N in x and x[_N]:compress=bytearray(byte_read)
			elif _w in x and x[_w]:compressor=zlib.compressobj(zlib.Z_BEST_COMPRESSION,zlib.DEFLATED,25);compress=compressor.compress(byte_read);compress+=compressor.flush();compress=bytearray(compress);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			else:compress=bytearray(gzip.compress(byte_read,compresslevel=9));compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			print(' - Writing '+x[_I]+' ('+hex(len(compress))+_x)
			if _C in x and _D in x:replaceROMFile(fh,x[_C],x[_D],compress,uncompressed_size)
			elif _V in x:
				if isROMAddressOverlay(x[_V]):replaceOverlayData(x[_V],compress)
				else:fh.seek(x[_V]);fh.write(compress)
			else:print("  - WARNING: Can't find address information in file_dict entry to write "+x[_I]+' ('+hex(len(compress))+_x)
		else:print(x[_I]+' does not exist')
		if not(_y in x and x[_y]):
			if not(_z in x and x[_z]):
				if os.path.exists(x[_I])and x[_I]!=x[_A]:os.remove(x[_I])
			if not(_L in x and x[_L]):
				if os.path.exists(x[_A]):os.remove(x[_A])
	print('[5 / 7] - Writing recomputed pointer tables to ROM');writeModifiedPointerTablesToROM(fh);writeModifiedOverlaysToROM(fh);print('[6 / 7] - Dumping details of all pointer tables to rom/build.log');dumpPointerTableDetails('rom/build.log',fh);main_pointer_table_offset=1055824;fh.seek(main_pointer_table_offset+12*4);text_table=main_pointer_table_offset+int.from_bytes(fh.read(4),_K);fh.seek(text_table+19*4);misc_text=main_pointer_table_offset+int.from_bytes(fh.read(4),_K);fh.seek(misc_text+1872);fh.write('?'.encode('ascii'))
	for i in range(21):fh.write('\x00'.encode('ascii'))
	fh.seek(33476640);arr=[]
	for x in range(512):arr.append(0)
	fh.write(bytearray(arr));writeVanillaMoveData(fh);adjustExits(fh);replaceSimSlam(fh);writeVanillaSongData(fh)
	for x in portal_images:
		for y in x:
			if os.path.exists(y):os.remove(y)
	fh.seek(33476640+321);fh.write((0).to_bytes(1,_K));fh.seek(33476640+322);fh.write((1).to_bytes(1,_K));fh.seek(33476640+323);fh.write((0).to_bytes(1,_K));fh.seek(33476640+324);fh.write((2).to_bytes(1,_K));fh.seek(33476640+325);fh.write((0).to_bytes(1,_K));fh.seek(33476640+326);fh.write((3).to_bytes(1,_K));fh.seek(33476640+327);fh.write((1).to_bytes(1,_K));fh.seek(33476640+328);fh.write((4).to_bytes(1,_K));fh.seek(33476640+329);fh.write((2).to_bytes(1,_K));fh.seek(33476640+315);fh.write((1).to_bytes(1,_K));piano_vanilla=[2,1,2,3,4,2,0]
	for (piano_index,piano_key) in enumerate(piano_vanilla):fh.seek(33476640+348+piano_index);fh.write(piano_key.to_bytes(1,_K))
	with open('assets/Non-Code/credits/squish.bin',_c)as squish:fh.seek(33552384);fh.write(squish.read())
	vanilla_coin_reqs=[{_T:300,_U:50},{_T:301,_U:50},{_T:302,_U:10},{_T:303,_U:10},{_T:304,_U:10},{_T:305,_U:50},{_T:306,_U:50},{_T:307,_U:25}]
	for coinreq in vanilla_coin_reqs:fh.seek(33476640+coinreq[_T]);fh.write(coinreq[_U].to_bytes(1,_K))
	for x in hash_icons:
		pth=f"assets/Non-Code/hash/{x}"
		if os.path.exists(pth):os.remove(pth)
	other_remove=[];displays=['dk_face','diddy_face','lanky_face','tiny_face','chunky_face','none','shared','soldout32','wxys','yellow_qmark_0','yellow_qmark_1','empty44',_u,_A0,_A1,_A2,_A3,_t]
	for disp in displays:
		for ext in [_f,_v]:other_remove.append(f"displays/{disp}{ext}")
	for x in range(8):other_remove.append(f"file_screen/key{x+1}.png")
	for x in other_remove:
		pth=f"assets/Non-Code/{x}"
		if os.path.exists(pth):os.remove(pth)
	hash_items=['dk_tie_palette','homing_crate_0','homing_crate_1','num_1_lit','num_1_unlit',_A0,_A1,'num_7_lit','num_7_unlit',_A2,_A3,'standard_crate_0','standard_crate_1','tiny_palette']
	for hash_item in hash_items:
		for f_t in [_G,'png']:
			pth=f"assets/Non-Code/hash/{hash_item}.{f_t}"
			if os.path.exists(pth):os.remove(pth)
	credits_bins=['credits','squish']
	for x in credits_bins:
		pth=f"assets/Non-Code/credits/{x}.bin"
		if os.path.exists(pth):os.remove(pth)
	if os.path.exists(_m):os.remove(_m)
	for x in model_changes:
		if os.path.exists(x[_P]):os.remove(x[_P])
	if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
print('[7 / 7] - Generating BizHawk RAM watch')
sys.exit()