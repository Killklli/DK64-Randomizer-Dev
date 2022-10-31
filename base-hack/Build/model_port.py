'Port models to actors and model two objects, based on inputs of vertices and a display list.'
_I='potion_any'
_H='potion_chunky'
_G='potion_tiny'
_F='potion_lanky'
_E='potion_diddy'
_D='potion_dk'
_C=None
_B='rb'
_A='big'
import zlib,os
rom_file='rom/dk64.z64'
temp_file='temp.bin'
ptr_offset=1055824
m2_table=4
ac_table=5
def portalModel_M2(vtx_file,dl_file,overlay_dl_file,model_name,base):
	'Convert model two model file from various source files.';K=overlay_dl_file
	with open(rom_file,_B)as C:
		C.seek(ptr_offset+m2_table*4);Q=ptr_offset+int.from_bytes(C.read(4),_A);C.seek(Q+base*4);E=ptr_offset+(int.from_bytes(C.read(4),_A)&2147483647);R=ptr_offset+(int.from_bytes(C.read(4),_A)&2147483647);S=R-E;C.seek(E);F=C.read(S);C.seek(E);T=int.from_bytes(C.read(2),_A)
		if T==8075:F=zlib.decompress(F,15+32)
		with open(temp_file,'wb')as A:A.write(F)
	with open(temp_file,_B)as A:
		with open(f"{model_name}_om2.bin",'wb')as B:
			A.seek(64);G=int.from_bytes(A.read(4),_A);A.seek(0);U=A.read(G);B.write(U);L=0
			with open(dl_file,_B)as H:M=H.read();L=len(M);B.write(M)
			I=0
			if K!=0:
				with open(K,_B)as H:N=H.read();I=len(N);B.write(N)
			else:I=8;B.write((223<<56).to_bytes(8,_A))
			O=0
			with open(vtx_file,_B)as V:P=V.read();O=len(P);B.write(P)
			A.seek(76);W=int.from_bytes(A.read(4),_A);A.seek(W);X=A.read();B.write(X);B.seek(68);D=G+L;B.write(D.to_bytes(4,_A));D+=I;B.write(D.to_bytes(4,_A));D+=O;A.seek(76);J=int.from_bytes(A.read(4),_A);B.write(D.to_bytes(4,_A));Y=D-J;Z=int((G-1-80)/4)
			for a in range(Z):J=int.from_bytes(A.read(4),_A);B.write((J+Y).to_bytes(4,_A))
	if os.path.exists(temp_file):os.remove(temp_file)
def portalModel_Actor(vtx_file,dl_file,model_name,base):
	'Create actor file from various source files.';L=dl_file;K=vtx_file
	with open(rom_file,_B)as C:
		C.seek(ptr_offset+ac_table*4);S=ptr_offset+int.from_bytes(C.read(4),_A);C.seek(S+base*4);G=ptr_offset+(int.from_bytes(C.read(4),_A)&2147483647);T=ptr_offset+(int.from_bytes(C.read(4),_A)&2147483647);U=T-G;C.seek(G);H=C.read(U);C.seek(G);V=int.from_bytes(C.read(2),_A)
		if V==8075:H=zlib.decompress(H,15+32)
		with open(temp_file,'wb')as B:B.write(H)
	with open(temp_file,_B)as B:
		with open(f"{model_name}_om1.bin",'w+b')as A:
			if L is _C:
				A.write(B.read());A.seek(40);W=10
				with open(K,_B)as I:
					E=I.read();F=int(len(E)/16);A.write(E);b=A.tell()
					for M in range(F):
						for N in range(3):
							A.seek(M*16+40+2*N);D=int.from_bytes(A.read(2),_A)
							if D>32767:D-=65536
							D*=W;A.seek(M*16+40+2*N)
							if D<0:D+=65536
							A.write(D.to_bytes(2,_A))
			else:
				B.seek(0);J=int.from_bytes(B.read(4),_A);O=int.from_bytes(B.read(4),_A);A.write(B.read(40));F=0
				with open(K,_B)as I:E=I.read();F=len(E);A.write(E)
				X=0
				with open(L,_B)as Y:P=Y.read()[48:];X=len(P);A.write(P)
				Q=A.tell();A.seek(4);R=Q+J-40;A.write(R.to_bytes(4,_A));Z=R-O
				for c in range(3):a=int.from_bytes(B.read(4),_A);A.write((a+Z).to_bytes(4,_A))
				A.seek(Q);A.write((J+F).to_bytes(4,_A));B.seek(O+44-J);A.write(B.read())
	if os.path.exists(temp_file):os.remove(temp_file)
model_dir='assets/Non-Code/models/'
portalModel_M2(f"{model_dir}coin.vtx",f"{model_dir}nin_coin.dl",f"{model_dir}coin_overlay.dl",'nintendo_coin',144)
portalModel_M2(f"{model_dir}coin.vtx",f"{model_dir}rw_coin.dl",f"{model_dir}coin_overlay.dl",'rareware_coin',144)
portalModel_M2(f"{model_dir}potion_dk.vtx",f"{model_dir}potion.dl",0,_D,144)
portalModel_M2(f"{model_dir}potion_diddy.vtx",f"{model_dir}potion.dl",0,_E,144)
portalModel_M2(f"{model_dir}potion_lanky.vtx",f"{model_dir}potion.dl",0,_F,144)
portalModel_M2(f"{model_dir}potion_tiny.vtx",f"{model_dir}potion.dl",0,_G,144)
portalModel_M2(f"{model_dir}potion_chunky.vtx",f"{model_dir}potion.dl",0,_H,144)
portalModel_M2(f"{model_dir}potion_any.vtx",f"{model_dir}potion.dl",0,_I,144)
portalModel_Actor(f"{model_dir}potion_dk.vtx",_C,_D,184)
portalModel_Actor(f"{model_dir}potion_diddy.vtx",_C,_E,184)
portalModel_Actor(f"{model_dir}potion_lanky.vtx",_C,_F,184)
portalModel_Actor(f"{model_dir}potion_tiny.vtx",_C,_G,184)
portalModel_Actor(f"{model_dir}potion_chunky.vtx",_C,_H,184)
portalModel_Actor(f"{model_dir}potion_any.vtx",_C,_I,184)