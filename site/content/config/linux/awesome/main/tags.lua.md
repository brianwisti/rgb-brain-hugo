---
title: My awesome tags.lua
tags:
- config
---

Awesome uses string tags to enumerate and identify virtual desktops.

````lua
local awful = require("awful")

local _M = {}
local tag_names = { "1", "2", "3", "4", "5" }

awful.screen.connect_for_each_screen(function(s)
  _M[s] = awful.tag(tag_names, s, RC.layouts[1])
end)

return _M
````
