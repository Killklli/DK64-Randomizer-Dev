'Compile a list of hints based on the settings.'
_p=' from '
_o='Factory LZR hint unable to be placed!'
_n='Aztec LZR hint unable to be placed!'
_m='Japes LZR hint unable to be placed!'
_l='Small Banana'
_k='Small Bananas'
_j='puzzle'
_i='locked'
_h='Tiny Temple'
_g='Llama Temple'
_f='Ammo Belt Upgrade'
_e='Gorilla Gone'
_d='Mini Monkey'
_c='Rocketbarrel Boost'
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
from randomizer.Enums.Events import Events
from randomizer.Enums.HintType import HintType
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Types import Types
from randomizer.ItemPool import AllKongMoves
from randomizer.Lists.Item import ItemList,NameFromKong
from randomizer.Lists.Location import LocationList,SharedShopLocations,TrainingBarrelLocations
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Lists.WrinklyHints import hints
from randomizer.Logic import Regions as RegionList
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
moves_data=[MoveInfo(name='Baboon Blast',move_level=1,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Strong Kong',move_level=2,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Gorilla Grab',move_level=3,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Chimpy Charge',move_level=1,move_type=_D,kong=Kongs.diddy),MoveInfo(name=_c,move_level=2,move_type=_D,kong=Kongs.diddy,important=_A),MoveInfo(name='Simian Spring',move_level=3,move_type=_D,kong=Kongs.diddy),MoveInfo(name='Orangstand',move_level=1,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Baboon Balloon',move_level=2,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Orangstand Sprint',move_level=3,move_type=_D,kong=Kongs.lanky),MoveInfo(name=_d,move_level=1,move_type=_D,kong=Kongs.tiny,important=_A),MoveInfo(name='Ponytail Twirl',move_level=2,move_type=_D,kong=Kongs.tiny),MoveInfo(name='Monkeyport',move_level=3,move_type=_D,kong=Kongs.tiny,important=_A),MoveInfo(name='Hunky Chunky',move_level=1,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name='Primate Punch',move_level=2,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name=_e,move_level=3,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name=_V,move_level=1,move_type=_M,kong=Kongs.any),MoveInfo(name=_V,move_level=2,move_type=_M,kong=Kongs.any),MoveInfo(name=_V,move_level=3,move_type=_M,kong=Kongs.any),MoveInfo(name='Coconut Shooter',move_level=1,move_type=_J,kong=Kongs.donkey,important=_A),MoveInfo(name='Peanut Popguns',move_level=1,move_type=_J,kong=Kongs.diddy,important=_A),MoveInfo(name='Grape Shooter',move_level=1,move_type=_J,kong=Kongs.lanky),MoveInfo(name='Feather Bow',move_level=1,move_type=_J,kong=Kongs.tiny,important=_A),MoveInfo(name='Pineapple Launcher',move_level=1,move_type=_J,kong=Kongs.chunky),MoveInfo(name='Homing Ammo',move_level=2,move_type=_J,kong=Kongs.any),MoveInfo(name='Sniper Scope',move_level=3,move_type=_J,kong=Kongs.any),MoveInfo(name=_f,move_level=1,move_type=_T,kong=Kongs.any),MoveInfo(name=_f,move_level=2,move_type=_T,kong=Kongs.any),MoveInfo(name='Bongo Blast',move_level=1,move_type=_I,kong=Kongs.donkey,important=_A),MoveInfo(name='Guitar Gazump',move_level=1,move_type=_I,kong=Kongs.diddy,important=_A),MoveInfo(name='Trombone Tremor',move_level=1,move_type=_I,kong=Kongs.lanky,important=_A),MoveInfo(name='Saxophone Slam',move_level=1,move_type=_I,kong=Kongs.tiny,important=_A),MoveInfo(name='Triangle Trample',move_level=1,move_type=_I,kong=Kongs.chunky,important=_A),MoveInfo(name=_W,move_level=2,move_type=_I,kong=Kongs.any),MoveInfo(name=_W,move_level=3,move_type=_I,kong=Kongs.any),MoveInfo(name=_W,move_level=4,move_type=_I,kong=Kongs.any)]
kong_placement_levels=[{_F:_K,_G:0},{_F:_g,_G:1},{_F:_h,_G:1},{_F:_L,_G:2}]
hint_distribution={HintType.Joke:1,HintType.KRoolOrder:2,HintType.HelmOrder:2,HintType.FullShop:8,HintType.MoveLocation:7,HintType.BLocker:2,HintType.TroffNScoff:0,HintType.KongLocation:1,HintType.Entrance:8,HintType.RequiredKeyHint:-1,HintType.RequiredKRoolHint:0,HintType.WothLocation:8,HintType.FullShopWithItems:4,HintType.FoolishMove:4}
HINT_CAP=35
def compileHints(spoiler):
	'Create a hint distribution, generate buff hints, and place them in locations.';Aq=', then ';Ap='beat_krool';A=spoiler;M=not A.settings.no_logic and A.settings.shuffle_loading_zones!=_X;G=[HintType.Joke]
	if A.settings.krool_phase_count<5 and A.settings.win_condition==Ap:G.append(HintType.KRoolOrder)
	if A.settings.helm_setting!='skip_all'and A.settings.helm_phase_count<5:G.append(HintType.HelmOrder)
	if not A.settings.unlock_all_moves and A.settings.move_rando not in('off','item_shuffle'):G.append(HintType.FullShop);G.append(HintType.MoveLocation)
	if A.settings.shuffle_items and Types.Shop in A.settings.shuffled_location_types:
		G.append(HintType.FullShopWithItems)
		if not A.settings.no_logic:
			G.append(HintType.FoolishMove);G.append(HintType.WothLocation)
			if A.settings.win_condition==Ap:
				G.append(HintType.RequiredKRoolHint)
				if Kongs.diddy in A.settings.krool_order:hint_distribution[HintType.RequiredKRoolHint]+=1
				if Kongs.tiny in A.settings.krool_order:hint_distribution[HintType.RequiredKRoolHint]+=1
				if Kongs.chunky in A.settings.krool_order:hint_distribution[HintType.RequiredKRoolHint]+=1
	if A.settings.randomize_blocker_required_amounts:G.append(HintType.BLocker)
	if A.settings.randomize_cb_required_amounts and len(A.settings.krool_keys_required)>0 and A.settings.krool_keys_required!=[Events.HelmKeyTurnedIn]:G.append(HintType.TroffNScoff)
	if A.settings.kong_rando:G.append(HintType.KongLocation)
	if A.settings.shuffle_loading_zones==_X:Ar=hint_distribution[HintType.BLocker];hint_distribution[HintType.BLocker]=max(1,hint_distribution[HintType.TroffNScoff]);hint_distribution[HintType.TroffNScoff]=Ar;G.append(HintType.Entrance)
	if Types.Key in A.settings.shuffled_location_types:
		G.append(HintType.RequiredKeyHint);AD=0;AE=0;As=[LocationList[B].item for B in A.woth_locations if ItemList[LocationList[B].item].type==Types.Key]
		for b in As:
			if not M and not A.settings.hard_level_progression and b>=Items.JungleJapesKey and b<=Items.AngryAztecKey:AD+=1
			else:AE+=1
		hint_distribution[HintType.RequiredKeyHint]=AD+2*AE
	c=0
	for type in hint_distribution:
		if type in G:c+=hint_distribution[type]
		else:hint_distribution[type]=0
	while c<HINT_CAP:
		AF=random.choice(G)
		if AF in(HintType.RequiredKeyHint,HintType.RequiredKRoolHint):continue
		hint_distribution[AF]+=1;c+=1
	while c>HINT_CAP:
		q=random.choice(G)
		if q in(HintType.RequiredKeyHint,HintType.RequiredKRoolHint):continue
		if hint_distribution[q]>0:hint_distribution[q]-=1;c-=1
	Z=_C
	if M:
		Z=[]
		for D in all_levels:
			for R in A.settings.owned_kongs_by_level[D]:
				if not A.settings.wrinkly_location_rando:
					if D==Levels.FranticFactory and R not in[Kongs.donkey,Kongs.chunky]and(Kongs.donkey not in A.settings.owned_kongs_by_level[D]or Items.GorillaGrab not in A.settings.owned_moves_by_level[D]):continue
					if D==Levels.FungiForest and R is not Kongs.chunky and(Kongs.donkey not in A.settings.owned_kongs_by_level[D]or Items.GorillaGrab not in A.settings.owned_moves_by_level[D]):continue
					if D==Levels.CrystalCaves and R is Kongs.diddy and(Kongs.chunky not in A.settings.owned_kongs_by_level[D]or Items.PrimatePunch not in A.settings.owned_moves_by_level[D]or Items.RocketbarrelBoost not in A.settings.owned_moves_by_level[D]or Items.Barrels not in A.settings.owned_moves_by_level[D]):continue
					if D==Levels.CrystalCaves and(Kongs.chunky not in A.settings.owned_kongs_by_level[D]or Items.PrimatePunch not in A.settings.owned_moves_by_level[D]or Items.Barrels not in A.settings.owned_moves_by_level[D]):continue
					if D==Levels.AngryAztec and R is Kongs.chunky and(Kongs.tiny not in A.settings.owned_kongs_by_level[D]or Items.Feather not in A.settings.owned_moves_by_level[D]or Items.HunkyChunky not in A.settings.owned_moves_by_level[D]):continue
				At=[A for A in hints if A.level==D and A.kong==R][0];Z.append(At)
	AG=[];AH=0
	while AH<hint_distribution[HintType.KongLocation]:
		h=random.choice(kong_placement_levels);K=A.shuffled_kong_placement[h[_F]][_i][_H];AI=A.shuffled_kong_placement[h[_F]][_j][_H];AJ=h[_G];r=_C
		if M and K not in AG:r=[B for B in all_levels if A.settings.EntryGBs[B]<=A.settings.EntryGBs[h[_G]]]
		s=A.settings.starting_kong_list.copy();s.append(AI);B=getRandomHintLocation(kongs=s,levels=r)
		if B is _C:
			if r is not _C:B=getRandomHintLocation(kongs=s)
			else:hint_distribution[HintType.Joke]+=1;hint_distribution[HintType.KongLocation]-=1;continue
		Au=kong_list[AI]
		if A.settings.wrinkly_hints==_E:
			if not K==Kongs.any:a=random.choice(kong_cryptic[K])
			E=random.choice(level_cryptic[AJ])
		else:
			if not K==Kongs.any:a=kong_list[K]
			E=level_list[AJ]
		AK='frees'
		if K==Kongs.any:AK='accesses';a='an empty cage'
		C=f"{Au} {AK} {a} in {E}.";AG.append(K);B.hint_type=HintType.KongLocation;UpdateHint(B,C);AH+=1
	AL=[]
	for I in range(hint_distribution[HintType.BLocker]):
		d=_C
		if M:d=Z
		H=[]
		while len(H)==0:
			B=getRandomHintLocation(location_list=d);H=[C for C in all_levels if(not M or A.settings.EntryGBs[C]>A.settings.EntryGBs[B.level])and(B.level,C)not in AL]
			if not A.settings.maximize_helm_blocker:
				if I==0:H=[Levels.HideoutHelm]
				else:H.append(Levels.HideoutHelm)
		O=random.choice(H);AL.append((B.level,O));E=level_list[O]
		if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic[O])
		C=f"The barrier to {E} can be cleared by obtaining {A.settings.EntryGBs[O]} Golden Bananas.";B.hint_type=HintType.BLocker;UpdateHint(B,C)
	AM=_B
	for I in range(hint_distribution[HintType.HelmOrder]):
		d=_C
		if M and not AM and I==hint_distribution[HintType.HelmOrder]-1:d=Z
		B=getRandomHintLocation(location_list=d)
		if Z is _C or B in Z:AM=_A
		Av=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];Aw=[Av[B]for B in A.settings.helm_order];Ax=[NameFromKong(A)for A in Aw];Ay=Aq.join(Ax);t=f"The Blast-O-Matic can be disabled by using {Ay}.";B.hint_type=HintType.HelmOrder;UpdateHint(B,t)
	if hint_distribution[HintType.RequiredKeyHint]>0:
		i=[LocationList[B].item for B in A.woth_locations if ItemList[LocationList[B].item].type==Types.Key]
		if not M or A.settings.hard_level_progression:AN=i;AO=[]
		else:AO=[A for A in i if A<=Items.AngryAztecKey];AN=[A for A in i if A>Items.AngryAztecKey]
		u={}
		for (J,F) in LocationList.items():
			if F.item in i:u[F.item]=J
		for b in AO:
			F=LocationList[u[b]];e=ItemList[b];K=F.kong
			if F.kong==Kongs.any and F.type==Types.Key:K=A.settings.boss_kongs[F.level]
			if A.settings.wrinkly_hints==_E:
				if F.level==Levels.Shops:E="Cranky's Lab"
				else:E=random.choice(level_cryptic_helm_isles[F.level])
				a=random.choice(kong_cryptic[K])
			else:
				if F.level==Levels.Shops:E=random.choice(crankys_cryptic)
				else:E=level_list_helm_isles[F.level]
				a=kong_list[K]
			H=[]
			for (j,D) in A.settings.level_order.items():
				if j<=e.index:H.append(D)
			B=getRandomHintLocation(levels=H)
			if B is _C:B=getRandomHintLocation()
			C=f"{e.name} can be acquired with {a} in {E}.";B.hint_type=HintType.RequiredKeyHint;UpdateHint(B,C)
		for AP in AN:
			S=A.woth_paths[u[AP]];e=ItemList[AP]
			for I in range(2):
				N=random.choice(S);T=GetRegionOfLocation(N);v=T.hint_name;B=getRandomHintLocation()
				if N in TrainingBarrelLocations:Az=ItemList[LocationList[N].item].name;C=f"Your training with {Az} will aid in unlocking {e.name}."
				else:C=f"Investigating the {v} will aid in unlocking {e.name}."
				B.hint_type=HintType.RequiredKeyHint;UpdateHint(B,C)
	if hint_distribution[HintType.RequiredKRoolHint]>0:
		k={};AQ=_C;AR=_C;AS=_C
		for J in A.woth_paths.keys():
			if LocationList[J].item==Items.RocketbarrelBoost:AQ=J
			if LocationList[J].item==Items.MiniMonkey:AR=J
			if LocationList[J].item==Items.GorillaGone:AS=J
		if Kongs.diddy in A.settings.krool_order:S=A.woth_paths[AQ];N=random.choice(S);T=GetRegionOfLocation(N);k[_c]=T.hint_name
		if Kongs.tiny in A.settings.krool_order:S=A.woth_paths[AR];N=random.choice(S);T=GetRegionOfLocation(N);k[_d]=T.hint_name
		if Kongs.chunky in A.settings.krool_order:S=A.woth_paths[AS];N=random.choice(S);T=GetRegionOfLocation(N);k[_e]=T.hint_name
		for (l,v) in k.items():B=getRandomHintLocation();C=f"Investigating the {v} will aid in your fight against K. Rool.";B.hint_type=HintType.RequiredKRoolHint;UpdateHint(B,C)
	m={};AT=[];w=0
	while w<hint_distribution[HintType.MoveLocation]:
		U=_C;AU=[B for B in A.woth.keys()if B not in AT and any((A in B for A in shop_owners))]
		if len(AU)==0:P=hint_distribution[HintType.MoveLocation]-w;hint_distribution[HintType.Joke]+=P;hint_distribution[HintType.MoveLocation]-=P;break
		f=random.choice(AU);n=level_list_isles.index([A for A in level_list_isles if f[:5]in A][0])
		for x in ItemList:
			if ItemList[x].name==A.woth[f]:
				if x==Items.ProgressiveSlam:continue
				U=x;break
		H=all_levels.copy()
		if M and not A.settings.hard_level_progression:
			AV=all_levels.copy();AV.sort(key=lambda l:A.settings.EntryGBs[l]);H=[];y=[]
			for D in AV:
				if U not in A.settings.owned_moves_by_level[D]:H.append(D)
				else:
					z=[B for B in all_levels if A.settings.EntryGBs[B]==A.settings.EntryGBs[D]and B not in H]
					if len(z)==1 or n>=7:y=z
					else:
						AW=-1
						for j in A.settings.level_order:
							if n==A.settings.level_order[j]:AW=j;break
						for AX in z:
							A_=[B for B in A.settings.level_order if AX==A.settings.level_order[B]][0]
							if A_<=AW:y.append(AX)
					break
			H.extend(y)
		if U in m.keys():
			for AY in m[U]:
				if AY in H:H.remove(AY)
		else:m[U]=[]
		B=getRandomHintLocation(levels=H,move_name=A.woth[f])
		if B is _C:AT.append(f);continue
		AZ=level_list_isles[n]
		if A.settings.wrinkly_hints==_E:AZ=random.choice(level_cryptic_isles[n])
		A0=[A for A in shop_owners if A in f][0];C=f"On the Way of the Hoard, {ItemList[U].name} is bought from {A0} in {AZ}.";m[U].append(B.level);B.hint_type=HintType.MoveLocation;UpdateHint(B,C);w+=1
	if hint_distribution[HintType.TroffNScoff]>0:
		Q=[]
		for V in A.settings.krool_keys_required:
			if V==Events.JapesKeyTurnedIn:Q.append(A.settings.level_order[1])
			if V==Events.AztecKeyTurnedIn:Q.append(A.settings.level_order[2])
			if V==Events.FactoryKeyTurnedIn:Q.append(A.settings.level_order[3])
			if V==Events.GalleonKeyTurnedIn:Q.append(A.settings.level_order[4])
			if V==Events.ForestKeyTurnedIn:Q.append(A.settings.level_order[5])
			if V==Events.CavesKeyTurnedIn:Q.append(A.settings.level_order[6])
			if V==Events.CastleKeyTurnedIn:Q.append(A.settings.level_order[7])
		A1=0
		while A1<hint_distribution[HintType.TroffNScoff]:
			A2=0;A3=[]
			while not any(A3):
				A2+=1
				if A2>15:break
				B=getRandomHintLocation();A3=[C for C in all_levels if C in Q and(not M or A.settings.EntryGBs[C]>=A.settings.EntryGBs[B.level])]
			if A2>15:P=hint_distribution[HintType.TroffNScoff]-A1;hint_distribution[HintType.Joke]+=P;hint_distribution[HintType.TroffNScoff]-=P;break
			O=random.choice(A3);E=level_list[O]
			if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic[O])
			Aa=A.settings.BossBananas[O];Ab=_k
			if Aa==1:Ab=_l
			C=f"The barrier to the boss in {E} can be cleared by obtaining {Aa} {Ab}.";B.hint_type=HintType.TroffNScoff;UpdateHint(B,C);A1+=1
	if hint_distribution[HintType.Entrance]>0:
		A4=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];A5=[Regions.AngryAztecStart,Regions.AngryAztecOasis,Regions.AngryAztecMain];A6=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];B0=[A4,A5,A6,[Regions.BananaFairyRoom],[Regions.TrainingGrounds],[Regions.GloomyGalleonStart,Regions.LighthousePlatform,Regions.LighthouseUnderwater,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]]
		for I in range(hint_distribution[HintType.Entrance]):
			C=''
			if I==0:
				A7=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in A4];random.shuffle(A7);Ac=_B
				while len(A7)>0:
					B1=A7.pop();C=TryCreatingLoadingZoneHint(A,B1,A4)
					if C!='':Ac=_A;break
				if not Ac:print(_m)
			elif I==1:
				A8=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in A5];random.shuffle(A8);Ad=_B
				while len(A8)>0:
					B2=A8.pop();C=TryCreatingLoadingZoneHint(A,B2,A5)
					if C!='':Ad=_A;break
				if not Ad:print(_n)
			elif I==2:
				A9=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in A6];random.shuffle(A9);Ae=_B
				while len(A9)>0:
					B3=A9.pop();C=TryCreatingLoadingZoneHint(A,B3,A6)
					if C!='':Ae=_A;break
				if not Ae:print(_o)
			else:
				Af=random.choice(B0);AA=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in Af];random.shuffle(AA);Ag=_B
				while len(AA)>0:
					Ah=AA.pop();C=TryCreatingLoadingZoneHint(A,Ah,Af)
					if C!='':Ag=_A;break
				if not Ag:print(f"Useful LZR hint to {Ah.name} unable to be placed!")
			B=getRandomHintLocation();B.hint_type=HintType.Entrance;UpdateHint(B,C)
	if hint_distribution[HintType.FullShop]>0:
		o=[]
		for Ai in range(3):
			for D in range(8):
				W=[]
				for R in range(5):
					B4=A.move_data[0][Ai][R][D]
					for AB in moves_data:
						if AB.item_key==B4:
							if AB.name not in W:W.append(AB.name)
				if len(W)==0:continue
				X=W[0]
				if len(W)>1:X=f"{', '.join(W[:-1])} and {W[-1]}"
				A0=shop_owners[Ai];E=level_list_isles[D]
				if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic_isles[D])
				B5=f"{A0}'s in {E} contains {X}";o.append(B5)
		random.shuffle(o);AC=0
		while AC<hint_distribution[HintType.FullShop]:
			B=getRandomHintLocation()
			if len(o)==0:P=hint_distribution[HintType.FullShop]-AC;hint_distribution[HintType.Joke]+=P;hint_distribution[HintType.FullShop]-=P;break
			C=o.pop();B.hint_type=HintType.FullShop;UpdateHint(B,C);AC+=1
	if hint_distribution[HintType.FoolishMove]>0:
		Y=AllKongMoves();Y.append(Items.Shockwave)
		for J in A.woth_locations:
			F=LocationList[J]
			if F.item in Y:Y.remove(F.item)
		B6=2-Y.count(Items.ProgressiveSlam);random.shuffle(Y)
		for I in range(hint_distribution[HintType.FoolishMove]):
			if len(Y)==0:hint_distribution[HintType.FoolishMove]-=1;hint_distribution[HintType.WothLocation]+=1
			Aj=Y.pop()
			if Aj==Items.ProgressiveSlam:
				if B6==0:l='Super Simian Slam'
				else:l='Super Duper Simian Slam'
			else:l=ItemList[Aj].name
			B=getRandomHintLocation();C=f"It would be foolish to seek out {l}.";B.hint_type=HintType.FoolishMove;UpdateHint(B,C)
	if hint_distribution[HintType.WothLocation]>0:
		p=[]
		for J in A.woth_locations:
			F=LocationList[J]
			if F.type in A.settings.shuffled_location_types and F.type!=Types.TrainingBarrel:p.append(F)
		random.shuffle(p)
		for I in range(hint_distribution[HintType.WothLocation]):
			if len(p)==0:hint_distribution[HintType.WothLocation]-=1;hint_distribution[HintType.Joke]+=1;continue
			B7=p.pop();B=getRandomHintLocation();C=f"{B7.name} is on the Way of the Hoard.";B.hint_type=HintType.WothLocation;UpdateHint(B,C)
	Ak=[]
	for I in range(hint_distribution[HintType.FullShopWithItems]):
		Al=random.choice([A for A in SharedShopLocations if A not in Ak]);Ak.append(Al);L=LocationList[Al];Am=[A for(id,A)in LocationList.items()if A.type==Types.Shop and A.level==L.level and A.vendor==L.vendor and A.kong!=Kongs.any]
		if L.item is not _C and L.item!=Items.NoItem:
			An=shop_owners[L.vendor];E=level_list_helm_isles[L.level]
			if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic_helm_isles[L.level])
			X=ItemList[L.item].name
		else:
			random.shuffle(Am);g=[ItemList[A.item].name for A in Am if A.item is not _C and A.item!=Items.NoItem]
			if len(g)==0:X='nothing'
			else:
				X=g[0]
				if len(g)>1:X=f"{', '.join(g[:-1])} and {g[-1]}"
		An=shop_owners[L.vendor];E=level_list_helm_isles[L.level]
		if A.settings.wrinkly_hints==_E:E=random.choice(level_cryptic_helm_isles[L.level])
		B=getRandomHintLocation();C=f"{An}'s in {E} contains {X}.";B.hint_type=HintType.FullShopWithItems;UpdateHint(B,C)
	for I in range(hint_distribution[HintType.KRoolOrder]):B=getRandomHintLocation();B8=[NameFromKong(B)for B in A.settings.krool_order];B9=Aq.join(B8);t=f"King K. Rool will face off in the ring against {B9}.";B.hint_type=HintType.KRoolOrder;UpdateHint(B,t)
	for I in range(hint_distribution[HintType.Joke]):B=getRandomHintLocation();Ao=hint_list.copy();random.shuffle(Ao);C=Ao.pop().hint;B.hint_type=HintType.Joke;UpdateHint(B,C)
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
		A0=A.shuffled_kong_placement;AU=[{_F:_K,_G:0},{_F:_g,_G:1},{_F:_h,_G:1},{_F:_L,_G:2}]
		for l in AU:
			S=A0[l[_F]][_i][_H];AV=A0[l[_F]][_j][_H];L=l[_G]
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
		U=A.settings.BossBananas[C];AG=_k
		if U==1:AG=_l
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
	if not J:print(_m)
	C=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in H];random.shuffle(C);K=_B
	while len(C)>0:
		R=C.pop()
		if TryAddingLoadingZoneHint(A,R,1,H):K=_A;break
	if not K:print(_n)
	D=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in I];random.shuffle(D);L=_B
	while len(D)>0:
		S=D.pop()
		if TryAddingLoadingZoneHint(A,S,1,I):L=_A;break
	if not L:print(_o)
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
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(_p)
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
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(_p)
	if G!=-1:C=C[:G]
	return f"If you're looking for {C}, follow the path from {J}."
def UpdateSpoilerHintList(spoiler):
	'Write hints to spoiler object.'
	for A in hints:spoiler.hint_list[A.name]=A.hint
def GetRegionOfLocation(location_id):
	'Given the id of a Location, return the Region it belongs to.';B=location_id;C=LocationList[B]
	if C.type==Types.Shop:
		for A in [A for(id,A)in RegionList.items()if A.level==Levels.Shops]:
			if B in[B.id for B in A.locations]:return A
	for D in Regions:
		A=RegionList[D]
		if A.level==C.level:
			if B in[B.id for B in A.locations]:return A
	raise Exception('Unable to find Region for Location')