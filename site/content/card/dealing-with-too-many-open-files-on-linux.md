---
created: 2024-06-15T08:49:12-07:00
updated: 2024-06-15T08:52:10-07:00
title: Dealing with "too many open files" on Linux
---

`ulimit` shows the maximum number of files you can open. Use `-S` to see the *soft limit*.

````bash
ulimit -S -n
1024
````

And `-H` for the hard limit

````bash
ulimit -H -n
1048576
````

Increase the soft limit — up to your hard limit — for the current session.

````bash
ulimit -n 2048
````

## To permanently change file limits

Edit `/etc/systemd/system.conf`

````
DefaultLimitNOFILE=4096:1048576
````

Then `/etc/systemd/user.conf`

````
DefaultLimitNOFILE=4096:1048576
````

Apply the change with Systemd

````bash
sudo systemctl daemon-reexec
````
