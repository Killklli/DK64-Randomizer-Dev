'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from random import randint
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';J='red';I='purple';H='green';G=True;F='vanilla';C='randomized';A=spoiler;D=False;E=33476640
	if A.settings.random_colors:A.settings.dk_colors=C;A.settings.diddy_colors=C;A.settings.lanky_colors=C;A.settings.tiny_colors=C;A.settings.chunky_colors=C
	if A.settings.dk_colors!=F:
		D=G;B=0
		if A.settings.dk_colors==C:B=randint(0,3)
		elif A.settings.dk_colors=='blue':B=1
		elif A.settings.dk_colors==H:B=2
		elif A.settings.dk_colors==I:B=3
		ROM().seek(E+295);ROM().write(B)
	if A.settings.diddy_colors!=F:
		D=G;B=0
		if A.settings.diddy_colors==C:B=randint(0,3)
		elif A.settings.diddy_colors=='dark_blue':B=1
		elif A.settings.diddy_colors=='yellow':B=2
		elif A.settings.diddy_colors=='light_blue':B=3
		ROM().seek(E+296);ROM().write(B)
	if A.settings.lanky_colors!=F:
		D=G;B=0
		if A.settings.lanky_colors==C:B=randint(0,3)
		elif A.settings.lanky_colors==H:B=1
		elif A.settings.lanky_colors==I:B=2
		elif A.settings.lanky_colors==J:B=3
		ROM().seek(E+297);ROM().write(B)
	if A.settings.tiny_colors!=F:
		D=G;B=0
		if A.settings.tiny_colors==C:B=randint(0,3)
		elif A.settings.tiny_colors==H:B=1
		elif A.settings.tiny_colors==I:B=2
		elif A.settings.tiny_colors==J:B=3
		ROM().seek(E+298);ROM().write(B)
	if A.settings.chunky_colors!=F:
		D=G;B=0
		if A.settings.chunky_colors==C:B=randint(0,3)
		elif A.settings.chunky_colors==J:B=1
		elif A.settings.chunky_colors==I:B=2
		elif A.settings.chunky_colors==H:B=3
		ROM().seek(E+299);ROM().write(B)
	if D:ROM().seek(E+294);ROM().write(1)