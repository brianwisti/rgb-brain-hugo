---
aliases:
- /note/2019/09/i-fixed-my-dot-pages/
category: note
date: 2019-09-19 01:43:31-07:00
slug: i-fixed-my-dot-pages
syndication:
  mastodon: https://hackers.town/@randomgeek/102818332962454350
tags:
- hugo
- oops
title: I FIXED MY .Pages
---

Too tired to make it make sense. My site broke under [card/Hugo](../../../card/Hugo.md) .58. No front page listing. I fixed it. Yay!

Instead of (for notes):

````
{{- range first 1 (where .Pages "Section" "note") -}}
````

I used

````
{{- range first 1 (where .Site.RegularPages "Section" "note") -}}
````

I also fixed the RSS feed, and updated the [feeds post](../../2017/09/full-content-hugo-feeds.md)  with those (very similar) details.
