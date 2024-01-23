---
title: My awesome theme.lua
tags:
- config
---

Themes define colours, icons, font and wallpapers.

After installing `awesome`,
I can find the default themes under `/usr/share/awesome/themes`.

The builtin themes that come with every awesome install:

* `default`
* `gtk`
* `sky`
* `xresources`
* `zenburn`

Load the theme handler.

````lua
local gears = require("gears")
local awful = require("awful")
local beautiful = require("beautiful")
````

I just want to make sure things work.
Start with one of the built-in themes and reasonable defaults.

````lua
beautiful.init("/usr/share/awesome/themes/zenburn/theme.lua")
beautiful.font = "Noto Sans Regular 12"
beautiful.notification_font = "Noto Sans Bold 16"
beautiful.icon_theme="Papirus-Dark"
````

Set up background wallpaper if there is one — and if the file exists.

````lua
if (RC.vars.wallpaper) then
    local wallpaper = RC.vars.wallpaper
    if awful.util.file_readable(wallpaper) then beautiful.wallpaper = wallpaper end
end

if beautiful.wallpaper then
    for s = 1, screen.count() do
        gears.wallpaper.maximized(beautiful.wallpaper, s, true)
    end
end
````

Add a signal handler to redraw wallpaper when screen resolution changes.

````lua
local function set_wallpaper(s)
    if beautiful.wallpaper then
        local wallpaper = beautiful.wallpaper
        -- If wallpaper is a function, call it with the screen
        if type(wallpaper) == "function" then
            wallpaper = wallpaper(s)
        end
        gears.wallpaper.maximized(wallpaper, s, true)
    end
end

screen.connect_signal("property::geometry", set_wallpaper)
````
