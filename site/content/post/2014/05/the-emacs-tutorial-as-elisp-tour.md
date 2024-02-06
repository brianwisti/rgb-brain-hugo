---
aliases:
- /emacs/2014/05/24_the-emacs-tutorial-as-elisp-tour.html
- /post/2014/the-emacs-tutorial-as-elisp-tour/
- /2014/05/24/the-emacs-tutorial-as-elisp-tour/
category: post
created: 2024-01-15 15:25:28-08:00
date: 2014-05-24 00:00:00-07:00
slug: the-emacs-tutorial-as-elisp-tour
tags:
- emacs
- elisp
- tutorial
- tools
title: The Emacs Tutorial as ELisp Tour
updated: 2024-02-02 10:03:57-08:00
---

I am trying to *really* learn how to use [Emacs](../../../card/Emacs.md). One thing that strikes me is how the Emacs user interface can be thought of as a client application to an Emacs Lisp API. This is not a revolutionary thought, but it really stuck in my head. I reread the official tutorial, focusing on the functions rather than the keybindings that invoke them.

<!--more-->

The first function is obviously the one to get the tutorial started.

|Function|Keybinding|Description|
|--------|----------|-----------|
|`help-with-tutorial`|`C-h t`|Launch the Emacs learn-by-doing tutorial|

Then I spent a couple days with liberal usage of `describe-key` and `describe-function` to better understand what the tutorial was describing. It was helpful. Now I just want to organize those notes and post them on the blog.

Or I could [dump the list](elisp-functions-described-in-the-emacs-tutorial.md) onto a blog post.