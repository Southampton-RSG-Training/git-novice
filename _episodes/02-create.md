---
title: "Creating a Repository"
teaching: 10
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "Describe how to create a Git repository locally."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

![Creating a Repository](img/slides/version-control-with-git-slides - 10.jpg)

So, first let's **change to our code directory**.  

~~~
$ cd ~/2019-11-19-southampton-swc/novice/git/code
$ ls
~~~
{: .language-bash}

~~~
climate_analysis.py  temp_conversion.py
~~~
{: .output}

Once Git is configured,
we can start using it.

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
