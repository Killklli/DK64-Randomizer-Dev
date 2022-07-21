'Randomize puzzles.'
import random
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def chooseSFX():'Choose random SFX from bank of acceptable SFX.';B=[[98,138],[166,252],[398,411],[471,476],[519,535],[547,575],[614,631],[644,650]];A=random.choice(B);return random.randint(A[0],A[1])
def randomize_puzzles(spoiler):
	'Shuffle elements of puzzles. Currently limited to coin challenge requirements but will be extended in future.';B='coins';A='offset'
	if spoiler.settings.puzzle_rando:
		F=[{A:300,B:random.randint(10,50)},{A:301,B:random.randint(20,50)},{A:302,B:random.randint(5,15)},{A:303,B:random.randint(5,12)},{A:304,B:random.randint(5,15)},{A:305,B:random.randint(40,70)},{A:306,B:random.randint(25,55)},{A:307,B:random.randint(5,45)}]
		for D in F:ROM().seek(33476640+D[A]);ROM().writeMultipleBytes(D[B],1)
		E=[]
		for G in range(8):
			ROM().seek(33476640+332+2*G);C=chooseSFX()
			while C in E:C=chooseSFX()
			E.append(C);ROM().writeMultipleBytes(C,2)
		for H in range(7):ROM().seek(535625760+348+H);I=random.randint(0,5);ROM().writeMultipleBytes(I,1)