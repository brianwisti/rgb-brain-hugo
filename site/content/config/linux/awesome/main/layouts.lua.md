---
title: My awesomewm layouts.lua
tags:
- config
---

[`awful.layout`](https://awesomewm.org/apidoc/libraries/awful.layout.html#) provides predefined approaches to organizing
windows. I specify which ones to use, leaving out those which aren't useful on
my ludicrously wide monitor.

Eventually I need to come up with my own layout, because I can be *very* fussy.

````lua
local awful = require("awful")
local lain = require("lain")
````

Mainly got the *lain* centerwork in there for my wide monitor.
I want to cut down on the total layout selection.
I don't use many of these.

````lua
local _M = {
    lain.layout.centerwork,
    awful.layout.suit.floating,
    awful.layout.suit.tile,
    awful.layout.suit.tile.left,
    awful.layout.suit.fair,
    awful.layout.suit.fair.horizontal,
    awful.layout.suit.spiral,
    awful.layout.suit.spiral.dwindle,
    awful.layout.suit.magnifier,
    awful.layout.suit.corner.nw,
}

return _M
````
