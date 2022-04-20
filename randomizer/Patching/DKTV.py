'Setting data related to DKTV.'
import random,js
from randomizer.Patching.Patcher import ROM
def randomize_dktv():
	'Set our DKTV to a random intro.';A=[0,1,2,3,4,5];C=[67109344,660,16777696,50332248,33555032,83886560];random.shuffle(A)
	for B in range(5):ROM().seek(33476640+332+B*4);D=A[B];ROM().writeMultipleBytes(C[D],4)