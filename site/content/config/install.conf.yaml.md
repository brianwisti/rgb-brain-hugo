---
title: My Dotbot config
tags:
- config
created: 2024-01-15T17:29:23-08:00
updated: 2024-02-01T21:55:10-08:00
---

After *Yarner* extracts code and Markdown from my config sources, *Dotbot* creates symlinks from generated code files to their expected locations in my home folder.

I adjust my defaults to allow creation of parent directories when they do not already exist.

````yaml
- defaults:
    link:
        create: true
````

Then I define my links!

````yaml
- link:
    ~/.config/nvim/init.lua: code/editor/nvim/init.lua
    ~/.tmux.conf: code/tmux.conf
    ~/.config/starship.toml: code/starship.toml
    ~/.config/systemd/user/autostart.target: code/systemd/user/autostart.target
    ~/.config/wezterm: code/wezterm
    ~/.config/nushell/config.nu: code/shell/nushell/config.nu
    ~/.config/nushell/env.nu: code/shell/nushell/env.nu
    ~/.config/nushell/login.nu: code/shell/nushell/login.nu
    ~/.config/nushell/lib: code/nushell/lib
    ~/.config/awesome/rc.lua: code/linux/awesome/rc.lua
    ~/.config/awesome/main: code/linux/awesome/main
    ~/.config/awesome/autorun.sh: code/linux/awesome/autorun.sh
    ~/.config/qtile/config.py: code/linux/qtile/config.py
    ~/.config/qtile/autostart.sh: code/linux/qtile/autostart.sh
    ~/.config/qtile/modules: code/linux/qtile/modules
    ~/.config/dunst/dunstrc: code/linux/dunst/dunstrc
    ~/.bash_profile: code/shell/bash/bash_profile
    ~/.bashrc: code/shell/bash/bashrc
    ~/.bash_aliases: code/shell/bash/bash_aliases
````
