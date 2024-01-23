---
title: My rc.lua for awesome
aliases:
- /config/awesome/rc.lua/
tags:
- config
---

The source code for my [awesome](https://awesomewm.org/) window manager config.
It started with the default `rc.lua` and expanded from there —
with frequent checks at [My first Awesome](https://awesomewm.org/apidoc/documentation/07-my-first-awesome.md.html#) and Epsi's [step
by step guide](https://epsi-rns.github.io/desktop/2019/06/15/awesome-overview.html).

My awesome config started as a single `rc.lua`.
Breaking this down into modules is an ongoing process.

## Require the important libraries

If the Lua package manager [LuaRocks](https://luarocks.org/) is installed, make sure that
packages installed through it are found (e.g. lgi). If LuaRocks is not
installed, do nothing.

````lua
pcall(require, "luarocks.loader")
````

First I load the standard awesome library.

`gears`
: utility library for color parsing and objects

`awful`
: everything related to window management

`awful.autofocus`
: support for autofocus, I'm guessing

````lua
local gears = require("gears")
local awful = require("awful")
require("awful.autofocus")
````

Then a couple of libraries for widgets and themes.

[`wibox`](https://awesomewm.org/apidoc/popups_and_bars/wibox.html#)
: Awesome's built-in generic widget framework

[`beautiful`](https://awesomewm.org/apidoc/theme_related_libraries/beautiful.html)
: Awesome's build-in theme library

````lua
local wibox = require("wibox")
local beautiful = require("beautiful")
````

Libraries for some of the more refined behaviors we expect from a desktop these
days.

[`naughty`](https://awesomewm.org/apidoc/libraries/naughty.html#)
: notification handling

[`menubar`](https://awesomewm.org/apidoc/popups_and_bars/menubar.html#)
: [XDG](https://specifications.freedesktop.org/mime-apps-spec/mime-apps-spec-latest.html) application menu

[`awful.hotkeys_popup`](https://specifications.freedesktop.org/mime-apps-spec/mime-apps-spec-latest.html)
: The awesome help widget, explaining the hotkeys currently available

````lua
local naughty = require("naughty")
local menubar = require("menubar")
local hotkeys_popup = require("awful.hotkeys_popup")
````

Enable hotkeys help widget for VIM and other apps when client with a matching
name is opened:

````lua
require("awful.hotkeys_popup.keys")
````

### Additional modules

Freedesktop so I can have a full application menu.

````lua
local freedesktop = require("freedesktop")
````

[lain]'s `centerwork` layout seems be working nice with my ludicrously wide
monitor.

````lua
local lain = require("lain")
````

## User preference variables

Refactored to \[`user-variables.lua`\]\[user-variables\].

````lua
RC = {}
RC.vars = require("main.user-variables")
````

I use a couple of values from `RC.vars` pretty frequently.
May as well pull them into the local namespace.

````lua
local editor_cmd = RC.vars.editor_cmd
local modkey = RC.vars.modkey
````

## Error handling

Refactored out to \[`error-handling.lua`\]\[error-handling\].

\[user-variables\]: {{\< ref "config/linux/awesome/main/user-variables.lua.md" >}}
\[error-handling\]: {{\< ref "config/linux/awesome/main/error-handling.lua.md" >}}

## Autostart

For [dex](https://github.com/jceb/dex).

````lua
awful.spawn.with_shell(
  'systemctl --user start autostart.target'
)
````

## Widgets

Pavel Makhov's [Awesome WM Widgets](https://pavelmakhov.com/awesome-wm-widgets/) has several
goodies.

````sh
//- clone the Awesome WM Widgets repo
git clone \
  git@github.com:streetturtle/awesome-wm-widgets.git \
  ~/.config/awesome/awesome-wm-widgets
````

I'll start with the volume widget.

````lua
local volume_widget = require("awesome-wm-widgets.volume-widget.volume")
````

### Themes

Refactored to \[`theme.lua`\]\[theme\].

\[theme\]: {{\< ref "config/linux/awesome/main/theme.lua.md" >}}

````lua
local theme = require("main.theme")
````

### Layouts and tags

Layouts are defined over in \[`layouts.lua`\]\[layouts\].

\[layouts\]: {{\< ref "config/linux/awesome/main/layous.lua.md" >}}

````lua
RC.layouts = require("main.layouts")
awful.layout.layouts = RC.layouts
````

Awesome uses string tags to enumerate and identify virtual desktops.

````lua
local tags = require("main.tags")
````

## Menu

A handy-dandy application and system menu so I don't have to define and
memorize hotkeys for *everything*.

````lua
local menu = require("main.menu")
````

Adding a menu launcher widget.
Because I'll need some way to get *at* the menu I just loaded.
This goes in by widget bar later.

````lua
menu_launcher = awful.widget.launcher(
  {
    image = beautiful.awesome_icon,
    menu = menu.main,
  }
)

-- Menubar configuration
menubar.utils.terminal = RC.vars.terminal -- Set the terminal for applications that require it
````

## Keyboard map indicator and switcher

````lua
mykeyboardlayout = awful.widget.keyboardlayout()
````

## Wibar

Create a textclock widget.

````lua
mytextclock = wibox.widget.textclock()
````

Create a wibox for each screen and add it.

First we need buttons for all the tags.

````lua
local taglist_buttons = gears.table.join(
  awful.button({ }, 1, function(t) t:view_only() end),
  awful.button({ modkey }, 1,
    function(t)
      if client.focus then
        client.focus:move_to_tag(t)
      end
    end
  ),
  awful.button({ }, 3, awful.tag.viewtoggle),
  awful.button(
    { modkey }, 3,
    function(t)
      if client.focus then
        client.focus:toggle_tag(t)
      end
    end
  ),
  awful.button({ }, 4, function(t) awful.tag.viewnext(t.screen) end),
  awful.button({ }, 5, function(t) awful.tag.viewprev(t.screen) end)
)
````

Now we need buttons for all the tasks.

````lua
local tasklist_buttons = gears.table.join(
  awful.button(
    { }, 1,
    function (c)
      if c == client.focus then
        c.minimized = true
      else
        c:emit_signal(
          "request::activate",
          "tasklist",
          {raise = true}
        )
      end
    end
  ),
  awful.button(
    { }, 3,
    function()
      awful.menu.client_list({ theme = { width = 250 } })
    end
  ),
  awful.button(
    { }, 4,
    function ()
      awful.client.focus.byidx(1)
    end
  ),
  awful.button(
    { }, 5,
    function ()
      awful.client.focus.byidx(-1)
    end
  )
)
````

Tie everything together for each screen.

````lua
awful.screen.connect_for_each_screen(
  function(s)
    -- Create a promptbox for each screen
    s.mypromptbox = awful.widget.prompt()
    -- Create an imagebox widget which will contain an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(gears.table.join(
                           awful.button({ }, 1, function () awful.layout.inc( 1) end),
                           awful.button({ }, 3, function () awful.layout.inc(-1) end),
                           awful.button({ }, 4, function () awful.layout.inc( 1) end),
                           awful.button({ }, 5, function () awful.layout.inc(-1) end)))
    -- Create a taglist widget
    s.mytaglist = awful.widget.taglist {
        screen  = s,
        filter  = awful.widget.taglist.filter.all,
        buttons = taglist_buttons
    }

    -- Create a tasklist widget
    s.mytasklist = awful.widget.tasklist {
        screen  = s,
        filter  = awful.widget.tasklist.filter.currenttags,
        buttons = tasklist_buttons
    }

    // ==> Create wibox for this screen.
  end
)
````

Create the wibox and add its widgets. This is where I add the volume control I
required earlier.

````lua
//- Create wibox for this screen
s.mywibox = awful.wibar({ position = "top", screen = s })
s.mywibox:setup {
    layout = wibox.layout.align.horizontal,
    { -- Left widgets
        layout = wibox.layout.fixed.horizontal,
        menu_launcher,
        s.mytaglist,
        s.mypromptbox,
    },
    s.mytasklist, -- Middle widget
    { -- Right widgets
        layout = wibox.layout.fixed.horizontal,
        mykeyboardlayout,
        wibox.widget.systray(),
        volume_widget(),
        mytextclock,
        s.mylayoutbox,
    },
}
````

## Mouse bindings

````lua
root.buttons(gears.table.join(
    awful.button({ }, 3, function () menu.main:toggle() end),
    awful.button({ }, 4, awful.tag.viewnext),
    awful.button({ }, 5, awful.tag.viewprev)
))
````

## Key bindings

````lua
global_keys = gears.table.join(
    awful.key({ modkey,           }, "s",      hotkeys_popup.show_help,
              {description="show help", group="awesome"}),
    awful.key({ modkey,           }, "Left",   awful.tag.viewprev,
              {description = "view previous", group = "tag"}),
    awful.key({ modkey,           }, "Right",  awful.tag.viewnext,
              {description = "view next", group = "tag"}),
    awful.key({ modkey,           }, "Escape", awful.tag.history.restore,
              {description = "go back", group = "tag"}),

    awful.key({ modkey,           }, "j",
        function ()
            awful.client.focus.byidx( 1)
        end,
        {description = "focus next by index", group = "client"}
    ),
    awful.key({ modkey,           }, "k",
        function ()
            awful.client.focus.byidx(-1)
        end,
        {description = "focus previous by index", group = "client"}
    ),
    awful.key({ modkey,           }, "w", function () menu.main:show() end,
              {description = "show main menu", group = "awesome"}),

    -- Layout manipulation
    awful.key({ modkey, "Shift"   }, "j", function () awful.client.swap.byidx(  1)    end,
              {description = "swap with next client by index", group = "client"}),
    awful.key({ modkey, "Shift"   }, "k", function () awful.client.swap.byidx( -1)    end,
              {description = "swap with previous client by index", group = "client"}),
    awful.key({ modkey, "Control" }, "j", function () awful.screen.focus_relative( 1) end,
              {description = "focus the next screen", group = "screen"}),
    awful.key({ modkey, "Control" }, "k", function () awful.screen.focus_relative(-1) end,
              {description = "focus the previous screen", group = "screen"}),
    awful.key({ modkey,           }, "u", awful.client.urgent.jumpto,
              {description = "jump to urgent client", group = "client"}),
    awful.key({ modkey,           }, "Tab",
        function ()
            awful.client.focus.history.previous()
            if client.focus then
                client.focus:raise()
            end
        end,
        {description = "go back", group = "client"}),

    -- Standard program
    awful.key({ modkey,           }, "Return", function () awful.spawn(RC.vars.terminal) end,
              {description = "open a terminal", group = "launcher"}),
    awful.key({ modkey, "Control" }, "r", awesome.restart,
              {description = "reload awesome", group = "awesome"}),
    awful.key({ modkey, "Shift"   }, "q", awesome.quit,
              {description = "quit awesome", group = "awesome"}),

    awful.key({ modkey,           }, "l",     function () awful.tag.incmwfact( 0.05)          end,
              {description = "increase master width factor", group = "layout"}),
    awful.key({ modkey,           }, "h",     function () awful.tag.incmwfact(-0.05)          end,
              {description = "decrease master width factor", group = "layout"}),
    awful.key({ modkey, "Shift"   }, "h",     function () awful.tag.incnmaster( 1, nil, true) end,
              {description = "increase the number of master clients", group = "layout"}),
    awful.key({ modkey, "Shift"   }, "l",     function () awful.tag.incnmaster(-1, nil, true) end,
              {description = "decrease the number of master clients", group = "layout"}),
    awful.key({ modkey, "Control" }, "h",     function () awful.tag.incncol( 1, nil, true)    end,
              {description = "increase the number of columns", group = "layout"}),
    awful.key({ modkey, "Control" }, "l",     function () awful.tag.incncol(-1, nil, true)    end,
              {description = "decrease the number of columns", group = "layout"}),
    awful.key({ modkey,           }, "space", function () awful.layout.inc( 1)                end,
              {description = "select next", group = "layout"}),
    awful.key({ modkey, "Shift"   }, "space", function () awful.layout.inc(-1)                end,
              {description = "select previous", group = "layout"}),

    awful.key({ modkey, "Control" }, "n",
              function ()
                  local c = awful.client.restore()
                  -- Focus restored client
                  if c then
                    c:emit_signal(
                        "request::activate", "key.unminimize", {raise = true}
                    )
                  end
              end,
              {description = "restore minimized", group = "client"}),

    -- Prompt
    awful.key({ modkey },            "r",     function () awful.screen.focused().mypromptbox:run() end,
              {description = "run prompt", group = "launcher"}),

    awful.key({ modkey }, "x",
              function ()
                  awful.prompt.run {
                    prompt       = "Run Lua code: ",
                    textbox      = awful.screen.focused().mypromptbox.widget,
                    exe_callback = awful.util.eval,
                    history_path = awful.util.get_cache_dir() .. "/history_eval"
                  }
              end,
              {description = "lua execute prompt", group = "awesome"}),
    -- Menubar
    awful.key({ modkey }, "p", function() menubar.show() end,
              {description = "show the menubar", group = "launcher"})
)

clientkeys = gears.table.join(
    awful.key({ modkey,           }, "f",
        function (c)
            c.fullscreen = not c.fullscreen
            c:raise()
        end,
        {description = "toggle fullscreen", group = "client"}),
    awful.key({ modkey, "Shift"   }, "c",      function (c) c:kill()                         end,
              {description = "close", group = "client"}),
    awful.key({ modkey, "Control" }, "space",  awful.client.floating.toggle                     ,
              {description = "toggle floating", group = "client"}),
    awful.key({ modkey, "Control" }, "Return", function (c) c:swap(awful.client.getmaster()) end,
              {description = "move to master", group = "client"}),
    awful.key({ modkey,           }, "o",      function (c) c:move_to_screen()               end,
              {description = "move to screen", group = "client"}),
    awful.key({ modkey,           }, "t",      function (c) c.ontop = not c.ontop            end,
              {description = "toggle keep on top", group = "client"}),
    awful.key({ modkey,           }, "n",
        function (c)
            -- The client currently has the input focus, so it cannot be
            -- minimized, since minimized clients can't have the focus.
            c.minimized = true
        end ,
        {description = "minimize", group = "client"}),
    awful.key({ modkey,           }, "m",
        function (c)
            c.maximized = not c.maximized
            c:raise()
        end ,
        {description = "(un)maximize", group = "client"}),
    awful.key({ modkey, "Control" }, "m",
        function (c)
            c.maximized_vertical = not c.maximized_vertical
            c:raise()
        end ,
        {description = "(un)maximize vertically", group = "client"}),
    awful.key({ modkey, "Shift"   }, "m",
        function (c)
            c.maximized_horizontal = not c.maximized_horizontal
            c:raise()
        end ,
        {description = "(un)maximize horizontally", group = "client"})
)

-- Bind all key numbers to tags.
-- Be careful: we use keycodes to make it work on any keyboard layout.
-- This should map on the top row of your keyboard, usually 1 to 9.
for i = 1, 9 do
  global_keys = gears.table.join(
    global_keys,
    -- View tag only.
    awful.key(
      { modkey }, "#" .. i + 9,
      function ()
        local screen = awful.screen.focused()
        local tag = screen.tags[i]
        if tag then
          tag:view_only()
        end
      end,
      {description = "view tag #"..i, group = "tag"}
    ),
    -- Toggle tag display.
    awful.key(
      { modkey, "Control" }, "#" .. i + 9,
      function ()
        local screen = awful.screen.focused()
        local tag = screen.tags[i]
        if tag then
          awful.tag.viewtoggle(tag)
        end
      end,
      {description = "toggle tag #" .. i, group = "tag"}
    ),
    awful.key(
      { modkey, "Control" }, "=",
      function () lain.util.useless_gaps_resize(1) end,
      {description = "increase window gaps on tag #" .. i, group = "tag"}
    ),
    awful.key(
      { modkey, "Control" }, "-",
      function () lain.util.useless_gaps_resize(-1) end,
      {description = "decrease window gaps on tag #" .. i, group = "tag"}
    ),
    -- Move client to tag.
    awful.key(
      { modkey, "Shift" }, "#" .. i + 9,
      function ()
        if client.focus then
          local tag = client.focus.screen.tags[i]
          if tag then
            client.focus:move_to_tag(tag)
          end
        end
      end,
      {description = "move focused client to tag #"..i, group = "tag"}
    ),
    -- Toggle tag on focused client.
    awful.key(
      { modkey, "Control", "Shift" }, "#" .. i + 9,
      function ()
        if client.focus then
          local tag = client.focus.screen.tags[i]
          if tag then
            client.focus:toggle_tag(tag)
          end
        end
      end,
      {description = "toggle focused client on tag #" .. i, group = "tag"}
    )
  )
end

clientbuttons = gears.table.join(
    awful.button({ }, 1, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
    end),
    awful.button({ modkey }, 1, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
        awful.mouse.client.move(c)
    end),
    awful.button({ modkey }, 3, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
        awful.mouse.client.resize(c)
    end)
)

-- Set keys
root.keys(global_keys)
````

## Rules

````lua
-- Rules to apply to new clients (through the "manage" signal).
awful.rules.rules = {
    -- All clients will match this rule.
    { rule = { },
      properties = { border_width = beautiful.border_width,
                     border_color = beautiful.border_normal,
                     focus = awful.client.focus.filter,
                     raise = true,
                     keys = clientkeys,
                     buttons = clientbuttons,
                     screen = awful.screen.preferred,
                     placement = awful.placement.no_overlap+awful.placement.no_offscreen
     }
    },

    -- Floating clients.
    { rule_any = {
        instance = {
          "DTA",  -- Firefox addon DownThemAll.
          "copyq",  -- Includes session name in class.
          "pinentry",
        },
        class = {
          "Arandr",
          "Blueman-manager",
          "Gpick",
          "Kruler",
          "MessageWin",  -- kalarm.
          "Sxiv",
          "Tor Browser", -- Needs a fixed window size to avoid fingerprinting by screen size.
          "Wpa_gui",
          "veromix",
          "xtightvncviewer"},

        -- Note that the name property shown in xprop might be set slightly after creation of the client
        -- and the name shown there might not match defined rules here.
        name = {
          "Event Tester",  -- xev.
        },
        role = {
          "AlarmWindow",  -- Thunderbird's calendar.
          "ConfigManager",  -- Thunderbird's about:config.
          "pop-up",       -- e.g. Google Chrome's (detached) Developer Tools.
        }
      }, properties = { floating = true }},

    -- Add titlebars to normal clients and dialogs
    { rule_any = {type = { "normal", "dialog" }
      }, properties = { titlebars_enabled = true }
    },

    -- Set Firefox to always map on the tag named "2" on screen 1.
    -- { rule = { class = "Firefox" },
    --   properties = { screen = 1, tag = "2" } },
}
````

## Signals

````lua
-- Signal function to execute when a new client appears.
client.connect_signal("manage", function (c)
    -- Set the windows at the slave,
    -- i.e. put it at the end of others instead of setting it master.
    -- if not awesome.startup then awful.client.setslave(c) end

    if awesome.startup
      and not c.size_hints.user_position
      and not c.size_hints.program_position then
        -- Prevent clients from being unreachable after screen count changes.
        awful.placement.no_offscreen(c)
    end
end)

-- Add a titlebar if titlebars_enabled is set to true in the rules.
client.connect_signal("request::titlebars", function(c)
    -- buttons for the titlebar
    local buttons = gears.table.join(
        awful.button({ }, 1, function()
            c:emit_signal("request::activate", "titlebar", {raise = true})
            awful.mouse.client.move(c)
        end),
        awful.button({ }, 3, function()
            c:emit_signal("request::activate", "titlebar", {raise = true})
            awful.mouse.client.resize(c)
        end)
    )

    awful.titlebar(c) : setup {
        { -- Left
            awful.titlebar.widget.iconwidget(c),
            buttons = buttons,
            layout  = wibox.layout.fixed.horizontal
        },
        { -- Middle
            { -- Title
                align  = "center",
                widget = awful.titlebar.widget.titlewidget(c)
            },
            buttons = buttons,
            layout  = wibox.layout.flex.horizontal
        },
        { -- Right
            awful.titlebar.widget.floatingbutton (c),
            awful.titlebar.widget.maximizedbutton(c),
            awful.titlebar.widget.stickybutton   (c),
            awful.titlebar.widget.ontopbutton    (c),
            awful.titlebar.widget.closebutton    (c),
            layout = wibox.layout.fixed.horizontal()
        },
        layout = wibox.layout.align.horizontal
    }
end)

-- Enable sloppy focus, so that focus follows mouse.
client.connect_signal("mouse::enter", function(c)
    c:emit_signal("request::activate", "mouse_enter", {raise = false})
end)

client.connect_signal("focus", function(c) c.border_color = beautiful.border_focus end)
client.connect_signal("unfocus", function(c) c.border_color = beautiful.border_normal end)
````

[lain]: https://github.com/lcpz/lain
