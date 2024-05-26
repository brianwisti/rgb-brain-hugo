---
aliases:
- /2019/07/30/try-xkcdpass/
category: post
created: 2024-01-15 15:26:34-08:00
date: 2019-07-30 07:36:11-07:00
description: In which I suggest a password generator
slug: try-xkcdpass
syndication:
  mastodon: https://hackers.town/@randomgeek/102531070232066570
  twitter: https://twitter.com/brianwisti/status/1156223226063794182
tags:
- linux
- security
- tools
title: Try xkcdpass
updated: 2024-05-01 22:41:29-07:00
---

![attachments/img/2019/cover-2019-07-30.png](../../../attachments/img/2019/cover-2019-07-30.png)
[XKCD 936](https://xkcd.com/936/) *([CC BY-NC 2.5](https://xkcd.com/license.html))*

 > 
 > \[!Summary\]
 > Use [xkcdpass](https://pypi.org/project/xkcdpass/) to generate more secure passwords, like “correcthorsebatterystaple”.

This started as a Note but I passed my 15 minute rule — if I spend more than 15 minutes on it, it should be a post — so here we are.

It won’t satisfy your bank’s silly password requirements, but — as XKCD told us — using a random collection of words for your password provides more security than trying to [Leet-speak](https://simple.wikipedia.org/wiki/Leet) some word with numbers and symbols.

You could pick a handful of words by flipping through the dictionary, but why not let the computer do it for you? That’s where xkcdpass comes in.

It’s probably available in your package repository.

````console
$ pacman -Ss xkcdpass
````

It’s just #python , so you can use `pip` if you’re on macOS or Windows
or some other platform that doesn’t have `xkcdpass` handy.

````sh
pip install xkcdpass
````

Regardless of how you install it, run it and grab the output — but let your password manager remember it for you.

````console
$ xkcdpass
tiara embezzle stack doorway scrambled imitate
````