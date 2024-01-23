---
title: My GNU Bash Profile
tags:
- config
---

I use my `~/.bash_profile` to set environment variables and load config for assorted
package managers.

For a while there, tmux gave me nested login shells.
This confused `$PATH` handling in all sorts of ways.

````bash
PATH="/usr/bin:/bin:/usr/sbin:/sbin"
source /etc/profile
````

Some little convenience functions for viewing and managing the path.

````bash
showpath() {
  perl -E 'say for split /:/, $ENV{PATH}'
}

pathadd() {
  if [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]]; then
    PATH="$1${PATH:+":$PATH"}"
  fi
}
````

Ah, ~~Linuxbrew~~ Homebrew — the solution to, and cause of, so many shell problems.

````bash
if [ -d "/home/linuxbrew" ] ; then
  # For Homebrew on Linux
  # Output to `/home/linuxbrew/.linuxbrew/bin/brew shellenv`
  eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)

  if [ -d "/home/linuxbrew/.linuxbrew/lib/ruby/gems/3.1.0/bin" ] ; then
    pathadd "/home/linuxbrew/.linuxbrew/lib/ruby/gems/3.1.0/bin"
  fi

  export BREW_PYTHON_HOME="/home/linuxbrew/.linuxbrew/Cellar/python@3.10/3.10.8/libexec/bin"

fi
````

Set a few preferences for openers and editors.

````bash
export PAGER="less -FRX"
export EDITOR=nvim
export NNN_FALLBACK_OPENER=xdg-open
````

Make sure `doom` is available if I've got it that week.

````bash
export DOOM_HOME="$HOME/emacs-configs/emacs-doom"

if [ -d "$DOOM_HOME" ]; then
  pathadd "$DOOM_HOME/bin"
fi
````

## Programming Language Managers

GHCup for Haskell.

````bash
[ -f "$HOME/.ghcup/env" ] && source "$HOME/.ghcup/env"
````

Plenv for managing Perl versions.

````bash
export PLENV_HOME="$HOME/.plenv"

if [ -d "$PLENV_HOME" ]; then
  pathadd "$PLENV_HOME/bin"
fi

if which plenv > /dev/null; then eval "$(plenv init -)"; fi
````

Pyenv for managing Python versions.

````bash
export PYENV_ROOT="$HOME/.pyenv"

if [ -d "$PYENV_ROOT" ]; then
  pathadd "$PYENV_ROOT/bin"
fi

if which pyenv > /dev/null; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  if which pyenv-virtualenv-init > /dev/null; then
    eval "$(pyenv virtualenv-init -)"
  fi
fi
````

Poetry for managing Python projects and their language versions.

````bash
[ -d "$HOME/.poetry/bin" ] && pathadd "$HOME/.poetry/bin"
````

Rakubrew for managing Raku versions.

````bash
export RAKUBREW_HOME="$HOME/.rakubrew"

if [ -d "$RAKUBREW_HOME" ]; then
  pathadd "$RAKUBREW_HOME/bin"
  pathadd "$RAKUBREW_HOME/shims"
  eval "$(rakubrew init Bash)"
fi
````

Rbenv for managing Ruby versions.

````bash
if which rbenv > /dev/null; then
  pathadd "$HOME/.rbenv/shims"
  eval "$(rbenv init - bash)";
fi
````

Cargo for managing Rust versions.

````bash
[ -f "$HOME/.cargo/env" ] && . "$HOME/.cargo/env"
````

Volta for managing Node.js versions and global commands.

````bash
export VOLTA_HOME="$HOME/.volta"

[ -d "$VOLTA_HOME" ] && pathadd "$VOLTA_HOME/bin"
````

Better make sure `~/bin` and `~/.local/bin` are in my path.

````bash
[ -d "$HOME/bin" ] && pathadd "$HOME/bin"
[ -d "$HOME/.local/bin" ] && pathadd "$HOME/.local/bin"
````

Then at the end of the whole thing, if I'm running bash I source my `~/.bashrc`?
Well, okay.
I guess it made sense at the time.

````bash
if [ -n "$BASH_VERSION" -a -n "$PS1" ]; then
  if [ -f "$HOME/.bashrc" ]; then
    . "$HOME/.bashrc"
  fi
fi
````
