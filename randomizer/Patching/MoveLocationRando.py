'Randomize Move Locations.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
varspaceOffset=33476640
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
	'Randomize Move locations based on move_data from spoiler.';B=spoiler
	if B.settings.shuffle_items=='moves'and B.move_data is not None:
		A=B.move_data.copy()
		for C in range(3):
			for D in range(5):
				for E in range(7):
					if A[C][D][E]==-1:F=5;A[C][D][E]=F<<5
		G=A[0][0];H=A[0][1];I=A[0][2];J=A[0][3];K=A[0][4];L=A[1][0];M=A[1][1];N=A[1][2];O=A[1][3];P=A[1][4];Q=A[2][0];R=A[2][1];S=A[2][2];T=A[2][3];U=A[2][4];ROM().seek(varspaceOffset+moveRandoOffset);ROM().write(1);ROM().writeBytes(bytearray(G));ROM().writeBytes(bytearray(H));ROM().writeBytes(bytearray(I));ROM().writeBytes(bytearray(J));ROM().writeBytes(bytearray(K));ROM().writeBytes(bytearray(L));ROM().writeBytes(bytearray(M));ROM().writeBytes(bytearray(N));ROM().writeBytes(bytearray(O));ROM().writeBytes(bytearray(P));ROM().writeBytes(bytearray(Q));ROM().writeBytes(bytearray(R));ROM().writeBytes(bytearray(S));ROM().writeBytes(bytearray(T));ROM().writeBytes(bytearray(U))