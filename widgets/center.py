from libqtile import widget
from qtile_extras import widget as widget_extras
from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT
from libqtile.lazy import lazy

import copy

def setup_music(group_names: dict[int, tuple]) -> dict[int, tuple[widget.base._Widget, widget.base._Widget]]:
    return {
        screen: (
            widget_extras.Mpris2(
                # name="mpris",
                no_metadata_text="missing metadata",
                scroll=False,  # needs width
                format="{xesam:title} {xesam:artist}",
                popup_layout=DEFAULT_LAYOUT,
                paused_text="  {track}",  # 
                playing_text="  {track}",  #   󰝚
                stopped_text="  {track}",  # 
                mouse_callbacks={
                    "Button3": lazy.widget["mpris2"].toggle_player(),
                    # "Button2": lazy.widget["mpris2"].force_update(),
                    "Button2": lazy.spawn("pavucontrol"),
                }
            ),
            widget_extras.PulseVolumeExtra(
                # emoji = True,
                # emoji_list=["󰝟", "", "", ""],
                mode="bar",
                bar_text="Audio",
                paused_text="󰏤 {track}",  #  
                playing_text="󰐊 {track}",  #  
                hide_interval=10,
                limit_max_volume=True,
                # volume_app="wpctl",
                # volume_down_command="wpctl set-volume -l '1.25' @DEFAULT_AUDIO_SINK@ 5%-",
                # volume_up_command="wpctl set-volume -l '1.25' @DEFAULT_AUDIO_SINK@ 5%+",
                # mute_command="wpctl set-mute @DEFAULT_SINK@ toggle",
                # get_volume_command = "wpctl get-volume @DEFAULT_AUDIO_SINK@"
            ),
        )
        for screen in group_names.keys()
    }


