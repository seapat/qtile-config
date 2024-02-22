{
  pkgs,
  pkgs-unstable,
  lib,
  config,
  ...
}: let
  # qtile-config = pkgs.fetchFromGitHub {
  #   owner = "seapat";
  #   repo = "qtile-config";
  #   rev = "main";
  #   hash = "sha256-JWZIYH80vbTCiDe6rW4BObY1DX7pjfTQ92DTgUx9Whw=";
  # };
  qtile-examples =
    lib.sources.sourceFilesBySuffices
    (
      lib.sources.sourceByRegex
      (pkgs.fetchFromGitHub {
        owner = "qtile";
        repo = "qtile-examples";
        rev = "master";
        hash = "sha256-dwwJBNeU2NFsVF1bwNUlVVPwD9yMTLhyX9nD2Dxmcy0=";
      })
      [".*\.py$"]
    )
    [".py"];
in {
  xdg.configFile = {
    "qtile" = {
      # source = qtile-config;
      source = lib.fileset.toSource {
        root = ./.;
        # only copy python or shell scripts
        fileset = lib.fileset.fileFilter (file: file.hasExt "py" || file.hasExt "sh" || file.hasExt "svg") ./.;
      };
      target = "qtile";
      onChange = "qtile cmd-obj -o cmd -f reload_config || true"; # || true";
      recursive = true;
    };
    "qtile/_plugins" = {
      source = qtile-examples;
      recursive = true;
    };
  };
  home.file = {
    "Github/nixland/modules/home/desktop/qtile/_plugins" = {
      source = qtile-examples;
      recursive = true;
    };
    ".xinitrc" = {
      executable = true;
      inherit (config.home.file.".xsession") text;
    };
  };
  home.packages = [
    pkgs.pulseaudio # required for volume controls in qtile
    # rofi-search
    pkgs-unstable.playerctl
  ];
  xsession.windowManager.command = "exec qtile start -b x11"; # -l INFO";
  xsession = {
    enable = lib.mkDefault true;
    initExtra = ''
      autorandr --change
      # xset dpms 300 600 1800 # seconds till: standby suspend off
      dbus-update-activation-environment --systemd DISPLAY
    '';
  };
  services.playerctld = {
    enable = true;
  };
  # fixes some issues with tray
  systemd.user.targets.tray = {
    Unit = {
      Description = "Home Manager System Tray";
      Requires = ["graphical-session-pre.target"];
    };
  };
  programs.autorandr.enable = true;
}
