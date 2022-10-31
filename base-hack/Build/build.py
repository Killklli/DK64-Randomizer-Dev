'Build the ROM.'
_A5='num_9_unlit'
_A4='num_9_lit'
_A3='num_6_unlit'
_A2='num_6_lit'
_A1='do_not_delete_output'
_A0='do_not_delete'
_z='use_zlib'
_y='.rgba32'
_x='sparkle'
_w='checkered'
_v='homing_crate'
_u='standard_crate'
_t='Chunky'
_s='assets/Non-Code/credits'
_r='helm.bin'
_q='r+b'
_p='decoded_filename'
_o='encoder'
_n='assets/Non-Code/Gong/hint_door.bin'
_m='bps_file'
_l='ia4'
_k='compressed_size'
_j='is_diff_patch'
_i='patcher'
_h='.png'
_g='texture'
_f='rgba32'
_e='state'
_d='number'
_c='.bin'
_b=False
_a='encoded_filename'
_Z='coins'
_Y='offset'
_X='map_folder'
_W='block'
_V='do_not_recompress'
_U='target_uncompressed_size'
_T='bps'
_S='use_external_gzip'
_R='start'
_Q='rb'
_P='do_not_extract'
_O='output_file'
_N='do_not_compress'
_M='model_file'
_L='model_index'
_K='index'
_J='target_compressed_size'
_I='rgba5551'
_H='do_not_delete_source'
_G='texture_format'
_F='big'
_E='file_index'
_D='pointer_table_index'
_C='name'
_B='source_file'
_A=True
import gzip,json,os,shutil,subprocess,sys,zlib,create_helm_geo,generate_watch_file,shop_instance_script
from writeWarpData import generateDefaultPadPairing
import portal_instance_script,instance_script_maker,model_fix,generate_disco_models,model_port,patch_text
from adjust_exits import adjustExits
from convertPortalImage import convertPortalImage
from convertSetup import convertSetup
from end_seq_writer import createSquishFile,createTextFile
from generate_yellow_wrinkly import generateYellowWrinkly
from image_converter import convertToRGBA32
from map_names import maps
from populateSongData import writeVanillaSongData
from recompute_overlays import isROMAddressOverlay,readOverlayOriginalData,replaceOverlayData,writeModifiedOverlaysToROM
from recompute_pointer_table import dumpPointerTableDetails,getFileInfo,make_safe_filename,parsePointerTables,pointer_tables,replaceROMFile,writeModifiedPointerTablesToROM,clampCompressedTextures
from staticcode import patchStaticCode
from vanilla_move_data import writeVanillaMoveData
ROMName='rom/dk64.z64'
newROMName='rom/dk64-randomizer-base.z64'
if os.path.exists(newROMName):os.remove(newROMName)
shutil.copyfile(ROMName,newROMName)
portal_images=[]
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_1.png'))
portal_images.append(convertPortalImage('assets/Non-Code/portals/DK_rando_portal_2.png'))
createTextFile(_s)
createSquishFile(_s)
generateYellowWrinkly()
BLOCK_COLOR_SIZE=64
file_dict=[{_C:'Static ASM Code',_R:70640,_k:726500,_B:'StaticCode.bin',_S:_A,_i:patchStaticCode},{_C:'Dolby Logo',_D:14,_E:176,_B:'assets/Non-Code/Dolby/DolbyThin.png',_G:_l},{_C:'Thumb Image',_D:14,_E:94,_B:'assets/Non-Code/Nintendo Logo/Nintendo4.png',_G:_I},{_C:'DKTV Image',_D:14,_E:44,_B:'assets/Non-Code/DKTV/logo3.png',_G:_I},{_C:'Spin Transition Image',_D:14,_E:95,_B:'assets/Non-Code/transition/transition-body.png',_G:_l},{_C:'Moves Image',_D:14,_E:115,_B:'assets/Non-Code/file_screen/moves.png',_G:_I},{_C:'Blueprint Image',_D:14,_E:116,_B:'assets/Non-Code/file_screen/blueprint.png',_G:_I},{_C:'Tag Barrel Shell Texture',_D:25,_E:4938,_B:'assets/Non-Code/tagbarrel/shell.png',_G:_I},{_C:'Gong Geometry',_D:4,_E:195,_B:'assets/Non-Code/Gong/gong_geometry.bin',_m:'assets/Non-Code/Gong/gong_geometry.bps',_j:_A},{_C:'No Face',_D:14,_E:33,_B:'assets/Non-Code/displays/none.png',_G:_f},{_C:'Shared Face',_D:14,_E:39,_B:'assets/Non-Code/displays/shared.png',_G:_f},{_C:'Sold Out Face',_D:14,_E:40,_B:'assets/Non-Code/displays/soldout32.png',_G:_f},{_C:'End Sequence Credits',_D:19,_E:7,_B:'assets/Non-Code/credits/credits.bin',_H:_A},{_C:'DK Wrinkly Door',_D:4,_E:240,_B:_n,_H:_A},{_C:'WXY_Slash',_D:14,_E:12,_B:'assets/Non-Code/displays/wxys.png',_G:_I},{_C:'DK Tie Palette',_D:25,_E:6013,_B:'assets/Non-Code/hash/dk_tie_palette.png',_P:_A,_G:_I,_J:BLOCK_COLOR_SIZE},{_C:'Tiny Overalls Palette',_D:25,_E:6014,_B:'assets/Non-Code/hash/tiny_palette.png',_P:_A,_G:_I,_J:BLOCK_COLOR_SIZE},{_C:'DPad Image',_D:14,_E:187,_B:'assets/Non-Code/displays/dpad.png',_G:_I},{_C:'Tracker Image',_D:14,_E:161,_B:'assets/Non-Code/file_screen/tracker.png',_G:_I},{_C:'Nintendo Coin Model',_D:4,_E:72,_B:'nintendo_coin_om2.bin',_H:_A},{_C:'Rareware Coin Model',_D:4,_E:655,_B:'rareware_coin_om2.bin',_H:_A},{_C:'Potion (DK) Model',_D:4,_E:91,_B:'potion_dk_om2.bin',_H:_A},{_C:'Potion (Diddy) Model',_D:4,_E:498,_B:'potion_diddy_om2.bin',_H:_A},{_C:'Potion (Lanky) Model',_D:4,_E:89,_B:'potion_lanky_om2.bin',_H:_A},{_C:'Potion (Tiny) Model',_D:4,_E:499,_B:'potion_tiny_om2.bin',_H:_A},{_C:'Potion (Chunky) Model',_D:4,_E:501,_B:'potion_chunky_om2.bin',_H:_A},{_C:'Potion (Any) Model',_D:4,_E:502,_B:'potion_any_om2.bin',_H:_A},{_C:'Krusha Head',_R:33513472,_B:'assets/Non-Code/displays/krusha_head64.png',_H:_A,_G:_I,_N:_A}]
number_game_changes=[{_d:6,_e:'unlit',_g:520},{_d:6,_e:'lit',_g:521},{_d:9,_e:'unlit',_g:526},{_d:9,_e:'lit',_g:527}]
for num in number_game_changes:file_dict.append({_C:f"Number Game ({num[_d]}, {num[_e]})",_D:7,_E:num[_g],_B:f"assets/Non-Code/displays/num_{num[_d]}_{num[_e]}.png",_G:_I,_N:_A})
for (ci,coin) in enumerate(['nin_coin','rw_coin']):
	for item in range(2):file_dict.append({_C:f"{coin.replace('_',' ').capitalize()} ({item})",_D:25,_E:6015+item+2*ci,_B:f"assets/Non-Code/hash/{coin}_{item}.png",_P:_A,_G:_I})
file_dict.append({_C:'Special Coin Side',_D:25,_E:6019,_B:f"assets/Non-Code/hash/modified_coin_side.png",_P:_A,_G:_I})
kong_names=['DK','Diddy','Lanky','Tiny',_t]
ammo_names=[_u,_v]
for (ammo_index,ammo) in enumerate(ammo_names):file_dict.append({_C:f"{ammo.replace('_',' ')} Image",_D:14,_E:188+ammo_index,_B:f"assets/Non-Code/displays/{ammo}.png",_G:_I})
for (kong_index,kong) in enumerate(kong_names):
	for (x_i,x) in enumerate([_f,_I]):
		size=32*32*2
		if x_i==0:size=32*32*4
		file_dict.append({_C:f"{kong} Face ({x})",_D:14,_E:[34+kong_index,190+kong_index][x_i],_B:f"assets/Non-Code/displays/{kong.lower()}_face.png",_G:x,_J:size})
base_coin_sfx='assets/Non-Code/music/Win95_startup.dk64song'
new_coin_sfx='assets/Non-Code/music/coin_sfx.bin'
if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
shutil.copyfile(base_coin_sfx,new_coin_sfx)
map_replacements=[]
song_replacements=[{_C:'baboon_balloon',_K:107,_T:_A},{_C:'bonus_minigames',_K:8,_T:_A},{_C:'dk_rap',_K:75,_T:_A},{_C:'failure_races_try_again',_K:87,_T:_A},{_C:'move_get',_K:114,_T:_A},{_C:'nintendo_logo',_K:174,_T:_A},{_C:'success_races',_K:86,_T:_A},{_C:'klumsy_celebration',_K:125,_T:_A},{_C:'coin_sfx',_K:7,_T:_b}]
changed_song_indexes=[]
for song in song_replacements:
	item={_C:song[_C].replace('_',' '),_D:0,_E:song[_K],_B:f"assets/Non-Code/music/{song[_C]}.bin",_J:11742}
	if song[_T]:item[_j]=_A;item[_m]=f"assets/Non-Code/music/{song[_C]}.bps"
	else:item[_H]=_A;item[_P]=_A
	file_dict.append(item);changed_song_indexes.append(song[_K])
with open('./instance_scripts_data.json','r')as json_f:instance_script_maps=json.load(json_f)
maps_to_expand=list(range(0,216))
script_expansion_size=512
for x in instance_script_maps:
	maps_to_expand.remove(x['map']);script_file_name=f"{x[_C]}.raw";expand_size=8192
	with open(script_file_name,_Q)as script_f:data=script_f.read();compress=gzip.compress(data,compresslevel=9);expand_size=len(data)+script_expansion_size
	file_dict.append({_C:f"{x[_C].replace('_',' ')} Instance Scripts",_D:10,_E:x['map'],_B:script_file_name,_J:expand_size,_U:expand_size,_V:_A,_H:_A})
for x in maps_to_expand:
	with open(ROMName,_Q)as fh:
		fh.seek(1055824+10*4);script_table=1055824+int.from_bytes(fh.read(4),_F);fh.seek(script_table+x*4);item_start=1055824+(int.from_bytes(fh.read(4),_F)&2147483647);item_end=1055824+(int.from_bytes(fh.read(4),_F)&2147483647);fh.seek(item_start);is_compressed=int.from_bytes(fh.read(2),_F)==8075;item_size=item_end-item_start
		if is_compressed:fh.seek(item_start);data=fh.read(item_size);data=zlib.decompress(data,15+32);item_size=len(data)
		file_dict.append({_C:f"Script {x}",_D:10,_E:x,_B:f"script{x}.bin",_J:item_size+script_expansion_size,_U:item_size+script_expansion_size,_V:_A})
for x in range(175):
	if x>0:
		if x not in changed_song_indexes:file_dict.append({_C:'Song '+str(x),_D:0,_E:x,_B:'song'+str(x)+_c,_J:11742})
for x in range(6):file_dict.append({_C:'DKTV Inputs '+str(x),_D:17,_E:x,_B:'dktv'+str(x)+_c,_J:1816})
for x in range(221):file_dict.append({_C:'Zones for map '+str(x),_D:18,_E:x,_B:'lz'+str(x)+_c,_J:2128,_V:_A})
setup_expansion_size=4800
for x in range(221):
	local_expansion=setup_expansion_size
	if x in(0,1,2,5,9,15,25):local_expansion=0
	with open(ROMName,_Q)as fh:
		setup_tbl_index=9;fh.seek(1055824+setup_tbl_index*4);script_table=1055824+int.from_bytes(fh.read(4),_F);fh.seek(script_table+x*4);item_start=1055824+(int.from_bytes(fh.read(4),_F)&2147483647);item_end=1055824+(int.from_bytes(fh.read(4),_F)&2147483647);fh.seek(item_start);is_compressed=int.from_bytes(fh.read(2),_F)==8075;item_size=item_end-item_start
		if is_compressed:fh.seek(item_start);data=fh.read(item_size);data=zlib.decompress(data,15+32);item_size=len(data)
		file_dict.append({_C:'Setup for map '+str(x),_D:9,_E:x,_B:'setup'+str(x)+_c,_J:item_size+local_expansion,_U:item_size+local_expansion,_V:_A})
for x in range(221):
	if x!=2:file_dict.append({_C:'Paths for map '+str(x),_D:15,_E:x,_B:'paths'+str(x)+_c,_U:1536,_J:1536,_V:_A})
for x in range(221):file_dict.append({_C:'Character Spawners for map '+str(x),_D:16,_E:x,_B:'charspawners'+str(x)+_c,_J:5120,_U:5120,_V:_A})
for x in range(8):file_dict.append({_C:'Key '+str(x+1)+' file screen',_D:14,_E:107+x,_B:'assets/Non-Code/file_screen/key'+str(x+1)+_h,_G:_I})
for x in range(43):
	if x not in(13,32,24,39,8,37,2):file_dict.append({_C:'Text '+str(x),_D:12,_E:x,_B:'text'+str(x)+_c,_J:8192,_U:8192,_V:_A})
for x in range(10):file_dict.append({_C:f"Tag Barrel Bottom Texture ({x+1})",_D:25,_E:4749+x,_B:'assets/Non-Code/tagbarrel/bottom.png',_G:_I})
for x in range(4761,4768):file_dict.append({_C:f"Portal Ripple Texture ({x})",_D:25,_E:x,_B:f"assets/Non-Code/displays/empty11.png",_G:_I})
for x in range(2896,2902):file_dict.append({_C:f"Unused Texture ({x})",_D:25,_E:x,_B:f"assets/Non-Code/displays/empty11.png",_G:_I})
for x in range(3537,3542):file_dict.append({_C:f"Unused Texture ({x})",_D:25,_E:x,_B:f"assets/Non-Code/displays/empty11.png",_G:_I})
barrel_faces=['Dk','Diddy','Lanky','Tiny',_t]
barrel_offsets=[4817,4815,4819,4769,4747]
for x in range(5):
	for y in range(2):file_dict.append({_C:f"{barrel_faces[x]} Transform Barrel Shell ({y+1})",_D:25,_E:barrel_offsets[x]+y,_B:f"assets/Non-Code/tagbarrel/{barrel_faces[x]} barrel {y}a.png",_G:_I})
kong_palettes={3724:[(32,32),_W],3686:[(32,32),_W],3689:[(32,32),_W],3769:[(43,32),_w],3687:[(32,32),_W],3826:[(32,32),_W],3847:[(32,32),_W],3734:[(43,32),_w],3777:[(32,32),_x],3778:[(32,32),_x],4971:[(32,32),_W],4966:[(32,32),_W]}
for x in kong_palettes:
	x_s=kong_palettes[x][0][0]*kong_palettes[x][0][1]*2
	if kong_palettes[x][0][0]==32 and kong_palettes[x][0][1]==32 and kong_palettes[x][1]==_W:x_s=BLOCK_COLOR_SIZE
	file_dict.append({_C:f"Palette Expansion ({hex(x)})",_D:25,_E:x,_B:f"palette_{x}.bin",_J:x_s})
for tex in range(627,637):file_dict.append({_C:f"Head Expansion ({hex(tex)})",_D:25,_E:tex,_B:f"head_{tex}.bin",_J:32*64*2})
colorblind_changes=[[4120,4124,32,44],[5819,5858,32,64]]
for change in colorblind_changes:
	for file_index in range(change[0],change[1]+1):file_dict.append({_C:f"Colorblind Expansion {file_index}",_D:25,_E:file_index,_B:f"colorblind_exp_{file_index}.bin",_J:2*change[2]*change[3]})
model_changes=[{_L:0,_M:'diddy_base.bin'},{_L:1,_M:'diddy_ins.bin'},{_L:5,_M:'lanky_base.bin'},{_L:6,_M:'lanky_ins.bin'},{_L:3,_M:'dk_base.bin'},{_L:8,_M:'tiny_base.bin'},{_L:9,_M:'tiny_ins.bin'},{_L:236,_M:'disco_instrument.bin'},{_L:218,_M:'krusha_base.bin'},{_L:237,_M:'potion_dk_om1.bin'},{_L:238,_M:'potion_diddy_om1.bin'},{_L:239,_M:'potion_lanky_om1.bin'},{_L:240,_M:'potion_tiny_om1.bin'},{_L:241,_M:'potion_chunky_om1.bin'},{_L:242,_M:'potion_any_om1.bin'}]
for x in model_changes:
	data={_C:f"Model {x[_L]}",_D:5,_E:x[_L],_B:x[_M],_H:_A}
	if x[_L]>235:data[_P]=_A
	file_dict.append(data)
portal_image_order=[['SE','NE','SW','NW'],['NW','SW','NE','SE']]
for x in range(2):
	order=portal_image_order[x];image_series=portal_images[x]
	for y in range(4):
		segment=order[y];found_image=''
		for image in image_series:
			if segment in image:found_image=image
		if found_image!='':file_dict.append({_C:f"Portal Image {x+1} - {segment}",_D:7,_E:931+4*x+y,_B:found_image,_G:_I,_N:_A})
hash_icons=['bongos.png','crown.png','dkcoin.png','fairy.png','guitar.png','nin_coin.png','orange.png','rainbow_coin.png','rw_coin.png','sax.png']
hash_indexes=[48,49,50,51,55,62,63,64,65,76]
for x in range(len(hash_indexes)):idx=hash_indexes[x];file_dict.append({_C:f"Hash Icon {x+1}",_D:14,_E:idx,_B:f"assets/Non-Code/hash/{hash_icons[x]}",_G:_I})
file_dict.append({_C:'Dolby Text',_D:12,_E:13,_B:'dolby_text.bin',_N:_A,_H:_A})
file_dict.append({_C:'Custom Text',_D:12,_E:32,_B:'custom_text.bin',_N:_A,_H:_A})
file_dict.append({_C:'DK Text',_D:12,_E:24,_B:'dk_text.bin',_N:_A,_H:_A})
file_dict.append({_C:'Move Names Text',_D:12,_E:39,_B:'move_names.bin',_N:_A,_H:_A})
file_dict.append({_C:'Cranky Text',_D:12,_E:8,_B:'cranky_text.bin',_N:_A,_H:_A})
file_dict.append({_C:'Menu Text',_D:12,_E:37,_B:'menu_text.bin',_N:_A,_H:_A})
file_dict.append({_C:'Kong Name Text',_D:12,_E:2,_B:'kongname_text.bin',_N:_A,_H:_A})
with open(ROMName,_Q)as fh:adjustExits(fh)
for x in range(216):
	if os.path.exists(f"exit{x}.bin"):file_dict.append({_C:f"Map {x} Exits",_D:23,_E:x,_B:f"exit{x}.bin",_N:_A,_H:_A})
print('\nDK64 Extractor\nBuilt by Isotarge')
with open(ROMName,_Q)as fh:
	print('[1 / 7] - Parsing pointer tables');parsePointerTables(fh);readOverlayOriginalData(fh)
	for x in map_replacements:
		print(' - Processing map replacement '+x[_C])
		if os.path.exists(x[_X]):
			found_geometry=_b;found_floors=_b;found_walls=_b;should_compress_walls=_A;should_compress_floors=_A
			for y in pointer_tables:
				if _a not in y:continue
				if _o in y and callable(y[_o]):
					if _p in y and os.path.exists(x[_X]+y[_p]):y[_o](x[_X]+y[_p],x[_X]+y[_a])
				if os.path.exists(x[_X]+y[_a]):
					if y[_K]==1:
						with open(x[_X]+y[_a],_Q)as fg:byte_read=fg.read(10);should_compress_walls=byte_read[9]&1!=0;should_compress_floors=byte_read[9]&2!=0
						found_geometry=_A
					elif y[_K]==2:found_walls=_A
					elif y[_K]==3:found_floors=_A
			walls_floors_geometry_valid=found_geometry==found_walls and found_geometry==found_floors
			if not walls_floors_geometry_valid:print('  - WARNING: In map replacement: '+x[_C]);print('    - Need all 3 files present to replace walls, floors, and geometry.');print('    - Only found 1 or 2 of them out of 3. Make sure all 3 exist on disk.');print('    - Will skip replacing walls, floors, and geometry to prevent crashes.')
			for y in pointer_tables:
				if _a not in y:continue
				if os.path.exists(x[_X]+y[_a]):
					if y[_K]in[1,2,3]and not walls_floors_geometry_valid:continue
					do_not_compress=_N in y and y[_N]
					if y[_K]==2:do_not_compress=not should_compress_walls
					elif y[_K]==3:do_not_compress=not should_compress_floors
					print('  - Found '+x[_X]+y[_a]);file_dict.append({_C:x[_C]+y[_C],_D:y[_K],_E:x['map_index'],_B:x[_X]+y[_a],_P:_A,_N:do_not_compress,_S:_S in y and y[_S]})
	print('[2 / 7] - Extracting files from ROM')
	for x in file_dict:
		if _G in x:x[_P]=_A;x[_O]=x[_B].replace(_h,'.'+x[_G])
		if _O not in x:x[_O]=x[_B]
		if _S in x and x[_S]:x[_O]=x[_O]+'.gz'
		if _P in x and x[_P]:x[_H]=_A
		if not(_P in x and x[_P]):
			byte_read=bytes()
			if _D in x and _E in x:
				file_info=getFileInfo(x[_D],x[_E])
				if file_info:x[_R]=file_info['new_absolute_address'];x[_k]=len(file_info['data'])
			if _R not in x:print(x)
			fh.seek(x[_R]);byte_read=fh.read(x[_k])
			if not(_H in x and x[_H]):
				if os.path.exists(x[_B]):os.remove(x[_B])
				with open(x[_B],'wb')as fg:
					fh.seek(x[_R])
					if int.from_bytes(fh.read(2),_F)==8075:dec=zlib.decompress(byte_read,15+32)
					else:dec=byte_read
					fg.write(dec)
print('[3 / 7] - Patching Extracted Files')
for x in file_dict:
	if _i in x and callable(x[_i]):print(' - Running patcher for '+x[_B]);x[_i](x[_B])
with open(newROMName,_q)as fh:
	print('[4 / 7] - Writing patched files to ROM');clampCompressedTextures(fh,6030)
	for x in file_dict:
		if _j in x and x[_j]:
			with open(x[_B],_Q)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			subprocess.Popen(['build\\flips.exe','--apply',x[_m],x[_B],x[_B]]).wait()
		if _G in x:
			if x[_G]in[_I,'i4',_l,'i8','ia8']:
				result=subprocess.check_output(['./build/n64tex.exe',x[_G],x[_B]])
				if _J in x:x[_B]=x[_B].replace(_h,f".{x[_G]}")
			elif x[_G]==_f:convertToRGBA32(x[_B]);x[_B]=x[_B].replace(_h,_y)
			else:print(' - ERROR: Unsupported texture format '+x[_G])
		if _J in x:
			x[_N]=_A
			if x[_B][:5]=='setup':convertSetup(x[_B])
			with open(x[_B],_Q)as fg:byte_read=fg.read();uncompressed_size=len(byte_read)
			if _V in x and x[_V]:
				compress=bytearray(byte_read)
				if _U in x:
					diff=x[_U]-len(byte_read);byte_append=0
					if diff>0:byte_read+=byte_append.to_bytes(diff,_F)
					compress=bytearray(byte_read);uncompressed_size=x[_U]
			else:
				precomp=gzip.compress(byte_read,compresslevel=9);byte_append=0;diff=x[_J]-len(precomp)
				if diff>0:precomp+=byte_append.to_bytes(diff,_F)
				compress=bytearray(precomp);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			with open(x[_B],'wb')as fg:fg.write(compress)
			x[_O]=x[_B]
		if _S in x and x[_S]:
			if os.path.exists(x[_B]):
				result=subprocess.check_output(['./build/gzip.exe','-f','-n','-k','-q','-9',x[_O].replace('.gz','')])
				if os.path.exists(x[_O]):
					with open(x[_O],_q)as outputFile:outputFile.truncate(len(outputFile.read())-8)
		if os.path.exists(x[_O]):
			byte_read=bytes()
			if _J not in x:uncompressed_size=0
			with open(x[_O],_Q)as fg:
				byte_read=fg.read()
				if _J not in x:uncompressed_size=len(byte_read)
			if _N in x and x[_N]:compress=bytearray(byte_read)
			elif _S in x and x[_S]:compress=bytearray(byte_read)
			elif _z in x and x[_z]:compressor=zlib.compressobj(zlib.Z_BEST_COMPRESSION,zlib.DEFLATED,25);compress=compressor.compress(byte_read);compress+=compressor.flush();compress=bytearray(compress);compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			else:compress=bytearray(gzip.compress(byte_read,compresslevel=9));compress[4]=0;compress[5]=0;compress[6]=0;compress[7]=0
			print(' - Writing '+x[_O]+' ('+hex(len(compress))+') to ROM')
			if _D in x and _E in x:replaceROMFile(fh,x[_D],x[_E],compress,uncompressed_size)
			elif _R in x:
				if isROMAddressOverlay(x[_R]):replaceOverlayData(x[_R],compress)
				else:fh.seek(x[_R]);fh.write(compress)
			else:print("  - WARNING: Can't find address information in file_dict entry to write "+x[_O]+' ('+hex(len(compress))+') to ROM')
		else:print(x[_O]+' does not exist')
		if not(_A0 in x and x[_A0]):
			if not(_A1 in x and x[_A1]):
				if os.path.exists(x[_O])and x[_O]!=x[_B]:os.remove(x[_O])
			if not(_H in x and x[_H]):
				if os.path.exists(x[_B]):os.remove(x[_B])
	print('[5 / 7] - Writing recomputed pointer tables to ROM');writeModifiedPointerTablesToROM(fh);writeModifiedOverlaysToROM(fh);print('[6 / 7] - Dumping details of all pointer tables to rom/build.log');dumpPointerTableDetails('rom/build.log',fh);main_pointer_table_offset=1055824;fh.seek(main_pointer_table_offset+4);geo_table=main_pointer_table_offset+int.from_bytes(fh.read(4),_F);fh.seek(geo_table+17*4);helm_geo=main_pointer_table_offset+int.from_bytes(fh.read(4),_F);helm_geo_end=main_pointer_table_offset+int.from_bytes(fh.read(4),_F);helm_geo_size=helm_geo_end-helm_geo;fh.seek(helm_geo)
	for by_i in range(helm_geo_size):fh.write((0).to_bytes(1,_F))
	fh.seek(helm_geo)
	with open(_r,_Q)as helm_geo:fh.write(gzip.compress(helm_geo.read(),compresslevel=9))
	main_pointer_table_offset=1055824;fh.seek(main_pointer_table_offset+12*4);text_table=main_pointer_table_offset+int.from_bytes(fh.read(4),_F);fh.seek(text_table+19*4);misc_text=main_pointer_table_offset+int.from_bytes(fh.read(4),_F);fh.seek(misc_text+1872);fh.write('?'.encode('ascii'))
	for i in range(21):fh.write('\x00'.encode('ascii'))
	fh.seek(33476640);arr=[]
	for x in range(512):arr.append(0)
	fh.write(bytearray(arr));writeVanillaMoveData(fh);adjustExits(fh);generateDefaultPadPairing(fh);writeVanillaSongData(fh);fh.seek(33476640+286);fh.write((1).to_bytes(1,_F));fh.seek(33476640+284);fh.write((255).to_bytes(1,_F))
	for x in portal_images:
		for y in x:
			if os.path.exists(y):os.remove(y)
	fh.seek(33476640+337);fh.write((0).to_bytes(1,_F));fh.seek(33476640+338);fh.write((1).to_bytes(1,_F));fh.seek(33476640+339);fh.write((0).to_bytes(1,_F));fh.seek(33476640+340);fh.write((2).to_bytes(1,_F));fh.seek(33476640+341);fh.write((0).to_bytes(1,_F));fh.seek(33476640+342);fh.write((3).to_bytes(1,_F));fh.seek(33476640+343);fh.write((1).to_bytes(1,_F));fh.seek(33476640+344);fh.write((4).to_bytes(1,_F));fh.seek(33476640+345);fh.write((2).to_bytes(1,_F));pkmn_snap_enemies=[_A,_A,_A,_A,_A,_A,_A,_A,_A,_b,_b,_A,_A,_A,_A,_A,_A,_A,_A,_A,_b,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A,_A];values=[0,0,0,0,0]
	for (pi,p) in enumerate(pkmn_snap_enemies):
		if p is _A:offset=pi>>3;shift=pi&7;values[offset]|=1<<shift
	fh.seek(33476640+279)
	for x in range(5):fh.write(values[x].to_bytes(1,_F))
	fh.seek(33492992)
	for level_index in range(8):
		for bp_item in (78,75,77,79,76):fh.write(bp_item.to_bytes(1,_F))
	fh.seek(33493120)
	for medal_item in range(40):fh.write((5).to_bytes(1,_F))
	fh.seek(33493184)
	for crown_item in range(10):fh.write((86).to_bytes(1,_F))
	fh.seek(33493200)
	for crown_item in range(8):fh.write((72).to_bytes(1,_F))
	fh.seek(33476640+276)
	for x in range(2):fh.write((45).to_bytes(1,_F))
	fh.seek(33476640+331);fh.write((1).to_bytes(1,_F));piano_vanilla=[2,1,2,3,4,2,0]
	for (piano_index,piano_key) in enumerate(piano_vanilla):fh.seek(33476640+364+piano_index);fh.write(piano_key.to_bytes(1,_F))
	dk_face_puzzle_vanilla=[0,3,2,0,1,2,3,2,1];chunky_face_puzzle_vanilla=[0,1,3,1,2,1,3,0,1]
	for face_index in range(9):fh.seek(33476640+382+face_index);fh.write(dk_face_puzzle_vanilla[face_index].to_bytes(1,_F));fh.seek(33476640+391+face_index);fh.write(chunky_face_puzzle_vanilla[face_index].to_bytes(1,_F))
	with open('assets/Non-Code/credits/squish.bin',_Q)as squish:fh.seek(33552384);fh.write(squish.read())
	vanilla_coin_reqs=[{_Y:316,_Z:50},{_Y:317,_Z:50},{_Y:318,_Z:10},{_Y:319,_Z:10},{_Y:320,_Z:10},{_Y:321,_Z:50},{_Y:322,_Z:50},{_Y:323,_Z:25}]
	for coinreq in vanilla_coin_reqs:fh.seek(33476640+coinreq[_Y]);fh.write(coinreq[_Z].to_bytes(1,_F))
	for x in range(5):fh.seek(33476640+x);fh.write(x.to_bytes(1,_F))
	for x in hash_icons:
		pth=f"assets/Non-Code/hash/{x}"
		if os.path.exists(pth):os.remove(pth)
	other_remove=[];displays=['dk_face','diddy_face','lanky_face','tiny_face','chunky_face','none','shared','soldout32','wxys','yellow_qmark_0','yellow_qmark_1','empty44','empty3264',_v,_A2,_A3,_A4,_A5,_u]
	for disp in displays:
		for ext in [_h,_y]:other_remove.append(f"displays/{disp}{ext}")
	for x in range(8):other_remove.append(f"file_screen/key{x+1}.png")
	other_remove.append('file_screen/tracker.png')
	for x in other_remove:
		pth=f"assets/Non-Code/{x}"
		if os.path.exists(pth):os.remove(pth)
	hash_items=['dk_tie_palette','homing_crate_0','homing_crate_1','num_1_lit','num_1_unlit',_A2,_A3,'num_7_lit','num_7_unlit',_A4,_A5,'standard_crate_0','standard_crate_1','tiny_palette','coconut','feather','grape','peanut','pineapple','triangle','trombone','modified_coin_side','nin_coin_0','nin_coin_1','rw_coin_0','rw_coin_1','special_coin_side'];script_files=[A[0]for A in os.walk('assets/Non-Code/instance_scripts/')];shop_files=['snide.script','cranky.script','funky.script','candy.script']
	for folder in script_files:
		for file in os.listdir(folder):
			file=f"{folder}/{file}"
			for shop in shop_files:
				if shop in file:
					if os.path.exists(file):os.remove(file)
	for hash_item in hash_items:
		for f_t in [_I,'png']:
			pth=f"assets/Non-Code/hash/{hash_item}.{f_t}"
			if os.path.exists(pth):os.remove(pth)
	credits_bins=['credits','squish']
	for x in credits_bins:
		pth=f"assets/Non-Code/credits/{x}.bin"
		if os.path.exists(pth):os.remove(pth)
	if os.path.exists(_n):os.remove(_n)
	for x in model_changes:
		if os.path.exists(x[_M]):os.remove(x[_M])
	if os.path.exists(new_coin_sfx):os.remove(new_coin_sfx)
	if os.path.exists(_r):os.remove(_r)
	for x in range(216):
		if os.path.exists(f"exit{x}.bin"):os.remove(f"exit{x}.bin")
with open(newROMName,_q)as fh:
	size=len(fh.read());add=16-size%16
	if add!=16:size+=add
	fh.seek(33505280);fh.write(size.to_bytes(4,_F))
print('[7 / 7] - Generating BizHawk RAM watch')
sys.exit()