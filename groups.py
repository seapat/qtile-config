from libqtile.config import Group, Key
from bindings import mainMod
from libqtile.lazy import lazy
from libqtile import widget


def setup_groupboxes(group_names: dict[int, tuple]):
    # widgets: dict[int, widget.GroupBox] = {}
    # for screen, names in group_names.items():
    #     widgets[screen] = widget.GroupBox(
    #         highlight_method="block",
    #         visible_groups=[str(name) for name in names],
    #         hide_unused=False,
    #         disable_drag=True,
    #     )
    return {
        screen: widget.GroupBox(
            highlight_method="block",
            urgent_alert_method="line",
            visible_groups=[str(name) for name in names],
            hide_unused=False,
            disable_drag=True,
            invert_mouse_wheel=True, # wheel up moves to higher group
            toggle=False, # ? maybe deactivates "jump back" on "double activation" feautre?
        )
        for screen, names in group_names.items()
    }


def setup_groups(keys: list[Key], group_names: dict[int, tuple]) -> list[Group]:
    # FIXME: should we move this to function scope? allows to be removed by gc but needs to be recomputed on call
    inv_map = {
        str(name): screen for screen, names in group_names.items() for name in names
    }

    def go_to_group(name: str, group_names: dict):
        def _inner(qtile):
            if len(qtile.screens) == 1:
                qtile.groups_map[name].toscreen()
                return

            qtile.focus_screen(inv_map[name])
            qtile.groups_map[name].toscreen()

        return _inner

    groups = []
    for screen, names in group_names.items():
        for grp_name in names:
            groups.append(Group(name=str(grp_name), screen_affinity=int(screen)))

    for grp in groups:
        keys.extend(
            [
                Key(
                    [mainMod],
                    grp.name,
                    lazy.function(go_to_group(grp.name, group_names)),
                    desc="Switch to group {}".format(grp.name),
                ),
                Key(
                    [mainMod, "shift"],
                    grp.name,
                    lazy.window.togroup(grp.name, switch_group=False),
                    desc="Silently move focused window to group {}".format(grp.name),
                ),
            ]
        )

    return groups

    # @hook.subscribe.screens_reconfigured
    # async def _():
    #     if len(qtile.screens) > 1:
    #         groupbox[0].visible_groups = groups1
    #     else:
    #         groupbox[0].visible_groups = group_names
    #     if hasattr(groupbox[0], "bar"):
    #         groupbox[0].bar.draw()
