#!/bin/sh
numlockx &
feh --bg-fill --randomize /usr/share/endeavouros/backgrounds/eos_wallpapers_community/* & disown
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
# ~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

# Monitor setup
~/.screenlayout/monitor-setup.sh & disown
# xrandr --output DP-2 --mode 1920x1080 -r 144.00