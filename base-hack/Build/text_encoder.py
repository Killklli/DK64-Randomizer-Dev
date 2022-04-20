'Encode text file to ROM.'
def writeText(file_name,text):
	'Write the text to ROM.';F='big';D=text
	with open(file_name,'wb')as A:
		A.write(bytearray([len(D)]));E=0
		for B in D:
			A.write(bytearray([1,1,len(B)]))
			for C in B:A.write(E.to_bytes(4,F));A.write(len(C).to_bytes(2,F));A.write(bytearray([0,0]));E+=len(C)
			A.write(bytearray([0,0,0,0]))
		A.write(bytearray(E.to_bytes(2,F)))
		for B in D:
			for C in B:A.write(C.encode('ascii'))