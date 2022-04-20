'Generate UI elements via jinja2 to display on page load.'
import json,micropip
from jinja2 import Environment,FunctionLoader
from pyodide import to_js
import js
from js import document
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';I='settings=';H=False;G='async';F='url';await micropip.install('pyodide-importer');await micropip.install('pillow');from pyodide_importer import register_hook as J
	try:J('/')
	except Exception:pass
	js.listeners=[];js.progression_presets=[];js.background_worker=None
	def A(file):A=js.jquery.ajax(js.Object.fromEntries(to_js({'type':'GET',F:file,G:H}))).responseText;return A
	def K(template_name):return A('templates/'+template_name)
	for L in json.loads(A('static/presets/preset_files.json')).get('progression'):js.progression_presets.append(json.loads(A('static/presets/'+L)))
	M=Environment(loader=FunctionLoader(K),enable_async=True);N=M.get_template('base.html.jinja2');O=await N.render();js.document.documentElement.innerHTML='';js.document.open();js.document.write(O);js.document.close()
	try:
		B=document.cookie
		if B:
			for C in B.split(';'):
				if I in C:P=str(C).replace(I,'');break
			D=json.loads(P)
			for E in D:
				try:document.getElementById(E).value=D[E]
				except Exception:pass
	except Exception:pass
	js.pointer_addresses=json.loads(js.jquery.ajax(js.Object.fromEntries(to_js({F:'./static/patches/pointer_addresses.json',G:H}))).responseText)
initialize()