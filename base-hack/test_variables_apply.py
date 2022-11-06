'Set debugging vars to the build.'
_X=' (offset '
_W='- Writing '
_V='homing_balloons'
_U='hud_bp_multibunch'
_T='rambi_enguarde_pickup'
_S='caves_kosha_dead'
_R='textbox_hold'
_Q='vanilla_fixes'
_P='galleon_star'
_O='cb_indicator'
_N='ammo_swap'
_M='fast_transform'
_L='fast_boot'
_K='dance_skip'
_J='aztec_lobby_bonus'
_I='fast_picture'
_H='remove_cutscenes'
_G='reduce_lag'
_F='test_zone'
_E='r+b'
_D='special_move_prices'
_C='rom/dk64-randomizer-base-dev.z64'
_B='quality_of_life'
_A=True
import os
set_variables={'level_order_rando_on':0,'level_order':[1,5,4,0,6,2,3],'troff_scoff_count':[25,200,300,400,410,420,8],'blocker_normal_count':[2,3,4,5,6,7,8,9],'key_flags':[74,138,168,236,292,317,26],'unlock_kongs':31,'unlock_moves':1,'fast_start_beginning':1,'camera_unlocked':1,'tag_anywhere':1,'fast_start_helm':1,'crown_door_open':0,'coin_door_open':0,_B:{_G:_A,_H:_A,_I:_A,_J:_A,_K:_A,_L:_A,_M:_A,_N:_A,_O:_A,_P:_A,_Q:_A,_R:_A,_S:_A,_T:_A,_U:_A,_V:_A},'price_rando_on':1,'k_rool_order':[1,-1,-1,-1,-1],'damage_multiplier':0,'fps_on':1,'no_health_refill':0,'slam_prices':[4,5],'gun_prices':[1,2,3,4,5],'instrument_prices':[1,2,3,4,5],'gun_upgrade_prices':[1,2],'ammo_belt_prices':[1,2],'instrument_upgrade_prices':[1,2,3],'move_rando_on':1,'kut_out_kong_order':[0,0,0,0,0],'remove_blockers':127,'resolve_bonus':0,'disable_drops':0,'shop_indicator_on':2,'warp_to_isles_enabled':1,'lobbies_open_bitfield':255,'perma_lose_kongs':0,'jetpac_medal_requirement':1,'starting_kong':0,'free_target_llama':0,'free_source_llama':3,'keys_preturned':0,'short_bosses':1,'fast_warp':1,'activate_all_bananaports':1,'piano_game_order':[5,0,1,3,5,5,3],'dartboard_order':[0,1,2,3,4,5],'fast_gbs':1,'remove_high_requirements':1,'open_level_sections':1,'auto_keys':0,_F:[204,0],'klaptrap_color_bbother':150,'kut_out_phases':[3,2,0],'dpad_visual_enabled':1,_D:[[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6]],'tbarrel_prices':[1,2,3,4],'fairy_prices':[3,6],'helm_order':[2,0,255,255,255],'disco_chunky':1,'krusha_slot':2,'helm_hurry_mode':0,'win_condition':5,'version':2,'item_rando':1,'vulture_item':72,'japes_rock_item':76,'medal_cb_req':5,'hard_enemies':1,'remove_oscillation_effects':1}
def valtolst(val,size):
	'Convert the values to a list.';B=size;C=[]
	for D in range(B):C.append(0)
	A=val
	for D in range(B):
		if A!=0:C[B-D-1]=int(A%256);A=(A-A%256)/256
	return C
def readFromROM(offset,size):
	'Read from ROM.'
	with open(_C,'rb')as A:A.seek(offset);return int.from_bytes(A.read(size),'big')
def writeToROMNoOffset(offset,value,size,name):
	'Write to ROM without offset.';B=value;A=offset;print(_W+name+_X+hex(A)+') to '+str(B))
	with open(_C,_E)as C:C.seek(A);C.write(bytearray(valtolst(B,size)))
def writeToROM(offset,value,size,name):
	'Write byte data to rom.';B=value;A=offset;print(_W+name+_X+hex(A)+') to '+str(B))
	with open(_C,_E)as C:C.seek(33476640+A);C.write(bytearray(valtolst(B,size)))
with open('include/variable_space_structs.h','r')as varspace:
	varlines=varspace.readlines();struct_data=[]
	for x in varlines:
		start='ATTR_LINE';y=x.replace('\t',start)
		if y[:9]==start:struct_data.append(x.split(' //')[0].replace('\n','').replace('\t',''))
	struct_data2=[]
	for x in struct_data:
		location=x[3:8];other_info=x[12:].split(' ');other_data=[int(location,16),'','',1]
		for y in range(len(other_info)):
			if y==len(other_info)-1:
				other_data[2]=other_info[y][:-1];count_split=other_data[2].split('[')
				if len(count_split)>1:other_data[2]=count_split[0];other_data[3]=count_split[1].split(']')[0]
			else:other_data[1]+=other_info[y]+' '
		other_data[1]=other_data[1][:-1];data_type=other_data[1]
		if'char'in data_type:other_data[1]=1
		elif'short'in data_type:other_data[1]=2
		elif'int'in data_type:other_data[1]=4
		struct_data2.append(other_data)
	test_keys=set_variables.keys()
	for x in test_keys:
		if x==_D:
			for y in struct_data2:
				if x==y[2]:
					size=y[1];offset=y[0]
					for kong in set_variables[_D]:
						for lvl in kong:writeToROM(offset,lvl,size,x);offset+=size
		elif x==_F:
			ptr_table_offset=1055824;lz_table=ptr_table_offset+readFromROM(ptr_table_offset+18*4,4);isles_list=ptr_table_offset+readFromROM(lz_table+34*4,4);isles_list_end=ptr_table_offset+readFromROM(lz_table+34*4+4,4);isles_list_size=int((isles_list_end-isles_list)/56);isles_list+=2
			for lz_index in range(isles_list_size):
				lz_type=readFromROM(isles_list+56*lz_index+16,2);lz_map=readFromROM(isles_list+56*lz_index+18,2);lz_exit=readFromROM(isles_list+56*lz_index+20,2)
				if lz_type==9 and lz_map==176 and lz_exit==0:writeToROMNoOffset(isles_list+56*lz_index+18,set_variables[x][0],2,'Isles -> TGrounds Zone Map');writeToROMNoOffset(isles_list+56*lz_index+20,set_variables[x][1],2,'Isles -> TGrounds Zone Exit')
		elif x==_B:
			order=[_G,_H,_I,_J,_K,_L,_M,_N,_O,_P,_Q,_R,_S,_T,_U,_V]
			for y in set_variables[_B]:
				if set_variables[_B][y]:index=order.index(y);offset=int(index>>3);check=int(index%8);pre=readFromROM(33476640+176+offset,1);pre_copy=pre;pre|=128>>check;print('');print(f"{y} ({index}): {offset} {check} | {pre_copy} -> {pre}");writeToROM(176+offset,pre,1,y)
		else:
			for y in struct_data2:
				if x==y[2]:
					if type(set_variables[x])is int:
						if y[3]==1:writeToROM(y[0],set_variables[x],y[1],x)
					elif type(set_variables[x])is list:
						for z in range(min([int(y[3]),len(set_variables[x])])):writeToROM(y[0]+z*y[1],set_variables[x][z],y[1],x)
move_csv='move_placement.csv'
permit=False
if os.path.exists(move_csv)and permit:
	with open(move_csv,'r')as csv:
		csv_lines=csv.readlines()
		with open(_C,_E)as rom:
			rom.seek(33484800)
			for x in csv_lines:val=int(x.replace('\n',''));rom.write(val.to_bytes(4,'big'))