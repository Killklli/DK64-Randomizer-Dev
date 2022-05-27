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
from randomizer.Patching.KongRando import apply_kongrando_cosmetic
from randomizer.Patching.KRoolRando import randomize_krool
from randomizer.Patching.MoveLocationRando import randomize_moves
from randomizer.Patching.MusicRando import randomize_music
from randomizer.Patching.Patcher import ROM
from randomizer.Patching.PriceRando import randomize_prices
from randomizer.Patching.PuzzleRando import randomize_puzzles
from randomizer.Patching.UpdateHints import PushHints
from randomizer.Settings import Settings
from ui.progress_bar import ProgressBar
def patching_response(responded_data):
	'Response data from the background task.\n\n    Args:\n        responded_data (str): Pickled data (or json)\n    ';X='settings_table';W='none';V='spoiler_log_text';U='spoiler_log_block';T='nav-settings-tab';S='seed';R='base64';Q='error';I=responded_data;E=asyncio.get_event_loop()
	try:
		J=json.loads(I)
		if J.get(Q):K=J.get(Q);ProgressBar().set_class('bg-danger');js.toast_alert(K);E.run_until_complete(ProgressBar().update_progress(10,f"Error: {K}"));E.run_until_complete(ProgressBar().reset());return None
	except Exception:pass
	E.run_until_complete(ProgressBar().update_progress(8,'Applying Patches'));A=pickle.loads(codecs.decode(I.encode(),R));A.settings.verify_hash();Settings({S:0}).compare_hash(A.settings.public_hash);A.settings.set_seed()
	if A.settings.download_patch_file:A.settings.download_patch_file=False;js.save_text_as_file(codecs.encode(pickle.dumps(A),R).decode(),f"dk64-{A.settings.seed_id}.lanky")
	B=33476640
	if A.settings.shuffle_loading_zones=='levels':
		ROM().seek(B+0);ROM().write(1);Y=[Transitions.IslesMainToJapesLobby,Transitions.IslesMainToAztecLobby,Transitions.IslesMainToFactoryLobby,Transitions.IslesMainToGalleonLobby,Transitions.IslesMainToForestLobby,Transitions.IslesMainToCavesLobby,Transitions.IslesMainToCastleLobby];Z=[Transitions.IslesJapesLobbyToMain,Transitions.IslesAztecLobbyToMain,Transitions.IslesFactoryLobbyToMain,Transitions.IslesGalleonLobbyToMain,Transitions.IslesForestLobbyToMain,Transitions.IslesCavesLobbyToMain,Transitions.IslesCastleLobbyToMain];C=0
		for a in Y:ROM().seek(B+1+C);ROM().write(Z.index(A.shuffled_exit_data[int(a)].reverse));C+=1
		b={Transitions.IslesMainToJapesLobby:Transitions.IslesJapesLobbyToMain,Transitions.IslesMainToAztecLobby:Transitions.IslesAztecLobbyToMain,Transitions.IslesMainToFactoryLobby:Transitions.IslesFactoryLobbyToMain,Transitions.IslesMainToGalleonLobby:Transitions.IslesGalleonLobbyToMain,Transitions.IslesMainToForestLobby:Transitions.IslesForestLobbyToMain,Transitions.IslesMainToCavesLobby:Transitions.IslesCavesLobbyToMain,Transitions.IslesMainToCastleLobby:Transitions.IslesCastleLobbyToMain};c={Transitions.IslesJapesLobbyToMain:26,Transitions.IslesAztecLobbyToMain:74,Transitions.IslesFactoryLobbyToMain:138,Transitions.IslesGalleonLobbyToMain:168,Transitions.IslesForestLobbyToMain:236,Transitions.IslesCavesLobbyToMain:292,Transitions.IslesCastleLobbyToMain:317};C=0
		for (F,L) in b.items():d=A.shuffled_exit_data.get(F).reverse;ROM().seek(B+30+C);ROM().writeMultipleBytes(c[int(d)],2);C+=2
	C=0
	for D in A.settings.BossBananas:ROM().seek(B+8+C);ROM().writeMultipleBytes(D,2);C+=2
	C=0
	for D in A.settings.EntryGBs:ROM().seek(B+22+C);ROM().writeMultipleBytes(D,1);C+=1
	if A.settings.starting_kongs_count==5:ROM().seek(B+44);ROM().write(31)
	else:
		M=0
		for e in A.settings.starting_kong_list:M|=1<<e
		ROM().seek(B+44);ROM().write(M)
	if A.settings.unlock_all_moves:ROM().seek(B+45);ROM().write(1)
	if A.settings.fast_start_beginning_of_game:ROM().seek(B+46);ROM().write(1)
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
	if A.settings.disable_shop_hints:ROM().seek(B+315);ROM().write(1)
	G=[0,1,2,3,4,5,6,7]
	if len(A.settings.krool_keys_required)>0:
		for F in A.settings.krool_keys_required:
			N=F-4
			if N in G:G.remove(N)
	H=0
	for F in G:H=H|1<<F
	ROM().seek(B+280);ROM().write(H);ROM().seek(B+320);ROM().write(A.jetpac_medals_required);randomize_dktv();randomize_entrances(A);randomize_moves(A);randomize_prices(A);randomize_bosses(A);randomize_krool(A);randomize_barrels(A);randomize_bananaport(A);randomize_enemies(A);apply_kongrando_cosmetic(A);randomize_puzzles();random.seed(A.settings.seed);randomize_music(A);apply_cosmetic_colors(A);random.seed(A.settings.seed)
	if A.settings.wrinkly_hints:compileHints(A);PushHints()
	C=0;f=get_hash_images()
	for D in A.settings.seed_hash:ROM().seek(B+282+C);ROM().write(D);js.document.getElementById('hash'+str(C)).src='data:image/jpeg;base64,'+f[D];C+=1
	E.run_until_complete(ProgressBar().update_progress(10,'Seed Generated.'))
	if A.settings.generate_spoilerlog is True:js.document.getElementById(T).style.display='';js.document.getElementById(U).style.display='';js.document.getElementById(V).value=A.toJson()
	else:js.document.getElementById(T).style.display=W;js.document.getElementById(V).value='';js.document.getElementById(U).style.display=W
	js.document.getElementById('generated_seed_id').innerHTML=A.settings.seed_id;g=json.loads(A.toJson())['Settings'];js.document.getElementById(X).innerHTML='';h=js.document.getElementById(X)
	for (O,L) in g.items():
		i=[S,'algorithm','starting_kong','starting_kong_list','diddy_freeing_kong','tiny_freeing_kong','lanky_freeing_kong','chunky_freeing_kong','banana_medals_required','krool_phases','krool_keys_required','blocker_golden_bananas','troff_n_scoff_bananas']
		if O not in i:P=h.insertRow(-1);j=P.insertCell(0);k=P.insertCell(1);j.innerHTML=O;k.innerHTML=L
	ROM().fixSecurityValue();ROM().save(f"dk64-{A.settings.seed_id}.z64");E.run_until_complete(ProgressBar().reset());js.jq('#nav-settings-tab').tab('show')