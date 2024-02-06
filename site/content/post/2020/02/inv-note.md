---
aliases:
- /note/2020/36/inv-note/
- /note/2020/02/inv-note/
category: note
created: 2024-01-15 15:26:30-08:00
date: 2020-02-05 07:54:39-08:00
slug: inv-note
syndication:
  mastodon: https://hackers.town/@randomgeek/103607162408116784
  twitter: https://twitter.com/brianwisti/status/1225095517694242818
tags:
- site
- pyinvoke
- drawing
- amaziograph
- fun
title: inv note
updated: 2024-01-26 11:03:24-08:00
---

![attachments/img/2020/cover-2020-02-05.jpg](../../../attachments/img/2020/cover-2020-02-05.jpg)
I drew this with [Amaziograph](https://amaziograph.com)

````sh
inv note --title='inv note'
````

Don’t mind me. I’m just trying an experiment with using [Invoke](https://docs.pyinvoke.org) for my site workflow instead of [Make](https://www.gnu.org/software/make/).

````
$ inv serve
SHOW_INFO=1 hugo server --buildDrafts --bind 0.0.0.0 --navigateToChanged
...
Press Ctrl+C to stop
````

But that’s boring on its own. Here. Have a drawing.

I’ll probably make a proper blog post about Invoke later. Meanwhile, checkout the docs on [Getting started](https://docs.pyinvoke.org/en/stable/getting-started.html).

````sh
inv publish
````