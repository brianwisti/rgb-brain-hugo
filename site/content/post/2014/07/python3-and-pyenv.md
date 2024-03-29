---
aliases:
- /tools/2014/07/04_python3-venv.html
- /post/2014/python3-venv/
- /2014/07/04/python3-and-pyvenv/
category: post
created: 2024-01-15 15:26:15-08:00
date: 2014-07-04 00:00:00-07:00
slug: python3-and-pyenv
tags:
- python
- tools
title: Python3 and pyvenv
updated: 2024-02-01 20:40:00-08:00
---

I have been spending much of my coding time in [Python](../../../card/Python.md) recently. This site is built in [Pelican](../../../card/Pelican.md). Many lines of Python have been written for work. I have even been poking at [Google App Engine](https://developers.google.com/appengine/docs/python/) in what spare time is available. The only disappointment is that all of these have been in Python 2. I would prefer to be using [Python 3](https://wiki.python.org/moin/Python2orPython3). There is a little free time today, so I will set up a nice Python 3 workspace.

<!--more-->

One of the interesting things about Python is how it handles personal workspaces. Popular tools in other languages, such as [rbenv](http://rbenv.org/) for [Ruby](../../../card/Ruby.md) and [perlbrew](http://perlbrew.pl/) for [Perl](../../../card/Perl.md), focus on a complete localized installation for any version you care to use. Python tools assume a system standard version, and focus on making a snapshot for your projects. That works *sort of* like [Bundler](http://bundler.io/). Once you have your snapshot loaded, you use [pip](http://pip.readthedocs.org/) to install the exact libraries needed by your projects. That works very much like Bundler.

The tool of choice for making virtual environments in Python 3 is [pyvenv](https://docs.python.org/dev/library/venv.html). pyvenv actually comes with the standard installation of Python 3.3 or greater. That is good news. Python 2's [virtualenv](http://virtualenv.readthedocs.org/) was not hard to install, but it was not available by default. You still had to *install* it.

There is already an excellent [introduction](https://packaging.python.org/en/latest/tutorial.html#creating-and-using-virtual-environments) to using pyvenv. That tells most of what you need to know.

````console
$ pyvenv my-project
$ source my-project/bin/activate
(my-project) $
````

Now `my-project` holds the default Python interpreter until you exit that particular shell or activate a different virtual environment.

That is good enough to get started, but I often have several projects going. Each project gets its own virtual environment. Having my environment files just sitting there in my project folder bothers me, though.

I like things tidy, so I use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html). virtualenvwrapper creates a single folder to hold your virtual environments and provides you with a couple of shell commands to manage those environments. It's easy if you're only using a single system Python. Just follow their installation [instructions](http://virtualenvwrapper.readthedocs.org/en/latest/install.html). After that, `mkvirtualenv` and `workon` are your friends.

````console
$ mkvirtualenv mypy3
(mypy3) $
# later, in another shell
$ workon mypy3
(mypy3) $
````

What if I wanted to use both Python 2 and Python 3 virtual environments? Well, the virtual environments I already had set up for work function without any problem. Thank goodness. If I wanted to do new Python 2 work - well, that may be a good time to pull up a *real* virtual environment with a tool like [Vagrant](http://www.vagrantup.com/). I may come back to that later.