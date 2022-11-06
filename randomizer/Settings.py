'Settings class and functions.'
_L='item_shuffle'
_K='loadingzonesdecoupled'
_J='loadingzone'
_I='normal'
_H='all'
_G='start_with'
_F='none'
_E='off'
_D='vanilla'
_C=True
_B=None
_A=False
import hashlib,inspect,json,random,sys
from random import randint
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import GetKongs,Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Types import Types
import randomizer.ItemPool as ItemPool
from randomizer.Lists.Item import ItemList
from randomizer.Lists.Location import ChunkyMoveLocations,DiddyMoveLocations,DonkeyMoveLocations,LankyMoveLocations,LocationList,SharedShopLocations,TinyMoveLocations,TrainingBarrelLocations
from randomizer.Prices import CompleteVanillaPrices,RandomizePrices,VanillaPrices
from randomizer.ShuffleBosses import ShuffleBosses,ShuffleBossKongs,ShuffleKKOPhaseOrder,ShuffleKutoutKongs
class Settings:
	'Class used to store settings for seed generation.'
	def __init__(A,form_data):
		'Init all the settings using the form data to set the flags.\n\n        Args:\n            form_data (dict): Post data from the html form.\n        ';A.__hash=A.__get_hash();A.public_hash=A.__get_hash();A.algorithm='forward';A.generate_main();A.generate_progression();A.generate_misc();A.rom_data=33476640;A.move_location_data=33484800
		for (B,C) in form_data.items():setattr(A,B,C)
		A.seed_id=str(A.seed);A.seed=str(A.seed)+A.__hash;A.set_seed();A.seed_hash=[random.randint(0,9)for A in range(5)];A.krool_keys_required=[];A.blocker_max=int(A.blocker_text)if A.blocker_text else 50;A.troff_max=int(A.troff_text)if A.troff_text else 270;A.troff_min=[0.25,0.3,0.35,0.4,0.45,0.5,0.55]
		if A.hard_troff_n_scoff:A.troff_min=[0.45,0.5,0.55,0.6,0.65,0.7,0.75]
		if A.hard_level_progression:A.troff_min=[A.troff_min[-1]for B in A.troff_min]
		A.unlock_all_moves=_A;A.progressive_upgrades=_A;CompleteVanillaPrices();A.prices=VanillaPrices.copy();A.level_order={1:Levels.JungleJapes,2:Levels.AngryAztec,3:Levels.FranticFactory,4:Levels.GloomyGalleon,5:Levels.FungiForest,6:Levels.CrystalCaves,7:Levels.CreepyCastle};A.owned_kongs_by_level={Levels.JungleJapes:GetKongs().copy(),Levels.AngryAztec:GetKongs().copy(),Levels.FranticFactory:GetKongs().copy(),Levels.GloomyGalleon:GetKongs().copy(),Levels.FungiForest:GetKongs().copy(),Levels.CrystalCaves:GetKongs().copy(),Levels.CreepyCastle:GetKongs().copy()};A.owned_moves_by_level={Levels.JungleJapes:ItemPool.AllKongMoves().copy(),Levels.AngryAztec:ItemPool.AllKongMoves().copy(),Levels.FranticFactory:ItemPool.AllKongMoves().copy(),Levels.GloomyGalleon:ItemPool.AllKongMoves().copy(),Levels.FungiForest:ItemPool.AllKongMoves().copy(),Levels.CrystalCaves:ItemPool.AllKongMoves().copy(),Levels.CreepyCastle:ItemPool.AllKongMoves().copy()};A.resolve_settings();A.update_valid_locations()
	def update_progression_totals(A):
		"Update the troff and blocker totals if we're randomly setting them.";A.troff_weight_0=0.5;A.troff_weight_1=0.55;A.troff_weight_2=0.6;A.troff_weight_3=0.7;A.troff_weight_4=0.8;A.troff_weight_5=0.9;A.troff_weight_6=1.0
		if A.level_randomization in(_J,_K)or A.hard_level_progression:A.troff_weight_0=1;A.troff_weight_1=1;A.troff_weight_2=1;A.troff_weight_3=1;A.troff_weight_4=1;A.troff_weight_5=1;A.troff_weight_6=1
		if A.randomize_cb_required_amounts:
			D=[]
			for E in A.troff_min:D.append(random.randint(round(A.troff_max*E),A.troff_max))
			C=D;A.troff_0=round(min(C[0]*A.troff_weight_0,500));A.troff_1=round(min(C[1]*A.troff_weight_1,500));A.troff_2=round(min(C[2]*A.troff_weight_2,500));A.troff_3=round(min(C[3]*A.troff_weight_3,500));A.troff_4=round(min(C[4]*A.troff_weight_4,500));A.troff_5=round(min(C[5]*A.troff_weight_5,500));A.troff_6=round(min(C[6]*A.troff_weight_6,500))
		if A.randomize_blocker_required_amounts:
			D=random.sample(range(1,A.blocker_max),7);B=D
			if A.shuffle_loading_zones==_H or A.hard_level_progression:B.append(random.randint(1,A.blocker_max));random.shuffle(B)
			else:B.append(1);B.sort()
			A.blocker_0=B[0];A.blocker_1=B[1];A.blocker_2=B[2];A.blocker_3=B[3];A.blocker_4=B[4];A.blocker_5=B[5];A.blocker_6=B[6]
			if A.maximize_helm_blocker:A.blocker_7=A.blocker_max
			else:A.blocker_7=B[7]
		A.EntryGBs=[A.blocker_0,A.blocker_1,A.blocker_2,A.blocker_3,A.blocker_4,A.blocker_5,A.blocker_6,A.blocker_7];A.BossBananas=[A.troff_0,A.troff_1,A.troff_2,A.troff_3,A.troff_4,A.troff_5,A.troff_6]
	def generate_main(A):'Set Default items on main page.';A.seed=_B;A.download_patch_file=_B;A.bonus_barrel_rando=_B;A.loading_zone_coupled=_B;A.move_rando=_E;A.random_patches=_B;A.random_prices=_B;A.boss_location_rando=_B;A.boss_kong_rando=_B;A.kasplat_rando_setting=_B;A.puzzle_rando=_B;A.shuffle_shops=_B;A.shuffle_items=_C;A.free_trade_setting=_F
	def set_seed(A):'Forcibly re-set the random seed to the seed set in the config.';random.seed(A.seed)
	def generate_progression(A):'Set default items on progression page.';A.blocker_0=_B;A.blocker_1=_B;A.blocker_2=_B;A.blocker_3=_B;A.blocker_4=_B;A.blocker_5=_B;A.blocker_6=_B;A.blocker_7=_B;A.troff_0=_B;A.troff_1=_B;A.troff_2=_B;A.troff_3=_B;A.troff_4=_B;A.troff_5=_B;A.troff_6=_B;A.troff_min=_B;A.troff_max=_B;A.blocker_text=_B;A.troff_text=_B
	def generate_misc(A):'Set default items on misc page.';C='default';B='#000000';A.crown_door_open=_B;A.coin_door_open=_B;A.krool_phase_count=5;A.krool_random=_A;A.helm_phase_count=3;A.helm_random=_A;A.krool_key_count=8;A.keys_random=_A;A.starting_kongs_count=5;A.starting_random=_A;A.bonus_barrels=_I;A.helm_barrels=_I;A.bonus_barrel_auto_complete=_A;A.hard_shooting=_A;A.hard_bosses=_A;A.damage_amount=C;A.no_logic=_A;A.shuffle_loading_zones=_F;A.decoupled_loading_zones=_A;A.training_barrels=_I;A.shockwave_status=_D;A.music_bgm=C;A.music_fanfares=C;A.music_events=C;A.random_music=_A;A.colors={};A.color_palettes={};A.klaptrap_model='green';A.klaptrap_model_index=33;A.dk_colors=_D;A.dk_custom_color=B;A.diddy_colors=_D;A.diddy_custom_color=B;A.lanky_colors=_D;A.lanky_custom_color=B;A.tiny_colors=_D;A.tiny_custom_color=B;A.chunky_colors=_D;A.chunky_custom_color=B;A.rambi_colors=_D;A.rambi_custom_color=B;A.enguarde_colors=_D;A.enguarde_custom_color=B;A.disco_chunky=_A;A.krusha_slot='no_slot';A.misc_cosmetics=_A;A.remove_water_oscillation=_A;A.generate_spoilerlog=_B;A.fast_start_beginning_of_game=_B;A.helm_setting=_B;A.quality_of_life=_B;A.shorten_boss=_A;A.enable_tag_anywhere=_B;A.krool_phase_order_rando=_B;A.krool_access=_A;A.helm_phase_order_rando=_B;A.open_lobbies=_B;A.open_levels=_B;A.randomize_pickups=_A;A.random_medal_requirement=_A;A.medal_requirement=15;A.medal_cb_req=75;A.bananaport_rando=_E;A.activate_all_bananaports=_E;A.shop_indicator=_A;A.randomize_cb_required_amounts=_A;A.randomize_blocker_required_amounts=_A;A.maximize_helm_blocker=_A;A.perma_death=_A;A.disable_tag_barrels=_A;A.level_randomization=_F;A.kong_rando=_A;A.kongs_for_progression=_A;A.wrinkly_hints=_E;A.fast_warps=_A;A.dpad_display=_A;A.high_req=_A;A.fast_gbs=_A;A.auto_keys=_A;A.kko_phase_order=[0,0,0];A.enemy_rando=_A;A.crown_enemy_rando=_E;A.enemy_speed_rando=_A;A.cb_rando=_A;A.crown_placement_rando=_A;A.override_cosmetics=_A;A.random_colors=_A;A.hard_level_progression=_A;A.hard_blockers=_A;A.hard_troff_n_scoff=_A;A.hard_enemies=_A;A.wrinkly_location_rando=_A;A.tns_location_rando=_A;A.minigames_list_selected=[];A.item_rando_list_selected=[];A.misc_changes_selected=[];A.enemies_selected=[];A.starting_keys_list_selected=[];A.select_keys=_A;A.helm_hurry=_A;A.colorblind_mode=_E;A.win_condition='beat_krool';A.key_8_helm=_A
	def shuffle_prices(A):
		'Price randomization. Reuseable if we need to reshuffle prices.'
		if A.random_prices!=_D:A.prices=RandomizePrices(A.random_prices)
	def resolve_settings(A):
		'Resolve settings which are not directly set through the UI.';O='levels';N='random';M='skip';J=GetKongs();A.shuffled_location_types=[]
		if A.shuffle_items:
			if not A.item_rando_list_selected:A.shuffled_location_types=[Types.Shop,Types.Banana,Types.Crown,Types.Blueprint,Types.Key,Types.Medal,Types.Coin]
			else:
				for P in A.item_rando_list_selected:
					for type in Types:
						if type.name==P.capitalize():A.shuffled_location_types.append(type)
			if Types.Shop in A.shuffled_location_types:
				if A.move_rando!=_G:A.move_rando=_L
				if A.shockwave_status not in(_D,_G):A.shuffled_location_types.append(Types.Shockwave)
				if A.training_barrels!=_I:A.shuffled_location_types.append(Types.TrainingBarrel)
		A.progressives_locked_in_shops=_A;A.shuffle_prices();A.update_progression_totals();A.krool_donkey=_A;A.krool_diddy=_A;A.krool_lanky=_A;A.krool_tiny=_A;A.krool_chunky=_A;G=J.copy()
		if A.krool_phase_order_rando:random.shuffle(G)
		if A.krool_random:A.krool_phase_count=randint(1,5)
		if isinstance(A.krool_phase_count,str)is _C:A.krool_phase_count=5
		if A.krool_phase_count<5:G=random.sample(G,A.krool_phase_count)
		E=[]
		for B in G:
			if B==Kongs.donkey:A.krool_donkey=_C;E.append(Kongs.donkey)
			if B==Kongs.diddy:A.krool_diddy=_C;E.append(Kongs.diddy)
			if B==Kongs.lanky:A.krool_lanky=_C;E.append(Kongs.lanky)
			if B==Kongs.tiny:A.krool_tiny=_C;E.append(Kongs.tiny)
			if B==Kongs.chunky:A.krool_chunky=_C;E.append(Kongs.chunky)
		A.krool_order=E;A.helm_donkey=_A;A.helm_diddy=_A;A.helm_lanky=_A;A.helm_tiny=_A;A.helm_chunky=_A;H=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy]
		if A.helm_phase_order_rando:random.shuffle(H)
		if A.helm_random:A.helm_phase_count=randint(1,5)
		if isinstance(A.helm_phase_count,str)is _C:A.helm_phase_count=5
		if A.helm_phase_count<5:H=random.sample(H,A.helm_phase_count)
		F=[]
		for B in H:
			if B==Kongs.donkey:F.append(0);A.helm_donkey=_C
			elif B==Kongs.diddy:A.helm_diddy=_C;F.append(4)
			elif B==Kongs.lanky:A.helm_lanky=_C;F.append(3)
			elif B==Kongs.tiny:A.helm_tiny=_C;F.append(2)
			elif B==Kongs.chunky:A.helm_chunky=_C;F.append(1)
		A.helm_order=F;K=[Events.JapesKeyTurnedIn,Events.AztecKeyTurnedIn,Events.FactoryKeyTurnedIn,Events.GalleonKeyTurnedIn,Events.ForestKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn,Events.HelmKeyTurnedIn];C=K.copy();I=0
		if A.keys_random:I=randint(0,8)
		if A.select_keys:
			A.krool_keys_required=K.copy()
			for D in A.starting_keys_list_selected:
				if D=='key1':A.krool_keys_required.remove(C[0])
				if D=='key2':A.krool_keys_required.remove(C[1])
				if D=='key3':A.krool_keys_required.remove(C[2])
				if D=='key4':A.krool_keys_required.remove(C[3])
				if D=='key5':A.krool_keys_required.remove(C[4])
				if D=='key6':A.krool_keys_required.remove(C[5])
				if D=='key7':A.krool_keys_required.remove(C[6])
				if D=='key8':A.krool_keys_required.remove(C[7])
		else:I=A.krool_key_count
		if A.krool_access or A.win_condition=='get_key8':A.krool_keys_required.append(Events.HelmKeyTurnedIn);C.remove(Events.HelmKeyTurnedIn);I-=1
		if not A.select_keys:
			random.shuffle(C)
			for Q in range(I):A.krool_keys_required.append(C[Q])
		if Events.JapesKeyTurnedIn not in A.krool_keys_required:ItemList[Items.JungleJapesKey].playthrough=_A
		if Events.AztecKeyTurnedIn not in A.krool_keys_required:ItemList[Items.AngryAztecKey].playthrough=_A
		if Events.FactoryKeyTurnedIn not in A.krool_keys_required:ItemList[Items.FranticFactoryKey].playthrough=_A
		if Events.GalleonKeyTurnedIn not in A.krool_keys_required:ItemList[Items.GloomyGalleonKey].playthrough=_A
		if Events.ForestKeyTurnedIn not in A.krool_keys_required:ItemList[Items.FungiForestKey].playthrough=_A
		if Events.CavesKeyTurnedIn not in A.krool_keys_required:ItemList[Items.CrystalCavesKey].playthrough=_A
		if Events.CastleKeyTurnedIn not in A.krool_keys_required:ItemList[Items.CreepyCastleKey].playthrough=_A
		if Events.HelmKeyTurnedIn not in A.krool_keys_required:ItemList[Items.HideoutHelmKey].playthrough=_A
		if A.key_8_helm:LocationList[Locations.HelmKey].type=Types.Constant
		if A.random_medal_requirement:A.medal_requirement=round(random.normalvariate(10,1.5))
		A.boss_maps=ShuffleBosses(A.boss_location_rando);A.boss_kongs=ShuffleBossKongs(A);A.kutout_kongs=ShuffleKutoutKongs(A.boss_maps,A.boss_kongs,A.boss_kong_rando);A.kko_phase_order=ShuffleKKOPhaseOrder(A)
		if A.bonus_barrel_auto_complete:A.bonus_barrels=M
		elif A.bonus_barrel_rando and not A.minigames_list_selected:A.bonus_barrels=N
		elif A.bonus_barrel_rando and A.minigames_list_selected:A.bonus_barrels='selected'
		if A.helm_setting=='skip_all':A.helm_barrels=M
		elif A.bonus_barrel_rando:A.helm_barrels=N
		if A.level_randomization=='level_order':A.shuffle_loading_zones=O
		elif A.level_randomization==_J:A.shuffle_loading_zones=_H
		elif A.level_randomization==_K:A.shuffle_loading_zones=_H;A.decoupled_loading_zones=_C
		elif A.level_randomization==_D:A.shuffle_loading_zones=_F
		if A.starting_random:A.starting_kongs_count=randint(1,5)
		if A.starting_kongs_count==5:A.kong_rando=_A
		if A.kong_rando:A.starting_kong_list=random.sample(J,A.starting_kongs_count);A.starting_kong=random.choice(A.starting_kong_list);A.diddy_freeing_kong=Kongs.any;A.lanky_freeing_kong=Kongs.any;A.tiny_freeing_kong=Kongs.any;A.chunky_freeing_kong=Kongs.any;A.kong_locations=A.SelectKongLocations()
		else:
			A.possible_kong_list=J.copy();A.possible_kong_list.remove(0);A.starting_kong_list=random.sample(A.possible_kong_list,A.starting_kongs_count-1);A.starting_kong_list.append(Kongs.donkey);A.starting_kong=Kongs.donkey;A.diddy_freeing_kong=Kongs.donkey;A.lanky_freeing_kong=Kongs.donkey;A.tiny_freeing_kong=Kongs.diddy;A.chunky_freeing_kong=Kongs.lanky;A.kong_locations=[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]
			if Kongs.diddy in A.starting_kong_list:A.kong_locations.remove(Locations.DiddyKong)
			if Kongs.lanky in A.starting_kong_list:A.kong_locations.remove(Locations.LankyKong)
			if Kongs.tiny in A.starting_kong_list:A.kong_locations.remove(Locations.TinyKong)
			if Kongs.chunky in A.starting_kong_list:A.kong_locations.remove(Locations.ChunkyKong)
		LocationList[Locations.IslesDonkeyJapesRock].kong=A.starting_kong
		if A.starting_kongs_count<5 and(A.shuffle_loading_zones==O or A.shuffle_loading_zones==_F)and not A.no_logic:A.kongs_for_progression=_C
		if A.move_rando==_G:A.unlock_all_moves=_C
		A.kasplat_rando=_A;A.kasplat_location_rando=_A
		if A.kasplat_rando_setting=='vanilla_locations':A.kasplat_rando=_C
		if A.kasplat_rando_setting=='location_shuffle':A.kasplat_rando=_C;A.kasplat_location_rando=_C
		if A.win_condition=='all_fairies':ItemList[Items.BananaFairy].playthrough=_C
		if A.win_condition=='all_blueprints':
			for L in ItemList:
				if ItemList[L].type==Types.Blueprint:ItemList[L].playthrough=_C
		if A.win_condition=='all_medals':ItemList[Items.BananaMedal].playthrough=_C
		if not A.crown_door_open:ItemList[Items.BattleCrown].playthrough=_C
		A.free_trade_items=A.free_trade_setting!=_F;A.free_trade_blueprints=A.free_trade_setting=='major_collectibles'
	def update_valid_locations(A):
		'Calculate (or recalculate) valid locations for items by type.';G='shuffled';A.valid_locations={};A.valid_locations[Types.Kong]=[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]
		if A.move_rando not in(_E,_L):
			A.valid_locations[Types.Shop]={}
			if A.move_rando=='on':A.valid_locations[Types.Shop][Kongs.donkey]=DonkeyMoveLocations.copy();A.valid_locations[Types.Shop][Kongs.diddy]=DiddyMoveLocations.copy();A.valid_locations[Types.Shop][Kongs.lanky]=LankyMoveLocations.copy();A.valid_locations[Types.Shop][Kongs.tiny]=TinyMoveLocations.copy();A.valid_locations[Types.Shop][Kongs.chunky]=ChunkyMoveLocations.copy()
			elif A.move_rando=='cross_purchase':
				B=DonkeyMoveLocations.copy();B.update(DiddyMoveLocations.copy());B.update(TinyMoveLocations.copy());B.update(ChunkyMoveLocations.copy());B.update(LankyMoveLocations.copy())
				if A.training_barrels==G and Types.TrainingBarrel not in A.shuffled_location_types:B.update(TrainingBarrelLocations.copy())
				if A.shockwave_status in(_D,_G)and Types.Shockwave not in A.shuffled_location_types:B.remove(Locations.CameraAndShockwave)
				A.valid_locations[Types.Shop][Kongs.donkey]=B;A.valid_locations[Types.Shop][Kongs.diddy]=B;A.valid_locations[Types.Shop][Kongs.lanky]=B;A.valid_locations[Types.Shop][Kongs.tiny]=B;A.valid_locations[Types.Shop][Kongs.chunky]=B
			A.valid_locations[Types.Shop][Kongs.any]=SharedShopLocations
			if A.shockwave_status not in(_D,_G)and Types.Shockwave not in A.shuffled_location_types:A.valid_locations[Types.Shop][Kongs.any].add(Locations.CameraAndShockwave)
			elif Locations.CameraAndShockwave in A.valid_locations[Types.Shop][Kongs.tiny]:A.valid_locations[Types.Shop][Kongs.tiny].remove(Locations.CameraAndShockwave)
			if A.training_barrels==G and Types.TrainingBarrel not in A.shuffled_location_types:
				for H in Kongs:A.valid_locations[Types.Shop][H].update(TrainingBarrelLocations.copy())
			A.valid_locations[Types.Shockwave]=A.valid_locations[Types.Shop][Kongs.any];A.valid_locations[Types.TrainingBarrel]=A.valid_locations[Types.Shop][Kongs.any]
		if any(A.shuffled_location_types):
			C=[B for B in LocationList if LocationList[B].type in A.shuffled_location_types]
			if Types.Shop in A.shuffled_location_types:
				A.valid_locations[Types.Shop]={};B=DonkeyMoveLocations.copy();B.update(DiddyMoveLocations.copy());B.update(TinyMoveLocations.copy());B.update(ChunkyMoveLocations.copy());B.update(LankyMoveLocations.copy());F=[A for A in C if A not in B];A.valid_locations[Types.Shop][Kongs.any]=F
				if Types.Shockwave in A.shuffled_location_types:F.append(Locations.CameraAndShockwave);A.valid_locations[Types.Shockwave]=F
				if Types.TrainingBarrel in A.shuffled_location_types:A.valid_locations[Types.TrainingBarrel]=F
				D=[A for A in C if A not in SharedShopLocations];A.valid_locations[Types.Shop][Kongs.donkey]=D;A.valid_locations[Types.Shop][Kongs.diddy]=D;A.valid_locations[Types.Shop][Kongs.lanky]=D;A.valid_locations[Types.Shop][Kongs.tiny]=D;A.valid_locations[Types.Shop][Kongs.chunky]=D
			if Types.Blueprint in A.shuffled_location_types:I=[B for B in A.shuffled_location_types if B not in(Types.Crown,Types.Key)];J=Locations.IslesDonkeyJapesRock,Locations.JapesDonkeyFrontofCage,Locations.JapesDonkeyFreeDiddy,Locations.AztecDiddyFreeTiny,Locations.AztecDonkeyFreeLanky,Locations.FactoryLankyFreeChunky;E=[A for A in LocationList if A not in J and LocationList[A].type in I];A.valid_locations[Types.Blueprint]={};A.valid_locations[Types.Blueprint][Kongs.donkey]=[A for A in E if LocationList[A].kong==Kongs.donkey];A.valid_locations[Types.Blueprint][Kongs.diddy]=[A for A in E if LocationList[A].kong==Kongs.diddy];A.valid_locations[Types.Blueprint][Kongs.lanky]=[A for A in E if LocationList[A].kong==Kongs.lanky];A.valid_locations[Types.Blueprint][Kongs.tiny]=[A for A in E if LocationList[A].kong==Kongs.tiny];A.valid_locations[Types.Blueprint][Kongs.chunky]=[A for A in E if LocationList[A].kong==Kongs.chunky]
			if Types.Banana in A.shuffled_location_types:A.valid_locations[Types.Banana]=C
			if Types.Crown in A.shuffled_location_types:K=Locations.HelmDonkeyMedal,Locations.HelmDiddyMedal,Locations.HelmLankyMedal,Locations.HelmTinyMedal,Locations.HelmChunkyMedal,Locations.JapesDiddyMinecarts,Locations.CastleDonkeyMinecarts,Locations.ForestChunkyMinecarts,Locations.IslesDonkeyInstrumentPad,Locations.IslesDiddyInstrumentPad,Locations.IslesLankyInstrumentPad,Locations.IslesTinyInstrumentPad,Locations.IslesChunkyInstrumentPad;A.valid_locations[Types.Crown]=[A for A in C if A not in K]
			if Types.Key in A.shuffled_location_types:A.valid_locations[Types.Key]=C
			if Types.Medal in A.shuffled_location_types:A.valid_locations[Types.Medal]=C
			if Types.Coin in A.shuffled_location_types:A.valid_locations[Types.Coin]=C
	def GetValidLocationsForItem(C,item_id):
		'Return the valid locations the input item id can be placed in.';A=ItemList[item_id];B=[]
		if A.type in(Types.Shop,Types.Blueprint):B=C.valid_locations[A.type][A.kong]
		else:B=C.valid_locations[A.type]
		if C.progressives_locked_in_shops and A in SharedShopLocations:B=SharedShopLocations
		return B
	def SelectKongLocations(B):
		'Select which random kong locations to use depending on number of starting kongs.';A=[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]
		for E in range(0,B.starting_kongs_count-1):D=random.choice(A);A.remove(D)
		C=B.open_levels or B.activate_all_bananaports==_H
		if not C and B.starting_kongs_count==3 and Kongs.diddy not in B.starting_kong_list and Kongs.chunky not in B.starting_kong_list and Locations.TinyKong in A and Locations.LankyKong in A:A.pop();A.append(random.choice(Locations.DiddyKong,Locations.ChunkyKong))
		if not C and B.starting_kongs_count==4 and Kongs.diddy not in B.starting_kong_list and Locations.LankyKong in A:A.remove(Locations.LankyKong);A.append(random.choice(Locations.DiddyKong,Locations.TinyKong,Locations.ChunkyKong))
		return A
	def __repr__(A):'Return printable version of the object as json.\n\n        Returns:\n            str: Json string of the dict.\n        ';return json.dumps(A.__dict__)
	@staticmethod
	def __get_hash():
		'Get the hash value of all of the source code loaded.';B=[];A=[];A.append(inspect.getsource(Settings));A.append(inspect.getsource(__import__('randomizer.Spoiler')));A.append(inspect.getsource(__import__('randomizer.Fill')));A.append(inspect.getsource(__import__('randomizer.BackgroundRandomizer')))
		try:A.append(inspect.getsource(__import__('version')))
		except Exception:pass
		for C in sorted(A):B.append(hashlib.md5(C.encode('utf-8')).hexdigest())
		return ''.join(B)
	def compare_hash(A,hash):
		'Compare our hash with a passed hash value.'
		if A.__hash!=hash:raise Exception('Error: Comparison failed, Hashes do not match.')
	def verify_hash(A):
		'Verify our hash files match our existing code.'
		try:
			if A.__hash==A.__get_hash():return _C
			else:raise Exception('Error: Hashes do not match')
		except Exception:return _A
	def __setattr__(A,name,value):'Set an attributes value but only after verifying our hash.';A.verify_hash();super().__setattr__(name,value)
	def __delattr__(A,name):
		'Delete an attribute if its not our settings hash or if the code has been modified.';A.verify_hash()
		if name=='_Settings__hash':raise Exception('Error: Attempted deletion of race hash.')
		super().__delattr__(name)