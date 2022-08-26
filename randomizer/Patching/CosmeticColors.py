'Apply cosmetic skins to kongs.'
import random
from random import randint
import js
from randomizer.Patching.generate_kong_color_images import convertColors
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';r='checkered';q='patch';p='overalls';o='override_cosmetics';l='02x';k='enguarde_custom_color';j='enguarde_colors';i='rambi_custom_color';h='rambi_colors';g='chunky_custom_color';f='chunky_colors';e='tiny_custom_color';d='tiny_colors';c='lanky_custom_color';b='lanky_colors';a='diddy_custom_color';Z='diddy_colors';Y='dk_custom_color';X='dk_colors';W='base';U='colors';T='#000000';Q='zones';N='block';L='custom_setting';K='palettes';I='kong_index';H='base_setting';F='name';E='kong';D='image';C='fill_type';B='randomized';A=spoiler;M=0
	if js.document.getElementById(o).checked:O=js.document.getElementById('klaptrap_model').value
	else:O=A.settings.klaptrap_model
	if O=='green':M=33
	elif O=='purple':M=34
	elif O=='red':M=35
	elif O=='random_klap':M=random.randint(33,35)
	elif O=='random_model':s=[25,30,32,33,34,35,36,38,39,48,52,66,71,75,81,98,105,112,114,150,176,177,189];M=random.choice(s)
	A.settings.klaptrap_model_index=M;ROM().seek(A.settings.rom_data+310);ROM().writeMultipleBytes(M,1);V=[];m={};R={};t=[{E:'dk',K:[{F:W,D:3724,C:N}],H:X,L:Y,I:0},{E:'diddy',K:[{F:'cap_shirt',D:3686,C:N}],H:Z,L:a,I:1},{E:'lanky',K:[{F:p,D:3689,C:N},{F:q,D:3734,C:q}],H:b,L:c,I:2},{E:'tiny',K:[{F:p,D:6014,C:N}],H:d,L:e,I:3},{E:'chunky',K:[{F:'shirt_back',D:3769,C:r},{F:'shirt_front',D:3687,C:N}],H:f,L:g,I:4},{E:'rambi',K:[{F:W,D:3826,C:N}],H:h,L:i,I:5},{E:'enguarde',K:[{F:W,D:3847,C:N}],H:j,L:k,I:6}]
	if js.document.getElementById(o).checked:
		if js.document.getElementById('random_colors').checked:A.settings.dk_colors=B;A.settings.diddy_colors=B;A.settings.lanky_colors=B;A.settings.tiny_colors=B;A.settings.chunky_colors=B;A.settings.rambi_colors=B;A.settings.enguarde_colors=B
		else:A.settings.dk_colors=js.document.getElementById(X).value;A.settings.dk_custom_color=js.document.getElementById(Y).value;A.settings.diddy_colors=js.document.getElementById(Z).value;A.settings.diddy_custom_color=js.document.getElementById(a).value;A.settings.lanky_colors=js.document.getElementById(b).value;A.settings.lanky_custom_color=js.document.getElementById(c).value;A.settings.tiny_colors=js.document.getElementById(d).value;A.settings.tiny_custom_color=js.document.getElementById(e).value;A.settings.chunky_colors=js.document.getElementById(f).value;A.settings.chunky_custom_color=js.document.getElementById(g).value;A.settings.rambi_colors=js.document.getElementById(h).value;A.settings.rambi_custom_color=js.document.getElementById(i).value;A.settings.enguarde_colors=js.document.getElementById(j).value;A.settings.enguarde_custom_color=js.document.getElementById(k).value
	elif A.settings.random_colors:A.settings.dk_colors=B;A.settings.diddy_colors=B;A.settings.lanky_colors=B;A.settings.tiny_colors=B;A.settings.chunky_colors=B;A.settings.rambi_colors=B;A.settings.enguarde_colors=B
	R={X:A.settings.dk_colors,Y:A.settings.dk_custom_color,Z:A.settings.diddy_colors,a:A.settings.diddy_custom_color,b:A.settings.lanky_colors,c:A.settings.lanky_custom_color,d:A.settings.tiny_colors,e:A.settings.tiny_custom_color,f:A.settings.chunky_colors,g:A.settings.chunky_custom_color,h:A.settings.rambi_colors,i:A.settings.rambi_custom_color,j:A.settings.enguarde_colors,k:A.settings.enguarde_custom_color}
	for J in t:
		P={E:J[E],Q:[]}
		for S in J[K]:
			n=[T]
			if S[C]==r:n=[T,T]
			P[Q].append({'zone':S[F],D:S[D],C:S[C],U:n})
		if R[J[H]]!='vanilla':
			if R[J[H]]==B:G=f"#{format(randint(0,16777215),'06x')}"
			else:
				G=R[J[L]]
				if not G:G=T
			P[Q][0][U][0]=G
			if J[I]in(2,4):
				P[Q][1][U][0]=G
				if J[I]==4:u=int(f"0x{G[1:3]}",16);v=int(f"0x{G[3:5]}",16);w=int(f"0x{G[5:7]}",16);x=f"#{format(255-u,l)}{format(255-v,l)}{format(255-w,l)}";P[Q][0][U][1]=x
			V.append(P);m[f"{J[E]}"]=G
	A.settings.colors=m
	if len(V)>0:convertColors(V)