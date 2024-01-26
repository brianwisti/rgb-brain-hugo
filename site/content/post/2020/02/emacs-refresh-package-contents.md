---
aliases:
- /note/2020/59/emacs-refresh-package-contents/
- /note/2020/02/emacs-refresh-package-contents/
category: note
created: 2024-01-15 15:26:39-08:00
date: 2020-02-28 07:23:53-08:00
slug: emacs-refresh-package-contents
syndication:
  mastodon: https://hackers.town/@randomgeek/103737312348546113
  twitter: https://twitter.com/brianwisti/status/1233422528829444096
tags:
- emacs
- packages
title: Emacs refresh-package-contents
updated: 2024-01-26 11:03:20-08:00
---

Tried adding [Evil](https://www.emacswiki.org/emacs/Evil)  to [Emacs](../../../card/Emacs.md) with [use-package](../../2019/11/emacs-use-package.md). Didn’t work.

Didn’t write the error message down, of course. Something about MELPA looking for a package version from two months ago and deciding the package was "Not Found".

Eventually figured out I need to run `package-refresh-contents`, which grabs the latest package listings. Might be overkill to run that automatically in every Emacs session, so I won’t add it to my `.emacs`.

I will add a comment though.

````elisp
;; Package not installing?
;;  Try 'M-x package-refresh-contents'

(require 'package)
````

Hopefully I remember to read my own comments.

Or the [documentation](https://evil.readthedocs.io/en/latest/overview.html#installation-via-package-el).

 > 
 > **2020-04-29**
>
 > [john sj anderson](https://genehack.org) wrote a post   [expanding](https://genehack.blog/2020/04/a-bit-of-emacs-advice/) on a [suggestion](https://mastodon.social/@genehack/103737652356761968) to use [advising functions](https://www.gnu.org/software/emacs/manual/html_node/elisp/Advising-Functions.html).