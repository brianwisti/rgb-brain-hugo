---
created: 2024-06-15T08:45:50-07:00
updated: 2024-06-15T08:46:37-07:00
title: Massive Geek Attack
date: 2002-05-02
---

That [Seattle.rb](https://web.archive.org/web/20050206183943/http://www.zenspider.com/seattle.rb) meeting got me to thinking. Unit testing is a big part of software development, but I know very little about it. It seems to me that my cute little [pagetemplate](../06/pagetemplate.md) project presents a perfect opportunity to learn. It's a small project, so I can keep most of it in my head. It's not so small that unit testing would be overkill - "killing a fly with a bazooka". I was bothered by some of the robustness of the code anyways.

Why has the code been on my mind? I've been reading [The Practice of Programming](https://web.archive.org/web/20050206183943/http://tpop.awl.com/), by Kernighan and Pike. This book is a broad strokes overview of how to be a good developer. It covers design, algorithms, testing, and quite a bit more, in a thin volume. Good stuff. If you already have a good idea how to write code, but want to be an actual programmer, I highly recommend this book.

Enough with the sales pitch. The book helped me understand several data structures: what they are, how to use them, and most importantly, when you could use them. I've had several "a-ha" moments reading TPOP, and one of them involved a complete rewrite of the PageTemplate engine using much cleaner data structures.

That's my new plan. Write some test cases, write the code, release when everything is okay, and then do whatever my heart desires.
