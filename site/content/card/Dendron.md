---
created: 2024-02-04 06:29:47-08:00
title: Dendron
updated: 2024-02-04 06:50:51-08:00
---

A [PKM](PKM.md) in [VS Code](VS%20Code.md)

Even though technically it's in maintenance mode now, it's still my favorite way to manage information from inside VS Code. Plus it's under Apache licensing if anyone wants to fork it.

## Jots

Pulled almost verbatim from my Dendron vault because it's got some thoughts that remain useful for me.

### Workflow

I don't have one. But here are some things to keep in mind until I do.

* Dendron supports the [Amoeba](https://wiki.dendron.so/notes/e780000d-c784-4945-8e42-35218a3ecf10/) pattern
  * extract note via selection
    * select text
    * click :bulb: icon
    * select *refactor text to new note*
  * hierarchy refactoring
  * schemas
  * hierarchical graphs
* Dendron [Refactoring](https://wiki.dendron.so/notes/srajljj10V2dl19nCSFiC/) commands
  * *Dendron: Rename Note*
    * moves note to new location in hierarchy
    * updates backlinks to new location
  * *Dendron: Refactor Hierarchy*
    * updates multiple hierarchy pages via regular expressions

#### How I currently use Dendron

Not a formal process — trying to identify and improve my flow. Tweaked slightly as these days I use this vault for the stuff I don't mind people seeing, and other tools for work and other such sensitive bits.

* first stop is always `C-S-i` for the daily note in *Daily Journal*
  * my journal isn't really a "5 minute" or bujo; more of a "WTF is happening"
  * borrowing taxonomy, it's where I put my fleeting notes
* when I have a concept I think should be a node, I decide where it goes and
  link + `C-<click>` to add with summary and a resource link if handy

#### How I'd like to use Dendron

* first stop remains the daily note in my journal
* the day's tasks get added as task notes
* when I have a chunk or section that makes the journal note feel cumbersome,
  extract it to a *scratch* note
* periodically refactor scratch nodes into the schema heirarchy, either as new
  chunks in existing notes or as new notes

#### Command: *Dendron: Configure (YAML)*

Use the command! Stop looking in your workspace for the YAML file!

### Synchronization

* following wiki tips for a [synchronized repo](https://wiki.dendron.so/notes/8d3c8142-7481-40da-9a5c-69a3d4bab697/#synchronizing-everything-in-one-repo)
* [*Dendron: Workspace: Sync*](https://wiki.dendron.so/notes/c4cf5519-f7c2-4a23-b93b-1c9a02880f6b/#workspace-sync) manually synchronizes with repo
  * (commit, pull, push)
* when you get tired of that, set up [VS Code GitDoc](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.gitdoc)

### Fiddly customization

#### `Ctrl+Enter` should open note under the cursor

At some point `C-ENTER` stopped opening notes in Dendron. My own fault, I'm sure. But I figured it out! Fiddled with the *where* property of the VS Code binding for *Dendron: Go to Note*: `editorFocus && resourceExtName == '.md'`

### Task notes

[Dendron Wiki: Tasks](https://wiki.dendron.so/notes/SEASewZSteDK7ry1AshNG/)

Not as polished as [Taskwarrior](Taskwarrior.md) or [Org](Org.md), but more useful than your basic checkboxes.

#### Commands

* *Dendron: Create Task Note*
* *Dendron: Set Task Status*
* *Dendron: Complete Task*

#### Config

````yml
workspace:
    task:
        name: task
        dateFormat: y.MM.dd
        addBehavior: asOwnDomain
        statusSymbols:
            later: ' '
            now: '/'
            wait: '?'
            done: x
            nah: '-'
        taskCompleteStatus:
            - done
            - x
            - nah
        prioritySymbols:
            H: high
            M: medium
            L: low
        todoIntegration: false
        createTaskSelectionType: selection2link
````

#### Todo Tree Integration

Integrates with [VS Code Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)

If you enable `workspace.task.todoIntegration`, then Dendron adds a frontmatter item `TODO: TASK TITLE` on task creation. Since it already *has* task-specific frontmatter, I opted to tweak workspace settings for Todo Tree instead.

````json
{
    "settings": {
        "todo-tree.general.tags": [
            "FIXME",
            "TODO",
            "XXX",
            "[ ]",
            "[/]",
            "[?]",
            "[x]",
            "[-]",
            "status: ''",
            "status: x",
            "status: later",
            "status: now",
            "status: wait",
            "status: done",
            "status: nah"
        ],
        "todo-tree.general.tagGroups": {
            "NOW": ["[/]", "status: now"],
            "LATER": ["[ ]", "status: ''", "TODO", "FIXME", "XXX"],
            "WAIT": ["[?]", "status: wait"],
            "DONE": ["[x]", "status: done"],
            "NAH": ["status: nah"]
        },
    }
}
````

The tree is still a little iffy about grouped views, but that's probably a config thing for me to figure out rather than a bug.

## Related

* [Dendron Home](https://www.dendron.so/)
* [Dendron Wiki](https://wiki.dendron.so/)
* [Awesome Dendron](https://github.com/dendronhq/awesome-dendron/)
* [Source](https://github.com/dendronhq/dendron) (Apache-2.0 license)