'CLI script for running seed generation.'
import argparse,codecs,json,pickle,random,sys
from randomizer.Fill import Generate_Spoiler
from randomizer.Settings import Settings
from randomizer.SettingStrings import decrypt_setting_string
from randomizer.Spoiler import Spoiler
def generate(generate_settings,file_name):
	'Gen a seed and write the file to an output file.';B=Settings(generate_settings);A=Spoiler(B);Generate_Spoiler(A);C=codecs.encode(pickle.dumps(A),'base64').decode()
	with open(file_name,'w')as D:D.write(C)
def main():
	'CLI Entrypoint for generating seeds.';J='seed';I='name';F=None;D=False;C=argparse.ArgumentParser();C.add_argument('--settings_string',help='The settings string to use to generate a seed',required=D);C.add_argument('--preset',help='Preset to use',required=D);C.add_argument('--output',help='File to name patch file',required=True);C.add_argument('--seed',help='Seed ID to use',required=D);A=C.parse_args()
	if A.settings_string is not F:
		decrypt_setting_string(A.settings_string)
		try:B=decrypt_setting_string(A.settings_string)
		except Exception:print('Invalid settings String');sys.exit(2)
	elif A.preset is not F:
		K=json.load(open('static/presets/preset_files.json'));L=json.load(open('static/presets/default.json'));G=D
		for M in K.get('progression'):
			with open('static/presets/'+M,'r')as N:
				E=json.load(N)
				if A.preset==E.get(I):
					B=L
					for H in E:B[H]=E[H]
					B.pop(I);B.pop('description');G=True
		if G is D:sys.exit(2)
	if A.seed is not F:B[J]=A.seed
	else:B[J]=random.randint(0,100000000)
	generate(B,A.output)
if __name__=='__main__':main()