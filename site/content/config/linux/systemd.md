---
title: My user-level systemd
tags:
- config
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
