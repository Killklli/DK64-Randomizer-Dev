'Encryption and Decryption of settings strings.'
import json,collections,base64
from itertools import groupby
import js
def encrypt_settings_string(dict_data):
	'Take a dictionary and return an encrypted string.\n\n    Args:\n        dict_data (dict): Posted JSON data from the form.\n\n    Returns:\n        str: Returns an encrypted string.\n    ';D=dict_data
	for I in ['download_patch_file','seed','settings_string','chunky_colors','chunky_custom_color','diddy_colors','diddy_custom_color','dk_colors','dk_custom_color','enguarde_colors','enguarde_custom_color','klaptrap_model','lanky_colors','lanky_custom_color','rambi_colors','rambi_custom_color','random_colors','random_music','music_bgm','music_events','music_fanfares','tiny_colors','tiny_custom_color','override_cosmetics','search']:D.pop(I)
	B=collections.OrderedDict(sorted(D.items()));J=collections.OrderedDict(sorted(default_dict.items()));C=''
	for A in B:
		if J[A]==B[A]:C+=','
		elif type(B[A])==bool:
			if B[A]is True:C+='x1,'
			else:C+='x0,'
		else:C+=str(B[A])+','
	E=str(base64.b64encode(C.encode('ascii'))).replace("b'",'').replace("'",'');F=[]
	for G in range(0,len(E),4):F.append(E[G:G+4])
	def K(s_list):return[[len(list(B)),A]for(A,B)in groupby(s_list)]
	H=''
	for A in K(F):H+='|'+str(A[0])+':'+A[1]
	return H
def decrypt_setting_string(encrypted_string):
	'Take an encrypted string and return a dictionary.\n\n    Args:\n        encrypted_string (str): Passed settings string.\n\n    Returns:\n        dict: Returns the decrypted set of data.\n    ';J=' ';I=False;F=''
	for A in encrypted_string.split('|'):
		if A:
			if':'in A:K,L=A.split(':');F+=L*int(K)
			else:F+=A
	G={};B=0;H=I;C=[];D=collections.OrderedDict(sorted(default_dict.items()))
	for A in base64.b64decode(F).decode('ascii').split(','):
		if'['in A:H=True;str=A.replace('[','').replace("'",'').replace(J,'');C.append(str)
		elif']'in A:H=I;str=A.replace(']','').replace("'",'').replace(J,'');C.append(str);G[list(D.items())[B][0]]=C;B+=1;C=[]
		elif H:str=A.replace("'",'').replace(J,'');C.append(str)
		else:
			if B<len(list(D.items())):
				if A=='x1':E=True
				elif A=='x0':E=I
				elif A=='':E=list(D.items())[B][1]
				else:E=A
				G[list(D.items())[B][0]]=E
			B+=1
	return G
resp=js.getFile('./static/presets/default.json')
default_dict=json.loads(resp)