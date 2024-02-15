# https://uxwing.com/ https://www.svgrepo.com/ https://flaticons.net/
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
from libqtile.lazy import lazy

import colors

from pathlib import Path
pwd = str(Path(__file__).parent.resolve())

def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename=pwd+"/assets/lock.svg",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            background="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("/path/to/lock_cmd")
            }
        ),
        PopupImage(
            filename=pwd+"/assets/moon.svg",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            background="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("/path/to/sleep_cmd")
            }
        ),
        PopupImage(
            filename=pwd+"/assets/door.svg",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            background="A00000",
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupText(
            text="Lock",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background=colors.SolarizedDark[0][0],
        opacity=0.5,
        initial_focus=None,
    )

    layout.show(centered=True)