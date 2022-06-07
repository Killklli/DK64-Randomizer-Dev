'Options for the main rando tab.'
_f='gnawty_barrels'
_e='krool_random'
_d='starting_kongs_count'
_c='random_music'
_b='random_colors'
_a='vanilla'
_Z='level_order'
_Y='boss_kong_rando'
_X='boss_location_rando'
_W='randomize_cb_required_amounts'
_V='randomize_blocker_required_amounts'
_U='focusout'
_T='troff_'
_S='blocker_'
_R='enable_tag_anywhere'
_Q='change'
_P='unlock_all_moves'
_O='shop_location_rando'
_N='presets'
_M='kong_rando'
_L='level_randomization'
_K='keydown'
_J='input'
_I='disable_tag_barrels'
_H='name'
_G='troff_text'
_F='blocker_text'
_E='click'
_D=None
_C=False
_B=True
_A='disabled'
import random,js
from js import document
from ui.bindings import bind
def randomseed(evt):'Randomly generate a seed ID.';document.getElementById('seed').value=str(random.randint(100000,999999))
@bind(_J,_S,8)
@bind(_J,_T,8)
@bind(_J,_F)
@bind(_J,_G)
def on_input(event):
	'Limits inputs from input boxes on keypress.\n\n    Args:\n        event (domevent): The DOMEvent data.\n\n    Returns:\n        bool: False if we need to stop the event.\n    ';A=event
	if A.target.id==_F:return
	elif A.target.id==_G:return
	elif'troff'in A.target.id:min_max(A,0,500)
	elif'blocker'in A.target.id:min_max(A,0,200)
@bind(_U,_F)
def max_randomized_blocker(event):
	'Validate blocker input on loss of focus.';A=js.document.getElementById(_F)
	if not A.value:A.value=50
	elif 0<=int(A.value)<8:A.value=8
	elif int(A.value)>200:A.value=200
@bind(_U,_G)
def max_randomized_troff(event):
	'Validate troff input on loss of focus.';A=js.document.getElementById(_G)
	if not A.value:A.value=300
	elif int(A.value)>500:A.value=500
def min_max(event,min,max):
	'Check if the data is within bounds of requirements.\n\n    Args:\n        event (DomEvent): The doms event.\n        min (int): Minimum Value to keep.\n        max (int): Maximum value to allow.\n\n    Returns:\n        bool: Deny or Success for Handled\n    ';A=event
	try:
		if int(A.target.value)>=max:A.preventDefault();document.getElementById(A.target.id).value=max
		elif int(A.target.value)<=min:A.preventDefault();document.getElementById(A.target.id).value=min
		else:document.getElementById(A.target.id).value=str(A.target.value)
	except Exception:A.preventDefault();document.getElementById(A.target.id).value=min
@bind(_K,_S,8)
@bind(_K,_T,8)
@bind(_K,_F)
@bind(_K,_G)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';E='-- Select a Preset --';C=document.getElementById(_N);D=[]
	for F in C.children:D.append(F.value)
	for B in js.progression_presets:
		if B.get(_H)not in D:
			A=document.createElement('option');A.value=B.get(_H);A.innerHTML=B.get(_H);A.title=B.get('description');C.appendChild(A)
			if B.get(_H)==E:A.disabled=_B;A.hidden=_B
	js.jq('#presets').val(E);toggle_counts_boxes(_D);toggle_b_locker_boxes(_D);js.load_cookies()
@bind(_E,_V)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_B
	if js.document.getElementById(_V).checked:A=_C
	B=js.document.getElementById(_F)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"blocker_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_E,_W)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_B
	if js.document.getElementById(_W).checked:A=_C
	B=js.document.getElementById(_G)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"troff_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_Q,_L)
def update_boss_required(evt):
	'Disable certain page flags depending on checkboxes.';E=document.getElementById(_L);B=document.getElementById(_X);C=document.getElementById(_Y);D=document.getElementById(_M);A=document.getElementById(_O);F=document.getElementById(_P)
	if E.value==_Z:B.setAttribute(_A,_A);B.checked=_B;C.setAttribute(_A,_A);C.checked=_B;D.setAttribute(_A,_A);D.checked=_B;A.setAttribute(_A,_A);A.checked=_B
	elif E.value==_a and D.checked:B.setAttribute(_A,_A);B.checked=_B;C.setAttribute(_A,_A);C.checked=_B;D.removeAttribute(_A);A.removeAttribute(_A)
	else:
		try:C.removeAttribute(_A);B.removeAttribute(_A);D.removeAttribute(_A);A.removeAttribute(_A)
		except Exception:pass
	if F.checked:
		try:A.setAttribute(_A,_A);A.checked=_C
		except Exception:pass
@bind(_E,_M)
def disable_boss_rando(evt):
	'Disable Boss Kong and Boss Location Rando if Vanilla levels and Kong Rando.';D=document.getElementById(_L);A=document.getElementById(_X);B=document.getElementById(_Y);C=document.getElementById(_M);E=document.getElementById(_O)
	if C.checked and D.value==_a:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B;E.removeAttribute(_A)
	else:B.removeAttribute(_A);A.removeAttribute(_A);C.removeAttribute(_A)
@bind(_E,_b)
def disable_colors(evt):
	'Disable color options when Randomize All is selected.';A=_C
	if js.document.getElementById(_b).checked:A=_B
	for C in ['dk','diddy','tiny','lanky','chunky']:
		B=js.document.getElementById(f"{C}_colors")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_E,_R)
def disable_tag_spawn(evt):
	"Disable 'Disable Tag Spawn' option when 'Tag Anywhere' is off.";A=_C
	if js.document.getElementById(_R).checked is _C:A=_B
	if A:js.document.getElementById(_I).setAttribute(_A,_A);js.document.getElementById(_I).checked=_C
	else:js.document.getElementById(_I).removeAttribute(_A)
@bind(_E,_I)
def enable_tag_anywhere(evt):
	"Enable 'Tag Anywhere' if 'Disable Tag Spawn' option is on."
	if js.document.getElementById(_I).checked:js.document.getElementById(_R).checked=_B
@bind(_E,_c)
def disable_music(evt):
	'Disable music options when Randomize All is selected.';A=_C
	if js.document.getElementById(_c).checked:A=_B
	for C in ['bgm','fanfares','events']:
		B=js.document.getElementById(f"music_{C}")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_Q,_d)
def enable_kong_rando(evt):
	'Enable Kong Rando if less than 5 starting kongs.';A=js.document.getElementById(_M)
	if js.document.getElementById(_d).value=='5':A.checked=_C;A.setAttribute(_A,_A)
	else:A.removeAttribute(_A)
@bind(_E,_e)
def disable_krool_phases(evt):
	'Disable music options when Randomize All is selected.';A=_C;B=js.document.getElementById('krool_phase_count')
	if js.document.getElementById(_e).checked:A=_B
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_E,_P)
def disable_shuffle_shop(evt):
	'Disable Shuffle Shop Move Location when All Moves are Unlocked.';C=_C;A=js.document.getElementById(_O);B=js.document.getElementById('random_prices');D=js.document.getElementById(_P)
	if D.checked:C=_B
	try:
		if C:A.setAttribute(_A,_A);A.checked=_C;B.setAttribute(_A,_A)
		elif js.document.getElementById(_L).value!=_Z:A.removeAttribute(_A);B.removeAttribute(_A)
		else:B.removeAttribute(_A);A.checked=_B
	except AttributeError:pass
@bind(_E,_f)
def disable_barrel_rando(evt):
	'Disable Bonus Barrel Rando when Oops All Beaver Bother is selected.';B=_C;A=js.document.getElementById('bonus_barrel_rando')
	if js.document.getElementById(_f).checked:B=_B
	try:
		if B:A.setAttribute(_A,_A);A.checked=_C
		else:A.removeAttribute(_A)
	except AttributeError:pass
@bind(_Q,_N)
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';D=document.getElementById(_N);B=_D
	for C in js.progression_presets:
		if C.get(_H)==D.value:B=C
	for A in B:
		try:
			if type(B[A])is bool:
				if B[A]is _C:js.jq(f"#{A}").checked=_C;js.document.getElementsByName(A)[0].checked=_C
				else:js.jq(f"#{A}").checked=_B;js.document.getElementsByName(A)[0].checked=_B
				js.jq(f"#{A}").removeAttr(_A)
			else:
				if js.document.getElementsByName(A)[0].hasAttribute('data-slider-value'):js.jq(f"#{A}").slider('setValue',B[A]);js.jq(f"#{A}").slider('enable');js.jq(f"#{A}").parent().find('.slider-disabled').removeClass('slider-disabled')
				else:js.jq(f"#{A}").val(B[A])
				js.jq(f"#{A}").removeAttr(_A)
		except Exception as E:pass
	toggle_counts_boxes(_D);toggle_b_locker_boxes(_D);update_boss_required(_D);disable_colors(_D);disable_music(_D);disable_shuffle_shop(_D);max_randomized_blocker(_D);max_randomized_troff(_D);disable_barrel_rando(_D)