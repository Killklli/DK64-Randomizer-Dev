'Import functions within the UI folder to have them run on load of the UI.'
_A=None
from ui.generate_buttons import disable_input
from ui.rando_options import set_preset_options,toggle_b_locker_boxes,toggle_counts_boxes,update_disabled_progression,unlock_kongs_toggle
disable_input(_A)
set_preset_options()
toggle_counts_boxes(_A)
toggle_b_locker_boxes(_A)
update_disabled_progression(_A)
unlock_kongs_toggle(_A)