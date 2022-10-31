'Balloon importer from Bismuths Spreadsheet.'
_D='path'
_C='kongs'
_B='balloon'
_A=None
def convertTruthiness(truth_string):
	'Convert Excel truth strings to boolean.'
	if truth_string=='TRUE':return True
	return False
with open('import.csv',newline='')as csvfile:
	dataset=[];balloon=_A;name=_A;map=_A;speed=_A;kongs={}
	for (row_index,row) in enumerate(csvfile):
		if row_index>=2:
			rowdata=row.replace('\r\n','').split(',');newentry={}
			if rowdata[15]!=''and rowdata[15]!=balloon:balloon=rowdata[15];name=rowdata[16];speed=rowdata[17];map=rowdata[18];kongs={'dk':convertTruthiness(rowdata[23]),'diddy':convertTruthiness(rowdata[24]),'lanky':convertTruthiness(rowdata[25]),'tiny':convertTruthiness(rowdata[26]),'chunky':convertTruthiness(rowdata[27])};dataset.append({_B:int(balloon),'map':map,'name':name,'speed':int(speed),_C:kongs,_D:[]})
			if rowdata[19]!='':newentry['order']=int(rowdata[19]);newentry['x']=int(float(rowdata[20]));newentry['y']=int(float(rowdata[21]));newentry['z']=int(float(rowdata[22]));dict_index=next((A for(A,B)in enumerate(dataset)if B[_B]==int(balloon)),_A);dataset[dict_index][_D].append(newentry)
with open('balloons.txt','w')as outputfile:
	for bln_data in dataset:
		kong_lst=[]
		for kong in bln_data[_C]:
			if bln_data[_C][kong]:
				if kong=='dk':kong='donkey'
				kong_lst.append(f"Kongs.{kong}")
		points=[]
		for pt in bln_data[_D]:points.append([pt['order'],pt['x'],pt['y'],pt['z']])
		if len(points)>0:points.append('&nbsp;')
		translation={39:_A};outputfile.write(f'Balloon(id={bln_data[_B]}, map_id=Maps.{bln_data["map"]}, name="{bln_data["name"]}", speed={bln_data["speed"]}, konglist={str(kong_lst).translate(translation)}, region="", points={str(points)}),\n'.replace(" '&nbsp;'",''))