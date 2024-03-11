---
created: 2024-01-15 15:26:16-08:00
title: Python
updated: 2024-03-08 20:37:40-08:00
---

# Python

 > 
 > Python is a [Programming Language](Programming%20Language.md) that lets you work quickly and integrate systems more effectively.

Convincing people to give Python a try used to take a lot more work.

## Pyenv

[GitHub - pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)

For managing your Python installations. I use `pyenv` and `pyenv-virtualenv`.

### Pyenv Dependencies

[Pyenv wiki: Suggested build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

Ubuntu:

````
sudo apt install build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev
````

Arch:

````bash
yay -S --needed base-devel openssl zlib xz tk
````

## PDM

Package and dependency manager for Python

[Introduction - PDM](https://pdm.fming.dev/latest/)

### Commands

|Command|Description|
|-------|-----------|
|`add`|Add package(s) to pyproject.toml and install them|
|`build`|Build artifacts for distribution|
|`cache`|Control the caches of PDM|
|`completion`|Generate completion scripts for the given shell|
|`config`|Display the current configuration|
|`export`|Export the locked packages set to other formats|
|`fix`|Fix the project problems according to the latest version of PDM|
|`import`|Import project metadata from other formats|
|`info`|Show the project information|
|`init`|Initialize a pyproject.toml for PDM|
|`install`|Install dependencies from lock file|
|`list`|List packages installed in the current working set|
|`lock`|Resolve and lock dependencies|
|`publish`|Build and publish the project to PyPI|
|`remove`|Remove packages from pyproject.toml|
|`run`|Run commands or scripts with local packages loaded|
|`search`|Search for PyPI packages|
|`self`|Manage the PDM program itself (previously known as plugin)|
|`show`|Show the package information|
|`sync`|Synchronize the current working set with lock file|
|`update`|Update package(s) in pyproject.toml|
|`use`|Use the given python version or path as base interpreter|
|`venv`|Virtualenv management|

````
bsh ❯ pdm
Usage: pdm [-h] [-V] [-c CONFIG] [-v] [-I] [--pep582 [SHELL]] ...

    ____  ____  __  ___
   / __ \/ __ \/  |/  /
  / /_/ / / / / /|_/ /
 / ____/ /_/ / /  / /
/_/   /_____/_/  /_/

Options:
  -h, --help            Show this help message and exit.
  -V, --version         Show the version and exit
  -c CONFIG, --config CONFIG
                        Specify another config file path [env var: PDM_CONFIG_FILE]
  -v, --verbose         Use `-v` for detailed output and `-vv` for more detailed
  -I, --ignore-python   Ignore the Python path saved in .pdm-python. [env var: PDM_IGNORE_SAVED_PYTHON]
  --pep582 [SHELL]      Print the command line to be eval'd by the shell

Commands:
  add                   Add package(s) to pyproject.toml and install them
  build                 Build artifacts for distribution
  cache                 Control the caches of PDM
  completion            Generate completion scripts for the given shell
  config                Display the current configuration
  export                Export the locked packages set to other formats
  fix                   Fix the project problems according to the latest version of PDM
  import                Import project metadata from other formats
  info                  Show the project information
  init                  Initialize a pyproject.toml for PDM
  install               Install dependencies from lock file
  list                  List packages installed in the current working set
  lock                  Resolve and lock dependencies
  publish               Build and publish the project to PyPI
  remove                Remove packages from pyproject.toml
  run                   Run commands or scripts with local packages loaded
  search                Search for PyPI packages
  self (plugin)         Manage the PDM program itself (previously known as plugin)
  show                  Show the package information
  sync                  Synchronize the current working set with lock file
  update                Update package(s) in pyproject.toml
  use                   Use the given python version or path as base interpreter
  venv                  Virtualenv management

````

## Related

* https://www.python.org
* [GitHub - dabeaz-course/python-mastery: Advanced Python Mastery (course by @dabeaz)](https://github.com/dabeaz-course/python-mastery)