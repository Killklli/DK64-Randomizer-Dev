'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.generate_kong_color_images import convertColors
from random import randint
import random,js
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';r='enguarde_custom_color';q='rambi_custom_color';p='chunky_custom_color';o='checkered';n='tiny_custom_color';m='lanky_custom_color';l='patch';k='overalls';j='diddy_custom_color';i='dk_custom_color';h='override_cosmetics';e='02x';d='enguarde_colors';c='rambi_colors';b='chunky_colors';a='tiny_colors';Z='lanky_colors';Y='diddy_colors';X='dk_colors';W='base';U='colors';T='#000000';Q='zones';M='block';L='custom_setting';K='palettes';I='kong_index';H='base_setting';F='name';E='kong';D='image';C='fill_type';B='randomized';A=spoiler;N=0
	if js.document.getElementById(h).checked:O=js.document.getElementById('klaptrap_model').value
	else:O=A.settings.klaptrap_model
	if O=='green':N=33
	elif O=='purple':N=34
	elif O=='red':N=35
	elif O=='random_klap':N=random.randint(33,35)
	elif O=='random_model':s=[25,30,32,33,34,35,36,38,39,48,52,66,71,75,81,98,105,112,114,150,176,177,189];N=random.choice(s)
	ROM().seek(A.settings.rom_data+310);ROM().writeMultipleBytes(N,1);V=[];f={};R={};t=[{E:'dk',K:[{F:W,D:3724,C:M}],H:X,L:i,I:0},{E:'diddy',K:[{F:'cap_shirt',D:3686,C:M}],H:Y,L:j,I:1},{E:'lanky',K:[{F:k,D:3689,C:M},{F:l,D:3734,C:l}],H:Z,L:m,I:2},{E:'tiny',K:[{F:k,D:6014,C:M}],H:a,L:n,I:3},{E:'chunky',K:[{F:'shirt_back',D:3769,C:o},{F:'shirt_front',D:3687,C:M}],H:b,L:p,I:4},{E:'rambi',K:[{F:W,D:3826,C:M}],H:c,L:q,I:5},{E:'enguarde',K:[{F:W,D:3847,C:M}],H:d,L:r,I:6}]
	if js.document.getElementById(h).checked:
		if js.document.getElementById('random_colors').checked:A.settings.dk_colors=B;A.settings.diddy_colors=B;A.settings.lanky_colors=B;A.settings.tiny_colors=B;A.settings.chunky_colors=B;A.settings.rambi_colors=B;A.settings.enguarde_colors=B
		else:A.settings.dk_colors=js.document.getElementById(X).value;A.settings.diddy_colors=js.document.getElementById(Y).value;A.settings.lanky_colors=js.document.getElementById(Z).value;A.settings.tiny_colors=js.document.getElementById(a).value;A.settings.chunky_colors=js.document.getElementById(b).value;A.settings.rambi_colors=js.document.getElementById(c).value;A.settings.enguarde_colors=js.document.getElementById(d).value
	elif A.settings.random_colors:A.settings.dk_colors=B;A.settings.diddy_colors=B;A.settings.lanky_colors=B;A.settings.tiny_colors=B;A.settings.chunky_colors=B;A.settings.rambi_colors=B;A.settings.enguarde_colors=B
	R={X:A.settings.dk_colors,i:A.settings.dk_custom_color,Y:A.settings.diddy_colors,j:A.settings.diddy_custom_color,Z:A.settings.lanky_colors,m:A.settings.lanky_custom_color,a:A.settings.tiny_colors,n:A.settings.tiny_custom_color,b:A.settings.chunky_colors,p:A.settings.chunky_custom_color,c:A.settings.rambi_colors,q:A.settings.rambi_custom_color,d:A.settings.enguarde_colors,r:A.settings.enguarde_custom_color}
	for J in t:
		P={E:J[E],Q:[]}
		for S in J[K]:
			g=[T]
			if S[C]==o:g=[T,T]
			P[Q].append({'zone':S[F],D:S[D],C:S[C],U:g})
		if R[J[H]]!='vanilla':
			if R[J[H]]==B:G=f"#{format(randint(0,16777215),'06x')}"
			else:
				G=R[J[L]]
				if not G:G=T
			P[Q][0][U][0]=G
			if J[I]in(2,4):
				P[Q][1][U][0]=G
				if J[I]==4:u=int(f"0x{G[1:3]}",16);v=int(f"0x{G[3:5]}",16);w=int(f"0x{G[5:7]}",16);x=f"#{format(255-u,e)}{format(255-v,e)}{format(255-w,e)}";P[Q][0][U][1]=x
			V.append(P);f[f"{J[E]}"]=G
	A.settings.colors=f
	if len(V)>0:convertColors(V)