'Convert 63x63 Portal image into 4 32x32 segments.'
import os
from PIL import Image
def convertPortalImage(image_name):
	'Split image into 4 segments for the portal.';D=image_name;C=Image.open(D);C=C.transpose(Image.FLIP_TOP_BOTTOM);N=C.load();A={'NW':[[0,0],[32,32]],'SW':[[0,31],[32,63]],'SE':[[31,31],[63,63]],'NE':[[31,0],[63,32]]};E=[]
	for B in A.keys():
		F=A[B][0][0];O=A[B][1][0];G=O-F;H=A[B][0][1];P=A[B][1][1];I=P-H;J=Image.new('RGBA',size=(G,I));Q=J.load()
		for K in range(G):
			R=F+K
			for L in range(I):S=H+L;T=N[(R,S)];Q[(K,L)]=T
		M=D.replace('.png',f"_{B}.png");E.append(M);J.save(M)
	return E