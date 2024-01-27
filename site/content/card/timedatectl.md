---
created: 2024-01-19 15:37:27-08:00
title: timedatectl
updated: '2024-01-26T09:09:33'
---

Control system for time and date details on *Linux*

# Jots

Recurring issue on my frequent Linux reinstalls: reboot into *Windows*, and the time is off by my local UTC offset. Fix that in Linux by telling the system that the *Real Time Clock (RTC)* uses local time

````sh
timedatectl set-local-rtc 1 --adjust-system-clock
````