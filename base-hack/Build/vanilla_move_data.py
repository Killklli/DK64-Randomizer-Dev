'Get vanilla move data.'
_K='chunky'
_J='tiny'
_I='lanky'
_H='diddy'
_G='ammo_belt'
_F='gun'
_E='instrument'
_D='slam'
_C='flag'
_B='special'
_A='nothing'
from typing import BinaryIO
special_move_prices=[3,5,7]
gun_price=3
ins_price=3
slam_prices=[5,7]
gun_upg_prices=[5,7]
ammo_belt_prices=[3,5]
ins_upg_prices=[5,7,9]
class MoveType:
	'Class which stores info about move types.'
	def __init__(A,type,index=1,price=0):'Initialize with given data.';A.type=type;A.index=index;A.price=price
cranky_0=[MoveType(_B,1,3),MoveType(_B,2,5),MoveType(_B,3,7),MoveType(_A),MoveType(_D,2,5),MoveType(_A),MoveType(_D,2,7),MoveType(_A)]
cranky_1=[MoveType(_B,1,3),MoveType(_A),MoveType(_B,2,5),MoveType(_A),MoveType(_D,2,5),MoveType(_B,3,7),MoveType(_D,2,7),MoveType(_A)]
funky=[MoveType(_F,1,3),MoveType(_A),MoveType(_G,1,3),MoveType(_A),MoveType(_F,2,5),MoveType(_G,2,5),MoveType(_F,3,7),MoveType(_A)]
candy=[MoveType(_A),MoveType(_E,1,3),MoveType(_A),MoveType(_E,2,5),MoveType(_A),MoveType(_E,3,7),MoveType(_E,3,9),MoveType(_A)]
cranky_moves={'dk':cranky_0.copy(),_H:cranky_0.copy(),_I:cranky_1.copy(),_J:cranky_1.copy(),_K:cranky_1.copy()}
funky_moves={'dk':funky.copy(),_H:funky.copy(),_I:funky.copy(),_J:funky.copy(),_K:funky.copy()}
candy_moves={'dk':candy.copy(),_H:candy.copy(),_I:candy.copy(),_J:candy.copy(),_K:candy.copy()}
training={'dive':MoveType(_C,386),'orange':MoveType(_C,388),'barrel':MoveType(_C,389),'vine':MoveType(_C,387)}
bfi={'bfi':MoveType(_C,-2)}
def convertItem(item,kong):
	'Convert move item to encoded int.';A=item;B=0;C=65535;E=[_B,_D,_F,_G,_E,_C,'gb'];F=[_C,'gb'];G=[_D,_G]
	if A.type==_A:B=7<<5
	elif A.type in E:
		B=(E.index(A.type)&7)<<5;D=kong&7
		if A.type in G:D=0
		elif A.type==_E and A.index>1:D=0
		H=A.index-1&3;B|=H<<3;B|=D
		if A.type in F:
			C=A.index
			if C<0:C+=65536
	return B<<24|A.price<<16|C
price_offset=54
space_offset=33476640
move_offset=33484800
def getWrite(value,kong):
	'Get value of move.';A=value;type=A>>4&15
	if type==15:type=7
	if type==7:B=0
	else:B=(A&15)-1
	C=(type&7)<<5|(B&3)<<3|kong&7;return C
def writeVanillaMoveData(fh):
	'Write vanilla move data.';B='big';A=fh;print('Writing vanilla move data');A.seek(space_offset+69);A.write(bytearray(slam_prices));A.seek(space_offset+83);A.write(bytearray(ammo_belt_prices));A.write(bytearray(ins_upg_prices));A.seek(move_offset)
	for J in range(int(1024/4)):A.write((0).to_bytes(4,B))
	A.seek(move_offset);D=[cranky_moves,funky_moves,candy_moves]
	for C in D:
		for (E,F) in enumerate(C):
			for G in C[F]:A.write(convertItem(G,E).to_bytes(4,B))
	for H in training:I=training[H];A.write(convertItem(I,0).to_bytes(4,B))
	A.write(convertItem(bfi['bfi'],0).to_bytes(4,B))