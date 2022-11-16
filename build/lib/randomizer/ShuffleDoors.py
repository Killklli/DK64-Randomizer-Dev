'Shuffle Wrinkly and T&S Doors based on settings.'
import random
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.DoorLocations import door_locations
level_list=['Jungle Japes','Angry Aztec','Frantic Factory','Gloomy Galleon','Fungi Forest','Crystal Caves','Creepy Castle','Hideout Helm']
def ShuffleDoors(spoiler):
	'Shuffle Wrinkly and T&S Doors based on settings.';W=' T&S #';V='remove_wrinkly_puzzles';Q='none';O=True;N='tns';J='wrinkly';B=spoiler;K={};L={}
	for A in level_list:K[A]={};L[A]={}
	G={}
	for A in door_locations:
		for E in door_locations[A]:
			E.placed=E.default_placed
			if B.settings.wrinkly_location_rando:
				if E.placed==J:E.placed=Q
			if B.settings.tns_location_rando:
				if E.placed==N:E.placed=Q
	for A in door_locations:
		G[A]=[];C=[]
		for (R,E) in enumerate(door_locations[A]):
			if E.placed==Q and(B.settings.wrinkly_location_rando or B.settings.tns_location_rando):C.append(R)
			elif(V in B.settings.misc_changes_selected or len(B.settings.misc_changes_selected)==0)and E.default_placed==J:C.append(R)
		random.shuffle(C)
		if B.settings.wrinkly_location_rando:
			for M in range(5):
				H=Kongs(M%5)
				if len(C)>0:
					D=C.pop(0)
					while H not in door_locations[A][D].kongs or door_locations[A][D].door_type==N:C.append(D);D=C.pop(0)
					I=door_locations[A][D];I.assignDoor(H);K[level_list[A]][str(Kongs(M%5).name).capitalize()]=I.name;G[A].append((D,J,M%5))
		elif V in B.settings.misc_changes_selected or len(B.settings.misc_changes_selected)==0:
			S=[B for B in C if door_locations[A][B].default_placed==J]
			for M in range(5):
				if len(S)>0:D=S.pop();I=door_locations[A][D];H=I.default_kong;I.assignDoor(H);K[level_list[A]][str(H).capitalize()]=I.name;G[A].append((D,J,int(H)))
		if B.settings.tns_location_rando:
			T=random.choice([3,4,5]);U=False;C=[B for B in C if door_locations[A][B].door_type!=J]
			for P in range(T):
				if len(C)>0:
					if P<T-1 or U is O:
						D=C.pop();F=door_locations[A][D]
						if F.moveless is O:U=O
						C=[B for B in C if door_locations[A][B].group!=F.group];F.assignPortal();L[level_list[A]][W+str(P+1)]=F.name;G[A].append((D,N))
					else:D=random.choice([B for B in C if door_locations[A][B].moveless is O]);F=door_locations[A][D];F.assignPortal();L[level_list[A]][W+str(P+1)]=F.name;G[A].append((D,N))
	B.shuffled_door_data=G
	if B.settings.wrinkly_location_rando:B.human_hint_doors=K
	if B.settings.tns_location_rando:B.human_portal_doors=L