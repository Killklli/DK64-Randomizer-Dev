'Extracts data from a ROM regarding coins, balloons and bananas.'
_P='points'
_O='model_two'
_N='speed'
_M='path'
_L='scale'
_K='object_type'
_J='Kongs.chunky'
_I='Kongs.lanky'
_H='Kongs.tiny'
_G='Kongs.donkey'
_F='Kongs.diddy'
_E='objects'
_D='type'
_C='name'
_B='kong'
_A='big'
import zlib,struct,json,os
dk64_rom='bismuth-balloon-crash.z64'
pointer_table_offset=1055824
setup_table_index=9
path_table_index=15
model2_types=[{_C:'CB Single (Diddy)',_D:10,_B:_F},{_C:'CB Single (DK)',_D:13,_B:_G},{_C:'CB Single (Tiny)',_D:22,_B:_H},{_C:'CB Single (Lanky)',_D:30,_B:_I},{_C:'CB Single (Chunky)',_D:31,_B:_J},{_C:'CB Bunch (DK)',_D:43,_B:_G},{_C:'CB Bunch (Lanky)',_D:517,_B:_I},{_C:'CB Bunch (Chunky)',_D:518,_B:_J},{_C:'CB Bunch (Tiny)',_D:519,_B:_H},{_C:'CB Bunch (Diddy)',_D:520,_B:_F},{_C:'Coin (Tiny)',_D:28,_B:_H},{_C:'Coin (DK)',_D:29,_B:_G},{_C:'Coin (Lanky)',_D:35,_B:_I},{_C:'Coin (Diddy)',_D:36,_B:_F},{_C:'Coin (Chunky)',_D:39,_B:_J}]
actor_types=[{_C:'Balloon (Diddy)',_D:91,_B:_F},{_C:'Balloon (Chunky)',_D:111,_B:_J},{_C:'Balloon (Tiny)',_D:112,_B:_H},{_C:'Balloon (Lanky)',_D:113,_B:_I},{_C:'Balloon (DK)',_D:114,_B:_G}]
def intf_to_float(intf):
	'Int float rep to float.'
	if intf==0:return 0
	else:return struct.unpack('!f',bytes.fromhex(hex(intf)[2:]))[0]
def ushort_to_short(ushort):
	'Unsigned short to short converter.';A=ushort
	if A>32767:A-=65536
	return A
map_data=[]
cb_model2_name='bananas_modeltwo.txt'
cb_actor_name='bananas_actor.txt'
coin_model2_name='coins.txt'
files=[cb_model2_name,cb_actor_name,coin_model2_name]
for f in files:
	if os.path.exists(f):os.remove(f)
def handleCreate(f_name):
	'Create file.';A=f_name
	if not os.path.exists(A):
		with open(A,'w')as B:B.seek(0)
balloon_id=0
cb_group=0
coin_group=0
def dumpData(data,map):
	'Dump data to file.';D='a';A=data;global balloon_id;global cb_group;global coin_group
	if A[_K]==_O:
		if'CB'in A[_C]:
			handleCreate(cb_model2_name);E=1
			if'Bunch'in A[_C]:E=5
			with open(cb_model2_name,D)as B:B.write(f'ColoredBananaGroup(group={cb_group},map_id={map},name="",konglist=[{A[_B]}], region="", locations=[[{(E,A[_L],A["x"],A["y"],A["z"])}]]),\n')
			cb_group+=1
		else:
			handleCreate(coin_model2_name)
			with open(coin_model2_name,D)as B:B.write(f'CoinGroup(group={coin_group},map_id={map},name="",konglist=[{A[_B]}], region="", locations=[[{(1,A[_L],A["x"],A["y"],A["z"])}]]),\n')
			coin_group+=1
	elif A[_K]=='actor':
		handleCreate(cb_actor_name);F=[]
		for (G,C) in enumerate(A[_M][_P]):F.append([G,C['x'],C['y'],C['z']])
		with open(cb_actor_name,D)as B:B.write(f'Balloon(id={balloon_id},map_id={map},name="",speed={A[_N]},konglist=[{A[_B]}], region="", points={F}, path={A[_M]["id"]}),\n')
		balloon_id+=1
with open(dk64_rom,'rb')as fh:
	fh.seek(pointer_table_offset+setup_table_index*4);setup_table=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);fh.seek(pointer_table_offset+path_table_index*4);path_table=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647)
	for map_index in range(221):
		balloon_id=0;cb_group=0;coin_group=0;current_map_data={'map':map_index,_E:[]};fh.seek(setup_table+map_index*4);setup_map_start=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);setup_map_end=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);setup_map_size=setup_map_end-setup_map_start;fh.seek(setup_map_start);setup_map_compressed=int.from_bytes(fh.read(2),_A)==8075;fh.seek(setup_map_start);setup_raw=fh.read(setup_map_size)
		if setup_map_compressed:setup_raw=zlib.decompress(setup_raw,15+32)
		fh.seek(path_table+map_index*4);path_map_start=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);path_map_end=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);path_map_size=path_map_end-path_map_start;fh.seek(path_map_start);path_map_compressed=int.from_bytes(fh.read(2),_A)==8075;fh.seek(path_map_start);path_raw=fh.read(path_map_size)
		if path_map_compressed:path_raw=zlib.decompress(path_raw,15+32)
		path_list=[];fh.seek(path_map_start);path_count=int.from_bytes(path_raw[0:2],_A);read_location=2
		for path_index in range(path_count):
			path_id=int.from_bytes(path_raw[read_location+0:read_location+2],_A);point_count=int.from_bytes(path_raw[read_location+2:read_location+4],_A);unk_0=int.from_bytes(path_raw[read_location+4:read_location+6],_A);read_location+=6;points=[]
			for point_index in range(point_count):points.append({'unk0':int.from_bytes(path_raw[read_location+0:read_location+2],_A),'x':int.from_bytes(path_raw[read_location+2:read_location+4],_A),'y':int.from_bytes(path_raw[read_location+4:read_location+6],_A),'z':int.from_bytes(path_raw[read_location+6:read_location+8],_A),_N:int.from_bytes(path_raw[read_location+8:read_location+9],_A),'unk1':int.from_bytes(path_raw[read_location+9:read_location+10],_A)});read_location+=10
			path_list.append({'id':path_id,'unk0':unk_0,_P:points.copy()})
		model2_count=int.from_bytes(setup_raw[0:4],_A);read_location=4
		for model2_index in range(model2_count):
			model2_type=int.from_bytes(setup_raw[read_location+40:read_location+42],_A);is_good_type=False;model2_name='';kong_name=''
			for m2_t in model2_types:
				if m2_t[_D]==model2_type:is_good_type=True;model2_name=m2_t[_C];kong_name=m2_t[_B]
			if is_good_type:model2_x=intf_to_float(int.from_bytes(setup_raw[read_location+0:read_location+4],_A));model2_y=intf_to_float(int.from_bytes(setup_raw[read_location+4:read_location+8],_A));model2_z=intf_to_float(int.from_bytes(setup_raw[read_location+8:read_location+12],_A));model2_scale=intf_to_float(int.from_bytes(setup_raw[read_location+12:read_location+16],_A));data={_C:model2_name,_D:hex(model2_type),'x':model2_x,'y':model2_y,'z':model2_z,_L:model2_scale,_B:kong_name,_K:_O};current_map_data[_E].append(data);dumpData(data,map_index)
			read_location+=48
		mystery_count=int.from_bytes(setup_raw[read_location+0:read_location+4],_A);read_location+=4
		for mystery_index in range(mystery_count):read_location+=36
		actor_count=int.from_bytes(setup_raw[read_location+0:read_location+4],_A);read_location+=4
		for actor_index in range(actor_count):
			actor_type=int.from_bytes(setup_raw[read_location+50:read_location+52],_A)+16;is_good_type=False;actor_name='';kong_name=''
			for ac_t in actor_types:
				if ac_t[_D]==actor_type:is_good_type=True;actor_name=ac_t[_C];kong_name=ac_t[_B]
			if is_good_type:
				if map_index==24:
					with open(f"test{actor_index}.bin",'wb')as fg:fg.write(setup_raw[read_location+0:read_location+56])
				actor_x=intf_to_float(int.from_bytes(setup_raw[read_location+0:read_location+4],_A));actor_y=intf_to_float(int.from_bytes(setup_raw[read_location+4:read_location+8],_A));actor_z=intf_to_float(int.from_bytes(setup_raw[read_location+8:read_location+12],_A));actor_speed=int.from_bytes(setup_raw[read_location+22:read_location+24],_A);actor_path=int.from_bytes(setup_raw[read_location+18:read_location+20],_A);found_path={}
				for path in path_list:
					if path['id']==actor_path:found_path=path
				prev_len=len(current_map_data[_E]);data={_C:actor_name,_D:hex(actor_type),'x':actor_x,'y':actor_y,'z':actor_z,_N:actor_speed,_M:found_path,_B:kong_name,_K:'actor'};current_map_data[_E].append(data);dumpData(data,map_index)
			read_location+=56
		if len(current_map_data[_E])>0:map_data.append(current_map_data)
with open('cb_coin_data.json','w')as fh:fh.write(json.dumps(map_data,indent=4))
print('Dumped vanilla data')