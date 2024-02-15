import copy

from qtile_extras.popup.toolkit import hook

import colors
from widgets.left import setup_groupboxes, setup_tasklists
from widgets.right import setup_trays
from widgets.center import setup_music
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from libqtile import qtile

# from popup_layout import DEFAULT_LAYOUT
from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT
from qtile_extras import widget as widget_extras
from qtile_extras.popup.templates.volume import VOLUME_NOTIFICATION
from qtile_extras.resources import wallpapers
# import qtile_extras.hook

## 0.24
# import qtile_extras
# @qtile_extras.hook.subscribe.mpris_new_track
# async def new_track(metadata):
#     lazy.widget["mpris2"].show_popup()


def setup_bars(IS_WAYLAND: bool, group_names: dict) -> list[Screen]:
    # https://qtile-extras.readthedocs.io/en/stable/manual/ref/widgets.html#pulsevolumeextra
    # https://qtile-extras.readthedocs.io/en/stable/manual/ref/widgets.html#alsawidget

    group_boxes = setup_groupboxes(group_names)
    tasklists = setup_tasklists(group_names)
    trays = setup_trays(group_names, IS_WAYLAND)
    music_widgets = setup_music(group_names)
    return [
        Screen(
            top=bar.Bar(
                [
                    # left
                    widget.CurrentLayoutIcon(
                        padding=0,
                        scale=0.7,
                    ),
                    widget.CurrentLayout(
                        padding=5,
                        fmt="{:4}",
                    ),
                    group_boxes[idx],
                    tasklists[idx],
                    # center
                    # widget.Prompt(),  # <- TODO: popup
                    widget.Spacer(20),
                    *music_widgets[idx],
                    widget.Spacer(bar.STRETCH),
                    widget.Notify(scroll=True, scroll_fixed_width=True, scroll_clear=True, scroll_hide=True, width=200),  # max_chars=25, markup=True
                    *trays[idx],
                    # status_notifier if idx == 0 else copy.copy(status_notifier),
                    # widget_extras.Systray(padding=10, icon_size=20)
                    # if not IS_WAYLAND and idx == max(group_names.keys())
                    # else widget.Spacer(length=0),
                    widget.CPU(
                        format="󰣖  {load_percent:3.1f}%",
                        update_interval=5,
                    ),
                    widget.Memory(
                        # mouse_callbacks={"Button1": lambda: qtile.spawn(terminal + " -e htop")},
                        format="{MemPercent:3.0f}%",
                        # format="{MemUsed: .0f}{mm}",
                        fmt="󰍛  {}",
                        measure_mem="G",
                        update_interval=5,
                    ),
                    widget.Net(
                        format="↓{down:2.0f}{down_suffix} ↑{up:2.0f}{up_suffix}",
                        prefix="M",
                        fmt="󰓅  {}",
                        update_interval=5,
                    ),
                    ###
                    widget.Clock(
                        format=" %a, %b %d - %H:%M",
                    ),
                ],
                size=30,
                background=colors.SolarizedDark[0][0],
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
            wallpaper=str(wallpapers.WALLPAPER_TRIANGLES_ROUNDED),
            wallpaper_mode="fill",
            # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
            # By default we handle these events delayed to already improve performance, however your system might still be struggling
            # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
            x11_drag_polling_rate=60,
        )
        for idx in group_names.keys()
    ]
