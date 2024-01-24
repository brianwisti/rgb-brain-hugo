---
category: post
date: 2021-08-09 00:00:00-07:00
description: testing a python remote plugin for quicker reStructuredText in Hugo
slug: trying-a-thing-with-neovim
syndication:
  mastodon: https://hackers.town/@randomgeek/106729657575874145
  twitter: https://twitter.com/brianwisti/status/1424932452972343304
tags:
- neovim
- python
- hugo
- rst
- site
- tools
title: trying a thing with neovim
updated: 2021-08-10 00:00:00-07:00
---

But will it even work?

Oh right I need to `:UpdateRemotePlugins` first.

## Test \[PASSED\]

It worked!

### What did I just do?

I used a [remote plugin](https://neovim.io/doc/user/remote_plugin.html) in [card/Neovim](../../../card/Neovim.md) to transform my [card/reStructuredText](../../../card/reStructuredText.md) into an HTML source document, simplifying [card/Hugo](../../../card/Hugo.md)'s site-building duties.

I won't make you wait around for a proper post. Hugo lets you use reStructuredText.  But Hugo's way is slow and hard to customize. Not their fault. reStructuredText is not their focus.

Still — why not format it ahead of time?

 > 
 > **Answer**
>
 > Because it took a lot of work to figure this out? And most folks are perfectly happy with Markdown? And bloggers who prefer reStructuredText are probably using [card/Pelican](../../../card/Pelican.md) or [card/Nikola](../../../card/Nikola.md)?

Shush, me.

### The Implementation

Start with `content/whatever/index.rst.txt`.

Make sure Hugo won't track `rst.txt` files by explicitly adding an item the [`ignoreFiles`](https://gohugo.io/getting-started/configuration/#ignore-content-and-data-files-when-rendering) config setting.

````toml
# config.toml
ignoreFiles = ['\.rst\.txt$']
````

This way `hugo server --navigateToChanged` behaves how we expect.

I tried setting `ignoreFiles = ['\.rst$']` but as far as I could tell, Hugo ignored my request to ignore the file. Looks like I'm sticking with `.rst.txt` for now.

With the code down below in my Neovim python3 — that's *python3* not *python* — rplugin folder, and remote plugins updated, I write `index.rst.txt` to disk.

The remote plugin transforms it to HTML, copying my YAML frontmatter as is. So what Hugo sees is updated HTML with frontmatter, and builds that into the site templates nice and quick.

#### The Code

````python{title="~/.config/nvim/rplugin/python3/rstbuild_hugo.py"}
"""Give my reStructuredText posts in Hugo a little boost."""

import locale

import frontmatter
import pynvim
from docutils.core import publish_parts

locale.setlocale(locale.LC_ALL, "")


def determine_target(source: str) -> str:
    # Using an odd suffix so Hugo doesn't try to build the rst itself
    if not source.endswith(".rst.txt"):
        raise ValueError(f"Look at {source} more closely before transforming it.")

    return source.replace(".rst.txt", ".html")


@pynvim.plugin
class RSTBuildHugo:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.autocmd("BufWritePost", pattern="*.rst.txt", eval='expand("<afile>")')
    def convert_file(self, source_filename: str) -> None:
        target_path = determine_target(source_filename)
        post = frontmatter.load(source_filename)
        parts = publish_parts(source=post.content, writer_name="html")
        post.content = parts["body"]
        post.metadata["format"] = "rst"

        with open(target_path, "w") as out:
            out.write(frontmatter.dumps(post))

        self.nvim.out_write(f"Wrote {target_path}\n")
````

Lord knows this code ain't perfect. This post is its main test. Who knows what bugs and improvements will come later?

 > 
 > **NOTE**
>
 > *You* will, if you skim the Updates at the end.

If you grab a copy for your own nefarious plans — a similar template could get you fast Asciidoctor transforms as well — just remember a couple things:

* make sure the Python you're using has the libraries needed; I listed my  choices below

* put it in the right folder; `rplugin/python` is for Python 2; `rplugin/python3` is for Python 3

* run `:UpdateRemotePlugins` and restart Neovim when you make changes to the plugin file

### Libraries Used

* [Docutils](https://docutils.sourceforge.io/) of course, for transforming the reStructuredText
* Docutils takes advantage of the fact that I have [Pygments](https://pygments.org/) installed, for syntax highlighting
* [Python Frontmatter](https://python-frontmatter.readthedocs.io/en/latest/index.html) gives me a consistent tool for handling post frontmatter and content
* [pynvim](https://pynvim.readthedocs.io/en/latest/) is the bit that hooks it all into Neovim