'Get vanilla move data.'
from typing import BinaryIO
special_move_prices=[3,5,7]
gun_price=3
ins_price=3
slam_prices=[5,7]
gun_upg_prices=[5,7]
ammo_belt_prices=[3,5]
ins_upg_prices=[5,7,9]
cranky_0=[1,2,3,240,18,240,19]
cranky_1=[1,240,2,240,18,3,19]
funky=[33,240,49,240,34,50,35]
candy=[240,65,240,66,240,67,68]
move_offset=168
price_offset=54
space_offset=33476640
def writeVanillaMoveData(fh):
	'Write vanilla move data.';A=fh;print('Writing vanilla move data');A.seek(space_offset+price_offset)
	for B in range(5):A.write(bytearray(special_move_prices))
	A.write(bytearray(slam_prices))
	for B in range(5):A.write(bytearray([gun_price]))
	for B in range(5):A.write(bytearray([ins_price]))
	A.write(bytearray(gun_upg_prices));A.write(bytearray(ammo_belt_prices));A.write(bytearray(ins_upg_prices));A.seek(space_offset+move_offset)
	for B in range(2):A.write(bytearray(cranky_0))
	for B in range(3):A.write(bytearray(cranky_1))
	for B in range(5):A.write(bytearray(funky))
	for B in range(5):A.write(bytearray(candy))