'Options for the main rando tab.'
_Z='gnawty_barrels'
_Y='unlock_all_moves'
_X='krool_random'
_W='starting_kongs_count'
_V='random_music'
_U='random_colors'
_T='level_randomization'
_S='randomize_cb_required_amounts'
_R='randomize_blocker_required_amounts'
_Q='focusout'
_P='troff_'
_O='blocker_'
_N='enable_tag_anywhere'
_M='change'
_L='presets'
_K='kong_rando'
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
@bind(_H,_O,8)
@bind(_H,_P,8)
@bind(_H,_E)
@bind(_H,_F)
def on_input(event):
	'Limits inputs from input boxes on keypress.\n\n    Args:\n        event (domevent): The DOMEvent data.\n\n    Returns:\n        bool: False if we need to stop the event.\n    ';A=event
	if A.target.id==_E:return
	elif A.target.id==_F:return
	elif'troff'in A.target.id:min_max(A,0,500)
	elif'blocker'in A.target.id:min_max(A,0,200)
@bind(_Q,_E)
def max_randomized_blocker(event):
	'Validate blocker input on loss of focus.';A=js.document.getElementById(_E)
	if not A.value:A.value=50
	elif 0<=int(A.value)<8:A.value=8
	elif int(A.value)>200:A.value=200
@bind(_Q,_F)
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
@bind(_I,_O,8)
@bind(_I,_P,8)
@bind(_I,_E)
@bind(_I,_F)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';C=document.getElementById(_L);D=[]
	for E in C.children:D.append(E.value)
	for A in js.progression_presets:
		if A.get(_J)not in D:B=document.createElement('option');B.value=A.get(_J);B.innerHTML=A.get(_J);B.title=A.get('description');C.appendChild(B)
	js.jq('#presets').val('Suggested');toggle_counts_boxes(None);toggle_b_locker_boxes(None);js.load_cookies()
@bind(_M,_L)
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';C='checked';E=document.getElementById(_L);B=None
	for D in js.progression_presets:
		if D.get(_J)==E.value:B=D
	for A in B:
		try:
			if type(B[A])is bool:
				if B[A]is _B:document.getElementsByName(A)[0].removeAttribute(C)
				else:document.getElementsByName(A)[0].setAttribute(C,C)
			else:js.jq(f"#{A}").val(B[A])
		except Exception as F:pass
@bind(_D,_R)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_C
	if js.document.getElementById(_R).checked:A=_B
	B=js.document.getElementById(_E)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"blocker_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_D,_S)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_C
	if js.document.getElementById(_S).checked:A=_B
	B=js.document.getElementById(_F)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"troff_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_M,_T)
def update_boss_required(evt):
	'Disable certain page flags depending on checkboxes.';B='boss_kong_rando';A='boss_location_rando';C=document.getElementById(_T)
	if C.value=='level_order':document.getElementById(A).setAttribute(_A,_A);document.getElementById(A).checked=_C;document.getElementById(B).setAttribute(_A,_A);document.getElementById(B).checked=_C;document.getElementById(_K).setAttribute(_A,_A);document.getElementById(_K).checked=_C
	else:
		try:document.getElementById(B).removeAttribute(_A);document.getElementById(A).removeAttribute(_A);document.getElementById(_K).removeAttribute(_A)
		except Exception:pass
@bind(_D,_U)
def disable_colors(evt):
	'Disable color options when Randomize All is selected.';A=_B
	if js.document.getElementById(_U).checked:A=_C
	for C in ['dk','diddy','tiny','lanky','chunky']:
		B=js.document.getElementById(f"{C}_colors")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_D,_N)
def disable_tag_spawn(evt):
	"Disable 'Disable Tag Spawn' option when 'Tag Anywhere' is off.";A=_B
	if js.document.getElementById(_N).checked is _B:A=_C
	if A:js.document.getElementById(_G).setAttribute(_A,_A);js.document.getElementById(_G).checked=_B
	else:js.document.getElementById(_G).removeAttribute(_A)
@bind(_D,_G)
def enable_tag_anywhere(evt):
	"Enable 'Tag Anywhere' if 'Disable Tag Spawn' option is on."
	if js.document.getElementById(_G).checked:js.document.getElementById(_N).checked=_C
@bind(_D,_V)
def disable_music(evt):
	'Disable music options when Randomize All is selected.';A=_B
	if js.document.getElementById(_V).checked:A=_C
	for C in ['bgm','fanfares','events']:
		B=js.document.getElementById(f"music_{C}")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_M,_W)
def enable_kong_rando(evt):
	'Enable Kong Rando if less than 5 starting kongs.';print('Lanky');A=js.document.getElementById(_K)
	if js.document.getElementById(_W).value=='5':A.checked=_B;A.setAttribute(_A,_A)
	else:A.removeAttribute(_A)
@bind(_D,_X)
def disable_krool_phases(evt):
	'Disable music options when Randomize All is selected.';A=_B;B=js.document.getElementById('krool_phase_count')
	if js.document.getElementById(_X).checked:A=_C
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_Y)
def disable_shuffle_shop(evt):
	'Disable Shuffle Shop Move Location when All Moves are Unlocked.';C=_B;A=js.document.getElementById('shop_location_rando');B=js.document.getElementById('random_prices')
	if js.document.getElementById(_Y).checked:C=_C
	try:
		if C:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.value='free'
		else:A.removeAttribute(_A);B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_Z)
def disable_barrel_rando(evt):
	'Disable Bonus Barrel Rando when Oops All Beaver Bother is selected.';B=_B;A=js.document.getElementById('bonus_barrel_rando')
	if js.document.getElementById(_Z).checked:B=_C
	try:
		if B:A.setAttribute(_A,_A);A.checked=_B
		else:A.removeAttribute(_A)
	except AttributeError:pass