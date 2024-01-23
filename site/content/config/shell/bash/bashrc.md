---
title: My bashrc
tags:
- config
---

GNU Bash runs this for non-login shells.
So if we aren't running interactively, skip the rest of the file.

````bash
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
````

Manage the command history.
Only include unique commands that don't start with a space.
Append to the history file so it grows over time,
but don't let it get *too* big.

````bash
HISTCONTROL=ignoreboth
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000
````

Check the window size after each command and update the values of LINES and COLUMNS.

````bash
shopt -s checkwinsize
````

I'm accustomed to `**` meaning a recursive match in globs.
Just making sure that carries over to interactive shell sessions.

````bash
shopt -s globstar
````

Track those shell aliases I'm so fond of assembling.

````bash
[ -f ~/.bash_aliases ] && . ~/.bash_aliases
````

Enable tab-completion features in case they weren't already.

````bash
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
````

Add Homebrew completions when I've got that available.

````bash
if which brew &> /dev/null; then
  export BREW_PREFIX=`brew --prefix`
  if [ -f "$BREW_PREFIX/etc/bash_completion" ]; then
    . "$BREW_PREFIX/etc/bash_completion.d/git-completion.bash"
    . "$BREW_PREFIX/etc/bash_completion.d/git-prompt.sh"
    . "$BREW_PREFIX/etc/bash_completion"
  fi
fi
````

Run the `keychain` OpenSSH key manager for my shell sessions.

````bash
if which keychain > /dev/null; then
  eval `keychain --eval --agents ssh id_rsa`
fi
````

Load Direnv hooks if available.

````bash
if which direnv > /dev/null; then eval "$(direnv hook bash)"; fi
````

Load hooks for the `fzf` fuzzy finder.

````bash
[ -f ~/.fzf.bash ] && source ~/.fzf.bash
````

I sometimes have things to run locally that don't need to be in my universal config.

````bash
[ -f ~/.bashrc_local_after ] && . ~/.bashrc_local_after
````

Try to get tmux playing nice with existing sessions.

````bash
if [[ -n "\$PS1" ]] && [[ -z "\$TMUX" ]] && [[ -n "\$SSH_CONNECTION" ]]; then
  tmux attach-session -t remote || tmux new-session -s remote
fi
````

And finally, show my pretty prompt from Starship.

````bash
eval "$(starship init bash)"
````
