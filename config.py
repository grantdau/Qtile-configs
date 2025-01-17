import os
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# --- Startup hooks ---
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    os.system(f'{home}/.screenlayout/monitor_setup.sh')
    os.system(f'feh --bg-fill {home}/Pictures/wallpaper.jpg')

@hook.subscribe.client_new
def float_mediawriter(window):
    if window.window.get_wm_class() == ('mediawriter', 'Mediawriter'):
        window.cmd_toggle_floating()

# --- Variables ---
mod = "mod4"
terminal = "alacritty"

# --- Keybindings ---
keys = [
    # Monitor control
    # Corrected: Left moves to DP-2 (screen 1), Right moves to HDMI-0 (screen 0)
    Key(["mod4", "shift"], "Right", lazy.window.toscreen(0), desc="Move window to HDMI-0"),
    Key(["mod4", "shift"], "Left", lazy.window.toscreen(1), desc="Move window to DP-2"),
    Key(["mod4"], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key(["mod4"], "comma", lazy.prev_screen(), desc="Move focus to previous monitor"),

    # Application launching
    Key([mod, "shift"], "s", lazy.spawn("steam"), desc="Launch Steam"),
    Key([mod], "s", lazy.spawn("flatpak run com.spotify.Client"), desc="Launch Spotify"),
    Key([mod], "i", lazy.spawn("brave-browser"), desc="Launch Brave Browser"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch Rofi in drun mode"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch Alacritty"),

    # Window management
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Qtile management
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Media keys
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause media"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous track"),

    # VT switching in Wayland
    *[Key(["control", "mod1"], f"f{vt}", lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
         desc=f"Switch to VT{vt}") for vt in range(1, 8)]
]

# --- Groups ---
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc=f"Switch to & move focused window to group {i.name}"),
    ])

# --- Layouts ---
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Other layouts can be added here
]

# --- Widgets ---
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# --- Screens ---
screens = [
    Screen(  # Primary screen with the bar (HDMI-0)
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={"launch": ("#ff0000", "#ffffff")},
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Clock(format="%m/%d/%Y %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
    Screen(),  # Secondary screen without a bar (DP-2)
]

# --- Mouse bindings ---
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# --- Other configurations ---
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"
