'Apply item rando changes.'
import js
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Patching.Patcher import ROM
from randomizer.Spoiler import Spoiler
from randomizer.Enums.Types import Types
from randomizer.Enums.Locations import Locations
from randomizer.Patching.Lib import intf_to_float,float_to_hex
model_two_indexes={Types.Banana:116,Types.Blueprint:[222,224,225,221,223],Types.Coin:[72,655],Types.Key:316,Types.Crown:397,Types.Medal:144,Types.Shop:[91,498,89,499,501,502],Types.TrainingBarrel:502,Types.Shockwave:502,Types.NoItem:0}
model_two_scales={Types.Banana:0.25,Types.Blueprint:2,Types.Coin:0.4,Types.Key:0.17,Types.Crown:0.25,Types.Medal:0.22,Types.Shop:0.8,Types.TrainingBarrel:0.8,Types.Shockwave:0.8,Types.NoItem:0.25}
actor_indexes={Types.Banana:45,Types.Blueprint:[78,75,77,79,76],Types.Key:72,Types.Crown:86,Types.Coin:[151,152],Types.Shop:[157,158,159,160,161,162],Types.TrainingBarrel:162,Types.Shockwave:162,Types.NoItem:153,Types.Medal:154}
def place_randomized_items(spoiler):
	'Place randomized items into ROM.';Y='shared';X='kong';W='id';S='upscale';P=spoiler;O='flag';M='big';L=None;G='obj'
	if P.settings.shuffle_items:
		H=P.settings.rom_data;ROM().seek(H+52);ROM().write(1);d=P.item_assignment;e=[116,222,224,225,221,223,72,655,316,397,144,648];I={};Q=0;T=[]
		for A in d:
			if A.can_have_item:
				if A.is_shop:
					ROM().seek(H+167);ROM().write(1);f=P.settings.move_location_data
					for Z in A.placement_index:
						R=f+4*Z
						if A.new_item is L:
							ROM().seek(R);g=int.from_bytes(ROM().readBytes(4),M)
							if g==3758161919 or Z>=120:ROM().seek(R);ROM().writeMultipleBytes(7<<5,1);ROM().writeMultipleBytes(0,1);ROM().writeMultipleBytes(65535,2)
						elif A.new_flag&32768:
							h=A.new_flag>>12&7;a=A.new_flag>>8&15
							if a==7:b=0
							else:b=(A.new_flag&255)-1
							ROM().seek(R);ROM().writeMultipleBytes(a<<5|b<<3|h,1);ROM().writeMultipleBytes(A.price,1);ROM().writeMultipleBytes(65535,2)
						else:
							N=5
							if A.new_item==Types.Banana:N=6
							ROM().seek(R);ROM().writeMultipleBytes(N<<5,1);ROM().writeMultipleBytes(A.price,1);ROM().writeMultipleBytes(A.new_flag,2)
				elif not A.reward_spot:
					for E in A.placement_data:
						if E not in I:I[E]=[]
						if A.new_item is L:I[E].append({W:A.placement_data[E],G:Types.NoItem,X:0,O:0,S:1,Y:False})
						else:i=model_two_scales[A.new_item];j=model_two_scales[A.old_item];k=i/j;I[E].append({W:A.placement_data[E],G:A.new_item,X:A.new_kong,O:A.new_flag,S:k,Y:A.shared})
					if A.location==Locations.NintendoCoin and A.new_item==Types.Banana:ROM().seek(H+272);ROM().write(1)
					elif A.location==Locations.RarewareCoin and A.new_item==Types.Banana:ROM().seek(H+273);ROM().write(1)
					elif A.location in(Locations.ForestDonkeyBaboonBlast,Locations.CavesDonkeyBaboonBlast):
						if A.new_item is L:B=153
						elif A.new_item==Types.Blueprint:B=actor_indexes[Types.Blueprint][A.new_kong]
						elif A.new_item==Types.Coin:
							B=actor_indexes[Types.Coin][0]
							if A.new_flag==379:B=actor_indexes[Types.Coin][1]
						elif A.new_item in(Types.Shop,Types.Shockwave,Types.TrainingBarrel):
							if A.new_flag&32768==0:C=5
							else:
								C=A.new_flag>>12&7
								if A.shared or C>5:C=5
							B=actor_indexes[Types.Shop][C]
						else:B=actor_indexes[A.new_item]
						ROM().seek(33493504+4*Q);ROM().writeMultipleBytes(A.old_flag,2);ROM().writeMultipleBytes(B,1);Q+=1
				else:
					if A.old_item!=Types.Medal:
						if A.new_item is L:B=153
						elif A.new_item==Types.Blueprint:B=actor_indexes[Types.Blueprint][A.new_kong]
						elif A.new_item==Types.Coin:
							B=actor_indexes[Types.Coin][0]
							if A.new_flag==379:B=actor_indexes[Types.Coin][1]
						elif A.new_item in(Types.Shop,Types.Shockwave,Types.TrainingBarrel):
							if A.new_flag&32768==0:C=5
							else:
								C=A.new_flag>>12&7
								if A.shared or C>5:C=5
							B=actor_indexes[Types.Shop][C]
						else:B=actor_indexes[A.new_item]
					if A.old_item==Types.Blueprint:U=A.old_flag-469;ROM().seek(33492992+U);ROM().write(B)
					elif A.old_item==Types.Crown:l=[609,610,611,612,613,616,617,614,618,615];ROM().seek(33493184+l.index(A.old_flag));ROM().write(B)
					elif A.old_item==Types.Key:m=[26,74,138,168,236,292,317,380];ROM().seek(33493200+m.index(A.old_flag));ROM().write(B)
					elif A.old_item==Types.Medal:
						n=[Types.Banana,Types.Blueprint,Types.Key,Types.Crown,Types.Coin,Types.Medal,Types.Shop,Types.Shop,Types.Shop,Types.TrainingBarrel,Types.Shockwave,L];U=A.old_flag-549;ROM().seek(33493120+U)
						if A.new_item==Types.Shop:
							J=6
							if A.new_flag in(656,657):J=6
							elif A.new_flag in(658,659):J=7
							elif A.new_flag in(660,661,662):J=8
							else:
								N=A.new_flag>>8&15
								if N==4:J=8
								elif N in(2,3):J=7
							ROM().write(J)
						else:ROM().write(n.index(A.new_item))
					elif A.location==Locations.JapesChunkyBoulder:ROM().seek(H+276);ROM().write(B)
					elif A.location==Locations.AztecLankyVulture:ROM().seek(H+277);ROM().write(B)
					elif A.old_item==Types.Banana:ROM().seek(33493504+4*Q);ROM().writeMultipleBytes(A.old_flag,2);ROM().writeMultipleBytes(B,1);Q+=1
			if not A.is_shop and A.can_have_item:
				V=[A.old_flag]
				if A.new_item is L:V.append(0)
				else:V.append(A.new_flag)
				T.append(V)
		T.append([65535,65535]);ROM().seek(33497088)
		for o in sorted(T,key=lambda x:x[0]):
			for p in o:ROM().writeMultipleBytes(p,2)
		for E in I:
			c=js.pointer_addresses[9]['entries'][E]['pointing_to'];ROM().seek(c);q=int.from_bytes(ROM().readBytes(4),M)
			for A in range(q):
				F=c+4+A*48;ROM().seek(F+42);r=int.from_bytes(ROM().readBytes(2),M)
				for D in I[E]:
					if D[W]==r:
						ROM().seek(F+40);s=int.from_bytes(ROM().readBytes(2),M)
						if s in e:
							ROM().seek(F+40);K=0
							if D[G]==Types.Blueprint:K=model_two_indexes[Types.Blueprint][D[X]]
							elif D[G]==Types.Coin:
								K=model_two_indexes[Types.Coin][0]
								if D[O]==379:K=model_two_indexes[Types.Coin][1]
							elif D[G]==Types.Shop:
								if D[O]&32768==0:C=5
								else:
									C=D[O]>>12&7
									if D[Y]or C>5:C=5
								K=model_two_indexes[Types.Shop][C]
							else:K=model_two_indexes[D[G]]
							ROM().writeMultipleBytes(K,2);ROM().seek(F+12);t=intf_to_float(int.from_bytes(ROM().readBytes(4),M));u=t*D[S];ROM().seek(F+12);ROM().writeMultipleBytes(int(float_to_hex(u),16),4)
							if D[G]==Types.Blueprint:ROM().seek(F+4);v=intf_to_float(int.from_bytes(ROM().readBytes(4),M));w=v+D[S]*1.25;ROM().seek(F+4);ROM().writeMultipleBytes(int(float_to_hex(w),16),4)