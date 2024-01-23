---
title: My dunst dunstrc
tags:
- config
---

Just a dump of the inline documentation for the EndeavourOS dunst user defaults.

## Global Settings

````conf
[global]
````

### Display

{{% quote %}}
Which monitor notifications should be displayed on.
{{% /quote %}}

I only have one, so it's an easy choice.

````conf
monitor = 0
````

{{% quote %}}
Display notification on focused monitor.  Possible modes are:

`mouse`
: follow mouse pointer

`keyboard`
: follow window with keyboard focus

`none`
: don't follow anything

`keyboard` needs a window manager that exports the `_NET_ACTIVE_WINDOW` property.
This should be the case for almost all modern window managers.

If this option is set to mouse or keyboard, the monitor option will be ignored.
{{% /quote %}}

````conf
follow = mouse
````

{{% quote %}}
The geometry of the window: `[{width}]x{height}[+/-{x}+/-{y}]`

The geometry of the message window.

The height is measured in number of notifications everything else in pixels.
If the width is omitted but the height is given (`"-geometry x2"`),
the message window expands over the whole screen (dmenu-like).
If width is 0, the window expands to the longest message displayed.
A positive x is measured from the left, a negative from the right side of the screen.
Y is measured from the top and down respectively.

The width can be negative.
In this case the actual width is the screen width minus the width defined in within the geometry option.
{{% /quote %}}

````conf
geometry = "0x0-30+20"
````

{{% quote %}}
Show how many messages are currently hidden (because of geometry).
{{% /quote %}}

````conf
indicate_hidden = yes
````

{{% quote %}}
Shrink window if it's smaller than the width.
Will be ignored if width is 0.
{{% /quote %}}

````conf
shrink = no
````

{{% quote %}}
The transparency of the window.  Range: \[0; 100\].

This option will only work if a compositing window manager is present
(e.g. xcompmgr, compiz, etc.).
{{% /quote %}}

````conf
transparency = 0
````

{{% quote %}}
The height of the entire notification.
If the height is smaller than the font height and padding combined,
it will be raised to the font height and padding.
{{% /quote %}}

````conf
notification_height = 0
````

{{% quote %}}
Draw a line of `separator_height` pixel height between two notifications.

Set to `0` to disable.
{{% /quote %}}

````conf
    separator_height = 2
````

{{% quote %}}
Padding between text and separator.
{{% /quote %}}

````conf
padding = 8
````

{{% quote %}}
Horizontal padding.
{{% /quote %}}

````conf
horizontal_padding = 8
````

{{% quote %}}
Defines width in pixels of frame around the notification window.

Set to 0 to disable.
{{% /quote %}}

````conf
frame_width = 3
````

{{% quote %}}
Defines color of the frame around the notification window.
{{% /quote %}}

````conf
frame_color = "#aaaaaa"
````

{{% quote %}}
Define a color for the separator.
possible values are:

`auto`
: dunst tries to find a color fitting to the background

`foreground`
: use the same color as the foreground

`frame`
: use the same color as the frame

Anything else will be interpreted as a X color.
{{% /quote %}}

````conf
separator_color = auto
````

{{% quote %}}
Sort messages by urgency.
{{% /quote %}}

````conf
sort = yes
````

{{% quote %}}
Don't remove messages,
if the user is idle (no mouse or keyboard input) for longer than idle_threshold seconds.

Set to 0 to disable.

A client can set the 'transient' hint to bypass this.
See the rules section for how to disable this if necessary
{{% /quote %}}

````conf
idle_threshold = 120
````

### Text

````conf
font = JetBrains Mono Medium 10
````

{{% quote %}}
The spacing between lines.
If the height is smaller than the font height, it will get raised to the font height.
{{% /quote %}}

````conf
line_height = 0
````

{{% quote %}}
Possible values are:

full
: Allow a small subset of html markup in notifications
For a complete reference see <http://developer.gnome.org/pango/stable/PangoMarkupFormat.html>.

strip
: This setting is provided for compatibility with some broken
clients that send markup even though it's not enabled on the
server. Dunst will try to strip the markup but the parsing is
simplistic so using this option outside of matching rules for
specific applications *IS GREATLY DISCOURAGED*.

no
: Disable markup parsing, incoming notifications will be treated as
plain text. Dunst will not advertise that it has the body-markup
capability if this is set as a global setting.

It's important to note that markup inside the format option will be parsed
regardless of what this is set to.
{{% /quote %}}

````conf
markup = full
````

{{% quote %}}
The format of the message.
Possible variables are:

|Variable|Represents|
|--------|----------|
|`%a`|appname|
|`%s`|summary|
|`%b`|body|
|`%i`|iconname (including its path)|
|`%I`|iconname (without its path)|
|`%p`|progress value if set (\[  0%\] to \[100%\]) or nothing|
|`%n`|progress value if set without any extra characters|
|`%%`|Literal `%`|

Markup is allowed
{{% /quote %}}

````conf
format = "<b>%s</b>\n%b"
````

{{% quote %}}
Alignment of message text.

Possible values are "left", "center" and "right".
{{% /quote %}}

````conf
alignment = center
````

{{% quote %}}
Show age of message if message is older than `show_age_threshold` seconds.

Set to `-1` to disable.
{{% /quote %}}

````conf
show_age_threshold = 60
````

{{% quote %}}
Split notifications into multiple lines if they don't fit into geometry.
{{% /quote %}}

````conf
word_wrap = yes
````

{{% quote %}}
When word_wrap is set to no, specify where to make an ellipsis in long lines.

Possible values are "start", "middle" and "end".
{{% /quote %}}

````conf
ellipsize = middle
````

{{% quote %}}
Ignore newlines `\n` in notifications.
{{% /quote %}}

````conf
ignore_newline = no
````

{{% quote %}}
Stack together notifications with the same content
{{% /quote %}}

````conf
stack_duplicates = true
````

{{% quote %}}
Hide the count of stacked notifications with the same content
{{% /quote %}}

````conf
hide_duplicate_count = false
````

{{% quote %}}
Display indicators for URLs (U) and actions (A).
{{% /quote %}}

````conf
show_indicators = yes
````

### Icons

{{% quote %}}
Align icons left/right/off
{{% /quote %}}

````conf
icon_position = left
````

{{% quote %}}
Scale larger icons down to this size, set to 0 to disable
{{% /quote %}}

````conf
max_icon_size = 32
````

{{% quote %}}
icon_path = /usr/share/icons/gnome/16x16/status/:/usr/share/icons/gnome/16x16/devices/

{{% /quote %}}

````conf
# Paths to default icons.
````

### History

{{% quote %}}
Should a notification popped up from history be sticky or timeout as if it would normally do.
{{% /quote %}}

````conf
sticky_history = yes
````

{{% quote %}}
Maximum amount of notifications kept in history
{{% /quote %}}

````conf
history_length = 20
````

### Misc / Advanced

{{% quote %}}
dmenu path.
{{% /quote %}}

````conf
dmenu = /usr/bin/dmenu -p dunst:
````

{{% quote %}}
Browser for opening urls in context menu.
{{% /quote %}}

Defaults to Brave.
I use Firefox.

````conf
browser = /usr/bin/firefox
````

{{% quote %}}
Always run rule-defined scripts, even if the notification is suppressed
{{% /quote %}}

````conf
always_run_script = true
````

{{% quote %}}
Define the title of the windows spawned by dunst
{{% /quote %}}

````conf
title = Dunst
````

{{% quote %}}
Define the class of the windows spawned by dunst
{{% /quote %}}

````conf
class = Dunst
````

{{% quote %}}
Print a notification on startup.

This is mainly for error detection, since dbus (re-)starts dunst automatically after a crash.
{{% /quote %}}

````conf
startup_notification = false
````

{{% quote %}}
Manage dunst's desire for talking

Can be one of the following values:

crit
: Critical features. Dunst aborts

warn
: Only non-fatal warnings

mesg
: Important Messages

info
: all unimportant stuff

ebug
: all less than unimportant stuff
{{% /quote %}}

````conf
verbosity = mesg
````

{{% quote %}}
Define the corner radius of the notification window in pixel size.
If the radius is 0, you have no rounded corners.

The radius will be automatically lowered if it exceeds half of the notification height to avoid clipping text and/or icons.
{{% /quote %}}

````conf
corner_radius = 5
````

### Legacy

{{% quote %}}
Use the Xinerama extension instead of RandR for multi-monitor support.
This setting is provided for compatibility with older nVidia drivers that
do not support RandR and using it on systems that support RandR is highly
discouraged.

By enabling this setting dunst will not be able to detect when a monitor
is connected or disconnected which might break follow mode if the screen
layout changes.
{{% /quote %}}

````conf
force_xinerama = false
````

### Mouse

{{% quote %}}
Defines action of mouse event

Possible values are:

`none`
: Don't do anything.

`do_action`
: If the notification has exactly one action, or one is marked as default,
invoke it. If there are multiple and no default, open the context menu.

`close_current`
: Close current notification.

`close_all`
: Close all notifications.
{{% /quote %}}

````conf
mouse_left_click = do_action
mouse_middle_click = close_all
mouse_right_click = close_current
````

## Experimental

{{% quote %}}
Experimental features that may or may not work correctly.
Do not expect them to have a consistent behaviour across releases.
{{% /quote %}}

````conf
[experimental]
````

{{% quote %}}
Calculate the dpi to use on a per-monitor basis.

If this setting is enabled the Xft.dpi value will be ignored and instead
dunst will attempt to calculate an appropriate dpi value for each monitor
using the resolution and physical size. This might be useful in setups
where there are multiple screens with very different dpi values.
{{% /quote %}}

````conf
per_monitor_dpi = false
````

## Shortcuts

{{% quote %}}
Shortcuts are specified as `[modifier+][modifier+]...key`

Available modifiers are "ctrl", "mod1" (the alt-key), "mod2",
"mod3" and "mod4" (windows-key).

Xev might be helpful to find names for keys.
{{% /quote %}}

````conf
[shortcuts]
````

{{% quote %}}
Close notification.
{{% /quote %}}

````conf
close = ctrl+space
````

{{% quote %}}
Close all notifications.
{{% /quote %}}

````conf
close_all = ctrl+shift+space
````

{{% quote %}}
Redisplay last message(s).

On the US keyboard layout "grave" is normally above TAB and left of "1".
Make sure this key actually exists on your keyboard layout,
e.g. check output of `xmodmap -pke`
{{% /quote %}}

````conf
history = ctrl+grave
````

{{% quote %}}
Context menu.
{{% /quote %}}

````conf
context = ctrl+shift+period
````

## Low Urgency Notifications

{{% quote %}}
IMPORTANT: colors have to be defined in quotation marks.
Otherwise the "#" and following would be interpreted as a comment.
{{% /quote %}}

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
