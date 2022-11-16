'Patch some common text.'
_AS='c_down_button'
_AR='Not enough coins - Fairy Moves'
_AQ='Not enough coins - Training Barrels'
_AP='Not enough coins - Instrument'
_AO='Not enough coins - Ammo Belt'
_AN='Not enough coins - Gun'
_AM='Not enough coins - Slam'
_AL='Not enough coins - Special Move'
_AK='Rareware Coin'
_AJ='Nintendo Coin'
_AI='Banana Medal'
_AH='Battle Crown'
_AG='Golden Banana'
_AF='Shockwave Camera Combo'
_AE='Shockwave Solo'
_AD='Camera Solo'
_AC='Vine Barrel'
_AB='Barrel Barrel'
_AA='Orange Barrel'
_A9='Dive Barrel'
_A8='Instrument Upgrade'
_A7='Ammo Belt Upgrade'
_A6='Sniper Scope'
_A5='Homing Ammo'
_A4='Coconut Gun'
_A3='Simian Slam Upgrade'
_A2='Ponytail Twirl'
_A1='Rocketbarrel'
_A0='Triangle Trample'
_z='Saxophone Slam'
_y='Trombone Tremor'
_x='Guitar Gazump'
_w='Bongo Blast'
_v='Pineapple Launcher'
_u='Feather Bow'
_t='Grape Shooter'
_s='Peanut Popguns'
_r='Gorilla Gone'
_q='Primate Punch'
_p='Hunky Chunky'
_o='Monkeyport'
_n='Mini Monkey'
_m='Orangstand Sprint'
_l='Baboon Balloon'
_k='Orangstand'
_j='Simian Spring'
_i='Chimpy Charge'
_h='Gorilla Grab'
_g='Strong Kong'
_f='Baboon Blast'
_e='b_button'
_d='z_button'
_c=False
_b='ins_upg'
_a='ammo_belt'
_Z='gun_upg'
_Y='Chunky'
_X='Tiny'
_W='Lanky'
_V='Diddy'
_U='Donkey'
_T='slam'
_S='tbarrel_bfi'
_R='instrument'
_Q='gun'
_P='explanation'
_O='has_latin'
_N='arr_name'
_M='special'
_L='item'
_K='latin'
_J='indexes'
_I='~'
_H='text'
_G='kong'
_F='candy'
_E='funky'
_D='cranky'
_C='move_type'
_B='name'
_A='move'
from text_encoder import writeText
from text_decoder import grabText
import shutil
from text_encoder import writeText
move_hints=[{_A:_f,_G:_U,_D:'THIS POTION WILL MAKE YOU SOAR JUST LIKE I USED TO BEFORE YOU WERE BORN.',_E:"YOU WON'T BELIEVE HOW HIGH THIS IS GONNA SEND YA! GET READY FOR BLASTOFF!",_F:"WITH THIS THING, YOU'LL BE ON CLOUD NINE!"},{_A:_g,_G:_U,_D:"WITH THIS, YOU'LL HAVE NO EXCUSE TO FAIL, NOTHING WILL HURT YOU!",_E:"DRINK THIS AND SHOW THESE BADDIES WHO'S THE BOSS, HUH?",_F:'IF YOU CAN FIND THE BARREL WITH YOUR HANDSOME FACE ON IT, NOTHING WILL HURT YOU.'},{_A:_h,_G:_U,_D:"MAYBE YOU'LL FINALLY MATCH MY STRENGTH OF THE OLD DAYS ONCE YOU DRINK IT.",_E:"WITH THAT MUCH STRENGTH, YOU'LL BE GRABBIN' LEVERS LEFT AND RIGHT, MAN!",_F:'AFTER YOU DRINK THAT POTION, COULD YOU OPEN THIS JAR FOR ME, LOVE?'},{_A:_i,_G:_V,_D:"NOW DON'T GO SMASHING YOUR HEAD TOO MUCH OR YOU'LL END UP LIKE DONKEY!",_E:'THIS POTION WILL MAKE YOU ROCK! YOUR HEAD WILL BE AS HARD AS ONE!',_F:'WITH THIS, YOU WILL HAVE A STRONG HEAD! NOW, PLEASE TAKE CARE OF YOUR PRETTY LITTLE FACE...'},{_A:_A1,_G:_V,_D:'FIND MY BARREL WITH YOUR FACE ON IT TO TRY OUT MY PROTOTYPE JETBARREL.',_E:"YOU'LL LOVE THIS ONE! SWING BY THE SPECIAL BARREL AND BLAST OFF WITH ROCKETS ON YOUR BACK!",_F:"BE CAREFUL WITH THIS ONE, YOU'LL BE FLYING HIGH!"},{_A:_j,_G:_V,_D:"EVEN I COULD JUMP HIGHER THAN YOU, SO I'M SURE YOU'LL BE NEEDING THIS ONE.",_E:"IT'S GONNA TURN YOUR TAIL INTO A TRAMPOLINE!",_F:"LET'S ADD A BIT OF SPRING TO YOUR STEP, SHALL WE?"},{_A:_k,_G:_W,_D:'THIS HANDY LITTLE MOVE SHOULD HELP YOU GET UP STEEP SLOPES.',_E:"THIS'LL BE THE PERFECT UPPER BODY WORKOUT!",_F:'THIS DRINK WILL LET YOU MAKE USE OF THESE BIG LONG ARMS OF YOURS.'},{_A:_l,_G:_W,_D:'THE BUBBLES IN THIS POTION ARE HELIUM.',_E:'THIS MAGIC POTION WILL BLOW YOU AWAY!',_F:'THIS WILL GET YOU FEELING FLOATY!'},{_A:_m,_G:_W,_D:"I CAN RUN FASTER THAN YOU, EVEN WITH K.ROOL ON MY BACK! THAT'S WHY THIS POTION IS A MUST.",_E:"WITH THIS POTION, YOU'LL BE MOVING LIKE GREASED LIGHTNING!",_F:'THIS BARREL WILL GIVE YOU A BIG BURST OF SPEED.'},{_A:_n,_G:_X,_D:'LEAP INTO MY SPECIAL BARREL AND PREPARE TO BE AMAZED AS YOU SHRINK IN SIZE!',_E:"IT'S A MAGIC BARREL THAT'LL MAKE YOU THE SIZE OF A PEA.",_F:'THIS MAGIC POTION WILL MAKE YOU ITSY BITSY, ~.'},{_A:_A2,_G:_X,_D:'TIME TO DO SOMETHING WITH THAT SILLY HAIR OF YOURS.',_E:'TAKE A BIG LEAP AND FLY LIKE A \x01HAIRYCOPTER!\x01',_F:'NO GAP WILL BE TOO FAR FOR YOU TO CROSS!'},{_A:_o,_G:_X,_D:"IN MY DAY, YOU'D HAVE TO WALK UPHILL BOTH WAYS, BUT THIS WILL WARP YOU IN AN INSTANT.",_E:'THIS COOL MOVE WILL SEND YOU PLACES!',_F:"IT'S YOUR VERY OWN PERSONAL WARP PAD!"},{_A:_p,_G:_Y,_D:"ALTHOUGH I'M NOT SURE WHY YOU'D NEED IT, YOU'RE ALREADY BIG ENOUGH AS IT IS.",_E:"DRINK THIS AND YOU'LL BULK UP BIG TIME!",_F:'ONE SIP OF THIS MAGICAL DRINK CAN MAKE A BIG STRONG FELLA LIKE YOU EVEN BIGGER.'},{_A:_q,_G:_Y,_D:"YOU CAN'T SOLVE ALL YOUR PROBLEMS WITH YOUR FISTS, BUT WITH THIS, AT LEAST YOU COULD TRY.",_E:"POW! KNOCK 'EM OUT COLD WITH THIS ONE, DUDE!",_F:'THIS WILL LET YOU SMASH OBSTACLES AND BIG BAD GUYS ALIKE.'},{_A:_r,_G:_Y,_D:"WE FINALLY WON'T HAVE TO LOOK AT YOUR UGLY FEATURES! DO US A FAVOR AND USE IT AS OFTEN AS POSSIBLE, HUH?",_E:"USE THIS ONE TO GO UNDERCOVER. THEY WON'T SEE YOU COMIN'!",_F:'THIS IS PERFECT FOR A BIG SHY GUY LIKE YOU.'},{_A:_A3,_G:_I,_D:"WITH IT YOU'LL BE ABLE TO PRESS DOWN TOUGHER SWITCHES.",_E:"YOU'LL BE SMASHING SWITCHES EVEN HARDER THAN BEFORE!",_F:'IT WILL MAKE THAT USEFUL GROUND SLAM OF YOURS EVEN MORE POWERFUL.'},{_A:_A4,_G:_U,_D:"NOW, TAKE IT AND DON'T POINT IT AT ME! I DON'T WANT A COCONUT IN THE FACE!",_E:"THIS IS A REAL COOL COCONUT SHOOTER THAT'LL TRASH K.ROOL'S ARMY.",_F:'USE IT TO FIRE YOUR BIG COCONUTS AT YOUR ENEMIES.'},{_A:_s,_G:_V,_D:"NOW, TAKE IT AND DON'T POINT IT AT ME! I HATE PEANUTS!",_E:"THOSE ARE SOME REAL COOL LITTLE POPGUNS THAT'LL SUIT YOUR JETPACK PERFECTLY.",_F:'USE THEM TO FIRE LITTLE PEANUTS TO HURT YOUR ENEMIES AND FEED YOUR FRIENDS.'},{_A:_t,_G:_W,_D:"NOW, TAKE IT AND DON'T POINT IT AT ME! YOU'LL POKE AN EYE OUT WITH THIS THING!",_E:"THIS IS A REAL COOL BLOWGUN THAT'LL WRECK K.ROOL'S ARMY.",_F:'USE IT TO PAINT YOUR ENEMIES PURPLE.'},{_A:_u,_G:_X,_D:"NOW, TAKE IT AND DON'T POINT IT AT ME! THOSE FEATHERS ARE POINTY!",_E:"THIS IS A REAL COOL CROSSBOW THAT'LL POKE HOLES IN K.ROOL'S TOES.",_F:'USE IT TO FIRE FEATHERS TO STING YOUR ENEMIES.'},{_A:_v,_G:_Y,_D:"NOW, TAKE IT AND DON'T POINT IT AT ME! YOU'D RIP MY FEEBLE HEAD OFF WITH THESE PINEAPPLES!",_E:"THIS IS A REAL COOL LAUNCHER THAT'LL BLOW HOLES IN K.ROOL'S ARMY.",_F:'USE IT TO FIRE MASSIVE PINEAPPLES TO CLEAR EVERYTHING ON YOUR PATH.'},{_A:_A5,_G:_I,_D:"I'VE SEEN HOW POORLY YOU AIM THESE WEAPONS. YOU NEED AMMO THAT DOES THE AIMING FOR YOU.",_E:'I CAN UPGRADE YOUR SHOOTER WITH HEAT-SEEKING AMMO.',_F:"IT'S GOT FANCY TECHNOLOGY TO MAKE YOUR SHOTS ALWAYS HIT THEIR TARGET."},{_A:_A6,_G:_I,_D:'YOUR EYESIGHT IS SOMEHOW WORSE THAN MINE. YOU NEED THIS TO SEE PAST YOUR NOSE.',_E:'I CAN UPGRADE YOUR SHOOTER WITH A LONG-RANGE SCOPE.',_F:'THIS WILL LET YOU ZOOM IN ON FAR AWAY TARGETS.'},{_A:_A7,_G:_I,_D:"ALWAYS RUNNING OUT OF AMMO? WELL, MAYBE WITH THIS, YOU'LL FINALLY HAVE ENOUGH!",_E:"TAKE A LOOK AT THIS BELT. YOU'LL CARRY SO MUCH MORE AMMO WITH IT!",_F:"YOU'LL NEVER RUN OUT AGAIN WITH THIS MUCH STORAGE!"},{_A:_w,_G:_U,_D:'I FOUND IT LYING SOMEWHERE. IT MAKES A FUNNY SOUND WHEN YOU SMACK IT.',_E:'GO ON AND PLAY A SICK BEAT, ~!',_F:"I'LL SHOW YOU MY TWO BONGOS, AND HOW TO PLAY THEM, TOO."},{_A:_x,_G:_V,_D:"IT MAKES AN AWFUL RACKET. DON'T PLAY IT IN HERE!",_E:"WITH THIS, YOU'RE GONNA BE A ROCKSTAR!",_F:"I'LL SHOW YOU MY GUITAR AND HOW TO PLUCK THE STRINGS."},{_A:_y,_G:_W,_D:'I MADE THIS OUT OF A SPARE PIECE OF PIPE. IT MAKES A STUPID SOUND WHEN YOU BLOW IN IT.',_E:'A FUNNY INSTRUMENT FOR A FUNNY DUDE!',_F:"I'LL SHOW YOU MY TROMBONE AND ALL THE SLIDE POSITIONS."},{_A:_z,_G:_X,_D:'THE WHIPPERSNAPPERS CALL THIS THING A MUSICAL INSTRUMENT. THIS IS NOT MUSIC!',_E:"YOU'LL JAZZ THINGS UP WITH THIS!",_F:"I'LL SHOW YOU MY SAXOPHONE AND HOW TO PLAY IT, TOO."},{_A:_A0,_G:_Y,_D:"IT'S JUST SOME JUNK METAL. YOU COULD TRY SMACKING IT, I GUESS.",_E:"DING DING, LOSERS! SMACK THIS AND K.ROOL'S EARS WILL BE RINGING FOR DAYS.",_F:"I'LL SHOW YOU MY SPECIAL TRIANGLE AND HOW TO HIT IT JUST RIGHT."},{_A:_A8,_G:_I,_D:"YOU'LL BE ABLE TO MAKE EVEN MORE RACKET THAN BEFORE.",_E:'MORE MUSICAL ENERGY SO YOU CAN JAM OUT FOR LONGER!',_F:'I HAVE AN INSTRUMENT UPGRADE AVAILABLE FOR YOU.'},{_A:_A9,_G:_I,_D:"YOU'LL BE SUBMERGING YOURSELF LIKE THEM SUBMARINES IN GALLEON.",_E:"YOU'LL BE GLIDING UNDERWATER GROOVIER THAN BEFORE.",_F:"I'LL SHOW YOU HOW TO LAST LONGER UNDERWATER."},{_A:_AA,_G:_I,_D:"SET THE TIMER TO 5 AND THROW THIS FRUIT LIKE IT'S A WORMS GAME.",_E:'YOU BETTER CALL THE BOMB SQUAD, CAUSE THESE FRUIT ARE LIKE DYNAMITE.',_F:'I MAY HAVE MELONS, BUT I HAVE MORE EXPLOSIVE FRUIT LIKE THESE BAD BOYS.'},{_A:_AB,_G:_I,_D:"YOU WON'T EVEN BE BREAKING A SWEAT LIFTING UP BARRELS.",_E:"YOU'LL BE ABLE TO JAM OUT WITH DOGADON BY THROWING BARRELS IN HIS FACE.",_F:"I'M SURE YOU'LL BE ABLE TO PICK UP THOSE LARGE BARRELS FOR ME."},{_A:_AC,_G:_I,_D:"I DON'T REMEMBER THIS GAME BEING CALLED JUNGLE SWING, BUT THIS WILL CERTAINLY LET YOU SWING.",_E:"IS THIS THE 1920S? CAUSE THIS WILL LET YOU SWING LIKE IT'S THOSE DAYS.",_F:'THIS MOVE WILL ALLOW YOU TO GRAB ROPES.'},{_A:_AD,_G:_I,_D:'WITH THAT DEVICE, YOU MIGHT AS WELL CALL ME PROFESSOR OAK! WONDERFUL.',_E:'THIS DEVICE WILL ALLOW YOU TO TAKE THEM HIGH RESOLUTION POLAROIDS.',_F:"DON'T FLASH THAT THING TOO BRIGHT IN MY FACE."},{_A:_AE,_G:_I,_D:'THIS MOVE WILL LET YOU UNEARTH THOSE DASTARDLY MOUNDS WITH SOME LETTERS ON THEM.',_E:"WITH THIS MOVE, YOU'LL BE SHOCKING THE REST OF THE COMPETITION IN THOSE CROWNS.",_F:"I DIDN'T KNOW YOU HAD SO MUCH ENERGY IN YOU TO RELEASE SUCH A POWERFUL ENERGY CHARGE."},{_A:_AF,_G:_I,_D:'TWO MOVES IN ONE. BACK IN MY DAY YOU HAD TO PAY DOUBLE THE CREDITS FOR THAT.',_E:'I GOT A BONZA DEAL FOR YOU. TWO MOVES FOR THE PRICE OF.. TWO. WHAT DO YOU SAY?',_F:"TWO MOVES? WELL I GUESS SINCE YOU'VE BEEN WORKING HARD, WHAT DO YOU SAY?"},{_A:_AG,_G:_I,_D:'GB CRANKY',_E:'GB FUNKY',_F:'GB CANDY'},{_A:_AH,_G:_I,_D:'CROWN CRANKY',_E:'CROWN FUNKY',_F:'CROWN CANDY'},{_A:_AI,_G:_I,_D:'MEDAL CRANKY',_E:'MEDAL FUNKY',_F:'MEDAL CANDY'},{_A:'Boss Key',_G:_I,_D:'KEY CRANKY',_E:'KEY FUNKY',_F:'KEY CANDY'},{_A:'Blueprint',_G:_I,_D:'BP CRANKY',_E:'BP FUNKY',_F:'BP CANDY'},{_A:_AJ,_G:_I,_D:'NINTENDO COIN CRANKY',_E:'NINTENDO COIN FUNKY',_F:'NINTENDO COIN CANDY'},{_A:_AK,_G:_I,_D:'RAREWARE COIN CRANKY',_E:'RAREWARE COIN FUNKY',_F:'RAREWARE COIN CANDY'},{_A:'Bean',_G:_I,_D:'BEAN CRANKY',_E:'BEAN FUNKY',_F:'BEAN CANDY'},{_A:_AL,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD MY SPECIAL MOVE.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. SPECIAL MOVES DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET MY SPECIAL MOVE."},{_A:_AM,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD TO UPGRADE YOUR GROUND SLAM.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. YOU'LL HAVE TO KEEP YOUR WEAK SLAM FOR NOW!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO IMPROVE YOUR SLAM."},{_A:_AN,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS WEAPON.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. MY COOL WEAPONS DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS WEAPON."},{_A:_AO,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD TO UPGRADE YOUR AMMO COUNT.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. AMMO BELTS DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET MORE AMMO."},{_A:_AP,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD TO UPGRADE YOUR INSTRUMENT.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. MUSICAL ENERGY DOESN'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO UPGRADE YOUR INSTRUMENT."},{_A:_AQ,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS BASIC MOVE.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. BASIC MOVES DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS BASIC MOVE."},{_A:_AR,_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS FAIRY MOVE.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. FAIRY MOVES DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS FAIRY MOVE."},{_A:'Not enough coins - Item',_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS MAJOR ITEM.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. MAJOR ITEMS DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS MAJOR ITEM."},{_A:'Not enough coins - GB',_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS GOLDEN BANANA.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. GOLDEN BANANAS DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS GOLDEN BANANA."},{_A:'Not enough coins - BP',_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS BLUEPRINT.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. BLUEPRINTS DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS BLUEPRINT."},{_A:'Not enough coins - Medal',_G:_I,_D:"YOU'RE UNLUCKY TO BE SO POOR YOU CAN'T AFFORD THIS BANANA MEDAL.",_E:"'FRAID I CAN'T JUST GIVE IT TO YA, THOUGH. BANANA MEDALS DON'T GROW ON TREES!",_F:"BUT YOU'LL NEED TO SCRAPE TOGETHER SOME MORE COINS TO GET THIS BANANA MEDAL."}]
pre_amble={_D:"YOU'RE BACK AGAIN, ~? YOU'RE LUCKY I HAVE SOMETHING FOR YOU. ",_E:"WHAT'S UP, ~-DUDE! I JUST FINISHED MAKIN' THIS! ",_F:'WHY, ~, HAVE I GOT A TREAT FOR YOU. '}
moves=[_f,_g,_h,_i,_A1,_j,_k,_l,_m,_n,_A2,_o,_p,_q,_r,_A3,_A4,_s,_t,_u,_v,_A5,_A6,_A7,_w,_x,_y,_z,_A0,_A8,_A9,_AA,_AB,_AC,_AD,_AE,_AF,_AL,_AM,_AN,_AO,_AP,_AQ,_AR]
shop_owners=[_D,_E,_F]
hint_text=[]
for move in move_hints:
	for shop in shop_owners:hint_pre=pre_amble[shop];hint_post=move[shop];hint_text.append([{_H:[f"{hint_pre}{hint_post}"]}])
writeText('dolby_text.bin',[[{_H:['DONKEY KONG 64 RANDOMIZER']}],[{_H:['DEVELOPERS - 2DOS, BALLAAM, BISMUTH, CFOX, KILLKLLI, LRAUQ, SHADOWSHINE, ZNERNICUS']}],[{_H:['DK64RANDOMIZER.COM']}]])
writeText('custom_text.bin',hint_text)
writeText('dk_text.bin',[[{_H:['WHAT DID CRANKY MEAN ABOUT TRAINING? DONKEY ALL CONFUSED...']}],[{_H:['AW NO! SO THAT WHAT CRANKY MEAN ABOUT REPTILE...','DONKEY NOT BELIEVE IT. KING K.ROOL? WE FINISHED K. ROOL OFF IN LAST GAME!']}],[{_H:['OKAY!','DONKEY IS FREE NOW. THANK YOU, MY FRIEND.','DONKEY CAN COLLECT YELLOW BANANAS.']},{_H:['dk_coloured_banana']},{_H:['DONKEY WILL BE INSIDE THE TAG BARREL UNTIL YOU NEED MY HELP.']}]])
move_names=[{_B:'Simian Slam',_K:'Buttus Bashium',_C:_T},{_B:'Super Simian Slam',_K:'Big Buttus Bashium',_C:_T},{_B:'Super Duper Simian Slam',_K:'Bigga Buttus Bashium',_C:_T},{_B:_f,_K:'Barrelum Perilous',_C:_M},{_B:_g,_K:'Strongum Kongus',_C:_M},{_B:_h,_K:'Simium Strainus',_C:_M},{_B:_i,_K:'Hurtus Cranium',_C:_M},{_B:'Rocketbarrel Boost',_K:'Boostum Highus',_C:_M},{_B:_j,_K:'Leapus Largium',_C:_M},{_B:_k,_K:'Palmus Walkum',_C:_M},{_B:_l,_K:'Baboonus Balloonus',_C:_M},{_B:_m,_K:'Palmus Dashium',_C:_M},{_B:_n,_K:'Kongum Smallus',_C:_M},{_B:'Pony Tail Twirl',_K:'Roundum Roundus',_C:_M},{_B:_o,_K:'Warpum Craftious',_C:_M},{_B:_p,_K:'Kremlinous Crushum',_C:_M},{_B:_q,_K:'Sandwichium Knucklus',_C:_M},{_B:_r,_K:'Wheresim Gonium',_C:_M},{_B:'Coconut Shooter',_C:_Q},{_B:_s,_C:_Q},{_B:_t,_C:_Q},{_B:_u,_C:_Q},{_B:_v,_C:_Q},{_B:_w,_C:_R},{_B:_x,_C:_R},{_B:_y,_C:_R},{_B:_z,_C:_R},{_B:_A0,_C:_R},{_B:'All Kongs - Homing Ammo',_C:_Z},{_B:'All Kongs - Sniper',_C:_Z},{_B:'All Kongs - Ammo Belt 1',_C:_a},{_B:'All Kongs - Ammo Belt 2',_C:_a},{_B:'3rd Melon',_C:_b},{_B:'All Kongs - Upgrade 1',_C:_b},{_B:'All Kongs - Upgrade 2',_C:_b},{_B:'Diving',_C:_S},{_B:'Orange Throwing',_C:_S},{_B:'Barrel Throwing',_C:_S},{_B:'Vine Swinging',_C:_S},{_B:'Fairy Camera',_C:_S},{_B:'Shockwave',_C:_S},{_B:'Fairy Camera and Shockwave',_C:_S},{_B:_AG,_C:_L},{_B:_AI,_C:_L},{_B:'Donkey Blueprint',_C:_L},{_B:'Diddy Blueprint',_C:_L},{_B:'Lanky Blueprint',_C:_L},{_B:'Tiny Blueprint',_C:_L},{_B:'Chunky Blueprint',_C:_L},{_B:_AJ,_C:_L},{_B:_AK,_C:_L},{_B:'Boss Key',_C:_L},{_B:_AH,_C:_L},{_B:'Bean',_C:_L},{_B:'Key 1',_C:_L},{_B:'Key 2',_C:_L},{_B:'Key 3',_C:_L},{_B:'Key 4',_C:_L},{_B:'Key 5',_C:_L},{_B:'Key 6',_C:_L},{_B:'Key 7',_C:_L},{_B:'Key 8',_C:_L}]
move_names_arr=[]
for move in move_names:
	init_len=len(move_names_arr);move_names_arr.append([{_H:[move[_B].upper()]}])
	if _K in move:move_names_arr.append([{_H:[f"({move[_K].upper()})"]}])
	if'print'in move and move['print']:print(f"{move[_B]}: {init_len}")
index_data={_T:{_J:[],_N:'SimianSlamNames',_O:True},_M:{_J:[],_N:'SpecialMovesNames',_O:True},_Q:{_J:[],_N:'GunNames',_O:_c},_Z:{_J:[],_N:'GunUpgNames',_O:_c},_a:{_J:[],_N:'AmmoBeltNames',_O:_c},_R:{_J:[],_N:'InstrumentNames',_O:_c},_b:{_J:[],_N:'InstrumentUpgNames',_O:_c}}
for kong_index in range(5):
	for move_index in range(4):
		for latin_index in range(2):
			if move_index==0:index_data[_M][_J].append(0)
			else:index_data[_M][_J].append(6+latin_index+2*(move_index-1)+6*kong_index)
	index_data[_Q][_J].append(36+kong_index);index_data[_R][_J].append(41+kong_index)
for move_index in range(4):
	for latin_index in range(2):
		if move_index==0:index_data[_T][_J].append(0)
		else:index_data[_T][_J].append(latin_index+2*(move_index-1))
for move_index in range(4):
	if move_index<2:index_data[_Z][_J].append(0)
	else:index_data[_Z][_J].append(move_index-2+46)
for move_index in range(3):
	if move_index==0:index_data[_a][_J].append(0)
	else:index_data[_a][_J].append(move_index-1+48)
index_data[_b][_J]=[0,0,51,50,52]
with open('src/randomizers/move_text.c','w')as fh:
	with open('include/text_items.h','w')as fg:
		fh.write('#include "../../include/common.h"\n\n');fg.write('#include "common.h"\n\n');disclaimer=['/*\n','\tFile is automatically generated from build/patch_text.py\n','\tIf you wish to modify this file, please modify the code there\n','*/\n\n']
		for line in disclaimer:fh.write(line);fg.write(line)
		fg.write('typedef struct name_latin_struct {\n');fg.write('\t/* 0x000 */ unsigned char name;\n');fg.write('\t/* 0x001 */ unsigned char latin;\n');fg.write('} name_latin_struct;\n\n')
		for move_type in index_data:
			arr_item_type='unsigned char';divisor=1
			if index_data[move_type][_O]:arr_item_type='name_latin_struct';divisor=2
			fh.write(f"const {arr_item_type} {index_data[move_type][_N]}[] = {{\n");fg.write(f"extern const {arr_item_type} {index_data[move_type][_N]}[{int(len(index_data[move_type][_J])/divisor)}];\n")
			for item_index in range(int(len(index_data[move_type][_J])/divisor)):
				if index_data[move_type][_O]:fh.write('\t{\n');fh.write(f"\t\t.name = {index_data[move_type][_J][divisor*item_index]},\n");fh.write(f"\t\t.latin = {index_data[move_type][_J][divisor*item_index+1]},\n");fh.write('\t},\n')
				else:fh.write(f"\t{index_data[move_type][_J][divisor*item_index]},\n")
			fh.write('};\n\n')
writeText('move_names.bin',move_names_arr)
move_explanations=[{_A:'dive_barrel',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW DIVE UNDERWATER. PRESS']},{_H:[_d]},{_H:['TO SUBMERGE YOURSELF.']}]},{_A:'orange_barrel',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW THROW ORANGE GRENADES. PRESS']},{_H:[_d]},{_H:['THEN']},{_H:['c_left_button']},{_H:['TO FIRE AN EXPLOSIVE FRUIT.']}]},{_A:'barrel_barrel',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW PICK UP OBJECTS. PRESS']},{_H:[_e]},{_H:['TO GRAB AN OBJECT WITH RELATIVE EASE.']}]},{_A:'vine_barrel',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW SWING ON VINES. JUMP TO GRAB ONTO THE VINE AND PRESS ']},{_H:['a_button']},{_H:['TO LAUNCH YOURSELF FROM IT.']}]},{_A:'camera_solo',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW USE A CAMERA TO SNAP BANANA FAIRIES. PRESS']},{_H:[_d]},{_H:['THEN']},{_H:[_AS]},{_H:['TO PULL OUT THE CAMERA. PRESS']},{_H:[_e]},{_H:['TO TAKE A PICTURE.']}]},{_A:'shockwave_solo',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW RELEASE A SHOCKWAVE CHARGE. PRESS AND HOLD']},{_H:[_e]},{_H:['TO CHARGE THE SHOCKWAVE.']}]},{_A:'camera_shockwave_combo',_P:[{_H:['PAY ATTENTION, ~. YOU AND ALL THE OTHER KONGS CAN NOW RELEASE A SHOCKWAVE CHARGE AND USE A CAMERA TO SNAP BANANA FAIRIES. PRESS AND HOLD']},{_H:[_e]},{_H:['TO CHARGE THE SHOCKWAVE. PRESS ']},{_H:[_d]},{_H:['THEN']},{_H:[_AS]},{_H:['TO PULL OUT THE CAMERA.']}]},{_A:'generic_item',_P:[{_H:["PAY ATTENTION, ~. THERE'S PLENTY MORE ITEMS TO GATHER IN THIS GAME. GET MOVING SO WE CAN DISPENSE OF K. ROOL"]}]}]
cranky_text=grabText(8)
for move in move_explanations:cranky_text.append(move[_P])
writeText('cranky_text.bin',cranky_text)
menu_text=grabText(37)
menu_text[46]=[{_H:['FIRST PERSON CAMERA']}]
writeText('menu_text.bin',menu_text)
kongname_text=grabText(2)
kongname_text.append([{_H:['KRUSHA']}])
writeText('kongname_text.bin',kongname_text)