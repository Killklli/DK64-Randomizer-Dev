'Enemy Replacement along with Kasplats.'
_I='ground_beefyboys'
_H='ground_simple'
_G='kasplat_swaps'
_F='offset'
_E='enemy_id'
_D='enemy_swaps'
_C='replace_with'
_B='vanilla_location'
_A='big'
enemy_replacements=[{'container_map':7,_G:[{_B:0,_C:1},{_B:1,_C:3},{_B:2,_C:0},{_B:3,_C:2}],_D:{_H:[4,3,2,3,6,12,7,3,8,3,3,12,0,5,6,10,4,12,6,8,11,7,5,9,1,7,5,5,8,6],'air':[1,3,2,2,2,1,2,2,1,1,3,3,1,0,0,2,0,3,2,2,1,3,0,1,1,2,3,2,2,3],_I:[1,0,2,0,1,3,0,3,3,0,0,3,0,1,2,0,0,3,0,2,0,2,3,3,2,0,3,0,2,0],'water':[2,1,1,0,1,0,0,0,2,0,1,1,2,0,1,1,2,1,2,1,0,1,0,0,0,1,0,2,0,0]}}]
enemy_classes={_H:[0,27,30,31,33,51,59,84,87,88,89,95,101],'air':[5,28,83,99],_I:[9,56,100,103],'water':[85,86,102]}
with open('dk64-randomizer-base-dev.z64','r+b')as fh:
	for cont_map in enemy_replacements:
		vanilla_spawners=[];japes_spawners=43832916;fh.seek(japes_spawners);fence_count=int.from_bytes(fh.read(2),_A);offset=2
		if fence_count>0:
			for x in range(fence_count):fh.seek(japes_spawners+offset);point_count=int.from_bytes(fh.read(2),_A);offset+=point_count*6+2;fh.seek(japes_spawners+offset);point0_count=int.from_bytes(fh.read(2),_A);offset+=point0_count*10+6
		fh.seek(japes_spawners+offset);spawner_count=int.from_bytes(fh.read(2),_A);offset+=2
		for x in range(spawner_count):fh.seek(japes_spawners+offset);enemy_id=int.from_bytes(fh.read(1),_A);init_offset=offset;fh.seek(japes_spawners+offset+17);extra_count=int.from_bytes(fh.read(1),_A);offset+=22+extra_count*2;vanilla_spawners.append({_E:enemy_id,_F:init_offset})
		for kasplat in cont_map[_G]:
			source_kasplat_type=kasplat[_B]+61;replacement_kasplat_type=kasplat[_C]+61
			for spawner in vanilla_spawners:
				if spawner[_E]==source_kasplat_type:fh.seek(japes_spawners+spawner[_F]);fh.write(replacement_kasplat_type.to_bytes(1,_A))
		for enemy_class in cont_map[_D]:
			arr=cont_map[_D][enemy_class];class_types=enemy_classes[enemy_class];sub_index=0
			for spawner in vanilla_spawners:
				if spawner[_E]in class_types:new_class_index=arr[sub_index];new_enemy_id=class_types[new_class_index];fh.seek(japes_spawners+spawner[_F]);fh.write(new_enemy_id.to_bytes(1,_A));sub_index+=1