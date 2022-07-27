'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.generate_kong_color_images import convertColors
from random import randint
import random,js
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';h='checkered';g='overalls';f='enguarde_colors';e='rambi_colors';d='chunky_colors';c='tiny_colors';b='lanky_colors';a='diddy_colors';Z='dk_colors';W='02x';V='base';T=spoiler;S='colors';R='#000000';P='zones';L='block';J='kong_index';I='custom_setting';H='palettes';G='randomized';F='name';E='base_setting';C='image';B='kong';A='fill_type'
	if T.settings.klaptrap_model:
		M=0;N=T.settings.klaptrap_model
		if N=='green':M=33
		elif N=='purple':M=34
		elif N=='red':M=35
		elif N=='random_klap':M=random.randint(33,35)
		elif N=='random_model':i=[25,30,32,33,34,35,36,38,39,46,48,52,62,66,71,75,77,81,84,98,105,112,114,150,176,177,189];M=random.choice(i)
		ROM().seek(33476640+294);ROM().writeMultipleBytes(M,1)
	U=[];X={}
	if js.document.getElementById('random_colors').checked:js.document.getElementById(Z).value=G;js.document.getElementById(a).value=G;js.document.getElementById(b).value=G;js.document.getElementById(c).value=G;js.document.getElementById(d).value=G;js.document.getElementById(e).value=G;js.document.getElementById(f).value=G
	j=[{B:'dk',H:[{F:V,C:3724,A:L}],E:Z,I:'dk_custom_color',J:0},{B:'diddy',H:[{F:'cap_shirt',C:3686,A:L}],E:a,I:'diddy_custom_color',J:1},{B:'lanky',H:[{F:g,C:3689,A:L}],E:b,I:'lanky_custom_color',J:2},{B:'tiny',H:[{F:g,C:6014,A:L}],E:c,I:'tiny_custom_color',J:3},{B:'chunky',H:[{F:'shirt_back',C:3769,A:h},{F:'shirt_front',C:3687,A:L}],E:d,I:'chunky_custom_color',J:4},{B:'rambi',H:[{F:V,C:3826,A:L}],E:e,I:'rambi_custom_color',J:5},{B:'enguarde',H:[{F:V,C:3847,A:L}],E:f,I:'enguarde_custom_color',J:6}]
	for K in j:
		O={B:K[B],P:[]}
		for Q in K[H]:
			Y=[R]
			if Q[A]==h:Y=[R,R]
			O[P].append({'zone':Q[F],C:Q[C],A:Q[A],S:Y})
		if js.document.getElementById(K[E]).value!='vanilla':
			if js.document.getElementById(K[E]).value==G:D=f"#{format(randint(0,16777215),'06x')}"
			else:
				D=js.document.getElementById(K[I]).value
				if not D:D=R
			O[P][0][S][0]=D
			if K[J]==4:O[P][1][S][0]=D;k=int(f"0x{D[1:3]}",16);l=int(f"0x{D[3:5]}",16);m=int(f"0x{D[5:7]}",16);n=f"#{format(255-k,W)}{format(255-l,W)}{format(255-m,W)}";O[P][0][S][1]=n
			U.append(O);X[f"{K[B]}"]=D
	T.settings.colors=X
	if len(U)>0:convertColors(U)