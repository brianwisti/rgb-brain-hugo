---
aliases:
- /tools/2015/07/23_pandoc.html
- /post/2015/pandoc/
- /2015/07/23/pandoc/
category: post
created: 2024-01-15 15:25:25-08:00
date: 2015-07-23 00:00:00-07:00
slug: pandoc
tags:
- pandoc
- tools
title: Pandoc
updated: 2024-05-02 07:33:06-07:00
---

I could use [Pandoc](http://pandoc.org/) to build HTML from my site
sources.

I could use it to convert them to different sources.

I’m not saying I *would*. But I *could*.

Okay I might.

````
$ pandoc --to org _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.org
$ pandoc --to asciidoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.adoc
$ pandoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.html
````

![Pandoc output in Emacs](attachments/img/2015/emacs-pandoc.png)

Honestly at this point I’d say it’s pretty likely.