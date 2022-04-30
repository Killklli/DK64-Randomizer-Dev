'Generate UI elements via jinja2 to display on page load.'
import micropip
from jinja2 import Environment,FunctionLoader
from pyodide import to_js
import time,js
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';A=js.window.location.origin;await micropip.install(f"{A}/static/py_libraries/pyodide_importer-0.0.2-py2.py3-none-any.whl");from pyodide_importer import register_hook as B
	try:B('/')
	except Exception:pass
	import version as C;js.listeners=[];js.progression_presets=[];js.background_worker=None
	def D(file):A=js.jquery.ajax(js.Object.fromEntries(to_js({'type':'GET','url':file,'async':False}))).responseText;return A
	def E(template_name):A=int(round(time.time()*1000));return D('templates/'+f"{template_name}?currtime={A}")
	F=Environment(loader=FunctionLoader(E),enable_async=True);G=F.get_template('frontpage.html.jinja2');H=await G.render(version=C);js.document.documentElement.innerHTML='';js.document.open();js.document.write(H);js.document.close()
initialize()