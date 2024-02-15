import gc
from typing import Any

from bars import setup_bars
from bindings import setup_binds
from env import setup_environment
from groups import setup_groups
from layouts import setup_floating_layout, setup_layouts
from libqtile import qtile

# from base16_colorlib import onedark

gc.set_threshold(200,10,10) # default (700, 10, 10)

NUM_SCREENS: int = 2
GROUPS_PER_SCREEN: int = 3

IS_WAYLAND: bool = qtile.core.name == "wayland" if qtile is not None else False

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
    markup=False,
    rounded=False
)
extension_defaults = widget_defaults.copy()

# {0: (1, 2, 3), 1: (4, 5, 6)}
group_names: dict[int, tuple] = dict(
    (
        screen,
        tuple(
            range(
                (screen * GROUPS_PER_SCREEN) + 1,
                (screen * GROUPS_PER_SCREEN) + GROUPS_PER_SCREEN + 1,
            )
        ),
    )
    for screen in range(NUM_SCREENS)
)

# auto_fullscreen = True # let apps fullscreen themselves
bring_front_click = "floating_only"
cursor_warp = False
# dgroups_app_rules: list[Rule] = []
# dgroups_key_binder: Any = simple_key_binder(mainMod)
floats_kept_above = True
# focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
auto_minimize = True
# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules: Any = None
# set to whitlisted value for better rendering by java swing
wmname = "LG3D"

## Setup
# Rules
keys, mouse = setup_binds()
floating_layout = setup_floating_layout()
# Configure
setup_environment(IS_WAYLAND)
layouts = setup_layouts()
groups = setup_groups(keys, group_names)
# Draw
screens = setup_bars(IS_WAYLAND, group_names)

