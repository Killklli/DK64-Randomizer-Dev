'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from random import randint
import js
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';N='red';M='purple';L='green';K=True;J='vanilla';I='chunky_colors';H='tiny_colors';G='lanky_colors';F='diddy_colors';E='dk_colors';B='randomized';C=False;D=33476640
	if js.document.getElementById('random_colors').value=='True':js.document.getElementById(E).value=B;js.document.getElementById(F).value=B;js.document.getElementById(G).value=B;js.document.getElementById(H).value=B;js.document.getElementById(I).value=B
	if js.document.getElementById(E).value!=J:
		C=K;A=0
		if js.document.getElementById(E).value==B:A=randint(0,3)
		elif js.document.getElementById(E).value=='blue':A=1
		elif js.document.getElementById(E).value==L:A=2
		elif js.document.getElementById(E).value==M:A=3
		ROM().seek(D+295);ROM().write(A)
	if js.document.getElementById(F).value!=J:
		C=K;A=0
		if js.document.getElementById(F).value==B:A=randint(0,3)
		elif js.document.getElementById(F).value=='dark_blue':A=1
		elif js.document.getElementById(F).value=='yellow':A=2
		elif js.document.getElementById(F).value=='light_blue':A=3
		ROM().seek(D+296);ROM().write(A)
	if js.document.getElementById(G).value!=J:
		C=K;A=0
		if js.document.getElementById(G).value==B:A=randint(0,3)
		elif js.document.getElementById(G).value==L:A=1
		elif js.document.getElementById(G).value==M:A=2
		elif js.document.getElementById(G).value==N:A=3
		ROM().seek(D+297);ROM().write(A)
	if js.document.getElementById(H).value!=J:
		C=K;A=0
		if js.document.getElementById(H).value==B:A=randint(0,3)
		elif js.document.getElementById(H).value==L:A=1
		elif js.document.getElementById(H).value==M:A=2
		elif js.document.getElementById(H).value==N:A=3
		ROM().seek(D+298);ROM().write(A)
	if js.document.getElementById(I).value!=J:
		C=K;A=0
		if js.document.getElementById(I).value==B:A=randint(0,3)
		elif js.document.getElementById(I).value==N:A=1
		elif js.document.getElementById(I).value==M:A=2
		elif js.document.getElementById(I).value==L:A=3
		ROM().seek(D+299);ROM().write(A)
	if C:ROM().seek(D+294);ROM().write(1)