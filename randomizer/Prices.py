'Functions and data for setting and calculating prices.'
_A=None
from math import ceil
import random
from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Types import Types
from randomizer.ItemPool import TrainingBarrelAbilities
from randomizer.Lists.Item import ItemList
from randomizer.Lists.Location import ChunkyMoveLocations,DiddyMoveLocations,DonkeyMoveLocations,LankyMoveLocations,LocationList,SharedMoveLocations,SharedShopLocations,TinyMoveLocations,TrainingBarrelLocations
VanillaPrices={Items.Vines:0,Items.Swim:0,Items.Barrels:0,Items.Oranges:0,Items.Camera:0,Items.Shockwave:0,Items.CameraAndShockwave:0,Items.BaboonBlast:3,Items.StrongKong:5,Items.GorillaGrab:7,Items.ChimpyCharge:3,Items.RocketbarrelBoost:5,Items.SimianSpring:7,Items.Orangstand:3,Items.BaboonBalloon:5,Items.OrangstandSprint:7,Items.MiniMonkey:3,Items.PonyTailTwirl:5,Items.Monkeyport:7,Items.HunkyChunky:3,Items.PrimatePunch:5,Items.GorillaGone:7,Items.Coconut:3,Items.Peanut:3,Items.Grape:3,Items.Feather:3,Items.Pineapple:3,Items.HomingAmmo:5,Items.SniperSight:7,Items.Bongos:3,Items.Guitar:3,Items.Trombone:3,Items.Saxophone:3,Items.Triangle:3,Items.ProgressiveSlam:[5,7],Items.ProgressiveAmmoBelt:[3,5],Items.ProgressiveInstrumentUpgrade:[5,7,9]}
ProgressiveMoves={Items.ProgressiveSlam:2,Items.ProgressiveAmmoBelt:2,Items.ProgressiveInstrumentUpgrade:3}
def CompleteVanillaPrices():
	'Complete the list of Vanilla prices with non-move items needing to cost 0.'
	for (A,B) in ItemList.items():
		if A not in VanillaPrices.keys():VanillaPrices[A]=0
def GetPriceWeights(weight):
	'Get the parameters for the price distribution.';D=weight;A=4.5;B=2;C=9
	if D=='high':A=6.5;B=3;C=12
	elif D=='low':A=2.5;B=1;C=6
	elif D=='extreme':A=11;B=2;C=15
	return A,B,C
def RandomizePrices(weight):
	'Generate randomized prices for each shop location.';C=weight;B={};A=GetPriceWeights(C);E=[A for(A,B)in LocationList.items()if B.type==Types.Shop]
	for F in E:B[F]=GenerateRandomPrice(C,A[0],A[1],A[2])
	for D in ProgressiveMoves.keys():
		B[D]=[]
		for G in range(ProgressiveMoves[D]):B[D].append(GenerateRandomPrice(C,A[0],A[1],A[2]))
	return B
def GenerateRandomPrice(weight,avg,stddev,upperLimit):
	'Generate a random price to assign.';B=upperLimit;C=1
	if weight=='free':A=0
	else:
		A=round(random.normalvariate(avg,stddev))
		if A<C:A=C
		elif A>B:A=B
	return A
def GetMaxForKong(settings,kong):
	'Get the maximum amount of coins the given kong can spend.';F=kong;C=settings;G=0;H=0;I=0;B=0;J=SharedMoveLocations-TrainingBarrelLocations-{Locations.CameraAndShockwave}
	for E in J:
		A=LocationList[E].item
		if A is not _A and A!=Items.NoItem:
			if A==Items.ProgressiveSlam:B+=C.prices[A][G];G+=1
			elif A==Items.ProgressiveInstrumentUpgrade:B+=C.prices[A][H];H+=1
			elif A==Items.ProgressiveAmmoBelt:B+=C.prices[A][I];I+=1
			else:B+=C.prices[E]
	D=DiddyMoveLocations.copy()
	if F==Kongs.donkey:D=DonkeyMoveLocations.copy();B+=2
	elif F==Kongs.lanky:D=LankyMoveLocations.copy()
	elif F==Kongs.tiny:D=TinyMoveLocations.copy();D.remove(Locations.CameraAndShockwave)
	elif F==Kongs.chunky:D=ChunkyMoveLocations.copy()
	for E in D:
		A=LocationList[E].item
		if A is not _A and A!=Items.NoItem:
			if A==Items.ProgressiveSlam:B+=C.prices[A][G];G+=1
			elif A==Items.ProgressiveInstrumentUpgrade:B+=C.prices[A][H];H+=1
			elif A==Items.ProgressiveAmmoBelt:B+=C.prices[A][I];I+=1
			else:B+=C.prices[E]
	return B
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
def GetPriceAtLocation(settings,location_id,location,slamLevel,ammoBelts,instUpgrades):
	'Get the price at this location.';E=instUpgrades;D=ammoBelts;C=slamLevel;B=settings;A=location.item
	if A is _A or A==Items.NoItem:return 0
	elif A==Items.ProgressiveSlam:
		if C in[1,2]:return B.prices[A][C-1]
		else:return 0
	elif A==Items.ProgressiveAmmoBelt:
		if D in[0,1]:return B.prices[A][D]
		else:return 0
	elif A==Items.ProgressiveInstrumentUpgrade:
		if E in[0,1,2]:return B.prices[A][E]
		else:return 0
	else:return B.prices[location_id]
def KongCanBuy(location_id,logic,kong):
	'Check if given kong can logically purchase the specified location.';C=location_id;A=logic;B=LocationList[C]
	if B.item is _A or B.item==Items.NoItem:return True
	D=GetPriceAtLocation(A.settings,C,B,A.Slam,A.AmmoBelts,A.InstUpgrades)
	if D is not _A:return A.Coins[kong]>=D
	else:return False
def AnyKongCanBuy(location,logic):'Check if any kong can logically purchase this location.';return any((KongCanBuy(location,logic,A)for A in[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]))
def EveryKongCanBuy(location,logic):'Check if any kong can logically purchase this location.';return all((KongCanBuy(location,logic,A)for A in[Kongs.donkey,Kongs.diddy,Kongs.lanky,Kongs.tiny,Kongs.chunky]))
def CanBuy(location,logic):
	'Check if an appropriate kong can logically purchase this location.';B=logic;A=location
	if A in TrainingBarrelLocations or A==Locations.CameraAndShockwave:return True
	if A in SharedMoveLocations:return KongCanBuy(A,B,B.kong)
	elif A in DonkeyMoveLocations:return KongCanBuy(A,B,Kongs.donkey)
	elif A in DiddyMoveLocations:return KongCanBuy(A,B,Kongs.diddy)
	elif A in LankyMoveLocations:return KongCanBuy(A,B,Kongs.lanky)
	elif A in TinyMoveLocations:return KongCanBuy(A,B,Kongs.tiny)
	elif A in ChunkyMoveLocations:return KongCanBuy(A,B,Kongs.chunky)