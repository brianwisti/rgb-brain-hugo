---
aliases:
- /blogspot/2007/02/12_mp4info-issues.html
- /post/2007/mp4info-issues/
- /2007/02/12/mp4info-issues/
category: post
created: 2024-01-15 15:25:40-08:00
date: 2007-02-12 00:00:00-08:00
slug: mp4info-issues
tags:
- ruby
- blogspot
title: Mp4Info issues
updated: 2024-01-26 09:21:44-08:00
---

> 
 > **2015-03-28**
>
 > No idea whether this is still true, or even if it was just something stupid I was doing in 2007.

[mp4info](https://github.com/arbarlow/ruby-mp4info) thinks that my 5 minute Bob Newhart track is 2 seconds long. Looks like that is an issue on several tracks. I need to dig into that, see why [Perl](../../../card/Perl.md)'s MP4::Info picks up the correct length but the [Ruby](../../../card/Ruby.md) counterpart does not.