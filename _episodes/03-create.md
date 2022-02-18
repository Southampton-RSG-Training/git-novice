---
title: "Creating a Repository"
slug: git-novice-creating-a-repository
teaching: 10
exercises: 0
questions:
- "Where does Git store information?"
objectives:
- "Create a local Git repository."
- "Describe the purpose of the `.git` directory."
keypoints:
- "`git init` initializes a repository."
- "Git stores all of its repository data in the `.git` directory."
---

![Introduction](fig/slides/03-create/0_introduction.png){:width="20%"}


![Downloading files](fig/slides/03-create/1_demo_files.png){:width="20%"}

First, if we haven't already we need to download the demonstration code to our computer. It's stored in git, so we do it as:

~~~
$ git clone http://github.com/Southampton-RSG-Training/git-novice
~~~
{: .language-bash}


This will download all our test files to our computer. Don't worry, we'll explain this bit later!


Now, let's **change to our code directory**.

~~~
$ cd ~/git-novice/code
$ ls
~~~
{: .language-bash}

~~~
climate_analysis.py  temp_conversion.py
~~~
{: .output}

These are some Python files for analysing climate data-
you'll recognise them if you've done some of our earlier lessons.
Don't worry, you don't need to know Python to follow along.

![Creating a Repository](fig/slides/03-create/2_key.png){:width="20%"}

Now, lets tell Git to create a [repository](reference.html#repository)&mdash; A storage area where git records the full history of commits of a project and information about **who** changed **what** and **when**.

~~~
$ git init
~~~
{: .language-bash}

If we use `ls` to show the directory's contents,
it appears that nothing has changed:

~~~
$ ls
~~~
{: .language-bash}



But, if we add the `-a` flag to show everything,
we can see that Git has created a hidden directory called `.git`:

~~~
$ ls -a
~~~
{: .language-bash}

~~~
.  ..  climate_analysis.py  .git  temp_conversion.py
~~~
{: .output}

Git stores information about the project in here.
If we ever delete it,
we will lose the project's history.

### Check Status

We can check that everything is set up correctly
by asking Git to tell us the status of our project with the **status** command:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	climate_analysis.py
	temp_conversion.py

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

A **branch** is an independent line of development.  We have only one, and the default name is **master**.

The **untracked files** message means that there are files in the directory
that Git isn't keeping track of.

{% include links.md %}
