'Set debugging vars to the build.'
_A='special_move_prices'
set_variables={'level_order_rando_on':0,'level_order':[1,5,4,0,6,2,3],'troff_scoff_count':[100,200,300,400,410,420,430],'blocker_normal_count':[2,3,4,5,6,7,8,9],'key_flags':[74,138,168,236,292,317,26],'unlock_kongs':0,'unlock_moves':0,'fast_start_beginning':1,'camera_unlocked':0,'tag_anywhere':1,'fast_start_helm':0,'crown_door_open':0,'coin_door_open':0,'quality_of_life':1,'price_rando_on':1,'k_rool_order':[0,3,1,2,4],'damage_multiplier':4,'fps_on':1,'no_health_refill':1,'slam_prices':[4,5],'gun_prices':[1,2,3,4,5],'instrument_prices':[1,2,3,4,5],'gun_upgrade_prices':[1,2],'ammo_belt_prices':[1,2],'instrument_upgrade_prices':[1,2,3],'move_rando_on':1,'dk_crankymoves':[1,33,65,18,18,255,255],'dk_candymoves':[2,34,66,18,18,255,255],'dk_funkymoves':[3,35,67,18,18,255,255],'kut_out_kong_order':[0,0,0,0,0],'remove_blockers':127,'resolve_bonus':3,'disable_drops':1,'shop_indicator_on':1,'warp_to_isles_enabled':1,'lobbies_open_bitfield':255,'perma_lose_kongs':0,'jetpac_medal_requirement':1,'kong_recolor_enabled':1,'dk_color':1,'diddy_color':1,'lanky_color':1,'tiny_color':1,'chunky_color':1,_A:[[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6]]}
def valtolst(val,size):
	'Convert the values to a list.';B=size;C=[]
	for D in range(B):C.append(0)
	A=val
	for D in range(B):
		if A!=0:C[B-D-1]=int(A%256);A=(A-A%256)/256
	return C
def writeToROM(offset,value,size,name):
	'Write byte data to rom.';B=value;A=offset;print('- Writing '+name+' (offset '+hex(A)+') to '+str(B))
	with open('rom/dk64-randomizer-base-dev.z64','r+b')as C:C.seek(33476640+A);C.write(bytearray(valtolst(B,size)))
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
		else:
			for y in struct_data2:
				if x==y[2]:
					if type(set_variables[x])is int:
						if y[3]==1:writeToROM(y[0],set_variables[x],y[1],x)
					elif type(set_variables[x])is list:
						for z in range(min([int(y[3]),len(set_variables[x])])):writeToROM(y[0]+z*y[1],set_variables[x][z],y[1],x)