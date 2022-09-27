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
> 
> {: .prereq}

## Get Started

**Linux and Mac** users should open a **terminal**, Windows users to should go to the Start Menu open GitBash from the Git group.

Follow along with the [slides](https://southampton-rsg-training.github.io/git-novice/slides/index.html) located here.
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

## GitHub ##
Later on in the session, we'll be demonstrating how to share work with collaborators using 
[GitHub](https://github.com/). You'll need to [create an account there](https://github.com/signup). As your GitHub 
username will appear in the URLs of your projects there, it's best to use a short, clear version of your name if you can.

In addition, we'll need to set up SSH access to GitHub from your computer. This is how GitHub checks your identity when 
you try to access it - and is more secure than a password. To set up SSH access, we generate a pair of 
keys - one public, one private. We want to add the public key to GitHub, whilst the private one stays on our computer.

There are full guides in the GitHub documentation for how to 
[Make an SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 
and 
[Add an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). 
However today we have simplified it like so:

If you already have an ssh key you can use it for Github by coping the public key into the clipboard and pasting it into
the GitHub settings page.

First we need to create a variable to store your GitHub email. Copy this command, substituting the email you signed up 
to GitHub with for `your_github_email@example.com`:
~~~
$ my_gh_email=your_github_email@example.com
~~~
{: .language-bash}

Then we can run the following command to generate a key-pair and display the public half:
~~~
$ ssh-keygen -t ed25519 -C $my_gh_email; eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_ed25519; cat ~/.ssh/id_ed25519.pub
~~~
{: .language-bash}

You will need to press enter a few times to select default options, and set the passphrase to empty.

Copy the last line of output that starts with `ssh-ed25519` and ends with your email (it may have gone over multiple 
lines if your terminal isn't wide enough).

![SSH-Output](fig/setup-SSH-Output.png){:width="50%"}

Finally, go to [your Settings -> SSH keys page and add a new SSH key](https://github.com/settings/ssh/new) 
(you'll need to be logged into GitHub with the account you have created). Give the key a memorable name (e.g. the name 
of the computer you are working on) and paste the key from your clipboard into the box labelled key. Then, 
click **Add SSH key** and you're done!

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
> {: .callout}

{% include links.md %}
