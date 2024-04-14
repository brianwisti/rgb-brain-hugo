---
category: post
date: 2022-12-25 11:00:00-08:00
description: Ain't no benchmark like an unscientific ad hoc benchmark
slug: nanoc-builds-faster-with-3-2-0
syndication:
  mastodon: https://hackers.town/@randomgeek/109576038838397555
tags:
- ruby
- nanoc
title: Nanoc builds sites faster with 3.2.0
created: 2024-01-15T15:26:02-08:00
updated: 2024-04-01T14:15:44-07:00
banner: attachments/img/2022/cover-2022-12-25.png
---

![tabular display of build time values described in post](attachments/img/2022/cover-2022-12-25.png "just the numbers")

Today is Christmas, which means version [3.2.0](https://www.ruby-lang.org/en/news/2022/12/25/ruby-3-2-0-released/) of [Ruby](../../../card/Ruby.md) has been released. I read Peter Solnica's post about [Benchmarking Ruby 3.2 with YJIT](https://www.solnic.dev/p/benchmarking-ruby-32-with-yjit). One bit of feedback he got was that YJIT — the now official Just In Time compiler — kicks in for frequently called methods:

 > 
 > By default, YJIT optimizes a method on the 30th time you call it.

— Noah Gibbs, [Ruby.social](https://ruby.social/@codefolio/109573860732354569)

Well hey. The [Nanoc](https://nanoc.app) iteration of my site has a few hundred pages. Nanoc probably calls some of its methods 30 or more times for that. Let's find out if 3.2.0 makes a difference.

## I should probably install 3.2.0

This is in my Windows 11 + WSL2 workspace. I wouldn't be surprised if Linux and macOS tests went faster.

Installed 3.2.0 on my system using `rbenv`. Worth mentioning that I had to `export CC=/home/linuxbrew/.linuxbrew/bin/gcc-12` for `rbenv install` to work at all. For some reason I had a `brew`-installed Ruby floating around, too. Removed that with `brew uninstall ruby` so `rbenv install 3.2.0` would work.

I have a very fiddly system.

## The "test"

1. Switch to the right version
1. Install dependencies for that version
1. Build the site
1. Build it again, to see how long things take when nothing's changed
1. Remove the build folder and move on to the next case

First in 3.1.3 to set a baseline of sorts.

````console
$ rbenv local 3.1.3
$ bundle
$ bundle exec nanoc
...
Site compiled in 50.39s.
$ bundle exec nanoc
Site compiled in 43.87s.
$ rm -r output/
````

Don't judge those numbers too harshly. Nanoc site configuration is Ruby code, and mine was very sloppy Ruby code. Regardless, it's way slower than [Hugo](https://gohugo.io).

Now in 3.2.0 without enabling YJIT, to see if just the plain old upgrade is quicker.

````console
$ rbenv local 3.2.0
$ bundle
$ bundle exec nanoc
...
Site compiled in 43.58s.
$ bundle exec nanoc
...
Site compiled in 37.30s.
$ rm -r output/
````

There's variation from one invocation to the next in 3.1.3, but 3.2.0's first build is consistently a sliver faster than 3.1.3's second build.

Finally with YJIT.

````console
$ RUBY_YJIT_ENABLE=1 bundle exec nanoc
...
Site compiled in 29.51s.
$ RUBY_YJIT_ENABLE=1 bundle exec nanoc
...
Site compiled in 23.28s.
````

That is an impressive difference. We're still not talking Hugo numbers, of course.
But under 30 seconds means I might be able to pay attention long enough to fix
my terrible site configuration code.
