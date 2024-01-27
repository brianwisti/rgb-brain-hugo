---
aliases:
- /tools/2014/06/18_pretty-recursive-grep.html
- /post/2014/pretty-recursive-grep/
- /2014/06/18/pretty-recursive-grep/
category: post
created: 2024-01-15 15:25:29-08:00
date: 2014-06-18 00:00:00-07:00
slug: pretty-recursive-grep
tags:
- shell
- tools
title: Pretty Recursive Grep
updated: '2024-01-26T10:11:43'
---

> 
 > **[tldr](../../../card/tldr.md)**
>
 > Set `GREP_OPTIONS='-RI --color=auto'`. Or install [ack](http://beyondgrep.com).

<!--more-->

I'm looking for TODO entries in source code on a machine that does not have Ack installed. It does have [GNU grep](http://www.gnu.org/software/grep/), though.

Obviously I want to search subdirectories. I can choose between `--recursive`, `-R`, or using `rgrep` on this particular machine.

I am usually searching through source code. I hardly ever want binary files to match. That means `--binary-file=without-match`  or `-I`.

Finally, I like pretty colors. The `--color=auto` option makes me happy.

That leaves me with this invocation.

````console
$ grep --recursive --binary-file=without-match --color=auto 'TODO' .
````

Or maybe the short form would be easier.

````console
$ rgrep -I --color=auto 'TODO' .
````

Probably smartest to look at what [environment variables](http://www.gnu.org/software/grep/manual/html_node/Environment-Variables.html) I could set up in order to skip remembering this stuff at all.

````bash
export GREP_OPTIONS='-RI --color=auto'
````

Pop that in my `.bashrc` and I'm set.

````console
$ grep 'TODO' .
````

All right. Back to work.