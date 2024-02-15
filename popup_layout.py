from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT
from qtile_extras.popup.toolkit import (
    PopupSlider,
    PopupText,
)

DEFAULT_LAYOUT.controls = list(
    # remove old progress bar, replace with shorter one w/ space for text
    filter(lambda x: x.name != "progress", DEFAULT_LAYOUT.controls)
) + [
    progress_bar := PopupSlider(
        name="progress", pos_x=0.2, pos_y=0.6, width=0.6, height=0.1, marker_size=0
    ),
    PopupText(
        "",
        name="position",
        pos_x=progress_bar.pos_x,
        pos_y=progress_bar.pos_y,
        width=0.1,
        height=progress_bar.height,
        h_align="left",
        v_align="top",
    ),
    PopupText(
        "",
        name="length",
        pos_x=progress_bar.pos_x,
        pos_y=progress_bar.pos_y,
        width=0.1,
        height=progress_bar.height,
        h_align="right",
        v_align="top",
    ),
]


# Alternatively, if you select the `popup` mode then no widget will
# appear on the bar and, instead, a small popup will be displayed.
# 
# The layout of the popup can be customised via the `popup_layout` parameter.
# Users should provide a _PopupLayout object. The layout should have at least one
# of the following controls: a PopupSlider named `volume` and a PopupText control
# named `text` as these controls will be updated whenever the volume changes.

# AUDIO_POPUP