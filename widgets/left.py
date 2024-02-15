from libqtile import widget
from libqtile.lazy import lazy

def setup_groupboxes(group_names: dict[int, tuple]) -> dict[int, widget.GroupBox]:
    widgets: dict[int, widget.GroupBox] = {}
    for screen, names in group_names.items():
        widgets[screen] = widget.GroupBox(
            highlight_method="block",
            visible_groups=[str(name) for name in names],
            hide_unused=False,
            disable_drag=True,
        )

    return widgets


def setup_layout_indicators(group_names: dict[int, tuple]) -> dict[int, tuple[widget.base._TextBox, widget.base._TextBox]]:
    return {
        screen: (
            widget.CurrentLayoutIcon(
                padding=0,
                scale=0.7,
            ),
            widget.CurrentLayout(padding=5),
        )
        for screen in group_names.keys()
    }


def setup_tasklists(group_names: dict[int, tuple]) -> dict[int, widget.TaskList]:
    return {
        screen: widget.TaskList(
            txt_floating="🗗",
            txt_maximized="🗖",
            txt_minimized=" ",  #   🗕
            # parse_text= TODO: function that only gets more genric name e.g. "firefox"
            max_title_width=100,
            highlight_method="block",
            mouse_callbacks={
                # Button1 is set by default
                "Button2": lazy.window.kill(),
                "Button3": lazy.window.toggle_floating(),
            }
        )
        for screen in group_names.keys()
    }
