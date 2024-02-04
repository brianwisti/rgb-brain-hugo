---
created: 2024-02-04 05:26:07-08:00
title: SDKMAN
updated: 2024-02-04 09:17:40-08:00
---

Command-line tool for version management of [Java](Java.md) and related tools for UNIX-like systems and Windows+MinGW.

## Jots

Installing SDKMAN

````sh
curl -s "https://get.sdkman.io" | bash
````

Get help for a specific command

````sh
sdk help list
````

List available versions for a specific tool

````sh
sdk list java
````

Install a specific JDK:

````sh
sdk install java 17.0.8-tem
````

Install a particular *JVM* tool:

````sh
sdk install maven
````

## Related

* [Home - SDKMAN! the Software Development Kit Manager](https://sdkman.io/)