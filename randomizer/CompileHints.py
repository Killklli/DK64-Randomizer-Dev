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
	'Push hints to hint list based on settings.';Ao='shop_dump';An="'s in ";Am='Cranky';Al='Their first special move';Ak='Their third special move';Aj='DK Isles';Ai='Chunky';Ah='Donkey';AG='Creepy Castle';AF='Crystal Caves';AE='Fungi Forest';AD='Gloomy Galleon';AC='Angry Aztec';z='levels';y='kongs';x='Frantic Factory';w='Jungle Japes';o='name_cryptic';g='color';f='cryptic';e='purchase_kong';Z='shared';S='moves';I='important';H='move_index';G='move_type';F='key';E='shop';D='kong';C='level';B='name';A=spoiler;resetHintList();AH=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
	if A.settings.krool_phase_order_rando and len(A.settings.krool_order)>1:
		AI=f"K. Rool order is {NameFromKong(A.settings.krool_order[0])}"
		for L in range(len(A.settings.krool_order)):
			if L!=0:AI+=f" then {NameFromKong(A.settings.krool_order[L])}"
		hint_list.append(Hint(hint=AI,repeats=2,kongs=A.settings.krool_order.copy(),subtype='k_rool'))
	AJ=[Ah,'Diddy','Lanky','Tiny',Ai];AK=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];V=[w,AC,x,AD,AE,AF,AG,'Hideout Helm'];Ap=[w,AC,x,AD,AE,AF,AG,Aj];a=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with four vases','The level with two kongs cages','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with a game from 1981','The level where you need two quarters to play'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level with two inches of water','The level with two ice shields','The level with an Ice Tomato'],['The level with battlements','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']];p=a.copy();p.remove(p[-1]);p.append(['The hub world',"The world with DK's ugly mug on it","The world with only a Cranky's Lab and Snide's HQ in it"])
	if A.settings.shuffle_items==S and A.move_data is not _C:
		Aq=[0,2,1,1,4];Ar=0
		for L in A.settings.krool_order:Ar+=Aq[L]
		A0=[{B:'Monkeyport',o:Ak,F:3,D:3,G:0,H:3,C:0,E:0,I:_B},{B:'Mini Monkey',o:Al,F:1,D:3,G:0,H:1,C:0,E:0,I:_B},{B:'Coconut Gun',o:'Their gun',F:33,D:0,G:2,H:1,C:0,E:0,I:_B},{B:'Chimpy Charge',o:Al,F:1,D:1,G:0,H:1,C:0,E:0,I:_B},{B:'Gorilla Gone',o:Ak,F:3,D:4,G:0,H:3,C:0,E:0,I:_B},{B:'Ponytail Twirl',F:2,D:3,G:0,H:2,C:0,E:0,I:_A},{B:'Baboon Blast',F:1,D:0,G:0,H:1,C:0,E:0,I:_A},{B:'Strong Kong',F:2,D:0,G:0,H:2,C:0,E:0,I:_A},{B:'Gorilla Grab',F:3,D:0,G:0,H:3,C:0,E:0,I:_A},{B:'Rocketbarrel Boost',F:2,D:1,G:0,H:2,C:0,E:0,I:_A},{B:'Simian Spring',F:3,D:1,G:0,H:3,C:0,E:0,I:_A},{B:'Orangstand',F:1,D:2,G:0,H:1,C:0,E:0,I:_A},{B:'Baboon Balloon',F:2,D:2,G:0,H:2,C:0,E:0,I:_A},{B:'Orangstand Sprint',F:3,D:2,G:0,H:3,C:0,E:0,I:_A},{B:'Hunky Chunky',F:1,D:4,G:0,H:1,C:0,E:0,I:_A},{B:'Primate Punch',F:2,D:4,G:0,H:2,C:0,E:0,I:_A},{B:'Peanut Popguns',F:33,D:1,G:2,H:1,C:0,E:0,I:_A},{B:'Grape Shooter',F:33,D:2,G:2,H:1,C:0,E:0,I:_A},{B:'Feather Bow',F:33,D:3,G:2,H:1,C:0,E:0,I:_A},{B:'Pineapple Launcher',F:33,D:4,C:0,G:2,H:1,E:0,I:_A},{B:'Bongo Blast',F:65,D:0,G:4,H:1,C:0,E:0,I:_A},{B:'Guitar Gazump',F:65,D:1,G:4,H:1,C:0,E:0,I:_A},{B:'Trombone Tremor',F:65,D:2,G:4,H:1,C:0,E:0,I:_A},{B:'Saxophone Slam',F:65,D:3,G:4,H:1,C:0,E:0,I:_A},{B:'Triangle Trample',F:65,D:4,G:4,H:1,C:0,E:0,I:_A},{B:'Slam Upgrade',F:18,D:0,G:1,H:2,C:0,E:0,I:_A,Z:_B},{B:'Homing Ammo',F:34,D:0,G:2,H:2,C:0,E:0,I:_A,Z:_B},{B:'Sniper Scope',F:35,D:0,G:2,H:3,C:0,E:0,I:_A,Z:_B},{B:'Ammo Belt Upgrade',F:50,D:0,G:3,H:2,C:0,E:0,I:_A,Z:_B},{B:'Instrument Upgrade',F:66,D:0,G:4,H:2,C:0,E:0,I:_A,Z:_B}];A1=[Am,'Funky','Candy'];BB=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for J in A0:J[F]=((J[G]&7)<<5)+((J[H]-1&3)<<3)+(J[D]&7);J[e]=-1;J[C]=-1;J[E]=-1
		O={}
		for N in range(3):
			for q in range(5):
				for W in range(8):
					for J in A0:
						if A.move_data[N][q][W]==J[F]:
							J[C]=W;J[E]=N;J[e]=q
							if A.settings.wrinkly_hints==f:h=f"{A1[N]}'s in {W}"
							else:h=f"{Ap[W]} {A1[N]}"
							A2=_A
							if Z in J:A2=J[Z]
							if h in O:
								if not A2:O[h][S].append(J[B]);O[h][y].append(q)
							else:
								AL=[q]
								if A2:AL=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
								O[h]={S:[J[B]],y:AL.copy()}
		AM=list(O.keys());random.shuffle(AM);A3=[3,6,10];i=1;A4=_B
		for (As,N) in enumerate(AM):
			X=N
			if An in X:r=int(X.split(An)[1].strip());X=random.choice(p[r])
			if len(O[N][S])>2:b=', '.join(O[N][S][:-1]);b=f"{b} and {O[N][S][-1]}"
			elif len(O[N][S])==2:b=' and '.join(O[N][S])
			else:b=O[N][S][0]
			hint_list.append(Hint(hint=f"{X} contains {b}",priority=i,important=A4,kongs=O[N][y],keywords=O[N][S],subtype=Ao))
			if A4:hint_list.append(Hint(hint=f"{X} contains {b}",important=_A,kongs=O[N][y],keywords=O[N][S],subtype=Ao))
			if i<=len(A3):
				if As+1>=A3[i-1]:
					if i==len(A3):A4=_A
					else:i+=1
		for J in A0:
			if J[C]>-1 and J[E]>-1 and J[e]>-1:
				if A.settings.wrinkly_hints==f:j=random.choice(AK[J[e]]);M=random.choice(a[J[C]])
				else:j=AJ[J[e]];M=V[J[C]]
				At=J[B];X=A1[J[E]];Au=f"{At} can be purchased from {X} in {M}.";hint_list.append(Hint(hint=Au,priority=2,kongs=[J[e]],important=J[I],keywords=[J[B]],subtype='move_location'))
	if A.settings.kong_rando:
		AN=A.shuffled_kong_placement;Av=[{B:w,C:0},{B:'Llama Temple',C:1},{B:'Tiny Temple',C:1},{B:x,C:2}]
		for A5 in Av:
			k=AN[A5[B]]['locked'][D];Aw=AN[A5[B]]['puzzle'][D];r=A5[C]
			if A.settings.wrinkly_hints==f:
				if not k==Kongs.any:j=random.choice(AK[k])
				M=random.choice(a[r])
			else:
				if not k==Kongs.any:j=AJ[k]
				M=V[r]
			AO=2
			if k==Kongs.any:j='An empty cage';AO=3
			hint_list.append(Hint(hint=f"{j} can be found in {M}.",kongs=[Aw],priority=AO,subtype='kong_location'))
	if A.settings.random_patches:
		s={Aj:0,w:0,AC:0,x:0,AD:0,AE:0,AF:0,AG:0}
		for Ax in A.dirt_patch_placement:
			for W in s:
				if W in Ax:s[W]+=1
		AP=list(s.keys());random.shuffle(AP)
		for t in range(2):
			for l in range(4):
				M=AP[l+4*t];A6=s[M]
				if A6>0:
					AQ='patches';AR='are'
					if A6==1:AQ='patch';AR='is'
					A7=f"There {AR} {A6} {AQ} in {M}";hint_list.append(Hint(hint=A7,priority=l+3,important=_A,subtype='level_patch_count'))
		AS=A.dirt_patch_placement.copy();random.shuffle(AS)
		for t in range(2):
			for l in range(4):Ay=AS[l+t*4];A7=f"There is a dirt patch located at {Ay}";hint_list.append(Hint(hint=A7,priority=l+4,important=t==0,subtype='patch_location'))
	if A.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(A)
	if A.settings.coin_door_open=='need_both'or A.settings.coin_door_open=='need_rw':hint_list.append(Hint(hint=f"{A.settings.medal_requirement} medals are required to access Jetpac.",priority=4,subtype='medal'))
	if A.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.',subtype='permadeath'))
	if A.settings.level_randomization!='level_order':
		for L in A.settings.krool_keys_required:
			AT=L-4
			if A.settings.wrinkly_hints==f:M=random.choice(a[AT])
			else:M=V[AT]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {M} to fight your greatest foe.",important=_A,subtype='key_is_required'))
	Az=['Candy','Funky',Am];A_=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];AU=[B for B in A.woth.keys()if any((A in B for A in Az))];B0=random.sample(AU,min(5,len(AU)));AV=random.randint(1,4)
	for AW in B0:
		AX=[A for A in A_ if A in AW]
		if len(AX)>0:B1=str(AW).removesuffix(AX[0])
		hint_list.append(Hint(hint=f"{B1} is on the Way of the Hoard.",important=random.choice([_B,_B,_A]),priority=AV,subtype='way_of_the_hoard'));AV+=random.randint(1,2)
	B2=[{D:Ah,g:'Yellow'},{D:'Diddy',g:'Red'},{D:'Lanky',g:'Blue'},{D:'Tiny',g:'Purple'},{D:Ai,g:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {V[random.randint(0,6)]}, but also in other levels.",important=_A,subtype=_D,joke=_B,joke_defined=_B));AY=random.choice(B2);hint_list.append(Hint(hint=f"{AY[D]} can find {AY[g]} bananas in {random.choice(V)}.",important=_A,subtype=_D,joke=_B,joke_defined=_B));hint_list.append(Hint(hint=f"{A.settings.krool_key_count} Keys are required to reach K. Rool.",important=_A,subtype='key_count_required'))
	if A.settings.shuffle_loading_zones==z:
		B3={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};B4={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle};A8={};u={};AZ=[]
		for (B5,Aa) in B3.items():Ab=B4[A.shuffled_exit_data[B5].reverse];A8[Ab]=Aa;u[Aa]=Ab
	if A.settings.randomize_blocker_required_amounts is _B and A.settings.shuffle_loading_zones==z:
		for B6 in list(u.values()):AZ.append(B6.name)
		for L in range(8):
			m=A.settings.EntryGBs[L];Ac='Golden Bananas'
			if m==1:Ac='Golden Banana'
			M=V[L];A9=_A;Y=AH.copy();c=L+1
			if A.settings.shuffle_loading_zones==z:
				if L!=7:
					AA=A8[L];Y=[]
					for n in range(7):
						if n<AA:Y.append(u[n])
					if M.replace(' ','')in AZ[4:7]:c=4;A9=_B
				if A.settings.maximize_helm_blocker is _A and L==7:c=1;A9=_B
			if A.settings.wrinkly_hints==f:M=random.choice(a[L])
			hint_list.append(Hint(hint=f"The barrier to {M} can be cleared by obtaining {m} {Ac}.",important=A9,priority=c,permitted_levels=Y.copy(),subtype='gb_amount'))
	for L in range(7):
		m=A.settings.BossBananas[L];Ad='Small Bananas'
		if m==1:Ad='Small Banana'
		if A.settings.wrinkly_hints==f:M=random.choice(a[L])
		else:M=V[L]
		Y=AH.copy()
		if A.settings.shuffle_loading_zones==z:
			AA=A8[L];Y=[]
			for n in range(7):
				if n<=AA:Y.append(u[n])
		hint_list.append(Hint(hint=f"The barrier to the boss in {M} can be cleared by obtaining {m} {Ad}.",important=_A,permitted_levels=Y.copy(),subtype='cb_amount'))
	R={};Q=[]
	for K in hint_list:
		if not K.important and not K.used and K.joke:Q.append(K)
	d=random.choice(Q);U=_A;B7=0
	while not U:
		U=updateRandomHint(d.hint,d.kongs.copy(),d.keywords.copy(),d.permitted_levels.copy())
		if U:
			d.use_hint();B7+=1;P=d.subtype
			if P in R:R[P]+=1
			else:R[P]=1
			break
	random.shuffle(hint_list);c=1;Ae=_A;B8=0
	while not Ae:
		Af=_A
		for K in hint_list:
			if K.important and K.priority==c and not K.used and not K.joke:
				Af=_B;U=updateRandomHint(K.hint,K.kongs.copy(),K.keywords.copy(),K.permitted_levels.copy())
				if U:
					K.use_hint();B8+=1;P=K.subtype
					if P in R:R[P]+=1
					else:R[P]=1
				else:K.downgrade()
		if not Af:Ae=_B
		c+=1
	Q=[];v=0
	for K in hint_list:
		if not K.important and not K.used and not K.joke:Q.append(K)
	for K in hints:
		if K.hint=='':v+=1
	random.shuffle(Q);B9=0;BA=0
	if v>0:
		AB=0;Ag=100;T=0
		while AB<v:
			U=_A
			if not Q[T].used:U=updateRandomHint(Q[T].hint,Q[T].kongs,Q[T].keywords.copy(),Q[T].permitted_levels.copy())
			if U:
				Q[T].use_hint();B9+=1;P=Q[T].subtype
				if P in R:R[P]+=1
				else:R[P]=1
				AB+=1
			else:Ag-=1
			T+=1
			if T>=len(Q):T=0
			if Ag==0:
				for K in hints:
					if K.hint=='':
						K.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.';P='error'
						if P in R:R[P]+=1
						else:R[P]=1
						BA+=1
				AB=v
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