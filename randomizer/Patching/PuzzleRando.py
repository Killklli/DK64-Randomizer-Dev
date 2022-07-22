'Randomize puzzles.'
import random
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def chooseSFX():'Choose random SFX from bank of acceptable SFX.';B=[[98,138],[166,252],[398,411],[471,476],[519,535],[547,575],[614,631],[644,650]];A=random.choice(B);return random.randint(A[0],A[1])
def randomize_puzzles(spoiler):
	'Shuffle elements of puzzles. Currently limited to coin challenge requirements but will be extended in future.';E=spoiler;C='coins';B='offset'
	if E.settings.puzzle_rando:
		A={'factory_race':[5,15],'castle_race':[5,15],'seal_race':[5,12]}
		if E.settings.fast_gbs:A.factory_race=[3,8];A.castle_race=[5,12];A.seal_race=[5,10]
		H=[{B:300,C:random.randint(10,50)},{B:301,C:random.randint(20,50)},{B:302,C:random.randint(A.factory_race[1],A.factory_race[2])},{B:303,C:random.randint(A.seal_race[1],A.seal_race[2])},{B:304,C:random.randint(A.castle_race[1],A.castle_race[2])},{B:305,C:random.randint(40,70)},{B:306,C:random.randint(25,55)},{B:307,C:random.randint(5,45)}]
		for F in H:ROM().seek(33476640+F[B]);ROM().writeMultipleBytes(F[C],1)
		G=[]
		for I in range(8):
			ROM().seek(33476640+332+2*I);D=chooseSFX()
			while D in G:D=chooseSFX()
			G.append(D);ROM().writeMultipleBytes(D,2)
		for J in range(7):ROM().seek(33476640+348+J);K=random.randint(0,5);ROM().writeMultipleBytes(K,1)