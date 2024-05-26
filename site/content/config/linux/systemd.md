---
title: My user-level systemd
tags:
- config
created: 2024-01-15T17:29:21-08:00
updated: 2024-05-01T22:38:50-07:00
---

The `autostart` target describes services that should start with a fresh user session.
Or it will eventually.
Mostly I'm just working on a reproducible setup for [dex](https://github.com/jceb/dex).

````conf
//- file:systemd/user/autostart.target
Description=current graphical user session
RefuseManualStart=no
StopWhenUnneeded=no
````
