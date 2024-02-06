---
aliases:
- /config/nushell/env.nu/
created: 2024-01-15 17:29:21-08:00
tags:
- config
- nushell
title: My Nushell environment file
updated: 2024-02-05 16:22:37-08:00
---

## Set up my prompt

Adds a Starship prompt on the right and a timestamp on the left.

````nu
def create_left_prompt [] {
  starship prompt --cmd-duration $env.CMD_DURATION_MS $'--status=($env.LAST_EXIT_CODE)'
}
def create_right_prompt [] {
    let time_segment = ([
        (date now | date format '%m/%d/%Y %r')
    ] | str collect)

    $time_segment
}
let-env STARSHIP_SHELL = "nu"
let-env PROMPT_COMMAND = { create_left_prompt }
let-env PROMPT_COMMAND_RIGHT = { create_right_prompt }
let-env PROMPT_INDICATOR = { "" }
let-env PROMPT_INDICATOR_VI_INSERT = { ": " }
let-env PROMPT_INDICATOR_VI_NORMAL = { "〉" }
let-env PROMPT_MULTILINE_INDICATOR = { "::: " }
````

## Environment conversions

Nushell isn't my login shell yet.
This logic converts existing environment variables to Nu equivalents.
So far it works on Linux, Windows, and macOS.

````nu
let-env ENV_CONVERSIONS = {
  "PATH": {
    from_string: { |s| $s | split row (char esep) }
    to_string: { |v| $v | str collect (char esep) }
  }
  "Path": {
    from_string: { |s| $s | split row (char esep) }
    to_string: { |v| $v | str collect (char esep) }
  }
}
````

## Nu libraries and plugins

I don't have many yet, but here's where Nu should expect to find them.

````nu
let-env NU_LIB_DIRS = [
    ($nu.config-path | path dirname | path join 'scripts')
]
let-env NU_PLUGIN_DIRS = [
    ($nu.config-path | path dirname | path join 'plugins')
]
````

## Path management

Environment variables in Nushell are a bit more strict than other shells.
You can't just re-export.
You have to redeclare.
So this function helps me with my most common case:
managing entries in the executable path.

If `new_path` isn't already in `$env.PATH`,
a new `$env.PATH` is declared by prepending the new path to the current list of paths.

````nu
def-env ensure-path [new_path: string] {
  let full_path = ($new_path | path expand)
  let updated_env_path = (
    if $new_path in $env.PATH { $env.PATH }
    else {
      $env.PATH | prepend $full_path
    }
  )
  let-env PATH = $updated_env_path
}
````

And then I use it for the paths I care about most.
Mostly useful when using Nushell as login,
since these entries are usually picked up from the parent shell.

````nu
(ensure-path "~/.local/bin")
(ensure-path "~/.volta/bin")
(ensure-path "~/.cargo/bin")
(ensure-path "~/.rakubrew/bin")
````

Kinda suggests maybe these invocations should go in `login.nu`.

## Miscellaneous

Load the script that nicely formats Taskwarrior output.

````nu
source /home/random/.config/nushell/lib/task.nu
````

Add a function to read from EDN sources such as output by `nbb-logseq`.
Requires the `jet` CLI tool.

````nu
def from-edn [] {
  $in | str collect | jet --to json | from json
}
````