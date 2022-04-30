'Generate UI elements via jinja2 to display on page load.'
import json,micropip
from jinja2 import Environment,FunctionLoader
from pyodide import to_js
import time,js
from js import document
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';I='settings=';H=False;G='async';F='url';J=js.window.location.origin;await micropip.install(f"{J}/static/py_libraries/pyodide_importer-0.0.2-py2.py3-none-any.whl");await micropip.install('pillow');from pyodide_importer import register_hook as K
	try:K('/')
	except Exception:pass
	js.listeners=[];js.progression_presets=[];js.background_worker=None
	def A(file):A=js.jquery.ajax(js.Object.fromEntries(to_js({'type':'GET',F:file,G:H}))).responseText;return A
	def L(template_name):B=int(round(time.time()*1000));return A('templates/'+f"{template_name}?currtime={B}")
	M=int(round(time.time()*1000))
	for N in json.loads(A(f"static/presets/preset_files.json?currtime={M}")).get('progression'):js.progression_presets.append(json.loads(A('static/presets/'+N)))
	O=Environment(loader=FunctionLoader(L),enable_async=True);P=O.get_template('base.html.jinja2');Q=await P.render();js.document.documentElement.innerHTML='';js.document.open();js.document.write(Q);js.document.close()
	try:
		B=document.cookie
		if B:
			for C in B.split(';'):
				if I in C:R=str(C).replace(I,'');break
			D=json.loads(R)
			for E in D:
				try:document.getElementById(E).value=D[E]
				except Exception:pass
	except Exception:pass
	js.pointer_addresses=json.loads(js.jquery.ajax(js.Object.fromEntries(to_js({F:'./static/patches/pointer_addresses.json',G:H}))).responseText)
initialize()