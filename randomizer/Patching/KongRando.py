'Apply cosmetic elements of Kong Rando.'
from imp import source_from_cache
from random import shuffle
import js
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Lists.EnemyTypes import Enemies
def apply_kongrando_cosmetic(spoiler):
	'Rando write bananaport locations.';j=False;i='pointing_to';h='entries';g='Frantic Factory';W='Tiny Temple';V='Llama Temple';R='locked';Q='Jungle Japes';N='type';K='charspawner_changes';J='model2_changes';I='map_index';G='big';F='puzzle';E='index';C='kong';B='new_type';A=spoiler
	if A.settings.kong_rando:
		O=[297,294,296,295,293];X=[148,147,149,150,146];Y=[168,169,172,170,171];P=[Enemies.CutsceneDK,Enemies.CutsceneDiddy,Enemies.CutsceneLanky,Enemies.CutsceneTiny,Enemies.CutsceneChunky];k=[];l=[{I:7,J:[{E:48,B:O[A.shuffled_kong_placement[Q][F][C]]},{E:49,B:O[A.shuffled_kong_placement[Q][F][C]]},{E:50,B:O[A.shuffled_kong_placement[Q][F][C]]}],K:[{N:Enemies.CutsceneDiddy,B:P[A.shuffled_kong_placement[Q][R][C]]}]},{I:38,J:k,K:[]},{I:20,J:[{E:22,B:Y[A.shuffled_kong_placement[V][F][C]]},{E:18,B:O[A.shuffled_kong_placement[V][F][C]]}],K:[{N:Enemies.CutsceneLanky,B:P[A.shuffled_kong_placement[V][R][C]]}]},{I:16,J:[{E:0,B:X[A.shuffled_kong_placement[W][F][C]]},{E:4,B:Y[A.shuffled_kong_placement[W][F][C]]}],K:[{N:Enemies.CutsceneTiny,B:P[A.shuffled_kong_placement[W][R][C]]}]},{I:26,J:[{E:36,B:X[A.shuffled_kong_placement[g][F][C]]}],K:[{N:Enemies.CutsceneChunky,B:P[A.shuffled_kong_placement[g][R][C]]}]}]
		for S in A.shuffled_kong_placement.keys():
			for Z in A.shuffled_kong_placement[S].keys():ROM().seek(33476640+A.shuffled_kong_placement[S][Z]['write']);ROM().writeMultipleBytes(A.shuffled_kong_placement[S][Z][C],1)
		for T in l:
			a=int(T[I]);b=js.pointer_addresses[9][h][a][i];ROM().seek(b);m=int.from_bytes(ROM().readBytes(4),G)
			for U in range(m):
				c=b+4+U*48;ROM().seek(c+42);n=int.from_bytes(ROM().readBytes(2),G);L=j;M=0
				for d in T[J]:
					if d[E]==n:L=True;M=d[B]
				if L:ROM().seek(c+40);ROM().writeMultipleBytes(M,2)
			H=js.pointer_addresses[16][h][a][i];ROM().seek(H);e=int.from_bytes(ROM().readBytes(2),G);D=2
			if e>0:
				for U in range(e):ROM().seek(H+D);o=int.from_bytes(ROM().readBytes(2),G);D+=o*6+2;ROM().seek(H+D);p=int.from_bytes(ROM().readBytes(2),G);D+=p*10+6
			ROM().seek(H+D);q=int.from_bytes(ROM().readBytes(2),G);D+=2
			for U in range(q):
				ROM().seek(H+D);r=int.from_bytes(ROM().readBytes(1),G);s=D;ROM().seek(H+D+17);t=int.from_bytes(ROM().readBytes(1),G);D+=22+t*2;L=j;M=0
				for f in T[K]:
					if f[N]==r:L=True;M=f[B]
				if L:ROM().seek(H+s);ROM().writeMultipleBytes(M,1)