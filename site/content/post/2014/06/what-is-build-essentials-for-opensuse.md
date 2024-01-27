---
aliases:
- /tools/2014/06/22_what-is-build-essentials-for-opensuse.html
- /post/2014/what-is-build-essentials-for-opensuse/
- /2014/06/22/what-is-build-essentials-for-opensuse/
category: post
created: 2024-01-15 15:25:28-08:00
date: 2014-06-22 00:00:00-07:00
slug: what-is-build-essentials-for-opensuse
tags:
- suse
- tools
title: What is build-essentials for openSUSE
updated: '2024-01-26T10:11:45'
---

> 
 > **[tldr](../../../card/tldr.md)**
>
 > `devel_basis`

<!--more-->

This is the umpteenth time I looked up what [build-essential](http://packages.ubuntu.com/trusty/build-essential) is on [openSUSE](http://opensuse.org).
For my purposes, it's the [devel_basis](http://software.opensuse.org/package/patterns-openSUSE-devel_basis) pattern.

To see what packages have the pattern,

````sh
zypper info -t pattern devel_basis
````

Yes it has a lot of packages, but I usually end up installing many of those anyways.

To install `devel_basis`,

````sh
sudo zypper install -t pattern devel_basis
````

That's all. I've started remembering to *use* the notes on my site, which  means it occurs to me that more notes would be helpful.