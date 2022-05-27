'Import functions within the UI folder to have them run on load of the UI.'
_A=None
from ui.generate_buttons import disable_input
from ui.rando_options import set_preset_options,toggle_b_locker_boxes,toggle_counts_boxes,update_boss_required,disable_colors,disable_music,disable_shuffle_shop,max_randomized_blocker,max_randomized_troff,disable_barrel_rando
disable_input(_A)
set_preset_options()
toggle_counts_boxes(_A)
toggle_b_locker_boxes(_A)
update_boss_required(_A)
disable_colors(_A)
disable_music(_A)
disable_shuffle_shop(_A)
max_randomized_blocker(_A)
max_randomized_troff(_A)
disable_barrel_rando(_A)