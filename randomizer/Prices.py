'Functions and data for setting and calculating prices.'
_A=None
import random
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Locations import Locations
from randomizer.ItemPool import ChunkyMoveLocations,DiddyMoveLocations,DonkeyMoveLocations,LankyMoveLocations,TinyMoveLocations
from randomizer.ItemPool import DonkeyMoves,DiddyMoves,LankyMoves,TinyMoves,ChunkyMoves
from randomizer.Lists.Location import LocationList
VanillaPrices={Items.BaboonBlast:3,Items.StrongKong:5,Items.GorillaGrab:7,Items.ChimpyCharge:3,Items.RocketbarrelBoost:5,Items.SimianSpring:7,Items.Orangstand:3,Items.BaboonBalloon:5,Items.OrangstandSprint:7,Items.MiniMonkey:3,Items.PonyTailTwirl:5,Items.Monkeyport:7,Items.HunkyChunky:3,Items.PrimatePunch:5,Items.GorillaGone:7,Items.Coconut:3,Items.Peanut:3,Items.Grape:3,Items.Feather:3,Items.Pineapple:3,Items.HomingAmmo:5,Items.SniperSight:7,Items.Bongos:3,Items.Guitar:3,Items.Trombone:3,Items.Saxophone:3,Items.Triangle:3,Items.ProgressiveSlam:[5,7],Items.ProgressiveAmmoBelt:[3,5],Items.ProgressiveInstrumentUpgrade:[5,7,9]}
ProgressiveMoves={Items.ProgressiveSlam:2,Items.ProgressiveAmmoBelt:2,Items.ProgressiveInstrumentUpgrade:3}
def RandomizePrices(weight):
	'Generate randomized prices based on given weight (free, low, medium, or high).';C=weight;A=VanillaPrices.copy();D=4.5;E=2;F=9
	if C=='high':D=6.5;E=3;F=12
	elif C=='low':D=2.5;E=1;F=6
	for B in A.keys():
		if B in ProgressiveMoves.keys():
			A[B]=[]
			for G in range(ProgressiveMoves[B]):A[B].append(GenerateRandomPrice(C,D,E,F))
		else:A[B]=GenerateRandomPrice(C,D,E,F)
	return A
def GenerateRandomPrice(weight,avg,stddev,upperLimit):
	'Generate a random price to assign.';B=upperLimit;C=1
	if weight=='free':A=0
	else:
		A=round(random.normalvariate(avg,stddev))
		if A<C:A=C
		elif A>B:A=B
	return A
def GetMaxForKong(settings,kong):
	'Get the maximum amount of coins the given kong can spend.';C=kong;B=settings;A=sum([C for(A,C)in B.prices.items()if A in[Items.HomingAmmo,Items.SniperSight]])
	for D in ProgressiveMoves.keys():
		for E in range(ProgressiveMoves[D]):A+=B.prices[D][E]
	if C==Kongs.donkey:A+=sum([C for(A,C)in B.prices.items()if A in DonkeyMoves]);A+=2
	elif C==Kongs.diddy:A+=sum([C for(A,C)in B.prices.items()if A in DiddyMoves])
	elif C==Kongs.lanky:A+=sum([C for(A,C)in B.prices.items()if A in LankyMoves])
	elif C==Kongs.tiny:A+=sum([C for(A,C)in B.prices.items()if A in TinyMoves])
	else:A+=sum([C for(A,C)in B.prices.items()if A in ChunkyMoves])
	return A
SlamProgressiveSequence=[Locations.SuperSimianSlam,Locations.SuperDuperSimianSlam]
FunkySequence=[[Locations.CoconutGun,Locations.PeanutGun,Locations.GrapeGun,Locations.FeatherGun,Locations.PineappleGun],Locations.AmmoBelt1,Locations.HomingAmmo,Locations.AmmoBelt2,Locations.SniperSight]
CandySequence=[[Locations.Bongos,Locations.Guitar,Locations.Trombone,Locations.Saxophone,Locations.Triangle],Locations.MusicUpgrade1,Locations.ThirdMelon,Locations.MusicUpgrade2]
DonkeySequence=[Locations.BaboonBlast,Locations.StrongKong,Locations.GorillaGrab]
DiddySequence=[Locations.ChimpyCharge,Locations.RocketbarrelBoost,Locations.SimianSpring]
LankySequence=[Locations.Orangstand,Locations.BaboonBalloon,Locations.OrangstandSprint]
TinySequence=[Locations.MiniMonkey,Locations.PonyTailTwirl,Locations.Monkeyport]
ChunkySequence=[Locations.HunkyChunky,Locations.PrimatePunch,Locations.GorillaGone]
Sequences=[SlamProgressiveSequence,FunkySequence,CandySequence,DonkeySequence,DiddySequence,LankySequence,TinySequence,ChunkySequence]
'\nSo for coin logic, we want to make sure the player can\'t spend coins incorrectly and lock themselves out.\nThis means every buyable item has to account for, potentially, buying every other possible item first.\nSo each price will be inflated by a lot for logic purposes.\nTotal prices are as follows, in vanilla:\nCranky generic: 12\nCranky specific: 15\nCandy generic: 21\nCandy specific: 3\nFunky generic: 20\nFunky specific: 3\nTotal one kong can possibly spend: 74\n\nThe following only applies if move locations are not decoupled, meaning certain locations must be bought in sequence:\nSo basically, whatever "line" the kong is buying from, need to subtract prices\nfrom future entries in that line from 74 (or whatever the max is if prices are random).\nSo since Cranky\'s upgrades cost 3, 5, and 7, the logical price of his\nfirst upgrade will be 74 - 7 - 5 = 62.\nSince prices can be randomized, we will dynamically subtract the prices of future purchases\nin any given sequence.\n\nIf moves are decoupled so that they don\'t need be bought in sequence, then any location could be the final location,\nmeaning we just must consider the maximum price for every location.\n'
def GetPriceOfMoveItem(item,settings,slamLevel,ammoBelts,instUpgrades):
	'Get price of a move item. Needs to know current level of owned progressive moves to give correct price for progressive items.';E=instUpgrades;D=ammoBelts;C=slamLevel;B=settings;A=item
	if A==Items.ProgressiveSlam:
		if C in[1,2]:return B.prices[A][C-1]
		else:return _A
	elif A==Items.ProgressiveAmmoBelt:
		if D in[0,1]:return B.prices[A][D]
		else:return _A
	elif A==Items.ProgressiveInstrumentUpgrade:
		if E in[0,1,2]:return B.prices[A][E]
		else:return _A
	else:return B.prices[A]
def KongCanBuy(location,coins,settings,kong,slamLevel,ammoBelts,instUpgrades):
	'Check if given kong can logically purchase the specified location.';A=location
	if LocationList[A].item is _A or LocationList[A].item==Items.NoItem:return True
	B=GetPriceOfMoveItem(LocationList[A].item,settings,slamLevel,ammoBelts,instUpgrades)
	if B is not _A:return coins[kong]>=B
	else:return False
def AnyKongCanBuy(location,coins,settings,slamLevel,ammoBelts,instUpgrades):'Check if any kong can logically purchase this location.';return any((KongCanBuy(location,coins,settings,A,slamLevel,ammoBelts,instUpgrades)for A in[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]))
def EveryKongCanBuy(location,coins,settings,slamLevel,ammoBelts,instUpgrades):'Check if any kong can logically purchase this location.';return all((KongCanBuy(location,coins,settings,A,slamLevel,ammoBelts,instUpgrades)for A in[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]))
def CanBuy(location,coins,settings,slamLevel,ammoBelts,instUpgrades):
	'Check if an appropriate kong can logically purchase this location.';F=instUpgrades;E=ammoBelts;D=slamLevel;C=settings;B=coins;A=location
	if A in DonkeyMoveLocations:return KongCanBuy(A,B,C,Kongs.donkey,D,E,F)
	elif A in DiddyMoveLocations:return KongCanBuy(A,B,C,Kongs.diddy,D,E,F)
	elif A in LankyMoveLocations:return KongCanBuy(A,B,C,Kongs.lanky,D,E,F)
	elif A in TinyMoveLocations:return KongCanBuy(A,B,C,Kongs.tiny,D,E,F)
	elif A in ChunkyMoveLocations:return KongCanBuy(A,B,C,Kongs.chunky,D,E,F)
	else:return AnyKongCanBuy(A,B,C,D,E,F)