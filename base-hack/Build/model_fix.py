'Generate corrected Diddy and Lanky models.'
_E='big'
_D='add'
_C='wipe'
_B='model_index'
_A='model_file'
import zlib
rom_file='rom/dk64.z64'
pointer_offset=1055824
diddy_fix='\n    E7 00 00 00 00 00 00 00\n    FC 12 18 24 FF 33 FF FF\n    D7 00 00 02 08 00 08 00\n    FD 10 00 00 0E 00 00 00\n    E6 00 00 00 00 00 00 00\n    F3 00 00 00 07 3F F1 00\n    E7 00 00 00 00 00 00 00\n    E3 00 10 01 00 00 00 00\n    D9 FF FF FF 00 04 00 00\n    DA 38 00 03 04 00 00 40\n'
lanky_fix='\n    E7 00 00 00 00 00 00 00\n    FC 12 18 24 FF 33 FF FF\n    D7 00 00 02 08 00 08 00\n    FD 10 00 00 0D 00 00 00\n    E6 00 00 00 00 00 00 00\n    F3 00 00 00 07 3F F1 00\n    E7 00 00 00 00 00 00 00\n    E3 00 10 01 00 00 00 00\n    D9 FF FF FF 00 04 00 00\n    DA 38 00 03 04 00 03 C0\n'
lanky_fix2='\n    FD 10 00 00 0D 00 00 00\n'
lanky_fix3='\n    FC 12 18 24 FF 33 FF FF\n    D7 00 00 02 08 00 08 00\n    FD 10 00 00 0D 00 00 00\n    E6 00 00 00 00 00 00 00\n    F3 00 00 00 07 3F F1 00\n    E7 00 00 00 00 00 00 00\n    E3 00 10 01 00 00 00 00\n    D9 FF FF FF 00 04 00 00\n'
lanky_fix4='\n    FC 12 18 24 FF 33 FF FF\n'
lanky_fix5='\n    00 00 0E 69\n'
dk_adjustment='\n    17 7D\n'
tiny_adjustment='\n    17 7E\n'
modifications=[{_B:0,_A:'diddy_base.bin',_C:[[18384,18552]],_D:[diddy_fix]},{_B:1,_A:'diddy_ins.bin',_C:[[17816,17952]],_D:[diddy_fix]},{_B:5,_A:'lanky_base.bin',_C:[[20996,21000],[21532,21536],[22220,22224]],_D:[lanky_fix5,lanky_fix5,lanky_fix5]},{_B:6,_A:'lanky_ins.bin',_C:[[23532,23536],[24228,24232],[22860,22864],[24556,24560]],_D:[lanky_fix5,lanky_fix5,lanky_fix5,lanky_fix5]},{_B:3,_A:'dk_base.bin',_C:[[24994,24996]],_D:[dk_adjustment]},{_B:8,_A:'tiny_base.bin',_C:[[25556,25558]],_D:[tiny_adjustment]},{_B:9,_A:'tiny_ins.bin',_C:[[26524,26526]],_D:[tiny_adjustment]}]
with open(rom_file,'rb')as rom:
	rom.seek(pointer_offset+5*4);actor_table=pointer_offset+int.from_bytes(rom.read(4),_E)
	for model in modifications:
		idx=model[_B];rom.seek(actor_table+idx*4);model_start=pointer_offset+int.from_bytes(rom.read(4),_E);model_end=pointer_offset+int.from_bytes(rom.read(4),_E);model_size=model_end-model_start;rom.seek(model_start)
		with open(model[_A],'wb')as fh:compress=rom.read(model_size);decompress=zlib.decompress(compress,15+32);fh.write(decompress)
		with open(model[_A],'r+b')as fh:
			sub_idx=0
			for wipe in model[_C]:
				fh.seek(wipe[0]);wipe_size=wipe[1]-wipe[0];wipe_lst=[]
				for x in range(wipe_size):wipe_lst.append(0)
				fh.write(bytearray(wipe_lst));fix_arr=model[_D][sub_idx].split('\n');fix_lst=[]
				for f in fix_arr:
					if not f=='':
						for x in f.strip().split(' '):fix_lst.append(int(f"0x{x}",16))
				fh.seek(wipe[0]);fh.write(bytearray(fix_lst));sub_idx+=1