'Update wrinkly hints compressed file.'
import random
from io import BytesIO
import js
from randomizer.Enums.WrinklyKong import WrinklyKong
from randomizer.Lists.WrinklyHints import Hint,hints
from randomizer.Patching.Patcher import ROM
def writeWrinklyHints(file_start_offset,text):
	'Write the text to ROM.';E=text;B=file_start_offset;ROM().seek(B);ROM().writeMultipleBytes(len(E),1);F=0;A=1
	for D in E:
		ROM().seek(B+A);ROM().writeMultipleBytes(1,1);ROM().seek(B+A+1);ROM().writeMultipleBytes(1,1);ROM().seek(B+A+2);ROM().writeMultipleBytes(len(D),1);A+=3
		for C in D:ROM().seek(B+A);ROM().writeMultipleBytes(F,4);ROM().seek(B+A+4);ROM().writeMultipleBytes(len(C),2);ROM().seek(B+A+6);ROM().writeMultipleBytes(0,2);A+=8;F+=len(C)
		ROM().seek(B+A);ROM().writeMultipleBytes(0,4);A+=4
	ROM().seek(B+A);ROM().writeMultipleBytes(F,2);A+=2
	for D in E:
		for C in D:
			for G in range(len(C)):ROM().seek(B+A+G);ROM().writeMultipleBytes(int.from_bytes(C[G].encode('ascii'),'big'),1)
			A+=len(C)
def UpdateHint(WrinklyHint,message):
	'Update the wrinkly hint with the new string.\n\n    Args:\n        WrinklyHint (Hint): Wrinkly hint object.\n        message (str): Hint message to write.\n    ';A=message
	if len(A)<=914:WrinklyHint.hint=A
	else:raise Exception('Hint message is longer than allowed.')
def updateRandomHint(message):
	'Update a random hint with the string specifed.\n\n    Args:\n        message (str): Hint message to write.\n    ';A=[]
	for B in range(len(hints)):
		if hints[B].hint=='':A.append(B)
	if len(A)>0:C=random.choice(A);UpdateHint(hints[C],message)
def PushHints():
	'Update the ROM with all hints.';B=[]
	for C in hints:
		A=C.hint
		if A=='':A='PLACEHOLDER HINT'
		B.append([A.upper()])
	writeWrinklyHints(js.pointer_addresses[12]['entries'][41]['pointing_to'],B)