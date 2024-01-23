---
title: My awesomewm config user-variables.lua
tags:
- config
---

`user-variables.lua` holds my defaults for other contexts:
what terminal to load, which modifier key starts shortcuts, what to edit files with.

Return it as a table that can be held in the global `RC` table.

````lua
local terminal = "wezterm"
local editor = os.getenv("EDITOR") or "nvim"
local editor_cmd = terminal .. " -e " .. editor

local _M = {
    terminal = terminal,
    editor = editor,
    editor_cmd = editor_cmd,
    modkey = "Mod4",
    wallpaper = "/usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png",
}

return _M
````

`Mod4` is the Windows key on most keyboards I see.
