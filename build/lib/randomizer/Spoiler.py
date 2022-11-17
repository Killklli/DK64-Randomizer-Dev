'Spoiler class and functions.'
_L='locked'
_K='normal'
_J='write'
_I='container_map'
_H='kong'
_G='vanilla'
_F='Frantic Factory'
_E='Jungle Japes'
_D='price'
_C=None
_B='flag'
_A='move_type'
from email.policy import default
import json
from typing import OrderedDict
import randomizer.ItemPool as ItemPool
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
from randomizer.Prices import ProgressiveMoves
from randomizer.Settings import Settings
from randomizer.ShuffleExits import ShufflableExits
class Spoiler:
	'Class which contains all spoiler data passed into and out of randomizer.'
	def __init__(A,settings):
		'Initialize spoiler just with settings.';A.settings=settings;A.playthrough={};A.woth={};A.woth_locations={};A.woth_paths={};A.shuffled_barrel_data={};A.shuffled_exit_data={};A.shuffled_exit_instructions=[];A.music_bgm_data={};A.music_fanfare_data={};A.music_event_data={};A.location_data={};A.enemy_replacements=[];A.debug_human_item_assignment=_C;A.move_data=[]
		for C in range(3):
			B=[]
			if C==0:
				for G in range(3):
					D=[]
					for H in range(5):
						E=[]
						for I in range(8):E.append({_A:_C})
						D.append(E)
					B.append(D)
			elif C==1:
				if A.settings.training_barrels==_K:
					for F in ['dive','orange','barrel','vine']:B.append({_A:_B,_B:F,_D:0})
			elif C==2:
				if A.settings.shockwave_status==_G:B.append({_A:_B,_B:'camera_shockwave',_D:0})
				else:B.append({_A:_C})
			A.move_data.append(B)
		A.hint_list={}
	def createJson(A):
		'Convert spoiler to JSON and save it.';AL='Unknown Shop';AK='Castle';AJ='Galleon';AI='Factory';AH='Special';AG='Miscellaneous';AF='Klaptrap Model';t='Colored Banana Locations';s='randomized';r=', ';q='King Kut Out Properties';p='Hideout Helm';c='End Game';X='DK Isles';W='Items';V='Requirements';U='Colors and Models';Q=' ';P='Creepy Castle';O='Crystal Caves';N='Fungi Forest';M='Gloomy Galleon';L='Angry Aztec';I='Bosses';H='Kongs';G='';F='Cosmetics';A.settings.verify_hash();B=OrderedDict();C=OrderedDict();C['Seed']=A.settings.seed_id;C['No Logic']=A.settings.no_logic;C['Shuffle Enemies']=A.settings.enemy_rando;C['Move Randomization type']=A.settings.move_rando;C['Loading Zones Shuffled']=A.settings.shuffle_loading_zones;C['Decoupled Loading Zones']=A.settings.decoupled_loading_zones;u=[]
		for AM in A.settings.starting_kong_list:u.append(AM.name.capitalize())
		if A.settings.randomize_blocker_required_amounts:C['Maximum B Locker']=A.settings.blocker_text
		if A.settings.randomize_cb_required_amounts:C['Maximum Troff N Scoff']=A.settings.troff_text
		C['Open Lobbies']=A.settings.open_lobbies;C['Open Levels']=A.settings.open_levels;C['Randomize Pickups']=A.settings.randomize_pickups;C['Randomize Patches']=A.settings.random_patches;C['Randomize CB Locations']=A.settings.cb_rando;C['Puzzle Randomization']=A.settings.puzzle_rando;C['Crown Door Open']=A.settings.crown_door_open;C['Coin Door Open']=A.settings.coin_door_open;C['Shockwave Shuffle']=A.settings.shockwave_status;C['Random Jetpac Medal Requirement']=A.settings.random_medal_requirement;C['Bananas Required for Medal']=A.settings.medal_cb_req;C['Fairies Required for Rareware GB']=A.settings.rareware_gb_fairies;C['Random Shop Prices']=A.settings.random_prices;C['Banana Port Randomization']=A.settings.bananaport_rando;C['Shuffle Shop Locations']=A.settings.shuffle_shops;C['Shuffle Kasplats']=A.settings.kasplat_rando_setting;C['Key 8 Required']=A.settings.krool_access;C['Number of Keys Required']=A.settings.krool_key_count;C['Fast Start']=A.settings.fast_start_beginning_of_game;C['Helm Setting']=A.settings.helm_setting;C['Quality of Life']=A.settings.quality_of_life;C['Tag Anywhere']=A.settings.enable_tag_anywhere;C['Fast GBs']=A.settings.fast_gbs;C['High Requirements']=A.settings.high_req;C['Win Condition']=A.settings.win_condition;B['Settings']=C;B[F]={}
		if A.settings.colors!={}or A.settings.klaptrap_model_index:
			B[F][U]={}
			for Y in A.settings.colors:
				if Y=='dk':B[F][U]['DK Color']=A.settings.colors[Y]
				else:B[F][U][f"{Y.capitalize()} Color"]=A.settings.colors[Y]
			v={25:'Beaver',30:'Klobber',32:'Kaboom',33:'Green Klaptrap',34:'Purple Klaptrap',35:'Red Klaptrap',36:'Klaptrap Teeth',38:'Krash',39:'Troff',48:'N64 Logo',52:'Mech Fish',66:'Krossbones',71:'Rabbit',75:'Minecart Skeleton Head',81:'Tomato',98:'Ice Tomato',105:'Golden Banana',112:'Microbuffer',114:'Bell',150:'Missile (Car Race)',176:'Red Buoy',177:'Green Buoy',189:'Rareware Logo'}
			if A.settings.klaptrap_model_index in v:B[F][U][AF]=v[A.settings.klaptrap_model_index]
			else:B[F][U][AF]=f"Unknown Model {hex(A.settings.klaptrap_model_index)}"
		B[V]={};w={};x=[_E,L,_F,M,N,O,P,p]
		for (d,e) in enumerate(A.settings.EntryGBs):w[x[d]]=e
		B[V]['B Locker GBs']=w;y={}
		for (d,e) in enumerate(A.settings.BossBananas):y[x[d]]=e
		B[V]['Troff N Scoff Bananas']=y;B[V][AG]={};B[H]={};B[H]['Starting Kong List']=u;B[H]['Japes Kong Puzzle Solver']=ItemList[ItemFromKong(A.settings.diddy_freeing_kong)].name;B[H]['Tiny Temple Puzzle Solver']=ItemList[ItemFromKong(A.settings.tiny_freeing_kong)].name;B[H]['Llama Temple Puzzle Solver']=ItemList[ItemFromKong(A.settings.lanky_freeing_kong)].name;B[H]['Factory Kong Puzzle Solver']=ItemList[ItemFromKong(A.settings.chunky_freeing_kong)].name
		if A.settings.coin_door_open in['need_both','need_rw']:B[V][AG]['Medal Requirement']=A.settings.medal_requirement
		B[c]={};B[c]['Keys Required for K Rool']=A.GetKroolKeysRequired(A.settings.krool_keys_required);z=[]
		for f in A.settings.krool_order:z.append(ItemList[ItemFromKong(f)].name.capitalize())
		B[c]['K Rool Phases']=z;AN=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];A0=[]
		for AO in A.settings.helm_order:A0.append(AN[AO].name.capitalize())
		B[c]['Helm Rooms']=A0;B[W]={H:{},'Shops':{},X:{},_E:{},L:{},_F:{},M:{},N:{},O:{},P:{},p:{},AH:{}};B['Playthrough']=A.playthrough;B['Way of the Hoard']=A.woth;B['Paths']={};A1=0
		for (A2,AP) in A.woth_paths.items():
			AQ=ItemList[LocationList[A2].item];A3={}
			for AR in AP:A4=LocationList[AR];AS=ItemList[A4.item];A3[A4.name]=AS.name
			A5=G
			if LocationList[A2].item==Items.ProgressiveSlam:A1+=1;A5=Q+str(A1)
			B['Paths'][AQ.name+A5]=A3
		for (AT,D) in LocationList.items():
			if D.type==Types.Constant:continue
			if D.item is _C:Z=Items.NoItem
			else:Z=ItemList[D.item]
			if D.type==Types.Kong:B[W][H][D.name]=Z.name
			elif D.type==Types.Shop:
				if D.item is _C or D.item==Items.NoItem:continue
				J=G
				if D.item in ProgressiveMoves.keys():
					if D.item==Items.ProgressiveSlam:J=f"{A.settings.prices[Items.ProgressiveSlam][0]}->{A.settings.prices[Items.ProgressiveSlam][1]}"
					elif D.item==Items.ProgressiveAmmoBelt:J=f"{A.settings.prices[Items.ProgressiveAmmoBelt][0]}->{A.settings.prices[Items.ProgressiveAmmoBelt][1]}"
					elif D.item==Items.ProgressiveInstrumentUpgrade:J=f"{A.settings.prices[Items.ProgressiveInstrumentUpgrade][0]}->{A.settings.prices[Items.ProgressiveInstrumentUpgrade][1]}->{A.settings.prices[Items.ProgressiveInstrumentUpgrade][2]}"
				elif A.settings.random_prices==_G:J=str(A.settings.prices[D.item])
				else:J=str(A.settings.prices[AT])
				B[W]['Shops'][D.name]=Z.name+f" ({J})"
			else:
				E=AH
				if'Isles'in D.name:E=X
				elif'Japes'in D.name:E=_E
				elif'Aztec'in D.name:E=L
				elif AI in D.name:E=_F
				elif AJ in D.name:E=M
				elif'Forest'in D.name:E=N
				elif'Caves'in D.name:E=O
				elif AK in D.name:E=P
				elif'Helm'in D.name:E=p
				B[W][E][D.name]=Z.name
		if A.settings.shuffle_loading_zones=='levels':
			R=OrderedDict();AU={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};AV={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle}
			for (AW,AX) in AU.items():AY=AV[A.shuffled_exit_data[AW].reverse];R[AX.name]=AY.name
			B['Shuffled Level Order']=R
		elif A.settings.shuffle_loading_zones!='none':
			R=OrderedDict();g={X:[X,'Japes Lobby','Aztec Lobby','Factory Lobby','Galleon Lobby','Fungi Lobby','Caves Lobby','Castle Lobby',"Snide's Room",'Training Grounds','Banana Fairy Isle',"DK's Treehouse"],_E:[_E],L:[L],_F:[_F],M:[M],N:[N],O:[O],P:[P]};h={'Other':{}}
			for E in g:h[E]={}
			for (exit,i) in A.shuffled_exit_data.items():
				S='Other'
				for E in g:
					for AZ in g[E]:
						if i.spoilerName.find(AZ)==0:S=E
				R[ShufflableExits[exit].name]=i.spoilerName;h[S][ShufflableExits[exit].name]=i.spoilerName
			B['Shuffled Exits']=R;B['Shuffled Exits (Sorted by destination)']=h
		B[I]={}
		if A.settings.boss_location_rando:
			A6=OrderedDict();Aa={'JapesBoss':'Army Dillo 1','AztecBoss':'Dogadon 1','FactoryBoss':'Mad Jack','GalleonBoss':'Pufftoss','FungiBoss':'Dogadon 2','CavesBoss':'Army Dillo 2','CastleBoss':'King Kut Out'}
			for T in range(7):A6[G.join(map(lambda x:x if x.islower()else Q+x,Levels(T).name)).strip()]=Aa[Maps(A.settings.boss_maps[T]).name]
			B[I]['Shuffled Boss Order']=A6
		B[I][q]={}
		if A.settings.boss_kong_rando:
			A7=OrderedDict()
			for T in range(7):A7[G.join(map(lambda x:x if x.islower()else Q+x,Levels(T).name)).strip()]=Kongs(A.settings.boss_kongs[T]).name.capitalize()
			B[I]['Shuffled Boss Kongs']=A7;j=G
			for Ab in A.settings.kutout_kongs:j=j+Kongs(Ab).name.capitalize()+r
			B[I][q]['Shuffled Kutout Kong Order']=j.removesuffix(r)
		if A.settings.hard_bosses:
			A8=[]
			for f in A.settings.kko_phase_order:A8.append(f"Phase {f+1}")
			B[I][q]['Shuffled Kutout Phases']=r.join(A8)
		if A.settings.bonus_barrels in('random','selected'):
			k=OrderedDict()
			for (D,Ac) in A.shuffled_barrel_data.items():
				if D in HelmMinigameLocations and A.settings.helm_barrels=='skip':continue
				if D not in HelmMinigameLocations and A.settings.bonus_barrels=='skip':continue
				k[LocationList[D].name]=MinigameRequirements[Ac].name
			if len(k)>0:B['Shuffled Bonus Barrels']=k
		if A.settings.music_bgm==s:B[F]['Background Music']=A.music_bgm_data
		if A.settings.music_fanfares==s:B[F]['Fanfares']=A.music_fanfare_data
		if A.settings.music_events==s:B[F]['Event Themes']=A.music_event_data
		if A.settings.kasplat_rando:B['Shuffled Kasplats']=A.human_kasplats
		if A.settings.random_patches:B['Shuffled Dirt Patches']=A.human_patches
		if A.settings.bananaport_rando!='off':B['Shuffled Bananaports']=A.human_warp_locations
		if len(A.hint_list)>0:B['Wrinkly Hints']=A.hint_list
		if A.settings.wrinkly_location_rando:B['Wrinkly Door Locations']=A.human_hint_doors
		if A.settings.tns_location_rando:B['T&S Portal Locations']=A.human_portal_doors
		if A.settings.crown_placement_rando:B['Shuffled Crowns']=A.human_crowns
		l={Levels.DKIsles:X,Levels.JungleJapes:_E,Levels.AngryAztec:L,Levels.FranticFactory:_F,Levels.GloomyGalleon:M,Levels.FungiForest:N,Levels.CrystalCaves:O,Levels.CreepyCastle:P}
		if A.settings.shuffle_shops:
			A9={}
			for E in A.shuffled_shop_locations:
				S='Unknown Level';a={Regions.CrankyGeneric:'Cranky',Regions.CandyGeneric:'Candy',Regions.FunkyGeneric:'Funky',Regions.Snide:'Snide'}
				if E in l:S=l[E]
				for m in A.shuffled_shop_locations[E]:
					AA=AL;AB=AL;AC=A.shuffled_shop_locations[E][m]
					if m in a:AA=a[m]
					if AC in a:AB=a[AC]
					A9[f"{S} - {AA}"]=AB
			B['Shop Locations']=A9
		for n in (W,I):
			AD=True
			for Ad in B[n]:
				if B[n][Ad]!={}:AD=False
			if AD:del B[n]
		if A.settings.cb_rando:
			Ae={'cb':' Bananas','balloons':' Balloons'};B[t]={};Af=['Japes','Aztec',AI,AJ,'Fungi','Caves',AK];Ag=['Donkey','Diddy','Lanky','Tiny','Chunky']
			for Ah in Af:
				for Ai in Ag:B[t][f"{Ah} {Ai}"]={'Balloons':G,'Bananas':G}
			for K in A.cb_placements:
				Aj=l[K['level']];AE=1
				if K['level']==Levels.FungiForest:AE=0
				b=G.join(map(lambda x:x if x.islower()else Q+x,Maps(K['map']).name)).strip();Ak=['2 D Ship','5 D Ship','5 D Temple']
				for o in Ak:
					if o in b:b=b.replace(o,o.replace(Q,G))
				B[t][f"{Aj.split(Q)[AE]} {NameFromKong(K[_H])}"][Ae[K['type']].strip()]+=f"{b.strip()}: {K['name']}<br>"
		A.json=json.dumps(B,indent=4)
	def UpdateKasplats(A,kasplat_map):
		'Update kasplat data.';C='kasplat_swaps'
		for (G,D) in kasplat_map.items():
			B=LocationList[G];E=B.map;H=B.kong;A.human_kasplats[B.name]=NameFromKong(D);map=_C
			for F in A.enemy_replacements:
				if F[_I]==E:map=F;break
			if map is _C:map={_I:E};A.enemy_replacements.append(map)
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
					if C not in B:B[C]={_I:C,H:[]}
					A={};A['vanilla_map']=GetMapId(G.regionId);A['vanilla_exit']=GetExitId(G);A['new_map']=GetMapId(E.regionId);A['new_exit']=GetExitId(E);B[C][H].append(A)
				except Exception as I:print(I)
		for (F,J) in B.items():D.shuffled_exit_instructions.append(J)
	def UpdateLocations(A,locations):
		'Update location list for what was produced by the fill.';R='instrument';Q='ammo_belt';P='gun';O='slam';N='special';M='move_kong';L='move_lvl';A.location_data={};A.shuffled_kong_placement={};S={_H:A.settings.starting_kong,_J:337};T={_L:S};A.shuffled_kong_placement['TrainingGrounds']=T;U=[B for B in[Locations.DiddyKong,Locations.LankyKong,Locations.TinyKong,Locations.ChunkyKong]if B not in A.settings.kong_locations]
		for V in U:A.WriteKongPlacement(V,Items.NoItem)
		for (id,B) in locations.items():
			if B.item is not _C and B.item is not Items.NoItem and not B.constant and B.type not in A.settings.shuffled_location_types:
				A.location_data[id]=B.item
				if B.type==Types.Shop:
					H=0
					if B.movetype in[MoveTypes.Guns,MoveTypes.AmmoBelt]:H=1
					elif B.movetype==MoveTypes.Instruments:H=2
					K=[B.kong]
					if B.kong==Kongs.any:K=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
					I=B.level
					if I==8:I=7
					C=ItemList[B.item];D=C.movetype;E=0
					if id in A.settings.prices:E=A.settings.prices[id]
					if A.settings.random_prices==_G:E=A.settings.prices[B.item]
					if D==MoveTypes.Flag:
						for J in K:A.move_data[0][H][J][I]={_A:_B,_B:C.flag,_D:E}
					else:
						F=C.index-1;G=C.kong
						for J in K:
							if D==MoveTypes.Slam or D==MoveTypes.AmmoBelt or D==MoveTypes.Guns and F>0 or D==MoveTypes.Instruments and F>0:G=J
							A.move_data[0][H][J][I]={_A:[N,O,P,Q,R][D],L:F,M:G,_D:E}
				elif B.type==Types.Kong:A.WriteKongPlacement(id,B.item)
				elif B.type==Types.TrainingBarrel and A.settings.training_barrels!=_K:
					C=ItemList[B.item];D=C.movetype;E=0
					if D==MoveTypes.Flag:A.move_data[1].append({_A:_B,_B:C.flag,_D:E})
					else:F=C.index-1;G=C.kong;A.move_data[1].append({_A:[N,O,P,Q,R][D],L:F,M:G%5,_D:E})
				elif B.type==Types.Shockwave and A.settings.shockwave_status!=_G:
					C=ItemList[B.item];D=C.movetype;E=0
					if D==MoveTypes.Flag:A.move_data[2].append({_A:_B,_B:C.flag,_D:E})
					else:F=C.index-1;G=C.kong;A.move_data[2]=[{_A:[N,O,P,Q,R][D],L:F,M:G%5,_D:E}]
	def WriteKongPlacement(A,locationId,item):
		'Write kong placement information for the given kong cage location.';F=locationId;B=_E;C=A.settings.diddy_freeing_kong;D=338;E=339
		if F==Locations.LankyKong:B='Llama Temple';C=A.settings.lanky_freeing_kong;D=340;E=341
		elif F==Locations.TinyKong:B='Tiny Temple';C=A.settings.tiny_freeing_kong;D=342;E=343
		elif F==Locations.ChunkyKong:B=_F;C=A.settings.chunky_freeing_kong;D=344;E=345
		G={};G[_H]=KongFromItem(item);G[_J]=D;H={_H:C,_J:E};I={_L:G,'puzzle':H};A.shuffled_kong_placement[B]=I
	def UpdatePlaythrough(A,locations,playthroughLocations):
		'Write playthrough as a list of dicts of location/item pairs.';A.playthrough={};C=0
		for D in playthroughLocations:
			B={};B['Available GBs']=D.availableGBs;E=list(map(lambda l:locations[l],D.locations));E.sort(key=A.ScoreLocations)
			for F in E:B[F.name]=ItemList[F.item].name
			A.playthrough[C]=B;C+=1
	def UpdateWoth(A,locations,wothLocations):
		'Write woth locations as a dict of location/item pairs.';B=wothLocations;A.woth={};A.woth_locations=B
		for D in B:C=locations[D];A.woth[C.name]=ItemList[C.item].name
	def ScoreLocations(B,location):
		'Score a location with the given settings for sorting the Playthrough.';A=location
		if A==Locations.BananaHoard:return 250
		if A.type==Types.Banana:return 100
		elif B.settings.win_condition=='all_fairies'and A.type==Types.Fairy:return 10
		elif B.settings.win_condition=='all_blueprints'and A.type==Types.Blueprint:return 10
		elif B.settings.win_condition=='all_medals'and A.type==Types.Medal:return 10
		elif A.type==Types.Kong:return 0
		elif A.type==Types.Constant:return 2
		return 1
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