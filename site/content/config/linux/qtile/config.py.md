---
title: My Qtile config.py
tags:
- config
---

This is the entry point for a Qtile session.

Do system imports.

````python
import os
````

Import the useful bits from my config modules.

````python
from modules import const
from modules.groups import groups
from modules.hooks import *
from modules.keys import keys, mod
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens
````

I don't like that `import *`.
Gonna see if I *really* need to do it that way.

````python
dgroups_key_binder = None
dgroups_app_rules = []  # type: List

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
widget_defaults = dict(
        font=const.FONT_FAMILY_FIXED,
        fontsize=13,
        padding=3
)
````
