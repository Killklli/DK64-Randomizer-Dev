'Build Helm Geometry file.'
_A='big'
import zlib
rom_file='./rom/dk64.z64'
pointer_table_offset=1055824
geo_file='helm.bin'
with open(rom_file,'rb')as rom:
	rom.seek(pointer_table_offset+4*1);geo_table=pointer_table_offset+int.from_bytes(rom.read(4),_A);rom.seek(geo_table+17*4);helm_start=pointer_table_offset+(int.from_bytes(rom.read(4),_A)&2147483647);helm_end=pointer_table_offset+(int.from_bytes(rom.read(4),_A)&2147483647);helm_size=helm_end-helm_start;rom.seek(helm_start);compress=rom.read(helm_size);rom.seek(helm_start);compress_0=int.from_bytes(rom.read(2),_A)
	if compress_0==8075:data=zlib.decompress(compress,15+32)
	else:data=compress
	with open(geo_file,'wb')as geo:geo.write(data)
	with open(geo_file,'r+b')as geo:
		geo_points=[14276,14388,14484,14580,14676,14780,14876,14972,15068,15164];geo_overwrite=4761
		for point in geo_points:geo.seek(point);geo.write(geo_overwrite.to_bytes(4,_A))