'Compile a list of hints based on the settings.'
import random
from randomizer.Lists.Item import NameFromKong
from randomizer.Spoiler import Spoiler
from randomizer.Patching.UpdateHints import updateRandomHint
def compileHints(spoiler):
	'Push hints to hint list based on settings.';j='Frantic Factory';i='Jungle Japes';h='Gorilla Gone';g='Their first special move';f='Their third special move';Q=True;P='name_cryptic';N='color';H=spoiler;G=False;F='important';E='key';D='shop';C='name';B='level';A='kong'
	if H.settings.krool_phase_order_rando:
		R=f"K. Rool order is {NameFromKong(H.settings.krool_order[0])}"
		for I in range(len(H.settings.krool_order)):
			if I!=0:R+=f" then {NameFromKong(H.settings.krool_order[I])}"
		updateRandomHint(R)
	L=['Did you know - Donkey Kong officially features in Donkey Kong 64.','Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.','Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.','Tiny Kong is the youngest sister of Dixie Kong.','Mornin.','Lanky Kong is the only kong with no canonical relation to the main Kong family tree.','Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.','Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.','Candy Kong does not appear in Jungle Japes or Fungi Forest.','If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.','Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.','The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.','Chunky Kong is the brother of Kiddy Kong.','Fungi Forest contains mushrooms.','Igloos can be found in Crystal Caves.','Frantic Factory has multiple floors where things can be found.',"Angry Aztec has so much sand, it's even in the wind.",'DK Isles does not have a key.','You can find a rabbit in Fungi Forest and in Crystal Caves.','You can find a beetle in Angry Aztec and in Crystal Caves.','You can find a vulture in Angry Aztec.','You can find an owl in Fungi Forest.','To buy moves, you will need coins.','You can change the music and sound effects volume in the sound settings on the main menu.','Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.','Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.','I have nothing to say to you.','I had something to tell you, but I forgot what it is.',"I don't know anything.","I'm as lost as you are. Good luck!",'Wrinkly? Never heard of him.','This is it. The peak of all randomizers. No other randomizer exists besides dk64randomizer.com where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.'];S=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who shares a home with a thirsty dweller'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];M=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with sporadic gusts of sand','The level with two kongs to free','The level who is home to a humped animal'],['The level with a toy production facility','The level with a tower of blocks','The level with Cranky and Candy adjacent to each other'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level where it rains rocks','The level with two ice shields','The level with an Ice Tomato'],['The level with constant rain','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']]
	if H.settings.shuffle_items=='moves'and H.move_data is not None:
		k=[0,2,1,1,4];l=0
		for I in H.settings.krool_order:l+=k[I]
		T=[{C:'Monkeyport',P:f,E:3,A:3,B:0,D:0,F:Q},{C:'Mini Monkey',P:g,E:1,A:3,B:0,D:0,F:Q},{C:'Coconut Gun',P:'Their gun',E:33,A:0,B:0,D:0,F:Q},{C:'Chimpy Charge',P:g,E:1,A:1,B:0,D:0,F:Q},{C:h,P:f,E:3,A:4,B:0,D:0,F:Q},{C:'Ponytail Twirl',E:2,A:3,B:0,D:0,F:G},{C:'Baboon Blast',E:1,A:0,B:0,D:0,F:G},{C:'Strong Kong',E:2,A:0,B:0,D:0,F:G},{C:h,E:3,A:0,B:0,D:0,F:G},{C:'Rocketbarrel Boost',E:2,A:1,B:0,D:0,F:G},{C:'Simian Spring',E:3,A:1,B:0,D:0,F:G},{C:'Orangstand',E:1,A:2,B:0,D:0,F:G},{C:'Baboon Balloon',E:2,A:2,B:0,D:0,F:G},{C:'Orangstand Sprint',E:3,A:2,B:0,D:0,F:G},{C:'Hunky Chunky',E:1,A:4,B:0,D:0,F:G},{C:'Primate Punch',E:2,A:4,B:0,D:0,F:G},{C:'Peanut Popguns',E:33,A:1,B:0,D:0,F:G},{C:'Grape Shooter',E:33,A:2,B:0,D:0,F:G},{C:'Feather Bow',E:33,A:3,B:0,D:0,F:G},{C:'Pineapple Launcher',E:33,A:4,B:0,D:0,F:G},{C:'Bongo Blast',E:65,A:0,B:0,D:0,F:G},{C:'Guitar Gazump',E:65,A:1,B:0,D:0,F:G},{C:'Trombone Tremor',E:65,A:2,B:0,D:0,F:G},{C:'Saxophone Slam',E:65,A:3,B:0,D:0,F:G},{C:'Triangle Trample',E:65,A:4,B:0,D:0,F:G}];m=['Cranky','Funky','Candy'];w=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for U in range(3):
			for V in range(5):
				for W in range(7):
					for K in T:
						if H.move_data[U][V][W]==K[E]and V==K[A]:K[B]=W;K[D]=U
		for K in T:
			X=random.choice(S[K[A]]);n=K[C];J=random.choice(M[K[B]]);o=m[K[D]];Y=f"{n} can be purchased in {J} from {o}."
			if K[F]:updateRandomHint(Y)
			else:L.append(Y)
	if H.settings.kong_rando:
		p=H.shuffled_kong_placement;q=[{C:i,B:0},{C:'Llama Temple',B:1},{C:'Tiny Temple',B:1},{C:j,B:2}]
		for Z in q:r=p[Z[C]]['locked'][A];s=Z[B];X=random.choice(S[r]);J=random.choice(M[s]);updateRandomHint(f"{X} can be found in {J}.")
	if H.settings.BananaMedalsRequired:updateRandomHint(f"{H.settings.BananaMedalsRequired} medals are required to access Jetpac.")
	if H.settings.perma_death:updateRandomHint('The curse can only be removed upon disabling K. Rools machine.')
	updateRandomHint(f"{H.settings.krool_key_count} Keys are required to turn in K. Rool.")
	if H.settings.level_randomization!='level_order':
		for I in H.settings.krool_keys_required:t=I-4;J=random.choice(M[t]);updateRandomHint(f"You will need to obtain the key from {J} to fight your greatest foe.")
	for I in range(7):
		u=H.settings.boss_maps[I];J=random.choice(M[I])
		if u==199:updateRandomHint(f"The cardboard boss can be found in {J}.")
	a=[i,'Angry Aztec',j,'Gloomy Galleon','Fungi Forest','Crystal Caves','Creepy Castle'];v=[{A:'Donkey',N:'Yellow'},{A:'Diddy',N:'Red'},{A:'Lanky',N:'Blue'},{A:'Tiny',N:'Purple'},{A:'Chunky',N:'Green'}];L.append(f"You can find bananas in {random.choice(a)}, but also in other levels.");b=random.choice(v);L.append(f"{b[A]} can find {b[N]} bananas in {random.choice(a)}.")
	for I in range(8):
		O=H.settings.EntryGBs[I];c='Golden Bananas'
		if O==1:c='Golden Banana'
		J=random.choice(M[I]);L.append(f"The barrier to {J} can be cleared by obtaining {O} {c}.")
	for I in range(7):
		O=H.settings.BossBananas[I];d='Small Bananas'
		if O==1:d='Small Banana'
		J=random.choice(M[I]);L.append(f"The barrier to the boss in {J} can be cleared by obtaining {O} {d}.")
	e=35
	if len(L)<35:e=len(L)
	random.shuffle(L)
	for I in range(e):updateRandomHint(L[I])