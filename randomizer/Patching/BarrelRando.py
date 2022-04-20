'Apply Boss Locations.'
import js
from randomizer.Lists.Minigame import BarrelMetaData,MinigameRequirements
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
def randomize_barrels(spoiler):
	'Randomize barrel locations.';R='new_map';Q='instance_id';I=spoiler;H='barrels';G='containing_map';A='big';S=[12,91]
	if I.settings.bonus_barrel_rando:
		B=[]
		for (J,T) in I.shuffled_barrel_data.items():
			K=int(BarrelMetaData[J].map);L={Q:int(BarrelMetaData[J].barrel_id),R:int(MinigameRequirements[T].map)};M=True
			if len(B)>0:
				for C in B:
					if C[G]==K:C[H].append(L);M=False
			if M:B.append({G:K,H:[L]})
		for N in B:
			U=int(N[G]);D=js.pointer_addresses[9]['entries'][U]['pointing_to'];ROM().seek(D);F=int.from_bytes(ROM().readBytes(4),A);ROM().seek(D+4+F*48);O=int.from_bytes(ROM().readBytes(4),A);ROM().seek(D+4+F*48+4+O*36);V=int.from_bytes(ROM().readBytes(4),A);W=D+4+F*48+4+O*36+4
			for C in range(V):
				E=W+56*C;ROM().seek(E);ROM().seek(E+50);X=int.from_bytes(ROM().readBytes(2),A)
				if X in S:
					ROM().seek(E+52);Y=int.from_bytes(ROM().readBytes(2),A)
					for P in N[H]:
						if int(P[Q])==Y:ROM().seek(E+18);ROM().writeMultipleBytes(P[R],2)