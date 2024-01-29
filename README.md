# Random Geekery Blog Public Brain

This grabs my notes from Obsidian and builds them into a Web site with Hugo.

## Environment

`$PYTHONPATH` needs to include `note_processor`. For the moment I have a
`.envrc` with the relevant line:

```sh
export PYTHONPATH="note_processor:$PYTHONPATH"
```

### Environment variables

`VAULT_HOME`
: path to my Obsidian notes

## License

This is a personal project, but you're free to use the code found in here as
inspiration for your own export / publishing system. Please follow [MIT
License](./LICENSE.md) terms when using that code in your own work.
