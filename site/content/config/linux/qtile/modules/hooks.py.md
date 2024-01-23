---
title: My Qtile hooks module
tags:
- config
---

Hooks specific functions to specific Qtile events.

## Imports

````python
import os
import subprocess

from libqtile import hook
````

## Run `autostart.sh` once on startup

````python
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
````
