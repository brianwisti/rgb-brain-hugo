---
title: timedatectl
---

Control system for time and date details on *Linux*

## Jots

Recurring issue on my frequent Linux reinstalls: reboot into *Windows*, and the time is off by my local UTC offset. Fix that in Linux by telling the system that the *Real Time Clock (RTC)* uses local time

````sh
timedatectl set-local-rtc 1 --adjust-system-clock
````