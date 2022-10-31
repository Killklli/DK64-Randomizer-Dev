'Randomize Price Locations.'
from randomizer.Enums.Items import Items
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_prices(spoiler):
	'Write prices to ROM variable space based on settings.';F='vanilla';A=spoiler
	if A.settings.random_prices!=F or A.settings.move_rando!='starts_with':
		C=A.settings.rom_data;ROM().seek(C+53)
		if A.settings.random_prices!=F:ROM().write(1)
		else:ROM().write(0)
		D={Items.ProgressiveAmmoBelt:2,Items.ProgressiveInstrumentUpgrade:3,Items.ProgressiveSlam:2}
		for B in D:
			if B not in A.settings.prices:A.settings.prices[B]=[]
			E=D[B]
			if len(A.settings.prices[B])<E:
				G=E-len(A.settings.prices[B])
				for H in range(G):A.settings.prices[B].append(0)
		ROM().seek(C+69);ROM().write(A.settings.prices[Items.ProgressiveSlam][0]);ROM().write(A.settings.prices[Items.ProgressiveSlam][1]);ROM().seek(C+83);ROM().write(A.settings.prices[Items.ProgressiveAmmoBelt][0]);ROM().write(A.settings.prices[Items.ProgressiveAmmoBelt][1]);ROM().write(A.settings.prices[Items.ProgressiveInstrumentUpgrade][0]);ROM().write(A.settings.prices[Items.ProgressiveInstrumentUpgrade][1]);ROM().write(A.settings.prices[Items.ProgressiveInstrumentUpgrade][2])