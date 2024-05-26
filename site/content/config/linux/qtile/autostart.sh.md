---
title: My Qtile autostart.sh
tags:
- config
created: 2024-01-15T17:29:21-08:00
updated: 2024-05-01T22:39:25-07:00
---

Fires up tasks and applications which should run for every session.
I skip the battery check from the default setup since I am running on a plugged-in desktop.

````sh
#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
````
