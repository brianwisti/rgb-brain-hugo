---
aliases:
- /tools/2014/05/31_pulling-a-remote-branch-in-git.html
- /post/2014/pulling-a-remote-branch-in-git/
- /2014/05/31/pulling-a-remote-branch-in-git/
category: post
created: 2024-01-15 15:25:28-08:00
date: 2014-05-31 00:00:00-07:00
slug: pulling-a-remote-branch-in-git
tags:
- git
- shell
- tools
title: Pulling a Remote Branch In Git
updated: '2024-01-26T10:11:37'
---

> 
 > **[tldr](../../../card/tldr.md)**
>
 > `git branch -r` to list remote branches. `git checkout --track -b <local-branch> <remote>/<branch>` to check your branch out.

<!--more-->

Because I know I'll forget it if I don't write it down now.

I've been doing a thing in a branch on one machine, but now I want to do that thing on another machine. I've already pushed that branch to origin, so I don't need to - hold on. I better put that down as well.

# On One Machine

The main concern here is to ensure that my work isn't stuck on the one machine. The `-u` flag (or `--set-upstream` for the verbose) creates a tracking reference upstream, so that the remote repository remembers the branch.

````console
$ git branch
master
* oh-hai
$ git push -u origin oh-hai
````

# On Another Machine

Now that I've created the tracking reference upstream, I can pull it down from the other machine.

````console
$ git branch
* master
$ git branch -r
origin/master
origin/oh-hai
$ git checkout --track -b oh-hai origin/oh-hai
````

Hope I didn't forget anything. I'll find out soon enough.