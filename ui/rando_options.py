'Options for the main rando tab.'
_b='gnawty_barrels'
_a='krool_random'
_Z='starting_kongs_count'
_Y='random_music'
_X='random_colors'
_W='level_order'
_V='shop_location_rando'
_U='kong_rando'
_T='randomize_cb_required_amounts'
_S='randomize_blocker_required_amounts'
_R='focusout'
_Q='troff_'
_P='blocker_'
_O='enable_tag_anywhere'
_N='unlock_all_moves'
_M='level_randomization'
_L='change'
_K='presets'
_J='name'
_I='keydown'
_H='input'
_G='disable_tag_barrels'
_F='troff_text'
_E='blocker_text'
_D='click'
_C=True
_B=False
_A='disabled'
import random,js
from js import document
from ui.bindings import bind
def randomseed(evt):'Randomly generate a seed ID.';document.getElementById('seed').value=str(random.randint(100000,999999))
@bind(_H,_P,8)
@bind(_H,_Q,8)
@bind(_H,_E)
@bind(_H,_F)
def on_input(event):
	'Limits inputs from input boxes on keypress.\n\n    Args:\n        event (domevent): The DOMEvent data.\n\n    Returns:\n        bool: False if we need to stop the event.\n    ';A=event
	if A.target.id==_E:return
	elif A.target.id==_F:return
	elif'troff'in A.target.id:min_max(A,0,500)
	elif'blocker'in A.target.id:min_max(A,0,200)
@bind(_R,_E)
def max_randomized_blocker(event):
	'Validate blocker input on loss of focus.';A=js.document.getElementById(_E)
	if not A.value:A.value=50
	elif 0<=int(A.value)<8:A.value=8
	elif int(A.value)>200:A.value=200
@bind(_R,_F)
def max_randomized_troff(event):
	'Validate troff input on loss of focus.';A=js.document.getElementById(_F)
	if not A.value:A.value=300
	elif int(A.value)>500:A.value=500
def min_max(event,min,max):
	'Check if the data is within bounds of requirements.\n\n    Args:\n        event (DomEvent): The doms event.\n        min (int): Minimum Value to keep.\n        max (int): Maximum value to allow.\n\n    Returns:\n        bool: Deny or Success for Handled\n    ';A=event
	try:
		if int(A.target.value)>=max:A.preventDefault();document.getElementById(A.target.id).value=max
		elif int(A.target.value)<=min:A.preventDefault();document.getElementById(A.target.id).value=min
		else:document.getElementById(A.target.id).value=str(A.target.value)
	except Exception:A.preventDefault();document.getElementById(A.target.id).value=min
@bind(_I,_P,8)
@bind(_I,_Q,8)
@bind(_I,_E)
@bind(_I,_F)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';C=document.getElementById(_K);D=[]
	for E in C.children:D.append(E.value)
	for A in js.progression_presets:
		if A.get(_J)not in D:B=document.createElement('option');B.value=A.get(_J);B.innerHTML=A.get(_J);B.title=A.get('description');C.appendChild(B)
	js.jq('#presets').val('Suggested');toggle_counts_boxes(None);toggle_b_locker_boxes(None);js.load_cookies()
@bind(_L,_K)
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';C='checked';E=document.getElementById(_K);B=None
	for D in js.progression_presets:
		if D.get(_J)==E.value:B=D
	for A in B:
		try:
			if type(B[A])is bool:
				if B[A]is _B:document.getElementsByName(A)[0].removeAttribute(C)
				else:document.getElementsByName(A)[0].setAttribute(C,C)
			else:js.jq(f"#{A}").val(B[A])
		except Exception as F:pass
@bind(_D,_S)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_C
	if js.document.getElementById(_S).checked:A=_B
	B=js.document.getElementById(_E)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"blocker_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_D,_T)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_C
	if js.document.getElementById(_T).checked:A=_B
	B=js.document.getElementById(_F)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"troff_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_L,_M)
def update_boss_required(evt):
	'Disable certain page flags depending on checkboxes.';E=document.getElementById(_M);B=document.getElementById('boss_location_rando');C=document.getElementById('boss_kong_rando');D=document.getElementById(_U);A=document.getElementById(_V);F=document.getElementById(_N)
	if E.value==_W:B.setAttribute(_A,_A);B.checked=_C;C.setAttribute(_A,_A);C.checked=_C;D.setAttribute(_A,_A);D.checked=_C;A.setAttribute(_A,_A);A.checked=_C
	else:
		try:C.removeAttribute(_A);B.removeAttribute(_A);D.removeAttribute(_A);A.removeAttribute(_A)
		except Exception:pass
	if F.checked:
		try:A.setAttribute(_A,_A);A.checked=_B
		except Exception:pass
@bind(_D,_X)
def disable_colors(evt):
	'Disable color options when Randomize All is selected.';A=_B
	if js.document.getElementById(_X).checked:A=_C
	for C in ['dk','diddy','tiny','lanky','chunky']:
		B=js.document.getElementById(f"{C}_colors")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_D,_O)
def disable_tag_spawn(evt):
	"Disable 'Disable Tag Spawn' option when 'Tag Anywhere' is off.";A=_B
	if js.document.getElementById(_O).checked is _B:A=_C
	if A:js.document.getElementById(_G).setAttribute(_A,_A);js.document.getElementById(_G).checked=_B
	else:js.document.getElementById(_G).removeAttribute(_A)
@bind(_D,_G)
def enable_tag_anywhere(evt):
	"Enable 'Tag Anywhere' if 'Disable Tag Spawn' option is on."
	if js.document.getElementById(_G).checked:js.document.getElementById(_O).checked=_C
@bind(_D,_Y)
def disable_music(evt):
	'Disable music options when Randomize All is selected.';A=_B
	if js.document.getElementById(_Y).checked:A=_C
	for C in ['bgm','fanfares','events']:
		B=js.document.getElementById(f"music_{C}")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_L,_Z)
def enable_kong_rando(evt):
	'Enable Kong Rando if less than 5 starting kongs.';print('Lanky');A=js.document.getElementById(_U)
	if js.document.getElementById(_Z).value=='5':A.checked=_B;A.setAttribute(_A,_A)
	else:A.removeAttribute(_A)
@bind(_D,_a)
def disable_krool_phases(evt):
	'Disable music options when Randomize All is selected.';A=_B;B=js.document.getElementById('krool_phase_count')
	if js.document.getElementById(_a).checked:A=_C
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_N)
def disable_shuffle_shop(evt):
	'Disable Shuffle Shop Move Location when All Moves are Unlocked.';C=_B;A=js.document.getElementById(_V);B=js.document.getElementById('random_prices');D=js.document.getElementById(_N)
	if D.checked:C=_C
	try:
		if C:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A)
		elif js.document.getElementById(_M).value!=_W:A.removeAttribute(_A);B.removeAttribute(_A)
		else:B.removeAttribute(_A);A.checked=_C
	except AttributeError:pass
@bind(_D,_b)
def disable_barrel_rando(evt):
	'Disable Bonus Barrel Rando when Oops All Beaver Bother is selected.';B=_B;A=js.document.getElementById('bonus_barrel_rando')
	if js.document.getElementById(_b).checked:B=_C
	try:
		if B:A.setAttribute(_A,_A);A.checked=_B
		else:A.removeAttribute(_A)
	except AttributeError:pass