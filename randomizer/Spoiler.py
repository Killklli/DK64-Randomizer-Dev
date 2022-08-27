'Spoiler class and functions.'
_F='locked'
_E='write'
_D='kong'
_C='container_map'
_B='Frantic Factory'
_A='Jungle Japes'
from email.policy import default
import json
from typing import OrderedDict
from randomizer.Enums.Events import Events
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.MoveTypes import MoveTypes
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.Lists.Item import ItemFromKong,ItemList,KongFromItem,NameFromKong
from randomizer.Lists.Location import LocationList
from randomizer.Lists.MapsAndExits import GetExitId,GetMapId,Maps
from randomizer.Lists.Minigame import BarrelMetaData,HelmMinigameLocations,MinigameRequirements
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
		'Convert spoiler to JSON.';AC='Unknown Shop';AB='Cranky';AA='vanilla';A9='Others';A8='Miscellaneous';A7='Klatrap Model';q='randomized';p=', ';o='King Kut Out Properties';n='DK Isles';b='Shops';a='End Game';Z='Creepy Castle';Y='Crystal Caves';X='Fungi Forest';W='Gloomy Galleon';V='Angry Aztec';S='Items';R='Requirements';Q='Colors and Models';J='Bosses';I='Kongs';F='Cosmetics';A.settings.verify_hash();B=OrderedDict();C=OrderedDict();C['Seed']=A.settings.seed_id;C['No Logic']=A.settings.no_logic;C['Shuffle Enemies']=A.settings.enemy_rando;C['Move Randomization type']=A.settings.move_rando;C['Loading Zones Shuffled']=A.settings.shuffle_loading_zones;C['Decoupled Loading Zones']=A.settings.decoupled_loading_zones;r=[]
		for AD in A.settings.starting_kong_list:r.append(AD.name.capitalize())
		if A.settings.randomize_blocker_required_amounts:C['Maximum B Locker']=A.settings.blocker_text
		if A.settings.randomize_cb_required_amounts:C['Maximum Troff N Scoff']=A.settings.troff_text
		C['Open Lobbies']=A.settings.open_lobbies;C['Open Levels']=A.settings.open_levels;C['Randomize Pickups']=A.settings.randomize_pickups;C['Randomize Patches']=A.settings.random_patches;C['Puzzle Randomization']=A.settings.puzzle_rando;C['Crown Door Open']=A.settings.crown_door_open;C['Coin Door Open']=A.settings.coin_door_open;C['Unlock Fairy Shockwave']=A.settings.unlock_fairy_shockwave;C['Random Medal Requirement']=A.settings.random_medal_requirement;C['Random Shop Prices']=A.settings.random_prices;C['Banana Port Randomization']=A.settings.bananaport_rando;C['Shuffle Shop Locations']=A.settings.shuffle_shops;C['Shuffle Kasplats']=A.settings.kasplat_rando_setting;C['Key 8 Required']=A.settings.krool_access;C['Number of Keys Required']=A.settings.krool_key_count;C['Fast Start']=A.settings.fast_start_beginning_of_game;C['Helm Setting']=A.settings.helm_setting;C['Quality of Life']=A.settings.quality_of_life;C['Tag Anywhere']=A.settings.enable_tag_anywhere;C['Fast GBs']=A.settings.fast_gbs;C['High Requirements']=A.settings.high_req;B['Settings']=C;B[F]={}
		if A.settings.colors!={}or A.settings.klaptrap_model_index:
			B[F][Q]={}
			for T in A.settings.colors:
				if T=='dk':B[F][Q]['DK Color']=A.settings.colors[T]
				else:B[F][Q][f"{T.capitalize()} Color"]=A.settings.colors[T]
			s={25:'Beaver',30:'Klobber',32:'Kaboom',33:'Green Klaptrap',34:'Purple Klaptrap',35:'Red Klaptrap',36:'Klaptrap Teeth',38:'Krash',39:'Troff',48:'N64 Logo',52:'Mech Fish',66:'Krossbones',71:'Rabbit',75:'Minecart Skeleton Head',81:'Tomato',98:'Ice Tomato',105:'Golden Banana',112:'Microbuffer',114:'Bell',150:'Missile (Car Race)',176:'Red Buoy',177:'Green Buoy',189:'Rareware Logo'}
			if A.settings.klaptrap_model_index in s:B[F][Q][A7]=s[A.settings.klaptrap_model_index]
			else:B[F][Q][A7]=f"Unknown Model {hex(A.settings.klaptrap_model_index)}"
		B[R]={};t={};u=[_A,V,_B,W,X,Y,Z,'Hideout Helm']
		for (c,d) in enumerate(A.settings.EntryGBs):t[u[c]]=d
		B[R]['B Locker GBs']=t;v={}
		for (c,d) in enumerate(A.settings.BossBananas):v[u[c]]=d
		B[R]['Troff N Scoff Bananas']=v;B[R][A8]={};B[I]={};B[I]['Starting Kong List']=r;B[I]['Japes Kong Puzzle Solver']=ItemList[ItemFromKong(A.settings.diddy_freeing_kong)].name;B[I]['Tiny Temple Puzzle Solver']=ItemList[ItemFromKong(A.settings.tiny_freeing_kong)].name;B[I]['Llama Temple Puzzle Solver']=ItemList[ItemFromKong(A.settings.lanky_freeing_kong)].name;B[I]['Factory Kong Puzzle Solver']=ItemList[ItemFromKong(A.settings.chunky_freeing_kong)].name
		if A.settings.coin_door_open in['need_both','need_rw']:B[R][A8]['Medal Requirement']=A.settings.medal_requirement
		B[a]={};B[a]['Keys Required for K Rool']=A.GetKroolKeysRequired(A.settings.krool_keys_required);w=[]
		for e in A.settings.krool_order:w.append(ItemList[ItemFromKong(e)].name.capitalize())
		B[a]['K Rool Phases']=w;AE=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];x=[]
		for AF in A.settings.helm_order:x.append(AE[AF].name.capitalize())
		B[a]['Helm Rooms']=x;B[S]={I:{},b:{},A9:{}};G=OrderedDict()
		if A.settings.random_prices!=AA:
			for (K,D) in A.settings.prices.items():
				if K==Items.ProgressiveSlam:G['Progressive Slam']=f"{D[0]}→{D[1]}"
				elif K==Items.ProgressiveAmmoBelt:G['Progressive Ammo Belt']=f"{D[0]}→{D[1]}"
				elif K==Items.ProgressiveInstrumentUpgrade:G['Progressive Instrument Upgrade']=f"{D[0]}→{D[1]}→{D[2]}"
				else:G[f"{ItemList[K].name}"]=D
		if A.settings.shuffle_items!='none':
			B['Playthrough']=A.playthrough;B['Way of the Hoard']=A.woth;AQ=OrderedDict()
			for (L,K) in A.location_data.items():
				if not LocationList[L].constant:
					M=ItemList[K].name;H=LocationList[L].name;f=A9
					if H in('Diddy Kong','Lanky Kong','Tiny Kong','Chunky Kong'):f=I
					elif AB in H or'Funky'in H or'Candy'in H:f=b
					if A.settings.random_prices!=AA:
						if M in G:M=f"{M} ({G[M]})"
					B[S][f][H]=M
		if len(B[S][b].keys())==0:
			y={}
			for D in G:y[f"{D} Cost"]=G[D]
			B[S][b]=y
		if A.settings.shuffle_loading_zones=='levels':
			N=OrderedDict();AG={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};AH={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle}
			for (AI,AJ) in AG.items():AK=AH[A.shuffled_exit_data[AI].reverse];N[AJ.name]=AK.name
			B['Shuffled Level Order']=N
		elif A.settings.shuffle_loading_zones!='none':
			N=OrderedDict();g={n:[n,'Japes Lobby','Aztec Lobby','Factory Lobby','Galleon Lobby','Fungi Lobby','Caves Lobby','Castle Lobby',"Snide's Room",'Training Grounds','Banana Fairy Isle',"DK's Treehouse"],_A:[_A],V:[V],_B:[_B],W:[W],X:[X],Y:[Y],Z:[Z]};h={'Other':{}}
			for E in g:h[E]={}
			for (exit,i) in A.shuffled_exit_data.items():
				O='Other'
				for E in g:
					for AL in g[E]:
						if i.spoilerName.find(AL)==0:O=E
				N[ShufflableExits[exit].name]=i.spoilerName;h[O][ShufflableExits[exit].name]=i.spoilerName
			B['Shuffled Exits']=N;B['Shuffled Exits (Sorted by destination)']=h
		B[J]={}
		if A.settings.boss_location_rando:
			z=OrderedDict();AM={'JapesBoss':'Army Dillo 1','AztecBoss':'Dogadon 1','FactoryBoss':'Mad Jack','GalleonBoss':'Pufftoss','FungiBoss':'Dogadon 2','CavesBoss':'Army Dillo 2','CastleBoss':'King Kut Out'}
			for P in range(7):z[''.join(map(lambda x:x if x.islower()else' '+x,Levels(P).name))]=AM[Maps(A.settings.boss_maps[P]).name]
			B[J]['Shuffled Boss Order']=z
		B[J][o]={}
		if A.settings.boss_kong_rando:
			A0=OrderedDict()
			for P in range(7):A0[''.join(map(lambda x:x if x.islower()else' '+x,Levels(P).name))]=Kongs(A.settings.boss_kongs[P]).name.capitalize()
			B[J]['Shuffled Boss Kongs']=A0;j=''
			for AN in A.settings.kutout_kongs:j=j+Kongs(AN).name.capitalize()+p
			B[J][o]['Shuffled Kutout Kong Order']=j.removesuffix(p)
		if A.settings.hard_bosses:
			A1=[]
			for e in A.settings.kko_phase_order:A1.append(f"Phase {e+1}")
			B[J][o]['Shuffled Kutout Phases']=p.join(A1)
		if A.settings.bonus_barrels in('random','selected'):
			k=OrderedDict()
			for (L,AO) in A.shuffled_barrel_data.items():
				if L in HelmMinigameLocations and A.settings.helm_barrels=='skip':continue
				if L not in HelmMinigameLocations and A.settings.bonus_barrels=='skip':continue
				k[LocationList[L].name]=MinigameRequirements[AO].name
			if len(k)>0:B['Shuffled Bonus Barrels']=k
		if A.settings.music_bgm==q:B[F]['Background Music']=A.music_bgm_data
		if A.settings.music_fanfares==q:B[F]['Fanfares']=A.music_fanfare_data
		if A.settings.music_events==q:B[F]['Event Themes']=A.music_event_data
		if A.settings.kasplat_rando:B['Shuffled Kasplats']=A.human_kasplats
		if A.settings.random_patches:B['Shuffled Dirt Patches']=A.human_patches
		if A.settings.bananaport_rando:B['Shuffled Bananaports']=A.human_warp_locations
		if len(A.hint_list)>0:B['Wrinkly Hints']=A.hint_list
		if A.settings.shuffle_shops:
			A2={}
			for E in A.shuffled_shop_locations:
				O='Unknown Level';A3={Levels.DKIsles:n,Levels.JungleJapes:_A,Levels.AngryAztec:V,Levels.FranticFactory:_B,Levels.GloomyGalleon:W,Levels.FungiForest:X,Levels.CrystalCaves:Y,Levels.CreepyCastle:Z};U={Regions.CrankyGeneric:AB,Regions.CandyGeneric:'Candy',Regions.FunkyGeneric:'Funky',Regions.Snide:'Snide'}
				if E in A3:O=A3[E]
				for l in A.shuffled_shop_locations[E]:
					H=AC;A4=AC;A5=A.shuffled_shop_locations[E][l]
					if l in U:H=U[l]
					if A5 in U:A4=U[A5]
					A2[f"{O} - {H}"]=A4
			B['Shop Locations']=A2
		for m in (S,J):
			A6=True
			for AP in B[m]:
				if B[m][AP]!={}:A6=False
			if A6:del B[m]
		return json.dumps(B,indent=4)
	def UpdateKasplats(A,kasplat_map):
		'Update kasplat data.';C='kasplat_swaps'
		for (G,D) in kasplat_map.items():
			B=LocationList[G];E=B.map;H=B.kong;A.human_kasplats[B.name]=NameFromKong(D);map=None
			for F in A.enemy_replacements:
				if F[_C]==E:map=F;break
			if map is None:map={_C:E};A.enemy_replacements.append(map)
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
					if C not in B:B[C]={_C:C,H:[]}
					A={};A['vanilla_map']=GetMapId(G.regionId);A['vanilla_exit']=GetExitId(G);A['new_map']=GetMapId(E.regionId);A['new_exit']=GetExitId(E);B[C][H].append(A)
				except Exception as I:print(I)
		for (F,J) in B.items():D.shuffled_exit_instructions.append(J)
	def UpdateLocations(B,locations):
		'Update location list for what was produced by the fill.';B.location_data={};B.shuffled_kong_placement={};J={_D:B.settings.starting_kong,_E:337};K={_F:J};B.shuffled_kong_placement['TrainingGrounds']=K;L=[A for A in[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]if A not in B.settings.kong_locations]
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
		'Write kong placement information for the given kong cage location.';F=locationId;B=_A;C=A.settings.diddy_freeing_kong;D=338;E=339
		if F==Locations.LankyKong:B='Llama Temple';C=A.settings.lanky_freeing_kong;D=340;E=341
		elif F==Locations.TinyKong:B='Tiny Temple';C=A.settings.tiny_freeing_kong;D=342;E=343
		elif F==Locations.ChunkyKong:B=_B;C=A.settings.chunky_freeing_kong;D=344;E=345
		G={};G[_D]=KongFromItem(item);G[_E]=D;H={_D:C,_E:E};I={_F:G,'puzzle':H};A.shuffled_kong_placement[B]=I
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