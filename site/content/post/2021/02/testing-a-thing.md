---
aliases:
- /note/2021/02/testing-a-thing/
category: note
created: 2024-01-15 15:26:28-08:00
date: 2021-02-14 18:29:10-08:00
slug: testing-a-thing
syndication:
  dev-to: https://dev.to/brianwisti/note-testing-a-thing-ad3
  mastodon: https://hackers.town/@randomgeek/105732993013826473
  twitter: https://twitter.com/brianwisti/status/1361146116495060992
tags:
- asciidoctor
- hugo
- site
title: testing a thing
updated: 2024-02-02 10:04:14-08:00
---

Sometime [last year](../../2020/05/letting-ruby-build-asciidoctor-files-for-hugo.md) I had half of a great idea for better [Asciidoctor](../../../card/Asciidoctor.md) handling in [Hugo](../../../card/Hugo.md). I *might* have the other half now:

* keep my content in the content folder.
* Use `adoc.txt` for the extension so Hugo ignores it.
* Point my `build-adoc` script there instead of a neighboring `adoc` folder.
* profit?

Would work for [reStructuredText](../../../card/reStructuredText.md) too.

Need to get through a few post cycles to see how it works.