---
created: 2024-01-15 15:26:37-08:00
title: Lua
updated: 2024-03-21 04:43:41-07:00
---

[Programming Language](Programming%20Language.md) *usually* used in an embedded context

## Installing packages with Luarocks

If installing packages with `--local`, then your shell init must include where to find those local packages.

````bash
# ~/.bash_profile

if [[ -n "`which luarocks 2>/dev/null`" ]]; then
  eval `luarocks path --bin`
fi
````

## Related

* [The Programming Language Lua](https://www.lua.org/home.html)
* [Lua Programming Gems](https://www.lua.org/gems/)