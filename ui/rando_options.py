'Options for the main rando tab.'
_f='gnawty_barrels'
_e='move_rando'
_d='krool_random'
_c='starting_kongs_count'
_b='random_music'
_a='enguarde'
_Z='chunky'
_Y='vanilla'
_X='boss_kong_rando'
_W='boss_location_rando'
_V='randomize_cb_required_amounts'
_U='randomize_blocker_required_amounts'
_T='focusout'
_S='troff_'
_R='blocker_'
_Q='enable_tag_anywhere'
_P='random_colors'
_O='level_randomization'
_N='presets'
_M='kong_rando'
_L='keydown'
_K='input'
_J='disable_tag_barrels'
_I='name'
_H='troff_text'
_G='blocker_text'
_F='click'
_E='change'
_D=None
_C=False
_B=True
_A='disabled'
import random,js
from js import document
from ui.bindings import bind
def randomseed(evt):'Randomly generate a seed ID.';document.getElementById('seed').value=str(random.randint(100000,999999))
@bind(_K,_R,8)
@bind(_K,_S,8)
@bind(_K,_G)
@bind(_K,_H)
def on_input(event):
	'Limits inputs from input boxes on keypress.\n\n    Args:\n        event (domevent): The DOMEvent data.\n\n    Returns:\n        bool: False if we need to stop the event.\n    ';A=event
	if A.target.id==_G:return
	elif A.target.id==_H:return
	elif'troff'in A.target.id:min_max(A,0,500)
	elif'blocker'in A.target.id:min_max(A,0,200)
@bind(_T,_G)
def max_randomized_blocker(event):
	'Validate blocker input on loss of focus.';A=js.document.getElementById(_G)
	if not A.value:A.value=50
	elif 0<=int(A.value)<8:A.value=8
	elif int(A.value)>200:A.value=200
@bind(_T,_H)
def max_randomized_troff(event):
	'Validate troff input on loss of focus.';A=js.document.getElementById(_H)
	if not A.value:A.value=300
	elif int(A.value)>500:A.value=500
def min_max(event,min,max):
	'Check if the data is within bounds of requirements.\n\n    Args:\n        event (DomEvent): The doms event.\n        min (int): Minimum Value to keep.\n        max (int): Maximum value to allow.\n\n    Returns:\n        bool: Deny or Success for Handled\n    ';A=event
	try:
		if int(A.target.value)>=max:A.preventDefault();document.getElementById(A.target.id).value=max
		elif int(A.target.value)<=min:A.preventDefault();document.getElementById(A.target.id).value=min
		else:document.getElementById(A.target.id).value=str(A.target.value)
	except Exception:A.preventDefault();document.getElementById(A.target.id).value=min
@bind(_L,_R,8)
@bind(_L,_S,8)
@bind(_L,_G)
@bind(_L,_H)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';E='-- Select a Preset --';C=document.getElementById(_N);D=[]
	for F in C.children:D.append(F.value)
	for B in js.progression_presets:
		if B.get(_I)not in D:
			A=document.createElement('option');A.value=B.get(_I);A.innerHTML=B.get(_I);A.title=B.get('description');C.appendChild(A)
			if B.get(_I)==E:A.disabled=_B;A.hidden=_B
	js.jq('#presets').val(E);toggle_counts_boxes(_D);toggle_b_locker_boxes(_D);js.load_cookies()
@bind(_F,_U)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_B
	if js.document.getElementById(_U).checked:A=_C
	B=js.document.getElementById(_G);C=js.document.getElementById('maximize_helm_blocker')
	if A:B.setAttribute(_A,_A);C.setAttribute(_A,_A)
	else:B.removeAttribute(_A);C.removeAttribute(_A)
	for E in range(0,10):
		D=js.document.getElementById(f"blocker_{E}")
		try:
			if A:D.removeAttribute(_A)
			else:D.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_F,_V)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_B
	if js.document.getElementById(_V).checked:A=_C
	B=js.document.getElementById(_H)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"troff_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_E,_O)
def update_boss_required(evt):
	'Disable certain page flags depending on checkboxes.';E=document.getElementById(_O);A=document.getElementById(_W);B=document.getElementById(_X);C=document.getElementById(_M);D=document.getElementById('move_off')
	if E.value=='level_order':
		A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B;C.setAttribute(_A,_A);C.checked=_B
		if D.selected is _B:document.getElementById('move_on').selected=_B
		D.setAttribute(_A,_A)
	elif E.value==_Y and C.checked:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B;C.removeAttribute(_A);D.removeAttribute(_A)
	else:
		try:B.removeAttribute(_A);A.removeAttribute(_A);C.removeAttribute(_A);D.removeAttribute(_A)
		except Exception:pass
@bind(_F,_M)
def disable_boss_rando(evt):
	'Disable Boss Kong and Boss Location Rando if Vanilla levels and Kong Rando.';D=document.getElementById(_O);A=document.getElementById(_W);B=document.getElementById(_X);C=document.getElementById(_M)
	if C.checked and D.value==_Y:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B
	else:B.removeAttribute(_A);A.removeAttribute(_A);C.removeAttribute(_A)
@bind(_F,_P)
def disable_colors(evt):
	'Disable color options when Randomize All is selected.';A=_C
	if js.document.getElementById(_P).checked:A=_B
	for C in ['dk','diddy','tiny','lanky',_Z,'rambi',_a]:
		B=js.document.getElementById(f"{C}_colors")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
	hide_rgb(_D)
@bind(_F,_Q)
def disable_tag_spawn(evt):
	"Disable 'Disable Tag Spawn' option when 'Tag Anywhere' is off.";A=_C
	if js.document.getElementById(_Q).checked is _C:A=_B
	if A:js.document.getElementById(_J).setAttribute(_A,_A);js.document.getElementById(_J).checked=_C
	else:js.document.getElementById(_J).removeAttribute(_A)
@bind(_F,_J)
def enable_tag_anywhere(evt):
	"Enable 'Tag Anywhere' if 'Disable Tag Spawn' option is on."
	if js.document.getElementById(_J).checked:js.document.getElementById(_Q).checked=_B
@bind(_F,_b)
def disable_music(evt):
	'Disable music options when Randomize All is selected.';A=_C
	if js.document.getElementById(_b).checked:A=_B
	for C in ['bgm','fanfares','events']:
		B=js.document.getElementById(f"music_{C}")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_E,_c)
def enable_kong_rando(evt):
	'Enable Kong Rando if less than 5 starting kongs.';A=js.document.getElementById(_M)
	if js.document.getElementById(_c).value=='5':A.checked=_C;A.setAttribute(_A,_A)
	else:A.removeAttribute(_A)
@bind(_F,_d)
def disable_krool_phases(evt):
	'Disable K Rool options when Randomize All is selected.';A=_C;B=js.document.getElementById('krool_phase_count')
	if js.document.getElementById(_d).checked:A=_B
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_E,_e)
def disable_prices(evt):
	'Disable prices if move rando is set to start with all moves.';B=js.document.getElementById(_e);A=js.document.getElementById('random_prices')
	try:
		if B.value=='start_with':A.setAttribute(_A,_A)
		else:A.removeAttribute(_A)
	except AttributeError:pass
@bind(_F,_f)
def disable_barrel_rando(evt):
	'Disable Bonus Barrel Rando when Oops All Beaver Bother is selected.';B=_C;A=js.document.getElementById('bonus_barrel_rando')
	if js.document.getElementById(_f).checked:B=_B
	try:
		if B:A.setAttribute(_A,_A);A.checked=_C
		else:A.removeAttribute(_A)
	except AttributeError:pass
@bind(_E,_N)
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';D=document.getElementById(_N);B=_D
	for C in js.progression_presets:
		if C.get(_I)==D.value:B=C
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
	toggle_counts_boxes(_D);toggle_b_locker_boxes(_D);update_boss_required(_D);disable_colors(_D);disable_music(_D);disable_prices(_D);max_randomized_blocker(_D);max_randomized_troff(_D);disable_barrel_rando(_D)
@bind(_E,'dk_colors')
@bind(_E,'diddy_colors')
@bind(_E,'lanky_colors')
@bind(_E,'tiny_colors')
@bind(_E,'chunky_colors')
@bind(_E,'rambi_colors')
@bind(_E,'enguarde_colors')
def hide_rgb(event):
	'Show RGB Selector if Custom Color is selected.'
	for A in ['dk','diddy','lanky','tiny',_Z,'rambi',_a]:
		B=_B;C=js.document.getElementById(f"{A}_custom")
		if js.document.getElementById(f"{A}_colors").value=='custom':B=_C
		try:
			if B or js.document.getElementById(_P).checked:C.style.display='none'
			else:C.style=''
		except AttributeError:pass