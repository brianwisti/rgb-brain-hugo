---
aliases:
- /note/2021/09/finally-have-all-my-content-in-one-format/
category: note
date: 2021-09-16 00:00:00-07:00
slug: finally-have-all-my-content-in-one-format
syndication:
  mastodon: https://hackers.town/@randomgeek/106945161649678603
  twitter: https://twitter.com/brianwisti/status/1438724710884335618
tags:
- site
- asciidoctor
title: finally have all my content in one format
created: 2024-01-15T15:26:11-08:00
updated: 2024-02-01T20:12:23-08:00
---


````
content/**/*{.md,.md.txt,.rst,.rst.txt,.adoc,.adoc.txt,.org}
┌─────────┬─────┐
│Format   │Count│
├─────────┼─────┤
│.md      │48   │
│.adoc.txt│574  │
│.md.txt  │579  │
│.rst.txt │32   │
└─────────┴─────┘
````

Okay yes I also have it in several other formats. Came up with an approach where I can keep all my formats in the [base blog](../08/pared-down-to-the-base-blog.md) and build whatever I prefer.

My *point* is that all the content that counts is available in [Asciidoctor](../../../card/Asciidoctor.md) format. Better choice for me than Markdown since Asciidoctor already has built-in understanding of notes and asides. Better choice for me than [reStructuredText](../../../card/reStructuredText.md) because it's easier to find Asciidoctor processors for assorted static site generators.
