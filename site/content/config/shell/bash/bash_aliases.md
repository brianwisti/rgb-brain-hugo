---
title: My Bash aliases
tags:
- config
---

Some of these are specific to specific machines.
If I cared more about my GNU Bash setup, I would tidy a bit.

````bash
alias realias='$EDITOR ~/.aliases; source ~/.aliases'

alias bbd='brew bundle dump --force --describe --global'
alias be='bundle exec'
alias blf='beet ls -f "$BF" album+ track+'
alias dnuke='docker kill $(docker ps -q);docker system prune --all --volumes -f'
alias e='emacs -nw'
alias kexp='mplayer http://live-aacplus-64.kexp.org/kexp64.aac'
alias ll='lsd -lF'
alias l='lsd -lahF'
alias ls='lsd'
alias pr='poetry run'
alias pri='poetry run invoke'
alias rire='ripit && beet import ~/mp3 && rmdir ~/mp3 && eject'
alias tsite='task project:Site'
alias tt='task +ticket'
alias ttw='task +ticket +Work +prl'
alias tw='task +Work +prl'
alias unflicker='xrandr --output DisplayPort-0 --mode 2560x1440 --rate 59.95'
alias ymd='date +"%Y%m%d"'
````
