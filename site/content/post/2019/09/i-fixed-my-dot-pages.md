---
aliases:
- /note/2019/09/i-fixed-my-dot-pages/
category: note
created: 2024-01-15 15:26:37-08:00
date: 2019-09-19 01:43:31-07:00
slug: i-fixed-my-dot-pages
syndication:
  mastodon: https://hackers.town/@randomgeek/102818332962454350
tags:
- hugo
- oops
title: I FIXED MY .Pages
updated: 2024-02-01 20:18:09-08:00
---

Too tired to make it make sense. My site broke under [Hugo](../../../card/Hugo.md) .58. No front page listing. I fixed it. Yay!

Instead of (for notes):

````
{{- range first 1 (where .Pages "Section" "note") -}}
````

I used

````
{{- range first 1 (where .Site.RegularPages "Section" "note") -}}
````

I also fixed the RSS feed, and updated the [feeds post](../../2017/09/full-content-hugo-feeds.md)  with those (very similar) details.