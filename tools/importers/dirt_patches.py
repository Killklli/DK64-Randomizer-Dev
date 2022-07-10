'Convert Dirt Patch CSV into a python list.'
_D='vanilla'
_C='subname'
_B=' - '
_A='coords'
import csv,re
with open('dirt_patches.csv',newline='')as csvfile:
	patch_data=csv.reader(csvfile,delimiter=',',quotechar='|');patch_data_json=[]
	for (idx,row) in enumerate(patch_data):
		if idx>0:patch_data_json.append({'map':row[1],_C:row[3],'name':row[4],_A:[float(row[5]),float(row[6]),float(row[7])],'rot':int(row[9]),_D:row[10]=='YES'})
	print(f"{len(patch_data_json)} patches found");print('-----------------')
	for x in patch_data_json:
		vanilla_text=''
		if x[_D]:vanilla_text=', vanilla=True'
		subname=x[_C]
		if _B in subname:pre=subname.split(_B)[0];post=subname.split(_B)[1].split(': ')[0];post=re.sub('((?<=[a-z])[A-Z]|(?<!\\A)[A-Z](?=[a-z]))',' \\1',post);subname=f"{pre} - {post}: "
		name=f"{subname}{x['name']}";print(f'DirtPatchData(name="{name}", map_id=Maps.{x["map"]}, x={x[_A][0]}, y={x[_A][1]}, z={x[_A][2]}, rotation={x["rot"]}{vanilla_text}),')