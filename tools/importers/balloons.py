'Balloon importer from Bismuths Spreadsheet.'
_B='balloon'
_A=None
with open('import.csv',newline='')as csvfile:
	dataset=[];balloon=_A;map=_A;speed=_A
	for row in csvfile:
		rowdata=row.replace('\r\n','').split(',');newentry={}
		if rowdata[0]!=''and rowdata[0]!=balloon:balloon=rowdata[0];speed=rowdata[1];map=rowdata[2];dataset.append({_B:int(balloon),'map':map,'speed':int(speed),'path':[]})
		newentry['order']=int(rowdata[3]);newentry['x']=int(float(rowdata[4]));newentry['y']=int(float(rowdata[5]));newentry['z']=int(float(rowdata[6]));dict_index=next((A for(A,B)in enumerate(dataset)if B[_B]==int(balloon)),_A);dataset[dict_index]['path'].append(newentry)
	print(dataset)