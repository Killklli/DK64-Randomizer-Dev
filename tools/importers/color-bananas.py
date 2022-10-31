'Color Banana importer from Bismuths Spreadsheet.'
_E='amount'
_D='locations'
_C='kongs'
_B='group'
_A=None
def convertTruthiness(truth_string):
	'Convert Excel truth strings to boolean.'
	if truth_string=='TRUE':return True
	return False
with open('import.csv',newline='')as csvfile:
	dataset=[];group=_A;name=_A;map=_A;kongs={}
	for (row_index,row) in enumerate(csvfile):
		if row_index>=2:
			rowdata=row.replace('\r\n','').split(',');newentry={}
			if rowdata[0]!=''and rowdata[0]!=group:group=rowdata[0];name=rowdata[1];map=rowdata[2];kongs={'dk':convertTruthiness(rowdata[9]),'diddy':convertTruthiness(rowdata[10]),'lanky':convertTruthiness(rowdata[11]),'tiny':convertTruthiness(rowdata[12]),'chunky':convertTruthiness(rowdata[13])};dataset.append({_B:int(group),'map':map,'name':name,_C:kongs,_D:[]})
			newentry[_E]=int(rowdata[3]);newentry['scale']=float(rowdata[5]);newentry['x']=int(float(rowdata[6]));newentry['y']=int(float(rowdata[7]));newentry['z']=int(float(rowdata[8]));dict_index=next((A for(A,B)in enumerate(dataset)if B[_B]==int(group)),_A);dataset[dict_index][_D].append(newentry)
with open('coloredbananas.txt','w')as outputfile:
	for cb_group in dataset:
		kong_lst=[]
		for kong in cb_group[_C]:
			if cb_group[_C][kong]:
				if kong=='dk':kong='donkey'
				kong_lst.append(f"Kongs.{kong}")
		locations=[]
		for loc in cb_group[_D]:locations.append([loc[_E],loc['scale'],loc['x'],loc['y'],loc['z']])
		if len(locations)>0:locations.append('&nbsp;')
		translation={39:_A};outputfile.write(f'ColoredBananaGroup(group={cb_group[_B]}, map_id=Maps.{cb_group["map"]}, name="{cb_group["name"]}", konglist={str(kong_lst).translate(translation)}, region="", locations={str(locations)}),\n'.replace(" '&nbsp;'",''))