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
def writeMoveDataToROM(arr):
	'Write move data to ROM.';F='price';C='flag';B='move_type'
	for A in arr:
		if A[B]==C:
			D={'dive':386,'orange':388,'barrel':389,'vine':387,'camera':765,'shockwave':377,'camera_shockwave':65534};E=65535
			if A[C]in D:E=D[A[C]]
			ROM().writeMultipleBytes(5<<5,1);ROM().writeMultipleBytes(A[F],1);ROM().writeMultipleBytes(E,2)
		elif A[B]is None:ROM().writeMultipleBytes(7<<5,1);ROM().writeMultipleBytes(0,1);ROM().writeMultipleBytes(65535,2)
		else:G=['special','slam','gun','ammo_belt','instrument'];H=G.index(A[B])<<5|A['move_lvl']<<3|A['move_kong'];ROM().writeMultipleBytes(H,1);ROM().writeMultipleBytes(A[F],1);ROM().writeMultipleBytes(65535,2)
def randomize_moves(spoiler):
	'Randomize Move locations based on move_data from spoiler.';B=spoiler;C=B.settings.rom_data;D=B.settings.move_location_data
	if B.settings.move_rando not in('off','starts_with')and B.move_data is not None:A=B.move_data.copy();E=A[0][0][0];F=A[0][0][1];G=A[0][0][2];H=A[0][0][3];I=A[0][0][4];J=A[0][1][0];K=A[0][1][1];L=A[0][1][2];M=A[0][1][3];N=A[0][1][4];O=A[0][2][0];P=A[0][2][1];Q=A[0][2][2];R=A[0][2][3];S=A[0][2][4];T=A[1];U=A[2];ROM().seek(C+moveRandoOffset);ROM().write(1);ROM().seek(D);writeMoveDataToROM(E);writeMoveDataToROM(F);writeMoveDataToROM(G);writeMoveDataToROM(H);writeMoveDataToROM(I);writeMoveDataToROM(J);writeMoveDataToROM(K);writeMoveDataToROM(L);writeMoveDataToROM(M);writeMoveDataToROM(N);writeMoveDataToROM(O);writeMoveDataToROM(P);writeMoveDataToROM(Q);writeMoveDataToROM(R);writeMoveDataToROM(S);writeMoveDataToROM(T);writeMoveDataToROM(U)