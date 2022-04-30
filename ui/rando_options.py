'Options for the main rando tab.'
_N='level_randomization'
_M='randomize_cb_required_amounts'
_L='unlock_all_kongs'
_K='randomize_blocker_required_amounts'
_J='change'
_I='keydown'
_H='troff_'
_G='blocker_'
_F='click'
_E='presets'
_D='name'
_C=True
_B=False
_A='disabled'
import random,js
from js import document
from ui.bindings import bind
def randomseed(evt):'Randomly generate a seed ID.';document.getElementById('seed').value=str(random.randint(100000,999999))
@bind('input',_G,8)
@bind('input',_H,8)
def on_input(event):
	'Limits inputs from input boxes on keypress.\n\n    Args:\n        event (domevent): The DOMEvent data.\n\n    Returns:\n        bool: False if we need to stop the event.\n    ';A=event
	if'troff'in A.target.id:min_max(A,0,500)
	elif'blocker'in A.target.id:min_max(A,0,200)
def min_max(event,min,max):
	'Check if the data is within bounds of requirements.\n\n    Args:\n        event (DomEvent): The doms event.\n        min (int): Minimum Value to keep.\n        max (int): Maximum value to allow.\n\n    Returns:\n        bool: Deny or Success for Handled\n    ';A=event
	try:
		if int(A.target.value)>=max:A.preventDefault();document.getElementById(A.target.id).value=max
		elif int(A.target.value)<=min:A.preventDefault();document.getElementById(A.target.id).value=min
		else:document.getElementById(A.target.id).value=str(A.target.value)
	except Exception:A.preventDefault();document.getElementById(A.target.id).value=min
@bind(_I,_G,8)
@bind(_I,_H,8)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';C=document.getElementById(_E);D=[]
	for E in C.children:D.append(E.value)
	for A in js.progression_presets:
		if A.get(_D)not in D:B=document.createElement('option');B.value=A.get(_D);B.innerHTML=A.get(_D);B.title=A.get('description');C.appendChild(B)
	js.jq('#presets').val('Suggested');toggle_counts_boxes(None);toggle_b_locker_boxes(None);js.load_cookies()
@bind(_J,_E)
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';C='checked';E=document.getElementById(_E);B=None
	for D in js.progression_presets:
		if D.get(_D)==E.value:B=D
	for A in B:
		try:
			if type(B[A])is bool:
				if B[A]is _B:document.getElementsByName(A)[0].removeAttribute(C)
				else:document.getElementsByName(A)[0].setAttribute(C,C)
			else:js.jq(f"#{A}").val(B[A])
		except Exception as F:pass
@bind(_F,_K)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_C
	if js.document.getElementById(_K).checked:A=_B
	for C in range(0,10):
		B=js.document.getElementById(f"blocker_{C}")
		try:
			if A:B.removeAttribute(_A)
			else:B.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_F,_L)
def unlock_kongs_toggle(event):
	'Toggle the textboxes for unlock_all_kongs.';A='kong_rando';B=_B
	if js.document.getElementById(_L).checked:B=_C
	if B:js.document.getElementById(A).setAttribute(_A,_A);js.document.getElementById(A).checked=_B
	else:js.document.getElementById(A).removeAttribute(_A)
@bind(_F,_M)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_C
	if js.document.getElementById(_M).checked:A=_B
	for C in range(0,10):
		B=js.document.getElementById(f"troff_{C}")
		try:
			if A:B.removeAttribute(_A)
			else:B.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_J,_N)
def update_boss_required(evt):
	'Disable certain page flags depending on checkboxes.';B='boss_kong_rando';A='boss_location_rando';C=document.getElementById(_N)
	if C.value=='level_order':document.getElementById(A).setAttribute(_A,_A);document.getElementById(A).checked=_C;document.getElementById(B).setAttribute(_A,_A);document.getElementById(B).checked=_C
	else:
		try:document.getElementById(B).removeAttribute(_A);document.getElementById(A).removeAttribute(_A)
		except Exception:pass