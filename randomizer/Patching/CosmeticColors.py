'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.generate_kong_color_images import convertColors
from random import randint
import js
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';d='checkered';c='overalls';b='enguarde_colors';a='rambi_colors';Z='chunky_colors';Y='tiny_colors';X='lanky_colors';W='diddy_colors';V='dk_colors';T='02x';S='base';Q='colors';P='#000000';N='zones';K='radial';J='kong_index';I='custom_setting';H='palettes';G='randomized';E='name';D='base_setting';C='kong';B='image';A='fill_type';R=[]
	if js.document.getElementById('random_colors').checked:js.document.getElementById(V).value=G;js.document.getElementById(W).value=G;js.document.getElementById(X).value=G;js.document.getElementById(Y).value=G;js.document.getElementById(Z).value=G;js.document.getElementById(a).value=G;js.document.getElementById(b).value=G
	e=[{C:'dk',H:[{E:S,B:3724,A:K}],D:V,I:'dk_custom_color',J:0},{C:'diddy',H:[{E:'cap_shirt',B:3686,A:K}],D:W,I:'diddy_custom_color',J:1},{C:'lanky',H:[{E:c,B:3689,A:K}],D:X,I:'lanky_custom_color',J:2},{C:'tiny',H:[{E:c,B:6014,A:K}],D:Y,I:'tiny_custom_color',J:3},{C:'chunky',H:[{E:'shirt_back',B:3769,A:d},{E:'shirt_front',B:3687,A:K}],D:Z,I:'chunky_custom_color',J:4},{C:'rambi',H:[{E:S,B:3826,A:K}],D:a,I:'rambi_custom_color',J:5},{C:'enguarde',H:[{E:S,B:3847,A:K}],D:b,I:'enguarde_custom_color',J:6}]
	for L in e:
		M={C:L[C],N:[]}
		for O in L[H]:
			U=[P]
			if O[A]==d:U=[P,P]
			M[N].append({'zone':O[E],B:O[B],A:O[A],Q:U})
		if js.document.getElementById(L[D]).value!='vanilla':
			if js.document.getElementById(L[D]).value==G:F=f"#{format(randint(0,16777215),'06x')}"
			else:
				F=js.document.getElementById(L[I]).value
				if not F:F=P
			M[N][0][Q][0]=F
			if L[J]==4:M[N][1][Q][0]=F;f=int(f"0x{F[1:3]}",16);g=int(f"0x{F[3:5]}",16);h=int(f"0x{F[5:7]}",16);i=f"#{format(255-f,T)}{format(255-g,T)}{format(255-h,T)}";M[N][0][Q][1]=i
			R.append(M)
	if len(R)>0:convertColors(R)