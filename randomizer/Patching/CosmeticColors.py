'Apply cosmetic skins to kongs.'
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def apply_cosmetic_colors(spoiler):
	'Apply cosmetic skins to kongs.';I='red';H='purple';G='green';F=True;E='vanilla';B=spoiler;C=False;D=33476640
	if B.settings.dk_colors!=E:
		C=F;A=0
		if B.settings.dk_colors=='blue':A=1
		elif B.settings.dk_colors==G:A=2
		elif B.settings.dk_colors==H:A=3
		ROM().seek(D+295);ROM().write(A)
	if B.settings.diddy_colors!=E:
		C=F;A=0
		if B.settings.diddy_colors=='dark_blue':A=1
		elif B.settings.diddy_colors=='yellow':A=2
		elif B.settings.diddy_colors=='light_blue':A=3
		ROM().seek(D+296);ROM().write(A)
	if B.settings.lanky_colors!=E:
		C=F;A=0
		if B.settings.lanky_colors==G:A=1
		elif B.settings.lanky_colors==H:A=2
		elif B.settings.lanky_colors==I:A=3
		ROM().seek(D+297);ROM().write(A)
	if B.settings.tiny_colors!=E:
		C=F;A=0
		if B.settings.tiny_colors==G:A=1
		elif B.settings.tiny_colors==H:A=2
		elif B.settings.tiny_colors==I:A=3
		ROM().seek(D+298);ROM().write(A)
	if B.settings.chunky_colors!=E:
		C=F;A=0
		if B.settings.tiny_colors==I:A=1
		elif B.settings.tiny_colors==H:A=2
		elif B.settings.tiny_colors==G:A=3
		ROM().seek(D+299);ROM().write(A)
	if C:ROM().seek(D+294);ROM().write(1)