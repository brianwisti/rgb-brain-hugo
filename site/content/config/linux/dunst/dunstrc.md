---
title: My dunst dunstrc
tags:
- config
created: 2024-01-15T17:29:21-08:00
updated: 2024-02-01T16:01:08-08:00
---

Just a dump of the inline documentation for the EndeavourOS dunst user defaults.

## Global Settings

````conf
[global]
````

### Display

 > 
 > Which monitor notifications should be displayed on.

I only have one, so it's an easy choice.

````conf
monitor = 0
````

 > 
 > Display notification on focused monitor.  Possible modes are:
 > 
 > `mouse`
 > : follow mouse pointer
 > 
 > `keyboard`
 > : follow window with keyboard focus
 > 
 > `none`
 > : don't follow anything
 > 
 > `keyboard` needs a window manager that exports the `_NET_ACTIVE_WINDOW` property.
 > This should be the case for almost all modern window managers.
 > 
 > If this option is set to mouse or keyboard, the monitor option will be ignored.

````conf
follow = mouse
````

 > 
 > The geometry of the window: `[{width}]x{height}[+/-{x}+/-{y}]`
 > 
 > The geometry of the message window.
 > 
 > The height is measured in number of notifications everything else in pixels.
 > If the width is omitted but the height is given (`"-geometry x2"`),
 > the message window expands over the whole screen (dmenu-like).
 > If width is 0, the window expands to the longest message displayed.
 > A positive x is measured from the left, a negative from the right side of the screen.
 > Y is measured from the top and down respectively.
 > 
 > The width can be negative.
 > In this case the actual width is the screen width minus the width defined in within the geometry option.

````conf
geometry = "0x0-30+20"
````

 > 
 > Show how many messages are currently hidden (because of geometry).

````conf
indicate_hidden = yes
````

 > 
 > Shrink window if it's smaller than the width. Will be ignored if width is 0.

````conf
shrink = no
````

 > 
 > The transparency of the window.  Range: \[0; 100\].
 > 
 > This option will only work if a compositing window manager is present (e.g. xcompmgr, compiz, etc.).

````conf
transparency = 0
````

 > 
 > The height of the entire notification. If the height is smaller than the font height and padding combined, it will be raised to the font height and padding.

````conf
notification_height = 0
````

 > 
 > Draw a line of `separator_height` pixel height between two notifications.
 > 
 > Set to `0` to disable.

````conf
    separator_height = 2
````

 > 
 > Padding between text and separator.

````conf
padding = 8
````

 > 
 > Horizontal padding.

````conf
horizontal_padding = 8
````

 > 
 > Defines width in pixels of frame around the notification window.
 > 
 > Set to 0 to disable.

````conf
frame_width = 3
````

 > 
 > Defines color of the frame around the notification window.

````conf
frame_color = "#aaaaaa"
````

 > 
 > Define a color for the separator. possible values are:
 > 
 > `auto`
 > : dunst tries to find a color fitting to the background
 > 
 > `foreground`
 > : use the same color as the foreground
 > 
 > `frame`
 > : use the same color as the frame
 > 
 > Anything else will be interpreted as a X color.

````conf
separator_color = auto
````

 > 
 > Sort messages by urgency.

````conf
sort = yes
````

 > 
 > Don't remove messages, if the user is idle (no mouse or keyboard input) for longer than idle_threshold seconds.
 > 
 > Set to 0 to disable.
 > 
 > A client can set the 'transient' hint to bypass this. See the rules section for how to disable this if necessary

````conf
idle_threshold = 120
````

### Text

````conf
font = JetBrains Mono Medium 10
````

 > 
 > The spacing between lines. If the height is smaller than the font height, it will get raised to the font height.

````conf
line_height = 0
````

 > 
 > Possible values are:
 > 
 > full
 > : Allow a small subset of html markup in notifications. For a complete reference see <http://developer.gnome.org/pango/stable/PangoMarkupFormat.html>.
 > 
 > strip
 > : This setting is provided for compatibility with some broken clients that send markup even though it's not enabled on the server. Dunst will try to strip the markup but the parsing is simplistic so using this option outside of matching rules for specific applications *IS GREATLY DISCOURAGED*.
 > 
 > no
 > : Disable markup parsing, incoming notifications will be treated as plain text. Dunst will not advertise that it has the body-markup capability if this is set as a global setting.
 > 
 > It's important to note that markup inside the format option will be parsed regardless of what this is set to.

````conf
markup = full
````

 > 
 > The format of the message. Possible variables are:
 > 
 > |Variable|Represents|
 > |--------|----------|
 > |`%a`|appname|
 > |`%s`|summary|
 > |`%b`|body|
 > |`%i`|iconname (including its path)|
 > |`%I`|iconname (without its path)|
 > |`%p`|progress value if set (\[  0%\] to \[100%\]) or nothing|
 > |`%n`|progress value if set without any extra characters|
 > |`%%`|Literal `%`|
 > 
 > Markup is allowed

````conf
format = "<b>%s</b>\n%b"
````

 > 
 > Alignment of message text.
 > 
 > Possible values are "left", "center" and "right".

````conf
alignment = center
````

 > 
 > Show age of message if message is older than `show_age_threshold` seconds.
 > 
 > Set to `-1` to disable.

````conf
show_age_threshold = 60
````

 > 
 > Split notifications into multiple lines if they don't fit into geometry.

````conf
word_wrap = yes
````

 > 
 > When word_wrap is set to no, specify where to make an ellipsis in long lines.
 > 
 > Possible values are "start", "middle" and "end".

````conf
ellipsize = middle
````

 > 
 > Ignore newlines `\n` in notifications.

````conf
ignore_newline = no
````

 > 
 > Stack together notifications with the same content

````conf
stack_duplicates = true
````

 > 
 > Hide the count of stacked notifications with the same content

````conf
hide_duplicate_count = false
````

 > 
 > Display indicators for URLs (U) and actions (A).

````conf
show_indicators = yes
````

### Icons

 > 
 > Align icons left/right/off

````conf
icon_position = left
````

 > 
 > Scale larger icons down to this size, set to 0 to disable

````conf
max_icon_size = 32
````

 > 
 > icon_path = `/usr/share/icons/gnome/16x16/status/:/usr/share/icons/gnome/16x16/devices/`

````conf
# Paths to default icons.
````

### History

 > 
 > Should a notification popped up from history be sticky or timeout as if it would normally do.

````conf
sticky_history = yes
````

 > 
 > Maximum amount of notifications kept in history

````conf
history_length = 20
````

### Misc / Advanced

 > 
 > dmenu path.

````conf
dmenu = /usr/bin/dmenu -p dunst:
````

 > 
 > Browser for opening urls in context menu.

Defaults to Brave. I use Firefox.

````conf
browser = /usr/bin/firefox
````

 > 
 > Always run rule-defined scripts, even if the notification is suppressed

````conf
always_run_script = true
````

 > 
 > Define the title of the windows spawned by dunst

````conf
title = Dunst
````

 > 
 > Define the class of the windows spawned by dunst

````conf
class = Dunst
````

 > 
 > Print a notification on startup.
 > 
 > This is mainly for error detection, since dbus (re-)starts dunst automatically after a crash.

````conf
startup_notification = false
````

 > 
 > Manage dunst's desire for talking
 > 
 > Can be one of the following values:
 > 
 > crit
 > : Critical features. Dunst aborts
 > 
 > warn
 > : Only non-fatal warnings
 > 
 > mesg
 > : Important Messages
 > 
 > info
 > : all unimportant stuff
 > 
 > ebug
 > : all less than unimportant stuff

````conf
verbosity = mesg
````

 > 
 > Define the corner radius of the notification window in pixel size. If the radius is 0, you have no rounded corners.
 > 
 > The radius will be automatically lowered if it exceeds half of the notification height to avoid clipping text and/or icons.

````conf
corner_radius = 5
````

### Legacy

 > 
 > Use the Xinerama extension instead of RandR for multi-monitor support. This setting is provided for compatibility with older nVidia drivers that do not support RandR and using it on systems that support RandR is highly discouraged.
 > 
 > By enabling this setting dunst will not be able to detect when a monitor is connected or disconnected which might break follow mode if the screen layout changes.

````conf
force_xinerama = false
````

### Mouse

 > 
 > Defines action of mouse event
 > 
 > Possible values are:
 > 
 > `none`
 > : Don't do anything.
 > 
 > `do_action`
 > : If the notification has exactly one action, or one is marked as default, invoke it. If there are multiple and no default, open the context menu.
 > 
 > `close_current`
 > : Close current notification.
 > 
 > `close_all`
 > : Close all notifications.

````conf
mouse_left_click = do_action
mouse_middle_click = close_all
mouse_right_click = close_current
````

## Experimental

 > 
 > Experimental features that may or may not work correctly. Do not expect them to have a consistent behaviour across releases.

````conf
[experimental]
````

 > 
 > Calculate the dpi to use on a per-monitor basis.
 > 
 > If this setting is enabled the Xft.dpi value will be ignored and instead dunst will attempt to calculate an appropriate dpi value for each monitor using the resolution and physical size. This might be useful in setups where there are multiple screens with very different dpi values.

````conf
per_monitor_dpi = false
````

## Shortcuts

 > 
 > Shortcuts are specified as `[modifier+][modifier+]...key`
 > 
 > Available modifiers are "ctrl", "mod1" (the alt-key), "mod2", "mod3" and "mod4" (windows-key).
 > 
 > Xev might be helpful to find names for keys.

````conf
[shortcuts]
````

 > 
 > Close notification.

````conf
close = ctrl+space
````

 > 
 > Close all notifications.

````conf
close_all = ctrl+shift+space
````

 > 
 > Redisplay last message(s).
 > 
 > On the US keyboard layout "grave" is normally above TAB and left of "1". Make sure this key actually exists on your keyboard layout, e.g. check output of `xmodmap -pke`

````conf
history = ctrl+grave
````

 > 
 > Context menu.

````conf
context = ctrl+shift+period
````

## Low Urgency Notifications

 > 
 > IMPORTANT: colors have to be defined in quotation marks. Otherwise the "#" and following would be interpreted as a comment.

````conf
[urgency_low]
background = "#2b2b2b"
foreground = "#ffffff"
timeout = 5
````

## Normal Urgency Notifications

````conf
[urgency_normal]
background = "#2b2b2b"
foreground = "#ffffff"
timeout = 5
````

## Critical Urgency Notifications

````conf
[urgency_critical]
background = "#900000"
foreground = "#ffffff"
frame_color = "#ff0000"
timeout = 5
````

## Everything else

There's a lot.
See the EndeavourOS Qtile Community Edition [dunstrc](https://github.com/EndeavourOS-Community-Editions/qtile/blob/main/.config/dunst/dunstrc) for the whole
thing.
