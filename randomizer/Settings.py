'Settings class and functions.'
_F='level_order'
_E='all'
_D='none'
_C=True
_B=False
_A=None
import hashlib,inspect,json,random,sys
from randomizer.ShuffleBosses import ShuffleBosses,ShuffleBossKongs,ShuffleKutoutKongs
from randomizer.Enums.Events import Events
from randomizer.Enums.Kongs import Kongs,GetKongs
from randomizer.Prices import RandomizePrices,VanillaPrices
class Settings:
	'Class used to store settings for seed generation.'
	def __init__(A,form_data):
		'Init all the settings using the form data to set the flags.\n\n        Args:\n            form_data (dict): Post data from the html form.\n        ';A.__hash=A.__get_hash();A.public_hash=A.__get_hash();A.algorithm='forward';A.generate_main();A.generate_progression();A.generate_misc()
		for (B,C) in form_data.items():setattr(A,B,C)
		A.seed_id=str(A.seed);A.seed=str(A.seed)+A.__hash;A.set_seed();A.update_progression_totals();A.EntryGBs=[A.blocker_0,A.blocker_1,A.blocker_2,A.blocker_3,A.blocker_4,A.blocker_5,A.blocker_6,A.blocker_7];A.BossBananas=[A.troff_0,A.troff_1,A.troff_2,A.troff_3,A.troff_4,A.troff_5,A.troff_6];A.seed_hash=[random.randint(0,9)for A in range(5)];A.krool_keys_required=[];A.training_barrels='startwith';A.shuffle_items=_D;A.progressive_upgrades=_B;A.prices=VanillaPrices.copy();A.resolve_settings()
	def update_progression_totals(A):
		"Update the troff and blocker totals if we're randomly setting them.";A.troff_min=0;A.troff_max=260
		if A.level_randomization==_F:A.troff_min=100;A.troff_max=300
		A.troff_weight_0=0.7;A.troff_weight_1=0.8;A.troff_weight_2=0.9;A.troff_weight_3=1.0;A.troff_weight_4=1.1;A.troff_weight_5=1.2;A.troff_weight_6=1.3
		if A.randomize_cb_required_amounts:D=random.sample(range(A.troff_min,A.troff_max),7);C=D;A.troff_0=round(C[0]*A.troff_weight_0);A.troff_1=round(C[1]*A.troff_weight_1);A.troff_2=round(C[2]*A.troff_weight_2);A.troff_3=round(C[3]*A.troff_weight_3);A.troff_4=round(C[4]*A.troff_weight_4);A.troff_5=round(C[5]*A.troff_weight_5);A.troff_6=round(C[6]*A.troff_weight_6)
		if A.randomize_blocker_required_amounts:
			D=random.sample(range(0,50),7);B=D;B.append(1)
			if A.shuffle_loading_zones==_E:random.shuffle(B)
			else:B.sort()
			A.blocker_0=B[0];A.blocker_1=B[1];A.blocker_2=B[2];A.blocker_3=B[3];A.blocker_4=B[4];A.blocker_5=B[5];A.blocker_6=B[6];A.blocker_7=B[7]
	def generate_main(A):'Set Default items on main page.';A.seed=_A;A.download_patch_file=_A;A.bonus_barrel_rando=_A;A.loading_zone_coupled=_A;A.shop_location_rando=_A;A.random_prices=_A;A.boss_location_rando=_A;A.boss_kong_rando=_A;A.kasplat_rando=_A
	def set_seed(A):'Forcibly re-set the random seed to the seed set in the config.';random.seed(A.seed)
	def generate_progression(A):'Set default items on progression page.';A.blocker_0=_A;A.blocker_1=_A;A.blocker_2=_A;A.blocker_3=_A;A.blocker_4=_A;A.blocker_5=_A;A.blocker_6=_A;A.blocker_7=_A;A.troff_0=_A;A.troff_1=_A;A.troff_2=_A;A.troff_3=_A;A.troff_4=_A;A.troff_5=_A;A.troff_6=_A;A.troff_min=_A;A.troff_max=_A
	def generate_misc(A):'Set default items on misc page.';A.unlock_all_moves=_A;A.unlock_all_kongs=_A;A.crown_door_open=_A;A.coin_door_open=_A;A.unlock_fairy_shockwave=_A;A.krool_phase_count=5;A.krool_key_count=8;A.bonus_barrels='normal';A.hard_shooting=_B;A.shuffle_loading_zones=_D;A.decoupled_loading_zones=_B;A.music_bgm=_A;A.music_fanfares=_A;A.music_events=_A;A.generate_spoilerlog=_A;A.fast_start_beginning_of_game=_A;A.helm_setting=_A;A.quality_of_life=_A;A.enable_tag_anywhere=_A;A.krool_phase_order_rando=_A;A.krool_access=_A;A.open_lobbies=_A;A.random_medal_requirement=_C;A.bananaport_rando=_B;A.shop_indicator=_B;A.randomize_cb_required_amounts=_B;A.randomize_blocker_required_amounts=_B;A.perma_death=_B;A.disable_tag_barrels=_B;A.level_randomization=_D;A.kong_rando=_B;A.kongs_for_progression=_B
	def resolve_settings(A):
		'Resolve settings which are not directly set through the UI.';L='levels';K='random';J='random_helm';F='vanilla';G=GetKongs()
		if A.random_prices!=F:A.prices=RandomizePrices(A.random_prices)
		A.krool_donkey=_B;A.krool_diddy=_B;A.krool_lanky=_B;A.krool_tiny=_B;A.krool_chunky=_C;C=[A for A in G if A!=Kongs.chunky]
		if A.krool_phase_order_rando:random.shuffle(C)
		if A.krool_phase_count<5:C=random.sample(C,A.krool_phase_count-1)
		B=[]
		for D in C:
			if D==Kongs.donkey:A.krool_donkey=_C;B.append(Kongs.donkey)
			if D==Kongs.diddy:A.krool_diddy=_C;B.append(Kongs.diddy)
			if D==Kongs.lanky:A.krool_lanky=_C;B.append(Kongs.lanky)
			if D==Kongs.tiny:A.krool_tiny=_C;B.append(Kongs.tiny)
		B.append(Kongs.chunky);A.krool_order=B;H=[Events.JapesKeyTurnedIn,Events.AztecKeyTurnedIn,Events.FactoryKeyTurnedIn,Events.GalleonKeyTurnedIn,Events.ForestKeyTurnedIn,Events.CavesKeyTurnedIn,Events.CastleKeyTurnedIn,Events.HelmKeyTurnedIn];E=H.copy();I=A.krool_key_count
		if A.krool_access==J:A.krool_keys_required.append(Events.HelmKeyTurnedIn);E.remove(Events.HelmKeyTurnedIn);I-=1
		if A.krool_access==F:A.krool_keys_required.extend([Events.FactoryKeyTurnedIn,Events.HelmKeyTurnedIn])
		elif A.krool_access==_E:A.krool_keys_required.extend(H)
		elif A.krool_access==K or A.krool_access==J:
			random.shuffle(E)
			for M in range(I):A.krool_keys_required.append(E[M])
		if A.random_medal_requirement:A.BananaMedalsRequired=round(random.normalvariate(10,1.5))
		else:A.BananaMedalsRequired=15
		A.boss_maps=ShuffleBosses(A.boss_location_rando);A.boss_kongs=ShuffleBossKongs(A.boss_maps,A.boss_kong_rando);A.kutout_kongs=ShuffleKutoutKongs(A.boss_maps,A.boss_kongs,A.boss_kong_rando)
		if A.bonus_barrel_rando:A.bonus_barrels=K
		if A.level_randomization==_F:A.shuffle_loading_zones=L
		elif A.level_randomization=='loadingzone':A.shuffle_loading_zones=_E
		elif A.level_randomization=='loadingzonesdecoupled':A.shuffle_loading_zones=_E;A.decoupled_loading_zones=_C
		elif A.level_randomization==F:A.shuffle_loading_zones=_D
		if A.kong_rando:
			A.starting_kong=random.choice(G)
			if A.shuffle_loading_zones==L:A.kongs_for_progression=_C
			A.diddy_freeing_kong=Kongs.any;A.lanky_freeing_kong=Kongs.any;A.tiny_freeing_kong=Kongs.any;A.chunky_freeing_kong=Kongs.any
		else:A.starting_kong=Kongs.donkey;A.diddy_freeing_kong=Kongs.donkey;A.lanky_freeing_kong=Kongs.donkey;A.tiny_freeing_kong=Kongs.diddy;A.chunky_freeing_kong=Kongs.lanky
		if A.shop_location_rando:A.shuffle_items='moves'
	def __repr__(A):'Return printable version of the object as json.\n\n        Returns:\n            str: Json string of the dict.\n        ';return json.dumps(A.__dict__)
	def __get_hash(D):
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
		except Exception:return _B
	def __setattr__(A,name,value):'Set an attributes value but only after verifying our hash.';A.verify_hash();super().__setattr__(name,value)
	def __delattr__(A,name):
		'Delete an attribute if its not our settings hash or if the code has been modified.';A.verify_hash()
		if name=='_Settings__hash':raise Exception('Error: Attempted deletion of race hash.')
		super().__delattr__(name)