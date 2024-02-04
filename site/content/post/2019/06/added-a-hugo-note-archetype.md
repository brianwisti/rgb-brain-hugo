---
aliases:
- /note/2019/0003/
- /note/2019/174/added-a-hugo-note-archetype/
- /note/2019/06/added-a-hugo-note-archetype/
category: note
created: 2024-01-15 15:26:37-08:00
date: 2019-06-23 19:55:11-07:00
slug: added-a-hugo-note-archetype
syndication:
  mastodon: https://hackers.town/@randomgeek/102324468805367109
  twitter: https://twitter.com/brianwisti/status/1143000378511941632
tags:
- notes
- hugo
- posted-from-my-phone
- sort-of
- mobile-hotspot
- my-data-usage-is-gonna-hurt
title: Added a Hugo note archetype
updated: 2024-02-01 19:52:59-08:00
---

Moved into a new apartment. Waiting for Internet on Tuesday. It's Sunday.

Continuing to work slow but sure on my notes experiment. Today: a [Hugo](../../../card/Hugo.md) [archetype](https://gohugo.io/content-management/archetypes/) that includes a full *ISO 8601* timestamp, via [`dateFormat`](https://gohugo.io/functions/dateformat).

````
---
date: "{{ dateFormat "2006-01-02T15:04:05-07:00" .Date }}"
hashtags:
-
---

SAY SOMETHING
````

And yeah, hashtags are related to but distinct from tags. Basically, I have a particular protocol for tags and posts. I can be more informal with notes and hashtags. The silly name reminds me they're supposed to be fun.

Working out the occasional overlap is a pending item in [Taskwarrior](../../../card/Taskwarrior.md).