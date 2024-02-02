---
created: 2024-01-24 07:56:36-08:00
title: Remove a file from git history
updated: 2024-01-26 09:08:52-08:00
---

\#process

Oops I had `.envrc` in my *Git* repo.  Fixing it with `git-filter-repo`.

````shell
git clone URL ~/tmp/
cd ~/tmp/REPO
git filter-repo --invert-paths --path .envrc
echo ".envrc" >> .gitignore
git commit -m 'ignore direnv files'
git remote add origin URL
git push origin --force --all
````

It had zero eyes on it that I know of, but I better delete and refresh any associated tokens just in case. One can be pretty sure there's scrapers out there specifically looking for silly mistakes like this.

# Related

* 

[GitHub - newren/git-filter-repo: Quickly rewrite git repository history (filter-branch replacement)](https://github.com/newren/git-filter-repo)