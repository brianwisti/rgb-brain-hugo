---
aliases:
- /note/2020/79/vs-code-pylint-needs-pylintrc/
- /note/2020/03/vs-code-pylint-needs-pylintrc/
category: note
date: 2020-03-19 10:15:30-07:00
slug: vs-code-pylint-needs-pylintrc
syndication:
  mastodon: https://hackers.town/@randomgeek/103850887978218387
  twitter: https://twitter.com/brianwisti/status/1240691693331943424
tags:
- python
- vscode
- editors
title: VS Code pylint needs pylintrc
---

[Visual Studio Code](https://code.visualstudio.com/) doesn’t seem to pick up my environment’s [PYTHONPATH](https://docs.python.org/3.8/using/cmdline.html#envvar-PYTHONPATH) when running [pylint](https://www.pylint.org/). Makes project-local modules a headache. The solution: put it in your pylint config.

**`${workspaceFolder}/.pylintrc`**

````ini
[MASTER]
init-hook='import sys; sys.path.append("pylib")'
````

Okay, I got more planned for today than messing with code. Back to that other stuff.
