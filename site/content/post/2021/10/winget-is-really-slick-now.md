---
aliases:
- /note/2021/10/winget-is-pretty-slick-now/
category: note
date: 2021-10-16 00:00:00-07:00
slug: winget-is-pretty-slick-now
syndication:
  mastodon: https://hackers.town/@randomgeek/107112953002673686
  twitter: https://twitter.com/brianwisti/status/1449463811489116163
tags:
- windows
- package-manager
- respect-the-command-line
title: winget is pretty slick now
created: 2024-01-15T15:26:25-08:00
updated: 2024-02-02T10:02:59-08:00
---

Just updated PowerShell via [winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/), Microsoft's command line package manager. And Firefox. And Volta. And HeidiSQL. And Alacritty. And Go. And some other stuff.

Trying to recover a post about [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/index.html) that I accidentally deleted, so I won't sidetrack myself with a detailed follow-up on the last time I really [looked at winget](../../2020/06/winget.md).

Instead, here's the [TIL](../../../card/TIL.md):

`winget upgrade`
: shows what's out of date

`winget upgrade --id=<package.id>`
: upgrades a package

`winget upgrade --all`
: upgrades everything.

No "Run As Administrator" needed, though you need to click the <abbr title="User Access Control">UAC</abbr> dialog. Another caveat: it's coming from the application's own download servers, not some Azure-backed central repository. Sometimes the fetching may take a minute.
