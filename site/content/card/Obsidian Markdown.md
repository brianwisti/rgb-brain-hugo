---
title: Obsidian Markdown
created: 2024-01-15T15:28:16-08:00
updated: 2024-01-26T09:08:16-08:00
---

Special considerations and features that I care about for [Markdown](Markdown.md) in [Obsidian](Obsidian.md)

# Linking

* Internal links with `[[link]]`
* Internal images with regular `![](link)` or `![[link]]`
* YouTube embeds with `![](link)`

# Callouts

aka admonitions

````md
> [!TYPE] OPTIONAL TITLE
> BODY
````

Officially supported types. Each entry gets its own rendering style. Any unrecognized type is treated as *Note*.

* Note
* Abstract / summary / tldr
* Info
* Todo
* Tip / Hint / Important
* Success / Check / Done
* Question / Help / Faq
* Warning / Caution / Attention
* Failure / Fail / Missing
* Danger / Error
* Bug
* Example
* Quote / Cite

# Related

* https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown
