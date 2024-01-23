---
title: My micro editor config
tags:
- config
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
