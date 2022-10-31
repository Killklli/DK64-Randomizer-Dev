'Shuffle Wrinkly and T&S Doors based on settings.'
import random
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Lists.DoorLocations import door_locations
level_list=['Jungle Japes','Angry Aztec','Frantic Factory','Gloomy Galleon','Fungi Forest','Crystal Caves','Creepy Castle','Hideout Helm']
def ShuffleDoors(spoiler):
	'Shuffle Wrinkly and T&S Doors based on settings.';T=' T&S #';O='none';N='wrinkly';J=True;I='tns';D=spoiler;K={};H={}
	for A in level_list:K[A]={};H[A]={}
	G={}
	for A in door_locations:
		for E in door_locations[A]:
			E.placed=E.default_placed
			if D.settings.wrinkly_location_rando:
				if E.placed==N:E.placed=O
			if D.settings.tns_location_rando:
				if E.placed==I:E.placed=O
	for A in door_locations:
		G[A]=[];B=[]
		for (U,E) in enumerate(door_locations[A]):
			if E.placed==O:B.append(U)
		random.shuffle(B)
		if D.settings.wrinkly_location_rando:
			for L in range(5):
				P=Kongs(L%5)
				if len(B)>0:
					C=B.pop(0)
					while P not in door_locations[A][C].kongs or door_locations[A][C].door_type==I:B.append(C);C=B.pop(0)
					Q=door_locations[A][C];Q.assignDoor(P);K[level_list[A]][str(Kongs(L%5).name).capitalize()]=Q.name;G[A].append((C,N,L%5))
		if D.settings.tns_location_rando:
			R=random.choice([3,4,5]);S=False;B=[C for C in B if door_locations[A][C].door_type!=N]
			for M in range(R):
				if len(B)>0:
					if M<R-1 or S is J:
						C=B.pop();F=door_locations[A][C]
						if F.moveless is J:S=J
						B=[C for C in B if door_locations[A][C].group!=F.group];F.assignPortal();H[level_list[A]][T+str(M+1)]=F.name;G[A].append((C,I))
					else:C=random.choice([C for C in B if door_locations[A][C].moveless is J]);F=door_locations[A][C];F.assignPortal();H[level_list[A]][T+str(M+1)]=F.name;G[A].append((C,I))
	D.shuffled_door_data=G
	if D.settings.wrinkly_location_rando:D.human_hint_doors=K
	if D.settings.tns_location_rando:D.human_portal_doors=H