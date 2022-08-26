'Static code patching.'
jump_data_start=33550336
with open('rom/dk64-randomizer-base-temp.z64','rb')as fg:fg.seek(jump_data_start+0);patch_lag_hook=fg.read(8)
def patchStaticCode(filename):
	'Patch the static related code.';B='big'
	with open(filename,'r+b')as A:A.seek(3684);A.write(bytearray([8,0,55,162]));A.seek(86546);A.write(bytearray([128,93]));A.seek(586543);A.write(bytearray([0]));A.seek(586064);A.write(bytearray([0,0,0,0]));A.seek(586072);A.write(bytearray([0,0,0,0]));A.seek(21364);A.write(patch_lag_hook);C=[256,105];D=640-2*C[0];A.seek(1466);A.write(C[0].to_bytes(2,B));A.seek(1530);A.write(C[1].to_bytes(2,B));A.seek(1538);A.write(D.to_bytes(2,B));A.seek(1450);A.write((30784).to_bytes(2,B))