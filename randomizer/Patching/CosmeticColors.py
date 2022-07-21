'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.generate_kong_color_images import convertColors
from random import randint
import js
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';e='checkered';d='overalls';c='enguarde_colors';b='rambi_colors';a='chunky_colors';Z='tiny_colors';Y='lanky_colors';X='diddy_colors';W='dk_colors';T='02x';S='base';Q='colors';P='#000000';N='zones';L='block';J='kong_index';I='custom_setting';H='palettes';G='randomized';F='name';E='base_setting';C='image';B='kong';A='fill_type';R=[];U={}
	if js.document.getElementById('random_colors').checked:js.document.getElementById(W).value=G;js.document.getElementById(X).value=G;js.document.getElementById(Y).value=G;js.document.getElementById(Z).value=G;js.document.getElementById(a).value=G;js.document.getElementById(b).value=G;js.document.getElementById(c).value=G
	f=[{B:'dk',H:[{F:S,C:3724,A:L}],E:W,I:'dk_custom_color',J:0},{B:'diddy',H:[{F:'cap_shirt',C:3686,A:L}],E:X,I:'diddy_custom_color',J:1},{B:'lanky',H:[{F:d,C:3689,A:L}],E:Y,I:'lanky_custom_color',J:2},{B:'tiny',H:[{F:d,C:6014,A:L}],E:Z,I:'tiny_custom_color',J:3},{B:'chunky',H:[{F:'shirt_back',C:3769,A:e},{F:'shirt_front',C:3687,A:L}],E:a,I:'chunky_custom_color',J:4},{B:'rambi',H:[{F:S,C:3826,A:L}],E:b,I:'rambi_custom_color',J:5},{B:'enguarde',H:[{F:S,C:3847,A:L}],E:c,I:'enguarde_custom_color',J:6}]
	for K in f:
		M={B:K[B],N:[]}
		for O in K[H]:
			V=[P]
			if O[A]==e:V=[P,P]
			M[N].append({'zone':O[F],C:O[C],A:O[A],Q:V})
		if js.document.getElementById(K[E]).value!='vanilla':
			if js.document.getElementById(K[E]).value==G:D=f"#{format(randint(0,16777215),'06x')}"
			else:
				D=js.document.getElementById(K[I]).value
				if not D:D=P
			M[N][0][Q][0]=D
			if K[J]==4:M[N][1][Q][0]=D;g=int(f"0x{D[1:3]}",16);h=int(f"0x{D[3:5]}",16);i=int(f"0x{D[5:7]}",16);j=f"#{format(255-g,T)}{format(255-h,T)}{format(255-i,T)}";M[N][0][Q][1]=j
			R.append(M);U[f"{K[B]}"]=D
	spoiler.settings.colors=U
	if len(R)>0:convertColors(R)