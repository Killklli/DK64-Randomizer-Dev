'Spoiler class and functions.'
_F='locked'
_E='Frantic Factory'
_D='Jungle Japes'
_C='write'
_B='kong'
_A='container_map'
import json
from typing import OrderedDict
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MoveTypes import MoveTypes
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Regions import Regions
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
				for F in range(8):C.append(-1)
				B.append(C)
			A.move_data.append(B)
		A.hint_list={}
	def toJson(A):
		'Convert spoiler to JSON.';e='Unknown Shop';d='skip';c='none';P='randomized';O=', ';A.settings.verify_hash();C=OrderedDict();B=OrderedDict();B['Seed']=A.settings.seed_id;B['No Logic']=A.settings.no_logic;B['Shuffle Enemies']=A.settings.enemy_rando;B['Move Randomization type']=A.settings.move_rando;B['Loading Zones Shuffled']=A.settings.shuffle_loading_zones;B['Decoupled Loading Zones']=A.settings.decoupled_loading_zones;Q=[]
		for f in A.settings.starting_kong_list:Q.append(f.name.capitalize())
		B['Starting Kong List']=Q;B['Colors']=A.settings.colors;B['B Locker GBs']=A.settings.EntryGBs
		if A.settings.randomize_blocker_required_amounts:B['Maximum B Locker']=A.settings.blocker_text
		if A.settings.randomize_cb_required_amounts:B['Maximum Troff N Scoff']=A.settings.troff_text
		B['Troff N Scoff Bananas']=A.settings.BossBananas;B['Diddy Freeing Kong']=ItemList[ItemFromKong(A.settings.diddy_freeing_kong)].name;B['Tiny Freeing Kong']=ItemList[ItemFromKong(A.settings.tiny_freeing_kong)].name;B['Lanky Freeing Kong']=ItemList[ItemFromKong(A.settings.lanky_freeing_kong)].name;B['Chunky Freeing Kong']=ItemList[ItemFromKong(A.settings.chunky_freeing_kong)].name;B['Open Lobbies']=A.settings.open_lobbies;B['Open Levels']=A.settings.open_levels;B['Randomize Pickups']=A.settings.randomize_pickups;B['Randomize Patches']=A.settings.random_patches;B['Puzzle Randomization']=A.settings.puzzle_rando;B['Crown Door Open']=A.settings.crown_door_open;B['Coin Door Open']=A.settings.coin_door_open;B['Unlock Fairy Shockwave']=A.settings.unlock_fairy_shockwave;B['Random Medal Requirement']=A.settings.random_medal_requirement
		if A.settings.coin_door_open in['need_both','need_rw']:B['Medal Requirement']=A.settings.medal_requirement
		B['Random Shop Prices']=A.settings.random_prices;B['Banana Port Randomization']=A.settings.bananaport_rando;B['Shuffle Shop Locations']=A.settings.shuffle_shops;B['Shuffle Kasplats']=A.settings.kasplat_rando_setting;B['K Rool Phases']=A.settings.krool_order;B['Key 8 Required']=A.settings.krool_access;B['Keys Required for K Rool']=A.GetKroolKeysRequired(A.settings.krool_keys_required);B['Number of Keys Required']=A.settings.krool_key_count;B['Fast Start']=A.settings.fast_start_beginning_of_game;B['Helm Setting']=A.settings.helm_setting;B['Quality of Life']=A.settings.quality_of_life;B['Tag Anywhere']=A.settings.enable_tag_anywhere;B['Fast GBs']=A.settings.fast_gbs;B['High Requirements']=A.settings.high_req;C['Settings']=B;g=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];R=[]
		for h in A.settings.helm_order:R.append(g[h].name)
		C['Helm Rooms']=R
		if A.settings.shuffle_items!=c:
			C['Playthrough']=A.playthrough;C['Way_of_the_Hoard']=A.woth;S=OrderedDict()
			for (F,G) in A.location_data.items():
				if not LocationList[F].constant:S[LocationList[F].name]=ItemList[G].name
			C['Locations']=S
		if A.settings.random_prices!='vanilla':
			D=OrderedDict()
			for (G,E) in A.settings.prices.items():
				if G==Items.ProgressiveSlam:D['Super Simian Slam']=E[0];D['Super Duper Simian Slam']=E[1]
				elif G==Items.ProgressiveAmmoBelt:D['Ammo Belt 1']=E[0];D['Ammo Belt 2']=E[1]
				elif G==Items.ProgressiveInstrumentUpgrade:D['Music Upgrade 1']=E[0];D['Third Melon']=E[1];D['Music Upgrade 2']=E[2]
				else:D[ItemList[G].name]=E
			C['Prices']=D
		if A.settings.shuffle_loading_zones=='levels':
			H=OrderedDict();i={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};j={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle}
			for (k,l) in i.items():m=j[A.shuffled_exit_data[k].reverse];H[l.name]=m.name
			C['Shuffled Level Order']=H
		elif A.settings.shuffle_loading_zones!=c:
			H=OrderedDict()
			for (exit,n) in A.shuffled_exit_data.items():H[ShufflableExits[exit].name]=n.spoilerName
			C['Shuffled Exits']=H
		if A.settings.boss_location_rando:
			T=OrderedDict()
			for I in range(7):T[Levels(I).name]=Maps(A.settings.boss_maps[I]).name
			C['Shuffled Boss Order']=T
		if A.settings.boss_kong_rando:
			U=OrderedDict()
			for I in range(7):U[Levels(I).name]=Kongs(A.settings.boss_kongs[I]).name
			C['Shuffled Boss Kongs']=U;L=''
			for o in A.settings.kutout_kongs:L=L+Kongs(o).name+O
			C['Shuffled Kutout Kong Order']=L.removesuffix(O)
		if A.settings.hard_bosses:
			V=[]
			for p in A.settings.kko_phase_order:V.append(f"Phase {p+1}")
			C['Shuffled Kutout Phases']=O.join(V)
		if A.settings.bonus_barrels in('random','all_beaver_bother'):
			M=OrderedDict()
			for (F,q) in A.shuffled_barrel_data.items():
				if F in HelmMinigameLocations and A.settings.helm_barrels==d:continue
				if F not in HelmMinigameLocations and A.settings.bonus_barrels==d:continue
				M[LocationList[F].name]=MinigameRequirements[q].name
			if len(M)>0:C['Shuffled Bonus Barrels']=M
		if A.settings.music_bgm==P:C['Shuffled Music (BGM)']=A.music_bgm_data
		if A.settings.music_fanfares==P:C['Shuffled Music Fanfares']=A.music_fanfare_data
		if A.settings.music_events==P:C['Shuffled Music Events']=A.music_event_data
		if A.settings.kasplat_rando:C['Shuffled Kasplats']=A.human_kasplats
		if A.settings.random_patches:C['Shuffled Dirt Patches']=A.human_patches
		if A.settings.bananaport_rando:C['Shuffled Bananaports']=A.human_warp_locations
		if len(A.hint_list)>0:C['Wrinkly Hints']=A.hint_list
		if A.settings.shuffle_shops:
			W={}
			for J in A.shuffled_shop_locations:
				X='Unknown Level';Y={Levels.DKIsles:'DK Isles',Levels.JungleJapes:_D,Levels.AngryAztec:'Angry Aztec',Levels.FranticFactory:_E,Levels.GloomyGalleon:'Gloomy Galleon',Levels.FungiForest:'Fungi Forest',Levels.CrystalCaves:'Crystal Caves',Levels.CreepyCastle:'Creepy Castle'};K={Regions.CrankyGeneric:'Cranky',Regions.CandyGeneric:'Candy',Regions.FunkyGeneric:'Funky',Regions.Snide:'Snide'}
				if J in Y:X=Y[J]
				for N in A.shuffled_shop_locations[J]:
					Z=e;a=e;b=A.shuffled_shop_locations[J][N]
					if N in K:Z=K[N]
					if b in K:a=K[b]
					W[f"{X} - {Z}"]=a
			C['Shop Locations']=W
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
		'Update location list for what was produced by the fill.';B.location_data={};B.shuffled_kong_placement={};J={_B:B.settings.starting_kong,_C:337};K={_F:J};B.shuffled_kong_placement['TrainingGrounds']=K;L=[A for A in[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]if A not in B.settings.kong_locations]
		for M in L:B.WriteKongPlacement(M,Items.NoItem)
		for (id,A) in locations.items():
			if A.item is not None and A.item is not Items.NoItem and not A.constant:
				B.location_data[id]=A.item
				if A.type==Types.Shop:
					D=0
					if A.movetype in[MoveTypes.Guns,MoveTypes.AmmoBelt]:D=1
					elif A.movetype==MoveTypes.Instruments:D=2
					G=[A.kong]
					if A.kong==Kongs.any:G=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
					E=A.level
					if E==8:E=7
					C=ItemList[A.item].movetype;F=ItemList[A.item].index-1;H=ItemList[A.item].kong
					for I in G:
						if C==1 or C==3 or C==2 and F>0 or C==4 and F>0:H=I
						N=C<<5|F<<3|H;B.move_data[D][I][E]=N
				elif A.type==Types.Kong:B.WriteKongPlacement(id,A.item)
	def WriteKongPlacement(A,locationId,item):
		'Write kong placement information for the given kong cage location.';F=locationId;B=_D;C=A.settings.diddy_freeing_kong;D=338;E=339
		if F==Locations.LankyKong:B='Llama Temple';C=A.settings.lanky_freeing_kong;D=340;E=341
		elif F==Locations.TinyKong:B='Tiny Temple';C=A.settings.tiny_freeing_kong;D=342;E=343
		elif F==Locations.ChunkyKong:B=_E;C=A.settings.chunky_freeing_kong;D=344;E=345
		G={};G[_B]=KongFromItem(item);G[_C]=D;H={_B:C,_C:E};I={_F:G,'puzzle':H};A.shuffled_kong_placement[B]=I
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