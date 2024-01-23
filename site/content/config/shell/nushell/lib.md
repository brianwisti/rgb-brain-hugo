---
title: My Nushell custom libraries
tags:
- config
- nushell
---

## `task.nu`

The idea here is to make a pretty Nu-style table from my Taskwarrior reports.

````nushell
//- file:nushell/lib/task.nu
# Prettify taskwarrior output with nushell

# Ensure field has string value or explicit null
def upsert-string [field] {
  $in | upsert $field { |it|
    let value = ($in | get -i $field)

    if ($value | empty?) { "" } else { $value | str collect " " }
  }
}

# Ensure field has datetime value or explicit null
def upsert-date [field] {
  $in | upsert $field { |it|
    let value = ($in | get -i $field)

    if ($value | empty?) { $nothing } else { $value | into datetime }
  }
}

# Format a taskwarrior export into a table
def from-tw [] {
  (
    $in
    | from json
    | upsert-string project
    | upsert-date entry
    | upsert-date modified
    | upsert-date end
  )
}

# stock reports

# next (the default)
def tw-next [] {
  (
    task status:pending -WAITING limit:page -Work -pay -finances -personal export
    | from-tw
    | upsert-string tags
    | select id entry priority project tags description urgency
    | sort-by -r urgency
    | rename ID Age P Project Tag Description Urg
  )
}


# active
# all
# blocked
# blocking
# burndown.daily
# burndown.monthly
# burndown.weekly
# completed
# ghistory.annual
# ghistory.monthly
# history.annual
# history.monthly
# information
# list
# long
# ls
# minimal
# newest
# oldest
# overdue
# projects
# ready
# recurring
# summary
# tags
# unblocked
# waiting
````
