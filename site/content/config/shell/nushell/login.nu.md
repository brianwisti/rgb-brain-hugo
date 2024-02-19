---
title: My Nushell login settings
tags:
- config
- nushell
created: 2024-01-15T17:29:21-08:00
updated: 2024-02-09T21:17:44-08:00
---

For my occasional experiments using Nu as my login shell.
Evaluated *after* `env.nu` and `config.nu`.

````nushell
let-env BAT_THEME = 'Solarized (dark)'
let-env BF = '$albumartist | $album | $track/$tracktotal | $title'
let-env CLICOLOR = '1'
let-env EDITOR = 'nvim'
let-env LANG = 'en_US.UTF-8'
let-env NNN_FALLBACK_OPENER = 'xdg-open'
let-env PAGER = 'less -FRX'
let-env PLENV_HOME = '/home/random/.plenv'
let-env PYENV_ROOT = '/home/random/.pyenv'
let-env PYENV_SHELL = 'nu'
let-env PYENV_VIRTUALENV_INIT = '1'
let-env RAKUBREW_HOME = '~/.rakubrew'
let-env STARSHIP_SHELL = 'nu'
let-env TERM = 'xterm-256color'
````
