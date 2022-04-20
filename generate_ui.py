'Generate UI elements via jinja2 to display on page load.'
import micropip
from jinja2 import Environment,FunctionLoader
from pyodide import to_js
import js
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';await micropip.install('pyodide-importer');from pyodide_importer import register_hook as A
	try:A('/')
	except Exception:pass
	import version as B;js.listeners=[];js.progression_presets=[];js.background_worker=None
	def C(file):A=js.jquery.ajax(js.Object.fromEntries(to_js({'type':'GET','url':file,'async':False}))).responseText;return A
	def D(template_name):return C('templates/'+template_name)
	E=Environment(loader=FunctionLoader(D),enable_async=True);F=E.get_template('frontpage.html.jinja2');G=await F.render(version=B);js.document.documentElement.innerHTML='';js.document.open();js.document.write(G);js.document.close()
initialize()