'Generate UI elements via jinja2 to display on page load.'
import json,micropip
from jinja2 import Environment,FunctionLoader
import time,js
from js import document
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';G='settings=';B=js.window.location.origin;await micropip.install(f"{B}/static/py_libraries/pyodide_importer-0.0.2-py2.py3-none-any.whl")
	if js.location.hostname in['dev.dk64randomizer.com','dk64randomizer.com']:await micropip.install(f"{B}/static/py_libraries/dk64rando-web-py3-none-any.whl")
	await micropip.install('pillow');from pyodide_importer import register_hook as H
	try:H('/')
	except Exception:pass
	js.listeners=[];js.progression_presets=[];js.background_worker=None
	def A(file):A=js.getFile(file);return A
	def I(template_name):B=int(round(time.time()*1000));return A('templates/'+f"{template_name}?currtime={B}")
	J=int(round(time.time()*1000))
	for K in json.loads(A(f"static/presets/preset_files.json?currtime={J}")).get('progression'):js.progression_presets.append(json.loads(A('static/presets/'+K)))
	js.pointer_addresses=json.loads(js.getFile('./static/patches/pointer_addresses.json'));L=Environment(loader=FunctionLoader(I),enable_async=True);M=L.get_template('base.html.jinja2');N=await M.render();js.document.documentElement.innerHTML='';js.document.open();js.document.write(N);js.document.close()
	try:
		C=document.cookie
		if C:
			for D in C.split(';'):
				if G in D:O=str(D).replace(G,'');break
			E=json.loads(O)
			for F in E:
				try:document.getElementById(F).value=E[F]
				except Exception:pass
	except Exception:pass
initialize()