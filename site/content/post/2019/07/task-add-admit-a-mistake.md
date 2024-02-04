---
aliases:
- /note/2019/184/task-add-admit-a-mistake/
- /note/2019/07/task-add-admit-a-mistake/
category: note
date: 2019-07-03 09:18:47-07:00
slug: task-add-admit-a-mistake
syndication:
  mastodon: https://hackers.town/@randomgeek/102378568642490016
  twitter: https://twitter.com/brianwisti/status/1146464654262095872
tags:
- taskwarrior
- oops
title: task add 'admit a mistake'
created: 2024-01-15T15:26:42-08:00
updated: 2024-02-02T10:07:45-08:00
---

[checking-in-on-my-idea-bucket](../06/checking-in-on-my-idea-bucket.md) only worked by luck. The `+LATEST` virtual tag is for the latest task in the system, not just the latest in the filter. I want the `newest` report, which lists tasks by freshness, then `limit:` to control the number of tasks reported.

````
$ task '(+idea or +learn)' newest limit:1

ID  Created    Age Mod Project Tags     Description
180 2019-07-02 19h 19h Site    idea ops automate permalink switches
                                          2019-07-02 for when I do a mass change, create aliases of old form

54 tasks, 1 shown
````

Okay right. I threw some new ideas in the last few days. Better set a higher limit.

````
$ task '(+idea or +learn)' newest limit:3

ID  Created    Age Mod Project Tags             Description
180 2019-07-02 19h 19h Site    idea ops         automate permalink switches
                                                  2019-07-02 for when I do a mass change, create aliases of old form
176 2019-06-28 4d  4d          db learn         json1 extension for sqlite
175 2019-06-28 4d  4d          javascript learn set up entropic for Node
````
