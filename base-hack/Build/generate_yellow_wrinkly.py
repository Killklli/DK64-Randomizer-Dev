'File to modify Chunky Wrinkly door to a yellow one to place inside the DK Wrinkly slot.'
import os,shutil,zlib
new_file='assets/Non-Code/Gong/hint_door.bin'
def generateYellowWrinkly():
	'Pull geo file from ROM and modify.';D='big';E=1055824
	with open('rom/dk64.z64','rb')as B:
		B.seek(E+4*4);G=E+int.from_bytes(B.read(4),D);B.seek(G+4*241);H=E+int.from_bytes(B.read(4),D);B.seek(G+4*241+4);I=E+int.from_bytes(B.read(4),D);J=I-H;B.seek(H);K=zlib.decompress(B.read(J),15+32)
		with open(new_file,'wb')as L:L.write(K)
	with open(new_file,'r+b')as A:
		for F in range(int((3072-1536)/16)):
			A.seek(1548+16*F);C=[]
			for O in range(3):C.append(int.from_bytes(A.read(1),D))
			if C[0]==110 and C[1]==228 and C[2]==48:A.seek(1548+16*F);A.write(bytearray([255,255,0]))
			elif C[0]==62 and C[1]==130 and C[2]==26:A.seek(1548+16*F);A.write(bytearray([145,145,0]))
		M=583;N=590;A.seek(4906);A.write(M.to_bytes(2,D));A.seek(5038);A.write(N.to_bytes(2,D))