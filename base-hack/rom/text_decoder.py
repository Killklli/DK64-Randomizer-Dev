'Decode text file into arrays of text items.'
_G='section3count'
_F='section2count'
_E='normal'
_D='size'
_C='type'
_B='text'
_A='big'
with open('1114DD6_ZLib.bin','rb')as fh:
	fh.seek(0);count=int.from_bytes(fh.read(1),_A);print(count);text=[];text_data=[];text_start=count*15+3;data_start=1
	for i in range(count):
		fh.seek(data_start);section_1_count=int.from_bytes(fh.read(1),_A);section_2_count=int.from_bytes(fh.read(1),_A);section_3_count=int.from_bytes(fh.read(1),_A);fh.seek(data_start+5);start=int.from_bytes(fh.read(2),_A);size=int.from_bytes(fh.read(2),_A);block_start=1;blocks=[]
		for k in range(section_1_count):
			fh.seek(data_start+block_start);sec2ct=int.from_bytes(fh.read(1),_A);offset=0
			if sec2ct&4!=0:offset+=4
			text_blocks=[]
			if sec2ct&1==0:
				if sec2ct&2!=0:
					fh.seek(data_start+block_start+offset+1);sec3ct=int.from_bytes(fh.read(1),_A)
					for j in range(sec3ct):_block=block_start+2+offset+4*j-1;fh.seek(data_start+_block);_pos=int.from_bytes(fh.read(2),_A);fh.seek(data_start+_block);_dat=int.from_bytes(fh.read(4),_A);text_blocks.append({_C:'unk','position':_pos,'data':hex(_dat)})
					added=block_start+2+offset+4*sec3ct+4
			else:
				fh.seek(data_start+block_start+offset+1);sec3ct=int.from_bytes(fh.read(1),_A)
				for j in range(sec3ct):_block=block_start+2+offset+8*j-1;fh.seek(data_start+_block+3);_start=int.from_bytes(fh.read(2),_A);fh.seek(data_start+_block+5);_size=int.from_bytes(fh.read(2),_A);text_blocks.append({_C:_E,'start':_start,_D:_size})
				added=block_start+2+offset+8*sec3ct+4
			blocks.append({'block_start':hex(block_start+data_start),_F:sec2ct,_G:sec3ct,'offset':offset,_B:text_blocks});block_start=added
		fh.seek(data_start)
		if added<data_start:info=b''
		else:info=fh.read(added-data_start)
		text_data.append({'arr':info,_B:blocks,'section1count':section_1_count,_F:section_2_count,_G:section_3_count,'data_start':hex(data_start)});text_start+=added-data_start;data_start+=block_start
	for item in text_data:
		text_block=[]
		for item2 in item[_B]:
			temp=[]
			for item3 in item2[_B]:
				if item3[_C]==_E:start=item3['start']+data_start+2;end=start+item3[_D];fh.seek(start);temp.append(fh.read(item3[_D]).decode())
			text_block.append(temp)
		text.append(text_block)
	text_idx=0
	for t in text:print(f"[{text_idx}] - {t}");text_idx+=1