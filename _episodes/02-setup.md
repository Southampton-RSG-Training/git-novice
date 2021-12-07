---
title: "Setting Up Git"
slug: git-novice-setting-up-git
teaching: 5
exercises: 0
questions:
- "How do I get set up to use Git?"
objectives:
- "Configure `git` the first time it is used on a computer"
- "Understand the meaning of the `--global` configuration flag"
keypoints:
- "Use `git config` with the `--global` option to configure a user name, email address, editor, and other preferences once per machine."
---


> ## Prerequisites
>
> In this lesson we use Git from the Bash Shell.
> Some previous experience with the shell is expected,
> *but isn't mandatory*.
{: .prereq}

## Get Started

**Linux and Mac** users should open a **terminal**, Windows users to should go to the Start Menu open GitBash from the Git group.

**[Post-Its Reminder]** / **[Switch out of fullscreen]**

**[Open Terminal]** / **[Use other projector]**



Follow along with the [slides](slides/index.html) located here.
![Introduction](fig/slides/02-setup/0_introduction.png){:width="20%"}


**Working individually**, we’ll start by exploring how version control can be used to keep track of what **one person** did and when.

## Setting Up ##

The first time we use Git on a new machine,
we need to configure a few things.

Make sure you're in your **home directory** (not another repository).

~~~
$ cd
~~~
{: .language-bash}

![Key commands](fig/slides/02-setup/1_key.png){:width="20%"}

Now we're going to set some global options, so when Git starts tracking changes to files it records who made them and how to contact them.

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

> ## Git Help and Manual
>
> If you forget a `git` command, you can access the list of commands by using `-h` and access the Git manual by using `--help` :
>
> ~~~
> $ git config -h
> $ git config --help
> ~~~
> {: .language-bash}
>
> While viewing the manual, remember the `:` is a prompt waiting for commands and you can press <kbd>Q</kbd> to exit the manual.
>
{: .callout}

{% include links.md %}
