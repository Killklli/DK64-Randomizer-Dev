'Store vanilla warp data and write to ROM.'
from typing import BinaryIO
class WarpInfo:
	'Warp Vanilla Information.'
	def __init__(A,map,ids,tied_exits,active_flags,appear_flags=[-1,-1]):'Initialize with given data.';A.map=map;A.ids=ids;A.tied_exits=tied_exits;A.active_flags=active_flags;A.appear_flags=appear_flags
warp_info_data=[WarpInfo(34,[16,17],[13,14],[433,434]),WarpInfo(34,[18,19],[15,16],[435,436]),WarpInfo(34,[20,22],[17,19],[438,437]),WarpInfo(34,[23,24],[20,21],[439,440]),WarpInfo(34,[21,25],[18,22],[442,441]),WarpInfo(7,[89,90],[17,21],[32,33]),WarpInfo(7,[152,159],[19,23],[35,34]),WarpInfo(7,[158,151],[20,22],[36,37]),WarpInfo(7,[94,111],[24,26],[40,41]),WarpInfo(7,[298,299],[18,25],[38,39],[-1,23]),WarpInfo(38,[6,7],[19,24],[79,80]),WarpInfo(38,[128,127],[20,21],[81,82]),WarpInfo(38,[152,149],[23,26],[84,83]),WarpInfo(38,[115,177],[25,27],[85,86]),WarpInfo(38,[130,135],[22,28],[87,757],[-1,62]),WarpInfo(20,[88,78],[1,2],[89,88]),WarpInfo(20,[153,154],[3,4],[90,91]),WarpInfo(26,[125,322],[25,26],[141,142]),WarpInfo(26,[321,324],[18,20],[143,144]),WarpInfo(26,[217,323],[19,21],[145,146]),WarpInfo(26,[268,261],[22,23],[147,148]),WarpInfo(26,[238,267],[24,27],[149,150]),WarpInfo(30,[502,503],[25,33],[177,178]),WarpInfo(30,[95,108],[28,30],[172,171]),WarpInfo(30,[102,96],[26,29],[174,173]),WarpInfo(30,[85,86],[31,32],[758,175],[163,-1]),WarpInfo(30,[21,22],[24,27],[169,170]),WarpInfo(48,[54,53],[28,29],[238,237]),WarpInfo(48,[73,74],[30,31],[239,240]),WarpInfo(48,[75,78],[32,37],[241,242]),WarpInfo(48,[79,81],[33,34],[243,244]),WarpInfo(48,[85,86],[35,36],[245,246]),WarpInfo(72,[34,33],[32,34],[284,283]),WarpInfo(72,[55,54],[33,35],[285,286]),WarpInfo(72,[86,87],[37,38],[759,291],[295,-1]),WarpInfo(72,[106,107],[39,40],[287,288]),WarpInfo(72,[181,96],[36,41],[290,289]),WarpInfo(87,[36,34],[24,26],[327,328]),WarpInfo(87,[40,43],[22,28],[329,330]),WarpInfo(87,[44,35],[27,30],[331,332]),WarpInfo(87,[33,41],[29,31],[333,334]),WarpInfo(87,[42,45],[23,25],[336,335]),WarpInfo(112,[24,29],[2,7],[337,338]),WarpInfo(112,[25,28],[3,6],[339,340]),WarpInfo(112,[26,27],[4,5],[341,342])]
script_folder_list={7:'japes',38:'aztec',20:'llama_temple',26:'factory',30:'galleon',48:'fungi',72:'caves',87:'castle',112:'crypt_ddc',34:'isles'}
for pad_pair in warp_info_data:
	for sub_index in range(2):
		pad_id=pad_pair.ids[sub_index];script_lines=[f"EXEC 7 | 125 65535 {pad_id}",'ENDBLOCK']
		with open(f"./assets/Non-Code/instance_scripts/{script_folder_list[pad_pair.map]}/warp{hex(pad_id)[2:]}.script",'w')as script_f:script_f.write(f".data\nid = {f'0x{hex(pad_id)[2:].upper()}'}\n.code\n");script_f.write('\n'.join(script_lines))
def generateDefaultPadPairing(fh):
	'Generate the default pad pairing and write to ROM.';B='big';A=fh;A.seek(33488896)
	for (F,C) in enumerate(warp_info_data):
		for D in range(2):
			exit=C.tied_exits[D];A.write(C.map.to_bytes(1,B));A.write((F*2+(1-D)).to_bytes(1,B));A.write(C.ids[D].to_bytes(2,B));A.write(C.active_flags[D].to_bytes(2,B));E=C.appear_flags[D]
			if E<0:E+=65536
			A.write(E.to_bytes(2,B));A.write(exit.to_bytes(1,B));A.write((0).to_bytes(1,B))