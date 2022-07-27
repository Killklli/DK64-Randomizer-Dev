"ROM TESTER.\n\nDisplays all values in the variable space in an easier-to-read format rather than a hex editor\n***PURELY*** for debugging purposes\nTo use:\n    - Place your modified Rando ROM in /rom_tester\n    - Run this script\n    - This script will spit out details for ALL .z64 files in /rom_tester, so if you only want data for a specific rom, make sure that's the only one in /rom_tester\n"
_G='Castle'
_F='Galleon'
_E='Fungi'
_D='Factory'
_C='Japes'
_B='map'
_A='name'
import os
from typing import BinaryIO
levels_isles=[_C,'Aztec',_D,_F,_E,'Caves',_G,'Isles']
levels=[_C,'Aztec',_D,_F,_E,'Caves',_G,'Helm']
keys=[26,74,138,168,236,292,317]
special_moves=['Baboon Blast','Strong Kong','Gorilla Grab','Chimpy Charge','Rocketbarrel','Simian Spring','Orangstand','Baboon Balloon','Orangstand Sprint','Mini Monkey','Pony Tail Twirl','Monkeyport','Hunky Chunky','Primate Punch','Gorilla Gone','Super Simian Slam','Super Duper Simian Slam','Coconut Gun','Peanut Popguns','Grape Shooter','Feather Bow','Pineapple Launcher','Bongo Blast','Guitar Gazump','Trombone Tremor','Saxaphone Slam','Triangle Trample','Homing Ammo','Sniper Scope','Ammo Belt 1','Ammo Belt 2','Instrument Upgrade 1','3rd Melon','Instrument Upgrade 2']
kongs=['DK','Diddy','Lanky','Tiny','Chunky','Krusha','Rambi','Enguarde']
shops=['Cranky','Funky','Candy']
bosses=[{_A:'Army Dillo 1',_B:8},{_A:'Dogadon 1',_B:197},{_A:'Mad Jack',_B:154},{_A:'Pufftoss',_B:111},{_A:'Dogadon 2',_B:83},{_A:'Army Dillo 2',_B:196},{_A:'King Kut Out',_B:199}]
move_types=['Special Move','Slam','Gun','Ammo Belt','Instrument']
key_goals=['Angry Aztec','Factory & Galleon','K. Rool Part 1',_E,'Caves & Castle','Helm Part 1','Helm Part 2']
def getValue(fh,offset,size):'Get the value of the object.';fh.seek(33476640+offset);return int.from_bytes(fh.read(size),'big')
def getTrueFalse(fh,offset,size):
	'Get if the value is true or false.';A=getValue(fh,offset,size)
	if A!=0:return True
	return False
def getMapExit(fh,offset):'Get the current map exit.';A=offset;B=getValue(fh,A,1);C=getValue(fh,A+1,1);return f"Map {B}, Exit {C}"
def getKong(fh,offset):
	'Get the current kong.';A=getValue(fh,offset,1)
	if A>=0:
		if A<8:return kongs[A]
	return f"Kong {hex(A)}"
def getMove(fh,offset):
	'Get the current move.';A=getValue(fh,offset,1);B=A>>5&7;C=(A>>3&3)+1;D=A&7
	if B==5:return'No Upgrade'
	return f"{move_types[B]} level {str(C)} (Kong {D})"
output_file='output.txt'
if os.path.exists(output_file):os.remove(output_file)
with open(output_file,'w')as fh:print('Created File')
def output(string):
	'Write the output.'
	with open(output_file,'a')as A:A.write(string+'\n')
files=[A for A in os.listdir('.')if os.path.isfile(A)]
for f in files:
	if'.z64'in f:
		output(f"Analyzing {f}")
		with open(f,'rb')as fh:
			output(f"\tLevel Order Rando: {str(getTrueFalse(fh,0,1))}");output(f"\tLevel Order:")
			for x in range(7):idx_val=getValue(fh,1+x,1);output(f"\t\t[{x}] - {levels[idx_val]} ({idx_val})")
			output(f"\tTroff 'n' Scoff Count:")
			for x in range(7):output(f"\t\t{levels[x]}: {getValue(fh,8+2*x,2)}")
			output(f"\tB. Locker Requirement:")
			for x in range(8):output(f"\t\t{levels[x]} Lobby: {getValue(fh,22+x,1)}")
			output(f"\tKey Flags:")
			for x in range(7):
				key_str='';flag_val=getValue(fh,30+2*x,2)
				if flag_val in keys:key_str=f" (Key {keys.index(flag_val)+1})"
				output(f"\t\tOpens {key_goals[x]}: {hex(flag_val)}{key_str}")
			output(f"\tUnlock Kongs: {str(getTrueFalse(fh,44,1))}");output(f"\tUnlock Moves: {str(getTrueFalse(fh,45,1))}");output(f"\tFast Start (Beginning): {str(getTrueFalse(fh,46,1))}");output(f"\tCamera Unlocked: {str(getTrueFalse(fh,47,1))}");output(f"\tTag Anywhere: {str(getTrueFalse(fh,48,1))}");output(f"\tFast Start (Helm): {str(getTrueFalse(fh,49,1))}");output(f"\tCrown Door Open: {str(getTrueFalse(fh,50,1))}");output(f"\tCoin Door Open: {str(getTrueFalse(fh,51,1))}");output(f"\tQuality of Life changes: {str(getTrueFalse(fh,52,1))}");output(f"\tPrice Rando On: {str(getTrueFalse(fh,53,1))}")
			for x in range(34):output(f"\t\t{special_moves[x]}: {getValue(fh,54+x,1)}")
			output(f"\tK Rool Order:")
			for x in range(5):output(f"\t\t[{x}] - {getKong(fh,88+x)} Phase")
			output(f"\tRandomize More Loading Zones: {str(getTrueFalse(fh,93,1))}");output(f"\t\tAztec Beetle Enter: {getMapExit(fh,94)}");output(f"\t\tAztec Beetle Exit: {getMapExit(fh,96)}");output(f"\t\tCaves Beetle Exit: {getMapExit(fh,98)}");output(f"\t\tSeal Race Exit: {getMapExit(fh,100)}");output(f"\t\tFactory Car Exit: {getMapExit(fh,102)}");output(f"\t\tCastle Car Exit: {getMapExit(fh,104)}");output(f"\t\tSeasick Ship Enter: {getMapExit(fh,106)}");output(f"\t\tFungi Minecart Enter: {getMapExit(fh,108)}");output(f"\t\tFungi Minecart Exit: {getMapExit(fh,110)}");output(f"\t\tJapes Minecart Exit: {getMapExit(fh,112)}");output(f"\t\tCastle Minecart Exit: {getMapExit(fh,114)}");output(f"\t\tCastle Lobby Entrance: {getMapExit(fh,116)}");output(f"\t\tK. Rool Exit: {getMapExit(fh,118)}");output(f"\t\tBallroom to Museum (Monkeyport): {getMapExit(fh,304)}");output(f"\t\tMuseum to Ballroom (Monkeyport): {getMapExit(fh,306)}")
			for x in range(8):output(f"\t\t{levels[x]} Exit: {getMapExit(fh,120+2*x)}")
			for x in range(7):output(f"\t\t{levels[x]} Entrance: {getMapExit(fh,136+2*x)}")
			output(f"\tFPS Display On: {str(getTrueFalse(fh,150,1))}");output(f"\tBoss Kongs:")
			for x in range(7):output(f"\t\t{levels[x]} Boss: {getKong(fh,151+x)}")
			output(f"\tBoss Locations:")
			for x in range(7):
				boss_val=getValue(fh,158+x,1);boss_str=hex(boss_val)
				for y in bosses:
					if y[_B]==boss_val:boss_str=y[_A]
				output(f"\t\t{levels[x]} Boss: {boss_str}")
			output(f"\tDamage Multiplier: {getValue(fh,165,1)}");output(f"\tNo Health Refills: {str(getTrueFalse(fh,166,1))}");output(f"\tMove Rando On: {str(getTrueFalse(fh,167,1))}")
			for shop in range(3):
				for kong in range(5):
					for level in range(8):output(f"\t\t{kongs[kong]} {shops[shop]} {levels_isles[level]}: {getMove(fh,168+level+8*kong+40*shop)}")
			output(f"\tKut Out Kong Order:")
			for x in range(5):output(f"\t\t[{x}] - {getKong(fh,288+x)}")
			output(f"\tRemove B. Lockers:")
			for x in range(8):output(f"\t\t{levels[x]} Lobby: {str(getValue(fh,293,1)>>x&1!=0)}")
			output(f"\tRemove Minigame Barrels:");output(f"\t\tBonus Barrels: {str(getValue(fh,294,1)&1!=0)}");output(f"\t\tHelm Barrels: {str(getValue(fh,294,1)&2!=0)}");output(f"\tKeys Pre-Turned:")
			for x in range(8):output(f"\t\tKey {x+1}: {str(getValue(fh,295,1)>>x&1!=0)}")
			output(f"\tDisable Drops: {str(getTrueFalse(fh,296,1))}");output(f"\tHash:")
			for x in range(5):output(f"\t\t[{x}] - {str(getValue(fh,297+x,1))}")
			output(f"\tMusic Rando On: {str(getTrueFalse(fh,302,1))}");output(f"\tShop Indicator On: {str(getTrueFalse(fh,308,1))}");output(f"\tWarp to Isles Enabled: {str(getTrueFalse(fh,309,1))}");klap_model=getValue(fh,310,1)
			if klap_model==0:klap_model==33
			output(f"\tKlaptrap Model: {hex(klap_model)}");output(f"\tOpen Levels: {str(getTrueFalse(fh,311,1))}");output(f"\tActivate All Warps: {str(getTrueFalse(fh,312,1))}");output(f"\tD-Pad Visual Showed: {str(getTrueFalse(fh,313,1))}");output(f"\tFast Warps: {str(getTrueFalse(fh,314,1))}");output(f"\tShort Bosses: {str(getTrueFalse(fh,315,1))}");output(f"\tCoin Requirements")
			for (x_i,x) in enumerate(['Caves Beetle Race','Aztec Beetle Race','Factory Car Race','Seal Race','Castle Car Race','Japes Minecart','Fungi Minecart','Castle Minecart']):output(f"\t\t{x}: {str(getValue(fh,316+x_i,1))}")
			output(f"\tShop Hints: {str(getTrueFalse(fh,331,1))}");output(f"\tLobbies Auto-opened:")
			for x in range(8):output(f"\t\t{levels[x]} Lobby Entrance: {str(getValue(fh,332,1)>>x&1!=0)}")
			output(f"\tPerma-Lose Kongs: {str(getTrueFalse(fh,333,1))}");output(f"\tDisable Boss Kong Check: {str(getTrueFalse(fh,334,1))}");output(f"\tPrevent Tag Spawn: {str(getTrueFalse(fh,335,1))}");jetpac_req=getValue(fh,336,1)
			if jetpac_req==0:output(f"\tJetpac Requirement: Vanilla")
			else:output(f"\tJetpac Requirement: {jetpac_req} Medals")
			output(f"\tStarting Kong: {str(getTrueFalse(fh,337,1))}");output(f"\tLocked Kongs:")
			for (x_i,x) in enumerate([_C,'Llama Temple','Dome Temple',_D]):
				for (y_i,y) in enumerate(['Locked','Puzzle Solver']):output(f"\t\t{x} ({y}): {getKong(fh,338+x_i*2+y_i)}")
			versions=['Live','Dev Site','Localhost'];output(f"\tVersion: {versions[getValue(fh,346,1)]}");output(f"\tAuto-Keys: {str(getTrueFalse(fh,347,1))}");output(f"\tMatching Game Sounds:")
			for x in range(8):output(f"\t\tSound {x+1}: {getValue(fh,348+2*x,2)}")
			piano_keys=['A','B','C','D','E','F'];piano_str=''
			for x in range(7):
				if x>0:piano_str+=f", {piano_keys[getValue(fh,364+x,1)]}"
				else:piano_str+=piano_keys[getValue(fh,364+x,1)]
			output(f"\tPiano Game Order: {piano_str}");output(f"\tRemove High Requirements: {str(getTrueFalse(fh,377,1))}");output(f"\tFast GBs: {str(getTrueFalse(fh,378,1))}")