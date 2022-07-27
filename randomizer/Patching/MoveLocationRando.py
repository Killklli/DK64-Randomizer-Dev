'Randomize Move Locations.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
moveRandoOffset=167
dk_crankymoves=[]
diddy_crankymoves=[]
lanky_crankymoves=[]
tiny_crankymoves=[]
chunky_crankymoves=[]
dk_funkymoves=[]
diddy_funkymoves=[]
lanky_funkymoves=[]
tiny_funkymoves=[]
chunky_funkymoves=[]
dk_candymoves=[]
diddy_candymoves=[]
lanky_candymoves=[]
tiny_candymoves=[]
chunky_candymoves=[]
def randomize_moves(spoiler):
	'Randomize Move locations based on move_data from spoiler.';B=spoiler;F=B.settings.rom_data
	if B.settings.shuffle_items=='moves'and B.move_data is not None:
		A=B.move_data.copy()
		for C in range(3):
			for D in range(5):
				for E in range(8):
					if A[C][D][E]==-1:G=5;A[C][D][E]=G<<5
		H=A[0][0];I=A[0][1];J=A[0][2];K=A[0][3];L=A[0][4];M=A[1][0];N=A[1][1];O=A[1][2];P=A[1][3];Q=A[1][4];R=A[2][0];S=A[2][1];T=A[2][2];U=A[2][3];V=A[2][4];ROM().seek(F+moveRandoOffset);ROM().write(1);ROM().writeBytes(bytearray(H));ROM().writeBytes(bytearray(I));ROM().writeBytes(bytearray(J));ROM().writeBytes(bytearray(K));ROM().writeBytes(bytearray(L));ROM().writeBytes(bytearray(M));ROM().writeBytes(bytearray(N));ROM().writeBytes(bytearray(O));ROM().writeBytes(bytearray(P));ROM().writeBytes(bytearray(Q));ROM().writeBytes(bytearray(R));ROM().writeBytes(bytearray(S));ROM().writeBytes(bytearray(T));ROM().writeBytes(bytearray(U));ROM().writeBytes(bytearray(V))