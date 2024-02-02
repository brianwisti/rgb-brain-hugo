---
aliases:
- /2017/10/31/wellington-for-sass/
category: post
date: 2017-10-31 00:00:00-07:00
slug: wellington-for-sass
syndication:
  twitter: https://twitter.com/brianwisti/status/925593674230112256
tags:
- site
- css
- tools
title: Wellington for Sass
created: 2024-01-15T15:26:47-08:00
updated: 2024-02-01T21:17:48-08:00
---

I found [Wellington](https://getwt.io/), a [Sass](http://sass-lang.com/) compiler written in [Go](../../../card/Go.md).

I installed Wellington with [Homebrew](https://brew.sh/) - actually Linuxbrew but that’s a post for another day maybe, once I’m sure this Linuxbrew experiment worked for me.

````
$ brew install wellington
````

This is not the night to redesign the whole site, though. Make sure everything works.

````
$ wt compile assets/scss/main.scss -b static/css
2017/10/31 21:09:54 Compilation took: 28.333622ms
````

Seems to produce the same style output. I had no complaint about the speed of Ruby’s Sass compiler, but Wellington is certainly quicker.

I guess now I can start thinking about redesigning the site layout.
