---
aliases:
- /note/2020/10/i-added-this-note-from-org-mode/
category: note
created: 2024-01-15 15:26:23-08:00
date: 2020-10-24 18:26:00-07:00
slug: i-added-this-note-from-org-mode
syndication:
  mastodon: https://hackers.town/@randomgeek/105092928276510026
  twitter: https://twitter.com/brianwisti/status/1320181752493735936
tags:
- emacs
- orgmode
title: I added this note from org mode
updated: 2024-02-01 20:18:04-08:00
---

Trying an experiment with setting up a [capture template](https://orgmode.org/manual/Capture-templates.html) so [ox-hugo](https://ox-hugo.scripter.co/) can add short notes to the site from [Org](../../../card/Org.md).

I built up the [ox-hugo capture sample](https://ox-hugo.scripter.co/doc/org-capture-setup/) to get my preferred `SECTION/YEAR/MONTH/STUB` folder layout.

````elisp
(defun org-hugo-note-capture-template ()
  "Returns `org-capture' template string for new site note."
  (let* ((title (read-from-minibuffer "Title: "))
         (fname (org-hugo-slug title))
         (year (format-time-string "%Y"))
         (month (format-time-string "%m")))
    (mapconcat #'identity
               `(
                 ,(concat "* TODO " title)
                 ":properties:"
                 ,(concat ":export_hugo_bundle: "
                          (mapconcat #'identity (list year month fname) "/"))
                 ":export_file_name: index"
                 ":end:"
                 "%?\n")
               "\n")))
````

Then the important bits of my capture template…

````elisp
(use-package org
  :custom
  (org-capture-templates
   (quote ("s" "Site")
          ("sn" "Note" entry
           (file+olp+datetree bmw/org-site "Notes")
           (function org-hugo-note-capture-template)))))
````

Eventually I got it right, and `C-c c s n` brought me to this buffer, where I'm editing a note that's already longer than I usually intend these to be.

````org
* Notes
:properties:
:export_hugo_section: note
:end:
** 2020
*** 2020-10 October
**** 2020-10-24 Saturday
***** TODO I added this note from org mode                        :emacs:
:properties:
:export_hugo_bundle: 2020/10/i-added-this-note-from-org-mode
:export_file_name: index
:end:

Trying an experiment: setting up a [[https://orgmode.org/manual/Capture-templates.html][capture template]] so [[https://ox-hugo.scripter.co/][ox-hugo]] can add short notes to the site.
````

Still loads to figure out — for example, how will I get cover images working? But at least I proved to myself that it works.

Back to fixing the broken [IndieWeb](../../../card/IndieWeb.md) mentions, which is why I opened my editor a couple of hours ago.