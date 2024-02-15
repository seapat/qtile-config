from libqtile.config import Match
from libqtile.backend.base.window import Window
from libqtile.layout import columns, floating, max, tree, matrix, stack, base

import re
import colors


def setup_layouts() -> list[base.Layout]:
    return [
        max.Max(),
        # tree.TreeTab(
        #     # sections = ["ONE", "TWO", "THREE"],
        #     # border_width=1,
        #     # fontsize=12,
        #     # vspace=1,
        #     # panel_width=100,
        #     # place_right=False,
        #     # previous_on_rm=True,
        #     bg_color=colors.SolarizedDark[0][0]
        # ),
        # stack.Stack(num_stacks=2),
        matrix.Matrix(),
        columns.Columns(
            # border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1, split=False
        ),
    ]


def setup_floating_layout() -> floating.Floating:
    # use `xprop`+`lmb` to find more on x11
    return floating.Floating(
        border_width=1,
        border_focus="#ff0000",
        # border_normal="00000000",
        fullscreen_border_width=0,
        float_rules=[
            *floating.Floating.default_float_rules,
            Match(func=lambda c: bool(c.is_transient_for())),
            Match(func=Window.has_fixed_ratio),
            Match(func=Window.has_fixed_size),
            Match(role="gimp-file-export"),
            Match(title="Bluetooth Devices"),
            Match(title="branchdialog"),  # gitk
            Match(title="File Operation Progress", wm_class=re.compile("[Tt]hunar")),
            Match(title="Firefox — Sharing Indicator"), 
            Match(title="Picture-in-Picture"), # firefox
            Match(title="KDE Connect Daemon"),
            Match(title="KeePassXC -  Access Request"),
            Match(title="Open File"),
            Match(title="pinentry"),  # GPG key password entry
            Match(title="Unlock Database - KeePassXC"),
            Match(title=re.compile("Presenting: .*"), wm_class="libreoffice-impress"),
            Match(wm_class="Arandr"),
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="Dragon-drag-and-drop"),
            Match(wm_class="Dragon"),
            Match(wm_class="eog"),
            Match(wm_class="file_progress"),
            Match(wm_class="imv"),
            Match(wm_class="lxappearance"),
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="matplotlib"),
            Match(wm_class="mpv"),
            Match(wm_class="umpv"),
            Match(wm_class="nm-connection-editor"),
            Match(wm_class="notification"),
            Match(wm_class="org.gnome.clocks"),
            Match(wm_class="org.kde.ark"),
            Match(wm_class="pavucontrol"),
            Match(wm_class="Pinentry-gtk-2"),
            Match(wm_class="qt5ct"),
            Match(wm_class="ssh-askpass"),
            Match(wm_class="thunar"),
            Match(wm_class="tridactyl"),
            Match(wm_class="wdisplays"),
            Match(wm_class="wlroots"),
            Match(wm_class="Xephyr"),
            Match(wm_class="zoom"),
            Match(wm_class="kdenlive"), 
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(wm_class="Yad"),  # yad boxes
            Match(title="Confirmation"),  # tastyworks exit box
            Match(title="Qalculate!"),  # qalculate-gtk
            Match(title="Friends List") # Steam
        ],
    )
