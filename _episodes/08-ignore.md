---
title: "Ignoring Things"
slug: git-novice-ignoring-things
teaching: 5
exercises: 0
questions:
- "How can I tell Git to ignore files I don’t want to track?"
objectives:
- "Use a `.gitignore` file to ignore specific files and explain why this is useful."
keypoints:
- "The `.gitignore` file tells Git what files to ignore."
---

> ## Optional Episode
>
> If you don't want to do this section, [just head straight to the survey!]({{ site.url }}{{ site.baseurl }}/lesson-survey)
{: .callout}

What if we have files that we **do not** want Git to track for us,
like **backup files** created by our editor
or **intermediate** files created during data analysis.
Let's switch to our dev branch, and create a few dummy files:

~~~
$ git switch dev
$ mkdir results
$ touch example.csv results/example.txt
~~~
{: .language-bash}

and see what Git says:

~~~
$ git status
~~~
{: .language-bash}

~~~
# On branch dev
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	example.csv
#	results/
nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

Putting these files under version control would be a **waste of disk space**.
What's worse,
having them all listed could **distract** us from changes that actually matter,
so let's tell Git to **ignore** them.

We do this by creating a file in the root directory of our project called `.gitignore`.

~~~
$ nano .gitignore
$ cat .gitignore
~~~
{: .language-bash}

~~~
*.csv
results/
~~~
{: .output}

These patterns tell Git to **ignore** any file whose name ends in **`.csv`**
and everything in the **`results`** directory.
(If any of these files were **already** being tracked,
Git would **continue** to track them.)

Once we have created this file,
the output of `git status` is much cleaner:

~~~
$ git status
~~~
{: .language-bash}

~~~
# On branch dev
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	.gitignore
nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

The only thing Git notices now is the newly-created `.gitignore` file.
You might think we wouldn't want to track it,
but everyone we're **sharing** our repository with will probably **want to ignore
the same** things that we're ignoring.
Let's add and commit `.gitignore`:

~~~
$ git add .gitignore
$ git commit -m "Add the ignore file"
$ git status
~~~
{: .language-bash}

~~~
# On branch dev
nothing to commit, working directory clean
~~~
{: .output}

As a bonus,
using `.gitignore` helps us **avoid accidentally adding files** to the repository that we don't want.

~~~
$ git add example.csv
~~~
{: .language-bash}

~~~
The following paths are ignored by one of your .gitignore files:
examples.csv
Use -f if you really want to add them.
fatal: no files added
~~~
{: .output}

If we really want to override our ignore settings,
we can use `git add -f` to force Git to add something.
We can also always see the status of ignored files if we want:

~~~
$ git status --ignored
~~~
{: .language-bash}

~~~
# On branch dev
# Ignored files:
#  (use "git add -f <file>..." to include in what will be committed)
#
#        example.csv
#        results/example.txt

nothing to commit, working directory clean
~~~
{: .output}

Force adding can be useful for adding a `.gitkeep` file. You can't add empty directories to a repository- they have to have some files within them. But if your code expects there to be a `results/` directory to output to, for example, this can be a problem. Users will run your code, and have it error out at a missing directory and have to create it themselves.

Instead, we can create an empty `.gitkeep` file using `touch` in the `results/` directory, and force-add it. As it starts with a `.`, it's a special file and won't appear in `ls` (only `ls -a`), but it will ensure that the directory structure is kept as part of your repository.
