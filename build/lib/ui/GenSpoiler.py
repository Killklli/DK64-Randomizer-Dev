'Push jinja2 file to spoiler.'
from jinja2 import Environment,FunctionLoader
import js,json,time
def ajax_call(file):'Get file.';A=js.getFile(file);return A
def loader_func(template_name):'Load template file.';A=int(round(time.time()*1000));return ajax_call('templates/'+f"{template_name}?currtime={A}")
async def GenerateSpoiler(spoiler):
	'Pass spoiler to jinja2 file and modify DOM with rendered jinja2 file.';F='spoiler_log_text';E='Settings';C=spoiler;G=Environment(loader=FunctionLoader(loader_func),enable_async=True);H=G.get_template('spoiler.html.jinja2');D=''
	for I in C.split('\n'):D+=I.strip()
	A=json.loads(D);B='none'
	if A[E]['Loading Zones Shuffled']=='all':
		if A[E]['Decoupled Loading Zones']is False:B='coupled'
		else:B='decoupled'
	J=await H.render(spoiler=A,lzr_type=B);js.document.getElementById(F).value=C;js.document.getElementById(F).innerHTML=J