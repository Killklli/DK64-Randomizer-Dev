'Update all the overlays in the ROM.'
_F='dataCompressedData'
_E='codeCompressedData'
_D='dataCompressedSize'
_C='name'
_B='dataROMAddress'
_A='codeROMAddress'
from typing import BinaryIO
overlays=[{_C:'global_asm',_A:70640,_B:797140,_D:38044},{_C:'menu',_A:835184,_B:869716,_D:1442},{_C:'multiplayer',_A:871168,_B:879096,_D:251},{_C:'minecart',_A:879360,_B:891040,_D:407},{_C:'bonus',_A:891456,_B:914246,_D:682},{_C:'race',_A:914944,_B:943258,_D:731},{_C:'?',_A:944000,_B:957719,_D:908},{_C:'boss',_A:958640,_B:997519,_D:2314},{_C:'arcade',_A:999840,_B:1029164,_D:7876},{_C:'jetpac',_A:1037040,_B:1052925,_D:2358}]
def isROMAddressOverlay(absolute_address):
	'Check if its an overlay.';A=absolute_address
	for B in overlays:
		if B[_A]==A:return True
		if B[_B]==A:return True
	return False
def readOverlayOriginalData(fr):
	'Read the original overlay data.';C='codeCompressedSize';B=fr
	for A in overlays:A[C]=A[_B]-A[_A];B.seek(A[_A]);A[_E]=B.read(A[C]-8);B.read(8);A[_F]=B.read(A[_D]-8);B.read(8)
def replaceOverlayData(absolute_address,newCompressedData):
	'Replace the overlay.';D=' - Replacing ';C=newCompressedData;B=absolute_address
	for A in overlays:
		if B==A[_A]:print(D+A[_C]+' .code with modified data');A[_E]=C;return
		if B==A[_B]:print(D+A[_C]+' .data with modified data');A[_F]=C;return
def writeModifiedOverlaysToROM(fr):
	'Write the data to ROM.';A=fr
	for B in overlays:A.seek(B[_A]);A.write(B[_E]);A.write(bytes([0,0,0,0,0,0,0,0]));A.write(B[_F]);A.write(bytes([0,0,0,0,0,0,0,0]))