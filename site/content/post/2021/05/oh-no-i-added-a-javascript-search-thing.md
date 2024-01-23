---
aliases:
- /note/2021/05/oh-no-i-added-a-javascript-search-thing/
category: note
date: 2021-05-14 00:00:00-07:00
slug: oh-no-i-added-a-javascript-search-thing
syndication:
  mastodon: https://hackers.town/@randomgeek/106236540435473063
  twitter: https://twitter.com/brianwisti/status/1393373142807158787
tags:
- site
- javascript
- hyperscript
title: oh no i added a javascript search thing
---

And a touch of [\_hyperscript](https://hyperscript.org/).
Started from [this post](https://makewithhugo.com/add-search-to-a-hugo-site/) and leaned on the \_hyperscript to tie some bits together.

````html
<button _="on click
           get value of #searchQuery
           call executeSearch(it, false)">Search</button>

````

And yeah I'm back on [card/Hugo](../../../card/Hugo.md). Spent so much time in the last couple weeks touching up the static repo and ignoring the [card/Statamic](../../../card/Statamic.md) live site. Decided not to fight it. Anyways, now that I started clearly the logical next step will be [card/Gatsby](../../../card/Gatsby.md). For flexible values of "logical."
