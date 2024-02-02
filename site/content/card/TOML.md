---
created: 2024-01-15 15:26:52-08:00
title: TOML
updated: 2024-02-01 14:07:33-08:00
---

Tom's Obvious Minimal Language

A minimal configuration file format.

## Syntax

### Comments

````toml
# comments are single-line
````

### Pairs

````toml
name = value
````

#### Keys

* bare: `name`
* quoted: `"user name"` or `'user name'`
* dotted: `user.name` or `'my."user name"'` but please no

#### Value Types

* string
* integer
* float
* boolean
* offset date-time
* local date-time
* local time
* array
* table

## Related

* https://toml.io/en/
* https://github.com/toml-lang/toml
* [TOML: English v1.0.0](https://toml.io/en/v1.0.0)