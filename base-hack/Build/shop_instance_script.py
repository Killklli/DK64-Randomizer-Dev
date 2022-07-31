'Copies a base shop script to all shops.'
_E='candy'
_D='funky'
_C='snide'
_B='map'
_A='shops'
ref_script='assets/Non-Code/instance_scripts/base_shop_script/shop.script'
shop_db=[{_B:'japes',_A:{_C:84,_D:83}},{_B:'aztec',_A:{_C:42,_E:43,_D:500}},{_B:'factory',_A:{_C:100,_E:209,_D:101}},{_B:'galleon',_A:{_C:55}},{_B:'fungi',_A:{_C:65,_D:64}},{_B:'caves',_A:{_C:59,_E:60,_D:57}},{_B:'castle',_A:{_C:38}},{_B:'dungeon_tunnel',_A:{_E:3}},{_B:'isles_snide_room',_A:{_C:1}},{_B:'crypt_hub',_A:{_D:1}}]
with open(ref_script,'r')as fh:
	for map_obj in shop_db:
		for shop in map_obj[_A]:
			shop_id=map_obj[_A][shop]
			with open(f"assets/Non-Code/instance_scripts/{map_obj[_B]}/{shop}.script",'w')as fg:fg.write(f".data\nid = {hex(shop_id)}\n.code\n");fh.seek(0);fg.write(fh.read())