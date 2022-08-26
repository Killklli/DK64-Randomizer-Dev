'Apply Patch data to the ROM.'
import asyncio,codecs,json,math,pickle,random,js
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
from randomizer.Patching.MiscSetupChanges import randomize_setup
from randomizer.Patching.MoveLocationRando import randomize_moves
from randomizer.Patching.MusicRando import randomize_music
from randomizer.Patching.Patcher import ROM
from randomizer.Patching.PhaseRando import randomize_helm,randomize_krool
from randomizer.Patching.PriceRando import randomize_prices
from randomizer.Patching.PuzzleRando import randomize_puzzles
from randomizer.Patching.ShopRandomizer import ApplyShopRandomizer
from randomizer.Patching.UpdateHints import PushHints,wipeHints
from randomizer.Settings import Settings
from ui.GenTracker import generateTracker
from ui.progress_bar import ProgressBar
def patching_response(responded_data):
	'Response data from the background task.\n\n    Args:\n        responded_data (str): Pickled data (or json)\n    ';d='tracker_text';c='spoiler_log_text';b='spoiler_log_block';a='need_rw';Z='need_both';Y='base64';X='error';M=responded_data;G='';E=asyncio.get_event_loop()
	try:
		N=json.loads(M)
		if N.get(X):O=N.get(X);ProgressBar().set_class('bg-danger');js.toast_alert(O);E.run_until_complete(ProgressBar().update_progress(10,f"Error: {O}"));E.run_until_complete(ProgressBar().reset());return None
	except Exception:pass
	E.run_until_complete(ProgressBar().update_progress(8,'Applying Patches'));A=pickle.loads(codecs.decode(M.encode(),Y));A.settings.verify_hash();Settings({'seed':0}).compare_hash(A.settings.public_hash);A.settings.set_seed()
	if A.settings.download_patch_file:A.settings.download_patch_file=False;js.save_text_as_file(codecs.encode(pickle.dumps(A),Y).decode(),f"dk64-{A.settings.seed_id}.lanky")
	B=A.settings.rom_data
	if A.settings.shuffle_loading_zones=='levels':
		ROM().seek(B+0);ROM().write(1);e=[Transitions.IslesMainToJapesLobby,Transitions.IslesMainToAztecLobby,Transitions.IslesMainToFactoryLobby,Transitions.IslesMainToGalleonLobby,Transitions.IslesMainToForestLobby,Transitions.IslesMainToCavesLobby,Transitions.IslesMainToCastleLobby];f=[Transitions.IslesJapesLobbyToMain,Transitions.IslesAztecLobbyToMain,Transitions.IslesFactoryLobbyToMain,Transitions.IslesGalleonLobbyToMain,Transitions.IslesForestLobbyToMain,Transitions.IslesCavesLobbyToMain,Transitions.IslesCastleLobbyToMain];C=0
		for g in e:ROM().seek(B+1+C);ROM().write(f.index(A.shuffled_exit_data[int(g)].reverse));C+=1
		h={Transitions.IslesMainToJapesLobby:Transitions.IslesJapesLobbyToMain,Transitions.IslesMainToAztecLobby:Transitions.IslesAztecLobbyToMain,Transitions.IslesMainToFactoryLobby:Transitions.IslesFactoryLobbyToMain,Transitions.IslesMainToGalleonLobby:Transitions.IslesGalleonLobbyToMain,Transitions.IslesMainToForestLobby:Transitions.IslesForestLobbyToMain,Transitions.IslesMainToCavesLobby:Transitions.IslesCavesLobbyToMain,Transitions.IslesMainToCastleLobby:Transitions.IslesCastleLobbyToMain};i={Transitions.IslesJapesLobbyToMain:26,Transitions.IslesAztecLobbyToMain:74,Transitions.IslesFactoryLobbyToMain:138,Transitions.IslesGalleonLobbyToMain:168,Transitions.IslesForestLobbyToMain:236,Transitions.IslesCavesLobbyToMain:292,Transitions.IslesCastleLobbyToMain:317};C=0
		for (F,P) in h.items():j=A.shuffled_exit_data.get(F).reverse;ROM().seek(B+30+C);ROM().writeMultipleBytes(i[int(j)],2);C+=2
	C=0
	for D in A.settings.BossBananas:ROM().seek(B+8+C);ROM().writeMultipleBytes(D,2);C+=2
	C=0
	for D in A.settings.EntryGBs:ROM().seek(B+22+C);ROM().writeMultipleBytes(D,1);C+=1
	if A.settings.starting_kongs_count==5:ROM().seek(B+44);ROM().write(31)
	else:
		Q=0
		for k in A.settings.starting_kong_list:Q|=1<<k
		ROM().seek(B+44);ROM().write(Q)
	if A.settings.unlock_all_moves:ROM().seek(B+45);ROM().write(1)
	ROM().seek(B+46);ROM().write(1)
	if A.settings.unlock_fairy_shockwave:ROM().seek(B+47);ROM().write(1)
	if A.settings.enable_tag_anywhere:ROM().seek(B+48);ROM().write(1)
	if A.settings.fps_display:ROM().seek(B+150);ROM().write(1)
	if A.settings.helm_setting=='skip_start':ROM().seek(B+49);ROM().write(1)
	elif A.settings.helm_setting=='skip_all':ROM().seek(B+49);ROM().write(2)
	if A.settings.crown_door_open:ROM().seek(B+50);ROM().write(1)
	if A.settings.coin_door_open==Z:ROM().seek(B+51);ROM().write(0)
	elif A.settings.coin_door_open=='need_zero':ROM().seek(B+51);ROM().write(1)
	elif A.settings.coin_door_open=='need_nin':ROM().seek(B+51);ROM().write(2)
	elif A.settings.coin_door_open==a:ROM().seek(B+51);ROM().write(3)
	if A.settings.quality_of_life:ROM().seek(B+52);ROM().write(1)
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
	if A.settings.shop_indicator:ROM().seek(B+308);ROM().write(1)
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
		for R in range(3):ROM().seek(B+379+R);ROM().write(A.settings.kko_phase_order[R])
	I=[0,1,2,3,4,5,6,7]
	if len(A.settings.krool_keys_required)>0:
		for F in A.settings.krool_keys_required:
			S=F-4
			if S in I:I.remove(S)
	J=0
	for F in I:J=J|1<<F
	ROM().seek(B+295);ROM().write(J)
	if A.settings.coin_door_open in[Z,a]:ROM().seek(B+336);ROM().write(A.settings.medal_requirement)
	randomize_entrances(A);randomize_moves(A);randomize_prices(A);randomize_bosses(A);randomize_krool(A);randomize_helm(A);randomize_barrels(A);randomize_bananaport(A);randomize_kasplat_locations(A);randomize_enemies(A);apply_kongrando_cosmetic(A);randomize_setup(A);randomize_puzzles(A);ApplyShopRandomizer(A);random.seed(A.settings.seed);randomize_music(A);apply_cosmetic_colors(A);random.seed(A.settings.seed)
	if A.settings.wrinkly_hints in['standard','cryptic']:wipeHints();PushHints(A)
	C=0;l=get_hash_images()
	for D in A.settings.seed_hash:ROM().seek(B+297+C);ROM().write(D);js.document.getElementById('hash'+str(C)).src='data:image/jpeg;base64,'+l[D];C+=1
	E.run_until_complete(ProgressBar().update_progress(10,'Seed Generated.'));js.document.getElementById('nav-settings-tab').style.display=G
	if A.settings.generate_spoilerlog is True:js.document.getElementById(b).style.display=G;js.document.getElementById(c).value=A.toJson();js.document.getElementById(d).value=generateTracker(A.toJson())
	else:js.document.getElementById(c).value=G;js.document.getElementById(d).value=G;js.document.getElementById(b).style.display='none'
	js.document.getElementById('generated_seed_id').innerHTML=A.settings.seed_id;T=json.loads(A.toJson())['Settings'];H={};K=0
	for L in range(0,3):js.document.getElementById(f"settings_table_{L}").innerHTML=G;H[L]=js.document.getElementById(f"settings_table_{L}")
	for (U,P) in T.items():
		V=['Seed','algorithm','starting_kong','Starting Kong List','Diddy Freeing Kong','Tiny Freeing Kong','Lanky Freeing Kong','Chunky Freeing Kong','Medal Requirement','K Rool Phases','Keys Required for K Rool','B Locker GBs','Troff N Scoff Bananas','Colors']
		if U not in V:
			if H[K].rows.length>math.ceil((len(T.items())-len(V))/len(H)):K+=1
			W=H[K].insertRow(-1);m=W.insertCell(0);n=W.insertCell(1);m.innerHTML=U;n.innerHTML=FormatSpoiler(P)
	ROM().fixSecurityValue();ROM().save(f"dk64-{A.settings.seed_id}.z64");E.run_until_complete(ProgressBar().reset());js.jq('#nav-settings-tab').tab('show')
def FormatSpoiler(value):'Format the values passed to the settings table into a more readable format.\n\n    Args:\n        value (str) or (bool)\n    ';A=str(value);B=A.replace('_',' ');C=B.title();return C