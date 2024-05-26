---
created: 2024-01-24 09:44:59-08:00
title: My export-ignore
updated: 2024-01-26 20:31:48-08:00
---

The folders [obsidian-export](obsidian-export.md) should *never* pull into [My Public Brain](My%20Public%20Brain.md).

````
_scripts/
_templates/
canvas/
inbox/
jot/
journal/
````

[How These Notes are Organized](How%20These%20Notes%20are%20Organized.md) covers the folder convention, but basically:

* folders with a leading underscore (`_`)  hold support files for my Obsidian vault
* I haven't figured out how or even whether I should publish canvas whiteboards
* the other folders contain explicitly private notes.

Probably a good idea to add a test for these.