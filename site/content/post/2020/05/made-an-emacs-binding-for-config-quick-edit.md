---
aliases:
- /note/2020/05/made-an-emacs-binding-for-config-quick-edit/
category: note
date: 2020-05-07 14:30:00-07:00
slug: made-an-emacs-binding-for-config-quick-edit
syndication:
  mastodon: https://hackers.town/@randomgeek/104129350946938060
  twitter: https://twitter.com/brianwisti/status/1258513226649620480
tags:
- emacs
- orgconfig
title: Made an Emacs Binding for Config Quick Edit
---

I hit `F5`, [Emacs](../../../card/Emacs.md) opens my `config.org` for editing. It might not be much but it feels good to scratch such a specific itch. Feeling pretty good about myself.

````elisp
(global-set-key (kbd "<f5>")
                (lambda ()
                  (interactive)
                  (find-file "~/.dotfiles/config.org")))
````
