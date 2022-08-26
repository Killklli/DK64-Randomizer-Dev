'Generate UI elements via jinja2 to display on page load.'
import time,micropip
from jinja2 import Environment,FunctionLoader
import js
async def initialize():
	'Shifted code into an async function so we can properly lint await calls.';A=js.window.location.origin;await micropip.install([f"{A}/static/py_libraries/charset_normalizer-2.1.0-py3-none-any.whl",f"{A}/static/py_libraries/urllib3-1.26.11-py2.py3-none-any.whl",f"{A}/static/py_libraries/certifi-2022.6.15-py3-none-any.whl",f"{A}/static/py_libraries/idna-3.3-py3-none-any.whl",f"{A}/static/py_libraries/requests-2.28.1-py3-none-any.whl",f"{A}/static/py_libraries/pyodide_importer-0.0.2-py2.py3-none-any.whl"],deps=False);from pyodide_importer import register_hook as B
	try:B('/')
	except Exception:pass
	import version as C;js.listeners=[];js.progression_presets=[];js.background_worker=None
	def D(file):A=js.getFile(file);return A
	def E(template_name):A=int(round(time.time()*1000));return D('templates/'+f"{template_name}?currtime={A}")
	F=Environment(loader=FunctionLoader(E),enable_async=True);G=F.get_template('frontpage.html.jinja2');H=await G.render(version=C);js.document.documentElement.innerHTML='';js.document.open();js.document.write(H);js.document.close()
initialize()