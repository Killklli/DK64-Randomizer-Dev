'Apply cosmetic elements of Kong Rando.'
from imp import source_from_cache
from random import shuffle
import js
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Lists.EnemyTypes import Enemies
def apply_kongrando_cosmetic(spoiler):
	'Rando write bananaport locations.';h=False;g='pointing_to';f='entries';e='Frantic Factory';d='Tiny Temple';V='Llama Temple';R='locked';Q='Jungle Japes';N='type';K='charspawner_changes';J='model2_changes';I='map_index';H='puzzle';F='big';E='index';C='kong';B='new_type';A=spoiler
	if A.settings.kong_rando:
		O=[297,294,296,295,293];i=[148,147,149,150,146];j=[168,169,172,170,171];k=[227,227,227,227,112];P=[Enemies.CutsceneDK,Enemies.CutsceneDiddy,Enemies.CutsceneLanky,Enemies.CutsceneTiny,Enemies.CutsceneChunky];l=[];m=[{I:7,J:[{E:48,B:O[A.shuffled_kong_placement[Q][H][C]]},{E:49,B:O[A.shuffled_kong_placement[Q][H][C]]},{E:50,B:O[A.shuffled_kong_placement[Q][H][C]]}],K:[{N:Enemies.CutsceneDiddy,B:P[A.shuffled_kong_placement[Q][R][C]]}]},{I:38,J:l,K:[]},{I:20,J:[{E:22,B:j[A.shuffled_kong_placement[V][H][C]]},{E:18,B:O[A.shuffled_kong_placement[V][H][C]]}],K:[{N:Enemies.CutsceneLanky,B:P[A.shuffled_kong_placement[V][R][C]]}]},{I:16,J:[{E:20,B:k[A.shuffled_kong_placement[d][H][C]]}],K:[{N:Enemies.CutsceneTiny,B:P[A.shuffled_kong_placement[d][R][C]]}]},{I:26,J:[{E:36,B:i[A.shuffled_kong_placement[e][H][C]]}],K:[{N:Enemies.CutsceneChunky,B:P[A.shuffled_kong_placement[e][R][C]]}]}]
		for S in A.shuffled_kong_placement.keys():
			for W in A.shuffled_kong_placement[S].keys():ROM().seek(33476640+A.shuffled_kong_placement[S][W]['write']);ROM().writeMultipleBytes(A.shuffled_kong_placement[S][W][C],1)
		for T in m:
			X=int(T[I]);Y=js.pointer_addresses[9][f][X][g];ROM().seek(Y);n=int.from_bytes(ROM().readBytes(4),F)
			for U in range(n):
				Z=Y+4+U*48;ROM().seek(Z+42);o=int.from_bytes(ROM().readBytes(2),F);L=h;M=0
				for a in T[J]:
					if a[E]==o:L=True;M=a[B]
				if L:ROM().seek(Z+40);ROM().writeMultipleBytes(M,2)
			G=js.pointer_addresses[16][f][X][g];ROM().seek(G);b=int.from_bytes(ROM().readBytes(2),F);D=2
			if b>0:
				for U in range(b):ROM().seek(G+D);p=int.from_bytes(ROM().readBytes(2),F);D+=p*6+2;ROM().seek(G+D);q=int.from_bytes(ROM().readBytes(2),F);D+=q*10+6
			ROM().seek(G+D);r=int.from_bytes(ROM().readBytes(2),F);D+=2
			for U in range(r):
				ROM().seek(G+D);s=int.from_bytes(ROM().readBytes(1),F);t=D;ROM().seek(G+D+17);u=int.from_bytes(ROM().readBytes(1),F);D+=22+u*2;L=h;M=0
				for c in T[K]:
					if c[N]==s:L=True;M=c[B]
				if L:ROM().seek(G+t);ROM().writeMultipleBytes(M,1)