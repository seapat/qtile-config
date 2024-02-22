from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from libqtile.config import Mouse

from env import mainMod, terminal
from popups.power_menu import show_power_menu


def setup_binds() -> tuple[list, list]:
    keys: list[Key] = [
        # Reference https://docs.qtile.org/en/latest/manual/config/lazy.html
        Key([mainMod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mainMod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mainMod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mainMod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mainMod], "left", lazy.layout.left(), desc="Move focus to left"),
        Key([mainMod], "right", lazy.layout.right(), desc="Move focus to right"),
        Key([mainMod], "down", lazy.layout.down(), desc="Move focus down"),
        Key([mainMod], "up", lazy.layout.up(), desc="Move focus up"),
        Key(
            [mainMod],
            "space",
            lazy.layout.next(),
            desc="Move window focus to other window",
        ),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key(
            [mainMod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mainMod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key(
            [mainMod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"
        ),
        Key([mainMod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key(
            [mainMod, "shift"],
            "left",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mainMod, "shift"],
            "right",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key(
            [mainMod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"
        ),
        Key([mainMod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key(
            [mainMod, "control"],
            "h",
            lazy.layout.grow_left(),
            desc="Grow window to the left",
        ),
        Key(
            [mainMod, "control"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key(
            [mainMod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"
        ),
        Key([mainMod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mainMod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mainMod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([mainMod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([mainMod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mainMod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key(
            [mainMod],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
        ),
        Key(
            [mainMod],
            "t",
            lazy.window.toggle_floating(),
            desc="Toggle floating on the focused window",
        ),
        Key([mainMod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mainMod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        # Sound
        Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_SINK@ toggle")),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("wpctl set-volume -l '1.25' @DEFAULT_AUDIO_SINK@ 5%-"),
        ),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("wpctl set-volume -l '1.25' @DEFAULT_AUDIO_SINK@ 5%+"),
        ),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
        # Key([], "XF86AudioPlay", lazy.spawn("playerctl play")),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        Key([], "XF86AudioStop", lazy.spawn("playerctl pause")),
        Key([mainMod, "shift"], "q", lazy.function(show_power_menu)),
        
        ## Rofi
        # Key(
        #     [mainMod],
        #     "r",
        #     lazy.spawncmd(),
        #     desc="Spawn a command using a prompt widget",
        # ),
        Key([mainMod], "r", lazy.spawn("rofi -show drun")),
        # Key([mainMod], "v", lazy.spawn("rofi -modi clipboard:${cliphist-rofi-img}/bin/cliphist-rofi-img -show clipboard -show-icons")),
        # Key(["ALT"], "r", lazy.spawn("pkill ${launcher} || ${launcher} -show run")),

    ]
    mouse: list[Mouse] = [
        Drag(
            [mainMod],
            "Button1",
            # lazy.window.set_position_floating(), # change window to floating, then move around
            lazy.window.set_position(), # swap windows within tiled layouts
            start=lazy.window.get_position(),
        ),
        Drag(
            [mainMod],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([mainMod], "Button2", lazy.window.bring_to_front()),
    ]

    return keys, mouse

# XF86AudioRaiseVolume
# XF86AudioLowerVolume
# XF86AudioMute
# XF86AudioNext
# XF86AudioPrev
# XF86AudioPlay
# XF86MonBrightnessUp
# XF86MonBrightnessDown
