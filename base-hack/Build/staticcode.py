'Static code patching.'
jump_data_start=33550336
with open('rom/dk64-randomizer-base-temp.z64','rb')as fg:fg.seek(jump_data_start+0);patch_lag_hook=fg.read(8)
def patchStaticCode(filename):
	'Patch the static related code.'
	with open(filename,'r+b')as A:A.seek(3684);A.write(bytearray([8,0,55,162]));A.seek(86546);A.write(bytearray([128,93]));A.seek(586543);A.write(bytearray([0]));A.seek(586064);A.write(bytearray([0,0,0,0]));A.seek(586072);A.write(bytearray([0,0,0,0]));A.seek(21364);A.write(patch_lag_hook)