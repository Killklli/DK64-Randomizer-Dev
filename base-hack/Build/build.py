'Build the ROM.'
_u='do_not_delete_output'
_t='do_not_delete'
_s=') to ROM'
_r='use_zlib'
_q='.rgba32'
_p='Chunky'
_o='assets/Non-Code/hash/tiny_palette.png'
_n='Tiny Overalls Palette'
_m='assets/Non-Code/credits'
_l='decoded_filename'
_k='encoder'
_j='assets/Non-Code/Gong/hint_door.bin'
_i='bps_file'
_h='ia4'
_g='compressed_size'
_f=False
_e='is_diff_patch'
_d='patcher'
_c='.png'
_b='rgba32'
_a='rb'
_Z='target_uncompressed_size'
_Y='do_not_recompress'
_X='.bin'
_W='encoded_filename'
_V='start'
_U='coins'
_T='offset'
_S='map_folder'
_R='model_index'
_Q='bps'
_P='do_not_compress'
_O='model_file'
_N='do_not_extract'
_M='use_external_gzip'
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
createTextFile(_m)
createSquishFile(_m)
generateYellowWrinkly()
file_dict=[{_B:'Static ASM Code',_V:70640,_g:726500,_A:'StaticCode.bin',_M:_E,_d:patchStaticCode},{_B:'Dolby Logo',_C:14,_D:176,_A:'assets/Non-Code/Dolby/DolbyThin.png',_F:_h},{_B:'Thumb Image',_C:14,_D:94,_A:'assets/Non-Code/Nintendo Logo/Nintendo4.png',_F:_G},{_B:'DKTV Image',_C:14,_D:44,_A:'assets/Non-Code/DKTV/logo3.png',_F:_G},{_B:'Spin Transition Image',_C:14,_D:95,_A:'assets/Non-Code/transition/transition-body.png',_F:_h},{_B:'Moves Image',_C:14,_D:115,_A:'assets/Non-Code/file_screen/moves.png',_F:_G},{_B:'Blueprint Image',_C:14,_D:116,_A:'assets/Non-Code/file_screen/blueprint.png',_F:_G},{_B:'Tag Barrel Shell Texture',_C:25,_D:4938,_A:'assets/Non-Code/tagbarrel/shell.png',_F:_G},{_B:'Gong Geometry',_C:4,_D:195,_A:'assets/Non-Code/Gong/gong_geometry.bin',_i:'assets/Non-Code/Gong/gong_geometry.bps',_e:_E},{_B:'No Face',_C:14,_D:33,_A:'assets/Non-Code/displays/none.png',_F:_b},{_B:'Shared Face',_C:14,_D:39,_A:'assets/Non-Code/displays/shared.png',_F:_b},{_B:'Sold Out Face',_C:14,_D:40,_A:'assets/Non-Code/displays/soldout32.png',_F:_b},{_B:'End Sequence Credits',_C:19,_D:7,_A:'assets/Non-Code/credits/credits.bin',_L:_E},{_B:'DK Wrinkly Door',_C:4,_D:240,_A:_j,_L:_E},{_B:'WXY_Slash',_C:14,_D:12,_A:'assets/Non-Code/displays/wxys.png',_F:_G},{_B:'DK Tie Palette',_C:25,_D:6013,_A:'assets/Non-Code/hash/dk_tie_palette.png',_N:_E,_F:_G,_J:32*32*2},{_B:_n,_C:25,_D:6014,_A:_o,_N:_E,_F:_G,_J:32*32*2},{_B:_n,_C:25,_D:6014,_A:_o,_N:_E,_F:_G,_J:32*32*2},{_B:'DPad Image',_C:14,_D:187,_A:'assets/Non-Code/displays/dpad.png',_F:_G}]
kong_names=['DK','Diddy','Lanky','Tiny',_p]
ammo_names=['standard_crate','homing_crate']
for (ammo_index,ammo) in enumerate(ammo_names):file_dict.append({_B:f"{ammo.replace('_',' ')} Image",_C:14,_D:188+ammo_index,_A:f"assets/Non-Code/displays/{ammo}.png",_F:_G})
for (kong_index,kong) in enumerate(kong_names):
	for (x_i,x) in enumerate([_b,_G]):file_dict.append({_B:f"{kong} Face ({x})",_C:14,_D:[34+kong_index,190+kong_index][x_i],_A:f"assets/Non-Code/displays/{kong.lower()}_face.png",_F:x})
base_coin_sfx='assets/Non-Code/music/Win95_startup.dk64song'
new_coin_sfx='assets/Non-Code/music/coin_sfx.bin'
if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
shutil.copyfile(base_coin_sfx,new_coin_sfx)
map_replacements=[]
song_replacements=[{_B:'baboon_balloon',_H:107,_Q:_E},{_B:'bonus_minigames',_H:8,_Q:_E},{_B:'dk_rap',_H:75,_Q:_E},{_B:'failure_races_try_again',_H:87,_Q:_E},{_B:'move_get',_H:114,_Q:_E},{_B:'nintendo_logo',_H:174,_Q:_E},{_B:'success_races',_H:86,_Q:_E},{_B:'coin_sfx',_H:7,_Q:_f}]
changed_song_indexes=[]
for song in song_replacements:
	item={_B:song[_B].replace('_',' '),_C:0,_D:song[_H],_A:f"assets/Non-Code/music/{song[_B]}.bin",_J:11742}
	if song[_Q]:item[_e]=_E;item[_i]=f"assets/Non-Code/music/{song[_B]}.bps"
	else:item[_L]=_E;item[_N]=_E
	file_dict.append(item);changed_song_indexes.append(song[_H])
with open('./instance_scripts_data.json','r')as json_f:instance_script_maps=json.load(json_f)
for x in instance_script_maps:file_dict.append({_B:f"{x[_B].replace('_',' ')} Instance Scripts",_C:10,_D:x['map'],_A:f"{x[_B]}.raw",_L:_E})
for x in range(175):
	if x>0:
		if x not in changed_song_indexes:file_dict.append({_B:'Song '+str(x),_C:0,_D:x,_A:'song'+str(x)+_X,_J:11742})
for x in range(6):file_dict.append({_B:'DKTV Inputs '+str(x),_C:17,_D:x,_A:'dktv'+str(x)+_X,_J:1816})
for x in range(221):file_dict.append({_B:'Zones for map '+str(x),_C:18,_D:x,_A:'lz'+str(x)+_X,_J:2128,_Y:_E})
for x in range(221):file_dict.append({_B:'Setup for map '+str(x),_C:9,_D:x,_A:'setup'+str(x)+_X,_J:32768,_Z:32768,_Y:_E})
for x in range(221):file_dict.append({_B:'Character Spawners for map '+str(x),_C:16,_D:x,_A:'charspawners'+str(x)+_X,_J:5120,_Z:5120,_Y:_E})
for x in range(8):file_dict.append({_B:'Key '+str(x+1)+' file screen',_C:14,_D:107+x,_A:'assets/Non-Code/file_screen/key'+str(x+1)+_c,_F:_G})
for x in range(43):
	if x!=13:
		if x!=32:
			if x!=24:file_dict.append({_B:'Text '+str(x),_C:12,_D:x,_A:'text'+str(x)+_X,_J:8192,_Z:8192,_Y:_E})
for x in range(10):file_dict.append({_B:f"Tag Barrel Bottom Texture ({x+1})",_C:25,_D:4749+x,_A:'assets/Non-Code/tagbarrel/bottom.png',_F:_G})
for x in range(4761,4768):file_dict.append({_B:f"Portal Ripple Texture ({x})",_C:25,_D:x,_A:'assets/Non-Code/displays/empty44.png',_F:_G})
barrel_faces=['Dk','Diddy','Lanky','Tiny',_p]
barrel_offsets=[4817,4815,4819,4769,4747]
for x in range(5):
	for y in range(2):file_dict.append({_B:f"{barrel_faces[x]} Transform Barrel Shell ({y+1})",_C:25,_D:barrel_offsets[x]+y,_A:f"assets/Non-Code/tagbarrel/{barrel_faces[x]} barrel {y}a.png",_F:_G})
kong_palettes=[3724,3686,3689,3769,3687,3826,3847]
for x in kong_palettes:
	x_s=32*32*2
	if x==3769:x_s=43*32*2
	file_dict.append({_B:f"Palette Expansion ({hex(x)})",_C:25,_D:x,_A:f"palette_{x}.bin",_J:x_s})
model_changes=[{_R:0,_O:'diddy_base.bin'},{_R:1,_O:'diddy_ins.bin'},{_R:5,_O:'lanky_base.bin'},{_R:6,_O:'lanky_ins.bin'},{_R:3,_O:'dk_base.bin'},{_R:8,_O:'tiny_base.bin'},{_R:9,_O:'tiny_ins.bin'}]
for x in model_changes:file_dict.append({_B:f"Model {x[_R]}",_C:5,_D:x[_R],_A:x[_O],_L:_E})
portal_image_order=[['SE','NE','SW','NW'],['NW','SW','NE','SE']]
for x in range(2):
	order=portal_image_order[x];image_series=portal_images[x]
	for y in range(4):
		segment=order[y];found_image=''
		for image in image_series:
			if segment in image:found_image=image
		if found_image!='':file_dict.append({_B:f"Portal Image {x+1} - {segment}",_C:7,_D:931+4*x+y,_A:found_image,_F:_G,_P:_E})
hash_icons=['bongos.png','crown.png','dkcoin.png','fairy.png','guitar.png','nin_coin.png','orange.png','rainbow_coin.png','rw_coin.png','sax.png']
hash_indexes=[48,49,50,51,55,62,63,64,65,76]
for x in range(len(hash_indexes)):idx=hash_indexes[x];file_dict.append({_B:f"Hash Icon {x+1}",_C:14,_D:idx,_A:f"assets/Non-Code/hash/{hash_icons[x]}",_F:_G})
file_dict.append({_B:'Dolby Text',_C:12,_D:13,_A:'dolby_text.bin',_P:_E,_L:_E})
file_dict.append({_B:'Custom Text',_C:12,_D:32,_A:'custom_text.bin',_P:_E,_L:_E})
file_dict.append({_B:'DK Text',_C:12,_D:24,_A:'dk_text.bin',_P:_E,_L:_E})
print('DK64 Extractor')
with open(ROMName,_a)as fh:
	print('[1 / 7] - Parsing pointer tables');parsePointerTables(fh);readOverlayOriginalData(fh)
	for x in map_replacements:
		print(' - Processing map replacement '+x[_B])
		if os.path.exists(x[_S]):
			found_geometry=_f;found_floors=_f;found_walls=_f;should_compress_walls=_E;should_compress_floors=_E
			for y in pointer_tables:
				if _W not in y:continue
				if _k in y and callable(y[_k]):
					if _l in y and os.path.exists(x[_S]+y[_l]):y[_k](x[_S]+y[_l],x[_S]+y[_W])
				if os.path.exists(x[_S]+y[_W]):
					if y[_H]==1:
						with open(x[_S]+y[_W],_a)as fg:byte_read=fg.read(10);should_compress_walls=byte_read[9]&1!=0;should_compress_floors=byte_read[9]&2!=0
						found_geometry=_E
					elif y[_H]==2:found_walls=_E
					elif y[_H]==3:found_floors=_E
			walls_floors_geometry_valid=found_geometry==found_walls and found_geometry==found_floors
			if not walls_floors_geometry_valid:print('  - WARNING: In map replacement: '+x[_B]);print('    - Need all 3 files present to replace walls, floors, and geometry.');print('    - Only found 1 or 2 of them out of 3. Make sure all 3 exist on disk.');print('    - Will skip replacing walls, floors, and geometry to prevent crashes.')
			for y in pointer_tables:
				if _W not in y:continue
				if os.path.exists(x[_S]+y[_W]):
					if y[_H]in[1,2,3]and not walls_floors_geometry_valid:continue
					do_not_compress=_P in y and y[_P]
					if y[_H]==2:do_not_compress=not should_compress_walls
					elif y[_H]==3:do_not_compress=not should_compress_floors
					print('  - Found '+x[_S]+y[_W]);file_dict.append({_B:x[_B]+y[_B],_C:y[_H],_D:x['map_index'],_A:x[_S]+y[_W],_N:_E,_P:do_not_compress,_M:_M in y and y[_M]})
	print('[2 / 7] - Extracting files from ROM')
	for x in file_dict:
		if _F in x:x[_N]=_E;x[_I]=x[_A].replace(_c,'.'+x[_F])
		if _I not in x:x[_I]=x[_A]
		if _M in x and x[_M]:x[_I]=x[_I]+'.gz'
		if _N in x and x[_N]:x[_L]=_E
		if not(_N in x and x[_N]):
			byte_read=bytes()
			if _C in x and _D in x:
				file_info=getFileInfo(x[_C],x[_D])
				if file_info:x[_V]=file_info['new_absolute_address'];x[_g]=len(file_info['data'])
			if _V not in x:print(x)
			fh.seek(x[_V]);byte_read=fh.read(x[_g])
			if not(_L in x and x[_L]):
				if os.path.exists(x[_A]):os.remove(x[_A])
				with open(x[_A],'wb')as fg:dec=zlib.decompress(byte_read,15+32);fg.write(dec)
print('[3 / 7] - Patching Extracted Files')
for x in file_dict:
	if _d in x and callable(x[_d]):print(' - Running patcher for '+x[_A]);x[_d](x[_A])
with open(newROMName,'r+b')as fh:
	print('[4 / 7] - Writing patched files to ROM')
	for x in file_dict:
		if _e in x and x[_e]:
			with open(x[_A],_a)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			subprocess.Popen(['build\\flips.exe','--apply',x[_i],x[_A],x[_A]]).wait()
		if _F in x:
			if x[_F]in[_G,'i4',_h,'i8','ia8']:
				result=subprocess.check_output(['./build/n64tex.exe',x[_F],x[_A]])
				if _J in x:x[_A]=x[_A].replace(_c,f".{x[_F]}")
			elif x[_F]==_b:convertToRGBA32(x[_A]);x[_A]=x[_A].replace(_c,_q)
			else:print(' - ERROR: Unsupported texture format '+x[_F])
		if _J in x:
			x[_P]=_E
			if x[_A][:5]=='setup':convertSetup(x[_A])
			with open(x[_A],_a)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			if _Y in x and x[_Y]:
				compress=bytearray(byte_read)
				if _Z in x:
					diff=x[_Z]-len(byte_read);byte_append=0
					if diff>0:byte_read+=byte_append.to_bytes(diff,_K)
					compress=bytearray(byte_read);uncompressed_size=x[_Z]
			else:
				precomp=gzip.compress(byte_read,compresslevel=9);byte_append=0;diff=x[_J]-len(precomp)
				if diff>0:precomp+=byte_append.to_bytes(diff,_K)
				compress=bytearray(precomp);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			with open(x[_A],'wb')as fg:fg.write(compress)
			x[_I]=x[_A]
		if _M in x and x[_M]:
			if os.path.exists(x[_A]):
				result=subprocess.check_output(['./build/gzip.exe','-f','-n','-k','-q','-9',x[_I].replace('.gz','')])
				if os.path.exists(x[_I]):
					with open(x[_I],'r+b')as outputFile:outputFile.truncate(len(outputFile.read())-8)
		if os.path.exists(x[_I]):
			byte_read=bytes()
			if _J not in x:uncompressed_size=0
			with open(x[_I],_a)as fg:
				byte_read=fg.read()
				if _J not in x:uncompressed_size=len(byte_read)
			if _P in x and x[_P]:compress=bytearray(byte_read)
			elif _M in x and x[_M]:compress=bytearray(byte_read)
			elif _r in x and x[_r]:compressor=zlib.compressobj(zlib.Z_BEST_COMPRESSION,zlib.DEFLATED,25);compress=compressor.compress(byte_read);compress+=compressor.flush();compress=bytearray(compress);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			else:compress=bytearray(gzip.compress(byte_read,compresslevel=9));compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			print(' - Writing '+x[_I]+' ('+hex(len(compress))+_s)
			if _C in x and _D in x:replaceROMFile(fh,x[_C],x[_D],compress,uncompressed_size)
			elif _V in x:
				if isROMAddressOverlay(x[_V]):replaceOverlayData(x[_V],compress)
				else:fh.seek(x[_V]);fh.write(compress)
			else:print("  - WARNING: Can't find address information in file_dict entry to write "+x[_I]+' ('+hex(len(compress))+_s)
		else:print(x[_I]+' does not exist')
		if not(_t in x and x[_t]):
			if not(_u in x and x[_u]):
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
	with open('assets/Non-Code/credits/squish.bin',_a)as squish:fh.seek(33552384);fh.write(squish.read())
	vanilla_coin_reqs=[{_T:300,_U:50},{_T:301,_U:50},{_T:302,_U:10},{_T:303,_U:10},{_T:304,_U:10},{_T:305,_U:50},{_T:306,_U:50},{_T:307,_U:25}]
	for coinreq in vanilla_coin_reqs:fh.seek(33476640+coinreq[_T]);fh.write(coinreq[_U].to_bytes(1,_K))
	for x in hash_icons:
		pth=f"assets/Non-Code/hash/{x}"
		if os.path.exists(pth):os.remove(pth)
	other_remove=[];displays=['dk_face','diddy_face','lanky_face','tiny_face','chunky_face','none','shared','soldout32','wxys','yellow_qmark_0','yellow_qmark_1','empty44']
	for disp in displays:
		for ext in [_c,_q]:other_remove.append(f"displays/{disp}{ext}")
	for x in range(8):other_remove.append(f"file_screen/key{x+1}.png")
	for x in other_remove:
		pth=f"assets/Non-Code/{x}"
		if os.path.exists(pth):os.remove(pth)
	credits_bins=['credits','squish']
	for x in credits_bins:
		pth=f"assets/Non-Code/credits/{x}.bin"
		if os.path.exists(pth):os.remove(pth)
	if os.path.exists(_j):os.remove(_j)
	for x in model_changes:
		if os.path.exists(x[_O]):os.remove(x[_O])
	if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
print('[7 / 7] - Generating BizHawk RAM watch')
sys.exit()