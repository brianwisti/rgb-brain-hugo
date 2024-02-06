---
aliases:
- /config/alacritty.yml/
created: 2024-01-15 17:29:21-08:00
tags:
- config
title: My Alacritty Config
updated: 2024-02-05 16:22:12-08:00
---

Setting to my preferred font and SpaceDuck colors.

````yaml
//- file:alacritty/alacritty.yml
font:
  normal:
    family: FantasqueSansMono Nerd Font
  size: 14
# Space Duck
colors:
  # Default colors
  primary:
    background: '#0f111b'
    foreground: '#ecf0c1'
  # Normal colors
  normal:
    black:   '#000000'
    red:     '#e33400'
    green:   '#5ccc96'
    yellow:  '#b3a1e6'
    blue:    '#00a3cc'
    magenta: '#f2ce00'
    cyan:    '#7a5ccc'
    white:   '#686f9a'

  # Bright colors
  bright:
    black:   '#686f9a'
    red:     '#e33400'
    green:   '#5ccc96'
    yellow:  '#b3a1e6'
    blue:    '#00a3cc'
    magenta: '#f2ce00'
    cyan:    '#7a5ccc'
    white:   '#f0f1ce'
````