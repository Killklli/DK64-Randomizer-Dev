'Compile a list of hints based on the settings.'
_C=None
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
class Hint:
	'Hint object for Wrinkly hint text.'
	def __init__(A,*,hint='',important=_B,priority=1,kongs=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],repeats=1,base=_A,keywords=[],permitted_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]):'Create wrinkly hint text object.';D=repeats;C=priority;B=important;A.kongs=kongs.copy();A.hint=hint;A.important=B;A.priority=C;A.repeats=D;A.base=base;A.used=_A;A.was_important=B;A.original_repeats=D;A.original_priority=C;A.keywords=keywords.copy();A.permitted_levels=permitted_levels.copy()
	def use_hint(A):
		'Set hint as used.'
		if A.repeats==1:A.used=_B;A.repeats=0
		else:A.repeats-=1;A.priority+=1
	def downgrade(A):'Downgrade hint status.';A.important=_A
hint_list=[Hint(hint='Did you know - Donkey Kong officially features in Donkey Kong 64.',important=_A,base=_B),Hint(hint='Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie.',important=_A,base=_B),Hint(hint='Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick.',important=_A,base=_B),Hint(hint='Tiny Kong is the youngest sister of Dixie Kong.',important=_A,base=_B),Hint(hint='Mornin.',important=_A,base=_B),Hint(hint='Lanky Kong is the only kong with no canonical relation to the main Kong family tree.',important=_A,base=_B),Hint(hint='Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64.',important=_A,base=_B),Hint(hint='Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64.',important=_A,base=_B),Hint(hint='Candy Kong does not appear in Jungle Japes or Fungi Forest.',important=_A,base=_B),Hint(hint='If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight.',important=_A,base=_B),Hint(hint='Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021.',important=_A,base=_B),Hint(hint='The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes.',important=_A,base=_B),Hint(hint='Chunky Kong is the brother of Kiddy Kong.',important=_A,base=_B),Hint(hint='Fungi Forest contains mushrooms.',important=_A,base=_B),Hint(hint='Igloos can be found in Crystal Caves.',important=_A,base=_B),Hint(hint='Frantic Factory has multiple floors where things can be found.',important=_A,base=_B),Hint(hint="Angry Aztec has so much sand, it's even in the wind.",important=_A,base=_B),Hint(hint='DK Isles does not have a key.',important=_A,base=_B),Hint(hint='You can find a rabbit in Fungi Forest and in Crystal Caves.',important=_A,base=_B),Hint(hint='You can find a beetle in Angry Aztec and in Crystal Caves.',important=_A,base=_B),Hint(hint='You can find a vulture in Angry Aztec.',important=_A,base=_B),Hint(hint='You can find an owl in Fungi Forest.',important=_A,base=_B),Hint(hint='To buy moves, you will need coins.',important=_A,base=_B),Hint(hint='You can change the music and sound effects volume in the sound settings on the main menu.',important=_A,base=_B),Hint(hint='Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins.',important=_A,base=_B),Hint(hint='Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena.',important=_A,base=_B),Hint(hint='I have nothing to say to you.',important=_A,base=_B),Hint(hint='I had something to tell you, but I forgot what it is.',important=_A,base=_B),Hint(hint="I don't know anything.",important=_A,base=_B),Hint(hint="I'm as lost as you are. Good luck!",important=_A,base=_B),Hint(hint='Wrinkly? Never heard of him.',important=_A,base=_B),Hint(hint='This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes.',important=_A,base=_B),Hint(hint='Why do they call it oven when you of in the cold food of out hot eat the food?',important=_A,base=_B),Hint(hint='Wanna become famous? Buy followers, coconuts and donks at DK64Randomizer (DK64Randomizer . com)!',important=_A,base=_B),Hint(hint='What you gonna do, SpikeVegeta?',important=_A,base=_B)]
def pushHintToList(hint):'Push hint to hint list.';hint_list.append(hint)
def resetHintList():
	'Reset hint list to default state.'
	for A in hint_list:
		if not A.base:hint_list.remove(A)
		else:A.used=_A;A.important=A.was_important;A.repeats=A.original_repeats;A.priority=A.original_priority
def compileHints(spoiler):
	'Push hints to hint list based on settings.';Ad="'s in ";Ac='Cranky';Ab='Their first special move';Aa='Their third special move';AZ='Creepy Castle';AY='Crystal Caves';AX='Fungi Forest';AW='Gloomy Galleon';AV='Angry Aztec';AU='Chunky';AT='Donkey';A4='levels';A3='kongs';A2='Frantic Factory';A1='Jungle Japes';n='name_cryptic';b='color';a='cryptic';Z='purchase_kong';W='shared';P='moves';I='important';H='move_index';G='move_type';F='key';E='shop';D=spoiler;C='kong';B='level';A='name';resetHintList();A5=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
	if D.settings.krool_phase_order_rando:
		A6=f"K. Rool order is {NameFromKong(D.settings.krool_order[0])}"
		for K in range(len(D.settings.krool_order)):
			if K!=0:A6+=f" then {NameFromKong(D.settings.krool_order[K])}"
		hint_list.append(Hint(hint=A6,repeats=3,kongs=D.settings.krool_order.copy()))
	A7=[AT,'Diddy','Lanky','Tiny',AU];A8=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];Q=[A1,AV,A2,AW,AX,AY,AZ,'Hideout Helm'];X=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with sporadic gusts of sand','The level with two kongs to free','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with Cranky and Candy adjacent to each other'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level where it rains rocks','The level with two ice shields','The level with an Ice Tomato'],['The level with constant rain','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']]
	if D.settings.shuffle_items==P and D.move_data is not _C:
		Ae=[0,2,1,1,4];Af=0
		for K in D.settings.krool_order:Af+=Ae[K]
		s=[{A:'Monkeyport',n:Aa,F:3,C:3,G:0,H:3,B:0,E:0,I:_B},{A:'Mini Monkey',n:Ab,F:1,C:3,G:0,H:1,B:0,E:0,I:_B},{A:'Coconut Gun',n:'Their gun',F:33,C:0,G:2,H:1,B:0,E:0,I:_B},{A:'Chimpy Charge',n:Ab,F:1,C:1,G:0,H:1,B:0,E:0,I:_B},{A:'Gorilla Gone',n:Aa,F:3,C:4,G:0,H:3,B:0,E:0,I:_B},{A:'Ponytail Twirl',F:2,C:3,G:0,H:2,B:0,E:0,I:_A},{A:'Baboon Blast',F:1,C:0,G:0,H:1,B:0,E:0,I:_A},{A:'Strong Kong',F:2,C:0,G:0,H:2,B:0,E:0,I:_A},{A:'Gorilla Grab',F:3,C:0,G:0,H:3,B:0,E:0,I:_A},{A:'Rocketbarrel Boost',F:2,C:1,G:0,H:2,B:0,E:0,I:_A},{A:'Simian Spring',F:3,C:1,G:0,H:3,B:0,E:0,I:_A},{A:'Orangstand',F:1,C:2,G:0,H:1,B:0,E:0,I:_A},{A:'Baboon Balloon',F:2,C:2,G:0,H:2,B:0,E:0,I:_A},{A:'Orangstand Sprint',F:3,C:2,G:0,H:3,B:0,E:0,I:_A},{A:'Hunky Chunky',F:1,C:4,G:0,H:1,B:0,E:0,I:_A},{A:'Primate Punch',F:2,C:4,G:0,H:2,B:0,E:0,I:_A},{A:'Peanut Popguns',F:33,C:1,G:2,H:1,B:0,E:0,I:_A},{A:'Grape Shooter',F:33,C:2,G:2,H:1,B:0,E:0,I:_A},{A:'Feather Bow',F:33,C:3,G:2,H:1,B:0,E:0,I:_A},{A:'Pineapple Launcher',F:33,C:4,B:0,G:2,H:1,E:0,I:_A},{A:'Bongo Blast',F:65,C:0,G:4,H:1,B:0,E:0,I:_A},{A:'Guitar Gazump',F:65,C:1,G:4,H:1,B:0,E:0,I:_A},{A:'Trombone Tremor',F:65,C:2,G:4,H:1,B:0,E:0,I:_A},{A:'Saxophone Slam',F:65,C:3,G:4,H:1,B:0,E:0,I:_A},{A:'Triangle Trample',F:65,C:4,G:4,H:1,B:0,E:0,I:_A},{A:'Slam Upgrade',F:18,C:0,G:1,H:2,B:0,E:0,I:_A,W:_B},{A:'Homing Ammo',F:34,C:0,G:2,H:2,B:0,E:0,I:_A,W:_B},{A:'Sniper Scope',F:35,C:0,G:2,H:3,B:0,E:0,I:_A,W:_B},{A:'Ammo Belt Upgrade',F:50,C:0,G:3,H:2,B:0,E:0,I:_A,W:_B},{A:'Instrument Upgrade',F:66,C:0,G:4,H:2,B:0,E:0,I:_A,W:_B}];t=[Ac,'Funky','Candy'];As=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for J in s:J[F]=((J[G]&7)<<5)+((J[H]-1&3)<<3)+(J[C]&7);J[Z]=-1;J[B]=-1;J[E]=-1
		O={}
		for N in range(3):
			for o in range(5):
				for U in range(7):
					for J in s:
						if D.move_data[N][o][U]==J[F]:
							J[B]=U;J[E]=N;J[Z]=o
							if D.settings.wrinkly_hints==a:c=f"{t[N]}'s in {U}"
							else:c=f"{Q[U]} {t[N]}"
							u=_A
							if W in J:u=J[W]
							if c in O:
								if not u:O[c][P].append(J[A]);O[c][A3].append(o)
							else:
								A9=[o]
								if u:A9=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
								O[c]={P:[J[A]],A3:A9.copy()}
		AA=list(O.keys());random.shuffle(AA);v=[3,6,10];d=1;AB=_B
		for (Ag,N) in enumerate(AA):
			Y=N
			if Ad in Y:p=int(Y.split(Ad)[1].strip());Y=random.choice(X[p])
			if len(O[N][P])>2:e=', '.join(O[N][P][:-1]);e=f"{e} and {O[N][P][-1]}"
			elif len(O[N][P])==2:e=' and '.join(O[N][P])
			else:e=O[N][P][0]
			hint_list.append(Hint(hint=f"{Y} contains {e}",priority=d,important=AB,kongs=O[N][A3],keywords=O[N][P]))
			if d<=len(v):
				if Ag+1>=v[d-1]:
					if d==len(v):AB=_A
					else:d+=1
		for J in s:
			if J[B]>-1 and J[E]>-1 and J[Z]>-1:
				if D.settings.wrinkly_hints==a:f=random.choice(A8[J[Z]]);M=random.choice(X[J[B]])
				else:f=A7[J[Z]];M=Q[J[B]]
				Ah=J[A];Y=t[J[E]];Ai=f"{Ah} can be purchased from {Y} in {M}.";hint_list.append(Hint(hint=Ai,priority=2,kongs=[J[Z]],important=J[I],keywords=[J[A]]))
	if D.settings.kong_rando:
		AC=D.shuffled_kong_placement;Aj=[{A:A1,B:0},{A:'Llama Temple',B:1},{A:'Tiny Temple',B:1},{A:A2,B:2}]
		for w in Aj:
			g=AC[w[A]]['locked'][C];Ak=AC[w[A]]['puzzle'][C];p=w[B]
			if D.settings.wrinkly_hints==a:
				if not g==Kongs.any:f=random.choice(A8[g])
				M=random.choice(X[p])
			else:
				if not g==Kongs.any:f=A7[g]
				M=Q[p]
			AD=2
			if g==Kongs.any:f='An empty cage';AD=3
			hint_list.append(Hint(hint=f"{f} can be found in {M}.",kongs=[Ak],priority=AD))
	if D.settings.random_patches:
		q={'DK Isles':0,A1:0,AV:0,A2:0,AW:0,AX:0,AY:0,AZ:0}
		for Al in D.dirt_patch_placement:
			for U in q:
				if U in Al:q[U]+=1
		AE=list(q.keys());random.shuffle(AE)
		for h in range(2):
			for i in range(4):
				M=AE[i+4*h];x=q[M]
				if x>0:
					AF='patches';AG='are'
					if x==1:AF='patch';AG='is'
					y=f"There {AG} {x} {AF} in {M}";hint_list.append(Hint(hint=y,priority=i+3,important=h==0))
		AH=D.dirt_patch_placement.copy();random.shuffle(AH)
		for h in range(2):
			for i in range(4):Am=AH[i+h*4];y=f"There is a dirt patch located at {Am}";hint_list.append(Hint(hint=y,priority=i+4,important=h==0))
	if D.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(D)
	if D.settings.coin_door_open=='need_both'or D.settings.coin_door_open=='need_rw':hint_list.append(Hint(hint=f"{D.settings.medal_requirement} medals are required to access Jetpac.",priority=4))
	if D.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.'))
	if D.settings.level_randomization!='level_order':
		for K in D.settings.krool_keys_required:
			AI=K-4
			if D.settings.wrinkly_hints==a:M=random.choice(X[AI])
			else:M=Q[AI]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {M} to fight your greatest foe.",important=_A))
	An=['Candy','Funky',Ac];Ao=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];AJ=[A for A in D.woth.keys()if any((B in A for B in An))];Ap=random.sample(AJ,min(5,len(AJ)))
	for AK in Ap:
		AL=[A for A in Ao if A in AK]
		if len(AL)>0:Aq=str(AK).removesuffix(AL[0])
		hint_list.append(Hint(hint=f"{Aq} is on the Way of the Hoard."))
	Ar=[{C:AT,b:'Yellow'},{C:'Diddy',b:'Red'},{C:'Lanky',b:'Blue'},{C:'Tiny',b:'Purple'},{C:AU,b:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {Q[random.randint(0,6)]}, but also in other levels.",important=_A));AM=random.choice(Ar);hint_list.append(Hint(hint=f"{AM[C]} can find {AM[b]} bananas in {random.choice(Q)}.",important=_A));hint_list.append(Hint(hint=f"{D.settings.krool_key_count} Keys are required to reach K. Rool.",important=_A))
	if D.settings.shuffle_loading_zones==A4:
		j={}
		for K in range(7):j[D.settings.level_order[K+1]]=K
	for K in range(8):
		k=D.settings.EntryGBs[K];AN='Golden Bananas'
		if k==1:AN='Golden Banana'
		if D.settings.wrinkly_hints==a:M=random.choice(X[K])
		else:M=Q[K]
		AO=_A;V=A5.copy();l=K+1
		if D.settings.shuffle_loading_zones==A4:
			if K!=7:
				z=j[K];V=[]
				for m in range(7):
					if j[m]>=z:V.append(m)
			if K>3 and K<7:l=K-3;AO=_B
		hint_list.append(Hint(hint=f"The barrier to {M} can be cleared by obtaining {k} {AN}.",important=AO,priority=l,permitted_levels=V.copy()))
	for K in range(7):
		k=D.settings.BossBananas[K];AP='Small Bananas'
		if k==1:AP='Small Banana'
		if D.settings.wrinkly_hints==a:M=random.choice(X[K])
		else:M=Q[K]
		V=A5.copy()
		if D.settings.shuffle_loading_zones==A4:
			z=j[K];V=[]
			for m in range(7):
				if j[m]>=z:V.append(m)
		hint_list.append(Hint(hint=f"The barrier to the boss in {M} can be cleared by obtaining {k} {AP}.",important=_A,permitted_levels=V.copy()))
	random.shuffle(hint_list);l=1;AQ=_A
	while not AQ:
		AR=_A
		for L in hint_list:
			if L.important and L.priority==l and not L.used:
				AR=_B;r=updateRandomHint(L.hint,L.kongs.copy(),L.keywords.copy(),L.permitted_levels.copy())
				if r:L.use_hint()
				else:L.downgrade()
		if not AR:AQ=_B
		l+=1
	R=[];S=35
	for L in hint_list:
		if not L.important and not L.used:R.append(L)
		if L.used:
			S-=1
			if S<0:S=0
	random.shuffle(R);print(f"{S} unimportant hints placed ({int(S*100/35)}%)")
	if S>0:
		A0=0;AS=100;T=0
		while A0<S:
			r=_A
			if not R[T].used:r=updateRandomHint(R[T].hint,R[T].kongs,R[T].keywords.copy(),R[T].permitted_levels.copy())
			if r:L.use_hint();A0+=1
			else:AS-=1
			T+=1
			if T>=len(R):T=0
			if AS==0:
				for L in hints:
					if L.hint=='':L.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.'
				A0=S
	UpdateSpoilerHintList(D);return _B
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
def TryAddingLoadingZoneHint(spoiler,transition,useful_rating,disallowedRegions=_C):
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
	pushHintToList(Hint(hint=f"If you're looking for {C}, follow the path from {J}.",priority=useful_rating));return _B
def UpdateSpoilerHintList(spoiler):
	'Write hints to spoiler object.'
	for A in hints:
		if A.kong!=Kongs.any:spoiler.hint_list[A.name]=A.hint