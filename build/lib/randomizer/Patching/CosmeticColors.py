'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Patching.generate_kong_color_images import convertColors
from random import randint
import random,js
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';q='enguarde_custom_color';p='rambi_custom_color';o='chunky_custom_color';n='checkered';m='tiny_custom_color';l='lanky_custom_color';k='overalls';j='diddy_custom_color';i='dk_custom_color';h='override_cosmetics';e='02x';d='enguarde_colors';c='rambi_colors';b='chunky_colors';a='tiny_colors';Z='lanky_colors';Y='diddy_colors';X='dk_colors';W='base';U='colors';T='#000000';Q='zones';M='block';K='kong_index';J='custom_setting';I='palettes';H='name';G='base_setting';E='image';D='kong';C='fill_type';B='randomized';A=spoiler;N=0
	if js.document.getElementById(h).checked:O=js.document.getElementById('klaptrap_model').value
	else:O=A.settings.klaptrap_model
	if O=='green':N=33
	elif O=='purple':N=34
	elif O=='red':N=35
	elif O=='random_klap':N=random.randint(33,35)
	elif O=='random_model':r=[25,30,32,33,34,35,36,38,39,48,52,66,71,75,81,98,105,112,114,150,176,177,189];N=random.choice(r)
	ROM().seek(A.settings.rom_data+310);ROM().writeMultipleBytes(N,1);V=[];f={};R={};s=[{D:'dk',I:[{H:W,E:3724,C:M}],G:X,J:i,K:0},{D:'diddy',I:[{H:'cap_shirt',E:3686,C:M}],G:Y,J:j,K:1},{D:'lanky',I:[{H:k,E:3689,C:M}],G:Z,J:l,K:2},{D:'tiny',I:[{H:k,E:6014,C:M}],G:a,J:m,K:3},{D:'chunky',I:[{H:'shirt_back',E:3769,C:n},{H:'shirt_front',E:3687,C:M}],G:b,J:o,K:4},{D:'rambi',I:[{H:W,E:3826,C:M}],G:c,J:p,K:5},{D:'enguarde',I:[{H:W,E:3847,C:M}],G:d,J:q,K:6}]
	if js.document.getElementById(h).checked:
		if js.document.getElementById('random_colors').checked:A.settings.dk_colors=B;A.settings.diddy_colors=B;A.settings.lanky_colors=B;A.settings.tiny_colors=B;A.settings.chunky_colors=B;A.settings.rambi_colors=B;A.settings.enguarde_colors=B
		else:A.settings.dk_colors=js.document.getElementById(X).value;A.settings.diddy_colors=js.document.getElementById(Y).value;A.settings.lanky_colors=js.document.getElementById(Z).value;A.settings.tiny_colors=js.document.getElementById(a).value;A.settings.chunky_colors=js.document.getElementById(b).value;A.settings.rambi_colors=js.document.getElementById(c).value;A.settings.enguarde_colors=js.document.getElementById(d).value
	elif A.settings.random_colors:A.settings.dk_colors=B;A.settings.diddy_colors=B;A.settings.lanky_colors=B;A.settings.tiny_colors=B;A.settings.chunky_colors=B;A.settings.rambi_colors=B;A.settings.enguarde_colors=B
	R={X:A.settings.dk_colors,i:A.settings.dk_custom_color,Y:A.settings.diddy_colors,j:A.settings.diddy_custom_color,Z:A.settings.lanky_colors,l:A.settings.lanky_custom_color,a:A.settings.tiny_colors,m:A.settings.tiny_custom_color,b:A.settings.chunky_colors,o:A.settings.chunky_custom_color,c:A.settings.rambi_colors,p:A.settings.rambi_custom_color,d:A.settings.enguarde_colors,q:A.settings.enguarde_custom_color}
	for L in s:
		P={D:L[D],Q:[]}
		for S in L[I]:
			g=[T]
			if S[C]==n:g=[T,T]
			P[Q].append({'zone':S[H],E:S[E],C:S[C],U:g})
		if R[L[G]]!='vanilla':
			if R[L[G]]==B:F=f"#{format(randint(0,16777215),'06x')}"
			else:
				F=R[L[J]]
				if not F:F=T
			P[Q][0][U][0]=F
			if L[K]==4:P[Q][1][U][0]=F;t=int(f"0x{F[1:3]}",16);u=int(f"0x{F[3:5]}",16);v=int(f"0x{F[5:7]}",16);w=f"#{format(255-t,e)}{format(255-u,e)}{format(255-v,e)}";P[Q][0][U][1]=w
			V.append(P);f[f"{L[D]}"]=F
	A.settings.colors=f
	if len(V)>0:convertColors(V)