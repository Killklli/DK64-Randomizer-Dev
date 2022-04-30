'Generate the BPS files from the .raw script files.'
_D='.raw'
_C='flips.exe'
_B='map'
_A='name'
import os,subprocess,shutil
maps=[{_A:'aztec',_B:38},{_A:'ballroom',_B:88},{_A:'caves',_B:72},{_A:'chunky_phase',_B:207},{_A:'diddy_5dc_upper',_B:200},{_A:'dungeon',_B:163},{_A:'factory',_B:26},{_A:'fungi',_B:48},{_A:'galleon',_B:30},{_A:'giant_mushroom',_B:64},{_A:'helm',_B:17},{_A:'isles',_B:34},{_A:'japes',_B:7},{_A:'japes_mountain',_B:4},{_A:'llama_temple',_B:20},{_A:'mill_front',_B:61},{_A:'mill_rear',_B:62},{_A:'museum',_B:113},{_A:'tgrounds',_B:176},{_A:'tiny_temple',_B:16},{_A:'wind_tower',_B:105}]
script_dir='../../../../../map_script_stuff/map_scripts_us/'
files=[A for A in os.listdir('.')if os.path.isfile(A)]
printed=False
file_total=0
converted=0
shutil.copyfile('..\\..\\..\\build\\flips.exe',_C)
for f in files:
	if _D in f:
		file_total+=1;file_name=f.replace(_D,'');map_index=-1
		for map_obj in maps:
			if map_obj[_A]==file_name:map_index=map_obj[_B]
		if map_index>-1:
			map_index_str=str(map_index);script_folder_list=[A for A in os.listdir(script_dir)if not os.path.isfile(A)]
			for folder in script_folder_list:
				index=folder.split(' - ')[0];folder_name=folder.split(' - ')[1]
				if map_index_str==index:
					vanilla_script=f"{script_dir}{folder}/scripts.raw";temp_bps=f.replace(_D,'_.bps');orig_bps=f.replace(_D,'.bps');subprocess.Popen([_C,'--create',vanilla_script,f,temp_bps,'--bps']).wait()
					if os.path.exists(temp_bps):
						if os.path.exists(orig_bps):os.remove(orig_bps)
						if os.path.exists(f):os.remove(f)
						shutil.copyfile(temp_bps,orig_bps);os.remove(temp_bps);print(f"Created script for {folder_name}");converted+=1
if os.path.exists(_C):os.remove(_C)
print(f"{converted}/{file_total} scripts converted")