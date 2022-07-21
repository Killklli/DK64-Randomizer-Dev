'Apply Patch data to the ROM.'
import asyncio,codecs,json,pickle,random,js
from randomizer.CompileHints import compileHints
from randomizer.Enums.Transitions import Transitions
from randomizer.Patching.BananaPortRando import randomize_bananaport
from randomizer.Patching.BarrelRando import randomize_barrels
from randomizer.Patching.BossRando import randomize_bosses
from randomizer.Patching.CosmeticColors import apply_cosmetic_colors
from randomizer.Patching.DKTV import randomize_dktv
from randomizer.Patching.EnemyRando import randomize_enemies
from randomizer.Patching.EntranceRando import randomize_entrances
from randomizer.Patching.Hash import get_hash_images
from randomizer.Patching.KasplatLocationRando import randomize_kasplat_locations
from randomizer.Patching.KongRando import apply_kongrando_cosmetic
from randomizer.Patching.KRoolRando import randomize_krool
from randomizer.Patching.MoveLocationRando import randomize_moves
from randomizer.Patching.MusicRando import randomize_music
from randomizer.Patching.Patcher import ROM
from randomizer.Patching.PriceRando import randomize_prices
from randomizer.Patching.PuzzleRando import randomize_puzzles
from randomizer.Patching.UpdateHints import PushHints,wipeHints
from randomizer.Patching.MiscSetupChanges import randomize_setup
from GenTracker import generateTracker
from randomizer.Settings import Settings
from ui.progress_bar import ProgressBar
def patching_response(responded_data):
	'Response data from the background task.\n\n    Args:\n        responded_data (str): Pickled data (or json)\n    ';X='settings_table';W='tracker_text';V='spoiler_log_text';U='spoiler_log_block';T='seed';S='base64';R='error';J=responded_data;G='';E=asyncio.get_event_loop()
	try:
		K=json.loads(J)
		if K.get(R):L=K.get(R);ProgressBar().set_class('bg-danger');js.toast_alert(L);E.run_until_complete(ProgressBar().update_progress(10,f"Error: {L}"));E.run_until_complete(ProgressBar().reset());return None
	except Exception:pass
	E.run_until_complete(ProgressBar().update_progress(8,'Applying Patches'));A=pickle.loads(codecs.decode(J.encode(),S));A.settings.verify_hash();Settings({T:0}).compare_hash(A.settings.public_hash);A.settings.set_seed()
	if A.settings.download_patch_file:A.settings.download_patch_file=False;js.save_text_as_file(codecs.encode(pickle.dumps(A),S).decode(),f"dk64-{A.settings.seed_id}.lanky")
	B=33476640
	if A.settings.shuffle_loading_zones=='levels':
		ROM().seek(B+0);ROM().write(1);Y=[Transitions.IslesMainToJapesLobby,Transitions.IslesMainToAztecLobby,Transitions.IslesMainToFactoryLobby,Transitions.IslesMainToGalleonLobby,Transitions.IslesMainToForestLobby,Transitions.IslesMainToCavesLobby,Transitions.IslesMainToCastleLobby];Z=[Transitions.IslesJapesLobbyToMain,Transitions.IslesAztecLobbyToMain,Transitions.IslesFactoryLobbyToMain,Transitions.IslesGalleonLobbyToMain,Transitions.IslesForestLobbyToMain,Transitions.IslesCavesLobbyToMain,Transitions.IslesCastleLobbyToMain];C=0
		for a in Y:ROM().seek(B+1+C);ROM().write(Z.index(A.shuffled_exit_data[int(a)].reverse));C+=1
		b={Transitions.IslesMainToJapesLobby:Transitions.IslesJapesLobbyToMain,Transitions.IslesMainToAztecLobby:Transitions.IslesAztecLobbyToMain,Transitions.IslesMainToFactoryLobby:Transitions.IslesFactoryLobbyToMain,Transitions.IslesMainToGalleonLobby:Transitions.IslesGalleonLobbyToMain,Transitions.IslesMainToForestLobby:Transitions.IslesForestLobbyToMain,Transitions.IslesMainToCavesLobby:Transitions.IslesCavesLobbyToMain,Transitions.IslesMainToCastleLobby:Transitions.IslesCastleLobbyToMain};c={Transitions.IslesJapesLobbyToMain:26,Transitions.IslesAztecLobbyToMain:74,Transitions.IslesFactoryLobbyToMain:138,Transitions.IslesGalleonLobbyToMain:168,Transitions.IslesForestLobbyToMain:236,Transitions.IslesCavesLobbyToMain:292,Transitions.IslesCastleLobbyToMain:317};C=0
		for (F,M) in b.items():d=A.shuffled_exit_data.get(F).reverse;ROM().seek(B+30+C);ROM().writeMultipleBytes(c[int(d)],2);C+=2
	C=0
	for D in A.settings.BossBananas:ROM().seek(B+8+C);ROM().writeMultipleBytes(D,2);C+=2
	C=0
	for D in A.settings.EntryGBs:ROM().seek(B+22+C);ROM().writeMultipleBytes(D,1);C+=1
	if A.settings.starting_kongs_count==5:ROM().seek(B+44);ROM().write(31)
	else:
		N=0
		for e in A.settings.starting_kong_list:N|=1<<e
		ROM().seek(B+44);ROM().write(N)
	if A.settings.unlock_all_moves:ROM().seek(B+45);ROM().write(1)
	ROM().seek(B+46);ROM().write(1)
	if A.settings.unlock_fairy_shockwave:ROM().seek(B+47);ROM().write(1)
	if A.settings.enable_tag_anywhere:ROM().seek(B+48);ROM().write(1)
	if A.settings.fps_display:ROM().seek(B+150);ROM().write(1)
	if A.settings.helm_setting=='skip_start':ROM().seek(B+49);ROM().write(1)
	elif A.settings.helm_setting=='skip_all':ROM().seek(B+49);ROM().write(2)
	if A.settings.crown_door_open:ROM().seek(B+50);ROM().write(1)
	if A.settings.coin_door_open:ROM().seek(B+51);ROM().write(1)
	if A.settings.quality_of_life:ROM().seek(B+52);ROM().write(1)
	ROM().seek(B+165)
	if A.settings.damage_amount!='default':
		if A.settings.damage_amount=='double':ROM().write(2)
		elif A.settings.damage_amount=='ohko':ROM().write(12)
		elif A.settings.damage_amount=='quad':ROM().write(4)
	else:ROM().write(1)
	if A.settings.no_healing:ROM().seek(B+166);ROM().write(1)
	if A.settings.no_melons:ROM().seek(B+281);ROM().write(1)
	if A.settings.bonus_barrel_auto_complete:ROM().seek(B+279);ROM().write(1)
	if A.settings.warp_to_isles:ROM().seek(B+293);ROM().write(1)
	if A.settings.shop_indicator:ROM().seek(B+292);ROM().write(1)
	if A.settings.perma_death:ROM().seek(B+317);ROM().write(1);ROM().seek(B+318);ROM().write(1)
	if A.settings.open_lobbies:ROM().seek(B+316);ROM().write(255)
	if A.settings.disable_tag_barrels:ROM().seek(B+319);ROM().write(1)
	if A.settings.skip_arcader1:ROM().seek(B+294);ROM().write(1)
	if A.settings.disable_shop_hints:ROM().seek(B+315);ROM().write(0)
	if A.settings.open_levels:ROM().seek(B+295);ROM().write(1)
	if A.settings.shorten_boss:ROM().seek(B+299);ROM().write(1)
	if A.settings.fast_warps:ROM().seek(B+298);ROM().write(1)
	if A.settings.dpad_display:ROM().seek(B+297);ROM().write(1)
	if A.settings.activate_all_bananaports:ROM().seek(B+296);ROM().write(1)
	if A.settings.high_req:ROM().seek(B+361);ROM().write(1)
	if A.settings.fast_gbs:ROM().seek(B+362);ROM().write(1)
	H=[0,1,2,3,4,5,6,7]
	if len(A.settings.krool_keys_required)>0:
		for F in A.settings.krool_keys_required:
			O=F-4
			if O in H:H.remove(O)
	I=0
	for F in H:I=I|1<<F
	ROM().seek(B+280);ROM().write(I);ROM().seek(B+320);ROM().write(A.jetpac_medals_required);randomize_entrances(A);randomize_moves(A);randomize_prices(A);randomize_bosses(A);randomize_krool(A);randomize_barrels(A);randomize_bananaport(A);randomize_enemies(A);apply_kongrando_cosmetic(A);randomize_setup(A);randomize_puzzles(A);random.seed(A.settings.seed);randomize_music(A);apply_cosmetic_colors(A);random.seed(A.settings.seed)
	if A.settings.wrinkly_hints in['standard','cryptic']:wipeHints();compileHints(A);PushHints()
	C=0;f=get_hash_images()
	for D in A.settings.seed_hash:ROM().seek(B+282+C);ROM().write(D);js.document.getElementById('hash'+str(C)).src='data:image/jpeg;base64,'+f[D];C+=1
	E.run_until_complete(ProgressBar().update_progress(10,'Seed Generated.'));js.document.getElementById('nav-settings-tab').style.display=G
	if A.settings.generate_spoilerlog is True:js.document.getElementById(U).style.display=G;js.document.getElementById(V).value=A.toJson();js.document.getElementById(W).value=generateTracker(A.toJson())
	else:js.document.getElementById(V).value=G;js.document.getElementById(W).value=G;js.document.getElementById(U).style.display='none'
	js.document.getElementById('generated_seed_id').innerHTML=A.settings.seed_id;g=json.loads(A.toJson())['Settings'];js.document.getElementById(X).innerHTML=G;h=js.document.getElementById(X)
	for (P,M) in g.items():
		i=[T,'algorithm','starting_kong','starting_kong_list','diddy_freeing_kong','tiny_freeing_kong','lanky_freeing_kong','chunky_freeing_kong','banana_medals_required','krool_phases','krool_keys_required','blocker_golden_bananas','troff_n_scoff_bananas']
		if P not in i:Q=h.insertRow(-1);j=Q.insertCell(0);k=Q.insertCell(1);j.innerHTML=P;k.innerHTML=M
	ROM().fixSecurityValue();ROM().save(f"dk64-{A.settings.seed_id}.z64");E.run_until_complete(ProgressBar().reset());js.jq('#nav-settings-tab').tab('show')