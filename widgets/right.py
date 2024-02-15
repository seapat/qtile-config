from libqtile import widget

from qtile_extras import widget as widget_extras

def setup_monitor_widgets(
    group_names: dict[int, tuple],
) -> dict[int, list[widget.base.ThreadPoolText]]:
    return {
        screen: [
            widget.CPU(
                format="󰣖  {load_percent:3.1f}%",
                update_interval=5,
            ),
            # widget.DF(
            #     update_interval=60*10,
            #     # mouse_callbacks={"Button1": lambda: qtile.spawn(terminal + " -e df")},
            #     partition="/",
            #     # format = '[{p}] {uf}{m} ({r:.0f}%)',
            #     format="{uf}{m} free",
            #     fmt="🖴  Disk: {}",
            #     visible_on_warn=False,
            # ),
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
                fmt="{}",  # 󰓅
                update_interval=5,
            ),
        ]
        for screen in group_names.keys()
    }


def setup_trays(
    group_names: dict[int, tuple], IS_WAYLAND: bool
) -> dict[int, list[widget_extras.Systray | widget_extras.StatusNotifier]]:
    trays: dict[int, list[widget_extras.Systray | widget_extras.StatusNotifier]] = {
        screen: [widget_extras.StatusNotifier(padding=10, icon_size=18)] for screen in group_names.keys()
    }
    if not IS_WAYLAND:
        trays[max(group_names.keys())].append(
            widget_extras.Systray(padding=10, icon_size=20)
        )
    return trays


def setup_clock(
    group_names: dict[int, tuple],
) -> dict[int, list[widget.base.ThreadPoolText]]:
    # TODO: popup calendar?
    return {
        screen: widget.Clock(
            format=" %a, %b %d - %H:%M",
        )
        for screen in group_names.keys()
    }
