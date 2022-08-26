'Make Instance Scripts.'
_I='ignore'
_H=True
_G=False
_F='data'
_E='wb'
_D='rb'
_C='behav_9C'
_B='id'
_A='big'
import json,os,zlib
base_rom='./rom/dk64.z64'
instance_dir='./assets/Non-Code/instance_scripts'
pointer_table_offset=1055824
script_table=0
temp_file='temp.bin'
new_block_count=0
new_cond_count=0
new_exec_count=0
new_blocks=[]
new_block=[]
new_conds=[]
new_execs=[]
class bcolors:'Color codes for printing to console.';HEADER='\x1b[95m';OKBLUE='\x1b[94m';OKCYAN='\x1b[96m';OKGREEN='\x1b[92m';WARNING='\x1b[93m';FAIL='\x1b[91m';ENDC='\x1b[0m';BOLD='\x1b[1m';UNDERLINE='\x1b[4m'
def resetCond(reset_block):
	'Reset block data with relation to script.';global new_block_count;global new_cond_count;global new_exec_count;global new_blocks;global new_block;global new_conds;global new_execs
	if reset_block:new_block_count=0;new_blocks=[]
	new_cond_count=0;new_exec_count=0;new_block=[];new_conds=[];new_execs=[]
print('\nCOMPILING SCRIPTS')
with open(base_rom,_D)as fh:
	fh.seek(pointer_table_offset+10*4);script_table=pointer_table_offset+int.from_bytes(fh.read(4),_A);map_data=[]
	if script_table!=0:
		folders=[A[0]for A in os.walk(instance_dir)]
		for f in folders:
			if f!='./'and'pycache'not in f:
				files=[A[2]for A in os.walk(f)][0];map_index=-1
				if'.map'in files:
					with open(f"{f}/.map",'r')as map_info:
						data=map_info.readlines();map_index=data[0]
						if'x'in map_index:map_index=int(map_index,16)
						else:map_index=int(map_index)
				script_list=[]
				if map_index>-1:
					map_data.append({'name':f,'map':map_index});fh.seek(script_table+map_index*4);vanilla_start=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);vanilla_end=pointer_table_offset+(int.from_bytes(fh.read(4),_A)&2147483647);vanilla_size=vanilla_end-vanilla_start;fh.seek(vanilla_start);compress=fh.read(vanilla_size)
					if int.from_bytes(compress[0:1],_A)==31 and int.from_bytes(compress[1:2],_A)==139:data=zlib.decompress(compress,15+32)
					else:data=compress
					with open(temp_file,_E)as tp:tp.write(data)
					with open(temp_file,_D)as tp:
						tp.seek(0);script_count=int.from_bytes(tp.read(2),_A)
						if script_count>0:
							read_location=2
							for script_index in range(script_count):
								script_start=read_location;tp.seek(read_location);id=int.from_bytes(tp.read(2),_A);block_count=int.from_bytes(tp.read(2),_A);behav_9C=int.from_bytes(tp.read(2),_A);read_location+=6
								for block_index in range(block_count):tp.seek(read_location);cond_count=int.from_bytes(tp.read(2),_A);read_location+=2+cond_count*8;tp.seek(read_location);exec_count=int.from_bytes(tp.read(2),_A);read_location+=2+exec_count*8
								script_end=read_location;script_size=script_end-script_start;tp.seek(script_start);script_list.append({_B:id,_C:behav_9C,_F:tp.read(script_size)})
					if os.path.exists(temp_file):os.remove(temp_file)
					for file in files:
						if file!='.map':
							with open(f"{f}/{file}",'r')as script_file:
								script_info=script_file.readlines();contains_code=_G;contains_data=_G;code_start=-1;data_end=len(script_info)-1;data_start=-1
								for (line_index,script_line) in enumerate(script_info):
									if'.code'in script_line:contains_code=_H;code_start=line_index+1;data_end=line_index
									elif'.data'in script_line:contains_data=_H;data_start=line_index+1
								script_data={_B:-1,_C:-1,_I:0}
								if contains_data and data_start>-1:
									for data_line in script_info[data_start:data_end]:
										data_line=data_line.replace('\n','')
										for attr in [_B,_C,_I]:
											if f"{attr} = "in data_line:
												val=data_line.split(f"{attr} = ")[1]
												if'0x'in val:val=int(val,16)
												else:val=int(val)
												script_data[attr]=val
								pre_message=f"[x] - Ignoring"
								if script_data[_I]==0:pre_message=f"    - Compiling"
								print(f"{pre_message} {file.replace('.script','')} ({hex(script_data[_B])})")
								if contains_code and code_start>-1:
									resetCond(_H)
									for code_line in script_info[code_start:]:
										code_line=code_line.replace('\n','');code_split=code_line.split(' ')
										if'COND'in code_line.upper():
											cond_or=0
											if'CONDINV'in code_line.upper():cond_or=32768
											arr=[int(code_split[1])|cond_or]
											for i in range(3):arr.append(int(code_split[3+i]))
											new_conds.append(arr);new_cond_count+=1
										elif'EXEC'in code_line.upper():
											arr=[int(code_split[1])]
											for i in range(3):arr.append(int(code_split[3+i]))
											new_execs.append(arr);new_exec_count+=1
										elif'ENDBLOCK'in code_line.upper():
											arr=[new_cond_count]
											for x_i in new_conds:arr.extend(x_i)
											arr.append(new_exec_count)
											for x_i in new_execs:arr.extend(x_i)
											new_blocks.append(arr);resetCond(_G);new_block_count+=1
								if script_data[_B]>-1 and script_data[_I]==0:
									found_existing=_G;found_index=-1;found_9c=-1
									for (script_index,script_item) in enumerate(script_list):
										if script_item[_B]==script_data[_B]:found_index=script_index;found_9c=script_item[_C];found_existing=_H
									if found_existing and found_index>-1:
										data=[script_data[_B],new_block_count,found_9c]
										for n in new_blocks:data.extend(n)
										with open(temp_file,_E)as tp:
											for d in data:d=d%65536;tp.write(d.to_bytes(2,_A))
										with open(temp_file,_D)as tp:script_list[found_index][_F]=tp.read()
										if os.path.exists(temp_file):os.remove(temp_file)
									else:
										data=[script_data[_B],new_block_count,script_data[_C]]
										for n in new_blocks:data.extend(n)
										with open(temp_file,_E)as tp:
											for d in data:d=d%65536;tp.write(d.to_bytes(2,_A))
										with open(temp_file,_D)as tp:script_list.append({_B:script_data[_B],_C:script_data[_C],_F:tp.read()})
										if os.path.exists(temp_file):os.remove(temp_file)
					with open(f"{f.replace('./','')}.raw",_E)as new_raw:
						new_raw.write(len(script_list).to_bytes(2,_A))
						for script in script_list:new_raw.write(script[_F])
						new_size=new_raw.tell();offset=new_size%16
						if offset>0:to_add=16-offset;new_raw.write((0).to_bytes(to_add,_A))
			with open('./instance_scripts_data.json','w')as fg:json.dump(map_data,fg)
	else:print("Couldn't find instance script table")