'File containing main UI button events that travel between tabs.'
_J='download_patch_file'
_I='generate_seed'
_H='is-valid'
_G=False
_F='click'
_E='is-invalid'
_D='disabled'
_C='patchfileloader'
_B='rom'
_A=None
import asyncio,json,random,js
from randomizer.BackgroundRandomizer import generate_playthrough
from randomizer.Patching.ApplyRandomizer import patching_response
from randomizer.Worker import background
from ui.bindings import bind
from ui.progress_bar import ProgressBar
from ui.settings_strings import encrypt_settings_string,decrypt_setting_string
from ui.rando_options import toggle_counts_boxes,toggle_b_locker_boxes,update_boss_required,disable_colors,disable_music,disable_prices,max_randomized_blocker,max_randomized_troff,disable_barrel_rando
from pyodide import create_proxy
@bind(_F,'export_settings')
def export_settings_string(event):'Click event for exporting settings to a string.\n\n    Args:\n        event (event): Javascript event object.\n    ';A=serialize_settings();B=encrypt_settings_string(A);js.settings_string.value=B
@bind(_F,'import_settings')
def import_settings_string(event):
	'Click event for importing settings from a string.\n\n    Args:\n        event (event): Javascript Event object.\n    ';C=js.settings_string.value
	try:
		B=decrypt_setting_string(C)
		for A in B:
			try:
				if type(B[A])is bool:
					if B[A]is _G:js.jq(f"#{A}").checked=_G;js.document.getElementsByName(A)[0].checked=_G
					else:js.jq(f"#{A}").checked=True;js.document.getElementsByName(A)[0].checked=True
					js.jq(f"#{A}").removeAttr(_D)
				else:
					if js.document.getElementsByName(A)[0].hasAttribute('data-slider-value'):js.jq(f"#{A}").slider('setValue',B[A]);js.jq(f"#{A}").slider('enable');js.jq(f"#{A}").parent().find('.slider-disabled').removeClass('slider-disabled')
					else:js.jq(f"#{A}").val(B[A])
					js.jq(f"#{A}").removeAttr(_D)
			except Exception as D:pass
		toggle_counts_boxes(_A);toggle_b_locker_boxes(_A);update_boss_required(_A);disable_colors(_A);disable_music(_A);disable_prices(_A);max_randomized_blocker(_A);max_randomized_troff(_A);disable_barrel_rando(_A)
	except Exception:pass
@bind('change',_C)
def lanky_file_changed(event):
	'On the event of a lanky file being loaded.\n\n    Args:\n        event (event): Javascript event.\n    '
	def C(e):A=str(e.target.result);js.document.getElementById(_C).classList.add(_H);js.loaded_patch=A
	A=_A
	for D in js.document.getElementById(_C).files:A=D;break
	B=js.FileReader.new()
	if A is not _A:B.readAsText(A);E=create_proxy(C);B.addEventListener('load',E)
@bind(_F,'generate_lanky_seed')
def generate_seed_from_patch(event):
	'Generate a seed from a patch file.'
	if len(str(js.document.getElementById(_B).value).strip())==0 or _H not in list(js.document.getElementById(_B).classList):
		js.document.getElementById(_B).select()
		if _E not in list(js.document.getElementById(_B).classList):js.document.getElementById(_B).classList.add(_E)
	elif len(str(js.document.getElementById(_C).value).strip())==0:
		js.document.getElementById(_C).select()
		if _E not in list(js.document.getElementById(_C).classList):js.document.getElementById(_C).classList.add(_E)
	else:js.apply_bps_javascript();patching_response(str(js.loaded_patch))
def serialize_settings():
	'Serialize form settings into a JSON string.\n\n    Returns:\n        dict: Dictionary of form settings.\n    ';E='input';D=[]
	for A in js.document.getElementsByTagName(E):
		if A.disabled:D.append(A);A.removeAttribute(_D)
	for A in js.document.getElementsByTagName('select'):
		if A.disabled:D.append(A);A.removeAttribute(_D)
	F=js.jquery('#form').serializeArray();C={}
	def G(s):
		'Check if a string is a number or not.'
		try:int(s);return True
		except ValueError:pass
	for B in F:
		if B.value.lower()in['true','false']:C[B.name]=bool(B.value)
		elif G(B.value):C[B.name]=int(B.value)
		else:C[B.name]=B.value
	for A in js.document.getElementsByTagName(E):
		if A.type=='checkbox'and not A.checked:
			if not C.get(A.name):C[A.name]=_G
	for A in D:A.setAttribute(_D,_D)
	return C
@bind(_F,_I)
def generate_seed(event):
	'Generate a seed based off the current settings.\n\n    Args:\n        event (event): Javascript click event.\n    ';D="'''";C='seed'
	if len(str(js.document.getElementById(_B).value).strip())==0 or _H not in list(js.document.getElementById(_B).classList):
		js.document.getElementById(_B).select()
		if _E not in list(js.document.getElementById(_B).classList):js.document.getElementById(_B).classList.add(_E)
	else:
		B=asyncio.get_event_loop();B.run_until_complete(ProgressBar().update_progress(0,'Initalizing'));A=serialize_settings()
		if not A.get(C):A[C]=str(random.randint(100000,999999))
		js.apply_bps_javascript();B.run_until_complete(ProgressBar().update_progress(2,'Randomizing, this may take some time depending on settings.'));background(generate_playthrough,[D+json.dumps(A)+D],patching_response)
@bind(_F,_J)
def update_seed_text(event):
	'Set seed text based on the download_patch_file click event.\n\n    Args:\n        event (DOMEvent): Javascript dom click event.\n    '
	if js.document.getElementById(_J).checked:js.document.getElementById(_I).value='Generate Patch File and Seed'
	else:js.document.getElementById(_I).value='Generate Seed'