---
title: "Reference"
layout: reference
---

## Cheat Sheet

Many Git cheat sheets exist- [here's one example](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet).

## Glossary

### Repositories
* **Repository**: A directory set up to be able to track changes to specified files within it.
* **Tracked files**: Files set up to have their changes tracked via Git.
* **Staging Area**: A temporary record of the current state of all the tracked files, that can be turned into a **commit**.

### Commits
* **Commit**: A specific version of all the tracked files within a repository, that tracks the change made to them since the last commit.
* **Commit ID**: A long string of letters that references a specific commit (e.g. `7716d1bb10d82548cf8000abde123d812494b707`). Can use the first 7 as shorthand (e.g. `7bada3c`).
* **HEAD**: The most recent commit on the current **branch**.
* **HEAD~1**: The commit 1 before the current **HEAD**. Can also be expressed as `HEAD@{1}`.

### Branches
* **Branch**: A *version* of the state of a repository. **Commits** to a repository are specific to a branch, so different branches can hold different versions of the same files. Branches start from a specific commit on an existing branch.
* **Master/main branch**: The conventional name for the 'base' branch, and one that should be used for stable, reliable versions of the code.
* **Development/dev branch**: A branch that comes off of the **master branch**, and is used for work-in-progress versions of the code. It is merged back into the master when you have a stable version.
* **Feature branch**: A branch that comes off of the **development branch**, and is used to fix a bug or add a feature before being merged back into the development branch.

### Remotes & merges
* **Remote repository**: An online copy of the repository, that you can synchronise with and share. Conventionally called **origin**.
* **Upstream**: For a **branch**, the default **remote** branch to **push** and **pull** to. Set using `git push -u remote_name branch_name_on_that_remote`.
* **Push**: To send **commits** from the current **branch** to another branch, either locally or **remote**. Normally only used to push to *the same branch on a remote repository*.
* **Pull**: To bring the **commits** from another **branch**, either local or remote, into the current branch. Can be used to synchronise your current branch with changes on a **remote repository**, or **merge** two branches together.
* **Pull request**: On GitHub, a way of requesting that one **branch** **pulls** the **commits** from another into it. A way to **merge** branches.
* **Merge**: Adding the changes from one **branches'** **commits** to another branch. Should be done using **pull** or preferably via a **pull request**.
* **Merge conflict**: When two different **commits** change the same lines of the same file. Occurs when trying to add commits from one **branch** to another branch using **pull** or **push**.
* **Conflict marker**: A sequence of `<<<<`, `====` and `>>>>` added to a file to show where the **merge conflict** occurred. The section from `<<<<` to `====` is the version of the file in the current branch, the section from `====` to `>>>>` is the version of the file in the branch you're trying to **merge** in.

{% include links.md %}
