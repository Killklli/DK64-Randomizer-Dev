'Apply cosmetic elements of Kong Rando.'
import random
from imp import source_from_cache
import js
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.EnemyTypes import Enemies
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def apply_kongrando_cosmetic(spoiler):
	'Rando write bananaport locations.';n=False;m='pointing_to';l='entries';k='Frantic Factory';j='Llama Temple';i='Tiny Temple';h='Jungle Japes';Q='locked';P='puzzle';M='type';J='charspawner_changes';I='model2_changes';H='map_index';F='big';E='index';D='kong';B='new_type';A=spoiler
	if A.settings.kong_rando:
		N=[297,294,296,295,293];o=[148,147,149,150,146];p=[168,169,172,170,171];q=[227,227,227,227,112];O=[Enemies.CutsceneDK,Enemies.CutsceneDiddy,Enemies.CutsceneLanky,Enemies.CutsceneTiny,Enemies.CutsceneChunky];R=A.shuffled_kong_placement[h][P][D];S=A.shuffled_kong_placement[h][Q][D]
		if S==Kongs.any:S=Kongs.diddy
		r=A.shuffled_kong_placement[i][P][D];T=A.shuffled_kong_placement[i][Q][D]
		if T==Kongs.any:T=Kongs.tiny
		Z=A.shuffled_kong_placement[j][P][D];U=A.shuffled_kong_placement[j][Q][D]
		if U==Kongs.any:U=Kongs.lanky
		s=A.shuffled_kong_placement[k][P][D];V=A.shuffled_kong_placement[k][Q][D]
		if V==Kongs.any:V=Kongs.chunky
		t=[];u=[{H:7,I:[{E:48,B:N[R]},{E:49,B:N[R]},{E:50,B:N[R]}],J:[{M:Enemies.CutsceneDiddy,B:O[S]}]},{H:38,I:t,J:[]},{H:20,I:[{E:22,B:p[Z]},{E:18,B:N[Z]}],J:[{M:Enemies.CutsceneLanky,B:O[U]}]},{H:16,I:[{E:20,B:q[r]}],J:[{M:Enemies.CutsceneTiny,B:O[T]}]},{H:26,I:[{E:36,B:o[s]}],J:[{M:Enemies.CutsceneChunky,B:O[V]}]}]
		for W in A.shuffled_kong_placement.keys():
			for a in A.shuffled_kong_placement[W].keys():ROM().seek(A.settings.rom_data+A.shuffled_kong_placement[W][a]['write']);ROM().writeMultipleBytes(A.shuffled_kong_placement[W][a][D],1)
		for X in u:
			b=int(X[H]);c=js.pointer_addresses[9][l][b][m];ROM().seek(c);v=int.from_bytes(ROM().readBytes(4),F)
			for Y in range(v):
				d=c+4+Y*48;ROM().seek(d+42);w=int.from_bytes(ROM().readBytes(2),F);K=n;L=0
				for e in X[I]:
					if e[E]==w:K=True;L=e[B]
				if K:ROM().seek(d+40);ROM().writeMultipleBytes(L,2)
			G=js.pointer_addresses[16][l][b][m];ROM().seek(G);f=int.from_bytes(ROM().readBytes(2),F);C=2
			if f>0:
				for Y in range(f):ROM().seek(G+C);x=int.from_bytes(ROM().readBytes(2),F);C+=x*6+2;ROM().seek(G+C);y=int.from_bytes(ROM().readBytes(2),F);C+=y*10+6
			ROM().seek(G+C);z=int.from_bytes(ROM().readBytes(2),F);C+=2
			for Y in range(z):
				ROM().seek(G+C);A0=int.from_bytes(ROM().readBytes(1),F);A1=C;ROM().seek(G+C+17);A2=int.from_bytes(ROM().readBytes(1),F);C+=22+A2*2;K=n;L=0
				for g in X[J]:
					if g[M]==A0:K=True;L=g[B]
				if K:ROM().seek(G+A1);ROM().writeMultipleBytes(L,1)