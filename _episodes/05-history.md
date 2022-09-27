---
title: "Exploring History"
slug: git-novice-exploring-history
teaching: 10
exercises: 0
questions:
- "How can I review my changes?"
- "How can I recover old versions of files?"
objectives:
- "Identify and use Git revision numbers."
- "Compare files with previous versions of themselves."
- "Restore old versions of files."
keypoints:
- "`git diff` displays differences between commits."
- "`git checkout` recovers old versions of files."
---

![Introduction](fig/slides/05-history/0_introduction.png){:width="20%"}

### Relative History

![Tracking changes to files](fig/slides/05-history/1_differences.png){:width="20%"}

Let's look a bit deeper at how we can see **what we changed when**

**HEAD** is the conventional name used to refer to the **most recent** end of the chain of revisions.

We use `git diff` again,
but refer to old versions
using the notation `HEAD~1`, `HEAD~2`, and so on.

We can refer to previous revisions using the `~` notation,
so `HEAD~1` (pronounced "head minus one")
means "the previous revision",
while `HEAD~123` goes back 123 revisions from where we are now.

~~~
$ git diff HEAD~1 climate_analysis.py
~~~
{: .language-bash}

~~~
diff --git a/climate_analysis.py b/climate_analysis.py
index d5b442d..c463f71 100644
--- a/climate_analysis.py
+++ b/climate_analysis.py
@@ -26,3 +26,5 @@ for line in climate_data:
             kelvin = temp_conversion.fahr_to_kelvin(fahr)

             print(str(celsius)+", "+str(kelvin))
+
+# TODO(me): Add call to process rainfall
~~~
{: .output}

So we see the difference between the file as it is now, and as it was **before the last commit**

~~~
$ git diff HEAD~2 climate_analysis.py
~~~
{: .language-bash}

~~~
diff --git a/climate_analysis.py b/climate_analysis.py
index 277d6c7..c463f71 100644
--- a/climate_analysis.py
+++ b/climate_analysis.py
@@ -1,3 +1,4 @@
+""" Climate Analysis Tools """
 import sys
 import temp_conversion
 import signal
@@ -25,3 +26,5 @@ for line in climate_data:
             kelvin = temp_conversion.fahr_to_kelvin(fahr)

             print(str(celsius)+", "+str(kelvin))
+
+# TODO(me): Add call to process rainfall
~~~
{: .output}

And here we see the state **before the last two commits**, HEAD minus 2.

### Absolute History

So, that's useful as far as it goes, but we can also refer to **specific revisions** using
those long strings of digits and letters
that `git log` displays.

These are unique IDs for the changes,
and "unique" really does mean unique:
every change to any set of files on any machine
has a unique 40-character identifier. (A SHA-1 hash of the new, post-commit state of the repository).

Our first commit was given the ID: **[bottom ID from git log]**

a10bd8f6192f9ab29b1821d7d7929fbf6484686a,
so let's try this:

~~~
$ git diff a10bd8f6192f9ab29b1821d7d7929fbf6484686a climate_analysis.py
~~~
{: .language-bash}

~~~
diff --git a/climate_analysis.py b/climate_analysis.py
index 277d6c7..c463f71 100644
--- a/climate_analysis.py
+++ b/climate_analysis.py
@@ -1,3 +1,4 @@
+""" Climate Analysis Tools """
 import sys
 import temp_conversion
 import signal
@@ -25,3 +26,5 @@ for line in climate_data:
             kelvin = temp_conversion.fahr_to_kelvin(fahr)

             print(str(celsius)+", "+str(kelvin))
+
+# TODO(me): Add call to process rainfall
~~~
{: .output}

So that's all the changes since our first commit.
That's the right answer,but typing random 40-character strings is annoying,
so Git lets us use just the first **seven**:

~~~
$ git diff a10bd8f climate_analysis.py
~~~
{: .language-bash}

~~~
diff --git a/climate_analysis.py b/climate_analysis.py
index 277d6c7..c463f71 100644
--- a/climate_analysis.py
+++ b/climate_analysis.py
@@ -1,3 +1,4 @@
+""" Climate Analysis Tools """
 import sys
 import temp_conversion
 import signal
@@ -25,3 +26,5 @@ for line in climate_data:
             kelvin = temp_conversion.fahr_to_kelvin(fahr)

             print(str(celsius)+", "+str(kelvin))
+
+# TODO(me): Add call to process rainfall
~~~
{: .output}


> ## Other Ways To Reference Commits
>
> Git has some more advanced ways of referencing past commits. In place of `HEAD~1` you can use `HEAD~` or `HEAD@{1}`,
> or you can even use text to ask more advanced questions, like `git diff HEAD@{"yesterday"}` or `git diff HEAD@{"3 months ago"}`!
>
{: .callout}

### Restoring Files

All right:
we can **save changes** to files and **see what we've changed** &mdash; suppose we need to **restore** older versions of things?

Let's suppose we **accidentally** overwrite or delete our file:

~~~
$ rm climate_analysis.py
$ ls
~~~
{: .language-bash}

~~~
temp_conversion.py
~~~
{: .output}

**Whoops!**

`git status` now tells us that the file has been changed,
but those changes haven't been staged:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    climate_analysis.py

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

![Restoring Files](fig/slides/05-history/2_restore.png){:width="20%"}

Following the helpful hint in that output, we can put things back the way they were
by using `git checkout`:

~~~
$ git checkout HEAD climate_analysis.py
$ cat climate_analysis.py
~~~
{: .language-bash}

~~~
[SNIPPED - but changes rolled back]
~~~
{: .output}

As you might guess from its name,
`git checkout` checks out (i.e., restores) an old version of a file.

In this case,
we're telling Git that we want to recover the version of the file recorded in `HEAD`,
which is the last saved revision.

![Restoring Files](fig/slides/05-history/3_restore_commit.png){:width="20%"}

> ## Git Restore
>
> Newer versions of `git` have added `git restore` that work the same way as `git checkout` for recovering files.
> We teach `git checkout`, as some systems (for example, high-performance computing clusters) will only have older versions of Git.
>
> {: .callout}


If we want to go back even further,
we could use a revision identifier instead:


~~~
$ git checkout <last but one rev> climate_analysis.py
~~~
{: .language-bash}

The fact that files can be reverted one by one
tends to change the way people organize their work.

If everything is in one large document,
it's hard (but not impossible) to undo changes to the introduction
without also undoing changes made later to the conclusion.

If the introduction and conclusion are stored in **separate files**,
on the other hand, moving backward and forward in time becomes much easier.

{% include links.md %}
