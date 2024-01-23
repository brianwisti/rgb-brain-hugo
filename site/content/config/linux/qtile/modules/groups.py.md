---
title: My Qtile Groups Module
tags:
- config
---

Or screens, or virtual desktops.

## Imports

````python
from libqtile.command import lazy
from libqtile.config import Key, Group

from .keys import keys, mod
````

## Define Screen Groups

The defaults use a simple numbering scheme for its nine groups.

````python
groups = [Group(i) for i in "123456789"]
````

## Add keybindings for each group

* <kbd>Mod+<n></kbd> switches to group `<n>`
* <kbd>Mod+Shift+<n></kbd> moves currently focused window to group `<n>`
* <kbd>Mod+Right</kbd> switches to the group right of current (2 → 3, etc)
* <kbd>Mod+Left</kbd> switches to the group left of current (2 → 1, etc)

The directional switches wrap around.
Group 1 is to the right of group 9, and group 9 is to the left of group 1.

````python
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])
````
