---
aliases:
- /note/2021/02/tweaking-my-tools/
category: note
date: 2021-02-16 14:40:03-08:00
slug: tweaking-my-tools
syndication:
  dev-to: https://dev.to/brianwisti/note-tweaking-my-tools-3f6f
  mastodon: https://hackers.town/@randomgeek/105743422712512318
  twitter: https://twitter.com/brianwisti/status/1361813716367474688
tags:
- ruby
- site
title: Tweaking my tools
created: 2024-01-15T15:26:20-08:00
updated: 2024-01-26T10:22:18-08:00
---

Playing a little more with [TTY Toolkit](../../../card/TTY%20Toolkit.md) for the site workflow. I wanted to say I'm tightening focus, but with a `require` list like this for one tool?

````ruby
require 'pastel'
require 'ruby-slugify'
require 'tty-editor'
require 'tty-exit'
require 'tty-logger'
require 'tty-option'
require 'tty-prompt'
require 'tty-screen'
````

"Tightening focus" would be a lie.

Anyways, it seems to function correctly. Huzzah! Now back to work.
