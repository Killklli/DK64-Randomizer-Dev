'Compile a list of hints based on the settings.'
_m=' from '
_l='Factory LZR hint unable to be placed!'
_k='Aztec LZR hint unable to be placed!'
_j='Japes LZR hint unable to be placed!'
_i='Small Banana'
_h='Small Bananas'
_g='puzzle'
_f='locked'
_e='Tiny Temple'
_d='Llama Temple'
_c='Ammo Belt Upgrade'
_b='Cranky'
_a='Hideout Helm'
_Z='Chunky'
_Y='Donkey'
_X='all'
_W='Instrument Upgrade'
_V='Slam Upgrade'
_U='DK Isles'
_T='ammo_belt'
_S='joke'
_R='Creepy Castle'
_Q='Crystal Caves'
_P='Fungi Forest'
_O='Gloomy Galleon'
_N='Angry Aztec'
_M='slam'
_L='Frantic Factory'
_K='Jungle Japes'
_J='gun'
_I='instrument'
_H='kong'
_G='level'
_F='name'
_E='cryptic'
_D='special'
_C=None
_B=False
_A=True
import random
from re import U
from randomizer.Enums.Events import Events
from randomizer.Enums.HintType import HintType
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.ItemPool import AllKongMoves,ImportantSharedMoves
from randomizer.Lists.Item import ItemList,NameFromKong
from randomizer.Lists.Location import LocationList,SharedShopLocations
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Lists.WrinklyHints import HintLocation,hints
from randomizer.Patching.UpdateHints import UpdateHint,updateRandomHint
from randomizer.Spoiler import Spoiler
class Hint:
	'Hint object for Wrinkly hint text.'
	def __init__(A,*,hint='',important=_A,priority=1,kongs=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],repeats=1,base=_B,keywords=[],permitted_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle],subtype=_S,joke=_B,joke_defined=_B):
		'Create wrinkly hint text object.';D=repeats;C=priority;B=important;A.kongs=kongs.copy();A.hint=hint;A.important=B;A.priority=C;A.repeats=D;A.base=base;A.used=_B;A.was_important=B;A.original_repeats=D;A.original_priority=C;A.keywords=keywords.copy();A.permitted_levels=permitted_levels.copy();A.subtype=subtype;A.joke=base
		if joke_defined:A.joke=joke
	def use_hint(A):
		'Set hint as used.'
		if A.repeats==1:A.used=_A;A.repeats=0
		else:A.repeats-=1;A.priority+=1
	def downgrade(A):'Downgrade hint status.';A.important=_B
class MoveInfo:
	'Move Info for Wrinkly hint text.'
	def __init__(A,*,name='',kong='',move_type='',move_level=0,important=_B):
		'Create move info object.';D=move_level;C=move_type;A.name=name;A.kong=kong;E=[_D,_M,_J,_T,_I];F=E.index(C);A.move_type=F;A.move_level=D;A.important=important;B=kong
		if B==Kongs.any:B=Kongs.donkey
		A.item_key={'move_type':C,'move_lvl':D-1,'move_kong':B}
hint_list=[Hint(hint='Did you know - Donkey Kong officially features in Donkey Kong 64.',important=_B,base=_A),Hint(hint='Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.',important=_B,base=_A),Hint(hint='Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.',important=_B,base=_A),Hint(hint='Tiny Kong is the youngest sister of Dixie Kong.',important=_B,base=_A),Hint(hint='Mornin.',important=_B,base=_A),Hint(hint='Lanky Kong is the only kong with no canonical relation to the main Kong family tree.',important=_B,base=_A),Hint(hint='Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.',important=_B,base=_A),Hint(hint='Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.',important=_B,base=_A),Hint(hint='Candy Kong does not appear in Jungle Japes or Fungi Forest.',important=_B,base=_A),Hint(hint='If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.',important=_B,base=_A),Hint(hint='Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.',important=_B,base=_A),Hint(hint='The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.',important=_B,base=_A),Hint(hint='Chunky Kong is the brother of Kiddy Kong.',important=_B,base=_A),Hint(hint='Fungi Forest contains mushrooms.',important=_B,base=_A),Hint(hint='Igloos can be found in Crystal Caves.',important=_B,base=_A),Hint(hint='Frantic Factory has multiple floors where things can be found.',important=_B,base=_A),Hint(hint="Angry Aztec has so much sand, it's even in the wind.",important=_B,base=_A),Hint(hint='DK Isles does not have a key.',important=_B,base=_A),Hint(hint='You can find a rabbit in Fungi Forest and in Crystal Caves.',important=_B,base=_A),Hint(hint='You can find a beetle in Angry Aztec and in Crystal Caves.',important=_B,base=_A),Hint(hint='You can find a vulture in Angry Aztec.',important=_B,base=_A),Hint(hint='You can find an owl in Fungi Forest.',important=_B,base=_A),Hint(hint='To buy moves, you will need coins.',important=_B,base=_A),Hint(hint='You can change the music and sound effects volume in the sound settings on the main menu.',important=_B,base=_A),Hint(hint='Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.',important=_B,base=_A),Hint(hint='Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.',important=_B,base=_A),Hint(hint='I have nothing to say to you.',important=_B,base=_A),Hint(hint='I had something to tell you, but I forgot what it is.',important=_B,base=_A),Hint(hint="I don't know anything.",important=_B,base=_A),Hint(hint="I'm as lost as you are. Good luck!",important=_B,base=_A),Hint(hint='Wrinkly? Never heard of him.',important=_B,base=_A),Hint(hint='This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.',important=_B,base=_A),Hint(hint='Why do they call it oven when you of in the cold food of out hot eat the food?',important=_B,base=_A),Hint(hint='Wanna become famous? Buy followers, coconuts and donks at DK64Randomizer (DK64Randomizer . com)!',important=_B,base=_A),Hint(hint='What you gonna do, SpikeVegeta?',important=_B,base=_A),Hint(hint="You don't care? Just give it to me? Okay, here it is.",important=_B,base=_A),Hint(hint='Rumor has it this game was developed in a cave with only a box of scraps!',important=_B,base=_A),Hint(hint='If you backflip right before Chunky punches K. Rool, you must go into first person camera to face him before the punch.',important=_B,base=_A),Hint(hint='The barrier to Hideout Helm can be cleared by obtaining 801 Golden Bananas. It can also be cleared with fewer than that.',important=_B,base=_A)]
kong_list=[_Y,'Diddy','Lanky','Tiny',_Z,'Any kong']
kong_cryptic=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly'],['Members of the DK Crew','A specific set of relatives','A number of playable characters']]
all_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
level_list=[_K,_N,_L,_O,_P,_Q,_R,_a]
level_list_isles=[_K,_N,_L,_O,_P,_Q,_R,_U]
level_list_helm_isles=[_K,_N,_L,_O,_P,_Q,_R,_a,_U]
level_cryptic=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with four vases','The level with two kongs cages','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with a game from 1981','The level where you need two quarters to play'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level with two inches of water','The level with two ice shields','The level with an Ice Tomato'],['The level with battlements','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']]
level_cryptic_isles=level_cryptic.copy()
level_cryptic_isles.remove(level_cryptic_isles[-1])
level_cryptic_isles.append(['The hub world',"The world with DK's ugly mug on it","The world with only a Cranky's Lab and Snide's HQ in it"])
level_cryptic_helm_isles=level_cryptic.copy()
level_cryptic_helm_isles.append(level_cryptic_isles[-1])
shop_owners=[_b,'Funky','Candy']
shop_cryptic=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
crankys_cryptic=['a location out of this world','a location 5000 points deep',"a mad scientist's laboratory"]
moves_data=[MoveInfo(name='Baboon Blast',move_level=1,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Strong Kong',move_level=2,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Gorilla Grab',move_level=3,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Chimpy Charge',move_level=1,move_type=_D,kong=Kongs.diddy),MoveInfo(name='Rocketbarrel Boost',move_level=2,move_type=_D,kong=Kongs.diddy,important=_A),MoveInfo(name='Simian Spring',move_level=3,move_type=_D,kong=Kongs.diddy),MoveInfo(name='Orangstand',move_level=1,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Baboon Balloon',move_level=2,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Orangstand Sprint',move_level=3,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Mini Monkey',move_level=1,move_type=_D,kong=Kongs.tiny,important=_A),MoveInfo(name='Ponytail Twirl',move_level=2,move_type=_D,kong=Kongs.tiny),MoveInfo(name='Monkeyport',move_level=3,move_type=_D,kong=Kongs.tiny,important=_A),MoveInfo(name='Hunky Chunky',move_level=1,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name='Primate Punch',move_level=2,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name='Gorilla Gone',move_level=3,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name=_V,move_level=1,move_type=_M,kong=Kongs.any),MoveInfo(name=_V,move_level=2,move_type=_M,kong=Kongs.any),MoveInfo(name=_V,move_level=3,move_type=_M,kong=Kongs.any),MoveInfo(name='Coconut Shooter',move_level=1,move_type=_J,kong=Kongs.donkey,important=_A),MoveInfo(name='Peanut Popguns',move_level=1,move_type=_J,kong=Kongs.diddy,important=_A),MoveInfo(name='Grape Shooter',move_level=1,move_type=_J,kong=Kongs.lanky),MoveInfo(name='Feather Bow',move_level=1,move_type=_J,kong=Kongs.tiny,important=_A),MoveInfo(name='Pineapple Launcher',move_level=1,move_type=_J,kong=Kongs.chunky),MoveInfo(name='Homing Ammo',move_level=2,move_type=_J,kong=Kongs.any),MoveInfo(name='Sniper Scope',move_level=3,move_type=_J,kong=Kongs.any),MoveInfo(name=_c,move_level=1,move_type=_T,kong=Kongs.any),MoveInfo(name=_c,move_level=2,move_type=_T,kong=Kongs.any),MoveInfo(name='Bongo Blast',move_level=1,move_type=_I,kong=Kongs.donkey,important=_A),MoveInfo(name='Guitar Gazump',move_level=1,move_type=_I,kong=Kongs.diddy,important=_A),MoveInfo(name='Trombone Tremor',move_level=1,move_type=_I,kong=Kongs.lanky,important=_A),MoveInfo(name='Saxophone Slam',move_level=1,move_type=_I,kong=Kongs.tiny,important=_A),MoveInfo(name='Triangle Trample',move_level=1,move_type=_I,kong=Kongs.chunky,important=_A),MoveInfo(name=_W,move_level=2,move_type=_I,kong=Kongs.any),MoveInfo(name=_W,move_level=3,move_type=_I,kong=Kongs.any),MoveInfo(name=_W,move_level=4,move_type=_I,kong=Kongs.any)]
kong_placement_levels=[{_F:_K,_G:0},{_F:_d,_G:1},{_F:_e,_G:1},{_F:_L,_G:2}]
hint_distribution={HintType.Joke:1,HintType.KRoolOrder:2,HintType.HelmOrder:2,HintType.FullShop:8,HintType.MoveLocation:7,HintType.BLocker:3,HintType.TroffNScoff:0,HintType.KongLocation:2,HintType.Entrance:8,HintType.KeyLocation:-1,HintType.WothLocation:8,HintType.FullShopWithItems:5,HintType.FoolishMove:4}
HINT_CAP=35
def compileHints(spoiler):
	'Create a hint distribution, generate buff hints, and place them in locations.';Ac=', then ';A=spoiler;H=[HintType.Joke]
	if A.settings.krool_phase_count<5:H.append(HintType.KRoolOrder)
	if A.settings.helm_setting!='skip_all'and A.settings.helm_phase_count<5:H.append(HintType.HelmOrder)
	if not A.settings.unlock_all_moves and A.settings.move_rando not in('off','item_shuffle'):H.append(HintType.FullShop);H.append(HintType.MoveLocation)
	if A.settings.shuffle_items and Types.Shop in A.settings.shuffled_location_types:
		H.append(HintType.FullShopWithItems)
		if not A.settings.no_logic:H.append(HintType.FoolishMove);H.append(HintType.WothLocation)
	if A.settings.randomize_blocker_required_amounts:H.append(HintType.BLocker)
	if A.settings.randomize_cb_required_amounts and len(A.settings.krool_keys_required)>0 and A.settings.krool_keys_required!=[Events.HelmKeyTurnedIn]:H.append(HintType.TroffNScoff)
	if A.settings.kong_rando:H.append(HintType.KongLocation)
	if A.settings.shuffle_loading_zones==_X:Ad=hint_distribution[HintType.BLocker];hint_distribution[HintType.BLocker]=max(1,hint_distribution[HintType.TroffNScoff]);hint_distribution[HintType.TroffNScoff]=Ad;H.append(HintType.Entrance)
	if Types.Key in A.settings.shuffled_location_types:H.append(HintType.KeyLocation);hint_distribution[HintType.KeyLocation]=len(A.settings.krool_keys_required)
	Y=0
	for type in hint_distribution:
		if type in H:Y+=hint_distribution[type]
		else:hint_distribution[type]=0
	while Y<HINT_CAP:
		A4=random.choice(H)
		if A4==HintType.KeyLocation:continue
		hint_distribution[A4]+=1;Y+=1
	while Y>HINT_CAP:
		i=random.choice(H)
		if i==HintType.KeyLocation:continue
		if hint_distribution[i]>0:hint_distribution[i]-=1;Y-=1
	P=not A.settings.no_logic and A.settings.shuffle_loading_zones!=_X;W=_C
	if P:
		W=[]
		for C in all_levels:
			for Q in A.settings.owned_kongs_by_level[C]:
				if not A.settings.wrinkly_location_rando:
					if C==Levels.FranticFactory and Q not in[Kongs.donkey,Kongs.chunky]and(Kongs.donkey not in A.settings.owned_kongs_by_level[C]or Items.GorillaGrab not in A.settings.owned_moves_by_level[C]):continue
					if C==Levels.FungiForest and Q is not Kongs.chunky and(Kongs.donkey not in A.settings.owned_kongs_by_level[C]or Items.GorillaGrab not in A.settings.owned_moves_by_level[C]):continue
					if C==Levels.CrystalCaves and Q is Kongs.diddy and(Kongs.chunky not in A.settings.owned_kongs_by_level[C]or Items.PrimatePunch not in A.settings.owned_moves_by_level[C]or Items.RocketbarrelBoost not in A.settings.owned_moves_by_level[C]or Items.Barrels not in A.settings.owned_moves_by_level[C]):continue
					if C==Levels.CrystalCaves and(Kongs.chunky not in A.settings.owned_kongs_by_level[C]or Items.PrimatePunch not in A.settings.owned_moves_by_level[C]or Items.Barrels not in A.settings.owned_moves_by_level[C]):continue
					if C==Levels.AngryAztec and Q is Kongs.chunky and(Kongs.tiny not in A.settings.owned_kongs_by_level[C]or Items.Feather not in A.settings.owned_moves_by_level[C]or Items.HunkyChunky not in A.settings.owned_moves_by_level[C]):continue
				Ae=[A for A in hints if A.level==C and A.kong==Q][0];W.append(Ae)
	A5=[];A6=0
	while A6<hint_distribution[HintType.KongLocation]:
		c=random.choice(kong_placement_levels);J=A.shuffled_kong_placement[c[_F]][_f][_H];A7=A.shuffled_kong_placement[c[_F]][_g][_H];A8=c[_G];j=_C
		if P and J not in A5:j=[B for B in all_levels if A.settings.EntryGBs[B]<=A.settings.EntryGBs[c[_G]]]
		k=A.settings.starting_kong_list.copy();k.append(A7);B=getRandomHintLocation(kongs=k,levels=j)
		if B is _C:
			if j is not _C:B=getRandomHintLocation(kongs=k)
			else:hint_distribution[HintType.Joke]+=1;hint_distribution[HintType.KongLocation]-=1;continue
		Af=kong_list[A7]
		if A.settings.wrinkly_hints==_E:
			if not J==Kongs.any:X=random.choice(kong_cryptic[J])
			E=random.choice(level_cryptic[A8])
		else:
			if not J==Kongs.any:X=kong_list[J]
			E=level_list[A8]
		A9='frees'
		if J==Kongs.any:A9='accesses';X='an empty cage'
		D=f"{Af} {A9} {X} in {E}.";A5.append(J);B.hint_type=HintType.KongLocation;UpdateHint(B,D);A6+=1
	AA=[]
	for I in range(hint_distribution[HintType.BLocker]):
		Z=_C
		if P:Z=W
		G=[]
		while len(G)==0:
			B=getRandomHintLocation(location_list=Z);G=[C for C in all_levels if(not P or A.settings.EntryGBs[C]>A.settings.EntryGBs[B.level])and(B.level,C)not in AA]
			if not A.settings.maximize_helm_blocker:
				if I==0:G=[Levels.HideoutHelm]
				else:G.append(Levels.HideoutHelm)
		M=random.choice(G);AA.append((B.level,M));E=level_list[M]
		if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic[M])
		D=f"The barrier to {E} can be cleared by obtaining {A.settings.EntryGBs[M]} Golden Bananas.";B.hint_type=HintType.BLocker;UpdateHint(B,D)
	AB=_B
	for I in range(hint_distribution[HintType.HelmOrder]):
		Z=_C
		if P and not AB and I==hint_distribution[HintType.HelmOrder]-1:Z=W
		B=getRandomHintLocation(location_list=Z)
		if W is _C or B in W:AB=_A
		Ag=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];Ah=[Ag[B]for B in A.settings.helm_order];Ai=[NameFromKong(A)for A in Ah];Aj=Ac.join(Ai);l=f"The Blast-O-Matic can be disabled by using {Aj}.";B.hint_type=HintType.HelmOrder;UpdateHint(B,l)
	if hint_distribution[HintType.KeyLocation]>0:
		L=[];AC={}
		if Events.JapesKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.JungleJapesKey)
		if Events.AztecKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.AngryAztecKey)
		if Events.FactoryKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.FranticFactoryKey)
		if Events.GalleonKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.GloomyGalleonKey)
		if Events.ForestKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.FungiForestKey)
		if Events.CavesKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.CrystalCavesKey)
		if Events.CastleKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.CreepyCastleKey)
		if Events.HelmKeyTurnedIn in A.settings.krool_keys_required:L.append(Items.HideoutHelmKey)
		for (d,F) in LocationList.items():
			if F.item in L:AC[F.item]=F
		for AD in L:
			F=AC[AD];AE=ItemList[AD];J=F.kong
			if F.kong==Kongs.any and F.type==Types.Key:J=A.settings.boss_kongs[F.level]
			if A.settings.wrinkly_hints==_E:
				if F.level==Levels.Shops:E="Cranky's Lab"
				else:E=random.choice(level_cryptic_helm_isles[F.level])
				X=random.choice(kong_cryptic[J])
			else:
				if F.level==Levels.Shops:E=random.choice(crankys_cryptic)
				else:E=level_list_helm_isles[F.level]
				X=kong_list[J]
			G=[]
			for (e,C) in A.settings.level_order.items():
				if e<=AE.index:G.append(C)
			B=getRandomHintLocation(levels=G)
			if B is _C:B=getRandomHintLocation()
			D=f"{AE.name} can be acquired with {X} in {E}.";B.hint_type=HintType.KeyLocation;UpdateHint(B,D)
	f={};AF=[];m=0
	while m<hint_distribution[HintType.MoveLocation]:
		R=_C;AG=[B for B in A.woth.keys()if B not in AF and any((A in B for A in shop_owners))]
		if len(AG)==0:N=hint_distribution[HintType.MoveLocation]-m;hint_distribution[HintType.Joke]+=N;hint_distribution[HintType.MoveLocation]-=N;break
		a=random.choice(AG);g=level_list_isles.index([A for A in level_list_isles if a[:5]in A][0])
		for n in ItemList:
			if ItemList[n].name==A.woth[a]:
				if n==Items.ProgressiveSlam:continue
				R=n;break
		G=all_levels.copy()
		if P and not A.settings.hard_level_progression:
			AH=all_levels.copy();AH.sort(key=lambda l:A.settings.EntryGBs[l]);G=[];o=[]
			for C in AH:
				if R not in A.settings.owned_moves_by_level[C]:G.append(C)
				else:
					p=[B for B in all_levels if A.settings.EntryGBs[B]==A.settings.EntryGBs[C]and B not in G]
					if len(p)==1 or g>=7:o=p
					else:
						AI=-1
						for e in A.settings.level_order:
							if g==A.settings.level_order[e]:AI=e;break
						for AJ in p:
							Ak=[B for B in A.settings.level_order if AJ==A.settings.level_order[B]][0]
							if Ak<=AI:o.append(AJ)
					break
			G.extend(o)
		if R in f.keys():
			for AK in f[R]:
				if AK in G:G.remove(AK)
		else:f[R]=[]
		B=getRandomHintLocation(levels=G,move_name=A.woth[a])
		if B is _C:AF.append(a);continue
		AL=level_list_isles[g]
		if A.settings.wrinkly_hints==_E:AL=random.choice(level_cryptic_isles[g])
		q=[A for A in shop_owners if A in a][0];D=f"On the Way of the Hoard, {ItemList[R].name} is bought from {q} in {AL}.";f[R].append(B.level);B.hint_type=HintType.MoveLocation;UpdateHint(B,D);m+=1
	if hint_distribution[HintType.TroffNScoff]>0:
		O=[]
		for S in A.settings.krool_keys_required:
			if S==Events.JapesKeyTurnedIn:O.append(A.settings.level_order[1])
			if S==Events.AztecKeyTurnedIn:O.append(A.settings.level_order[2])
			if S==Events.FactoryKeyTurnedIn:O.append(A.settings.level_order[3])
			if S==Events.GalleonKeyTurnedIn:O.append(A.settings.level_order[4])
			if S==Events.ForestKeyTurnedIn:O.append(A.settings.level_order[5])
			if S==Events.CavesKeyTurnedIn:O.append(A.settings.level_order[6])
			if S==Events.CastleKeyTurnedIn:O.append(A.settings.level_order[7])
		r=0
		while r<hint_distribution[HintType.TroffNScoff]:
			s=0;t=[]
			while not any(t):
				s+=1
				if s>15:break
				B=getRandomHintLocation();t=[C for C in all_levels if C in O and(not P or A.settings.EntryGBs[C]>=A.settings.EntryGBs[B.level])]
			if s>15:N=hint_distribution[HintType.TroffNScoff]-r;hint_distribution[HintType.Joke]+=N;hint_distribution[HintType.TroffNScoff]-=N;break
			M=random.choice(t);E=level_list[M]
			if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic[M])
			AM=A.settings.BossBananas[M];AN=_h
			if AM==1:AN=_i
			D=f"The barrier to the boss in {E} can be cleared by obtaining {AM} {AN}.";B.hint_type=HintType.TroffNScoff;UpdateHint(B,D);r+=1
	if hint_distribution[HintType.Entrance]>0:
		u=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];v=[Regions.AngryAztecStart,Regions.AngryAztecOasis,Regions.AngryAztecMain];w=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];Al=[u,v,w,[Regions.BananaFairyRoom],[Regions.TrainingGrounds],[Regions.GloomyGalleonStart,Regions.LighthousePlatform,Regions.LighthouseUnderwater,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]]
		for I in range(hint_distribution[HintType.Entrance]):
			D=''
			if I==0:
				x=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in u];random.shuffle(x);AO=_B
				while len(x)>0:
					Am=x.pop();D=TryCreatingLoadingZoneHint(A,Am,u)
					if D!='':AO=_A;break
				if not AO:print(_j)
			elif I==1:
				y=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in v];random.shuffle(y);AP=_B
				while len(y)>0:
					An=y.pop();D=TryCreatingLoadingZoneHint(A,An,v)
					if D!='':AP=_A;break
				if not AP:print(_k)
			elif I==2:
				z=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in w];random.shuffle(z);AQ=_B
				while len(z)>0:
					Ao=z.pop();D=TryCreatingLoadingZoneHint(A,Ao,w)
					if D!='':AQ=_A;break
				if not AQ:print(_l)
			else:
				AR=random.choice(Al);A0=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in AR];random.shuffle(A0);AS=_B
				while len(A0)>0:
					AT=A0.pop();D=TryCreatingLoadingZoneHint(A,AT,AR)
					if D!='':AS=_A;break
				if not AS:print(f"Useful LZR hint to {AT.name} unable to be placed!")
			B=getRandomHintLocation();B.hint_type=HintType.Entrance;UpdateHint(B,D)
	if hint_distribution[HintType.FullShop]>0:
		h=[]
		for AU in range(3):
			for C in range(8):
				T=[]
				for Q in range(5):
					Ap=A.move_data[0][AU][Q][C]
					for A1 in moves_data:
						if A1.item_key==Ap:
							if A1.name not in T:T.append(A1.name)
				if len(T)==0:continue
				U=T[0]
				if len(T)>1:U=f"{', '.join(T[:-1])} and {T[-1]}"
				q=shop_owners[AU];E=level_list_isles[C]
				if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic_isles[C])
				Aq=f"{q}'s in {E} contains {U}";h.append(Aq)
		random.shuffle(h);A2=0
		while A2<hint_distribution[HintType.FullShop]:
			B=getRandomHintLocation()
			if len(h)==0:N=hint_distribution[HintType.FullShop]-A2;hint_distribution[HintType.Joke]+=N;hint_distribution[HintType.FullShop]-=N;break
			D=h.pop();B.hint_type=HintType.FullShop;UpdateHint(B,D);A2+=1
	if hint_distribution[HintType.FoolishMove]>0:
		V=AllKongMoves();V.append(Items.Shockwave)
		for d in A.woth_locations:
			F=LocationList[d]
			if F.item in V:V.remove(F.item)
		Ar=2-V.count(Items.ProgressiveSlam);random.shuffle(V)
		for I in range(hint_distribution[HintType.FoolishMove]):
			if len(V)==0:hint_distribution[HintType.FoolishMove]-=1;hint_distribution[HintType.WothLocation]+=1
			AV=V.pop()
			if AV==Items.ProgressiveSlam:
				if Ar==0:A3='Super Simian Slam'
				else:A3='Super Duper Simian Slam'
			else:A3=ItemList[AV].name
			B=getRandomHintLocation();D=f"It would be foolish to seek out {A3}.";B.hint_type=HintType.FoolishMove;UpdateHint(B,D)
	if hint_distribution[HintType.WothLocation]>0:
		AW=[]
		for d in A.woth_locations:
			F=LocationList[d]
			if F.type in A.settings.shuffled_location_types:AW.append(F)
		for I in range(hint_distribution[HintType.WothLocation]):B=getRandomHintLocation();As=random.choice(AW);B=getRandomHintLocation();D=f"{As.name} is on the Way of the Hoard.";B.hint_type=HintType.WothLocation;UpdateHint(B,D)
	AX=[]
	for I in range(hint_distribution[HintType.FullShopWithItems]):
		AY=random.choice([A for A in SharedShopLocations if A not in AX]);AX.append(AY);K=LocationList[AY];AZ=[A for(id,A)in LocationList.items()if A.type==Types.Shop and A.level==K.level and A.vendor==K.vendor and A.kong!=Kongs.any]
		if K.item is not _C and K.item!=Items.NoItem:
			Aa=shop_owners[K.vendor];E=level_list_helm_isles[K.level]
			if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic_helm_isles[K.level])
			U=ItemList[K.item].name
		else:
			random.shuffle(AZ);b=[ItemList[A.item].name for A in AZ if A.item is not _C and A.item!=Items.NoItem]
			if len(b)==0:U='nothing'
			else:
				U=b[0]
				if len(b)>1:U=f"{', '.join(b[:-1])} and {b[-1]}"
		Aa=shop_owners[K.vendor];E=level_list_helm_isles[K.level]
		if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic_helm_isles[K.level])
		B=getRandomHintLocation();D=f"{Aa}'s in {E} contains {U}.";B.hint_type=HintType.FullShopWithItems;UpdateHint(B,D)
	for I in range(hint_distribution[HintType.KRoolOrder]):B=getRandomHintLocation();At=[NameFromKong(B)for B in A.settings.krool_order];Au=Ac.join(At);l=f"King K. Rool will face off in the ring against {Au}.";B.hint_type=HintType.KRoolOrder;UpdateHint(B,l)
	for I in range(hint_distribution[HintType.Joke]):B=getRandomHintLocation();Ab=hint_list.copy();random.shuffle(Ab);D=Ab.pop().hint;B.hint_type=HintType.Joke;UpdateHint(B,D)
	UpdateSpoilerHintList(A);A.hint_distribution=hint_distribution;return _A
def getRandomHintLocation(location_list=_C,kongs=_C,levels=_C,move_name=_C):
	'Return an unoccupied hint location. The parameters can be used to specify location requirements.';D=levels;C=kongs;B=location_list;A=[A for A in hints if A.hint==''and(B is _C or A in B)and(C is _C or A.kong in C)and(D is _C or A.level in D)and move_name not in A.banned_keywords]
	if len(A)==0:return _C
	F=random.choice(A)
	for E in hints:
		if E.name==F.name:return E
	return _C
def pushHintToList(hint):'Push hint to hint list.';hint_list.append(hint)
def resetHintList():
	'Reset hint list to default state.'
	for A in hint_list:
		if not A.base:hint_list.remove(A)
		else:A.used=_B;A.important=A.was_important;A.repeats=A.original_repeats;A.priority=A.original_priority
def compileHintsOld(spoiler):
	'Push hints to hint list based on settings. Old method that is now unused.';AM='important';AL='k_rool';c='levels';b='hint';P='color';A=spoiler;resetHintList()
	if A.settings.krool_phase_order_rando and len(A.settings.krool_order)>1:
		Q=f"K. Rool order is {NameFromKong(A.settings.krool_order[0])}"
		for C in range(len(A.settings.krool_order)):
			if C!=0:Q+=f" then {NameFromKong(A.settings.krool_order[C])}"
		hint_list.append(Hint(hint=Q,repeats=2,kongs=A.settings.krool_order.copy(),subtype=AL))
	AN=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];R=[]
	if A.settings.helm_phase_order_rando and len(A.settings.helm_order)>1:
		for AO in A.settings.helm_order:R.append(AN[AO])
		Q=f"Helm Room order is {NameFromKong(R[0])}"
		for C in range(len(R)):
			if C!=0:Q+=f" then {NameFromKong(R[C])}"
		hint_list.append(Hint(hint=Q,repeats=3,kongs=R.copy(),subtype=AL))
	if A.settings.move_rando!='off'and A.move_data is not _C:
		AP=[0,2,1,1,4];AQ=0
		for C in A.settings.krool_order:AQ+=AP[C]
		t=[]
		for d in range(3):
			u=[]
			for G in range(8):
				e=[]
				for AR in range(5):
					AS=A.move_data[0][d][AR][G]
					for K in moves_data:
						if K.item_key==AS:
							if K.name not in e:e.append(K.name)
				u.append(e)
			t.append(u)
		f=[];g=[]
		for (h,d) in enumerate(t):
			for (L,G) in enumerate(d):
				for K in G:
					v=_B
					for w in moves_data:
						if w.name==K and w.important:v=_A
					i=shop_owners[h];D=level_list_isles[L]
					if A.settings.wrinkly_hints==_E:D=random.choice(level_cryptic_isles[L])
					g.append({b:f"{K} can be purchased from {i} in {D}",AM:v,'move':K})
				if len(G)>0:
					i=shop_owners[h];D=level_list_isles[L]
					if A.settings.wrinkly_hints==_E:D=random.choice(level_cryptic_isles[L])
					x=G[0]
					if len(G)>1:x=f"{', '.join(G[:-1])} and {G[-1]}"
					AT=f"{i}'s in {D} contains {x}";f.append({b:AT,'moves':G})
		random.shuffle(f);j=[3,6,10];W=1;y=_A
		for z in f:
			if y:hint_list.append(Hint(hint=z[b],important=_B,keywords=z['moves'],subtype='shop_dump'))
			if W<=len(j):
				if h+1>=j[W-1]:
					if W==len(j):y=_B
					else:W+=1
		random.shuffle(g)
		for k in g:hint_list.append(Hint(hint=k[b],priority=2,important=k[AM],keywords=[k['move']],subtype='move_location'))
	if A.settings.kong_rando:
		A0=A.shuffled_kong_placement;AU=[{_F:_K,_G:0},{_F:_d,_G:1},{_F:_e,_G:1},{_F:_L,_G:2}]
		for l in AU:
			S=A0[l[_F]][_f][_H];AV=A0[l[_F]][_g][_H];L=l[_G]
			if A.settings.wrinkly_hints==_E:
				if not S==Kongs.any:m=random.choice(kong_cryptic[S])
				D=random.choice(level_cryptic[L])
			else:
				if not S==Kongs.any:m=kong_list[S]
				D=level_list[L]
			A1=2
			if S==Kongs.any:m='An empty cage';A1=3
			hint_list.append(Hint(hint=f"{m} can be found in {D}.",kongs=[AV],priority=A1,subtype='kong_location'))
	if A.settings.random_patches:
		X={_U:0,_K:0,_N:0,_L:0,_O:0,_P:0,_Q:0,_R:0}
		for AW in A.dirt_patch_placement:
			for G in X:
				if G in AW:X[G]+=1
		A2=list(X.keys());random.shuffle(A2)
		for Y in range(2):
			for T in range(4):
				D=A2[T+4*Y];n=X[D]
				if n>0:
					A3='patches';A4='are'
					if n==1:A3='patch';A4='is'
					o=f"There {A4} {n} {A3} in {D}";hint_list.append(Hint(hint=o,priority=T+3,important=_B,subtype='level_patch_count'))
		A5=A.dirt_patch_placement.copy();random.shuffle(A5)
		for Y in range(2):
			for T in range(4):AX=A5[T+Y*4];o=f"There is a dirt patch located at {AX}";hint_list.append(Hint(hint=o,priority=T+4,important=Y==0,subtype='patch_location'))
	if A.settings.shuffle_loading_zones==_X:AddLoadingZoneHints(A)
	if A.settings.coin_door_open=='need_both'or A.settings.coin_door_open=='need_rw':hint_list.append(Hint(hint=f"{A.settings.medal_requirement} medals are required to access Jetpac.",priority=4,subtype='medal'))
	if A.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.',subtype='permadeath'))
	if A.settings.level_randomization!='level_order':
		for C in A.settings.krool_keys_required:
			A6=C-4
			if A.settings.wrinkly_hints==_E:D=random.choice(level_cryptic[A6])
			else:D=level_list[A6]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {D} to fight your greatest foe.",important=_B,subtype='key_is_required'))
	AY=['Candy','Funky',_b];AZ=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];A7=[B for B in A.woth.keys()if any((A in B for A in AY))];Aa=random.sample(A7,min(5,len(A7)));A8=random.randint(1,4)
	for A9 in Aa:
		AA=[A for A in AZ if A in A9]
		if len(AA)>0:Ab=str(A9).removesuffix(AA[0])
		hint_list.append(Hint(hint=f"{Ab} is on the Way of the Hoard.",important=random.choice([_A,_A,_B]),priority=A8,subtype='way_of_the_hoard'));A8+=random.randint(1,2)
	Ac=[{_H:_Y,P:'Yellow'},{_H:'Diddy',P:'Red'},{_H:'Lanky',P:'Blue'},{_H:'Tiny',P:'Purple'},{_H:_Z,P:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {level_list[random.randint(0,6)]}, but also in other levels.",important=_B,subtype=_S,joke=_A,joke_defined=_A));AB=random.choice(Ac);hint_list.append(Hint(hint=f"{AB[_H]} can find {AB[P]} bananas in {random.choice(level_list)}.",important=_B,subtype=_S,joke=_A,joke_defined=_A));hint_list.append(Hint(hint=f"{A.settings.krool_key_count} Keys are required to reach K. Rool.",important=_B,subtype='key_count_required'))
	if A.settings.shuffle_loading_zones==c:
		Ad={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};Ae={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle};p={};Z={};AC=[]
		for (Af,AD) in Ad.items():AE=Ae[A.shuffled_exit_data[Af].reverse];p[AE]=AD;Z[AD]=AE
	if A.settings.randomize_blocker_required_amounts is _A and A.settings.shuffle_loading_zones==c:
		for Ag in list(Z.values()):AC.append(Ag.name)
		for C in range(8):
			U=A.settings.EntryGBs[C];AF='Golden Bananas'
			if U==1:AF='Golden Banana'
			D=level_list[C];q=_B;M=all_levels.copy();N=C+1
			if A.settings.shuffle_loading_zones==c:
				if C!=7:
					r=p[C];M=[]
					for V in range(7):
						if V<r:M.append(Z[V])
					if D.replace(' ','')in AC[4:7]:N=4;q=_A
				if A.settings.maximize_helm_blocker is _B and C==7:N=1;q=_A
			if A.settings.wrinkly_hints==_E:D=random.choice(level_cryptic[C])
			hint_list.append(Hint(hint=f"The barrier to {D} can be cleared by obtaining {U} {AF}.",important=q,priority=N,permitted_levels=M.copy(),subtype='gb_amount'))
	for C in range(7):
		U=A.settings.BossBananas[C];AG=_h
		if U==1:AG=_i
		if A.settings.wrinkly_hints==_E:D=random.choice(level_cryptic[C])
		else:D=level_list[C]
		M=all_levels.copy()
		if A.settings.shuffle_loading_zones==c:
			r=p[C];M=[]
			for V in range(7):
				if V<=r:M.append(Z[V])
		hint_list.append(Hint(hint=f"The barrier to the boss in {D} can be cleared by obtaining {U} {AG}.",important=_B,permitted_levels=M.copy(),subtype='cb_amount'))
	H={};F=[]
	for B in hint_list:
		if not B.important and not B.used and B.joke:F.append(B)
	O=random.choice(F);J=_B;Ah=0
	while not J:
		J=updateRandomHint(O.hint,O.kongs.copy(),O.keywords.copy(),O.permitted_levels.copy())
		if J:
			O.use_hint();Ah+=1;E=O.subtype
			if E in H:H[E]+=1
			else:H[E]=1
			break
	random.shuffle(hint_list);N=1;AH=_B;Ai=0
	while not AH:
		AI=_B
		for B in hint_list:
			if B.important and B.priority==N and not B.used and not B.joke:
				AI=_A;J=updateRandomHint(B.hint,B.kongs.copy(),B.keywords.copy(),B.permitted_levels.copy())
				if J:
					B.use_hint();Ai+=1;E=B.subtype
					if E in H:H[E]+=1
					else:H[E]=1
				else:B.downgrade()
		if not AI:AH=_A
		N+=1
	F=[];a=0
	for B in hint_list:
		if not B.important and not B.used and not B.joke:F.append(B)
	for B in hints:
		if B.hint=='':a+=1
	random.shuffle(F);Aj=0;Ak=0
	if a>0:
		s=0;AJ=100;I=0
		while s<a:
			J=_B
			if not F[I].used:J=updateRandomHint(F[I].hint,F[I].kongs,F[I].keywords.copy(),F[I].permitted_levels.copy())
			if J:
				F[I].use_hint();Aj+=1;E=F[I].subtype
				if E in H:H[E]+=1
				else:H[E]=1
				s+=1
			else:AJ-=1
			I+=1
			if I>=len(F):I=0
			if AJ==0:
				AK=[]
				for B in hint_list:
					if not B.joke:AK.append(B.hint)
				for B in hints:
					if B.hint=='':B.hint=random.choice(AK)
				for B in hints:
					if B.hint=='':
						B.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.';E='error'
						if E in H:H[E]+=1
						else:H[E]=1
						Ak+=1
				s=a
	UpdateSpoilerHintList(A);return _A
def AddLoadingZoneHints(spoiler):
	'Add hints for loading zone transitions and their destinations.';A=spoiler;G=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];H=[Regions.AngryAztecStart,Regions.AngryAztecOasis,Regions.AngryAztecMain];I=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];B=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in G];random.shuffle(B);J=_B
	while len(B)>0:
		Q=B.pop()
		if TryAddingLoadingZoneHint(A,Q,1,G):J=_A;break
	if not J:print(_j)
	C=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in H];random.shuffle(C);K=_B
	while len(C)>0:
		R=C.pop()
		if TryAddingLoadingZoneHint(A,R,1,H):K=_A;break
	if not K:print(_k)
	D=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in I];random.shuffle(D);L=_B
	while len(D)>0:
		S=D.pop()
		if TryAddingLoadingZoneHint(A,S,1,I):L=_A;break
	if not L:print(_l)
	T=[[Regions.BananaFairyRoom],[Regions.GloomyGalleonStart,Regions.LighthousePlatform,Regions.LighthouseUnderwater,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]];U=random.sample(T,3)
	for M in U:
		E=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in M];random.shuffle(E);N=_B
		while len(E)>0:
			O=E.pop()
			if TryAddingLoadingZoneHint(A,O,3,M):N=_A;break
		if not N:print(f"Useful LZR hint to {O.name} unable to be placed!")
	V=[Regions.IslesMain,Regions.IslesMainUpper];P=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId not in V];random.shuffle(P);F=4
	for W in P:
		if F==0:break
		elif TryAddingLoadingZoneHint(A,W,5):F-=1
	if F>0:print('Unable to place remaining LZR hints!')
def TryAddingLoadingZoneHint(spoiler,transition,useful_rating,disallowedRegions=_C):
	'Try to write a hint for the given transition. If this hint is determined to be bad, it will return false and not place the hint.\n\n    NOTE: ONLY USED IN OLD HINT SYSTEM. Functionality was replicated for new hint system elsewhere.\n    ';E=disallowedRegions;D=transition;B=spoiler
	if E is _C:E=[]
	A=D
	if B.settings.decoupled_loading_zones:
		while ShufflableExits[A].category is _C:
			F=[C for(C,D)in B.shuffled_exit_data.items()if D.reverse==A]
			if len(F)==0:break
			A=F[0]
	elif ShufflableExits[A].category is _C:return _B
	if ShufflableExits[A].region in E:return _B
	H=GetMapId(ShufflableExits[A].region);I=GetMapId(B.shuffled_exit_data[D].regionId)
	if H==I:return _B
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(_m)
	if G!=-1:C=C[:G]
	pushHintToList(Hint(hint=f"If you're looking for {C}, follow the path from {J}.",priority=useful_rating,subtype='lzr'));return _A
def TryCreatingLoadingZoneHint(spoiler,transition,disallowedRegions=_C):
	'Try to create a hint message for the given transition. If this hint is determined to be bad, it will return false and not place the hint.';E=disallowedRegions;D=transition;B=spoiler
	if E is _C:E=[]
	A=D
	if B.settings.decoupled_loading_zones:
		while ShufflableExits[A].category is _C:
			F=[C for(C,D)in B.shuffled_exit_data.items()if D.reverse==A]
			if len(F)==0:break
			A=F[0]
	elif ShufflableExits[A].category is _C:return''
	if ShufflableExits[A].region in E:return''
	H=GetMapId(ShufflableExits[A].region);I=GetMapId(B.shuffled_exit_data[D].regionId)
	if H==I:return''
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(_m)
	if G!=-1:C=C[:G]
	return f"If you're looking for {C}, follow the path from {J}."
def UpdateSpoilerHintList(spoiler):
	'Write hints to spoiler object.'
	for A in hints:spoiler.hint_list[A.name]=A.hint