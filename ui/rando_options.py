'Options for the main rando tab.'
_x='nav-qol-tab'
_w='nav-difficulty-tab'
_v='nav-overworld-tab'
_u='nav-random-tab'
_t='nav-started-tab'
_s='no_logic'
_r='coin_door_open'
_q='item_rando_list_selected'
_p='shuffle_items'
_o='enemy_rando'
_n='bonus_barrel_rando'
_m='start_with'
_l='random_prices'
_k='move_rando'
_j='helm_random'
_i='krool_random'
_h='starting_kongs_count'
_g='random_music'
_f='enguarde'
_e='chunky'
_d='level_order'
_c='boss_kong_rando'
_b='boss_location_rando'
_a='randomize_cb_required_amounts'
_Z='randomize_blocker_required_amounts'
_Y='presets'
_X='medal_cb_req'
_W='troff_'
_V='blocker_'
_U='random_medal_requirement'
_T='shockwave_status'
_S='enable_tag_anywhere'
_R='random_colors'
_Q='level_randomization'
_P='vanilla'
_O='kong_rando'
_N='keydown'
_M='medal_requirement'
_L='focusout'
_K='input'
_J='disable_tag_barrels'
_I='name'
_H='troff_text'
_G='blocker_text'
_F='change'
_E=None
_D='click'
_C=False
_B=True
_A='disabled'
import random,js
from js import document
from ui.bindings import bind
def randomseed(evt):'Randomly generate a seed ID.';document.getElementById('seed').value=str(random.randint(100000,999999))
@bind(_K,_V,8)
@bind(_K,_W,8)
@bind(_K,_G)
@bind(_K,_H)
def on_input(event):
	'Limits inputs from input boxes on keypress.\n\n    Args:\n        event (domevent): The DOMEvent data.\n\n    Returns:\n        bool: False if we need to stop the event.\n    ';A=event
	if A.target.id==_G:return
	elif A.target.id==_H:return
	elif'troff'in A.target.id:min_max(A,0,500)
	elif'blocker'in A.target.id:min_max(A,0,200)
@bind(_L,_G)
def max_randomized_blocker(event):
	'Validate blocker input on loss of focus.';A=js.document.getElementById(_G)
	if not A.value:A.value=50
	elif 0<=int(A.value)<8:A.value=8
	elif int(A.value)>200:A.value=200
@bind(_L,_H)
def max_randomized_troff(event):
	'Validate troff input on loss of focus.';A=js.document.getElementById(_H)
	if not A.value:A.value=300
	elif int(A.value)>500:A.value=500
@bind(_L,_M)
def max_randomized_medals(event):
	'Validate medal input on loss of focus.';A=js.document.getElementById(_M)
	if not A.value:A.value=15
	elif 0>int(A.value):A.value=0
	elif int(A.value)>40:A.value=40
@bind(_L,_X)
def max_randomized_medals(event):
	'Validate cb medal input on loss of focus.';A=js.document.getElementById(_X)
	if not A.value:A.value=75
	elif 1>int(A.value):A.value=1
	elif int(A.value)>100:A.value=100
def min_max(event,min,max):
	'Check if the data is within bounds of requirements.\n\n    Args:\n        event (DomEvent): The doms event.\n        min (int): Minimum Value to keep.\n        max (int): Maximum value to allow.\n\n    Returns:\n        bool: Deny or Success for Handled\n    ';A=event
	try:
		if int(A.target.value)>=max:A.preventDefault();document.getElementById(A.target.id).value=max
		elif int(A.target.value)<=min:A.preventDefault();document.getElementById(A.target.id).value=min
		else:document.getElementById(A.target.id).value=str(A.target.value)
	except Exception:A.preventDefault();document.getElementById(A.target.id).value=min
@bind(_N,_V,8)
@bind(_N,_W,8)
@bind(_N,_G)
@bind(_N,_H)
def key_down(event):
	'Check if a key is a proper number, deletion, navigation, Copy/Cut/Paste.\n\n    Args:\n        event (DomEvent): Event from the DOM.\n    ';A=event;B=['Backspace','Delete','ArrowLeft','ArrowRight','Control_L','Control_R','x','v','c']
	if not A.key.isdigit()and A.key not in B:A.preventDefault()
	else:0
def set_preset_options():
	'Set the Blocker presets on the page.';E='-- Select a Preset --';C=document.getElementById(_Y);D=[]
	for F in C.children:D.append(F.value)
	for B in js.progression_presets:
		if B.get(_I)not in D:
			A=document.createElement('option');A.value=B.get(_I);A.innerHTML=B.get(_I);A.title=B.get('description');C.appendChild(A)
			if B.get(_I)==E:A.disabled=_B;A.hidden=_B
	js.jq('#presets').val(E);toggle_counts_boxes(_E);toggle_b_locker_boxes(_E);toggle_extreme_prices_option(_E);js.load_cookies()
@bind(_D,_Z)
def toggle_b_locker_boxes(event):
	'Toggle the textboxes for BLockers.';A=_B
	if js.document.getElementById(_Z).checked:A=_C
	B=js.document.getElementById(_G);C=js.document.getElementById('maximize_helm_blocker')
	if A:B.setAttribute(_A,_A);C.setAttribute(_A,_A)
	else:B.removeAttribute(_A);C.removeAttribute(_A)
	for E in range(0,10):
		D=js.document.getElementById(f"blocker_{E}")
		try:
			if A:D.removeAttribute(_A)
			else:D.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_D,_a)
def toggle_counts_boxes(event):
	'Toggle the textboxes for Troff.';A=_B
	if js.document.getElementById(_a).checked:A=_C
	B=js.document.getElementById(_H)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
	for D in range(0,10):
		C=js.document.getElementById(f"troff_{D}")
		try:
			if A:C.removeAttribute(_A)
			else:C.setAttribute(_A,_A)
		except AttributeError:pass
@bind(_F,_Q)
def update_boss_required(evt):
	'Disable certain page flags depending on checkboxes.';F=document.getElementById(_Q);A=document.getElementById(_b);B=document.getElementById(_c);C=document.getElementById(_O);E=document.getElementById('move_off');D=document.getElementById('hard_level_progression')
	if F.value==_d:
		A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B;C.setAttribute(_A,_A);C.checked=_B
		if E.selected is _B:document.getElementById('move_on').selected=_B
		E.setAttribute(_A,_A);D.removeAttribute(_A)
	elif F.value==_P and C.checked:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B;C.removeAttribute(_A);E.removeAttribute(_A);D.setAttribute(_A,_A);D.checked=_C
	else:
		try:B.removeAttribute(_A);A.removeAttribute(_A);C.removeAttribute(_A);E.removeAttribute(_A);D.setAttribute(_A,_A);D.checked=_C
		except Exception:pass
@bind(_D,_O)
def disable_boss_rando(evt):
	'Disable Boss Kong and Boss Location Rando if Vanilla levels and Kong Rando.';C=document.getElementById(_Q);A=document.getElementById(_b);B=document.getElementById(_c);D=document.getElementById(_O)
	if D.checked and C.value==_P or C.value==_d:A.setAttribute(_A,_A);A.checked=_B;B.setAttribute(_A,_A);B.checked=_B
	else:B.removeAttribute(_A);A.removeAttribute(_A);D.removeAttribute(_A)
@bind(_D,_R)
def disable_colors(evt):
	'Disable color options when Randomize All is selected.';A=_C
	if js.document.getElementById(_R).checked:A=_B
	for C in ['dk','diddy','tiny','lanky',_e,'rambi',_f]:
		B=js.document.getElementById(f"{C}_colors")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
	hide_rgb(_E)
@bind(_D,_S)
def disable_tag_spawn(evt):
	"Disable 'Disable Tag Spawn' option when 'Tag Anywhere' is off.";A=_C
	if js.document.getElementById(_S).checked is _C:A=_B
	if A:js.document.getElementById(_J).setAttribute(_A,_A);js.document.getElementById(_J).checked=_C
	else:js.document.getElementById(_J).removeAttribute(_A)
@bind(_D,_J)
def enable_tag_anywhere(evt):
	"Enable 'Tag Anywhere' if 'Disable Tag Spawn' option is on."
	if js.document.getElementById(_J).checked:js.document.getElementById(_S).checked=_B
@bind(_D,_g)
def disable_music(evt):
	'Disable music options when Randomize All is selected.';A=_C
	if js.document.getElementById(_g).checked:A=_B
	for C in ['bgm','fanfares','events']:
		B=js.document.getElementById(f"music_{C}")
		try:
			if A:B.setAttribute(_A,_A)
			else:B.removeAttribute(_A)
		except AttributeError:pass
@bind(_F,_h)
def enable_kong_rando(evt):
	'Enable Kong Rando if less than 5 starting kongs.';A=js.document.getElementById(_O)
	if js.document.getElementById(_h).value=='5':A.checked=_C;A.setAttribute(_A,_A)
	else:A.removeAttribute(_A)
@bind(_D,_i)
def disable_krool_phases(evt):
	'Disable K Rool options when Randomize All is selected.';A=_C;B=js.document.getElementById('krool_phase_count')
	if js.document.getElementById(_i).checked:A=_B
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_j)
def disable_helm_phases(evt):
	'Disable K Rool options when Randomize All is selected.';A=_C;B=js.document.getElementById('helm_phase_count')
	if js.document.getElementById(_j).checked:A=_B
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_F,_k)
def disable_move_shuffles(evt):
	'Disable some settings based on the move rando setting.';E='normal';D=js.document.getElementById(_k);C=js.document.getElementById(_l);A=js.document.getElementById('training_barrels');B=js.document.getElementById(_T)
	try:
		if D.value==_m:C.setAttribute(_A,_A);A.value=E;A.setAttribute(_A,_A);B.value=_P;B.setAttribute(_A,_A)
		elif D.value=='off':C.removeAttribute(_A);A.value=E;A.setAttribute(_A,_A);B.value=_P;B.setAttribute(_A,_A)
		else:C.removeAttribute(_A);A.removeAttribute(_A);B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_n)
def disable_barrel_modal(evt):
	'Disable Minigame Selector when Shuffle Bonus Barrels is off.';A=_B;B=js.document.getElementById('minigames_list_modal')
	if js.document.getElementById(_n).checked:A=_C
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_o)
def disable_enemy_modal(evt):
	'Disable Enemy Selector when Enemy Rando is off.';A=_B;B=js.document.getElementById('enemies_modal')
	if js.document.getElementById(_o).checked:A=_C
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_p)
def disable_items_modal(evt):
	'Disable Item Rando Selector when Item Rando is off.';A=_B;B=js.document.getElementById('item_rando_list_modal')
	if js.document.getElementById(_p).checked:A=_C
	try:
		if A:B.setAttribute(_A,_A)
		else:B.removeAttribute(_A)
	except AttributeError:pass
@bind(_D,_q)
def disable_coupled_camera_shockwave(evt):
	'Disable Item Rando Selector when Item Rando is off.';B=_C;D=document.getElementById(_q).options;A=document.getElementById('shockwave_status_shuffled')
	for C in D:
		if C.value=='shop'and C.selected:
			if A.selected is _B:document.getElementById('shockwave_status_shuffled_decoupled').selected=_B
			A.setAttribute(_A,_A);B=_B
		elif not B:A.removeAttribute(_A)
@bind(_D,'apply_preset')
def preset_select_changed(event):
	'Trigger a change of the form via the JSON templates.';F=document.getElementById(_Y);B=_E
	for D in js.progression_presets:
		if D.get(_I)==F.value:B=D
	for A in B:
		try:
			if type(B[A])is bool:
				if B[A]is _C:js.jq(f"#{A}").checked=_C;js.document.getElementsByName(A)[0].checked=_C
				else:js.jq(f"#{A}").checked=_B;js.document.getElementsByName(A)[0].checked=_B
				js.jq(f"#{A}").removeAttr(_A)
			elif type(B[A])is list:
				C=js.document.getElementById(A)
				for E in range(0,C.options.length):C.item(E).selected=C.item(E).value in B[A]
			else:
				if js.document.getElementsByName(A)[0].hasAttribute('data-slider-value'):js.jq(f"#{A}").slider('setValue',B[A]);js.jq(f"#{A}").slider('enable');js.jq(f"#{A}").parent().find('.slider-disabled').removeClass('slider-disabled')
				else:js.jq(f"#{A}").val(B[A])
				js.jq(f"#{A}").removeAttr(_A)
		except Exception as G:pass
	toggle_counts_boxes(_E);toggle_b_locker_boxes(_E);update_boss_required(_E);disable_colors(_E);disable_music(_E);disable_move_shuffles(_E);max_randomized_blocker(_E);max_randomized_troff(_E);disable_barrel_modal(_E)
@bind(_F,'dk_colors')
@bind(_F,'diddy_colors')
@bind(_F,'lanky_colors')
@bind(_F,'tiny_colors')
@bind(_F,'chunky_colors')
@bind(_F,'rambi_colors')
@bind(_F,'enguarde_colors')
def hide_rgb(event):
	'Show RGB Selector if Custom Color is selected.'
	for A in ['dk','diddy','lanky','tiny',_e,'rambi',_f]:
		B=_B;C=js.document.getElementById(f"{A}_custom")
		if js.document.getElementById(f"{A}_colors").value=='custom':B=_C
		try:
			if B or js.document.getElementById(_R).checked:C.style.display='none'
			else:C.style=''
		except AttributeError:pass
@bind(_D,_U)
def toggle_medals_box(event):
	'Toggle the textbox for Banana Medals.';A=_C
	if js.document.getElementById(_U).checked:A=_B
	B=js.document.getElementById(_M)
	if A:B.setAttribute(_A,_A)
	else:B.removeAttribute(_A)
@bind(_F,_r)
def disable_rw(evt):
	'Disable Banana Medal values from being changed if RW coin not needed.';B=document.getElementById(_r);A=document.getElementById(_U);C=document.getElementById(_M)
	if B.value=='need_zero'or B.value=='need_nin':
		try:A.setAttribute(_A,_A);A.checked=_C;C.setAttribute(_A,_A)
		except Exception:pass
	else:
		try:A.removeAttribute(_A);C.removeAttribute(_A)
		except Exception:pass
@bind(_F,_T)
def toggle_extreme_prices_option(event):
	'Determine the visibility of the extreme prices option.';C=document.getElementById(_T).value==_m;D=document.getElementById(_s).checked;A=document.getElementById('extreme_price_option')
	if C or D:A.removeAttribute(_A)
	else:
		A.setAttribute(_A,_A);B=document.getElementById(_l)
		if B.value=='extreme':B.value='high'
@bind(_F,_s)
def toggle_no_logic(event):'Toggle settings based on the presence of logic.';toggle_extreme_prices_option(event)
@bind(_D,'nav-patch-tab')
def toggle_patch_ui(event):
	'Disable non-cosmetic tabs if using patch file.'
	for A in [_t,_u,_v,_w,_x]:document.getElementById(A).setAttribute(_A,_A)
	document.getElementById('nav-cosmetics-tab').click()
@bind(_D,'nav-seed-gen-tab')
def toggle_patch_ui(event):
	'Re-enable non-cosmetic tabs and hide override option if generating a new seed.';A='hidden'
	for B in [_t,_u,_v,_w,_x]:document.getElementById(B).removeAttribute(_A)
	document.getElementById('override_div').setAttribute(A,A)