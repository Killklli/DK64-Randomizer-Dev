'Import functions within the UI folder to have them run on load of the UI.'
_A=None
from ui.generate_buttons import disable_input
from ui.rando_options import set_preset_options,toggle_b_locker_boxes,toggle_counts_boxes,unlock_kongs_toggle,update_boss_required,disable_colors,disable_music
disable_input(_A)
set_preset_options()
toggle_counts_boxes(_A)
toggle_b_locker_boxes(_A)
unlock_kongs_toggle(_A)
update_boss_required(_A)
disable_colors(_A)
disable_music(_A)