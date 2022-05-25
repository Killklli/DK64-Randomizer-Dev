'Generate Watch File.'
def read_symbols():
	'Read the symbols file and update the labels.';B=[];C='asm/symbols.asm'
	with open(C,'r')as D:
		E=D.readlines()
		for A in E:
			if'.definelabel'in A:F=A.split('.definelabel ')[1].split(', ')[0];G='0x'+A.split(', ')[1][4:10];B.append({F,G})
	return B
def read_h_file(symbols_data):
	'Read the H file and update the externs.';G='extern ';E=[];F=[]
	with open('include/dk64.h','r')as H:
		I=H.readlines()
		for C in symbols_data:
			for A in I:
				if G in A:
					if'('not in A and')'not in A:
						A=A.split(G)[1]
						if'//'in A:A=A.split('//')[0]
						D=A.split(' ');B='';J=D[-1].split(';')[-1]
						if J==list(C)[1]:
							for K in range(len(D)-1):B+=D[K]+' '
							if B not in F:F.append(B)
							E.append([list(C)[0],list(C)[1],B])
	return E
def create_wch_file(_data,watch_file_name):
	'Create an update WCH file.';E='w';C='d';A='h';H=[['*',C,A],['float',C,'f'],['unsigned int',C,A],['int',C,A],['unsigned short',E,A],['short',E,A],['unsigned char','b',A],['char','b',A]]
	with open(watch_file_name,E)as I:
		F=['SystemID N64']
		for B in _data:
			G=False
			for D in H:
				if D[0]in B[2]:J=D[1];K=D[2];G=True;break
			if G:F.append(str(B[0][2:])+'\t'+str(J)+'\t'+str(K)+'\t1\tRDRAM\t'+str(B[1]))
		for B in F:I.write(B+'\n')
a=read_symbols()
b=read_h_file(a)
create_wch_file(b,'rom/dk64-randomizer-base.wch')