---
created: 2024-01-15 15:26:23-08:00
title: Volta
updated: 2024-03-21 04:30:16-07:00
---

A version and tool manager for [Node.js](Node.js.md)

## Install and Use Volta

````sh
curl https://get.volta.sh | bash
````

### Usage

Install LTS Node, putting a `node` executable in your `$PATH`:

````shell
volta install node
````

Any `yarn global add` or `npm install -g` gets pinned to your current Node.  You can also use `volta install` for tools, likewise pinned to current Node installation.

````shell
volta install typescript
````

Specify tool versions with `pin`

````shell
volta pin node@20.11.1
volta pin yarn@4.1.1
````

Adds an entry to `package.json`

````json
"volta": {
	"node": "20.11.1",
	"yarn": "4.1.1"
}
````

This entry works like `.nvmrc` for `nvm`, just making it an explicit part of your project definition.

Mostly I just use the global `volta install` for Node and tools.

## Related

* [Volta - The Hassle-Free JavaScript Tool Manager](https://volta.sh/)