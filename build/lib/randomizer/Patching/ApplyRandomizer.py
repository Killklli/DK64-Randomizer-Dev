'Apply Patch data to the ROM.'
import asyncio,codecs,json,math,pickle,random,js
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Patching.BananaPortRando import randomize_bananaport
from randomizer.Patching.BarrelRando import randomize_barrels
from randomizer.Patching.BossRando import randomize_bosses
from randomizer.Patching.CosmeticColors import apply_cosmetic_colors,overwrite_object_colors,applyKrushaKong
from randomizer.Patching.DKTV import randomize_dktv
from randomizer.Patching.EnemyRando import randomize_enemies
from randomizer.Patching.EntranceRando import randomize_entrances,filterEntranceType
from randomizer.Patching.Hash import get_hash_images
from randomizer.Patching.KasplatLocationRando import randomize_kasplat_locations
from randomizer.Patching.KongRando import apply_kongrando_cosmetic
from randomizer.Patching.MiscSetupChanges import randomize_setup
from randomizer.Patching.MoveLocationRando import randomize_moves
from randomizer.Patching.MusicRando import randomize_music
from randomizer.Patching.ItemRando import place_randomized_items
from randomizer.Patching.Patcher import ROM
from randomizer.Patching.PhaseRando import randomize_helm,randomize_krool
from randomizer.Patching.PriceRando import randomize_prices
from randomizer.Patching.PuzzleRando import randomize_puzzles
from randomizer.Patching.UpdateHints import PushHints,wipeHints
from randomizer.Patching.MiscSetupChanges import randomize_setup
from randomizer.Patching.BananaPlacer import randomize_cbs
from randomizer.Patching.ShopRandomizer import ApplyShopRandomizer
from randomizer.Patching.CrownPlacer import randomize_crown_pads
from ui.GenTracker import generateTracker
from ui.GenSpoiler import GenerateSpoiler
from randomizer.Patching.UpdateHints import PushHints,wipeHints
from randomizer.Patching.DoorPlacer import place_door_locations
from randomizer.Lists.QoL import QoLSelector
from randomizer.Lists.EnemyTypes import EnemySelector
from randomizer.Settings import Settings
from ui.GenTracker import generateTracker
from ui.progress_bar import ProgressBar
def patching_response(responded_data):
	'Response data from the background task.\n\n    Args:\n        responded_data (str): Pickled data (or json)\n    ';l='spoiler_log_text';k='tracker_text';j='spoiler_log_block';i='big';h='error';T=responded_data;S='shift';R='value';Q='base64';H='';E=asyncio.get_event_loop()
	try:
		U=json.loads(T)
		if U.get(h):V=U.get(h);ProgressBar().set_class('bg-danger');js.toast_alert(V);E.run_until_complete(ProgressBar().update_progress(10,f"Error: {V}"));E.run_until_complete(ProgressBar().reset());return None
	except Exception:pass
	E.run_until_complete(ProgressBar().update_progress(8,'Applying Patches'));A=pickle.loads(codecs.decode(T.encode(),Q));A.settings.verify_hash();Settings({'seed':0}).compare_hash(A.settings.public_hash);A.settings.set_seed()
	if A.settings.download_patch_file:A.settings.download_patch_file=False;js.save_text_as_file(codecs.encode(pickle.dumps(A),Q).decode(),f"dk64-{A.settings.seed_id}.lanky")
	js.write_seed_history(A.settings.seed_id,codecs.encode(pickle.dumps(A),Q).decode(),A.settings.public_hash);B=A.settings.rom_data
	if A.settings.shuffle_loading_zones=='levels':
		ROM().seek(B+0);ROM().write(1);m=[Transitions.IslesMainToJapesLobby,Transitions.IslesMainToAztecLobby,Transitions.IslesMainToFactoryLobby,Transitions.IslesMainToGalleonLobby,Transitions.IslesMainToForestLobby,Transitions.IslesMainToCavesLobby,Transitions.IslesMainToCastleLobby];n=[Transitions.IslesJapesLobbyToMain,Transitions.IslesAztecLobbyToMain,Transitions.IslesFactoryLobbyToMain,Transitions.IslesGalleonLobbyToMain,Transitions.IslesForestLobbyToMain,Transitions.IslesCavesLobbyToMain,Transitions.IslesCastleLobbyToMain];C=0
		for o in m:ROM().seek(B+1+C);ROM().write(n.index(A.shuffled_exit_data[int(o)].reverse));C+=1
		p={Transitions.IslesMainToJapesLobby:Transitions.IslesJapesLobbyToMain,Transitions.IslesMainToAztecLobby:Transitions.IslesAztecLobbyToMain,Transitions.IslesMainToFactoryLobby:Transitions.IslesFactoryLobbyToMain,Transitions.IslesMainToGalleonLobby:Transitions.IslesGalleonLobbyToMain,Transitions.IslesMainToForestLobby:Transitions.IslesForestLobbyToMain,Transitions.IslesMainToCavesLobby:Transitions.IslesCavesLobbyToMain,Transitions.IslesMainToCastleLobby:Transitions.IslesCastleLobbyToMain};J={Transitions.IslesJapesLobbyToMain:26,Transitions.IslesAztecLobbyToMain:74,Transitions.IslesFactoryLobbyToMain:138,Transitions.IslesGalleonLobbyToMain:168,Transitions.IslesForestLobbyToMain:236,Transitions.IslesCavesLobbyToMain:292,Transitions.IslesCastleLobbyToMain:317};C=0
		if Types.Key not in A.settings.shuffled_location_types:
			for (D,W) in p.items():q=A.shuffled_exit_data.get(D).reverse;ROM().seek(B+30+C);ROM().writeMultipleBytes(J[int(q)],2);C+=2
		else:
			for D in J:ROM().seek(B+30+C);ROM().writeMultipleBytes(J[D],2);C+=2
	C=0
	for F in A.settings.BossBananas:ROM().seek(B+8+C);ROM().writeMultipleBytes(F,2);C+=2
	C=0
	for F in A.settings.EntryGBs:ROM().seek(B+22+C);ROM().writeMultipleBytes(F,1);C+=1
	if A.settings.starting_kongs_count==5:ROM().seek(B+44);ROM().write(31)
	else:
		X=0
		for r in A.settings.starting_kong_list:X|=1<<r
		ROM().seek(B+44);ROM().write(X)
	if A.settings.unlock_all_moves:ROM().seek(B+45);ROM().write(1)
	ROM().seek(B+46);ROM().write(1)
	if A.settings.shockwave_status=='start_with':ROM().seek(B+47);ROM().write(1)
	if A.settings.enable_tag_anywhere:ROM().seek(B+48);ROM().write(1)
	if A.settings.fps_display:ROM().seek(B+150);ROM().write(1)
	if A.settings.helm_setting=='skip_start':ROM().seek(B+49);ROM().write(1)
	elif A.settings.helm_setting=='skip_all':ROM().seek(B+49);ROM().write(2)
	if A.settings.crown_door_open:ROM().seek(B+50);ROM().write(1)
	if A.settings.coin_door_open=='need_both':ROM().seek(B+51);ROM().write(0)
	elif A.settings.coin_door_open=='need_zero':ROM().seek(B+51);ROM().write(1)
	elif A.settings.coin_door_open=='need_nin':ROM().seek(B+51);ROM().write(2)
	elif A.settings.coin_door_open=='need_rw':ROM().seek(B+51);ROM().write(3)
	if A.settings.free_trade_items:ROM().seek(B+275);K=int.from_bytes(ROM().readBytes(1),i);ROM().seek(B+275);ROM().write(K|1)
	if A.settings.free_trade_blueprints:ROM().seek(B+275);K=int.from_bytes(ROM().readBytes(1),i);ROM().seek(B+275);ROM().write(K|2)
	if A.settings.quality_of_life:
		L=A.settings.misc_changes_selected.copy()
		if len(L)==0:
			for G in QoLSelector:L.append(G[R])
		Y=[0,0]
		for G in QoLSelector:
			if G[R]in L and G[S]>=0:s=int(G[S]>>3);t=int(G[S]%8);Y[s]|=128>>t
		ROM().seek(B+176)
		for u in Y:ROM().writeMultipleBytes(u,1)
	ROM().seek(B+165)
	if A.settings.damage_amount!='default':
		if A.settings.damage_amount=='double':ROM().write(2)
		elif A.settings.damage_amount=='ohko':ROM().write(12)
		elif A.settings.damage_amount=='quad':ROM().write(4)
	else:ROM().write(1)
	if A.settings.no_healing:ROM().seek(B+166);ROM().write(1)
	if A.settings.no_melons:ROM().seek(B+296);ROM().write(1)
	if A.settings.bonus_barrel_auto_complete:ROM().seek(B+294);ROM().write(1)
	if A.settings.warp_to_isles:ROM().seek(B+309);ROM().write(1)
	if A.settings.shop_indicator:ROM().seek(B+308);ROM().write(2)
	if A.settings.perma_death:ROM().seek(B+333);ROM().write(1);ROM().seek(B+334);ROM().write(1)
	if A.settings.open_lobbies:ROM().seek(B+332);ROM().write(255)
	if A.settings.disable_tag_barrels:ROM().seek(B+335);ROM().write(1)
	if A.settings.disable_shop_hints:ROM().seek(B+331);ROM().write(0)
	if A.settings.open_levels:ROM().seek(B+311);ROM().write(1)
	if A.settings.shorten_boss:ROM().seek(B+315);ROM().write(1)
	if A.settings.fast_warps:ROM().seek(B+314);ROM().write(1)
	if A.settings.dpad_display:ROM().seek(B+313);ROM().write(1)
	if A.settings.activate_all_bananaports=='all':ROM().seek(B+312);ROM().write(1)
	if A.settings.activate_all_bananaports=='isles':ROM().seek(B+312);ROM().write(2)
	if A.settings.high_req:ROM().seek(B+377);ROM().write(1)
	if A.settings.fast_gbs:ROM().seek(B+378);ROM().write(1)
	if A.settings.auto_keys:ROM().seek(B+347);ROM().write(1)
	if A.settings.hard_bosses:
		for Z in range(3):ROM().seek(B+379+Z);ROM().write(A.settings.kko_phase_order[Z])
	if A.settings.disco_chunky:ROM().seek(B+303);ROM().write(1)
	if A.settings.tns_location_rando:ROM().seek(B+270);ROM().write(1)
	if A.settings.cb_rando:ROM().seek(B+175);ROM().write(1);ROM().seek(B+267);ROM().write(1)
	if A.settings.wrinkly_location_rando or('remove_wrinkly_puzzles'in A.settings.misc_changes_selected or len(A.settings.misc_changes_selected)==0):ROM().seek(B+287);ROM().write(1)
	if A.settings.helm_hurry:ROM().seek(B+174);ROM().write(1)
	if A.settings.remove_water_oscillation:ROM().seek(B+271);ROM().write(1)
	if A.settings.hard_enemies:ROM().seek(B+278);ROM().write(1)
	a=['beat_krool','get_key8','all_fairies','all_blueprints','all_medals','poke_snap','all_keys']
	if A.settings.win_condition in a:v=a.index(A.settings.win_condition);ROM().seek(B+285);ROM().write(v)
	M=[0,1,2,3,4,5,6,7]
	if len(A.settings.krool_keys_required)>0:
		for D in A.settings.krool_keys_required:
			b=D-4
			if b in M:M.remove(b)
	N=0
	for D in M:N=N|1<<D
	ROM().seek(B+295);ROM().write(N)
	if A.settings.medal_requirement!=15:ROM().seek(B+336);ROM().write(A.settings.medal_requirement)
	if A.settings.rareware_gb_fairies!=20:ROM().seek(B+54);ROM().write(A.settings.rareware_gb_fairies)
	if A.settings.medal_cb_req!=75:ROM().seek(B+274);ROM().write(A.settings.medal_cb_req)
	if len(A.settings.enemies_selected)==0 and(A.settings.enemy_rando or A.settings.crown_enemy_rando!='off'):
		c=[]
		for w in EnemySelector:c.append(w[R])
		A.settings.enemies_selected=c
	randomize_entrances(A);randomize_moves(A);randomize_prices(A);randomize_bosses(A);randomize_krool(A);randomize_helm(A);randomize_barrels(A);randomize_bananaport(A);randomize_kasplat_locations(A);randomize_enemies(A);apply_kongrando_cosmetic(A);randomize_setup(A);randomize_puzzles(A);randomize_cbs(A);ApplyShopRandomizer(A);place_randomized_items(A);place_door_locations(A);randomize_crown_pads(A);filterEntranceType();random.seed(A.settings.seed);randomize_music(A);applyKrushaKong(A);apply_cosmetic_colors(A);overwrite_object_colors(A);random.seed(A.settings.seed)
	if A.settings.wrinkly_hints in['standard','cryptic']:wipeHints();PushHints(A)
	C=0;x=get_hash_images()
	for F in A.settings.seed_hash:ROM().seek(B+297+C);ROM().write(F);js.document.getElementById('hash'+str(C)).src='data:image/jpeg;base64,'+x[F];C+=1
	E.run_until_complete(ProgressBar().update_progress(10,'Seed Generated.'));js.document.getElementById('nav-settings-tab').style.display=H
	if A.settings.generate_spoilerlog is True:js.document.getElementById(j).style.display=H;E.run_until_complete(GenerateSpoiler(A.json));js.document.getElementById(k).value=generateTracker(A.json)
	else:js.document.getElementById(l).innerHTML=H;js.document.getElementById(l).value=H;js.document.getElementById(k).value=H;js.document.getElementById(j).style.display='none'
	js.document.getElementById('generated_seed_id').innerHTML=A.settings.seed_id;d=json.loads(A.json)['Settings'];I={};O=0
	for P in range(0,3):js.document.getElementById(f"settings_table_{P}").innerHTML=H;I[P]=js.document.getElementById(f"settings_table_{P}")
	for (e,W) in d.items():
		f=['Seed','algorithm']
		if e not in f:
			if I[O].rows.length>math.ceil((len(d.items())-len(f))/len(I)):O+=1
			g=I[O].insertRow(-1);y=g.insertCell(0);z=g.insertCell(1);y.innerHTML=e;z.innerHTML=FormatSpoiler(W)
	ROM().fixSecurityValue();ROM().save(f"dk64-{A.settings.seed_id}.z64");E.run_until_complete(ProgressBar().reset());js.jq('#nav-settings-tab').tab('show')
def FormatSpoiler(value):'Format the values passed to the settings table into a more readable format.\n\n    Args:\n        value (str) or (bool)\n    ';A=str(value);B=A.replace('_',' ');C=B.title();return C