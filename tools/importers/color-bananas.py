'Color Banana importer from Bismuths Spreadsheet.'
_A='locations'
with open('import.csv',newline='')as csvfile:
	dataset=[];group=None;map=None;kongs={}
	for row in csvfile:
		rowdata=row.replace('\r\n','').split(',');newentry={}
		if rowdata[0]!=''and rowdata[0]!=group:group=rowdata[0];map=rowdata[1];kongs={'dk':bool(rowdata[7]),'diddy':bool(rowdata[8]),'lanky':bool(rowdata[9]),'tiny':bool(rowdata[10]),'chunky':bool(rowdata[11])};dataset.append({'group':int(group),'map':map,'kongs':kongs,_A:[]})
		newentry['amount']=int(rowdata[2]);newentry['x']=int(float(rowdata[4]));newentry['y']=int(float(rowdata[5]));newentry['z']=int(float(rowdata[6]));dict_index=next((A for(A,B)in enumerate(dataset)if B['group']==int(group)),None);dataset[dict_index][_A].append(newentry)
	print(dataset)