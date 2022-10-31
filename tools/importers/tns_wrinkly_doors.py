'Convert Dirt Patch CSV into a python list.'
_L='test_round'
_K='commented'
_J='moveless'
_I='logicregion'
_H='placed'
_G='kongs'
_F='door_type'
_E='scale'
_D='levelname'
_C='post_comment'
_B='coords'
_A='logic'
import csv,re
with open('doors.csv',newline='')as csvfile:
	patch_data=csv.reader(csvfile,delimiter=',',quotechar='|');door_data_json=[]
	for (idx,row) in enumerate(patch_data):
		if idx>0:door_data_json.append({_D:row[0],'map':row[1],_I:row[2],'name':row[3],_B:[float(row[4]),float(row[5]),float(row[6]),float(row[7])],'rx':row[9],'rz':row[10],_E:row[11],_F:row[12],'group':row[14],_J:row[15],_A:row[16],_G:row[17],_H:row[18],_K:row[19],_C:row[20],_L:row[21]})
	print(f"{len(door_data_json)} doors found");print('-----------------');print('Levels.JungleJapes: [');previous_levelname='JungleJapes'
	for x in door_data_json:
		precomment=''
		if x[_C]!='':x[_C]='  # '+x[_C]
		if x[_K]!='':precomment='# '
		level_name=x[_D].replace(' ','')
		if level_name!=previous_levelname:previous_levelname=level_name;print('],');print('Levels.'+level_name+': [')
		rx_text='';rz_text='';scale_text='';door_type_text='';placed_text=''
		if x['rx']:rx_text=', rx='+x['rx']+''
		if x['rz']:rz_text=', rz='+x['rz']+''
		if x[_E]:scale_text=', scale='+x[_E]+''
		if x[_F]:door_type_text=', door_type="'+x[_F]+'"'
		name=f"{x[_D]}: {x['name']}";moveless_text=', moveless=False'
		if x[_J].strip()=='':moveless_text=''
		if x[_A].strip()=='':x[_A]='True'
		x[_A]=x[_A].replace('|',',');logic=f"lambda l: {x[_A]}";kongs_text=''
		if x[_G]:kongs_text=x[_G].replace(' or ',', Kongs.');kongs_text=', kong_lst=[Kongs.'+kongs_text+']'
		if x[_H]!='':placed_text=', placed="'+x[_H]+'"'
		print(f"\t"+precomment+f'DoorData(name="{name}", map=Maps.{x["map"]}, logicregion=Regions.{x[_I]}, location=[{x[_B][0]}, {x[_B][1]}, {x[_B][2]}, {x[_B][3]}]{rx_text}{rz_text}{scale_text}{kongs_text}, group={x["group"]}{moveless_text}, logic={logic}{placed_text}{door_type_text}, test_round={x[_L]}),{x[_C]}')
	print('],')