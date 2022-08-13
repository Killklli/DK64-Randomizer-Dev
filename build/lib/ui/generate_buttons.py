'File containing main UI button events that travel between tabs.'
_K='download_patch_file'
_J='generate_seed'
_I='is-valid'
_H=True
_G='is-invalid'
_F='disabled'
_E=False
_D='patchfileloader'
_C='click'
_B=None
_A='input-file-rom'
import asyncio,json,random,js
from randomizer.BackgroundRandomizer import generate_playthrough
from randomizer.Patching.ApplyRandomizer import patching_response
from randomizer.Worker import background
from ui.bindings import bind
from ui.progress_bar import ProgressBar
from ui.settings_strings import encrypt_settings_string,decrypt_setting_string
from ui.rando_options import toggle_counts_boxes,toggle_b_locker_boxes,update_boss_required,disable_colors,disable_music,disable_prices,max_randomized_blocker,max_randomized_troff,disable_barrel_rando,disable_boss_rando,hide_rgb,toggle_medals_box,max_randomized_medals,disable_rw
from pyodide import create_proxy
@bind(_C,'export_settings')
def export_settings_string(event):'Click event for exporting settings to a string.\n\n    Args:\n        event (event): Javascript event object.\n    ';A=serialize_settings();B=encrypt_settings_string(A);js.settings_string.value=B
@bind(_C,'import_settings')
def import_settings_string(event):
	'Click event for importing settings from a string.\n\n    Args:\n        event (event): Javascript Event object.\n    ';C=js.settings_string.value
	try:
		B=decrypt_setting_string(C)
		for A in B:
			try:
				if type(B[A])is bool:
					if B[A]is _E:js.jq(f"#{A}").checked=_E;js.document.getElementsByName(A)[0].checked=_E
					else:js.jq(f"#{A}").checked=_H;js.document.getElementsByName(A)[0].checked=_H
					js.jq(f"#{A}").removeAttr(_F)
				else:
					if js.document.getElementsByName(A)[0].hasAttribute('data-slider-value'):js.jq(f"#{A}").slider('setValue',B[A]);js.jq(f"#{A}").slider('enable');js.jq(f"#{A}").parent().find('.slider-disabled').removeClass('slider-disabled')
					else:js.jq(f"#{A}").val(B[A])
					js.jq(f"#{A}").removeAttr(_F)
			except Exception as D:pass
		toggle_counts_boxes(_B);toggle_b_locker_boxes(_B);update_boss_required(_B);disable_colors(_B);disable_music(_B);disable_prices(_B);max_randomized_blocker(_B);max_randomized_troff(_B);disable_barrel_rando(_B)
	except Exception:pass
@bind('change',_D)
def lanky_file_changed(event):
	'On the event of a lanky file being loaded.\n\n    Args:\n        event (event): Javascript event.\n    '
	def C(e):A=str(e.target.result);js.document.getElementById(_D).classList.add(_I);js.loaded_patch=A
	A=_B
	for D in js.document.getElementById(_D).files:A=D;break
	B=js.FileReader.new()
	if A is not _B:B.readAsText(A);E=create_proxy(C);B.addEventListener('load',E)
@bind(_C,'generate_lanky_seed')
def generate_seed_from_patch(event):
	'Generate a seed from a patch file.'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _I not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _G not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_G)
	elif len(str(js.document.getElementById(_D).value).strip())==0:
		js.document.getElementById(_D).select()
		if _G not in list(js.document.getElementById(_D).classList):js.document.getElementById(_D).classList.add(_G)
	else:js.apply_bps_javascript();patching_response(str(js.loaded_patch))
def serialize_settings():
	'Serialize form settings into a JSON string.\n\n    Returns:\n        dict: Dictionary of form settings.\n    ';E='input';D=[]
	for A in js.document.getElementsByTagName(E):
		if A.disabled:D.append(A);A.removeAttribute(_F)
	for A in js.document.getElementsByTagName('select'):
		if A.disabled:D.append(A);A.removeAttribute(_F)
	F=js.jquery('#form').serializeArray();C={}
	def G(s):
		'Check if a string is a number or not.'
		try:int(s);return _H
		except ValueError:pass
	for B in F:
		if B.value.lower()in['true','false']:C[B.name]=bool(B.value)
		elif G(B.value):C[B.name]=int(B.value)
		else:C[B.name]=B.value
	for A in js.document.getElementsByTagName(E):
		if A.type=='checkbox'and not A.checked:
			if not C.get(A.name):C[A.name]=_E
	for A in D:A.setAttribute(_F,_F)
	return C
@bind(_C,_J)
def generate_seed(event):
	'Generate a seed based off the current settings.\n\n    Args:\n        event (event): Javascript click event.\n    ';D="'''";C='seed'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _I not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _G not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_G)
	else:
		B=asyncio.get_event_loop();B.run_until_complete(ProgressBar().update_progress(0,'Initalizing'));A=serialize_settings()
		if not A.get(C):A[C]=str(random.randint(100000,999999))
		js.apply_bps_javascript();B.run_until_complete(ProgressBar().update_progress(2,'Randomizing, this may take some time depending on settings.'));background(generate_playthrough,[D+json.dumps(A)+D],patching_response)
@bind(_C,_K)
def update_seed_text(event):
	'Set seed text based on the download_patch_file click event.\n\n    Args:\n        event (DOMEvent): Javascript dom click event.\n    '
	if js.document.getElementById(_K).checked:js.document.getElementById(_J).value='Generate Patch File and Seed'
	else:js.document.getElementById(_J).value='Generate Seed'
@bind(_C,'nav-seed-gen-tab')
@bind(_C,'nav-patch-tab')
def disable_input(event):
	'Disable input for the ROM Boxes as we rotate through the navbar.\n\n    Args:\n        event (DOMEvent): DOM item that triggered the event.\n    ';B='input-file-rom_1';A='input-file-rom_2';C=_E
	try:
		if'patch-tab'in event.target.id:C=_H
	except Exception:pass
	if C is _E:
		if not js.document.getElementById(A):
			try:js.document.getElementById(_A).id=A
			except Exception:pass
		try:js.document.getElementById(B).id=_A
		except Exception:pass
	else:
		if not js.document.getElementById(B):
			try:js.document.getElementById(_A).id=B
			except Exception:pass
		try:js.document.getElementById(A).id=_A
		except Exception:pass