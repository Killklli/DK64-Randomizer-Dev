'Write new Disco Chunky models.'
_C='wb'
_B='rb'
_A='big'
import zlib,os
class Vert:
	'Vertex Information.'
	def __init__(A,coords,rgba,other=[0,0,0]):
		'Initialize with given data.';D=[-10,0,-10];B=[0,0,0]
		for (C,E) in enumerate(coords):B[C]=E+D[C]
		A.coords=B;A.rgba=rgba;A.other=other
rom_file='rom/dk64.z64'
pointer_offset=1055824
temp_file='temp.bin'
ins_file='disco_instrument.bin'
ins_new_verts=[Vert([89,-5,-25],310575359),Vert([89,-5,24],8454399),Vert([85,-1,24],2164261119),Vert([85,-1,-25],3238030847),Vert([93,-1,-25],2080433663),Vert([93,-1,24],2130706687),Vert([89,3,-25],310182143),Vert([89,3,24],8323327),Vert([81,-5,28],8454399),Vert([39,-5,4],3984854527),Vert([41,-1,0],2130706687),Vert([83,-1,24],1057002495),Vert([79,-1,32],3238030847),Vert([37,-1,7],2751485695),Vert([81,3,28],8323327),Vert([39,3,4],3984330239),Vert([83,-5,-29],4186173951),Vert([39,-5,-4],3984913407),Vert([37,-1,-7],2751507199),Vert([81,-1,-32],3741353727),Vert([83,3,-29],4185780735),Vert([39,3,-4],3984389119),Vert([39,3,0],3682140415),Vert([39,-5,0],3683057919),Vert([35,-1,4],2231377663),Vert([90,-1,-33],1107334399),Vert([81,-5,28],1811956223),Vert([83,-1,24],1811956223),Vert([81,3,28],1811956223),Vert([79,-1,32],1811956223),Vert([89,-5,24],32767),Vert([93,-1,24],32767),Vert([89,3,24],32767),Vert([85,-1,24],32767),Vert([39,-5,-4],3984913407),Vert([35,-1,-4],2231427839),Vert([37,-1,-7],2751507199),Vert([90,-1,-33],1107334399),Vert([83,3,-29],4185780735),Vert([89,3,-25],310182143),Vert([39,3,-4],3984389119),Vert([35,-1,4],2231377663),Vert([39,3,4],3984330239),Vert([39,3,0],3682140415),Vert([39,-5,0],3683057919),Vert([6,-2,-11],873041407),Vert([15,-12,-10],1122736127),Vert([13,-20,-9],1188143871),Vert([-8,-2,0],2347576319),Vert([-12,-18,-8],2349453567),Vert([-8,-17,3],3036112127),Vert([15,-12,0],1727089151),Vert([10,-2,0],1813004543),Vert([9,-19,6],971271679),Vert([0,-19,6],3972952831),Vert([0,-2,11],4041571071),Vert([-7,-2,-10],2800724479),Vert([15,-3,-6],1164571391),Vert([58,-11,-12],1782907135),Vert([58,-16,-7],1629309951),Vert([58,-20,-12],3448504575),Vert([58,-16,-16],1629337087),Vert([-3,-16,-16],2682500607),Vert([-3,-20,-12],2528837887),Vert([-3,-16,-7],2682473471),Vert([-3,-11,-12],863240447),Vert([35,-1,4],32511,[0,1023,195]),Vert([39,3,0],3430088959,[0,1536,65342]),Vert([39,-5,0],881656063,[0,512,65339]),Vert([35,-1,-4],33535,[0,2049,196]),Vert([39,-5,0],881656063,[0,2560,65339]),Vert([13,-15,-1],3430088959,[0,1536,2500]),Vert([11,-19,2],32511,[0,1024,2612]),Vert([10,-23,-1],881656063,[0,512,2711]),Vert([11,-19,-5],33535,[0,2048,2612]),Vert([10,-23,-1],881656063,[0,2560,2711])]
ins_new_dl=['\n        E7 00 00 00 00 00 00 00\n        E2 00 00 1C 00 55 20 78\n        D7 00 00 02 08 00 08 00\n        FD 10 00 00 00 00 0E BF\n        E6 00 00 00 00 00 00 00\n        F3 00 00 00 07 3F F1 00\n        E7 00 00 00 00 00 00 00\n        E3 00 10 01 00 00 00 00\n        F5 10 10 00 00 01 40 50\n        DE 00 00 00 05 00 00 00\n        D9 FF FF FF 00 06 00 00\n        DA 38 00 03 04 00 01 C0\n        01 01 E0 3C 03 00 38 C0\n        06 00 02 04 00 00 04 06\n        06 02 00 08 00 02 08 0A\n        06 0A 08 0C 00 0A 0C 0E\n        06 06 04 0E 00 06 0E 0C\n        06 10 12 14 00 10 14 16\n        06 12 10 18 00 12 18 1A\n        06 1A 18 1C 00 1A 1C 1E\n        06 16 14 1E 00 16 1E 1C\n        06 20 22 24 00 20 24 26\n        06 22 20 06 00 22 06 14\n        06 14 06 28 00 14 28 2A\n        06 26 24 2A 00 26 2A 28\n        06 2A 2C 1E 00 2A 1E 14\n        06 14 12 2E 00 14 2E 22\n        06 30 1A 1E 00 12 1A 30\n        06 00 06 20 00 28 06 0C\n        06 32 08 00 00 32 26 28\n        06 32 20 26 00 32 00 20\n        06 12 30 2E 00 08 32 0C\n        06 34 36 38 00 34 38 3A\n        01 00 F0 1E 03 00 3A A0\n        06 00 02 04 00 00 04 06\n        06 08 0A 0C 00 0E 10 12\n        06 14 0C 0A 00 16 18 1A\n        06 1A 14 0A 00 1C 0A 08\n    ','\n        E7 00 00 00 00 00 00 00\n        E3 00 0A 01 00 10 00 00\n        E2 00 00 1C 0C 19 20 78\n        FC 26 A0 04 1F 10 93 FF\n        E3 00 0F 00 00 01 00 00\n        D7 00 28 02 FF FF FF FF\n        FD 10 00 00 00 00 0D 09\n        E6 00 00 00 00 00 00 00\n        F3 00 00 00 07 55 B0 00\n        E7 00 00 00 00 00 00 00\n        E3 00 10 01 00 00 00 00\n        F2 00 20 02 00 07 E0 7E\n        F5 10 09 00 01 01 04 41\n        F5 10 05 40 02 00 C8 32\n        F5 10 03 50 03 00 8C 23\n        F5 10 03 54 04 00 50 14\n        F5 10 03 56 05 00 14 05\n        D9 FB FF FF 00 00 00 00\n        DA 38 00 03 04 00 01 80\n        01 00 50 16 03 00 3D 30\n        DA 38 00 03 04 00 01 C0\n        01 00 50 0A 03 00 3C E0\n        06 00 02 0C 00 00 0C 0E\n        06 04 00 0E 00 04 0E 10\n        06 02 06 12 00 02 12 0C\n        06 06 08 14 00 06 14 12\n        D9 FD FF FF 00 00 00 00\n        DF 00 00 00 00 00 00 00\n    ']
beater_new_dl='\n    01 01 50 2A 03 00 3B 90\n    FD 10 00 00 00 00 0E BF\n    06 1A 1C 1E 00 1A 1E 20\n    06 22 24 26 00 22 26 28\n    06 1A 20 22 00 1A 22 28\n    06 20 1E 24 00 20 24 22\n    06 1E 1C 26 00 1E 26 24\n    06 1C 1A 28 00 1C 28 26\n'
with open(rom_file,_B)as rom:
	rom.seek(pointer_offset+5*4);actor_table=pointer_offset+int.from_bytes(rom.read(4),_A);rom.seek(actor_table+13*4);disco_start=pointer_offset+int.from_bytes(rom.read(4),_A);disco_finish=pointer_offset+int.from_bytes(rom.read(4),_A);disco_size=disco_finish-disco_start;rom.seek(disco_start);disco_data=zlib.decompress(rom.read(disco_size),15+32);vert_end=14568;dl_end=22712
	with open(ins_file,_C)as fh:fh.write(disco_data)
	with open(ins_file,_B)as fh:
		fh.seek(40);vert_data=fh.read(vert_end-40)
		with open(temp_file,_C)as fg:
			fg.write(vert_data)
			for vert_block in ins_new_verts:
				for c in vert_block.coords:
					if c<0:c+=65536
					fg.write(c.to_bytes(2,_A))
				for o in vert_block.other:fg.write(o.to_bytes(2,_A))
				fg.write(vert_block.rgba.to_bytes(4,_A))
		with open(temp_file,_B)as fg:vert_data=fg.read()
		fh.seek(vert_end);dl_mid=18432;dl_data=b'';dl_data_0=fh.read(dl_mid-vert_end);dl_data_1=fh.read(dl_end-dl_mid)
		with open(temp_file,_C)as fg:
			fg.write(dl_data_0);fg.write(dl_data_1);pos=fg.tell();fg.seek(pos-8)
			for dl_block in ins_new_dl:
				fix_arr=dl_block.split('\n');fix_lst=[]
				for f in fix_arr:
					if not f=='':
						for x in f.strip().split(' '):
							if x.strip()!='':fix_lst.append(int(f"0x{x}",16))
				fg.write(bytearray(fix_lst))
		with open(temp_file,_B)as fg:dl_data=fg.read()
		fh.seek(dl_end+4);other_data=fh.read();fh.seek(20);header_data=fh.read(40-20)
		with open(temp_file,_C)as fg:base=268439680;fg.write(base.to_bytes(4,_A));fg.write((base+len(vert_data)+len(dl_data)).to_bytes(4,_A));fg.write((base+len(vert_data)+len(dl_data)+4).to_bytes(4,_A));fg.write((base+len(vert_data)+len(dl_data)+372).to_bytes(4,_A));fg.write((base+len(vert_data)+len(dl_data)+812).to_bytes(4,_A));fg.write(header_data);fg.write(vert_data);fg.write(dl_data);fg.write((base+len(vert_data)).to_bytes(4,_A));fg.write(other_data)
	with open(temp_file,_B)as fg:
		with open(ins_file,_C)as fh:fh.write(fg.read())
	if os.path.exists(temp_file):os.remove(temp_file)