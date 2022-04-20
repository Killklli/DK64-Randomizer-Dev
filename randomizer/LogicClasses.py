'Contains classes used in the logic system.'
_C=None
_B=True
_A=False
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Transitions import Transitions
class LocationLogic:
	'Logic for a location.'
	def __init__(A,id,logic,bonusBarrel=_A):'Initialize with given parameters.';A.id=id;A.logic=logic;A.bonusBarrel=bonusBarrel
class Event:
	'Event within a region.\n\n    Events act as statically placed items\n    For example, if Lanky must press a button in region x to open something in region y,\n    that can be represented as a button press event in region x which is checked for in region y.\n    '
	def __init__(A,name,logic):'Initialize with given parameters.';A.name=name;A.logic=logic
class Collectible:
	'Class used for colored bananas and banana coins.'
	def __init__(A,type,kong,logic,coords,amount=1):'Initialize with given parameters.';A.type=type;A.kong=kong;A.logic=logic;A.amount=amount;A.coords=coords;A.added=_A
class Region:
	'Region contains shufflable locations, events, and transitions to other regions.'
	def __init__(A,name,level,tagbarrel,deathwarp,locations,events,transitionFronts,restart=_C):
		'Initialize with given parameters.';B=deathwarp;A.name=name;A.level=level;A.tagbarrel=tagbarrel;A.deathwarp=_C;A.locations=locations;A.events=events;A.exits=transitionFronts;A.restart=restart
		if B is not _C:
			if isinstance(B,TransitionFront):A.deathwarp=B
			else:
				if B==-1:B=A.GetDefaultDeathwarp()
				A.deathwarp=TransitionFront(B,lambda l:_B)
		A.ResetAccess()
	def UpdateAccess(A,kong,logicVariables):
		'Set that given kong has access to this region.';C=kong;B=logicVariables
		if A.tagbarrel:A.donkeyAccess=B.donkey;A.diddyAccess=B.diddy;A.lankyAccess=B.lanky;A.tinyAccess=B.tiny;A.chunkyAccess=B.chunky
		elif C==Kongs.donkey:A.donkeyAccess=_B
		elif C==Kongs.diddy:A.diddyAccess=_B
		elif C==Kongs.lanky:A.lankyAccess=_B
		elif C==Kongs.tiny:A.tinyAccess=_B
		else:A.chunkyAccess=_B
	def UpdateAccessFromRegion(A,region):'Set access to region from another region.';B=region;A.donkeyAccess=A.donkeyAccess or B.donkeyAccess;A.diddyAccess=A.diddyAccess or B.diddyAccess;A.lankyAccess=A.lankyAccess or B.lankyAccess;A.tinyAccess=A.tinyAccess or B.tinyAccess;A.chunkyAccess=A.chunkyAccess or B.chunkyAccess
	def HasAccess(A,kong):
		'Check if given kong has access through this area.\n\n        Used if a kong has access through a tag barrel only.\n        ';B=kong
		if B==Kongs.donkey:return A.donkeyAccess
		elif B==Kongs.diddy:return A.diddyAccess
		elif B==Kongs.lanky:return A.lankyAccess
		elif B==Kongs.tiny:return A.tinyAccess
		elif B==Kongs.chunky:return A.chunkyAccess
		else:return A.donkeyAccess or A.diddyAccess or A.lankyAccess or A.tinyAccess or A.chunkyAccess
	def ResetAccess(A):'Clear access for all kongs.';A.donkeyAccess=_A;A.diddyAccess=_A;A.lankyAccess=_A;A.tinyAccess=_A;A.chunkyAccess=_A
	def GetDefaultDeathwarp(A):
		"Get the default deathwarp depending on the region's level."
		if A.level==Levels.DKIsles:return Regions.IslesMain
		elif A.level==Levels.JungleJapes:return Regions.JungleJapesMain
		elif A.level==Levels.AngryAztec:return Regions.AngryAztecStart
		elif A.level==Levels.FranticFactory:return Regions.FranticFactoryStart
		elif A.level==Levels.GloomyGalleon:return Regions.GloomyGalleonStart
		elif A.level==Levels.FungiForest:return Regions.FungiForestStart
		elif A.level==Levels.CrystalCaves:return Regions.CrystalCavesMain
		elif A.level==Levels.CreepyCastle:return Regions.CreepyCastleMain
		elif A.level==Levels.HideoutHelm:return Regions.HideoutHelmStart
class TransitionBack:
	'The exited side of a transition between regions.'
	def __init__(A,regionId,exitName,reverse=_C):'Initialize with given parameters.';A.regionId=regionId;A.name=exitName;A.reverse=reverse
class TransitionFront:
	'The entered side of a transition between regions.'
	def __init__(A,dest,logic,exitShuffleId=_C,assumed=_A):'Initialize with given parameters.';A.dest=dest;A.logic=logic;A.exitShuffleId=exitShuffleId;A.assumed=assumed