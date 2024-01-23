---
title: My awesome config
aliases:
- /config/awesome/
tags:
- config
---

It's not like I know what I'm doing or anything. But at least I'm having fun.

## Requirements

* [awesomewm](https://awesomewm.org) provides the window manager of course
* [Vicious](https://vicious.readthedocs.io/en/latest) adds a widget framework
* [dex](https://github.com/jceb/dex) to generate and execute DesktopEntry files
* [Awesome-Freedesktop](https://github.com/lcpz/awesome-freedesktop) for an XDG-friendly app menu
* [Lain](https://github.com/lcpz/lain) provides layouts, widgets, and utilities
* [Xephyr](https://wiki.archlinux.org/title/Xephyr) to quality check my config

When I'm sitting in front of an Arch-based system:

````sh
//- Install awesomewm and related packages
yay -S awesome vicious dex lain-git awesome-freedesktop-git xorg-server-xephyr
````

## Testing

Until I figure out a proper path to automated testing, I launch awesome in a
Xephyr nested X server.

````bash
//- Preview awesome config
Xephyr :5 & sleep 1 ; DISPLAY=:5 awesome -c code/linux/awesome/rc.lua
````

It's not perfect, but at least it will tell me whether my config contains any
immediately obvious errors.
