'Bananaport Swapper.'
_D='pad_index'
_C='warp_ids'
_B='warp_index'
_A='big'
bananaport_replacements=[{'containing_map':20,'pads':[{_B:0,_C:[88,153]},{_B:1,_C:[78,154]}]}]
pad_types=[532,531,529,530,528]
with open('dk64-randomizer-base-dev.z64','r+b')as fh:
	pad_vanilla=[]
	for cont_map in bananaport_replacements:
		aztec_llama_setup=36451100;fh.seek(aztec_llama_setup);model2_count=int.from_bytes(fh.read(4),_A)
		for x in range(model2_count):
			start=aztec_llama_setup+4+x*48;fh.seek(start+40);obj_type=int.from_bytes(fh.read(2),_A)
			if obj_type in pad_types:pad_index=pad_types.index(obj_type);fh.seek(start+42);obj_id=int.from_bytes(fh.read(2),_A);fh.seek(start+0);obj_x=int.from_bytes(fh.read(4),_A);fh.seek(start+4);obj_y=int.from_bytes(fh.read(4),_A);fh.seek(start+8);obj_z=int.from_bytes(fh.read(4),_A);fh.seek(start+12);obj_scale=int.from_bytes(fh.read(4),_A);fh.seek(start+24);obj_rotx=int.from_bytes(fh.read(4),_A);fh.seek(start+28);obj_roty=int.from_bytes(fh.read(4),_A);fh.seek(start+32);obj_rotz=int.from_bytes(fh.read(4),_A);obj_index=x;pad_vanilla.append({_D:pad_index,'_id':obj_id,'x':obj_x,'y':obj_y,'z':obj_z,'scale':obj_scale,'rx':obj_rotx,'ry':obj_roty,'rz':obj_rotz,'idx':obj_index})
	for x in bananaport_replacements:
		for y in x['pads']:
			warp_idx=y[_B];repl_ids=y[_C];source_counter=0
			for repl in repl_ids:
				for vanilla_pad in pad_vanilla:
					if vanilla_pad['_id']==repl:
						vanilla_idx=vanilla_pad['idx'];start=aztec_llama_setup+48*vanilla_idx+4;ref_pad={};counter=0
						for vanilla_pad0 in pad_vanilla:
							if vanilla_pad0[_D]==warp_idx:
								if counter==source_counter:ref_pad=vanilla_pad0
								counter+=1
						fh.seek(start+40);fh.write(pad_types[vanilla_pad[_D]].to_bytes(2,_A));fh.seek(start+0);fh.write(ref_pad['x'].to_bytes(4,_A));fh.seek(start+4);fh.write(ref_pad['y'].to_bytes(4,_A));fh.seek(start+8);fh.write(ref_pad['z'].to_bytes(4,_A));fh.seek(start+12);fh.write(ref_pad['scale'].to_bytes(4,_A));fh.seek(start+24);fh.write(ref_pad['rx'].to_bytes(4,_A));fh.seek(start+28);fh.write(ref_pad['ry'].to_bytes(4,_A));fh.seek(start+32);fh.write(ref_pad['rz'].to_bytes(4,_A))
				source_counter+=1