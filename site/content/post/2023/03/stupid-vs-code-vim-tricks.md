---
category: note
date: 2023-03-20
slug: stupid-vs-code-vim-tricks
syndication:
  linkedin: https://www.linkedin.com/posts/brianwisti_stupid-vs-code-vim-tricks-activity-7043773885921599488-qAYr
  mastodon: https://hackers.town/@randomgeek/110058842352483483
tags:
- vs-code
- config
title: Stupid VS Code Vim Tricks
created: 2024-01-15T15:26:10-08:00
updated: 2024-01-26T10:18:33-08:00
---

Still trying my experiment with using [Dendron](https://dendron.so) in [Visual Studio Code](https://code.visualstudio.com) as part of some sort of public second brain. Honestly I don't know how long that'll last, so I figure better share the fun stuff I learn here too.

Anyways this afternoon I installed the [Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) extension and learned just enough about custom key bindings to add a few.

````json{title="settings.json"}
{
  "vim.leader": "<space>",
  "vim.normalModeKeyBindings": [
    {
      "before": ["<leader>", "t", "l"],
      "commands": ["workbench.action.toggleSidebarVisibility"]
    },
    {
      "before": ["<leader>", "t", "r"],
      "commands": ["workbench.action.toggleAuxiliaryBar"]
    },
    {
      "before": ["<leader>", "t", "t"],
      "commands": ["workbench.action.toggleLightDarkThemes"]
    }
  ]
}
````

* `vim.leader` is handy as a prefix for extended custom bindings in Vim; I prefer the spacebar as my leader
* `<leader> t l` toggles my left sidebar
* `<leader> t r` toggles my right sidebar
* `<leader> t t` toggles between light and dark theme

These bindings look and work very similar to some of [Logseq](../../../card/Logseq.md)'s default bindings. That's no accident. I like those bindings.
