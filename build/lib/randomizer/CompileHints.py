'Compile a list of hints based on the settings.'
_I='ammobelt'
_H='joke'
_G='slam'
_F=None
_E='gun'
_D='instrument'
_C='special'
_B=True
_A=False
import random
from re import U
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.Lists.Item import NameFromKong
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Lists.WrinklyHints import hints
from randomizer.Spoiler import Spoiler
from randomizer.Patching.UpdateHints import updateRandomHint
from randomizer.Lists.WrinklyHints import HintLocation,hints
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Transitions import Transitions
class Hint:
	'Hint object for Wrinkly hint text.'
	def __init__(A,*,hint='',important=_B,priority=1,kongs=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],repeats=1,base=_A,keywords=[],permitted_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle],subtype=_H,joke=_A,joke_defined=_A):
		'Create wrinkly hint text object.';D=repeats;C=priority;B=important;A.kongs=kongs.copy();A.hint=hint;A.important=B;A.priority=C;A.repeats=D;A.base=base;A.used=_A;A.was_important=B;A.original_repeats=D;A.original_priority=C;A.keywords=keywords.copy();A.permitted_levels=permitted_levels.copy();A.subtype=subtype;A.joke=base
		if joke_defined:A.joke=joke
	def use_hint(A):
		'Set hint as used.'
		if A.repeats==1:A.used=_B;A.repeats=0
		else:A.repeats-=1;A.priority+=1
	def downgrade(A):'Downgrade hint status.';A.important=_A
class MoveInfo:
	'Move Info for Wrinkly hint text.'
	def __init__(A,*,name='',kong='',move_type='',move_level=0,important=_A):
		'Create move info object.';C=move_level;A.name=name;A.kong=kong;E=[_C,_G,_E,_I,_D];D=E.index(move_type);A.move_type=D;A.move_level=C;A.important=important;B=kong
		if B==Kongs.any:B=Kongs.donkey
		A.item_key=D<<5|C-1<<3|B
hint_list=[Hint(hint='Did you know - Donkey Kong officially features in Donkey Kong 64.',important=_A,base=_B),Hint(hint='Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.',important=_A,base=_B),Hint(hint='Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.',important=_A,base=_B),Hint(hint='Tiny Kong is the youngest sister of Dixie Kong.',important=_A,base=_B),Hint(hint='Mornin.',important=_A,base=_B),Hint(hint='Lanky Kong is the only kong with no canonical relation to the main Kong family tree.',important=_A,base=_B),Hint(hint='Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.',important=_A,base=_B),Hint(hint='Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.',important=_A,base=_B),Hint(hint='Candy Kong does not appear in Jungle Japes or Fungi Forest.',important=_A,base=_B),Hint(hint='If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.',important=_A,base=_B),Hint(hint='Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.',important=_A,base=_B),Hint(hint='The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.',important=_A,base=_B),Hint(hint='Chunky Kong is the brother of Kiddy Kong.',important=_A,base=_B),Hint(hint='Fungi Forest contains mushrooms.',important=_A,base=_B),Hint(hint='Igloos can be found in Crystal Caves.',important=_A,base=_B),Hint(hint='Frantic Factory has multiple floors where things can be found.',important=_A,base=_B),Hint(hint="Angry Aztec has so much sand, it's even in the wind.",important=_A,base=_B),Hint(hint='DK Isles does not have a key.',important=_A,base=_B),Hint(hint='You can find a rabbit in Fungi Forest and in Crystal Caves.',important=_A,base=_B),Hint(hint='You can find a beetle in Angry Aztec and in Crystal Caves.',important=_A,base=_B),Hint(hint='You can find a vulture in Angry Aztec.',important=_A,base=_B),Hint(hint='You can find an owl in Fungi Forest.',important=_A,base=_B),Hint(hint='To buy moves, you will need coins.',important=_A,base=_B),Hint(hint='You can change the music and sound effects volume in the sound settings on the main menu.',important=_A,base=_B),Hint(hint='Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.',important=_A,base=_B),Hint(hint='Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.',important=_A,base=_B),Hint(hint='I have nothing to say to you.',important=_A,base=_B),Hint(hint='I had something to tell you, but I forgot what it is.',important=_A,base=_B),Hint(hint="I don't know anything.",important=_A,base=_B),Hint(hint="I'm as lost as you are. Good luck!",important=_A,base=_B),Hint(hint='Wrinkly? Never heard of him.',important=_A,base=_B),Hint(hint='This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.',important=_A,base=_B),Hint(hint='Why do they call it oven when you of in the cold food of out hot eat the food?',important=_A,base=_B),Hint(hint='Wanna become famous? Buy followers, coconuts and donks at DK64Randomizer (DK64Randomizer . com)!',important=_A,base=_B),Hint(hint='What you gonna do, SpikeVegeta?',important=_A,base=_B)]
def pushHintToList(hint):'Push hint to hint list.';hint_list.append(hint)
def resetHintList():
	'Reset hint list to default state.'
	for A in hint_list:
		if not A.base:hint_list.remove(A)
		else:A.used=_A;A.important=A.was_important;A.repeats=A.original_repeats;A.priority=A.original_priority
def compileHints(spoiler):
	'Push hints to hint list based on settings.';Am='important';Al='Cranky';Ak='Ammo Belt Upgrade';Aj='DK Isles';Ai='Chunky';Ah='Donkey';Ag='k_rool';A9='Instrument Upgrade';A8='Slam Upgrade';A7='moves';A6='Creepy Castle';A5='Crystal Caves';A4='Fungi Forest';A3='Gloomy Galleon';A2='Angry Aztec';l='levels';k='hint';j='Frantic Factory';i='Jungle Japes';c='level';T='color';S='name';R='cryptic';K='kong';A=spoiler;resetHintList();AA=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
	if A.settings.krool_phase_order_rando and len(A.settings.krool_order)>1:
		U=f"K. Rool order is {NameFromKong(A.settings.krool_order[0])}"
		for C in range(len(A.settings.krool_order)):
			if C!=0:U+=f" then {NameFromKong(A.settings.krool_order[C])}"
		hint_list.append(Hint(hint=U,repeats=2,kongs=A.settings.krool_order.copy(),subtype=Ag))
	An=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];V=[]
	if A.settings.helm_phase_order_rando and len(A.settings.helm_order)>1:
		for Ao in A.settings.helm_order:V.append(An[Ao])
		U=f"Helm Room order is {NameFromKong(V[0])}"
		for C in range(len(V)):
			if C!=0:U+=f" then {NameFromKong(V[C])}"
		hint_list.append(Hint(hint=U,repeats=3,kongs=V.copy(),subtype=Ag))
	Ap=[Ah,'Diddy','Lanky','Tiny',Ai];Aq=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];O=[i,A2,j,A3,A4,A5,A6,'Hideout Helm'];AB=[i,A2,j,A3,A4,A5,A6,Aj];W=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with four vases','The level with two kongs cages','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with a game from 1981','The level where you need two quarters to play'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level with two inches of water','The level with two ice shields','The level with an Ice Tomato'],['The level with battlements','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']];X=W.copy();X.remove(X[-1]);X.append(['The hub world',"The world with DK's ugly mug on it","The world with only a Cranky's Lab and Snide's HQ in it"])
	if A.settings.shuffle_items==A7 and A.move_data is not _F:
		Ar=[0,2,1,1,4];As=0
		for C in A.settings.krool_order:As+=Ar[C]
		AC=[MoveInfo(name='Baboon Blast',move_level=1,move_type=_C,kong=Kongs.donkey),MoveInfo(name='Strong Kong',move_level=2,move_type=_C,kong=Kongs.donkey),MoveInfo(name='Gorilla Grab',move_level=3,move_type=_C,kong=Kongs.donkey),MoveInfo(name='Chimpy Charge',move_level=1,move_type=_C,kong=Kongs.diddy),MoveInfo(name='Rocketbarrel Boost',move_level=2,move_type=_C,kong=Kongs.diddy,important=A.settings.krool_diddy or A.settings.helm_diddy),MoveInfo(name='Simian Spring',move_level=3,move_type=_C,kong=Kongs.diddy),MoveInfo(name='Orangstand',move_level=1,move_type=_C,kong=Kongs.lanky),MoveInfo(name='Baboon Balloon',move_level=2,move_type=_C,kong=Kongs.lanky),MoveInfo(name='Orangstand Sprint',move_level=3,move_type=_C,kong=Kongs.lanky),MoveInfo(name='Mini Monkey',move_level=1,move_type=_C,kong=Kongs.tiny,important=A.settings.krool_tiny),MoveInfo(name='Ponytail Twirl',move_level=2,move_type=_C,kong=Kongs.tiny),MoveInfo(name='Monkeyport',move_level=3,move_type=_C,kong=Kongs.tiny,important=_B),MoveInfo(name='Hunky Chunky',move_level=1,move_type=_C,kong=Kongs.chunky,important=A.settings.krool_chunky),MoveInfo(name='Primate Punch',move_level=2,move_type=_C,kong=Kongs.chunky,important=A.settings.krool_chunky),MoveInfo(name='Gorilla Gone',move_level=3,move_type=_C,kong=Kongs.chunky,important=A.settings.krool_chunky),MoveInfo(name=A8,move_level=1,move_type=_G,kong=Kongs.any),MoveInfo(name=A8,move_level=2,move_type=_G,kong=Kongs.any),MoveInfo(name=A8,move_level=3,move_type=_G,kong=Kongs.any),MoveInfo(name='Coconut Shooter',move_level=1,move_type=_E,kong=Kongs.donkey,important=_B),MoveInfo(name='Peanut Popguns',move_level=1,move_type=_E,kong=Kongs.diddy,important=A.settings.krool_diddy),MoveInfo(name='Grape Shooter',move_level=1,move_type=_E,kong=Kongs.lanky),MoveInfo(name='Feather Bow',move_level=1,move_type=_E,kong=Kongs.tiny,important=A.settings.krool_tiny),MoveInfo(name='Pineapple Launcher',move_level=1,move_type=_E,kong=Kongs.chunky),MoveInfo(name='Homing Ammo',move_level=2,move_type=_E,kong=Kongs.any),MoveInfo(name='Sniper Scope',move_level=3,move_type=_E,kong=Kongs.any),MoveInfo(name=Ak,move_level=1,move_type=_I,kong=Kongs.any),MoveInfo(name=Ak,move_level=2,move_type=_I,kong=Kongs.any),MoveInfo(name='Bongo Blast',move_level=1,move_type=_D,kong=Kongs.donkey,important=A.settings.helm_donkey),MoveInfo(name='Guitar Gazump',move_level=1,move_type=_D,kong=Kongs.diddy,important=A.settings.helm_diddy),MoveInfo(name='Trombone Tremor',move_level=1,move_type=_D,kong=Kongs.lanky,important=A.settings.helm_lanky or A.settings.krool_lanky),MoveInfo(name='Saxophone Slam',move_level=1,move_type=_D,kong=Kongs.tiny,important=A.settings.helm_tiny),MoveInfo(name='Triangle Trample',move_level=1,move_type=_D,kong=Kongs.chunky,important=A.settings.helm_chunky),MoveInfo(name=A9,move_level=2,move_type=_D,kong=Kongs.any),MoveInfo(name=A9,move_level=3,move_type=_D,kong=Kongs.any),MoveInfo(name=A9,move_level=4,move_type=_D,kong=Kongs.any)];AD=[Al,'Funky','Candy'];BC=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']];AE=[]
		for m in range(3):
			AF=[]
			for G in range(8):
				n=[]
				for At in range(5):
					Au=A.move_data[m][At][G]
					for L in AC:
						if L.item_key==Au:
							if L.name not in n:n.append(L.name)
				AF.append(n)
			AE.append(AF)
		o=[];p=[]
		for (q,m) in enumerate(AE):
			for (M,G) in enumerate(m):
				for L in G:
					AG=_A
					for AH in AC:
						if AH.name==L and AH.important:AG=_B
					r=AD[q];D=AB[M]
					if A.settings.wrinkly_hints==R:D=random.choice(X[M])
					p.append({k:f"{L} can be purchased from {r} in {D}",Am:AG,'move':L})
				if len(G)>0:
					r=AD[q];D=AB[M]
					if A.settings.wrinkly_hints==R:D=random.choice(X[M])
					AI=G[0]
					if len(G)>1:AI=f"{', '.join(G[:-1])} and {G[-1]}"
					Av=f"{r}'s in {D} contains {AI}";o.append({k:Av,A7:G})
		random.shuffle(o);s=[3,6,10];d=1;AJ=_B
		for AK in o:
			if AJ:hint_list.append(Hint(hint=AK[k],important=_A,keywords=AK[A7],subtype='shop_dump'))
			if d<=len(s):
				if q+1>=s[d-1]:
					if d==len(s):AJ=_A
					else:d+=1
		random.shuffle(p)
		for t in p:hint_list.append(Hint(hint=t[k],priority=2,important=t[Am],keywords=[t['move']],subtype='move_location'))
	if A.settings.kong_rando:
		AL=A.shuffled_kong_placement;Aw=[{S:i,c:0},{S:'Llama Temple',c:1},{S:'Tiny Temple',c:1},{S:j,c:2}]
		for u in Aw:
			Y=AL[u[S]]['locked'][K];Ax=AL[u[S]]['puzzle'][K];M=u[c]
			if A.settings.wrinkly_hints==R:
				if not Y==Kongs.any:v=random.choice(Aq[Y])
				D=random.choice(W[M])
			else:
				if not Y==Kongs.any:v=Ap[Y]
				D=O[M]
			AM=2
			if Y==Kongs.any:v='An empty cage';AM=3
			hint_list.append(Hint(hint=f"{v} can be found in {D}.",kongs=[Ax],priority=AM,subtype='kong_location'))
	if A.settings.random_patches:
		e={Aj:0,i:0,A2:0,j:0,A3:0,A4:0,A5:0,A6:0}
		for Ay in A.dirt_patch_placement:
			for G in e:
				if G in Ay:e[G]+=1
		AN=list(e.keys());random.shuffle(AN)
		for f in range(2):
			for Z in range(4):
				D=AN[Z+4*f];w=e[D]
				if w>0:
					AO='patches';AP='are'
					if w==1:AO='patch';AP='is'
					x=f"There {AP} {w} {AO} in {D}";hint_list.append(Hint(hint=x,priority=Z+3,important=_A,subtype='level_patch_count'))
		AQ=A.dirt_patch_placement.copy();random.shuffle(AQ)
		for f in range(2):
			for Z in range(4):Az=AQ[Z+f*4];x=f"There is a dirt patch located at {Az}";hint_list.append(Hint(hint=x,priority=Z+4,important=f==0,subtype='patch_location'))
	if A.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(A)
	if A.settings.coin_door_open=='need_both'or A.settings.coin_door_open=='need_rw':hint_list.append(Hint(hint=f"{A.settings.medal_requirement} medals are required to access Jetpac.",priority=4,subtype='medal'))
	if A.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.',subtype='permadeath'))
	if A.settings.level_randomization!='level_order':
		for C in A.settings.krool_keys_required:
			AR=C-4
			if A.settings.wrinkly_hints==R:D=random.choice(W[AR])
			else:D=O[AR]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {D} to fight your greatest foe.",important=_A,subtype='key_is_required'))
	A_=['Candy','Funky',Al];B0=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];AS=[B for B in A.woth.keys()if any((A in B for A in A_))];B1=random.sample(AS,min(5,len(AS)));AT=random.randint(1,4)
	for AU in B1:
		AV=[A for A in B0 if A in AU]
		if len(AV)>0:B2=str(AU).removesuffix(AV[0])
		hint_list.append(Hint(hint=f"{B2} is on the Way of the Hoard.",important=random.choice([_B,_B,_A]),priority=AT,subtype='way_of_the_hoard'));AT+=random.randint(1,2)
	B3=[{K:Ah,T:'Yellow'},{K:'Diddy',T:'Red'},{K:'Lanky',T:'Blue'},{K:'Tiny',T:'Purple'},{K:Ai,T:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {O[random.randint(0,6)]}, but also in other levels.",important=_A,subtype=_H,joke=_B,joke_defined=_B));AW=random.choice(B3);hint_list.append(Hint(hint=f"{AW[K]} can find {AW[T]} bananas in {random.choice(O)}.",important=_A,subtype=_H,joke=_B,joke_defined=_B));hint_list.append(Hint(hint=f"{A.settings.krool_key_count} Keys are required to reach K. Rool.",important=_A,subtype='key_count_required'))
	if A.settings.shuffle_loading_zones==l:
		B4={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};B5={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle};y={};g={};AX=[]
		for (B6,AY) in B4.items():AZ=B5[A.shuffled_exit_data[B6].reverse];y[AZ]=AY;g[AY]=AZ
	if A.settings.randomize_blocker_required_amounts is _B and A.settings.shuffle_loading_zones==l:
		for B7 in list(g.values()):AX.append(B7.name)
		for C in range(8):
			a=A.settings.EntryGBs[C];Aa='Golden Bananas'
			if a==1:Aa='Golden Banana'
			D=O[C];z=_A;N=AA.copy();P=C+1
			if A.settings.shuffle_loading_zones==l:
				if C!=7:
					A0=y[C];N=[]
					for b in range(7):
						if b<A0:N.append(g[b])
					if D.replace(' ','')in AX[4:7]:P=4;z=_B
				if A.settings.maximize_helm_blocker is _A and C==7:P=1;z=_B
			if A.settings.wrinkly_hints==R:D=random.choice(W[C])
			hint_list.append(Hint(hint=f"The barrier to {D} can be cleared by obtaining {a} {Aa}.",important=z,priority=P,permitted_levels=N.copy(),subtype='gb_amount'))
	for C in range(7):
		a=A.settings.BossBananas[C];Ab='Small Bananas'
		if a==1:Ab='Small Banana'
		if A.settings.wrinkly_hints==R:D=random.choice(W[C])
		else:D=O[C]
		N=AA.copy()
		if A.settings.shuffle_loading_zones==l:
			A0=y[C];N=[]
			for b in range(7):
				if b<=A0:N.append(g[b])
		hint_list.append(Hint(hint=f"The barrier to the boss in {D} can be cleared by obtaining {a} {Ab}.",important=_A,permitted_levels=N.copy(),subtype='cb_amount'))
	H={};F=[]
	for B in hint_list:
		if not B.important and not B.used and B.joke:F.append(B)
	Q=random.choice(F);J=_A;B8=0
	while not J:
		J=updateRandomHint(Q.hint,Q.kongs.copy(),Q.keywords.copy(),Q.permitted_levels.copy())
		if J:
			Q.use_hint();B8+=1;E=Q.subtype
			if E in H:H[E]+=1
			else:H[E]=1
			break
	random.shuffle(hint_list);P=1;Ac=_A;B9=0
	while not Ac:
		Ad=_A
		for B in hint_list:
			if B.important and B.priority==P and not B.used and not B.joke:
				Ad=_B;J=updateRandomHint(B.hint,B.kongs.copy(),B.keywords.copy(),B.permitted_levels.copy())
				if J:
					B.use_hint();B9+=1;E=B.subtype
					if E in H:H[E]+=1
					else:H[E]=1
				else:B.downgrade()
		if not Ad:Ac=_B
		P+=1
	F=[];h=0
	for B in hint_list:
		if not B.important and not B.used and not B.joke:F.append(B)
	for B in hints:
		if B.hint=='':h+=1
	random.shuffle(F);BA=0;BB=0
	if h>0:
		A1=0;Ae=100;I=0
		while A1<h:
			J=_A
			if not F[I].used:J=updateRandomHint(F[I].hint,F[I].kongs,F[I].keywords.copy(),F[I].permitted_levels.copy())
			if J:
				F[I].use_hint();BA+=1;E=F[I].subtype
				if E in H:H[E]+=1
				else:H[E]=1
				A1+=1
			else:Ae-=1
			I+=1
			if I>=len(F):I=0
			if Ae==0:
				Af=[]
				for B in hint_list:
					if not B.joke:Af.append(B.hint)
				for B in hints:
					if B.hint=='':B.hint=random.choice(Af)
				for B in hints:
					if B.hint=='':
						B.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.';E='error'
						if E in H:H[E]+=1
						else:H[E]=1
						BB+=1
				A1=h
	UpdateSpoilerHintList(A);return _B
def AddLoadingZoneHints(spoiler):
	'Add hints for loading zone transitions and their destinations.';A=spoiler;G=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];H=[Regions.AngryAztecStart,Regions.AngryAztecMain];I=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];B=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in G];random.shuffle(B);J=_A
	while len(B)>0:
		Q=B.pop()
		if TryAddingLoadingZoneHint(A,Q,1,G):J=_B;break
	if not J:print('Japes LZR hint unable to be placed!')
	C=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in H];random.shuffle(C);K=_A
	while len(C)>0:
		R=C.pop()
		if TryAddingLoadingZoneHint(A,R,1,H):K=_B;break
	if not K:print('Aztec LZR hint unable to be placed!')
	D=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in I];random.shuffle(D);L=_A
	while len(D)>0:
		S=D.pop()
		if TryAddingLoadingZoneHint(A,S,1,I):L=_B;break
	if not L:print('Factory LZR hint unable to be placed!')
	T=[[Regions.BananaFairyRoom],[Regions.GloomyGalleonStart,Regions.LighthouseArea,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]];U=random.sample(T,3)
	for M in U:
		E=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in M];random.shuffle(E);N=_A
		while len(E)>0:
			O=E.pop()
			if TryAddingLoadingZoneHint(A,O,3,M):N=_B;break
		if not N:print(f"Useful LZR hint to {O.name} unable to be placed!")
	V=[Regions.IslesMain,Regions.IslesMainUpper];P=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId not in V];random.shuffle(P);F=4
	for W in P:
		if F==0:break
		elif TryAddingLoadingZoneHint(A,W,5):F-=1
	if F>0:print('Unable to place remaining LZR hints!')
def TryAddingLoadingZoneHint(spoiler,transition,useful_rating,disallowedRegions=_F):
	'Try to write a hint for the given transition. If this hint is determined to be bad, it will return false and not place the hint.';E=disallowedRegions;D=transition;B=spoiler
	if E is _F:E=[]
	A=D
	if B.settings.decoupled_loading_zones:
		while ShufflableExits[A].category is _F:
			F=[C for(C,D)in B.shuffled_exit_data.items()if D.reverse==A]
			if len(F)==0:break
			A=F[0]
	elif ShufflableExits[A].category is _F:return _A
	if ShufflableExits[A].region in E:return _A
	H=GetMapId(ShufflableExits[A].region);I=GetMapId(B.shuffled_exit_data[D].regionId)
	if H==I:return _A
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(' from ')
	if G!=-1:C=C[:G]
	pushHintToList(Hint(hint=f"If you're looking for {C}, follow the path from {J}.",priority=useful_rating,subtype='lzr'));return _B
def UpdateSpoilerHintList(spoiler):
	'Write hints to spoiler object.'
	for A in hints:
		if A.kong!=Kongs.any:spoiler.hint_list[A.name]=A.hint