'Spoiler class and functions.'
_D='locked'
_C='write'
_B='kong'
_A='container_map'
import json
from typing import OrderedDict
from randomizer import Logic
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MoveTypes import MoveTypes
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Lists.Item import ItemFromKong,NameFromKong,KongFromItem,ItemList
from randomizer.Lists.Location import LocationList
from randomizer.Lists.Minigame import BarrelMetaData,HelmMinigameLocations,MinigameRequirements
from randomizer.Lists.MapsAndExits import GetExitId,GetMapId,Maps
from randomizer.Settings import Settings
from randomizer.ShuffleExits import ShufflableExits
class Spoiler:
	'Class which contains all spoiler data passed into and out of randomizer.'
	def __init__(A,settings):
		'Initialize spoiler just with settings.';A.settings=settings;A.playthrough={};A.woth={};A.shuffled_barrel_data={};A.shuffled_exit_data={};A.shuffled_exit_instructions=[];A.music_bgm_data={};A.music_fanfare_data={};A.music_event_data={};A.location_data={};A.enemy_replacements=[];A.move_data=[]
		for D in range(3):
			B=[]
			for E in range(5):
				C=[]
				for F in range(7):C.append(-1)
				B.append(C)
			A.move_data.append(B)
		A.jetpac_medals_required=A.settings.BananaMedalsRequired;A.hint_list={}
	def toJson(A):
		'Convert spoiler to JSON.';R='skip';Q='none';L='randomized';A.settings.verify_hash();C=OrderedDict();B=OrderedDict();B['seed']=A.settings.seed_id;B['algorithm']=A.settings.algorithm;B['move_rando']=A.settings.move_rando;B['shuffle_loading_zones']=A.settings.shuffle_loading_zones;B['decoupled_loading_zones']=A.settings.decoupled_loading_zones;B['starting_kongs_count']=A.settings.starting_kongs_count;M=[]
		for S in A.settings.starting_kong_list:M.append(S.name.capitalize())
		B['starting_kong_list']=M;B['diddy_freeing_kong']=ItemList[ItemFromKong(A.settings.diddy_freeing_kong)].name;B['tiny_freeing_kong']=ItemList[ItemFromKong(A.settings.tiny_freeing_kong)].name;B['lanky_freeing_kong']=ItemList[ItemFromKong(A.settings.lanky_freeing_kong)].name;B['chunky_freeing_kong']=ItemList[ItemFromKong(A.settings.chunky_freeing_kong)].name;B['open_lobbies']=A.settings.open_lobbies;B['open_levels']=A.settings.open_levels;B['randomize_pickups']=A.settings.randomize_pickups;B['random_patches']=A.settings.random_patches;B['puzzle_rando']=A.settings.puzzle_rando;B['crown_door_open']=A.settings.crown_door_open;B['coin_door_open']=A.settings.coin_door_open;B['unlock_fairy_shockwave']=A.settings.unlock_fairy_shockwave;B['random_medal_requirement']=A.settings.random_medal_requirement
		if A.settings.random_medal_requirement:B['banana_medals_required']=A.settings.BananaMedalsRequired
		B['random_prices']=A.settings.random_prices;B['bananaport_rando']=A.settings.bananaport_rando;B['krool_phases']=A.settings.krool_order;B['krool_access']=A.settings.krool_access;B['krool_keys_required']=A.GetKroolKeysRequired(A.settings.krool_keys_required);B['music_bgm']=A.settings.music_bgm;B['music_fanfares']=A.settings.music_fanfares;B['music_events']=A.settings.music_events;B['fast_start_beginning_of_game']=A.settings.fast_start_beginning_of_game;B['helm_setting']=A.settings.helm_setting;B['quality_of_life']=A.settings.quality_of_life;B['enable_tag_anywhere']=A.settings.enable_tag_anywhere;B['blocker_golden_bananas']=A.settings.EntryGBs;B['troff_n_scoff_bananas']=A.settings.BossBananas;C['Settings']=B
		if A.settings.shuffle_items!=Q:
			C['Playthrough']=A.playthrough;C['Way_of_the_Hoard']=A.woth;N=OrderedDict()
			for (F,G) in A.location_data.items():
				if not LocationList[F].constant:N[LocationList[F].name]=ItemList[G].name
			C['Locations']=N
		if A.settings.random_prices!='vanilla':
			D=OrderedDict()
			for (G,E) in A.settings.prices.items():
				if G==Items.ProgressiveSlam:D['Super Simian Slam']=E[0];D['Super Duper Simian Slam']=E[1]
				elif G==Items.ProgressiveAmmoBelt:D['Ammo Belt 1']=E[0];D['Ammo Belt 2']=E[1]
				elif G==Items.ProgressiveInstrumentUpgrade:D['Music Upgrade 1']=E[0];D['Third Melon']=E[1];D['Music Upgrade 2']=E[2]
				else:D[ItemList[G].name]=E
			C['Prices']=D
		if A.settings.shuffle_loading_zones=='levels':
			H=OrderedDict();T={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};U={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle}
			for (V,W) in T.items():X=U[A.shuffled_exit_data[V].reverse];H[W.name]=X.name
			C['Shuffled Level Order']=H
		elif A.settings.shuffle_loading_zones!=Q:
			H=OrderedDict()
			for (exit,Y) in A.shuffled_exit_data.items():H[ShufflableExits[exit].name]=Y.spoilerName
			C['Shuffled Exits']=H
		if A.settings.boss_location_rando:
			O=OrderedDict()
			for I in range(7):O[Levels(I).name]=Maps(A.settings.boss_maps[I]).name
			C['Shuffled Boss Order']=O
		if A.settings.boss_kong_rando:
			P=OrderedDict()
			for I in range(7):P[Levels(I).name]=Kongs(A.settings.boss_kongs[I]).name
			C['Shuffled Boss Kongs']=P;J=''
			for Z in A.settings.kutout_kongs:J=J+Kongs(Z).name+', '
			C['Shuffled Kutout Kong Order']=J.removesuffix(', ')
		if A.settings.bonus_barrels in('random','all_beaver_bother'):
			K=OrderedDict()
			for (F,a) in A.shuffled_barrel_data.items():
				if F in HelmMinigameLocations and A.settings.helm_barrels==R:continue
				if F not in HelmMinigameLocations and A.settings.bonus_barrels==R:continue
				K[LocationList[F].name]=MinigameRequirements[a].name
			if len(K)>0:C['Shuffled Bonus Barrels']=K
		if A.settings.music_bgm==L:C['Shuffled Music (BGM)']=A.music_bgm_data
		if A.settings.music_fanfares==L:C['Shuffled Music Fanfares']=A.music_fanfare_data
		if A.settings.music_events==L:C['Shuffled Music Events']=A.music_event_data
		if A.settings.kasplat_rando:C['Shuffled Kasplats']=A.human_kasplats
		if len(A.hint_list)>0:C['Wrinkly Hints']=A.hint_list
		return json.dumps(C,indent=4)
	def UpdateKasplats(A,kasplat_map):
		'Update kasplat data.';C='kasplat_swaps'
		for (G,D) in kasplat_map.items():
			B=LocationList[G];E=B.map;H=B.kong;A.human_kasplats[B.name]=NameFromKong(D);map=None
			for F in A.enemy_replacements:
				if F[_A]==E:map=F;break
			if map is None:map={_A:E};A.enemy_replacements.append(map)
			if C not in map:map[C]=[]
			I={'vanilla_location':H,'replace_with':D};map[C].append(I)
	def UpdateBarrels(A):
		'Update list of shuffled barrel minigames.';A.shuffled_barrel_data={}
		for (B,C) in [(A,B.minigame)for(A,B)in BarrelMetaData.items()]:A.shuffled_barrel_data[B]=C
	def UpdateExits(D):
		'Update list of shuffled exits.';H='zones';D.shuffled_exit_data={};B={}
		for (F,exit) in ShufflableExits.items():
			if exit.shuffled:
				try:
					G=exit.back;E=ShufflableExits[exit.shuffledId].back;D.shuffled_exit_data[F]=E;C=GetMapId(exit.region)
					if C not in B:B[C]={_A:C,H:[]}
					A={};A['vanilla_map']=GetMapId(G.regionId);A['vanilla_exit']=GetExitId(G);A['new_map']=GetMapId(E.regionId);A['new_exit']=GetExitId(E);B[C][H].append(A)
				except Exception as I:print(I)
		for (F,J) in B.items():D.shuffled_exit_instructions.append(J)
	def UpdateLocations(B,locations):
		'Update location list for what was produced by the fill.';B.location_data={};B.shuffled_kong_placement={};J={_B:B.settings.starting_kong,_C:321};K={_D:J};B.shuffled_kong_placement['TrainingGrounds']=K;L=[A for A in[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]if A not in B.settings.kong_locations]
		for M in L:B.WriteKongPlacement(M,Items.NoItem)
		for (id,A) in locations.items():
			if A.item is not None and A.item is not Items.NoItem and not A.constant:
				B.location_data[id]=A.item
				if A.type==Types.Shop:
					D=0
					if A.movetype in[MoveTypes.Guns,MoveTypes.AmmoBelt]:D=1
					elif A.movetype==MoveTypes.Instruments:D=2
					H=[A.kong]
					if A.kong==Kongs.any:H=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
					I=A.level;C=ItemList[A.item].movetype;E=ItemList[A.item].index-1;F=ItemList[A.item].kong
					for G in H:
						print(f"Shop {D}, Kong {G}, Level {I} | Move: {C} lvl {E} for kong {F}")
						if C==1 or C==3 or C==2 and E>0 or C==4 and E>0:F=G
						N=C<<5|E<<3|F;B.move_data[D][G][I]=N
				elif A.type==Types.Kong:B.WriteKongPlacement(id,A.item)
	def WriteKongPlacement(A,locationId,item):
		'Write kong placement information for the given kong cage location.';F=locationId;B='Jungle Japes';C=A.settings.diddy_freeing_kong;D=322;E=323
		if F==Locations.LankyKong:B='Llama Temple';C=A.settings.lanky_freeing_kong;D=324;E=325
		elif F==Locations.TinyKong:B='Tiny Temple';C=A.settings.tiny_freeing_kong;D=326;E=327
		elif F==Locations.ChunkyKong:B='Frantic Factory';C=A.settings.chunky_freeing_kong;D=328;E=329
		G={};G[_B]=KongFromItem(item);G[_C]=D;H={_B:C,_C:E};I={_D:G,'puzzle':H};A.shuffled_kong_placement[B]=I
	def UpdatePlaythrough(B,locations,playthroughLocations):
		'Write playthrough as a list of dicts of location/item pairs.';B.playthrough={};C=0
		for D in playthroughLocations:
			A={};A['Available GBs']=D.availableGBs;E=list(map(lambda l:locations[l],D.locations));E.sort(key=lambda l:l.type==Types.Banana)
			for F in E:A[F.name]=ItemList[F.item].name
			B.playthrough[C]=A;C+=1
	def UpdateWoth(A,locations,wothLocations):
		'Write woth locations as a dict of location/item pairs.';A.woth={}
		for C in wothLocations:B=locations[C];A.woth[B.name]=ItemList[B.item].name
	@staticmethod
	def GetKroolKeysRequired(keyEvents):
		'Get key names from required key events to print in the spoiler.';B=keyEvents;A=[]
		if Events.JapesKeyTurnedIn in B:A.append('Jungle Japes Key')
		if Events.AztecKeyTurnedIn in B:A.append('Angry Aztec Key')
		if Events.FactoryKeyTurnedIn in B:A.append('Frantic Factory Key')
		if Events.GalleonKeyTurnedIn in B:A.append('Gloomy Galleon Key')
		if Events.ForestKeyTurnedIn in B:A.append('Fungi Forest Key')
		if Events.CavesKeyTurnedIn in B:A.append('Crystal Caves Key')
		if Events.CastleKeyTurnedIn in B:A.append('Creepy Castle Key')
		if Events.HelmKeyTurnedIn in B:A.append('Hideout Helm Key')
		return A