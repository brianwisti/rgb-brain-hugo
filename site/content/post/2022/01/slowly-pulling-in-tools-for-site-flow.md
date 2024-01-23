---
aliases:
- /note/2022/01/slowly-pulling-in-tools-for-site-flow/
category: note
date: 2022-01-16 20:30:00-08:00
slug: slowly-pulling-in-tools-for-site-flow
syndication:
  mastodon: https://hackers.town/@randomgeek/107634186872393474
  twitter: https://twitter.com/brianwisti/status/1482822267427905537
tags:
- node-js
- indieweb
- posse
- site
title: Slowly pulling in tools for site flow
---

Made a [toot](https://hackers.town/@randomgeek/107630284879354154) with [Masto](https://www.npmjs.com/package/masto). Kinda need that for content syndication.

![Here's my toot](attachments/img/2022/toot.png "Here's my toot")

The [Mastodon Twitter Crossposter](https://crossposter.masto.donte.com.br/) works great, but waiting for the announcement toot to show up as a tweet was a tedious manual step that I hope to discard. So I figured out how to make a tweet with [twitter-api-v2](https://www.npmjs.com/package/twitter-api-v2).

Those are the pieces I need to get [POSSE](https://indieweb.org/POSSE) syndication working in this [card/Eleventy](../../../card/Eleventy.md) iteration of the site.

Now I just need to staple those pieces together, grab a sharpie, and label it "workflow."
