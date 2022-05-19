'Compile a list of hints based on the settings.'
_B=True
_A=False
import random
from randomizer.Enums.Regions import Regions
from randomizer.Lists.Item import NameFromKong
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Spoiler import Spoiler
from randomizer.Patching.UpdateHints import updateRandomHint
def compileHints(spoiler):
	'Push hints to hint list based on settings.';g='Frantic Factory';f='Jungle Japes';e='Their first special move';d='Their third special move';O='name_cryptic';M='color';G=spoiler;F='important';E='key';D='shop';C='name';B='level';A='kong'
	if G.settings.krool_phase_order_rando:
		P=f"K. Rool order is {NameFromKong(G.settings.krool_order[0])}"
		for H in range(len(G.settings.krool_order)):
			if H!=0:P+=f" then {NameFromKong(G.settings.krool_order[H])}"
		updateRandomHint(P)
	K=['Did you know - Donkey Kong officially features in Donkey Kong 64.','Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.','Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.','Tiny Kong is the youngest sister of Dixie Kong.','Mornin.','Lanky Kong is the only kong with no canonical relation to the main Kong family tree.','Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.','Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.','Candy Kong does not appear in Jungle Japes or Fungi Forest.','If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.','Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.','The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.','Chunky Kong is the brother of Kiddy Kong.','Fungi Forest contains mushrooms.','Igloos can be found in Crystal Caves.','Frantic Factory has multiple floors where things can be found.',"Angry Aztec has so much sand, it's even in the wind.",'DK Isles does not have a key.','You can find a rabbit in Fungi Forest and in Crystal Caves.','You can find a beetle in Angry Aztec and in Crystal Caves.','You can find a vulture in Angry Aztec.','You can find an owl in Fungi Forest.','To buy moves, you will need coins.','You can change the music and sound effects volume in the sound settings on the main menu.','Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.','Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.','I have nothing to say to you.','I had something to tell you, but I forgot what it is.',"I don't know anything.","I'm as lost as you are. Good luck!",'Wrinkly? Never heard of him.','This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.'];Q=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];L=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with sporadic gusts of sand','The level with two kongs to free','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with Cranky and Candy adjacent to each other'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level where it rains rocks','The level with two ice shields','The level with an Ice Tomato'],['The level with constant rain','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']]
	if G.settings.shuffle_items=='moves'and G.move_data is not None:
		h=[0,2,1,1,4];i=0
		for H in G.settings.krool_order:i+=h[H]
		R=[{C:'Monkeyport',O:d,E:3,A:3,B:0,D:0,F:_B},{C:'Mini Monkey',O:e,E:1,A:3,B:0,D:0,F:_B},{C:'Coconut Gun',O:'Their gun',E:33,A:0,B:0,D:0,F:_B},{C:'Chimpy Charge',O:e,E:1,A:1,B:0,D:0,F:_B},{C:'Gorilla Gone',O:d,E:3,A:4,B:0,D:0,F:_B},{C:'Ponytail Twirl',E:2,A:3,B:0,D:0,F:_A},{C:'Baboon Blast',E:1,A:0,B:0,D:0,F:_A},{C:'Strong Kong',E:2,A:0,B:0,D:0,F:_A},{C:'Gorilla Grab',E:3,A:0,B:0,D:0,F:_A},{C:'Rocketbarrel Boost',E:2,A:1,B:0,D:0,F:_A},{C:'Simian Spring',E:3,A:1,B:0,D:0,F:_A},{C:'Orangstand',E:1,A:2,B:0,D:0,F:_A},{C:'Baboon Balloon',E:2,A:2,B:0,D:0,F:_A},{C:'Orangstand Sprint',E:3,A:2,B:0,D:0,F:_A},{C:'Hunky Chunky',E:1,A:4,B:0,D:0,F:_A},{C:'Primate Punch',E:2,A:4,B:0,D:0,F:_A},{C:'Peanut Popguns',E:33,A:1,B:0,D:0,F:_A},{C:'Grape Shooter',E:33,A:2,B:0,D:0,F:_A},{C:'Feather Bow',E:33,A:3,B:0,D:0,F:_A},{C:'Pineapple Launcher',E:33,A:4,B:0,D:0,F:_A},{C:'Bongo Blast',E:65,A:0,B:0,D:0,F:_A},{C:'Guitar Gazump',E:65,A:1,B:0,D:0,F:_A},{C:'Trombone Tremor',E:65,A:2,B:0,D:0,F:_A},{C:'Saxophone Slam',E:65,A:3,B:0,D:0,F:_A},{C:'Triangle Trample',E:65,A:4,B:0,D:0,F:_A}];j=['Cranky','Funky','Candy'];t=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for S in range(3):
			for T in range(5):
				for U in range(7):
					for J in R:
						if G.move_data[S][T][U]==J[E]and T==J[A]:J[B]=U;J[D]=S
		for J in R:
			V=random.choice(Q[J[A]]);k=J[C];I=random.choice(L[J[B]]);l=j[J[D]];W=f"{k} can be purchased in {I} from {l}."
			if J[F]:updateRandomHint(W)
			else:K.append(W)
	if G.settings.kong_rando:
		m=G.shuffled_kong_placement;n=[{C:f,B:0},{C:'Llama Temple',B:1},{C:'Tiny Temple',B:1},{C:g,B:2}]
		for X in n:o=m[X[C]]['locked'][A];p=X[B];V=random.choice(Q[o]);I=random.choice(L[p]);updateRandomHint(f"{V} can be found in {I}.")
	if G.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(G)
	if G.settings.BananaMedalsRequired:updateRandomHint(f"{G.settings.BananaMedalsRequired} medals are required to access Jetpac.")
	if G.settings.perma_death:updateRandomHint('The curse can only be removed upon disabling K. Rools machine.')
	updateRandomHint(f"{G.settings.krool_key_count} Keys are required to turn in K. Rool.")
	if G.settings.level_randomization!='level_order':
		for H in G.settings.krool_keys_required:q=H-4;I=random.choice(L[q]);updateRandomHint(f"You will need to obtain the key from {I} to fight your greatest foe.")
	for H in range(7):
		r=G.settings.boss_maps[H];I=random.choice(L[H])
		if r==199:updateRandomHint(f"The cardboard boss can be found in {I}.")
	Y=[f,'Angry Aztec',g,'Gloomy Galleon','Fungi Forest','Crystal Caves','Creepy Castle'];s=[{A:'Donkey',M:'Yellow'},{A:'Diddy',M:'Red'},{A:'Lanky',M:'Blue'},{A:'Tiny',M:'Purple'},{A:'Chunky',M:'Green'}];K.append(f"You can find bananas in {random.choice(Y)}, but also in other levels.");Z=random.choice(s);K.append(f"{Z[A]} can find {Z[M]} bananas in {random.choice(Y)}.")
	for H in range(8):
		N=G.settings.EntryGBs[H];a='Golden Bananas'
		if N==1:a='Golden Banana'
		I=random.choice(L[H]);K.append(f"The barrier to {I} can be cleared by obtaining {N} {a}.")
	for H in range(7):
		N=G.settings.BossBananas[H];b='Small Bananas'
		if N==1:b='Small Banana'
		I=random.choice(L[H]);K.append(f"The barrier to the boss in {I} can be cleared by obtaining {N} {b}.")
	c=35
	if len(K)<35:c=len(K)
	random.shuffle(K)
	for H in range(c):updateRandomHint(K[H])
def AddLoadingZoneHints(spoiler):
	'Add hints for loading zone transitions and their destinations.';A=spoiler;G=[Regions.JungleJapesMain,Regions.JapesBeyondFeatherGate,Regions.TinyHive,Regions.JapesLankyCave,Regions.Mine];H=[Regions.AngryAztecStart,Regions.AngryAztecMain];I=[Regions.FranticFactoryStart,Regions.ChunkyRoomPlatform,Regions.PowerHut,Regions.BeyondHatch,Regions.InsideCore];B=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in G];random.shuffle(B);J=_A
	while len(B)>0:
		Q=B.pop()
		if TryAddingLoadingZoneHint(A,Q,G):J=_B;break
	if not J:print('Japes LZR hint unable to be placed!')
	C=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in H];random.shuffle(C);K=_A
	while len(C)>0:
		R=C.pop()
		if TryAddingLoadingZoneHint(A,R,H):K=_B;break
	if not K:print('Aztec LZR hint unable to be placed!')
	D=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in I];random.shuffle(D);L=_A
	while len(D)>0:
		S=D.pop()
		if TryAddingLoadingZoneHint(A,S,I):L=_B;break
	if not L:print('Factory LZR hint unable to be placed!')
	T=[[Regions.BananaFairyRoom],[Regions.GloomyGalleonStart,Regions.LighthouseArea,Regions.Shipyard],[Regions.FungiForestStart,Regions.GiantMushroomArea,Regions.MushroomLowerExterior,Regions.MushroomNightExterior,Regions.MushroomUpperExterior,Regions.MillArea],[Regions.CrystalCavesMain,Regions.IglooArea,Regions.CabinArea],[Regions.CreepyCastleMain,Regions.CastleWaterfall],[Regions.LowerCave],[Regions.UpperCave]];U=random.sample(T,3)
	for M in U:
		E=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId in M];random.shuffle(E);N=_A
		while len(E)>0:
			O=E.pop()
			if TryAddingLoadingZoneHint(A,O,M):N=_B;break
		if not N:print(f"Useful LZR hint to {O.name} unable to be placed!")
	V=[Regions.IslesMain,Regions.IslesMainUpper];P=[B for(B,C)in A.shuffled_exit_data.items()if C.regionId not in V];random.shuffle(P);F=4
	for W in P:
		if F==0:break
		elif TryAddingLoadingZoneHint(A,W):F-=1
	if F>0:print('Unable to place remaining LZR hints!')
def TryAddingLoadingZoneHint(spoiler,transition,disallowedRegions=[]):
	'Try to write a hint for the given transition. If this hint is determined to be bad, it will return false and not place the hint.';D=transition;B=spoiler;A=D
	if B.settings.decoupled_loading_zones:
		while ShufflableExits[A].category is None:
			E=[C for(C,D)in B.shuffled_exit_data.items()if D.reverse==A]
			if len(E)==0:break
			A=E[0]
	elif ShufflableExits[A].category is None:return _A
	if ShufflableExits[A].region in disallowedRegions:return _A
	G=GetMapId(ShufflableExits[A].region);H=GetMapId(B.shuffled_exit_data[D].regionId)
	if G==H:return _A
	I=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;F=C.find(' from ')
	if F!=-1:C=C[:F]
	updateRandomHint(f"If you're looking for {C}, follow the path from {I}.");return _B