'Set debugging vars to the build.'
_E=' (offset '
_D='- Writing '
_C='test_zone'
_B='rom/dk64-randomizer-base-dev.z64'
_A='special_move_prices'
set_variables={'level_order_rando_on':0,'level_order':[1,5,4,0,6,2,3],'troff_scoff_count':[25,200,300,400,410,420,8],'blocker_normal_count':[2,3,4,5,6,7,8,9],'key_flags':[74,138,168,236,292,317,26],'unlock_kongs':31,'unlock_moves':1,'fast_start_beginning':1,'camera_unlocked':1,'tag_anywhere':1,'fast_start_helm':1,'crown_door_open':0,'coin_door_open':0,'quality_of_life':1,'price_rando_on':1,'k_rool_order':[0,3,1,2,4],'damage_multiplier':0,'fps_on':1,'no_health_refill':0,'slam_prices':[4,5],'gun_prices':[1,2,3,4,5],'instrument_prices':[1,2,3,4,5],'gun_upgrade_prices':[1,2],'ammo_belt_prices':[1,2],'instrument_upgrade_prices':[1,2,3],'move_rando_on':1,'kut_out_kong_order':[0,0,0,0,0],'remove_blockers':127,'resolve_bonus':0,'disable_drops':0,'shop_indicator_on':1,'warp_to_isles_enabled':1,'lobbies_open_bitfield':255,'perma_lose_kongs':0,'jetpac_medal_requirement':1,'starting_kong':0,'free_target_llama':0,'free_source_llama':3,'keys_preturned':1,'short_bosses':1,'fast_warp':1,'activate_all_bananaports':1,'piano_game_order':[5,0,1,3,5,5,3],'dartboard_order':[0,1,2,3,4,5],'fast_gbs':1,'remove_high_requirements':1,'open_level_sections':1,'auto_keys':0,_C:[170,0],'klaptrap_color_bbother':150,'kut_out_phases':[3,2,0],'dpad_visual_enabled':1,_A:[[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6]],'helm_order':[2,3,1,255,255]}
def valtolst(val,size):
	'Convert the values to a list.';B=size;C=[]
	for D in range(B):C.append(0)
	A=val
	for D in range(B):
		if A!=0:C[B-D-1]=int(A%256);A=(A-A%256)/256
	return C
def readFromROM(offset,size):
	'Read from ROM.'
	with open(_B,'rb')as A:A.seek(offset);return int.from_bytes(A.read(size),'big')
def writeToROMNoOffset(offset,value,size,name):
	'Write to ROM without offset.';B=value;A=offset;print(_D+name+_E+hex(A)+') to '+str(B))
	with open(_B,'r+b')as C:C.seek(A);C.write(bytearray(valtolst(B,size)))
def writeToROM(offset,value,size,name):
	'Write byte data to rom.';B=value;A=offset;print(_D+name+_E+hex(A)+') to '+str(B))
	with open(_B,'r+b')as C:C.seek(33476640+A);C.write(bytearray(valtolst(B,size)))
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
		if x==_A:
			for y in struct_data2:
				if x==y[2]:
					size=y[1];offset=y[0]
					for kong in set_variables[_A]:
						for lvl in kong:writeToROM(offset,lvl,size,x);offset+=size
		elif x==_C:
			ptr_table_offset=1055824;lz_table=ptr_table_offset+readFromROM(ptr_table_offset+18*4,4);isles_list=ptr_table_offset+readFromROM(lz_table+34*4,4);isles_list_end=ptr_table_offset+readFromROM(lz_table+34*4+4,4);isles_list_size=int((isles_list_end-isles_list)/56);isles_list+=2
			for lz_index in range(isles_list_size):
				lz_type=readFromROM(isles_list+56*lz_index+16,2);lz_map=readFromROM(isles_list+56*lz_index+18,2);lz_exit=readFromROM(isles_list+56*lz_index+20,2)
				if lz_type==9 and lz_map==176 and lz_exit==0:writeToROMNoOffset(isles_list+56*lz_index+18,set_variables[x][0],2,'Isles -> TGrounds Zone Map');writeToROMNoOffset(isles_list+56*lz_index+20,set_variables[x][1],2,'Isles -> TGrounds Zone Exit')
		else:
			for y in struct_data2:
				if x==y[2]:
					if type(set_variables[x])is int:
						if y[3]==1:writeToROM(y[0],set_variables[x],y[1],x)
					elif type(set_variables[x])is list:
						for z in range(min([int(y[3]),len(set_variables[x])])):writeToROM(y[0]+z*y[1],set_variables[x][z],y[1],x)