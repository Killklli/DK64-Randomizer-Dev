'Generate Playthrough from the logic core.'
import codecs,json,pickle,random,traceback
from randomizer.Fill import Generate_Spoiler
from randomizer.Settings import Settings
from randomizer.Spoiler import Spoiler
def generate_playthrough(form_string):
	'Trigger a generation of the playthrough in a webworker.\n\n    Args:\n        form_string (str): The form data as json submitted.\n\n    Returns:\n        str: The Json data as a string.\n    '
	try:A=json.loads(form_string);random.seed(A.get('seed'));C=Settings(A);B=Spoiler(C);Generate_Spoiler(B);return codecs.encode(pickle.dumps(B),'base64').decode()
	except Exception as D:print('error: '+traceback.format_exc());return json.dumps({'error':str(traceback.format_exc())})