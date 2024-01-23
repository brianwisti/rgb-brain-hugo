---
aliases:
- /tools/2015/07/16_remote-editing-in-atom.html
- /post/2015/remote-editing-in-atom/
- /2015/07/16/remote-editing-in-atom/
category: post
date: 2015-07-16 00:00:00-07:00
description: I am slowly learning more about how to use Atom for real work.
slug: remote-editing-in-atom
tags:
- atom-editor
- editors
- tools
title: Remote Editing In Atom
---

I am slowly learning more about how to use [Atom](https://atom.io) for real work. First requirement: my "real work" almost exclusively takes place on a virtual machine. Atom alone cannot handle editing those files. [remote-atom](https://atom.io/packages/remote-atom) to the rescue!

Well, sort of. It’s not as reflexive as bouncing around in a [Vim](../../../card/Vim.md) session, but some of that must be due to lack of familiarity.

It works, though.

You can install the remote-atom package from Atom’s [Settings View](https://atom.io/packages/settings-view). Follow the directions on the [remote-atom](https://atom.io/packages/remote-atom) package page! You’ll end up with an `rmate` executable on your virtual machine, corresponding to a [master copy](https://raw.githubusercontent.com/aurora/rmate/master/rmate) in the remote-atom git repo.

`rmate` communicates with the Remote Atom service, which you need to manage yourself. You can do this from the *Packages* menu, but I want to get comfortable with the [Command Palette](https://atom.io/packages/command-palette).

![Start Remote Atom Server from Command Palette](attachments/img/2015/remote-atom-start-server.png)

Once the server is available, you can `rmate` files to your heart’s content.

````
$ rmate lib/secret-work-stuff
$ rmate test/secret-work-tests
````

No point showing a screenshot of `lib/secret-work-stuff`. It’s just another tab as far as the Atom user interface is concerned. Saving correctly updated the file on my virtual machine. Simple and straightforward.

Eventually you may want to stop the server. Again, from the Command Palette.

![Stop Server from the Command Palette](attachments/img/2015/remote-atom-stop-server.png)

I’m still not ready to use Atom as my primary or even secondary editor. However, it’s starting to feel useful — thanks to packages like remote-atom.
