'Replace Barrels in ROM.'
_D='new_map'
_C='instance_id'
_B='barrels'
_A='big'
barrel_replacements=[{'containing_map':38,_B:[{_C:33,_D:17}]}]
barrels=[12,91]
with open('dk64-randomizer-base-dev.z64','r+b')as fh:
	for cont_map in barrel_replacements:
		aztec_setup=37040924;fh.seek(aztec_setup);model2_count=int.from_bytes(fh.read(4),_A);fh.seek(aztec_setup+4+model2_count*48);mystery_count=int.from_bytes(fh.read(4),_A);fh.seek(aztec_setup+4+model2_count*48+4+mystery_count*36);actor_count=int.from_bytes(fh.read(4),_A);start_of_actor_range=aztec_setup+4+model2_count*48+4+mystery_count*36+4
		for x in range(actor_count):
			start_of_actor=start_of_actor_range+56*x;fh.seek(start_of_actor);fh.seek(start_of_actor+50);actor_type=int.from_bytes(fh.read(2),_A)
			if actor_type in barrels:
				fh.seek(start_of_actor+52);actor_id=int.from_bytes(fh.read(2),_A)
				for barrel in cont_map[_B]:
					if barrel[_C]==actor_id:fh.seek(start_of_actor+18);fh.write(barrel[_D].to_bytes(2,_A))