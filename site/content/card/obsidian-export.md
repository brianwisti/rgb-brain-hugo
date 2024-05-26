---
created: 2024-01-21 08:19:33-08:00
title: obsidian-export
updated: 2024-01-26 09:08:22-08:00
---

A [Rust](Rust.md) library and CLI tool for exporting [Obsidian](Obsidian.md) vault contents into regular [Markdown](Markdown.md). This cuts down a few steps for your [Static Site Generator](Static%20Site%20Generator.md) or other processing scripts.

There's curl-bash installation instructions corresponding to specific versions on the [Releases](https://github.com/zoni/obsidian-export/releases) page.

The `obsidian-export` README provides sample templates for [Using obsidian-export with Hugo](Using%20obsidian-export%20with%20Hugo.md)

# Jots

Obsidian Sync doesn't copy dotfiles. `.export-ignore` needs to be added on every platform that you're running `obsidian-export`. So, better keep track of [My export-ignore](My%20export-ignore.md)

Transforms unavailable links – say, *2024-01-21 Sun* for example – into unlinked italicized text during export.

# Related

* [GitHub - zoni/obsidian-export: Rust library and CLI to export an Obsidian vault to regular Markdown](https://github.com/zoni/obsidian-export)