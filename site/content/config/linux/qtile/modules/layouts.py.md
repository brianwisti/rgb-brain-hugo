---
title: My Qtile layouts.py
tags:
- config
---

My preferred layouts for Qtile on my ridiculously wide monitor.

* Columns
* MonadThreeCol
* Floating

Other built-in options that I may evaluate later:

* MonadTall
* Stack
* Bsp
* Matrix
* MonadTall
* MonadWide
* RatioTile
* Tile
* TreeTab
* VerticalTile
* Zoomy

````python
from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.MonadThreeCol(),
]
````

And then a floating layour because some application windows work best floating.

````python
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
````
