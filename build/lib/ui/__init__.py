'Import functions within the UI folder to have them run on load of the UI.'
_A=None
from ui.generate_buttons import update_seed_text
from ui.rando_options import disable_barrel_modal,disable_boss_rando,disable_colors,disable_music,disable_prices,disable_rw,hide_rgb,max_randomized_blocker,max_randomized_medals,max_randomized_troff,set_preset_options,toggle_b_locker_boxes,toggle_counts_boxes,toggle_medals_box,update_boss_required
update_seed_text(_A)
set_preset_options()
toggle_counts_boxes(_A)
toggle_b_locker_boxes(_A)
update_boss_required(_A)
disable_colors(_A)
disable_music(_A)
disable_prices(_A)
max_randomized_blocker(_A)
max_randomized_troff(_A)
disable_barrel_modal(_A)
disable_boss_rando(_A)
hide_rgb(_A)
toggle_medals_box(_A)
max_randomized_medals(_A)
disable_rw(_A)