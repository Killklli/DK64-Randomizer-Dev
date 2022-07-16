'Adjust exits to prevent logical problems with LZR.'
_F='exits'
_E='containing_map'
_D='z'
_C='y'
_B='x'
_A='exit_index'
from typing import BinaryIO
pointer_table_address=1055824
pointer_table_index=23
new_caves_portal_coords=[120.997,50,1182.974]
exit_adjustments=[{_E:48,_F:[{_A:3,_B:3429,_C:462,_D:4494},{_A:6,_B:4153,_C:163,_D:3721},{_A:4,_B:3982,_C:115,_D:2026},{_A:5,_B:4550,_C:162,_D:3646}]},{_E:30,_F:[{_A:10,_B:1524,_C:1754,_D:3964},{_A:19,_B:3380,_C:1640,_D:120}]},{_E:112,_F:[{_A:1,_B:1515,_C:80,_D:2506}]},{_E:34,_F:[{_A:3,_B:3464,_C:1040,_D:1716}]},{_E:26,_F:[{_A:8,_B:814,_C:8,_D:1334}]},{_E:87,_F:[{_A:15,_B:1293,_C:472,_D:238},{_A:11,_B:1808,_C:1406,_D:1270}]},{_E:72,_F:[{_A:11,_B:int(new_caves_portal_coords[0]-25),_C:int(new_caves_portal_coords[1]),_D:int(new_caves_portal_coords[2]-12)}]}]
def adjustExits(fh):
	'Write new exits.';B='big';A=fh;print('Adjusting Exits');A.seek(pointer_table_address+4*pointer_table_index);E=pointer_table_address+int.from_bytes(A.read(4),B)
	for D in exit_adjustments:
		F=D[_E];A.seek(E+4*F);C=int.from_bytes(A.read(4),B)+pointer_table_address
		for exit in D[_F]:A.seek(C+exit[_A]*10+0);A.write(exit[_B].to_bytes(2,B));A.seek(C+exit[_A]*10+2);A.write(exit[_C].to_bytes(2,B));A.seek(C+exit[_A]*10+4);A.write(exit[_D].to_bytes(2,B))