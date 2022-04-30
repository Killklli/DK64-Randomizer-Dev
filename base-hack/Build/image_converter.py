'Convert PNG to RGBA32 binary.'
from PIL import Image
def convertToRGBA32(png_file):
	'Convert PNG to RGBA32 binary.';D=png_file;B='big';C=Image.open(D);E,F=C.size;N=C.load();G=D.replace('.png','.rgba32')
	with open(G,'wb')as A:
		for H in range(F):
			for I in range(E):J,K,L,M=C.getpixel((I,H));A.write((J&255).to_bytes(1,B));A.write((K&255).to_bytes(1,B));A.write((L&255).to_bytes(1,B));A.write((M&255).to_bytes(1,B))