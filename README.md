# Random Geekery Blog Public Brain

This grabs my notes from Obsidian and builds them into a Web site with Hugo.

## Environment

`$PYTHONPATH` needs to include `note_processor`. For the moment I have a `.envrc` with the relevant line:

```sh
export PYTHONPATH="note_processor:$PYTHONPATH"
```

### Environment variables

`VAULT_HOME`
: path to my Obsidian notes