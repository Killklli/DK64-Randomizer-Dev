'Apply cosmetic skins to kongs.'
_K='big'
_J='lanky'
_I=True
_H='tiny'
_G='diddy'
_F='dk'
_E='#000000'
_D='chunky'
_C=False
_B='pointing_to'
_A='entries'
import random
from random import randint
import js
from randomizer.Patching.generate_kong_color_images import convertColors
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from PIL import Image,ImageEnhance
import zlib,gzip
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';y='sparkle';x='disco_chunky';w='checkered';v='patch';u='overalls';t='override_cosmetics';o='02x';n='enguarde_custom_color';m='enguarde_colors';l='rambi_custom_color';k='rambi_colors';j='tiny_custom_color';i='tiny_colors';h='lanky_custom_color';g='lanky_colors';f='diddy_custom_color';e='diddy_colors';d='dk_custom_color';c='dk_colors';b='base';X='chunky_custom_color';W='chunky_colors';S='colors';Q='zones';M='block';L='custom_setting';J='base_setting';I='palettes';H='kong_index';G='name';E='randomized';D='image';C='kong';B='fill_type';A=spoiler;N=0;T=A.settings.rom_data
	if js.document.getElementById(t).checked:O=js.document.getElementById('klaptrap_model').value
	else:O=A.settings.klaptrap_model
	if O=='green':N=33
	elif O=='purple':N=34
	elif O=='red':N=35
	elif O=='random_klap':N=random.randint(33,35)
	elif O=='random_model':z=[25,30,32,33,34,35,36,38,39,48,52,66,71,75,81,98,105,112,114,150,176,177,189];N=random.choice(z)
	A.settings.klaptrap_model_index=N
	if A.settings.misc_cosmetics:
		ROM().seek(T+406);ROM().write(1);ROM().seek(T+407)
		for A5 in range(24):ROM().writeMultipleBytes(random.randint(0,255),1)
		ROM().seek(T+431)
		for A6 in range(2):ROM().writeMultipleBytes(random.randint(0,2),1)
	ROM().seek(T+310);ROM().writeMultipleBytes(N,1);Y=[];p={};U={};A0=[{C:_F,I:[{G:b,D:3724,B:M}],J:c,L:d,H:0},{C:_G,I:[{G:'cap_shirt',D:3686,B:M}],J:e,L:f,H:1},{C:_J,I:[{G:u,D:3689,B:M},{G:v,D:3734,B:v}],J:g,L:h,H:2},{C:_H,I:[{G:u,D:6014,B:M}],J:i,L:j,H:3},{C:_D,I:[{G:'shirt_back',D:3769,B:w},{G:'shirt_front',D:3687,B:M}],J:W,L:X,H:4},{C:x,I:[{G:'shirt',D:3777,B:y},{G:'gloves',D:3778,B:y}],J:W,L:X,H:4},{C:'rambi',I:[{G:b,D:3826,B:M}],J:k,L:l,H:5},{C:'enguarde',I:[{G:b,D:3847,B:M}],J:m,L:n,H:6}]
	if js.document.getElementById(t).checked:
		if js.document.getElementById('random_colors').checked:A.settings.dk_colors=E;A.settings.diddy_colors=E;A.settings.lanky_colors=E;A.settings.tiny_colors=E;A.settings.chunky_colors=E;A.settings.rambi_colors=E;A.settings.enguarde_colors=E
		else:A.settings.dk_colors=js.document.getElementById(c).value;A.settings.dk_custom_color=js.document.getElementById(d).value;A.settings.diddy_colors=js.document.getElementById(e).value;A.settings.diddy_custom_color=js.document.getElementById(f).value;A.settings.lanky_colors=js.document.getElementById(g).value;A.settings.lanky_custom_color=js.document.getElementById(h).value;A.settings.tiny_colors=js.document.getElementById(i).value;A.settings.tiny_custom_color=js.document.getElementById(j).value;A.settings.chunky_colors=js.document.getElementById(W).value;A.settings.chunky_custom_color=js.document.getElementById(X).value;A.settings.rambi_colors=js.document.getElementById(k).value;A.settings.rambi_custom_color=js.document.getElementById(l).value;A.settings.enguarde_colors=js.document.getElementById(m).value;A.settings.enguarde_custom_color=js.document.getElementById(n).value
	elif A.settings.random_colors:A.settings.dk_colors=E;A.settings.diddy_colors=E;A.settings.lanky_colors=E;A.settings.tiny_colors=E;A.settings.chunky_colors=E;A.settings.rambi_colors=E;A.settings.enguarde_colors=E
	U={c:A.settings.dk_colors,d:A.settings.dk_custom_color,e:A.settings.diddy_colors,f:A.settings.diddy_custom_color,g:A.settings.lanky_colors,h:A.settings.lanky_custom_color,i:A.settings.tiny_colors,j:A.settings.tiny_custom_color,W:A.settings.chunky_colors,X:A.settings.chunky_custom_color,k:A.settings.rambi_colors,l:A.settings.rambi_custom_color,m:A.settings.enguarde_colors,n:A.settings.enguarde_custom_color}
	for F in A0:
		V=_I
		if F[H]==4:
			Z=A.settings.disco_chunky
			if A.settings.krusha_slot==_D:Z=_C
			if Z and F[C]==_D:V=_C
			elif not Z and F[C]==x:V=_C
		q=[_F,_G,_J,_H,_D];r=_C
		if A.settings.krusha_slot in q:
			if q.index(A.settings.krusha_slot)==F[H]:r=_I;F[I]=[{G:'krusha_skin',D:4971,B:M},{G:'krusha_indicator',D:4966,B:C}];V=_I
		if V:
			P={C:F[C],Q:[]}
			for R in F[I]:
				a=[_E]
				if R[B]==w:a=[_E,_E]
				elif R[B]==C:A1=['#ffd700','#ff0000','#1699ff','#B045ff','#41ff25'];a=[A1[F[H]]]
				P[Q].append({'zone':R[G],D:R[D],B:R[B],S:a})
			if U[F[J]]!='vanilla':
				if U[F[J]]==E:K=f"#{format(randint(0,16777215),'06x')}"
				else:
					K=U[F[L]]
					if not K:K=_E
				P[Q][0][S][0]=K
				if F[H]in(2,4)and not r:
					P[Q][1][S][0]=K
					if F[H]==4:
						A2=int(f"0x{K[1:3]}",16);A3=int(f"0x{K[3:5]}",16);A4=int(f"0x{K[5:7]}",16);s=f"#{format(255-A2,o)}{format(255-A3,o)}{format(255-A4,o)}"
						if A.settings.disco_chunky:P[Q][1][S][0]=s
						else:P[Q][0][S][1]=s
				Y.append(P);p[f"{F[C]}"]=K
	A.settings.colors=p
	if len(Y)>0:convertColors(Y)
color_bases=[]
balloon_single_frames=[(4,38),(5,38),(5,38),(5,38),(5,38),(5,38),(4,38),(4,38)]
def getFile(table_index,file_index,compressed,width,height):
	'Grab image from file.';F=height;E=file_index;D=table_index;B=width;G=js.pointer_addresses[D][_A][E][_B];L=js.pointer_addresses[D][_A][E+1][_B];M=L-G;ROM().seek(G);C=ROM().readBytes(M)
	if compressed:C=zlib.decompress(C,15+32)
	H=Image.new(mode='RGBA',size=(B,F));N=H.load()
	for I in range(F):
		for J in range(B):K=(I*B+J)*2;A=int.from_bytes(C[K:K+2],_K);O=(A>>11&31)<<3;P=(A>>6&31)<<3;Q=(A>>1&31)<<3;R=(A&1)*255;N[(J,I)]=O,P,Q,R
	return H
def getRGBFromHash(hash):'Convert hash RGB code to rgb array.';A=int(hash[1:3],16);B=int(hash[3:5],16);C=int(hash[5:7],16);return[A,B,C]
def maskImage(im_f,base_index,min_y):
	'Apply RGB mask to image.';D=min_y;A=im_f;E,F=A.size;K=ImageEnhance.Color(A);A=K.enhance(0);C=A.crop((0,D,E,F));L=ImageEnhance.Brightness(C);C=L.enhance(2);A.paste(C,(0,D),C);H=A.load();M=getRGBFromHash(color_bases[base_index]);E,F=A.size
	for I in range(E):
		for J in range(D,F):
			B=list(H[(I,J)])
			if B[3]>0:
				for G in range(3):B[G]=int(M[G]*(B[G]/255))
				H[(I,J)]=B[0],B[1],B[2],B[3]
	return A
def writeColorImageToROM(im_f,table_index,file_index,width,height):
	'Write texture to ROM.';F=height;E=width;C=file_index;A=table_index;G=js.pointer_addresses[A][_A][C][_B];J=js.pointer_addresses[A][_A][C+1][_B];K=J-G;ROM().seek(G);L=im_f.load();E,F=im_f.size;H=[]
	for M in range(F):
		for N in range(E):D=list(L[(N,M)]);O=int(D[0]>>3<<11);P=int(D[1]>>3<<6);Q=int(D[2]>>3<<1);R=int(D[3]!=0);I=O|P|Q|R;H.extend([I>>8&255,I&255])
	B=bytearray(H)
	if len(B)>2*E*F:print(f"Image too big error: {A} > {C}")
	if A==25:B=gzip.compress(B,compresslevel=9)
	if len(B)>K:print(f"File too big error: {A} > {C}")
	ROM().writeBytes(B)
def writeColorToROM(color,table_index,file_index):
	'Write color to ROM.';E=table_index;G=js.pointer_addresses[E][_A][file_index][_B];C=getRGBFromHash(color);H=int(C[0]>>3<<11);I=int(C[1]>>3<<6);J=int(C[2]>>3<<1);A=H|I|J|1;B=[]
	for K in range(42):
		for L in range(32):B.extend([A>>8&255,A&255])
	for F in range(18):B.extend([A>>8&255,A&255])
	for F in range(4):B.extend([0,0])
	for F in range(3):B.extend([A>>8&255,A&255])
	D=bytearray(B)
	if E==25:D=gzip.compress(D,compresslevel=9)
	ROM().seek(G);ROM().writeBytes(D)
def overwrite_object_colors(spoiler):
	'Overwrite object colors.';global color_bases;E=spoiler.settings.colorblind_mode
	if E!='off':
		if E=='prot-deut':color_bases=['#FFB000','#FF6666','#00A3FF','#E1F90C','#4C2E2A']
		elif E=='trit':color_bases=['#FFC302','#FF0000','#66C7FF','#1D439E',_E]
		A=175;C=getFile(7,A,_C,44,44);C=C.resize((21,21))
		for B in range(5):
			writeColorToROM(color_bases[B],25,[4124,4122,4123,4120,4121][B])
			for A in range(152,160):F=getFile(7,A,_C,44,44);F=maskImage(F,B,0);I=[168,152,232,208,240];writeColorImageToROM(F,7,I[B]+(A-152),44,44)
			for A in range(216,224):G=getFile(7,A,_C,48,42);G=maskImage(G,B,0);J=[224,256,248,216,264];writeColorImageToROM(G,7,J[B]+(A-216),48,42)
			for A in range(274,286):H=getFile(7,A,_C,44,44);H=maskImage(H,B,0);K=[274,854,818,842,830];writeColorImageToROM(H,7,K[B]+(A-274),44,44)
			for A in range(5819,5827):D=getFile(25,A,_I,32,64);D=maskImage(D,B,33);D.paste(C,balloon_single_frames[A-5819],C);L=[5835,5827,5843,5851,5819];writeColorImageToROM(D,25,L[B]+(A-5819),32,64)
def applyKrushaKong(spoiler):
	'Apply Krusha Kong setting.';A=spoiler;B=[_F,_G,_J,_H,_D]
	if A.settings.krusha_slot=='random':
		C=[_F,_G,_H]
		if not A.settings.disco_chunky:C.append(_D)
		A.settings.krusha_slot=random.choice(C)
	print(A.settings.krusha_slot);ROM().seek(A.settings.rom_data+284)
	if A.settings.krusha_slot=='no_slot':ROM().write(255)
	elif A.settings.krusha_slot in B:D=B.index(A.settings.krusha_slot);ROM().write(D);placeKrushaHead(D)
def placeKrushaHead(slot):
	"Replace a kong's face with the Krusha face.";C=slot;Q=[[636,635],[633,634],[631,632],[630,629],[627,628]];R=[[579,586],[580,587],[581,588],[582,589],[577,578]];ROM().seek(33513472);K=[];L=[];M=[];N=[];G=[];H=[]
	for B in range(64):
		I=[];J=[]
		for A in range(64):
			D=int.from_bytes(ROM().readBytes(1),_K);E=int.from_bytes(ROM().readBytes(1),_K);F=D<<8|E;S=(F>>11&31)<<3;T=(F>>6&31)<<3;U=(F>>1&31)<<3;O=0
			if F&1:O=255
			V=[S,T,U,O]
			if A<32:L.extend([D,E])
			else:K.extend([D,E])
			if A%2+B%2==0:I.extend([D,E]);J.extend(V)
		if len(I)>0 and len(J):G.append(I);H.append(J)
	G.reverse()
	for B in G:M.extend(B)
	H.reverse()
	for B in H:N.extend(B)
	for A in range(2):P=[L,K][A];W=Q[C][A];X=R[C][A];Y=js.pointer_addresses[25][_A][W][_B];Z=js.pointer_addresses[7][_A][X][_B];a=gzip.compress(bytearray(P),compresslevel=9);ROM().seek(Y);ROM().writeBytes(a);ROM().seek(Z);ROM().writeBytes(bytearray(P))
	b=js.pointer_addresses[14][_A][196+C][_B];c=js.pointer_addresses[14][_A][190+C][_B];d=gzip.compress(bytearray(M),compresslevel=9);e=gzip.compress(bytearray(N),compresslevel=9);ROM().seek(b);ROM().writeBytes(bytearray(e));ROM().seek(c);ROM().writeBytes(bytearray(d))