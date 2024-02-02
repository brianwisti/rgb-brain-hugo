---
title: My micro editor config
tags:
- config
created: 2024-01-15T17:29:21-08:00
updated: 2024-02-01T20:25:49-08:00
---

[micro](../../card/micro.md) makes it easy to set config from inside the editor. That means this file may be out of sync with my current config.

Keeping that warning in mind, I won't get clever with 1:1 file matches like in some other configs.

## `settings.json`

````json
//- file:micro/settings.json
{
    "colorcolumn": 80,
    "colorscheme": "dukedark-tc",
    "diffgutter": true,
    "ft:dart": {
        "tabsize": 2
    },
    "ft:go": {
        "tabstospaces": false
    },
    "rmtrailingws": true,
    "tabstospaces": true
}
````

## `bindings.json`

````json
//- file:micro/bindings.json
{
    "Alt-/": "lua:comment.comment",
    "CtrlUnderscore": "lua:comment.comment"
}
````
