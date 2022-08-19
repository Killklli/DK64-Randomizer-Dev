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
	'Push hints to hint list based on settings.';Ar='shop_dump';Aq="'s in ";Ap='Cranky';Ao='Their first special move';An='Their third special move';Am='DK Isles';Al='Chunky';Ak='Donkey';Aj='k_rool';AI='Creepy Castle';AH='Crystal Caves';AG='Fungi Forest';AF='Gloomy Galleon';AE='Angry Aztec';A1='levels';A0='kongs';z='Frantic Factory';y='Jungle Japes';q='name_cryptic';g='color';f='cryptic';e='purchase_kong';Z='shared';S='moves';J='important';I='move_index';H='move_type';G='key';E='shop';D='kong';C='level';B='name';A=spoiler;resetHintList();AJ=[Levels.JungleJapes,Levels.AngryAztec,Levels.FranticFactory,Levels.GloomyGalleon,Levels.FungiForest,Levels.CrystalCaves,Levels.CreepyCastle]
	if A.settings.krool_phase_order_rando and len(A.settings.krool_order)>1:
		h=f"K. Rool order is {NameFromKong(A.settings.krool_order[0])}"
		for L in range(len(A.settings.krool_order)):
			if L!=0:h+=f" then {NameFromKong(A.settings.krool_order[L])}"
		hint_list.append(Hint(hint=h,repeats=2,kongs=A.settings.krool_order.copy(),subtype=Aj))
	As=[Kongs.donkey,Kongs.chunky,Kongs.tiny,Kongs.lanky,Kongs.diddy];i=[]
	if A.settings.helm_phase_order_rando and len(A.settings.helm_order)>1:
		for At in A.settings.helm_order:i.append(As[At])
		h=f"Helm Room order is {NameFromKong(i[0])}"
		for L in range(len(i)):
			if L!=0:h+=f" then {NameFromKong(i[L])}"
		hint_list.append(Hint(hint=h,repeats=3,kongs=i.copy(),subtype=Aj))
	AK=[Ak,'Diddy','Lanky','Tiny',Al];AL=[['The kong who is bigger, faster and potentially stronger too','The kong who fires in spurts','The kong with a tie','The kong who slaps their instrument to the jungle beat'],['The kong who can fly real high','The kong who features in the first two Donkey Kong Country games','The kong who wants to see red','The kong who frees the only female playable kong'],['The kong who inflates like a balloon, just like a balloon','The kong who waddles in his overalls','The kong who has a cold race with an insect','The kong who lacks style, grace but not a funny face'],['The kong who likes jazz',"The kong who shoots K. Rool's tiny toes",'The kong who has ammo that is light as a feather','The kong who can shrink in size'],['The kong who is one hell of a guy','The kong who can pick up boulders','The kong who fights a blocky boss','The kong who bows down to a dragonfly']];V=[y,AE,z,AF,AG,AH,AI,'Hideout Helm'];Au=[y,AE,z,AF,AG,AH,AI,Am];a=[['The level with a localized storm','The level with a dirt mountain','The level which has two retailers and no race'],['The level with four vases','The level with two kongs cages','The level with a spinning totem'],['The level with a toy production facility','The level with a tower of blocks','The level with a game from 1981','The level where you need two quarters to play'],['The level with the most water','The level where you free a water dweller','The level with stacks of gold'],['The level with only two retailers and two races','The level where night can be acquired at will','The level with a nocturnal tree dweller'],['The level with two inches of water','The level with two ice shields','The level with an Ice Tomato'],['The level with battlements','The level with a dungeon, ballroom and a library','The level with drawbridge and a moat'],['The timed level','The level with no boss','The level with no small bananas']];r=a.copy();r.remove(r[-1]);r.append(['The hub world',"The world with DK's ugly mug on it","The world with only a Cranky's Lab and Snide's HQ in it"])
	if A.settings.shuffle_items==S and A.move_data is not _C:
		Av=[0,2,1,1,4];Aw=0
		for L in A.settings.krool_order:Aw+=Av[L]
		A2=[{B:'Monkeyport',q:An,G:3,D:3,H:0,I:3,C:0,E:0,J:_B},{B:'Mini Monkey',q:Ao,G:1,D:3,H:0,I:1,C:0,E:0,J:_B},{B:'Coconut Gun',q:'Their gun',G:33,D:0,H:2,I:1,C:0,E:0,J:_B},{B:'Chimpy Charge',q:Ao,G:1,D:1,H:0,I:1,C:0,E:0,J:_B},{B:'Gorilla Gone',q:An,G:3,D:4,H:0,I:3,C:0,E:0,J:_B},{B:'Ponytail Twirl',G:2,D:3,H:0,I:2,C:0,E:0,J:_A},{B:'Baboon Blast',G:1,D:0,H:0,I:1,C:0,E:0,J:_A},{B:'Strong Kong',G:2,D:0,H:0,I:2,C:0,E:0,J:_A},{B:'Gorilla Grab',G:3,D:0,H:0,I:3,C:0,E:0,J:_A},{B:'Rocketbarrel Boost',G:2,D:1,H:0,I:2,C:0,E:0,J:_A},{B:'Simian Spring',G:3,D:1,H:0,I:3,C:0,E:0,J:_A},{B:'Orangstand',G:1,D:2,H:0,I:1,C:0,E:0,J:_A},{B:'Baboon Balloon',G:2,D:2,H:0,I:2,C:0,E:0,J:_A},{B:'Orangstand Sprint',G:3,D:2,H:0,I:3,C:0,E:0,J:_A},{B:'Hunky Chunky',G:1,D:4,H:0,I:1,C:0,E:0,J:_A},{B:'Primate Punch',G:2,D:4,H:0,I:2,C:0,E:0,J:_A},{B:'Peanut Popguns',G:33,D:1,H:2,I:1,C:0,E:0,J:_A},{B:'Grape Shooter',G:33,D:2,H:2,I:1,C:0,E:0,J:_A},{B:'Feather Bow',G:33,D:3,H:2,I:1,C:0,E:0,J:_A},{B:'Pineapple Launcher',G:33,D:4,C:0,H:2,I:1,E:0,J:_A},{B:'Bongo Blast',G:65,D:0,H:4,I:1,C:0,E:0,J:_A},{B:'Guitar Gazump',G:65,D:1,H:4,I:1,C:0,E:0,J:_A},{B:'Trombone Tremor',G:65,D:2,H:4,I:1,C:0,E:0,J:_A},{B:'Saxophone Slam',G:65,D:3,H:4,I:1,C:0,E:0,J:_A},{B:'Triangle Trample',G:65,D:4,H:4,I:1,C:0,E:0,J:_A},{B:'Slam Upgrade',G:18,D:0,H:1,I:2,C:0,E:0,J:_A,Z:_B},{B:'Homing Ammo',G:34,D:0,H:2,I:2,C:0,E:0,J:_A,Z:_B},{B:'Sniper Scope',G:35,D:0,H:2,I:3,C:0,E:0,J:_A,Z:_B},{B:'Ammo Belt Upgrade',G:50,D:0,H:3,I:2,C:0,E:0,J:_A,Z:_B},{B:'Instrument Upgrade',G:66,D:0,H:4,I:2,C:0,E:0,J:_A,Z:_B}];A3=[Ap,'Funky','Candy'];BG=[['The shop owner with a walking stick','The shop owner who is old','The shop owner who is persistently grumpy','The shop owner who resides near your Treehouse'],['The shop owner who has an armory','The shop owner who has a banana on his shop','The shop owner with sunglasses','The shop owner who calls everyone Dude'],['The shop owner who is flirtatious','The shop owner who is not present in Fungi Forest','The shop owner who is not present in Jungle Japes','The shop owner with blonde hair']]
		for K in A2:K[G]=((K[H]&7)<<5)+((K[I]-1&3)<<3)+(K[D]&7);K[e]=-1;K[C]=-1;K[E]=-1
		O={}
		for N in range(3):
			for s in range(5):
				for W in range(8):
					for K in A2:
						if A.move_data[N][s][W]==K[G]:
							K[C]=W;K[E]=N;K[e]=s
							if A.settings.wrinkly_hints==f:j=f"{A3[N]}'s in {W}"
							else:j=f"{Au[W]} {A3[N]}"
							A4=_A
							if Z in K:A4=K[Z]
							if j in O:
								if not A4:O[j][S].append(K[B]);O[j][A0].append(s)
							else:
								AM=[s]
								if A4:AM=[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]
								O[j]={S:[K[B]],A0:AM.copy()}
		AN=list(O.keys());random.shuffle(AN);A5=[3,6,10];k=1;A6=_B
		for (Ax,N) in enumerate(AN):
			X=N
			if Aq in X:t=int(X.split(Aq)[1].strip());X=random.choice(r[t])
			if len(O[N][S])>2:b=', '.join(O[N][S][:-1]);b=f"{b} and {O[N][S][-1]}"
			elif len(O[N][S])==2:b=' and '.join(O[N][S])
			else:b=O[N][S][0]
			hint_list.append(Hint(hint=f"{X} contains {b}",priority=k,important=A6,kongs=O[N][A0],keywords=O[N][S],subtype=Ar))
			if A6:hint_list.append(Hint(hint=f"{X} contains {b}",important=_A,kongs=O[N][A0],keywords=O[N][S],subtype=Ar))
			if k<=len(A5):
				if Ax+1>=A5[k-1]:
					if k==len(A5):A6=_A
					else:k+=1
		for K in A2:
			if K[C]>-1 and K[E]>-1 and K[e]>-1:
				if A.settings.wrinkly_hints==f:l=random.choice(AL[K[e]]);M=random.choice(a[K[C]])
				else:l=AK[K[e]];M=V[K[C]]
				Ay=K[B];X=A3[K[E]];Az=f"{Ay} can be purchased from {X} in {M}.";hint_list.append(Hint(hint=Az,priority=2,kongs=[K[e]],important=K[J],keywords=[K[B]],subtype='move_location'))
	if A.settings.kong_rando:
		AO=A.shuffled_kong_placement;A_=[{B:y,C:0},{B:'Llama Temple',C:1},{B:'Tiny Temple',C:1},{B:z,C:2}]
		for A7 in A_:
			m=AO[A7[B]]['locked'][D];B0=AO[A7[B]]['puzzle'][D];t=A7[C]
			if A.settings.wrinkly_hints==f:
				if not m==Kongs.any:l=random.choice(AL[m])
				M=random.choice(a[t])
			else:
				if not m==Kongs.any:l=AK[m]
				M=V[t]
			AP=2
			if m==Kongs.any:l='An empty cage';AP=3
			hint_list.append(Hint(hint=f"{l} can be found in {M}.",kongs=[B0],priority=AP,subtype='kong_location'))
	if A.settings.random_patches:
		u={Am:0,y:0,AE:0,z:0,AF:0,AG:0,AH:0,AI:0}
		for B1 in A.dirt_patch_placement:
			for W in u:
				if W in B1:u[W]+=1
		AQ=list(u.keys());random.shuffle(AQ)
		for v in range(2):
			for n in range(4):
				M=AQ[n+4*v];A8=u[M]
				if A8>0:
					AR='patches';AS='are'
					if A8==1:AR='patch';AS='is'
					A9=f"There {AS} {A8} {AR} in {M}";hint_list.append(Hint(hint=A9,priority=n+3,important=_A,subtype='level_patch_count'))
		AT=A.dirt_patch_placement.copy();random.shuffle(AT)
		for v in range(2):
			for n in range(4):B2=AT[n+v*4];A9=f"There is a dirt patch located at {B2}";hint_list.append(Hint(hint=A9,priority=n+4,important=v==0,subtype='patch_location'))
	if A.settings.shuffle_loading_zones=='all':AddLoadingZoneHints(A)
	if A.settings.coin_door_open=='need_both'or A.settings.coin_door_open=='need_rw':hint_list.append(Hint(hint=f"{A.settings.medal_requirement} medals are required to access Jetpac.",priority=4,subtype='medal'))
	if A.settings.perma_death:hint_list.append(Hint(hint='The curse can only be removed upon disabling K. Rools machine.',subtype='permadeath'))
	if A.settings.level_randomization!='level_order':
		for L in A.settings.krool_keys_required:
			AU=L-4
			if A.settings.wrinkly_hints==f:M=random.choice(a[AU])
			else:M=V[AU]
			hint_list.append(Hint(hint=f"You will need to obtain the key from {M} to fight your greatest foe.",important=_A,subtype='key_is_required'))
	B3=['Candy','Funky',Ap];B4=[' Donkey',' Diddy',' Lanky',' Tiny',' Chunky',' Shared'];AV=[B for B in A.woth.keys()if any((A in B for A in B3))];B5=random.sample(AV,min(5,len(AV)));AW=random.randint(1,4)
	for AX in B5:
		AY=[A for A in B4 if A in AX]
		if len(AY)>0:B6=str(AX).removesuffix(AY[0])
		hint_list.append(Hint(hint=f"{B6} is on the Way of the Hoard.",important=random.choice([_B,_B,_A]),priority=AW,subtype='way_of_the_hoard'));AW+=random.randint(1,2)
	B7=[{D:Ak,g:'Yellow'},{D:'Diddy',g:'Red'},{D:'Lanky',g:'Blue'},{D:'Tiny',g:'Purple'},{D:Al,g:'Green'}];hint_list.append(Hint(hint=f"You can find bananas in {V[random.randint(0,6)]}, but also in other levels.",important=_A,subtype=_D,joke=_B,joke_defined=_B));AZ=random.choice(B7);hint_list.append(Hint(hint=f"{AZ[D]} can find {AZ[g]} bananas in {random.choice(V)}.",important=_A,subtype=_D,joke=_B,joke_defined=_B));hint_list.append(Hint(hint=f"{A.settings.krool_key_count} Keys are required to reach K. Rool.",important=_A,subtype='key_count_required'))
	if A.settings.shuffle_loading_zones==A1:
		B8={Transitions.IslesMainToJapesLobby:Levels.JungleJapes,Transitions.IslesMainToAztecLobby:Levels.AngryAztec,Transitions.IslesMainToFactoryLobby:Levels.FranticFactory,Transitions.IslesMainToGalleonLobby:Levels.GloomyGalleon,Transitions.IslesMainToForestLobby:Levels.FungiForest,Transitions.IslesMainToCavesLobby:Levels.CrystalCaves,Transitions.IslesMainToCastleLobby:Levels.CreepyCastle};B9={Transitions.IslesJapesLobbyToMain:Levels.JungleJapes,Transitions.IslesAztecLobbyToMain:Levels.AngryAztec,Transitions.IslesFactoryLobbyToMain:Levels.FranticFactory,Transitions.IslesGalleonLobbyToMain:Levels.GloomyGalleon,Transitions.IslesForestLobbyToMain:Levels.FungiForest,Transitions.IslesCavesLobbyToMain:Levels.CrystalCaves,Transitions.IslesCastleLobbyToMain:Levels.CreepyCastle};AA={};w={};Aa=[]
		for (BA,Ab) in B8.items():Ac=B9[A.shuffled_exit_data[BA].reverse];AA[Ac]=Ab;w[Ab]=Ac
	if A.settings.randomize_blocker_required_amounts is _B and A.settings.shuffle_loading_zones==A1:
		for BB in list(w.values()):Aa.append(BB.name)
		for L in range(8):
			o=A.settings.EntryGBs[L];Ad='Golden Bananas'
			if o==1:Ad='Golden Banana'
			M=V[L];AB=_A;Y=AJ.copy();c=L+1
			if A.settings.shuffle_loading_zones==A1:
				if L!=7:
					AC=AA[L];Y=[]
					for p in range(7):
						if p<AC:Y.append(w[p])
					if M.replace(' ','')in Aa[4:7]:c=4;AB=_B
				if A.settings.maximize_helm_blocker is _A and L==7:c=1;AB=_B
			if A.settings.wrinkly_hints==f:M=random.choice(a[L])
			hint_list.append(Hint(hint=f"The barrier to {M} can be cleared by obtaining {o} {Ad}.",important=AB,priority=c,permitted_levels=Y.copy(),subtype='gb_amount'))
	for L in range(7):
		o=A.settings.BossBananas[L];Ae='Small Bananas'
		if o==1:Ae='Small Banana'
		if A.settings.wrinkly_hints==f:M=random.choice(a[L])
		else:M=V[L]
		Y=AJ.copy()
		if A.settings.shuffle_loading_zones==A1:
			AC=AA[L];Y=[]
			for p in range(7):
				if p<=AC:Y.append(w[p])
		hint_list.append(Hint(hint=f"The barrier to the boss in {M} can be cleared by obtaining {o} {Ae}.",important=_A,permitted_levels=Y.copy(),subtype='cb_amount'))
	R={};Q=[]
	for F in hint_list:
		if not F.important and not F.used and F.joke:Q.append(F)
	d=random.choice(Q);U=_A;BC=0
	while not U:
		U=updateRandomHint(d.hint,d.kongs.copy(),d.keywords.copy(),d.permitted_levels.copy())
		if U:
			d.use_hint();BC+=1;P=d.subtype
			if P in R:R[P]+=1
			else:R[P]=1
			break
	random.shuffle(hint_list);c=1;Af=_A;BD=0
	while not Af:
		Ag=_A
		for F in hint_list:
			if F.important and F.priority==c and not F.used and not F.joke:
				Ag=_B;U=updateRandomHint(F.hint,F.kongs.copy(),F.keywords.copy(),F.permitted_levels.copy())
				if U:
					F.use_hint();BD+=1;P=F.subtype
					if P in R:R[P]+=1
					else:R[P]=1
				else:F.downgrade()
		if not Ag:Af=_B
		c+=1
	Q=[];x=0
	for F in hint_list:
		if not F.important and not F.used and not F.joke:Q.append(F)
	for F in hints:
		if F.hint=='':x+=1
	random.shuffle(Q);BE=0;BF=0
	if x>0:
		AD=0;Ah=100;T=0
		while AD<x:
			U=_A
			if not Q[T].used:U=updateRandomHint(Q[T].hint,Q[T].kongs,Q[T].keywords.copy(),Q[T].permitted_levels.copy())
			if U:
				Q[T].use_hint();BE+=1;P=Q[T].subtype
				if P in R:R[P]+=1
				else:R[P]=1
				AD+=1
			else:Ah-=1
			T+=1
			if T>=len(Q):T=0
			if Ah==0:
				Ai=[]
				for F in hint_list:
					if not F.joke:Ai.append(F.hint)
				for F in hints:
					if F.hint=='':F.hint=random.choice(Ai)
				for F in hints:
					if F.hint=='':
						F.hint='I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord.';P='error'
						if P in R:R[P]+=1
						else:R[P]=1
						BF+=1
				AD=x
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