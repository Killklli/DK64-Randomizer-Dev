'Compile a list of hints based on the settings.'
_C=None
_B=True
_A=False
import random
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions
from randomizer.Lists.Item import NameFromKong
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Spoiler import Spoiler
from randomizer.Patching.UpdateHints import updateRandomHint
def compileHints(spoiler):
	'Push hints to hint list based on settings.';w='Candy';v='Funky';u='Cranky';t='Their first special move';s='Their third special move';r='Frantic Factory';q='Jungle Japes';p='Chunky';o='Tiny';n='Lanky';m='Diddy';l='Donkey';R='name_cryptic';O='color';N='cryptic';G='important';F='key';E='shop';D=spoiler;C='name';B='level';A='kong'
	if D.settings.krool_phase_order_rando:
		T=f"K. Rool order is {NameFromKong(D.settings.krool_order[0])}"
		for H in range(len(D.settings.krool_order)):
			if H!=0:T+=f" then {NameFromKong(D.settings.krool_order[H])}"
		updateRandomHint(T)
	K=['Did you know - Donkey Kong officially features in Donkey Kong 64.','Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.','Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.','Tiny Kong is the youngest sister of Dixie Kong.','Mornin.','Lanky Kong is the only kong with no canonical relation to the main Kong family tree.','Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.','Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.','Candy Kong does not appear in Jungle Japes or Fungi Forest.','If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.','Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.','The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.','Chunky Kong is the brother of Kiddy Kong.','Fungi Forest contains mushrooms.','Igloos can be found in Crystal Caves.','Frantic Factory has multiple floors where things can be found.',"Angry Aztec has so much sand, it's even in the wind.",'DK Isles does not have a key.','You can find a rabbit in Fungi Forest and in Crystal Caves.','You can find a beetle in Angry Aztec and in Crystal Caves.','You can find a vulture in Angry Aztec.','You can find an owl in Fungi Forest.','To buy moves, you will need coins.','You can change the music and sound effects volume in the sound settings on the main menu.','Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.','Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.','I have nothing to say to you.','I had something to tell you, but I forgot what it is.',"I don't know anything.","I'm as lost as you are. Good luck!",'Wrinkly? Never heard of him.','This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.','Why do they call it oven when you of in the cold food of out hot eat the food?'];U=[l,m,n,o,p];V=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];L=[q,'Angry Aztec',r,'Gloomy Galleon','Fungi Forest','Crystal Caves','Creepy Castle','Hideout Helm'];M=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with sporadic gusts of sand','The level with two kongs to free','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with Cranky and Candy adjacent to each other'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level where it rains rocks','The level with two ice shields','The level with an Ice Tomato'],['The level with constant rain','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']]
	if D.settings.shuffle_items=='moves'and D.move_data is not _C:
		x=[0,2,1,1,4];y=0
		for H in D.settings.krool_order:y+=x[H]
		W=[{C:'Monkeyport',R:s,F:3,A:3,B:0,E:0,G:_B},{C:'Mini Monkey',R:t,F:1,A:3,B:0,E:0,G:_B},{C:'Coconut Gun',R:'Their gun',F:33,A:0,B:0,E:0,G:_B},{C:'Chimpy Charge',R:t,F:1,A:1,B:0,E:0,G:_B},{C:'Gorilla Gone',R:s,F:3,A:4,B:0,E:0,G:_B},{C:'Ponytail Twirl',F:2,A:3,B:0,E:0,G:_A},{C:'Baboon Blast',F:1,A:0,B:0,E:0,G:_A},{C:'Strong Kong',F:2,A:0,B:0,E:0,G:_A},{C:'Gorilla Grab',F:3,A:0,B:0,E:0,G:_A},{C:'Rocketbarrel Boost',F:2,A:1,B:0,E:0,G:_A},{C:'Simian Spring',F:3,A:1,B:0,E:0,G:_A},{C:'Orangstand',F:1,A:2,B:0,E:0,G:_A},{C:'Baboon Balloon',F:2,A:2,B:0,E:0,G:_A},{C:'Orangstand Sprint',F:3,A:2,B:0,E:0,G:_A},{C:'Hunky Chunky',F:1,A:4,B:0,E:0,G:_A},{C:'Primate Punch',F:2,A:4,B:0,E:0,G:_A},{C:'Peanut Popguns',F:33,A:1,B:0,E:0,G:_A},{C:'Grape Shooter',F:33,A:2,B:0,E:0,G:_A},{C:'Feather Bow',F:33,A:3,B:0,E:0,G:_A},{C:'Pineapple Launcher',F:33,A:4,B:0,E:0,G:_A},{C:'Bongo Blast',F:65,A:0,B:0,E:0,G:_A},{C:'Guitar Gazump',F:65,A:1,B:0,E:0,G:_A},{C:'Trombone Tremor',F:65,A:2,B:0,E:0,G:_A},{C:'Saxophone Slam',F:65,A:3,B:0,E:0,G:_A},{C:'Triangle Trample',F:65,A:4,B:0,E:0,G:_A}];z=[u,v,w];AA=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for X in range(3):
			for Y in range(5):
				for Z in range(7):
					for J in W:
						if D.move_data[X][Y][Z]==J[F]and Y==J[A]:J[B]=Z;J[E]=X
		for J in W:
			if D.settings.wrinkly_hints==N:P=random.choice(V[J[A]]);I=random.choice(M[J[B]])
			else:P=U[J[A]];I=L[J[B]]
			A0=J[C];A1=z[J[E]];a=f"{A0} can be purchased from {A1} in {I}."
			if J[G]:updateRandomHint(a)
			else:K.append(a)
	if D.settings.kong_rando:
		A2=D.shuffled_kong_placement;A3=[{C:q,B:0},{C:'Llama Temple',B:1},{C:'Tiny Temple',B:1},{C:r,B:2}]
		for b in A3:
			S=A2[b[C]]['locked'][A];c=b[B]
			if D.settings.wrinkly_hints==N:P=random.choice(V[S]);I=random.choice(M[c])
			else:P=U[S];I=L[c]
			if S==Kongs.any:P='An empty cage'
			updateRandomHint(f"{P} can be found in {I}.")
	if D.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(D)
	if D.settings.BananaMedalsRequired:updateRandomHint(f"{D.settings.BananaMedalsRequired} medals are required to access Jetpac.")
	if D.settings.perma_death:updateRandomHint('The curse can only be removed upon disabling K. Rools machine.')
	updateRandomHint(f"{D.settings.krool_key_count} Keys are required to turn in K. Rool.")
	if D.settings.level_randomization!='level_order':
		for H in D.settings.krool_keys_required:
			d=H-4
			if D.settings.wrinkly_hints==N:I=random.choice(M[d])
			else:I=L[d]
			updateRandomHint(f"You will need to obtain the key from {I} to fight your greatest foe.")
	for H in range(7):
		A4=D.settings.boss_maps[H]
		if D.settings.wrinkly_hints==N:I=random.choice(M[H])
		else:I=L[H]
		if A4==199:updateRandomHint(f"The cardboard boss can be found in {I}.")
	A5=[w,v,u];A6=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];e=[A for A in D.woth.keys()if any((B in A for B in A5))];A7=random.sample(e,min(5,len(e)))
	for f in A7:
		g=[A for A in A6 if A in f]
		if len(g)>0:A8=str(f).removesuffix(g[0])
		updateRandomHint(f"{A8} is on the Way of the Hoard.")
	A9=[{A:l,O:'Yellow'},{A:m,O:'Red'},{A:n,O:'Blue'},{A:o,O:'Purple'},{A:p,O:'Green'}];K.append(f"You can find bananas in {L[random.randint(0,6)]}, but also in other levels.");h=random.choice(A9);K.append(f"{h[A]} can find {h[O]} bananas in {random.choice(L)}.")
	for H in range(8):
		Q=D.settings.EntryGBs[H];i='Golden Bananas'
		if Q==1:i='Golden Banana'
		if D.settings.wrinkly_hints==N:I=random.choice(M[H])
		else:I=L[H]
		K.append(f"The barrier to {I} can be cleared by obtaining {Q} {i}.")
	for H in range(7):
		Q=D.settings.BossBananas[H];j='Small Bananas'
		if Q==1:j='Small Banana'
		if D.settings.wrinkly_hints==N:I=random.choice(M[H])
		else:I=L[H]
		K.append(f"The barrier to the boss in {I} can be cleared by obtaining {Q} {j}.")
	k=35
	if len(K)<35:k=len(K)
	random.shuffle(K)
	for H in range(k):updateRandomHint(K[H])
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
def TryAddingLoadingZoneHint(spoiler,transition,disallowedRegions=_C):
	'Try to write a hint for the given transition. If this hint is determined to be bad, it will return false and not place the hint.';E=disallowedRegions;D=transition;B=spoiler
	if E is _C:E=[]
	A=D
	if B.settings.decoupled_loading_zones:
		while ShufflableExits[A].category is _C:
			F=[C for(C,D)in B.shuffled_exit_data.items()if D.reverse==A]
			if len(F)==0:break
			A=F[0]
	elif ShufflableExits[A].category is _C:return _A
	if ShufflableExits[A].region in E:return _A
	H=GetMapId(ShufflableExits[A].region);I=GetMapId(B.shuffled_exit_data[D].regionId)
	if H==I:return _A
	J=ShufflableExits[A].name;C=B.shuffled_exit_data[D].spoilerName;G=C.find(' from ')
	if G!=-1:C=C[:G]
	updateRandomHint(f"If you're looking for {C}, follow the path from {J}.");return _B