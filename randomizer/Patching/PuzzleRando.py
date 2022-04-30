'Randomize puzzles.'
import random
from randomizer.Patching.Patcher import ROM
def randomize_puzzles():
	'Shuffle elements of puzzles. Currently limited to coin challenge requirements but will be extended in future.';B='coins';A='offset';D=[{A:300,B:random.randint(10,50)},{A:301,B:random.randint(20,50)},{A:302,B:random.randint(5,15)},{A:303,B:random.randint(5,12)},{A:304,B:random.randint(5,15)},{A:305,B:random.randint(40,70)},{A:306,B:random.randint(25,55)},{A:307,B:random.randint(5,45)}]
	for C in D:ROM().seek(33476640+C[A]);ROM().writeMultipleBytes(C[B],1)