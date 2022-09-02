'File containing main UI button events that travel between tabs.'
_J='download_patch_file'
_I='generate_seed'
_H='is-valid'
_G=False
_F='disabled'
_E='click'
_D='patchfileloader'
_C='is-invalid'
_B=None
_A='rom'
import asyncio,json,random
from pyodide import create_proxy
import js
from randomizer.BackgroundRandomizer import generate_playthrough
from randomizer.Patching.ApplyRandomizer import patching_response
from randomizer.SettingStrings import decrypt_setting_string,encrypt_settings_string
from randomizer.Worker import background
from ui.bindings import bind
from ui.progress_bar import ProgressBar
from ui.rando_options import disable_barrel_modal,disable_colors,disable_music,disable_prices,max_randomized_blocker,max_randomized_troff,toggle_b_locker_boxes,toggle_counts_boxes,update_boss_required
@bind(_E,'export_settings')
def export_settings_string(event):'Click event for exporting settings to a string.\n\n    Args:\n        event (event): Javascript event object.\n    ';A=serialize_settings();B=encrypt_settings_string(A);js.settings_string.value=B
@bind(_E,'import_settings')
def import_settings_string(event):
	'Click event for importing settings from a string.\n\n    Args:\n        event (event): Javascript Event object.\n    ';E=js.settings_string.value
	try:
		B=decrypt_setting_string(E)
		for A in B:
			try:
				if type(B[A])is bool:
					if B[A]is _G:js.jq(f"#{A}").checked=_G;js.document.getElementsByName(A)[0].checked=_G
					else:js.jq(f"#{A}").checked=True;js.document.getElementsByName(A)[0].checked=True
					js.jq(f"#{A}").removeAttr(_F)
				elif type(B[A])is list:
					C=js.document.getElementById(A)
					for D in range(0,C.options.length):C.item(D).selected=C.item(D).value in B[A]
				else:
					if js.document.getElementsByName(A)[0].hasAttribute('data-slider-value'):js.jq(f"#{A}").slider('setValue',B[A]);js.jq(f"#{A}").slider('enable');js.jq(f"#{A}").parent().find('.slider-disabled').removeClass('slider-disabled')
					else:js.jq(f"#{A}").val(B[A])
					js.jq(f"#{A}").removeAttr(_F)
			except Exception as F:pass
		toggle_counts_boxes(_B);toggle_b_locker_boxes(_B);update_boss_required(_B);disable_colors(_B);disable_music(_B);disable_prices(_B);max_randomized_blocker(_B);max_randomized_troff(_B);disable_barrel_modal(_B)
	except Exception:pass
@bind('change',_D)
def lanky_file_changed(event):
	'On the event of a lanky file being loaded.\n\n    Args:\n        event (event): Javascript event.\n    '
	def C(e):A=str(e.target.result);js.document.getElementById(_D).classList.add(_H);js.loaded_patch=A
	A=_B
	for D in js.document.getElementById(_D).files:A=D;break
	B=js.FileReader.new()
	if A is not _B:B.readAsText(A);E=create_proxy(C);B.addEventListener('load',E)
@bind(_E,'generate_pastgen_seed')
def generate_previous_seed(event):
	'Generate a seed from a previous seed file.'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _H not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _C not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_C)
	else:A=asyncio.get_event_loop();A.run_until_complete(ProgressBar().update_progress(0,'Loading Previous seed and applying data.'));js.apply_bps_javascript();patching_response(str(js.get_previous_seed_data()))
@bind(_E,'generate_lanky_seed')
def generate_seed_from_patch(event):
	'Generate a seed from a patch file.'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _H not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _C not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_C)
	elif len(str(js.document.getElementById(_D).value).strip())==0:
		js.document.getElementById(_D).select()
		if _C not in list(js.document.getElementById(_D).classList):js.document.getElementById(_D).classList.add(_C)
	else:js.apply_bps_javascript();patching_response(str(js.loaded_patch))
def serialize_settings():
	'Serialize form settings into a JSON string.\n\n    Returns:\n        dict: Dictionary of form settings.\n    ';H='select';G='input';D=[]
	for A in js.document.getElementsByTagName(G):
		if A.disabled:D.append(A);A.removeAttribute(_F)
	for A in js.document.getElementsByTagName(H):
		if A.disabled:D.append(A);A.removeAttribute(_F)
	I=js.jquery('#form').serializeArray();C={}
	def J(s):
		'Check if a string is a number or not.'
		try:int(s);return True
		except ValueError:pass
	for B in I:
		if B.value.lower()in['true','false']:C[B.name]=bool(B.value)
		elif J(B.value):C[B.name]=int(B.value)
		else:C[B.name]=B.value
	for A in js.document.getElementsByTagName(G):
		if A.type=='checkbox'and not A.checked:
			if not C.get(A.name):C[A.name]=_G
	for A in D:A.setAttribute(_F,_F)
	for A in js.document.getElementsByTagName(H):
		if'selected'in A.className:
			K=A.options.length;E=[]
			for F in range(0,K):
				if A.options.item(F).selected:E.append(A.options.item(F).value)
			C[A.getAttribute('name')]=E
	return C
@bind(_E,_I)
def generate_seed(event):
	'Generate a seed based off the current settings.\n\n    Args:\n        event (event): Javascript click event.\n    ';D="'''";C='seed'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _H not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _C not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_C)
	else:
		B=asyncio.get_event_loop();B.run_until_complete(ProgressBar().update_progress(0,'Initalizing'));A=serialize_settings()
		if not A.get(C):A[C]=str(random.randint(100000,999999))
		js.apply_bps_javascript();B.run_until_complete(ProgressBar().update_progress(2,'Randomizing, this may take some time depending on settings.'));background(generate_playthrough,[D+json.dumps(A)+D],patching_response)
@bind(_E,_J)
def update_seed_text(event):
	'Set seed text based on the download_patch_file click event.\n\n    Args:\n        event (DOMEvent): Javascript dom click event.\n    '
	if js.document.getElementById(_J).checked:js.document.getElementById(_I).value='Generate Patch File and Seed'
	else:js.document.getElementById(_I).value='Generate Seed'