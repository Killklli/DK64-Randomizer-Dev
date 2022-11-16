'Shuffles items for Item Rando.'
_C=False
_B=True
_A=None
import random,randomizer.Lists.Exceptions as Ex
from randomizer.Enums.Items import Items
from randomizer.Lists.Location import LocationList
from randomizer.Enums.Types import Types
from randomizer.Spoiler import Spoiler
from randomizer.Enums.Kongs import Kongs
from randomizer.Lists.Item import ItemList,NameFromKong
class LocationSelection:
	'Class which contains information pertaining to assortment.'
	def __init__(A,*,vanilla_item=_A,placement_data=_A,is_reward_point=_C,flag=_A,kong=Kongs.any,location=_A,name='',is_shop=_C,price=0,placement_index=0,can_have_item=_B,can_place_item=_B,shop_locked=_C,shared=_C,order=0,move_name=''):'Initialize with given data.';A.name=name;A.old_item=vanilla_item;A.placement_data=placement_data;A.old_flag=flag;A.old_kong=kong;A.reward_spot=is_reward_point;A.location=location;A.is_shop=is_shop;A.price=price;A.placement_index=placement_index;A.can_have_item=can_have_item;A.can_place_item=can_place_item;A.shop_locked=shop_locked;A.shared=shared;A.order=order;A.move_name='';A.new_item=_A;A.new_flag=_A;A.new_kong=_A
	def PlaceFlag(A,flag,kong):'Place item for assortment.';A.new_flag=flag;A.new_kong=kong
class MoveData:
	"Class which contains information pertaining to a move's attributes."
	def __init__(A,subtype,kong,index,shared=_C,count=1):'Initialize with given data.';A.subtype=subtype;A.kong=kong;A.index=index;A.shared=shared;A.count=count
move_list={Items.BaboonBlast:MoveData(0,Kongs.donkey,1),Items.ChimpyCharge:MoveData(0,Kongs.diddy,1),Items.Orangstand:MoveData(0,Kongs.lanky,1),Items.MiniMonkey:MoveData(0,Kongs.tiny,1),Items.HunkyChunky:MoveData(0,Kongs.chunky,1),Items.Coconut:MoveData(2,Kongs.donkey,1),Items.Peanut:MoveData(2,Kongs.diddy,1),Items.Grape:MoveData(2,Kongs.lanky,1),Items.Feather:MoveData(2,Kongs.tiny,1),Items.Pineapple:MoveData(2,Kongs.chunky,1),Items.StrongKong:MoveData(0,Kongs.donkey,2),Items.RocketbarrelBoost:MoveData(0,Kongs.diddy,2),Items.Bongos:MoveData(4,Kongs.donkey,1),Items.Guitar:MoveData(4,Kongs.diddy,1),Items.Trombone:MoveData(4,Kongs.lanky,1),Items.Saxophone:MoveData(4,Kongs.tiny,1),Items.Triangle:MoveData(4,Kongs.chunky,1),Items.GorillaGrab:MoveData(0,Kongs.donkey,3),Items.SimianSpring:MoveData(0,Kongs.diddy,3),Items.BaboonBalloon:MoveData(0,Kongs.lanky,2),Items.PonyTailTwirl:MoveData(0,Kongs.tiny,2),Items.PrimatePunch:MoveData(0,Kongs.chunky,2),Items.ProgressiveAmmoBelt:MoveData(3,Kongs.any,1,_B,2),Items.ProgressiveInstrumentUpgrade:MoveData(4,Kongs.any,2,_B,3),Items.ProgressiveSlam:MoveData(1,Kongs.any,2,_B,2),Items.HomingAmmo:MoveData(2,Kongs.any,2,_B,1),Items.OrangstandSprint:MoveData(0,Kongs.lanky,3),Items.Monkeyport:MoveData(0,Kongs.tiny,3),Items.GorillaGone:MoveData(0,Kongs.chunky,3),Items.SniperSight:MoveData(2,Kongs.any,3,_B,1)}
progressive_move_flag_dict={Items.ProgressiveSlam:[656,657],Items.ProgressiveAmmoBelt:[658,659],Items.ProgressiveInstrumentUpgrade:[660,661,662]}
def ShuffleItems(spoiler):
	'Shuffle items into assortment.';S='Kasplat';E=spoiler;B={};K=[];G=[]
	for L in LocationList:
		A=LocationList[L]
		if(A.default_mapid_data is not _A or A.type in(Types.Shop,Types.TrainingBarrel,Types.Shockwave))and A.type in E.settings.shuffled_location_types:
			O={}
			if A.default_mapid_data:
				for C in A.default_mapid_data:O[C.map]=C.id
				H=A.default_mapid_data[0].flag;M=A.default_mapid_data[0].kong;P=[-1]
			else:H=-1;M=A.kong;P=A.placement_index
			N=0
			if A.type==Types.Shop:
				if E.settings.random_prices=='vanilla':
					if A.item in E.settings.prices.keys():N=E.settings.prices[A.item]
				else:N=E.settings.prices[L]
			D=LocationSelection(vanilla_item=A.type,flag=H,placement_data=O,is_reward_point=A.is_reward,is_shop=A.type in(Types.Shop,Types.TrainingBarrel,Types.Shockwave),price=N,placement_index=P,kong=M,location=L,name=A.name)
			if A.item is _A or A.item==Items.NoItem:F=_A
			else:F=ItemList[A.item]
			if F is not _A:
				D.new_item=F.type;D.new_kong=F.kong
				if F.rando_flag is not _A:
					if F.rando_flag==-1:D.new_flag=progressive_move_flag_dict[A.item].pop()
					else:D.new_flag=F.rando_flag
					K.append(D)
				else:G.append(D)
			else:D.new_item=_A;D.new_kong=_A;D.new_flag=_A;K.append(D)
			if A.type not in B:
				if A.type==Types.Blueprint:B[A.type]={};B[A.type][Kongs.donkey]=[];B[A.type][Kongs.diddy]=[];B[A.type][Kongs.lanky]=[];B[A.type][Kongs.tiny]=[];B[A.type][Kongs.chunky]=[]
				else:B[A.type]=[]
			if A.type==Types.Blueprint:B[A.type][M].append(H)
			else:B[A.type].append(H)
	random.shuffle(G)
	for C in G:
		if C.new_flag is _A:
			if C.new_item==Types.Blueprint:C.new_flag=B[C.new_item][C.new_kong].pop()
			else:C.new_flag=B[C.new_item].pop()
	if any((A for A in G if A.new_flag is _A)):T=[A for A in G if A.new_flag is _A];raise Ex.FillException('ERROR: Failed to create a valid flag assignment for this fill!')
	E.item_assignment=G+K;Q={}
	for I in E.item_assignment:
		R='Nothing'
		if I.new_item is not _A:R=ItemList[LocationList[I.location].item].name
		J=I.name
		if S in J:J=f"{J.split(S)[0]} {NameFromKong(I.old_kong)} Kasplat"
		Q[J]=R
	E.debug_human_item_assignment=Q