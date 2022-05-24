'Convert vanilla scripts into modified rando scripts.'
_B='name'
_A='big'
from instance_script_maps import instance_script_maps
import zlib,os,shutil
instance_name='instance_script_maps.py'
instance_copy=f"../../../Build/{instance_name}"
shutil.copyfile(instance_copy,instance_name)
rom_dir='../../../rom/dk64.z64'
dump_dir='./dump'
pointer_table_offset=1055824
table=10
def getScriptName(script_list,id):
	'Grab script name from ID.'
	for A in script_list:
		if A['id']==id:return A[_B]
	return''
def addToFile(name,folder,line):
	'Add line to file if script is being modified.'
	if name!='':
		A=f"{dump_dir}/{folder}"
		if not os.path.exists(A):os.mkdir(A)
		B=f"{A}/{name}.txt"
		with open(B,'a'if os.path.exists(B)else'w')as C:C.write(f"{line}\n")
def parseData(data,folder_name,scripts_list):
	'Parse a script file into subscripts.';J=scripts_list;H=folder_name;F='temp.bin'
	with open(F,'wb')as A:A.write(data)
	with open(F,'rb')as A:
		A.seek(0);L=int.from_bytes(A.read(2),_A);B=2
		for P in range(L):
			A.seek(B);id=int.from_bytes(A.read(2),_A);I=getScriptName(J,id);M=int.from_bytes(A.read(2),_A);Q=int.from_bytes(A.read(2),_A);B+=6
			for R in range(M):
				A.seek(B);N=int.from_bytes(A.read(2),_A);B+=2
				for S in range(N):
					A.seek(B);G=int.from_bytes(A.read(2),_A);K='COND'
					if G&32768:K='CONDINV'
					C=[0,0,0];D=''
					for E in range(3):C[E]=int.from_bytes(A.read(2),_A);D+=str(C[E])+' '
					addToFile(I,H,f"{K} {G} | {D[:-1]}");B+=8
				O=int.from_bytes(A.read(2),_A);B+=2
				for T in range(O):
					A.seek(B);G=int.from_bytes(A.read(2),_A);C=[0,0,0];D=''
					for E in range(3):C[E]=int.from_bytes(A.read(2),_A);D+=str(C[E])+' '
					addToFile(I,H,f"EXEC {G} | {D[:-1]}");B+=8
				addToFile(I,H,'ENDBLOCK')
	if os.path.exists(F):os.remove(F)
	return len(J)!=0
def unpackFiles():
	'Unpack ROM to grab script files.'
	with open(rom_dir,'rb')as A:
		A.seek(pointer_table_offset+table*4);F=pointer_table_offset+int.from_bytes(A.read(4),_A)
		if os.path.exists(dump_dir):shutil.rmtree(dump_dir)
		if not os.path.exists(dump_dir):os.mkdir(dump_dir)
		C=0
		for B in instance_script_maps:
			print(f'[{C+1} / {len(instance_script_maps)}] Converting "{B[_B]}"');G=B['map'];A.seek(F+G*4);D=pointer_table_offset+int.from_bytes(A.read(4),_A);H=pointer_table_offset+int.from_bytes(A.read(4),_A);I=H-D;A.seek(D);J=A.read(I);E=zlib.decompress(J,15+32);K=parseData(E,B[_B],B['scripts'].copy())
			if not K:
				with open(f"./dump/{B[_B]}.bin",'wb')as L:L.write(E)
			C+=1
unpackFiles()