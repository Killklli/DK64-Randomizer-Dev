'Randomize puzzles.'
import random
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def chooseSFX():'Choose random SFX from bank of acceptable SFX.';B=[[98,138],[166,252],[398,411],[471,476],[519,535],[547,575],[614,631],[644,650]];A=random.choice(B);return random.randint(A[0],A[1])
def randomize_puzzles(spoiler):
	'Shuffle elements of puzzles. Currently limited to coin challenge requirements but will be extended in future.';J=spoiler;I='seal_race';H='castle_race';G='factory_race';C='coins';B='offset';D=J.settings.rom_data
	if J.settings.puzzle_rando:
		A={G:[5,15],H:[5,15],I:[5,12]}
		if J.settings.fast_gbs:A[G]=[3,8];A[H]=[5,12];A[I]=[5,10]
		M=[{B:316,C:random.randint(10,50)},{B:317,C:random.randint(20,50)},{B:318,C:random.randint(A[G][0],A[G][1])},{B:319,C:random.randint(A[I][0],A[I][1])},{B:320,C:random.randint(A[H][0],A[H][1])},{B:321,C:random.randint(40,70)},{B:322,C:random.randint(25,55)},{B:323,C:random.randint(5,45)}]
		for K in M:ROM().seek(D+K[B]);ROM().writeMultipleBytes(K[C],1)
		L=[]
		for N in range(8):
			ROM().seek(D+348+2*N);E=chooseSFX()
			while E in L:E=chooseSFX()
			L.append(E);ROM().writeMultipleBytes(E,2)
		for O in range(7):ROM().seek(D+364+O);P=random.randint(0,5);ROM().writeMultipleBytes(P,1)
		for F in range(9):
			ROM().seek(D+382+F)
			if F==8:ROM().writeMultipleBytes(random.choice([0,1,3]),1)
			else:ROM().writeMultipleBytes(random.randint(0,3),1)
			ROM().seek(D+391+F)
			if F==2:ROM().writeMultipleBytes(random.choice([0,1,3]),1)
			else:ROM().writeMultipleBytes(random.randint(0,3),1)