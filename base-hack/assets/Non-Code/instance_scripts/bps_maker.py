'Generate the BPS files from the .raw script files.'
_B='.raw'
_A='flips.exe'
import os,subprocess,shutil
from instance_script_maps import instance_script_maps
instance_name='instance_script_maps.py'
instance_copy=f"../../../Build/{instance_name}"
shutil.copyfile(instance_copy,instance_name)
maps=instance_script_maps.copy()
script_dir='../../../../../map_scripts/map_scripts/'
files=[A for A in os.listdir('.')if os.path.isfile(A)]
printed=False
file_total=0
converted=0
shutil.copyfile('..\\..\\..\\build\\flips.exe',_A)
for f in files:
	if _B in f:
		file_total+=1;file_name=f.replace(_B,'');map_index=-1
		for map_obj in maps:
			if map_obj['name']==file_name:map_index=map_obj['map']
		if map_index>-1:
			map_index_str=str(map_index);script_folder_list=[A for A in os.listdir(script_dir)if not os.path.isfile(A)]
			for folder in script_folder_list:
				index=folder.split(' - ')[0];folder_name=folder.split(' - ')[1]
				if map_index_str==index:
					vanilla_script=f"{script_dir}{folder}/scripts.raw";temp_bps=f.replace(_B,'_.bps');orig_bps=f.replace(_B,'.bps');subprocess.Popen([_A,'--create',vanilla_script,f,temp_bps,'--bps']).wait()
					if os.path.exists(temp_bps):
						if os.path.exists(orig_bps):os.remove(orig_bps)
						if os.path.exists(f):os.remove(f)
						shutil.copyfile(temp_bps,orig_bps);os.remove(temp_bps);print(f"Created script for {folder_name}");converted+=1
if os.path.exists(_A):os.remove(_A)
print(f"{converted}/{file_total} scripts converted")