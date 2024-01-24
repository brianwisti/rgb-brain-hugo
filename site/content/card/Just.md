---
aliases:
- justfile
title: just
---


 > 
 > Just a command runner

## Loading from `.env`

Once you tell it where to look, `just` loads dotenv files and treats its contents as environment variables.

So if my `.env` looks like this:

````sh
VAULT_HOME="/home/random/vaults/v2024"
````

And my justfile has this:

````
dotenv-file := ".env"

export:
  obsidian-export $VAULT_HOME site/content
````

Then I can stop hard-coding paths in my [obsidian-export](obsidian-export.md) invocation.

## Related

* https://github.com/casey/just
