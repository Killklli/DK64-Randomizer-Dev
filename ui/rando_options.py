'Options for the main rando tab.'
_N='randomize_cb_required_amounts'
_M='randomize_blocker_required_amounts'
_L='keydown'
_K='troff_'
_J='blocker_'
_I='change'
_H='level_randomization'
_G='click'
_F='presets'
_E='name'
_D=True
_C=False
_B='unlock_all_kongs'
_A='disabled'
import random,js
from js import document
from ui.bindings import bind
@bind(_I,_H)
def update_disabled_progression(evt):
	'Disable certain page flags depending on checkboxes.';A=document.getElementById(_H)
	if A.value=='level_order':document.getElementById(_B).setAttribute(_A,_A);document.getElementById(_B).checked=_D
	else:
		try:document.getElementById(_B).removeAttribute(_A)
		except Exception:pass
def randomseed(evt):'Randomly generate a seed ID.';document.getElementById('seed').value=str(random.randint(100000,999999))
@bind('input',_J,8)
@bind('input',_K,8)
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
@bind(_L,_J,8)
@bind(_L,_K,8)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';C=document.getElementById(_F);D=[]
	for E in C.children:D.append(E.value)
	for A in js.progression_presets:
		if A.get(_E)not in D:B=document.createElement('option');B.value=A.get(_E);B.innerHTML=A.get(_E);B.title=A.get('description');C.appendChild(B)
	js.jq('#presets').val('Suggested');toggle_counts_boxes(None);toggle_b_locker_boxes(None);js.load_cookies()
@bind(_I,_F)
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';C='checked';E=document.getElementById(_F);B=None
	for D in js.progression_presets:
		if D.get(_E)==E.value:B=D
	for A in B:
		try:
			if type(B[A])is bool:
				if B[A]is _C:document.getElementsByName(A)[0].removeAttribute(C)
				else:document.getElementsByName(A)[0].setAttribute(C,C)
			else:js.jq(f"#{A}").val(B[A])
		except Exception as F:pass
@bind(_G,_M)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_D
	if js.document.getElementById(_M).checked:A=_C
	for C in range(0,10):
		B=js.document.getElementById(f"blocker_{C}")
		try:
			if A:B.removeAttribute(_A)
			else:B.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_G,_B)
def unlock_kongs_toggle(event):
	'Toggle the textboxes for unlock_all_kongs.';A='kong_rando';B=_C
	if js.document.getElementById(_B).checked:B=_D
	if B:js.document.getElementById(A).setAttribute(_A,_A);js.document.getElementById(A).checked=_C
	else:js.document.getElementById(A).removeAttribute(_A)
@bind(_G,_N)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_D
	if js.document.getElementById(_N).checked:A=_C
	for C in range(0,10):
		B=js.document.getElementById(f"troff_{C}")
		try:
			if A:B.removeAttribute(_A)
			else:B.setAttribute(_A,_A)
		except AttributeError:pass