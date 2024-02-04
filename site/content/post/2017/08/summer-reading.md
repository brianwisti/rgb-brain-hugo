---
aliases:
- /post/2017/summer-reading/
- /2017/08/17/summer-reading/
category: post
date: 2017-08-17 00:00:00-07:00
slug: summer-reading
syndication:
  twitter: https://twitter.com/brianwisti/status/898433031416889344
tags:
- books
- marginalia
title: Summer Reading
created: 2024-01-15T15:26:50-08:00
updated: 2024-02-02T10:02:02-08:00
---

What have I been doing with my spare time? I’ve been reading books. Not too  much. Mostly tech.

<!--more-->

## The Imposter’s Handbook

[The Imposter’s Handbook](https://bigmachine.io/products/the-imposters-handbook/) aims for readers - especially experienced developers — who never got around to earning a degree related to software development. That’s me!

It describes the programming domain well enough, going so far as to discuss [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus). That chapter challenged me the most. The rest, on topics ranging from complexity theory to data structures, algorithms, computation, databases, design patterns, and the basics of the UNIX command line, whetted my appetite for more information on each topic.

That led me to the next book in my summer reading.

## The Linux Command Line

The first edition of *The Linux Command Line* appeared before [systemd](https://freedesktop.org/wiki/Software/systemd/) took over the world’s Linux systems. The change resulted in odd corners of incompatibility when working through the book on my [Linux Mint](https://linuxmint.com/) 18.2 desktop. Fortunately, William Shotts continued to update the book. The [Third Internet Edition](http://linuxcommand.org/tlcl.php) is available online under a Creative Commons License.

This book builds its reader up from minimal understanding to being comfortably competent using the Linux shell and scripting in [Bash](https://www.gnu.org/software/bash/). It applies well to most Linux systems, and some pieces also apply on OS X.

I particularly enjoyed the introduction to [GNU Coreutils](https://www.gnu.org/software/coreutils/coreutils.html), which does more than I ever knew. Seeing [`date`](https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html#date-invocation) do things I usually run to a library for in my favorite languages almost made me angry!

````
$ date --date='2 weeks ago' '+%F'
2017-08-03
````

Maybe not *angry*. It surprised me though. I explore new corners of GNU Coreutils regularly now.

Nevertheless, by the end of the book I was ready to jump back to a programming language with better features for describing complex problems. Perl, Python, Ruby - these are still more familiar to me.

I sort of wanted to learn an unfamiliar language, though.

## Go In Action

Just a couple chapters into [this one](https://www.manning.com/books/go-in-action). The author could use [emacs-writegood-mode](emacs-writegood-mode.md). Still, [Go](../../../card/Go.md) is a widely used language. I feel a certain moral responsibility to learn it. Of course, that’s how I felt about Java for the first 15 years of my career. Never really learned Java. My bad attitude about Java may be leaking over to my attitude about studying Go. I better keep an eye on that, and see how I feel at the end of *Go In Action*.

## Intermission

For the next couple of days I’ll focus on getting my notes for *The Imposter’s Handbook* and *The Linux Command Line* from paper into [Org](../../../card/Org.md). My old brain still finds it easier to get the initial thoughts down on paper. Then I copy the notes into org files, which simplifies searching and using those notes later. Honestly, I tend to abandon my paper notes and forget whatever I studied. This new two step process already has me using and referencing my notes more often.

Incidentally - I spend enough time in [Emacs](../../../card/Emacs.md) these days that it’s starting to become *more* comfortable for me than [Vim](../../../card/Vim.md). This is a strange and uncomfortable sensation for me. I may start editing something in Vim, but soon enough I switch over to Emacs.

Maybe I should add the [GNU Emacs Lisp Reference Manual](https://www.gnu.org/software/emacs/manual/elisp.html) to my reading list.
