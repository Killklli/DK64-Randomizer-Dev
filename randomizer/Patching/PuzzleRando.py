'Randomize puzzles.'
import random
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def chooseSFX():'Choose random SFX from bank of acceptable SFX.';B=[[98,138],[166,252],[398,411],[471,476],[519,535],[547,575],[614,631],[644,650]];A=random.choice(B);return random.randint(A[0],A[1])
def randomize_puzzles(spoiler):
	'Shuffle elements of puzzles. Currently limited to coin challenge requirements but will be extended in future.';H=spoiler;G='seal_race';F='castle_race';E='factory_race';C='coins';B='offset'
	if H.settings.puzzle_rando:
		A={E:[5,15],F:[5,15],G:[5,12]}
		if H.settings.fast_gbs:A[E]=[3,8];A[F]=[5,12];A[G]=[5,10]
		K=[{B:300,C:random.randint(10,50)},{B:301,C:random.randint(20,50)},{B:302,C:random.randint(A[E][0],A[E][1])},{B:303,C:random.randint(A[G][0],A[G][1])},{B:304,C:random.randint(A[F][0],A[F][1])},{B:305,C:random.randint(40,70)},{B:306,C:random.randint(25,55)},{B:307,C:random.randint(5,45)}]
		for I in K:ROM().seek(33476640+I[B]);ROM().writeMultipleBytes(I[C],1)
		J=[]
		for L in range(8):
			ROM().seek(33476640+332+2*L);D=chooseSFX()
			while D in J:D=chooseSFX()
			J.append(D);ROM().writeMultipleBytes(D,2)
		for M in range(7):ROM().seek(33476640+348+M);N=random.randint(0,5);ROM().writeMultipleBytes(N,1)