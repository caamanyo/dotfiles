from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "wezterm"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod],
    #     "space",
    #     lazy.layout.next(),
    #     desc="Move window focus to other window"),

    # Apps
    Key([mod], "e", lazy.spawn("vscodium"), desc="Open VScodium"),
    Key([mod], "n", lazy.spawn("obsidian"), desc="Start Obsidian"),



    # Rofi keys
    Key([mod], "space", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mod], "c", lazy.spawn(
        "rofi -show calc -modi calc -no-show-match -no-sort"), desc="spawn rofi"),
    Key([mod], "s", lazy.spawn("gnome-screenshot -i"), desc="Screenshot utility"),


    # Change Screen
    Key([mod, "mod1"], "h", lazy.to_screen(1), desc="Switch to left screen."),
    Key([mod, "mod1"], "l", lazy.to_screen(0), desc="Switch to right screen."),
    # Key([mod, "control"], "h", lazy.to_screen(
    #     1), desc="Move focus to left screen."),
    # Key([mod, "control"], "l", lazy.to_screen(
    #     0), desc="Move focus to right screen."),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.swap_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"],
    #     "h",
    #     lazy.layout.grow_left(),
    #     desc="Grow window to the left"),
    # Key([mod, "control"],
    #     "l",
    #     lazy.layout.grow_right(),
    #     desc="Grow window to the right"),
    Key([mod, "control"],
        "k",
        lazy.layout.grow_main(),
        desc="Grow window down"),
    Key([mod, "control"], "j", lazy.layout.shrink_main(), desc="Grow window up"),
    Key([mod, "control"], "h", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod, "control"], "l", lazy.layout.maximize(),
        desc="Toggle maximize windows."),
    Key([mod], "f", lazy.window.toggle_floating(),
        desc="Toggle floating windows."),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Kill window
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    # Swaping windows
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "mod1"], "q", lazy.spawn(
        "/home/miquel/.config/rofi/powermenu.sh"), desc="Powermenu."),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Audio control
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
]
