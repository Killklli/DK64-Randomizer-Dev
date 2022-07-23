'Convert Dirt Patch CSV into a python list.'
_H='resize'
_G='logicregion'
_F='vanilla'
_E='subname'
_D='levelname'
_C=' - '
_B='coords'
_A='logic'
import csv,re
with open('dirt_patches.csv',newline='')as csvfile:
	patch_data=csv.reader(csvfile,delimiter=',',quotechar='|');patch_data_json=[]
	for (idx,row) in enumerate(patch_data):
		if idx>0:patch_data_json.append({'map':row[1],_D:row[2],_E:row[3],'name':row[4],_B:[float(row[5]),float(row[6]),float(row[7])],'rot':int(row[9]),_F:row[10]=='YES','group':int(row[11]),_G:row[12],_A:row[13],_H:row[15]})
	print(f"{len(patch_data_json)} patches found");print('-----------------')
	for x in patch_data_json:
		level_name=x[_D].replace(' ','');vanilla_text=''
		if x[_F]:vanilla_text=', vanilla=True'
		subname=x[_E]
		if _C in subname:pre=subname.split(_C)[0];post=subname.split(_C)[1].split(': ')[0];post=re.sub('((?<=[a-z])[A-Z]|(?<!\\A)[A-Z](?=[a-z]))',' \\1',post);subname=f"{pre} - {post}: "
		name=f"{subname}{x['name']}"
		if x[_A].strip()=='':x[_A]='l.shockwave'
		else:x[_A]+=' and l.shockwave'
		x[_A]=x[_A].replace('|',',');logic=f"lambda l: {x[_A]}";print(f'DirtPatchData(name="{name}", level=Levels.{level_name}, map_id=Maps.{x["map"]}, x={x[_B][0]}, y={x[_B][1]}, z={x[_B][2]}, rotation={x["rot"]}{vanilla_text}, group={x["group"]}, logicregion=Regions.{x[_G]}, logic={logic}, resize="{x[_H]}"),')