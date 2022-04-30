'File containing main UI button events that travel between tabs.'
_H='download_patch_file'
_G='generate_seed'
_F=False
_E='is-valid'
_D='click'
_C='is-invalid'
_B='patchfileloader'
_A='input-file-rom'
import json,random,js
from randomizer.Patching.ApplyRandomizer import patching_response
from randomizer.BackgroundRandomizer import generate_playthrough
from randomizer.Worker import background
from ui.bindings import bind
from ui.progress_bar import ProgressBar
@bind('change',_B)
def lanky_file_changed(event):
	'On the event of a lanky file being loaded.\n\n    Args:\n        event (event): Javascript event.\n    '
	def C(e):A=str(e.target.result);js.document.getElementById(_B).classList.add(_E);js.loaded_patch=A
	A=None
	for D in js.document.getElementById(_B).files:A=D;break
	B=js.FileReader.new()
	if A is not None:B.readAsText(A);B.addEventListener('load',C)
@bind(_D,'generate_lanky_seed')
def generate_seed_from_patch(event):
	'Generate a seed from a patch file.'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _E not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _C not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_C)
	elif len(str(js.document.getElementById(_B).value).strip())==0:
		js.document.getElementById(_B).select()
		if _C not in list(js.document.getElementById(_B).classList):js.document.getElementById(_B).classList.add(_C)
	else:patching_response(str(js.loaded_patch))
@bind(_D,_G)
def generate_seed(event):
	'Generate a seed based off the current settings.\n\n    Args:\n        event (event): Javascript click event.\n    ';H="'''";G='seed';F='input';D='disabled'
	if len(str(js.document.getElementById(_A).value).strip())==0 or _E not in list(js.document.getElementById(_A).classList):
		js.document.getElementById(_A).select()
		if _C not in list(js.document.getElementById(_A).classList):js.document.getElementById(_A).classList.add(_C)
	else:
		ProgressBar().update_progress(0,'Initalizing');E=[]
		for A in js.document.getElementsByTagName(F):
			if A.disabled:E.append(A);A.removeAttribute(D)
		for A in js.document.getElementsByTagName('select'):
			if A.disabled:E.append(A);A.removeAttribute(D)
		I=js.jquery('#form').serializeArray();B={}
		def J(s):
			'Check if a string is a number or not.'
			try:int(s);return True
			except ValueError:pass
		for C in I:
			if C.value.lower()in['true','false']:B[C.name]=bool(C.value)
			elif J(C.value):B[C.name]=int(C.value)
			else:B[C.name]=C.value
		for A in js.document.getElementsByTagName(F):
			if A.type=='checkbox'and not A.checked:
				if not B.get(A.name):B[A.name]=_F
		for A in E:A.setAttribute(D,D)
		if not B.get(G):B[G]=str(random.randint(100000,999999))
		ProgressBar().update_progress(2,'Randomizing, this may take some time depending on settings.');background(generate_playthrough,[H+json.dumps(B)+H],patching_response)
@bind(_D,_H)
def update_seed_text(event):
	'Set seed text based on the download_patch_file click event.\n\n    Args:\n        event (DOMEvent): Javascript dom click event.\n    '
	if js.document.getElementById(_H).checked:js.document.getElementById(_G).value='Generate Patch File and Seed'
	else:js.document.getElementById(_G).value='Generate Seed'
@bind(_D,'nav-seed-gen-tab')
@bind(_D,'nav-patch-tab')
def disable_input(event):
	'Disable input for the ROM Boxes as we rotate through the navbar.\n\n    Args:\n        event (DOMEvent): DOM item that triggered the event.\n    ';B='input-file-rom_1';A='input-file-rom_2';C=_F
	try:
		if'patch-tab'in event.target.id:C=True
	except Exception:pass
	if C is _F:
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