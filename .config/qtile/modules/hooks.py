from libqtile import hook
import subprocess
import os


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


# Send window to specific group
@hook.subscribe.client_new
def func(c):
    if c.window.get_wm_class()[1] == "firefox":
        c.togroup("2")
    if c.window.get_wm_class()[1].__contains__("wezterm"):
        c.togroup("1")
    if c.window.get_wm_class()[0] == "vscodium":
        c.togroup("3")
