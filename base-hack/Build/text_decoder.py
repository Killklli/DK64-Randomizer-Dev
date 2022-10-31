'Decode text file into arrays of text items.'
_G='crystal_coconut'
_F='dk_coloured_banana'
_E='static_rain?'
_D='green_sparkle'
_C='yellow_sparkle'
_B='purple_sparkle'
_A='small_explosion'
import zlib,os
temp_file='decodedtext.bin'
pointer_table_offset=1055824
text_table_index=12
icon_db={0:'waterfall_tall',1:'waterfall_short',2:'water',3:'lava',4:'sparkles',5:'pop_explosion',6:'lava_explosion',7:'green_leaf?',8:'brown_smoke_explosion',9:_A,10:'solar_flare?',11:'splash',12:'bubble',13:_B,14:_C,15:_D,16:_B,17:_C,18:_D,19:'large_smoke_explosion',20:'pink_implosion',21:'brown_horizontal_spinning_plank',22:'birch_horizontal_spinning_plank',23:'brown_vertical_spinning_plank',24:'star_water_ripple',25:'circle_water_ripple',26:'small_smoke_explosion',27:'static_star',28:'static_z',29:'white_flare?',30:_E,31:'medium_smoke_explosion',32:'bouncing_melon',33:'vertical_rolling_melon',34:'red_flare?',35:'sparks',36:'peanut',37:'star_flare?',38:'peanut_shell',39:_A,40:'large_smoke_implosion',41:'blue_lazer',42:'pineapple',43:'fireball',44:'orange',45:'grape',46:'grape_splatter',47:'tnt_sparkle',48:'fire_explosion',49:'small_fireball',50:'diddy_coin',51:'chunky_coin',52:'lanky_coin',53:'dk_coin',54:'tiny_coin',55:_F,56:'film',57:'bouncing_orange',58:_G,59:'gb',60:'banana_medal',61:'diddy_coloured_banana',62:'chunky_coloured_banana',63:'lanky_coloured_banana',64:_F,65:'tiny_coloured_banana',66:'exploded_krash_barrel_enemy',67:'white_explosion_thing',68:'coconut',69:'coconut_shell',70:'spinning_watermelon_slice',71:'tooth',72:'ammo_crate',73:'race_coin',74:'lanky_bp',75:'cannonball',76:_G,77:'feather',78:'guitar_gazump',79:'bongo_blast',80:'saxophone',81:'triangle',82:'trombone',83:'waving_yellow_double_eighth_note',84:'waving_yellow_single_eighth_note',85:'waving_green_single_eighth_note',86:'waving_purple_double_eighth_note',87:'waving_red_double_eighth_note',88:'waving_red_single_eighth_note',89:'waving_white_double_eighth_note',90:'diddy_bp',91:'chunky_bp',92:'dk_bp',93:'tiny_bp',94:'spinning_sparkle',95:_E,96:'translucent_water',97:'unk61',98:'black_screen',99:'white_cloud',100:'thin_lazer',101:'blue_bubble',102:'white_faded_circle',103:'white_circle',104:'grape_particle?',105:'spinning_blue_sparkle',106:'white_smoke_explosion',107:'l-r_joystick',108:'fire_wall',109:'static_rain_bubble',110:'a_button',111:'b_button',112:'z_button',113:'c_down_button',114:'c_up_button',115:'c_left_button',116:'acid',117:'acid_explosion',118:'race_hoop',119:'acid_goop?',120:'unk78',121:'broken_bridge?',122:'white_pole?',123:'bridge_chip?',124:'wooden_beam_with_rivets',125:'chunky_bunch',126:'diddy_bunch',127:'lanky_bunch',128:'dk_bunch',129:'tiny_bunch',130:'chunky_balloon',131:'diddy_balloon',132:'dk_balloon',133:'lanky_balloon',134:'tiny_balloon',135:'r_button',136:'l_button',137:'fairy',138:'boss_key',139:'crown',140:'rareware_coin',141:'nintendo_coin',142:'no_symbol',143:'headphones',144:'opaque_blue_water',145:'start_button',146:'white_question_mark',147:'candy_face',148:'cranky_face',149:'snide_face',150:'funky_face',151:'left_arrow',152:'white_spark?',153:'black_boulder_chunk',154:'green_boulder_chunk',155:'wood_chip',156:'snowflake/dandelion',157:'static_water?',158:'spinning_leaf',159:'flashing_water?',160:'rainbow_coin',161:'shockwave_orange_particle',162:'implosion?',163:'rareware_employee_face',164:'smoke',165:'static_smoke?',166:'barrel_bottom_chunk',167:'scoff_face',168:'multicoloured_bunch',169:'dk_face',170:'diddy_face',171:'lanky_face',172:'tiny_face',173:'chunky_face',174:'fairy_tick',175:'wrinkly'}
def grabText(file_index):
	'Pull text from ROM with a particular file index.';i='section3count';h='section2count';g='normal';f='start';S='size';N='sprite';M='type';J='text';C='big'
	with open('rom/dk64.z64','rb')as A:
		A.seek(pointer_table_offset+text_table_index*4);j=pointer_table_offset+(int.from_bytes(A.read(4),C)&2147483647);A.seek(j+file_index*4);K=pointer_table_offset+(int.from_bytes(A.read(4),C)&2147483647);k=pointer_table_offset+(int.from_bytes(A.read(4),C)&2147483647);T=k;A.seek(K);l=int.from_bytes(A.read(2),C);A.seek(K)
		with open(temp_file,'wb')as U:
			if l==8075:U.write(zlib.decompress(A.read(T),15+32))
			else:U.write(A.read(T))
	with open(temp_file,'rb')as A:
		A.seek(0);V=int.from_bytes(A.read(1),C);W=[];X=[];K=V*15+3;B=1
		for v in range(V):
			A.seek(B);Y=int.from_bytes(A.read(1),C);m=int.from_bytes(A.read(1),C);n=int.from_bytes(A.read(1),C);A.seek(B+5);O=int.from_bytes(A.read(2),C);w=int.from_bytes(A.read(2),C);D=1;Z=[]
			for x in range(Y):
				A.seek(B+D);L=int.from_bytes(A.read(1),C);E=0
				if L&4!=0:E+=4
				P=[]
				if L&1==0:
					if L&2!=0:
						A.seek(B+D+E+1);F=int.from_bytes(A.read(1),C)
						for Q in range(F):H=D+2+E+4*Q-1;A.seek(B+H);o=int.from_bytes(A.read(2),C);A.seek(B+H);a=int.from_bytes(A.read(4),C);P.append({M:N,'position':o,'data':hex(a),N:icon_db[a>>8&255]})
						I=D+2+E+4*F+4
				else:
					A.seek(B+D+E+1);F=int.from_bytes(A.read(1),C)
					for Q in range(F):H=D+2+E+8*Q-1;A.seek(B+H+3);p=int.from_bytes(A.read(2),C);A.seek(B+H+5);q=int.from_bytes(A.read(2),C);P.append({M:g,f:p,S:q})
					I=D+2+E+8*F+4
				Z.append({'block_start':hex(D+B),h:L,i:F,'offset':E,J:P});D=I
			A.seek(B)
			if I<B:b=b''
			else:b=A.read(I-B)
			X.append({'arr':b,J:Z,'section1count':Y,h:m,i:n,'data_start':hex(B)});K+=I-B;B+=D
		for r in X:
			c=[]
			for s in r[J]:
				R=[]
				for G in s[J]:
					if G[M]==g:O=G[f]+B+2;y=O+G[S];A.seek(O);R.append(A.read(G[S]).decode())
					elif G[M]==N:R.append(G[N])
				c.append(R)
			W.append(c)
	if os.path.exists(temp_file):os.remove(temp_file)
	d=[]
	for t in W:
		e=[]
		for u in t:e.append({J:u})
		d.append(e)
	return d