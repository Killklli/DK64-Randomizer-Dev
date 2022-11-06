'Generate UI elements via jinja2 to display on page load.'
import json,time,micropip
from jinja2 import Environment,FunctionLoader
import js
from js import document
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';G='settings=';A=js.window.location.origin;await micropip.install([f"{A}/static/py_libraries/charset_normalizer-2.1.0-py3-none-any.whl",f"{A}/static/py_libraries/urllib3-1.26.11-py2.py3-none-any.whl",f"{A}/static/py_libraries/certifi-2022.6.15-py3-none-any.whl",f"{A}/static/py_libraries/idna-3.3-py3-none-any.whl",f"{A}/static/py_libraries/requests-2.28.1-py3-none-any.whl",f"{A}/static/py_libraries/pyodide_importer-0.0.2-py2.py3-none-any.whl",'pillow'],deps=False)
	if js.location.hostname in['dev.dk64randomizer.com','dk64randomizer.com']:await micropip.install(f"{A}/static/py_libraries/dk64rando-1.0.0-py3-none-any.whl")
	from pyodide_importer import register_hook as H
	try:H('/')
	except Exception:pass
	from randomizer.Lists.Minigame import MinigameSelector as I;from randomizer.Lists.QoL import QoLSelector as J;from randomizer.Lists.EnemyTypes import EnemySelector as K;from randomizer.Enums.Types import ItemRandoSelector as L,KeySelector as M;js.listeners=[];js.progression_presets=[];js.background_worker=None
	def B(file):A=js.getFile(file);return A
	def N(template_name):A=int(round(time.time()*1000));return B('templates/'+f"{template_name}?currtime={A}")
	O=int(round(time.time()*1000))
	for P in json.loads(B(f"static/presets/preset_files.json?currtime={O}")).get('progression'):js.progression_presets.append(json.loads(B('static/presets/'+P)))
	js.pointer_addresses=json.loads(js.getFile('./static/patches/pointer_addresses.json'));Q=Environment(loader=FunctionLoader(N),enable_async=True);R=Q.get_template('base.html.jinja2');S=await R.render(minigames=I,misc_changes=J,enemies=K,itemRando=L,keys=M);js.document.documentElement.innerHTML='';js.document.open();js.document.write(S);js.document.close()
	try:
		C=document.cookie
		if C:
			for D in C.split(';'):
				if G in D:T=str(D).replace(G,'');break
			E=json.loads(T)
			for F in E:
				try:document.getElementById(F).value=E[F]
				except Exception:pass
	except Exception:pass
initialize()