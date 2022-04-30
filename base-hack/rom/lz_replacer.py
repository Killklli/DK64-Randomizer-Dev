'Replace LZs in ROM.'
_E='new_exit'
_D='new_map'
_C='vanilla_exit'
_B='vanilla_map'
_A='big'
lz_replacements=[{'container_map':34,'zones':[{_B:176,_C:0,_D:17,_E:1}]}]
valid_lz_types=[9,12,13,16]
def intToArr(val,size):
	'Convert INT to an array.\n\n    Args:\n        val (int): Value to convert\n        size (int): Size to write as\n\n    Returns:\n        array: int array\n    ';A=val;C=[]
	for E in range(size):C.append(0)
	B=size-1
	while B>-1:
		D=A%256;C[B]=D;B-=1;A=int((A-D)/256)
		if B==-1:break
		elif A==0:break
	return C
with open('dk64-randomizer-base-dev.z64','r+b')as fh:
	for cont_map in lz_replacements:
		dk_isles_lzs=43486430;fh.seek(dk_isles_lzs);lz_count=int.from_bytes(fh.read(2),_A)
		for x in range(lz_count):
			start=x*56+2;fh.seek(dk_isles_lzs+start+16);lz_type=int.from_bytes(fh.read(2),_A)
			if lz_type in valid_lz_types:
				fh.seek(dk_isles_lzs+start+18);lz_map=int.from_bytes(fh.read(2),_A);fh.seek(dk_isles_lzs+start+20);lz_exit=int.from_bytes(fh.read(2),_A)
				for y in cont_map['zones']:
					if lz_map==y[_B]:
						if lz_exit==y[_C]:fh.seek(dk_isles_lzs+start+18);map_bytes=intToArr(y[_D],2);fh.write(bytearray(map_bytes));fh.seek(dk_isles_lzs+start+20);exit_bytes=intToArr(y[_E],2);fh.write(bytearray(exit_bytes))