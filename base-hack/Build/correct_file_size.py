'Correct the roms file size.'
with open('rom/dk64-randomizer-base-dev.z64','r+b')as fh:
	length=len(fh.read());to_add=length%16
	if to_add!=0:
		arr=[];to_add=16-to_add
		for x in range(to_add):arr.append(0)
		fh.write(bytearray(arr))