---
title: "Setting Up Git"
slug: git-novice-setting-up-git
teaching: 5
exercises: 0
questions:
- "How do I get set up to use Git?"
- "How do I set up my account on GitHub?"
objectives:
- "Configure `git` the first time it is used on a computer"
- "Understand the meaning of the `--global` configuration flag"
- "Add an SSH key to a GitHub account"
keypoints:
- "Use `git config` with the `--global` option to configure a user name, email address, editor, and other preferences once per machine."
- "GitHub needs an SSH key to allow access"
---


> ## Prerequisites
>
> In this lesson we use Git from the Bash Shell.
> Some previous experience with the shell is expected,
> *but isn't mandatory*.
> 
{: .prereq}

## Get Started

The slides for this material [are located here](https://southampton-rsg-training.github.io/git-novice/slides/index.html).

**Linux and Mac** users should open a **terminal**, Windows users to should go to the Start Menu and open **Git Bash** from the Git group.

We’ll start by exploring how version control can be used to keep track of what **one person** did and when.

## Setting Up Git

The first time we use Git on a new machine, we need to configure it. We're going to set some global options, so when Git starts tracking changes to files it records who made them and how to contact them.

~~~
$ git config --global user.name "Firstname Surname"
$ git config --global user.email "fsurname@university.ac.uk"
~~~
{: .language-bash}

(Please use your own name and the email address you used to sign up to GitHub!)

We're going to set **Nano**, a simple, minimal command-line text editor to be the default for when you need to edit messages.
~~~
$ git config --global core.editor "nano -w"`
~~~
{: .language-bash}

If you're already comfortable with another command-line editor, feel free to select that!

Git commands are written `git action`, where `action` is what we actually want it to do. In this case, we're telling Git:

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



## Setting Up GitHub

In order to make sure all our work is backed up online, as well as making it easy to share with collaborators, we're going to link our version control content to [GitHub](https://github.com/). You'll need to [create an account there](https://github.com/signup). As your GitHub 
username will appear in the URLs of your projects there, it's best to use a short, clear version of your name if you can.

{: .callout}
> ## Other Platforms
> There are other repository hosting sites like GitHub - Southampton has its own instance of [GitLab](https://git.soton.ac.uk) that's only accessible to Southampton user accounts.
> We'll use GitHub today, as it's the easiest one to use if you want to share your code with collaborators from outside the University - getting them access to the Southampton GitLab can be a pain!
> Both GitHub and GitLab have the same features, though some menu names will be different!

### Creating an SSH Key

We'll need to set up SSH access to GitHub from your computer. This is how GitHub checks your identity when you try to access it - and is more secure than a password. To set up SSH access, we generate a pair of keys - one public, one private. We want to add the public key to GitHub, whilst the private one stays on our computer.

{: .callout}
> ## More Detail
> There are full guides in the GitHub documentation for how to 
[Make an SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and 
> [Add an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). 
> We're going to simplify them for today.
>
> If you already have your own SSH key, feel free to skip to **Add an SSH Key**.

We can run a simple command to generate a new SSH key. It'll ask you for some settings, but you should just hit enter to use the defaults for everything:

~~~
$ ssh-keygen -t ed25519
~~~
{: .bash}

~~~
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/smangham/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in id_ed25519
Your public key has been saved in id_ed25519.pub
The key fingerprint is:
SHA256:tm2lRVXqWdkwiu+fvOF8WxRaf6peAqZHKSaWDO8jjjs user-name@computer-name
The key's randomart image is:
+--[ED25519 256]--+
|              +..|
|           . o +o|
|    .     . o .+o|
|     + .   + .ooo|
|      * S = +.o +|
|     o + B *   o.|
|    . o o = o + .|
|  Eo . . o   O oo|
|  oo.      .o B+.|
+----[SHA256]-----+
~~~
{: .output}

### Add an SSH Key

Now we've generated a key, we can add this to GitHub and register the key there. First, visit [GitHub](https://github.com), and make sure you've signed in to your account. Once you're signed in, go to [GitHub > Settings > SSH and GPG keys > Add new](https://github.com/settings/ssh/new), and you should see this:

![Add New SSH Key]({{ site.url }}{{ site.baseurl }}/fig/02-setup/ssh.png)

We need to fill in the details. Give the key a title like "Laptop SSH key", and then paste your **public key** into the key box - we can find it in our `~/.ssh` folder:

~~~
$ ls ~/.ssh
~~~
{: .bash}

~~~
id_ed25519  id_ed25519.pub  known_hosts
~~~
{: .output}

You want to copy the contents of the `.pub` file, which you can display with:

~~~
$ cat ~/.ssh/id_ed25519.pub
~~~
{: .language-bash}

~~~
ssh-ed25519 <SNIPPED FOR SECURITY> user-name@computer-name
~~~
{: .output}

**Make sure you copy the `.pub` file and not the private key!** Your private key lives on your machine and is never shared with anyone else. Then click **Add key**, and you're done!
