'Shuffle Wrinkly and T&S Doors based on settings.'
import random
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.DoorLocations import door_locations
level_list=['Jungle Japes','Angry Aztec','Frantic Factory','Gloomy Galleon','Fungi Forest','Crystal Caves','Creepy Castle','Hideout Helm']
def ShuffleDoors(spoiler):
	'Shuffle Wrinkly and T&S Doors based on settings.';V=' T&S #';U='remove_wrinkly_puzzles';Q='none';O=True;N='tns';J='wrinkly';C=spoiler;K={};L={}
	for A in level_list:K[A]={};L[A]={}
	H={}
	for A in door_locations:
		for E in door_locations[A]:
			E.placed=E.default_placed
			if C.settings.wrinkly_location_rando:
				if E.placed==J:E.placed=Q
			if C.settings.tns_location_rando:
				if E.placed==N:E.placed=Q
	for A in door_locations:
		H[A]=[];B=[]
		for (R,E) in enumerate(door_locations[A]):
			if E.placed==Q and(C.settings.wrinkly_location_rando or C.settings.tns_location_rando):B.append(R)
			elif(U in C.settings.misc_changes_selected or len(C.settings.misc_changes_selected)==0)and E.default_placed==J:B.append(R)
		random.shuffle(B)
		if C.settings.wrinkly_location_rando:
			for M in range(5):
				I=Kongs(M%5)
				if len(B)>0:
					D=B.pop(0)
					while I not in door_locations[A][D].kongs or door_locations[A][D].door_type==N:B.append(D);D=B.pop(0)
					F=door_locations[A][D];F.assignDoor(I);K[level_list[A]][str(Kongs(M%5).name).capitalize()]=F.name;H[A].append((D,J,M%5))
		elif U in C.settings.misc_changes_selected or len(C.settings.misc_changes_selected)==0:
			for M in range(5):
				if len(B)>0:
					D=B.pop();F=door_locations[A][D]
					if F.default_placed==J:I=F.default_kong;F.assignDoor(I);K[level_list[A]][str(I).capitalize()]=F.name;H[A].append((D,J,int(I)))
		if C.settings.tns_location_rando:
			S=random.choice([3,4,5]);T=False;B=[C for C in B if door_locations[A][C].door_type!=J]
			for P in range(S):
				if len(B)>0:
					if P<S-1 or T is O:
						D=B.pop();G=door_locations[A][D]
						if G.moveless is O:T=O
						B=[C for C in B if door_locations[A][C].group!=G.group];G.assignPortal();L[level_list[A]][V+str(P+1)]=G.name;H[A].append((D,N))
					else:D=random.choice([C for C in B if door_locations[A][C].moveless is O]);G=door_locations[A][D];G.assignPortal();L[level_list[A]][V+str(P+1)]=G.name;H[A].append((D,N))
	C.shuffled_door_data=H
	if C.settings.wrinkly_location_rando:C.human_hint_doors=K
	if C.settings.tns_location_rando:C.human_portal_doors=L