---
title: My awesomewm menu.lua
tags:
- config
---

My awesomewm application menu.

````lua
local awful = require("awful")
local hotkeys_popup = require("awful.hotkeys_popup").widget
local beautiful = require("beautiful")
local freedesktop = require("freedesktop")

local M = {}
````

## Awesome-specific actions

The most important stuff —
interacting with Awesome itself.

````lua
M.awesome = {
  {
    "hotkeys",
    function()
      hotkeys_popup.show_help(nil, awful.screen.focused())
    end
  },
  { "manual", RC.vars.terminal .. " -e man awesome" },
  { "edit config", RC.vars.editor_cmd .. " " .. awesome.conffile },
  { "restart", awesome.restart },
  { "quit", function() awesome.quit() end },
}
````

## Applications

I let `freedesktop` build the menu via XDG-related settings.
That's the stuff already in my KDE application menu.
It just loads straight over.
I'll put `awesome_menu` at the top and a quick entry for loading my preferred terminal emulator at the bottom.

````lua
M.main = freedesktop.menu.build(
  {
    before = {
      { "awesome", M.awesome, beautiful.awesome_icon },
    },
    after = {
      { "Terminal", RC.vars.terminal },
    },
  }
)

return M
````
