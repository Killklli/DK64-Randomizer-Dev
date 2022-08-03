'Compile a list of hints based on the settings.'
_D='joke'
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
from randomizer.Enums.Transitions import Transitions
class Hint:
	'Hint object for Wrinkly hint text.'
	def __init__(A,*,hint='',important=_B,priority=1,kongs=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky],repeats=1,base=_A,keywords=[],permitted_levels=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle],subtype=_D,joke=_A,joke_defined=_A):
		'Create wrinkly hint text object.';D=repeats;C=priority;B=important;A.kongs=kongs.copy();A.hint=hint;A.important=B;A.priority=C;A.repeats=D;A.base=base;A.used=_A;A.was_important=B;A.original_repeats=D;A.original_priority=C;A.keywords=keywords.copy();A.permitted_levels=permitted_levels.copy();A.subtype=subtype;A.joke=base
		if joke_defined:A.joke=joke
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
	'Push hints to hint list based on settings.';Ar='shop_dump';Aq="'s in ";Ap='Cranky';Ao='Their first special move';An='Their third special move';Am='DK Isles';Al='Chunky';Ak='Donkey';AI='levels';AH='Creepy Castle';AG='Crystal Caves';AF='Fungi Forest';AE='Gloomy Galleon';AD='Angry Aztec';x='kongs';w='Frantic Factory';v='Jungle Japes';p='name_cryptic';f='color';e='cryptic';d='purchase_kong';Z='shared';S='moves';I='important';H='move_index';G='move_type';F='key';E='shop';D=spoiler;C='kong';B='level';A='name';resetHintList();AJ=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
	if D.settings.krool_phase_order_rando and len(D.settings.krool_order)>1:
		AK=f"K. Rool order is {NameFromKong(D.settings.krool_order[0])}"
		for L in range(len(D.settings.krool_order)):
			if L!=0:AK+=f" then {NameFromKong(D.settings.krool_order[L])}"
		hint_list.append(Hint(hint=AK,repeats=2,kongs=D.settings.krool_order.copy(),subtype='k_rool'))
	AL=[Ak,'Diddy','Lanky','Tiny',Al];AM=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];V=[v,AD,w,AE,AF,AG,AH,'Hideout Helm'];As=[v,AD,w,AE,AF,AG,AH,Am];a=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with sporadic gusts of sand','The level with two kongs to free','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with Cranky and Candy adjacent to each other'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level where it rains rocks','The level with two ice shields','The level with an Ice Tomato'],['The level with constant rain','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']];q=a.copy();q.remove(q[-1]);q.append(['The hub world',"The world with DK's ugly mug on it","The world with only a Cranky's Lab and Snide's HQ in it"])
	if D.settings.shuffle_items==S and D.move_data is not _C:
		At=[0,2,1,1,4];Au=0
		for L in D.settings.krool_order:Au+=At[L]
		y=[{A:'Monkeyport',p:An,F:3,C:3,G:0,H:3,B:0,E:0,I:_B},{A:'Mini Monkey',p:Ao,F:1,C:3,G:0,H:1,B:0,E:0,I:_B},{A:'Coconut Gun',p:'Their gun',F:33,C:0,G:2,H:1,B:0,E:0,I:_B},{A:'Chimpy Charge',p:Ao,F:1,C:1,G:0,H:1,B:0,E:0,I:_B},{A:'Gorilla Gone',p:An,F:3,C:4,G:0,H:3,B:0,E:0,I:_B},{A:'Ponytail Twirl',F:2,C:3,G:0,H:2,B:0,E:0,I:_A},{A:'Baboon Blast',F:1,C:0,G:0,H:1,B:0,E:0,I:_A},{A:'Strong Kong',F:2,C:0,G:0,H:2,B:0,E:0,I:_A},{A:'Gorilla Grab',F:3,C:0,G:0,H:3,B:0,E:0,I:_A},{A:'Rocketbarrel Boost',F:2,C:1,G:0,H:2,B:0,E:0,I:_A},{A:'Simian Spring',F:3,C:1,G:0,H:3,B:0,E:0,I:_A},{A:'Orangstand',F:1,C:2,G:0,H:1,B:0,E:0,I:_A},{A:'Baboon Balloon',F:2,C:2,G:0,H:2,B:0,E:0,I:_A},{A:'Orangstand Sprint',F:3,C:2,G:0,H:3,B:0,E:0,I:_A},{A:'Hunky Chunky',F:1,C:4,G:0,H:1,B:0,E:0,I:_A},{A:'Primate Punch',F:2,C:4,G:0,H:2,B:0,E:0,I:_A},{A:'Peanut Popguns',F:33,C:1,G:2,H:1,B:0,E:0,I:_A},{A:'Grape Shooter',F:33,C:2,G:2,H:1,B:0,E:0,I:_A},{A:'Feather Bow',F:33,C:3,G:2,H:1,B:0,E:0,I:_A},{A:'Pineapple Launcher',F:33,C:4,B:0,G:2,H:1,E:0,I:_A},{A:'Bongo Blast',F:65,C:0,G:4,H:1,B:0,E:0,I:_A},{A:'Guitar Gazump',F:65,C:1,G:4,H:1,B:0,E:0,I:_A},{A:'Trombone Tremor',F:65,C:2,G:4,H:1,B:0,E:0,I:_A},{A:'Saxophone Slam',F:65,C:3,G:4,H:1,B:0,E:0,I:_A},{A:'Triangle Trample',F:65,C:4,G:4,H:1,B:0,E:0,I:_A},{A:'Slam Upgrade',F:18,C:0,G:1,H:2,B:0,E:0,I:_A,Z:_B},{A:'Homing Ammo',F:34,C:0,G:2,H:2,B:0,E:0,I:_A,Z:_B},{A:'Sniper Scope',F:35,C:0,G:2,H:3,B:0,E:0,I:_A,Z:_B},{A:'Ammo Belt Upgrade',F:50,C:0,G:3,H:2,B:0,E:0,I:_A,Z:_B},{A:'Instrument Upgrade',F:66,C:0,G:4,H:2,B:0,E:0,I:_A,Z:_B}];z=[Ap,'Funky','Candy'];B9=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for J in y:J[F]=((J[G]&7)<<5)+((J[H]-1&3)<<3)+(J[C]&7);J[d]=-1;J[B]=-1;J[E]=-1
		O={}
		for N in range(3):
			for r in range(5):
				for W in range(8):
					for J in y:
						if D.move_data[N][r][W]==J[F]:
							J[B]=W;J[E]=N;J[d]=r
							if D.settings.wrinkly_hints==e:g=f"{z[N]}'s in {W}"
							else:g=f"{As[W]} {z[N]}"
							A0=_A
							if Z in J:A0=J[Z]
							if g in O:
								if not A0:O[g][S].append(J[A]);O[g][x].append(r)
							else:
								AN=[r]
								if A0:AN=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
								O[g]={S:[J[A]],x:AN.copy()}
		AO=list(O.keys());random.shuffle(AO);A1=[3,6,10];h=1;A2=_B
		for (Av,N) in enumerate(AO):
			X=N
			if Aq in X:s=int(X.split(Aq)[1].strip());X=random.choice(q[s])
			if len(O[N][S])>2:b=', '.join(O[N][S][:-1]);b=f"{b} and {O[N][S][-1]}"
			elif len(O[N][S])==2:b=' and '.join(O[N][S])
			else:b=O[N][S][0]
			hint_list.append(Hint(hint=f"{X} contains {b}",priority=h,important=A2,kongs=O[N][x],keywords=O[N][S],subtype=Ar))
			if A2:hint_list.append(Hint(hint=f"{X} contains {b}",important=_A,kongs=O[N][x],keywords=O[N][S],subtype=Ar))
			if h<=len(A1):
				if Av+1>=A1[h-1]:
					if h==len(A1):A2=_A
					else:h+=1
		for J in y:
			if J[B]>-1 and J[E]>-1 and J[d]>-1:
				if D.settings.wrinkly_hints==e:i=random.choice(AM[J[d]]);M=random.choice(a[J[B]])
				else:i=AL[J[d]];M=V[J[B]]
				Aw=J[A];X=z[J[E]];Ax=f"{Aw} can be purchased from {X} in {M}.";hint_list.append(Hint(hint=Ax,priority=2,kongs=[J[d]],important=J[I],keywords=[J[A]],subtype='move_location'))
	if D.settings.kong_rando:
		AP=D.shuffled_kong_placement;Ay=[{A:v,B:0},{A:'Llama Temple',B:1},{A:'Tiny Temple',B:1},{A:w,B:2}]
		for A3 in Ay:
			j=AP[A3[A]]['locked'][C];Az=AP[A3[A]]['puzzle'][C];s=A3[B]
			if D.settings.wrinkly_hints==e:
				if not j==Kongs.any:i=random.choice(AM[j])
				M=random.choice(a[s])
			else:
				if not j==Kongs.any:i=AL[j]
				M=V[s]
			AQ=2
			if j==Kongs.any:i='An empty cage';AQ=3
			hint_list.append(Hint(hint=f"{i} can be found in {M}.",kongs=[Az],priority=AQ,subtype='kong_location'))
	if D.settings.random_patches:
		t={Am:0,v:0,AD:0,w:0,AE:0,AF:0,AG:0,AH:0}
		for A_ in D.dirt_patch_placement:
			for W in t:
				if W in A_:t[W]+=1
		AR=list(t.keys());random.shuffle(AR)
		for k in range(2):
			for l in range(4):
				M=AR[l+4*k];A4=t[M]
				if A4>0:
					AS='patches';AT='are'
					if A4==1:AS='patch';AT='is'
					A5=f"There {AT} {A4} {AS} in {M}";hint_list.append(Hint(hint=A5,priority=l+3,important=k==0,subtype='level_patch_count'))
		AU=D.dirt_patch_placement.copy();random.shuffle(AU)
		for k in range(2):
			for l in range(4):B0=AU[l+k*4];A5=f"There is a dirt patch located at {B0}";hint_list.append(Hint(hint=A5,priority=l+4,important=k==0,subtype='patch_location'))
	if D.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(D)
	if D.settings.coin_door_open=='need_both'or D.settings.coin_door_open=='need_rw':hint_list.append(Hint(hint=f"{D.settings.medal_requirement} medals are required to access Jetpac.",priority=4,subtype='medal'))
	if D.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.',subtype='permadeath'))
	if D.settings.level_randomization!='level_order':
		for L in D.settings.krool_keys_required:
			AV=L-4
			if D.settings.wrinkly_hints==e:M=random.choice(a[AV])
			else:M=V[AV]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {M} to fight your greatest foe.",important=_A,subtype='key_is_required'))
	B1=['Candy','Funky',Ap];B2=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];AW=[A for A in D.woth.keys()if any((B in A for B in B1))];B3=random.sample(AW,min(5,len(AW)));AX=random.randint(1,4)
	for AY in B3:
		AZ=[A for A in B2 if A in AY]
		if len(AZ)>0:B4=str(AY).removesuffix(AZ[0])
		hint_list.append(Hint(hint=f"{B4} is on the Way of the Hoard.",important=random.choice([_B,_B,_A]),priority=AX,subtype='way_of_the_hoard'));AX+=random.randint(1,2)
	B5=[{C:Ak,f:'Yellow'},{C:'Diddy',f:'Red'},{C:'Lanky',f:'Blue'},{C:'Tiny',f:'Purple'},{C:Al,f:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {V[random.randint(0,6)]}, but also in other levels.",important=_A,subtype=_D,joke=_B,joke_defined=_B));Aa=random.choice(B5);hint_list.append(Hint(hint=f"{Aa[C]} can find {Aa[f]} bananas in {random.choice(V)}.",important=_A,subtype=_D,joke=_B,joke_defined=_B));hint_list.append(Hint(hint=f"{D.settings.krool_key_count} Keys are required to reach K. Rool.",important=_A,subtype='key_count_required'))
	if D.settings.shuffle_loading_zones==AI:
		B6={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};B7={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle};A6={};A7={}
		for (B8,Ab) in B6.items():Ac=B7[D.shuffled_exit_data[B8].reverse];A6[Ac]=Ab;A7[Ab]=Ac
	for L in range(8):
		m=D.settings.EntryGBs[L];Ad='Golden Bananas'
		if m==1:Ad='Golden Banana'
		if D.settings.wrinkly_hints==e:M=random.choice(a[L])
		else:M=V[L]
		Ae=_A;Y=AJ.copy();n=L+1
		if D.settings.shuffle_loading_zones==AI:
			if L!=7:
				A8=A6[L];Y=[]
				for o in range(7):
					if o<A8:Y.append(A7[o])
			if L>3 and L<8:n=9-L;Ae=_B
		hint_list.append(Hint(hint=f"The barrier to {M} can be cleared by obtaining {m} {Ad}.",important=Ae,priority=n,permitted_levels=Y.copy(),subtype='gb_amount'))
	for L in range(7):
		m=D.settings.BossBananas[L];Af='Small Bananas'
		if m==1:Af='Small Banana'
		if D.settings.wrinkly_hints==e:M=random.choice(a[L])
		else:M=V[L]
		Y=AJ.copy()
		if D.settings.shuffle_loading_zones==AI:
			A8=A6[L];Y=[]
			for o in range(7):
				if o<=A8:Y.append(A7[o])
		hint_list.append(Hint(hint=f"The barrier to the boss in {M} can be cleared by obtaining {m} {Af}.",important=_A,permitted_levels=Y.copy(),subtype='cb_amount'))
	Q={};R=[]
	for K in hint_list:
		if not K.important and not K.used and K.joke:R.append(K)
	c=random.choice(R);U=_A;A9=0
	while not U:
		U=updateRandomHint(c.hint,c.kongs.copy(),c.keywords.copy(),c.permitted_levels.copy())
		if U:
			c.use_hint();A9+=1;P=c.subtype
			if P in Q:Q[P]+=1
			else:Q[P]=1
			break
	random.shuffle(hint_list);n=1;Ag=_A;AA=0
	while not Ag:
		Ah=_A
		for K in hint_list:
			if K.important and K.priority==n and not K.used and not K.joke:
				Ah=_B;U=updateRandomHint(K.hint,K.kongs.copy(),K.keywords.copy(),K.permitted_levels.copy())
				if U:
					K.use_hint();AA+=1;P=K.subtype
					if P in Q:Q[P]+=1
					else:Q[P]=1
				else:K.downgrade()
		if not Ah:Ag=_B
		n+=1
	R=[];u=0
	for K in hint_list:
		if not K.important and not K.used and not K.joke:R.append(K)
	for K in hints:
		if K.hint=='':u+=1
	random.shuffle(R);AB=0;Ai=0
	if u>0:
		AC=0;Aj=100;T=0
		while AC<u:
			U=_A
			if not R[T].used:U=updateRandomHint(R[T].hint,R[T].kongs,R[T].keywords.copy(),R[T].permitted_levels.copy())
			if U:
				R[T].use_hint();AB+=1;P=R[T].subtype
				if P in Q:Q[P]+=1
				else:Q[P]=1
				AC+=1
			else:Aj-=1
			T+=1
			if T>=len(R):T=0
			if Aj==0:
				for K in hints:
					if K.hint=='':
						K.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.';P='error'
						if P in Q:Q[P]+=1
						else:Q[P]=1
						Ai+=1
				AC=u
	print(f"Hint Distribution | Important: {AA}, Unimportant: {AB}, Jokes: {A9}, Errors: {Ai}, Total Good: {AA+AB+A9}");print(f"Hint JSON: {Q}");UpdateSpoilerHintList(D);return _B
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
	pushHintToList(Hint(hint=f"If you're looking for {C}, follow the path from {J}.",priority=useful_rating,subtype='lzr'));return _B
def UpdateSpoilerHintList(spoiler):
	'Write hints to spoiler object.'
	for A in hints:
		if A.kong!=Kongs.any:spoiler.hint_list[A.name]=A.hint