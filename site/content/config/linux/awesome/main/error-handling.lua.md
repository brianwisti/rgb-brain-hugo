---
created: 2024-01-15 17:29:21-08:00
tags:
- config
title: My awesomewm config error-handling.lua
updated: 2024-02-01 11:27:39-08:00
---

I'll need to notify about errors.
Loading *naughty* for its notification function.

````lua
local naughty = require("naughty")
````

Check if awesome encountered an error during startup and fell back to another config.

 > 
 > **NOTE**
>
 > This code should only ever execute for the fallback config.

````lua
if awesome.startup_errors then
  naughty.notify({
    preset = naughty.config.presets.critical,
    title = "Oops, there were errors during startup!",
    text = awesome.startup_errors
  })
end
````

Handle runtime errors after an otherwise normal startup.

````lua
do
  local in_error = false
  awesome.connect_signal("debug::error", function (err)
    -- Make sure we don't go into an endless error loop
    if in_error then return end
    in_error = true

    naughty.notify({
      preset = naughty.config.presets.critical,
      title = "Oops, an error happened!",
      text = tostring(err)
    })
    in_error = false
  end)
end
````