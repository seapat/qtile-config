import os

from libqtile.utils import guess_terminal
from libqtile import qtile

IS_XEPHYR: bool = int(os.environ.get("QTILE_XEPHYR", 0)) > 0

mainMod: str = "mod4"
terminal: str = "kitty"

def setup_environment(IS_WAYLAND: bool) -> None:
    if IS_WAYLAND:
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        os.environ["QT_QPA_PLATFORMTHEME"] = "wayland;xcb"
        os.environ["QT_WAYLAND_DISABLE_WINDOWDECORATION"] = "1"
        os.environ["WLR_NO_HARDWARE_CURSORS"] = "1"
        os.environ["NIXOS_OZONE_WL"] = "1"
        os.environ["XDG_SESSION_TYPE"] = "wayland"
        os.environ["GDK_BACKEND"] = "wayland,x11"
        os.environ["GBM_BACKEND"] = "nvidia-drm"
        os.environ["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
        os.environ["LIBVA_DRIVER_NAME"] = "nvidia"
        os.environ["__GL_GSYNC_ALLOWED"] = "0"
        os.environ["__GL_VRR_ALLOWED"] = "0"
        os.environ["WLR_DRM_NO_ATOMIC"] = "1"
        os.environ["WLR_RENDERER"] = "vulkan"
    else:
        return