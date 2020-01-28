---
title: "Setting Up Git"
teaching: 10
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "Identify which initialization and configuration steps are required once per machine and which are required once per repository."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---


> ## Prerequisites
>
> In this lesson we use Git from the Bash Shell.
> Some previous experience with the shell is expected,
> *but isn't mandatory*.
{: .prereq}

## Get Started - Continuing our climate data processing


**Linux and Mac** users should open a **terminal**, Windows users to should go to the Start Menu open GitBash from the Git group.

**[Post-Its Reminder]** / **[Switch out of fullscreen]**

**[Open Terminal]** / **[Use other projector]**


![Local Configuration](img/slides/version-control-with-git-slides - 09.jpg)
See [slides](../slides/index.html)

**Working individually**, we’ll start by exploring how version control can be used to keep track of what **one person** did and when.

## Setting Up ##

The first time we use Git on a new machine,
we need to configure a few things.

Make sure you're in your **home directory** (not another repository).

~~~
$ cd
~~~
{: .language-bash}

Set some global options

~~~
$ git config --global user.name "Norbert Nodinkle"
$ git config --global user.email "norbert@nodinkle.com"
~~~
{: .language-bash}

(Please use your own name and email address instead of Norbert's.)

You can set your favourite text editor, following this table:

| Editor             | Configuration command                            |
|:-------------------|:-------------------------------------------------|
| nano               | `$ git config --global core.editor "nano -w"`    |
| Notepad++ (Win)    | `$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`|

(See the Etherpad)

Git commands are written `git action`,
where `action` is what we actually want it to do.
In this case,
we're telling Git:

*   our **name** and **email address**,
*   what our favorite **text editor** is, and
*   that we want to use these settings **globally** (i.e., for every project),

The three commands above only need to be **run once**:
the flag `--global` tells Git to use the settings for every project on this machine.

You can check your settings at any time:

~~~
$ git config --list
~~~
{: .language-bash}

{% include links.md %}
