'Compile a list of hints based on the settings.'
_n=' from '
_m='Factory LZR hint unable to be placed!'
_l='Aztec LZR hint unable to be placed!'
_k='Japes LZR hint unable to be placed!'
_j='Small Banana'
_i='Small Bananas'
_h='puzzle'
_g='locked'
_f='need_rw'
_e='need_both'
_d='Tiny Temple'
_c='Llama Temple'
_b='Ammo Belt Upgrade'
_a='Cranky'
_Z='DK Isles'
_Y='Chunky'
_X='Donkey'
_W='all'
_V='Instrument Upgrade'
_U='Slam Upgrade'
_T='Creepy Castle'
_S='Crystal Caves'
_R='Fungi Forest'
_Q='Gloomy Galleon'
_P='Angry Aztec'
_O='ammobelt'
_N='joke'
_M='slam'
_L='Frantic Factory'
_K='Jungle Japes'
_J='gun'
_I='instrument'
_H='kong'
_G='cryptic'
_F='level'
_E='name'
_D='special'
_C=None
_B=False
_A=True
import random
from re import U
from randomizer.Enums.HintType import HintType
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Events import Events
from randomizer.Lists.Item import ItemList,NameFromKong
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Lists.WrinklyHints import hints
from randomizer.Spoiler import Spoiler
from randomizer.Patching.UpdateHints import UpdateHint,updateRandomHint
from randomizer.Lists.WrinklyHints import HintLocation,hints
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Transitions import Transitions
class Hint:
	'Hint object for Wrinkly hint text.'
	def __init__(A,*,hint='',important=_A,priority=1,kongs=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],repeats=1,base=_B,keywords=[],permitted_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle],subtype=_N,joke=_B,joke_defined=_B):
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
		'Create move info object.';C=move_level;A.name=name;A.kong=kong;E=[_D,_M,_J,_O,_I];D=E.index(move_type);A.move_type=D;A.move_level=C;A.important=important;B=kong
		if B==Kongs.any:B=Kongs.donkey
		A.item_key=D<<5|C-1<<3|B
hint_list=[Hint(hint='Did you know - Donkey Kong officially features in Donkey Kong 64.',important=_B,base=_A),Hint(hint='Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.',important=_B,base=_A),Hint(hint='Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.',important=_B,base=_A),Hint(hint='Tiny Kong is the youngest sister of Dixie Kong.',important=_B,base=_A),Hint(hint='Mornin.',important=_B,base=_A),Hint(hint='Lanky Kong is the only kong with no canonical relation to the main Kong family tree.',important=_B,base=_A),Hint(hint='Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.',important=_B,base=_A),Hint(hint='Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.',important=_B,base=_A),Hint(hint='Candy Kong does not appear in Jungle Japes or Fungi Forest.',important=_B,base=_A),Hint(hint='If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.',important=_B,base=_A),Hint(hint='Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.',important=_B,base=_A),Hint(hint='The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.',important=_B,base=_A),Hint(hint='Chunky Kong is the brother of Kiddy Kong.',important=_B,base=_A),Hint(hint='Fungi Forest contains mushrooms.',important=_B,base=_A),Hint(hint='Igloos can be found in Crystal Caves.',important=_B,base=_A),Hint(hint='Frantic Factory has multiple floors where things can be found.',important=_B,base=_A),Hint(hint="Angry Aztec has so much sand, it's even in the wind.",important=_B,base=_A),Hint(hint='DK Isles does not have a key.',important=_B,base=_A),Hint(hint='You can find a rabbit in Fungi Forest and in Crystal Caves.',important=_B,base=_A),Hint(hint='You can find a beetle in Angry Aztec and in Crystal Caves.',important=_B,base=_A),Hint(hint='You can find a vulture in Angry Aztec.',important=_B,base=_A),Hint(hint='You can find an owl in Fungi Forest.',important=_B,base=_A),Hint(hint='To buy moves, you will need coins.',important=_B,base=_A),Hint(hint='You can change the music and sound effects volume in the sound settings on the main menu.',important=_B,base=_A),Hint(hint='Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.',important=_B,base=_A),Hint(hint='Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.',important=_B,base=_A),Hint(hint='I have nothing to say to you.',important=_B,base=_A),Hint(hint='I had something to tell you, but I forgot what it is.',important=_B,base=_A),Hint(hint="I don't know anything.",important=_B,base=_A),Hint(hint="I'm as lost as you are. Good luck!",important=_B,base=_A),Hint(hint='Wrinkly? Never heard of him.',important=_B,base=_A),Hint(hint='This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.',important=_B,base=_A),Hint(hint='Why do they call it oven when you of in the cold food of out hot eat the food?',important=_B,base=_A),Hint(hint='Wanna become famous? Buy followers, coconuts and donks at DK64Randomizer (DK64Randomizer . com)!',important=_B,base=_A),Hint(hint='What you gonna do, SpikeVegeta?',important=_B,base=_A)]
kong_list=[_X,'Diddy','Lanky','Tiny',_Y]
kong_cryptic=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']]
all_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
level_list=[_K,_P,_L,_Q,_R,_S,_T,'Hideout Helm']
level_list_isles=[_K,_P,_L,_Q,_R,_S,_T,_Z]
level_cryptic=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with four vases','The level with two kongs cages','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with a game from 1981','The level where you need two quarters to play'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level with two inches of water','The level with two ice shields','The level with an Ice Tomato'],['The level with battlements','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']]
level_cryptic_isles=level_cryptic.copy()
level_cryptic_isles.remove(level_cryptic_isles[-1])
level_cryptic_isles.append(['The hub world',"The world with DK's ugly mug on it","The world with only a Cranky's Lab and Snide's HQ in it"])
shop_owners=[_a,'Funky','Candy']
shop_cryptic=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
moves_data=[MoveInfo(name='Baboon Blast',move_level=1,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Strong Kong',move_level=2,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Gorilla Grab',move_level=3,move_type=_D,kong=Kongs.donkey),MoveInfo(name='Chimpy Charge',move_level=1,move_type=_D,kong=Kongs.diddy),MoveInfo(name='Rocketbarrel Boost',move_level=2,move_type=_D,kong=Kongs.diddy,important=_A),MoveInfo(name='Simian Spring',move_level=3,move_type=_D,kong=Kongs.diddy),MoveInfo(name='Orangstand',move_level=1,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Baboon Balloon',move_level=2,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Orangstand Sprint',move_level=3,move_type=_D,kong=Kongs.lanky),MoveInfo(name='Mini Monkey',move_level=1,move_type=_D,kong=Kongs.tiny,important=_A),MoveInfo(name='Ponytail Twirl',move_level=2,move_type=_D,kong=Kongs.tiny),MoveInfo(name='Monkeyport',move_level=3,move_type=_D,kong=Kongs.tiny,important=_A),MoveInfo(name='Hunky Chunky',move_level=1,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name='Primate Punch',move_level=2,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name='Gorilla Gone',move_level=3,move_type=_D,kong=Kongs.chunky,important=_A),MoveInfo(name=_U,move_level=1,move_type=_M,kong=Kongs.any),MoveInfo(name=_U,move_level=2,move_type=_M,kong=Kongs.any),MoveInfo(name=_U,move_level=3,move_type=_M,kong=Kongs.any),MoveInfo(name='Coconut Shooter',move_level=1,move_type=_J,kong=Kongs.donkey,important=_A),MoveInfo(name='Peanut Popguns',move_level=1,move_type=_J,kong=Kongs.diddy,important=_A),MoveInfo(name='Grape Shooter',move_level=1,move_type=_J,kong=Kongs.lanky),MoveInfo(name='Feather Bow',move_level=1,move_type=_J,kong=Kongs.tiny,important=_A),MoveInfo(name='Pineapple Launcher',move_level=1,move_type=_J,kong=Kongs.chunky),MoveInfo(name='Homing Ammo',move_level=2,move_type=_J,kong=Kongs.any),MoveInfo(name='Sniper Scope',move_level=3,move_type=_J,kong=Kongs.any),MoveInfo(name=_b,move_level=1,move_type=_O,kong=Kongs.any),MoveInfo(name=_b,move_level=2,move_type=_O,kong=Kongs.any),MoveInfo(name='Bongo Blast',move_level=1,move_type=_I,kong=Kongs.donkey,important=_A),MoveInfo(name='Guitar Gazump',move_level=1,move_type=_I,kong=Kongs.diddy,important=_A),MoveInfo(name='Trombone Tremor',move_level=1,move_type=_I,kong=Kongs.lanky,important=_A),MoveInfo(name='Saxophone Slam',move_level=1,move_type=_I,kong=Kongs.tiny,important=_A),MoveInfo(name='Triangle Trample',move_level=1,move_type=_I,kong=Kongs.chunky,important=_A),MoveInfo(name=_V,move_level=2,move_type=_I,kong=Kongs.any),MoveInfo(name=_V,move_level=3,move_type=_I,kong=Kongs.any),MoveInfo(name=_V,move_level=4,move_type=_I,kong=Kongs.any)]
kong_placement_levels=[{_E:_K,_F:0},{_E:_c,_F:1},{_E:_d,_F:1},{_E:_L,_F:2}]
hint_distribution={HintType.Joke:1,HintType.KRoolOrder:2,HintType.HelmOrder:3,HintType.FullShop:8,HintType.MoveLocation:8,HintType.DirtPatch:0,HintType.BLocker:3,HintType.TroffNScoff:0,HintType.KongLocation:2,HintType.MedalsRequired:1,HintType.Entrance:8}
HINT_CAP=35
def compileHints(spoiler):
	'Create a hint distribution, generate buff hints, and place them in locations.';A=spoiler;F=[HintType.Joke]
	if A.settings.krool_phase_count<5:F.append(HintType.KRoolOrder)
	if A.settings.helm_setting!='skip_all'and A.settings.helm_phase_count<5:F.append(HintType.HelmOrder)
	if not A.settings.unlock_all_moves:F.append(HintType.FullShop);F.append(HintType.MoveLocation)
	if A.settings.random_patches:F.append(HintType.DirtPatch)
	if A.settings.randomize_blocker_required_amounts:F.append(HintType.BLocker)
	if A.settings.randomize_cb_required_amounts:F.append(HintType.TroffNScoff)
	if A.settings.kong_rando:F.append(HintType.KongLocation)
	if A.settings.coin_door_open==_e or A.settings.coin_door_open==_f:F.append(HintType.MedalsRequired)
	if A.settings.shuffle_loading_zones==_W:AB=hint_distribution[HintType.BLocker];hint_distribution[HintType.BLocker]=max(1,hint_distribution[HintType.TroffNScoff]);hint_distribution[HintType.TroffNScoff]=AB;F.append(HintType.Entrance)
	R=0
	for type in hint_distribution:
		if type in F:R+=hint_distribution[type]
		else:hint_distribution[type]=0
	while R<HINT_CAP:AC=random.choice(F);hint_distribution[AC]+=1;R+=1
	while R>HINT_CAP:
		p=random.choice(F)
		if hint_distribution[p]>0:hint_distribution[p]-=1;R-=1
	P=A.settings.shuffle_loading_zones!=_W;Q=_C
	if P:
		Q=[]
		for C in all_levels:
			for K in A.settings.owned_kongs_by_level[C]:
				if C==Levels.FranticFactory and K not in[Kongs.donkey,Kongs.chunky]and(Kongs.donkey not in A.settings.owned_kongs_by_level[C]or Items.GorillaGrab not in A.settings.owned_moves_by_level[C]):continue
				if C==Levels.FungiForest and K is not Kongs.chunky and(Kongs.donkey not in A.settings.owned_kongs_by_level[C]or Items.GorillaGrab not in A.settings.owned_moves_by_level[C]):continue
				if C==Levels.CrystalCaves and K is Kongs.diddy and(Kongs.chunky not in A.settings.owned_kongs_by_level[C]or Items.PrimatePunch not in A.settings.owned_moves_by_level[C]or Items.RocketbarrelBoost not in A.settings.owned_moves_by_level[C]):continue
				if C==Levels.CrystalCaves and(Kongs.chunky not in A.settings.owned_kongs_by_level[C]or Items.PrimatePunch not in A.settings.owned_moves_by_level[C]):continue
				if C==Levels.AngryAztec and K is Kongs.chunky and(Kongs.tiny not in A.settings.owned_kongs_by_level[C]or Items.Feather not in A.settings.owned_moves_by_level[C]or Items.HunkyChunky not in A.settings.owned_moves_by_level[C]):continue
				AD=[A for A in hints if A.level==C and A.kong==K][0];Q.append(AD)
	q=[]
	for E in range(hint_distribution[HintType.KongLocation]):
		W=random.choice(kong_placement_levels);L=A.shuffled_kong_placement[W[_E]][_g][_H];r=A.shuffled_kong_placement[W[_E]][_h][_H];s=W[_F];b=_C
		if P and L not in q:b=[B for B in all_levels if A.settings.EntryGBs[B]<=A.settings.EntryGBs[W[_F]]]
		t=A.settings.starting_kong_list.append(r);B=getRandomHintLocation(kongs=t,levels=b)
		if B is _C:
			if b is not _C:B=getRandomHintLocation(kongs=t)
			else:hint_distribution[HintType.Joke]+=1;hint_distribution[HintType.KongLocation]-=1;E-=1;continue
		AE=kong_list[r]
		if A.settings.wrinkly_hints==_G:
			if not L==Kongs.any:c=random.choice(kong_cryptic[L])
			H=random.choice(level_cryptic[s])
		else:
			if not L==Kongs.any:c=kong_list[L]
			H=level_list[s]
		u='frees'
		if L==Kongs.any:u='accesses';c='an empty cage'
		D=f"{AE} {u} {c} in {H}.";q.append(L);B.hint_type=HintType.KongLocation;UpdateHint(B,D)
	v=[]
	for E in range(hint_distribution[HintType.BLocker]):
		S=_C
		if P:S=Q
		G=[]
		while len(G)==0:
			B=getRandomHintLocation(location_list=S);G=[C for C in all_levels if(not P or A.settings.EntryGBs[C]>A.settings.EntryGBs[B.level])and(B.level,C)not in v]
			if not A.settings.maximize_helm_blocker:
				if E==0:G=[Levels.HideoutHelm]
				else:G.append(Levels.HideoutHelm)
		I=random.choice(G);v.append((B.level,I));H=level_list[I]
		if A.settings.wrinkly_hints==_G:H=random.choice(level_cryptic[I])
		D=f"The barrier to {H} can be cleared by obtaining {A.settings.EntryGBs[I]} Golden Bananas.";B.hint_type=HintType.BLocker;UpdateHint(B,D)
	w=_B
	for E in range(hint_distribution[HintType.HelmOrder]):
		S=_C
		if P and not w and E==hint_distribution[HintType.HelmOrder]-1:S=Q
		B=getRandomHintLocation(location_list=S)
		if Q is _C or B in Q:w=_A
		AF=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];X=[]
		for AG in A.settings.helm_order:X.append(AF[AG])
		T=f"Helm Room order is {NameFromKong(X[0])}"
		for U in range(len(X)):
			if U!=0:T+=f" then {NameFromKong(X[U])}"
		B.hint_type=HintType.HelmOrder;UpdateHint(B,T)
	Y={};x=[]
	for E in range(hint_distribution[HintType.MoveLocation]):
		M=_C;y=[B for B in A.woth.keys()if B not in x and any((A in B for A in shop_owners))]
		if len(y)==0:hint_distribution[HintType.Joke]+=hint_distribution[HintType.MoveLocation]-E;hint_distribution[HintType.MoveLocation]=hint_distribution[HintType.MoveLocation]-E;break
		Z=random.choice(y);a=level_list_isles.index([A for A in level_list_isles if Z[:5]in A][0])
		for z in ItemList.values():
			if z.name==A.woth[Z]:M=z;break
		G=all_levels.copy()
		if A.settings.owned_moves_by_level is not _C:
			for C in A.settings.owned_moves_by_level:
				if M in A.settings.owned_moves_by_level[C]:G.remove(C)
			if a<7:G.append(all_levels[a])
			if G==[]:
				V=[Levels.JungleJapes]
				for C in all_levels:
					if A.settings.EntryGBs[C]<A.settings.EntryGBs[V[0]]:V=[C]
					elif A.settings.EntryGBs[C]==A.settings.EntryGBs[V[0]]:V.append[C]
				G=V
		if M in Y.keys()and Y[M]in G:G.remove(Y[M])
		B=getRandomHintLocation(levels=G)
		if B is _C:x.append(Z);E-=1;continue
		d=level_list_isles[a]
		if A.settings.wrinkly_hints==_G:d=random.choice(level_cryptic_isles[a])
		e=[A for A in shop_owners if A in Z][0];D=f"On the Way of the Hoard, {M.name} is bought from {e} in {d}.";Y[M]=d;B.hint_type=HintType.MoveLocation;UpdateHint(B,D)
	for E in range(hint_distribution[HintType.TroffNScoff]):
		J=[]
		for N in A.settings.krool_keys_required:
			if N==Events.JapesKeyTurnedIn:J.append(Levels.JungleJapes)
			if N==Events.AztecKeyTurnedIn:J.append(Levels.AngryAztec)
			if N==Events.FactoryKeyTurnedIn:J.append(Levels.FranticFactory)
			if N==Events.GalleonKeyTurnedIn:J.append(Levels.GloomyGalleon)
			if N==Events.ForestKeyTurnedIn:J.append(Levels.FungiForest)
			if N==Events.CavesKeyTurnedIn:J.append(Levels.CrystalCaves)
			if N==Events.CastleKeyTurnedIn:J.append(Levels.CreepyCastle)
		f=[]
		while not any(f):B=getRandomHintLocation();f=[C for C in all_levels if C in J and(not P or A.settings.EntryGBs[C]>=A.settings.EntryGBs[B.level])]
		I=random.choice(f);H=level_list[I]
		if A.settings.wrinkly_hints==_G:H=random.choice(level_cryptic[I])
		A0=A.settings.BossBananas[I];A1=_i
		if A0==1:A1=_j
		D=f"The barrier to the boss in {H} can be cleared by obtaining {A0} {A1}.";B.hint_type=HintType.TroffNScoff;UpdateHint(B,D)
	if hint_distribution[HintType.Entrance]>0:
		g=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];h=[Regions.AngryAztecStart,Regions.AngryAztecMain];i=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];AH=[g,h,i,[Regions.BananaFairyRoom],[Regions.TrainingGrounds],[Regions.GloomyGalleonStart,Regions.LighthouseArea,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]]
		for E in range(hint_distribution[HintType.Entrance]):
			D=''
			if E==0:
				j=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in g];random.shuffle(j);A2=_B
				while len(j)>0:
					AI=j.pop();D=TryCreatingLoadingZoneHint(A,AI,g)
					if D!='':A2=_A;break
				if not A2:print(_k)
			elif E==1:
				k=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in h];random.shuffle(k);A3=_B
				while len(k)>0:
					AJ=k.pop();D=TryCreatingLoadingZoneHint(A,AJ,h)
					if D!='':A3=_A;break
				if not A3:print(_l)
			elif E==2:
				l=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in i];random.shuffle(l);A4=_B
				while len(l)>0:
					AK=l.pop();D=TryCreatingLoadingZoneHint(A,AK,i)
					if D!='':A4=_A;break
				if not A4:print(_m)
			else:
				A5=random.choice(AH);m=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in A5];random.shuffle(m);A6=_B
				while len(m)>0:
					A7=m.pop();D=TryCreatingLoadingZoneHint(A,A7,A5)
					if D!='':A6=_A;break
				if not A6:print(f"Useful LZR hint to {A7.name} unable to be placed!")
			B=getRandomHintLocation();B.hint_type=HintType.Entrance;UpdateHint(B,D)
	if hint_distribution[HintType.FullShop]>0:
		n=[]
		for A8 in range(3):
			for C in range(8):
				O=[]
				for K in range(5):
					AL=A.move_data[A8][K][C]
					for o in moves_data:
						if o.item_key==AL:
							if o.name not in O:O.append(o.name)
				if len(O)==0:continue
				A9=O[0]
				if len(O)>1:A9=f"{', '.join(O[:-1])} and {O[-1]}"
				e=shop_owners[A8];H=level_list_isles[C]
				if A.settings.wrinkly_hints==_G:H=random.choice(level_cryptic_isles[C])
				AM=f"{e}'s in {H} contains {A9}";n.append(AM)
		random.shuffle(n)
		for E in range(hint_distribution[HintType.FullShop]):B=getRandomHintLocation();D=n.pop();B.hint_type=HintType.FullShop;UpdateHint(B,D)
	for E in range(hint_distribution[HintType.KRoolOrder]):
		B=getRandomHintLocation();T=f"K. Rool order is {NameFromKong(A.settings.krool_order[0])}"
		for U in range(len(A.settings.krool_order)):
			if U!=0:T+=f" then {NameFromKong(A.settings.krool_order[U])}"
		B.hint_type=HintType.KRoolOrder;UpdateHint(B,T)
	for E in range(hint_distribution[HintType.DirtPatch]):AN=random.choice(A.dirt_patch_placement);B=getRandomHintLocation();D=f"There is a dirt patch located at {AN}";B.hint_type=HintType.DirtPatch;UpdateHint(B,D)
	for E in range(hint_distribution[HintType.MedalsRequired]):B=getRandomHintLocation();D=f"{A.settings.medal_requirement} medals are required to access Jetpac.";B.hint_type=HintType.MedalsRequired;UpdateHint(B,D)
	for E in range(hint_distribution[HintType.Joke]):B=getRandomHintLocation();AA=hint_list.copy();random.shuffle(AA);D=AA.pop().hint;B.hint_type=HintType.Joke;UpdateHint(B,D)
	UpdateSpoilerHintList(A);A.hint_distribution=hint_distribution;return _A
def getRandomHintLocation(location_list=_C,kongs=_C,levels=_C):
	'Return an unoccupied hint location. The parameters can be used to specify location requirements.';D=levels;C=kongs;B=location_list;A=[A for A in hints if A.hint==''and(B is _C or A in B)and(C is _C or A.kong in C)and(D is _C or A.level in D)]
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
	'Push hints to hint list based on settings. Old method that is now unused.';AN='important';AM='k_rool';t='moves';c='levels';b='hint';P='color';A=spoiler;resetHintList()
	if A.settings.krool_phase_order_rando and len(A.settings.krool_order)>1:
		Q=f"K. Rool order is {NameFromKong(A.settings.krool_order[0])}"
		for C in range(len(A.settings.krool_order)):
			if C!=0:Q+=f" then {NameFromKong(A.settings.krool_order[C])}"
		hint_list.append(Hint(hint=Q,repeats=2,kongs=A.settings.krool_order.copy(),subtype=AM))
	AO=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];R=[]
	if A.settings.helm_phase_order_rando and len(A.settings.helm_order)>1:
		for AP in A.settings.helm_order:R.append(AO[AP])
		Q=f"Helm Room order is {NameFromKong(R[0])}"
		for C in range(len(R)):
			if C!=0:Q+=f" then {NameFromKong(R[C])}"
		hint_list.append(Hint(hint=Q,repeats=3,kongs=R.copy(),subtype=AM))
	if A.settings.shuffle_items==t and A.move_data is not _C:
		AQ=[0,2,1,1,4];AR=0
		for C in A.settings.krool_order:AR+=AQ[C]
		u=[]
		for d in range(3):
			v=[]
			for G in range(8):
				e=[]
				for AS in range(5):
					AT=A.move_data[d][AS][G]
					for K in moves_data:
						if K.item_key==AT:
							if K.name not in e:e.append(K.name)
				v.append(e)
			u.append(v)
		f=[];g=[]
		for (h,d) in enumerate(u):
			for (L,G) in enumerate(d):
				for K in G:
					w=_B
					for x in moves_data:
						if x.name==K and x.important:w=_A
					i=shop_owners[h];D=level_list_isles[L]
					if A.settings.wrinkly_hints==_G:D=random.choice(level_cryptic_isles[L])
					g.append({b:f"{K} can be purchased from {i} in {D}",AN:w,'move':K})
				if len(G)>0:
					i=shop_owners[h];D=level_list_isles[L]
					if A.settings.wrinkly_hints==_G:D=random.choice(level_cryptic_isles[L])
					y=G[0]
					if len(G)>1:y=f"{', '.join(G[:-1])} and {G[-1]}"
					AU=f"{i}'s in {D} contains {y}";f.append({b:AU,t:G})
		random.shuffle(f);j=[3,6,10];W=1;z=_A
		for A0 in f:
			if z:hint_list.append(Hint(hint=A0[b],important=_B,keywords=A0[t],subtype='shop_dump'))
			if W<=len(j):
				if h+1>=j[W-1]:
					if W==len(j):z=_B
					else:W+=1
		random.shuffle(g)
		for k in g:hint_list.append(Hint(hint=k[b],priority=2,important=k[AN],keywords=[k['move']],subtype='move_location'))
	if A.settings.kong_rando:
		A1=A.shuffled_kong_placement;AV=[{_E:_K,_F:0},{_E:_c,_F:1},{_E:_d,_F:1},{_E:_L,_F:2}]
		for l in AV:
			S=A1[l[_E]][_g][_H];AW=A1[l[_E]][_h][_H];L=l[_F]
			if A.settings.wrinkly_hints==_G:
				if not S==Kongs.any:m=random.choice(kong_cryptic[S])
				D=random.choice(level_cryptic[L])
			else:
				if not S==Kongs.any:m=kong_list[S]
				D=level_list[L]
			A2=2
			if S==Kongs.any:m='An empty cage';A2=3
			hint_list.append(Hint(hint=f"{m} can be found in {D}.",kongs=[AW],priority=A2,subtype='kong_location'))
	if A.settings.random_patches:
		X={_Z:0,_K:0,_P:0,_L:0,_Q:0,_R:0,_S:0,_T:0}
		for AX in A.dirt_patch_placement:
			for G in X:
				if G in AX:X[G]+=1
		A3=list(X.keys());random.shuffle(A3)
		for Y in range(2):
			for T in range(4):
				D=A3[T+4*Y];n=X[D]
				if n>0:
					A4='patches';A5='are'
					if n==1:A4='patch';A5='is'
					o=f"There {A5} {n} {A4} in {D}";hint_list.append(Hint(hint=o,priority=T+3,important=_B,subtype='level_patch_count'))
		A6=A.dirt_patch_placement.copy();random.shuffle(A6)
		for Y in range(2):
			for T in range(4):AY=A6[T+Y*4];o=f"There is a dirt patch located at {AY}";hint_list.append(Hint(hint=o,priority=T+4,important=Y==0,subtype='patch_location'))
	if A.settings.shuffle_loading_zones==_W:AddLoadingZoneHints(A)
	if A.settings.coin_door_open==_e or A.settings.coin_door_open==_f:hint_list.append(Hint(hint=f"{A.settings.medal_requirement} medals are required to access Jetpac.",priority=4,subtype='medal'))
	if A.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.',subtype='permadeath'))
	if A.settings.level_randomization!='level_order':
		for C in A.settings.krool_keys_required:
			A7=C-4
			if A.settings.wrinkly_hints==_G:D=random.choice(level_cryptic[A7])
			else:D=level_list[A7]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {D} to fight your greatest foe.",important=_B,subtype='key_is_required'))
	AZ=['Candy','Funky',_a];Aa=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];A8=[B for B in A.woth.keys()if any((A in B for A in AZ))];Ab=random.sample(A8,min(5,len(A8)));A9=random.randint(1,4)
	for AA in Ab:
		AB=[A for A in Aa if A in AA]
		if len(AB)>0:Ac=str(AA).removesuffix(AB[0])
		hint_list.append(Hint(hint=f"{Ac} is on the Way of the Hoard.",important=random.choice([_A,_A,_B]),priority=A9,subtype='way_of_the_hoard'));A9+=random.randint(1,2)
	Ad=[{_H:_X,P:'Yellow'},{_H:'Diddy',P:'Red'},{_H:'Lanky',P:'Blue'},{_H:'Tiny',P:'Purple'},{_H:_Y,P:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {level_list[random.randint(0,6)]}, but also in other levels.",important=_B,subtype=_N,joke=_A,joke_defined=_A));AC=random.choice(Ad);hint_list.append(Hint(hint=f"{AC[_H]} can find {AC[P]} bananas in {random.choice(level_list)}.",important=_B,subtype=_N,joke=_A,joke_defined=_A));hint_list.append(Hint(hint=f"{A.settings.krool_key_count} Keys are required to reach K. Rool.",important=_B,subtype='key_count_required'))
	if A.settings.shuffle_loading_zones==c:
		Ae={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};Af={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle};p={};Z={};AD=[]
		for (Ag,AE) in Ae.items():AF=Af[A.shuffled_exit_data[Ag].reverse];p[AF]=AE;Z[AE]=AF
	if A.settings.randomize_blocker_required_amounts is _A and A.settings.shuffle_loading_zones==c:
		for Ah in list(Z.values()):AD.append(Ah.name)
		for C in range(8):
			U=A.settings.EntryGBs[C];AG='Golden Bananas'
			if U==1:AG='Golden Banana'
			D=level_list[C];q=_B;M=all_levels.copy();N=C+1
			if A.settings.shuffle_loading_zones==c:
				if C!=7:
					r=p[C];M=[]
					for V in range(7):
						if V<r:M.append(Z[V])
					if D.replace(' ','')in AD[4:7]:N=4;q=_A
				if A.settings.maximize_helm_blocker is _B and C==7:N=1;q=_A
			if A.settings.wrinkly_hints==_G:D=random.choice(level_cryptic[C])
			hint_list.append(Hint(hint=f"The barrier to {D} can be cleared by obtaining {U} {AG}.",important=q,priority=N,permitted_levels=M.copy(),subtype='gb_amount'))
	for C in range(7):
		U=A.settings.BossBananas[C];AH=_i
		if U==1:AH=_j
		if A.settings.wrinkly_hints==_G:D=random.choice(level_cryptic[C])
		else:D=level_list[C]
		M=all_levels.copy()
		if A.settings.shuffle_loading_zones==c:
			r=p[C];M=[]
			for V in range(7):
				if V<=r:M.append(Z[V])
		hint_list.append(Hint(hint=f"The barrier to the boss in {D} can be cleared by obtaining {U} {AH}.",important=_B,permitted_levels=M.copy(),subtype='cb_amount'))
	H={};F=[]
	for B in hint_list:
		if not B.important and not B.used and B.joke:F.append(B)
	O=random.choice(F);J=_B;Ai=0
	while not J:
		J=updateRandomHint(O.hint,O.kongs.copy(),O.keywords.copy(),O.permitted_levels.copy())
		if J:
			O.use_hint();Ai+=1;E=O.subtype
			if E in H:H[E]+=1
			else:H[E]=1
			break
	random.shuffle(hint_list);N=1;AI=_B;Aj=0
	while not AI:
		AJ=_B
		for B in hint_list:
			if B.important and B.priority==N and not B.used and not B.joke:
				AJ=_A;J=updateRandomHint(B.hint,B.kongs.copy(),B.keywords.copy(),B.permitted_levels.copy())
				if J:
					B.use_hint();Aj+=1;E=B.subtype
					if E in H:H[E]+=1
					else:H[E]=1
				else:B.downgrade()
		if not AJ:AI=_A
		N+=1
	F=[];a=0
	for B in hint_list:
		if not B.important and not B.used and not B.joke:F.append(B)
	for B in hints:
		if B.hint=='':a+=1
	random.shuffle(F);Ak=0;Al=0
	if a>0:
		s=0;AK=100;I=0
		while s<a:
			J=_B
			if not F[I].used:J=updateRandomHint(F[I].hint,F[I].kongs,F[I].keywords.copy(),F[I].permitted_levels.copy())
			if J:
				F[I].use_hint();Ak+=1;E=F[I].subtype
				if E in H:H[E]+=1
				else:H[E]=1
				s+=1
			else:AK-=1
			I+=1
			if I>=len(F):I=0
			if AK==0:
				AL=[]
				for B in hint_list:
					if not B.joke:AL.append(B.hint)
				for B in hints:
					if B.hint=='':B.hint=random.choice(AL)
				for B in hints:
					if B.hint=='':
						B.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.';E='error'
						if E in H:H[E]+=1
						else:H[E]=1
						Al+=1
				s=a
	UpdateSpoilerHintList(A);return _A
def AddLoadingZoneHints(spoiler):
	'Add hints for loading zone transitions and their destinations.';A=spoiler;G=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];H=[Regions.AngryAztecStart,Regions.AngryAztecMain];I=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];B=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in G];random.shuffle(B);J=_B
	while len(B)>0:
		Q=B.pop()
		if TryAddingLoadingZoneHint(A,Q,1,G):J=_A;break
	if not J:print(_k)
	C=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in H];random.shuffle(C);K=_B
	while len(C)>0:
		R=C.pop()
		if TryAddingLoadingZoneHint(A,R,1,H):K=_A;break
	if not K:print(_l)
	D=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in I];random.shuffle(D);L=_B
	while len(D)>0:
		S=D.pop()
		if TryAddingLoadingZoneHint(A,S,1,I):L=_A;break
	if not L:print(_m)
	T=[[Regions.BananaFairyRoom],[Regions.GloomyGalleonStart,Regions.LighthouseArea,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]];U=random.sample(T,3)
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
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(_n)
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
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(_n)
	if G!=-1:C=C[:G]
	return f"If you're looking for {C}, follow the path from {J}."
def UpdateSpoilerHintList(spoiler):
	'Write hints to spoiler object.'
	for A in hints:spoiler.hint_list[A.name]=A.hint