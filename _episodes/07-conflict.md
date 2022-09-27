---
title: "Conflicts"
slug: git-novice-conflicts
teaching: 20
exercises: 0
questions:
- "What do I do when my changes conflict with someone else’s?"
objectives:
- "Identify what conflicts are and when they can occur."
- "Resolve conflicts resulting from a merge."
keypoints:
- "Conflicts occur when different commits change the same lines of the same file."
- "The version control system does not allow changes to overwrite each other, but highlights conflicts so that they can be resolved."
- "`git checkout -b` creates a new branch and checks it out at the same time."
- "`git push -u` links a local branch with an 'upstream' branch on a remote repository."
- "`git pull` can pull changes from one branch into another locally."
---

![Introduction](fig/slides/07-conflict/0_introduction.png){:width="20%"}

As soon as people can work in **parallel**,
someone is going to step on someone else's toes.


This will even happen with a single person:
if we are working on a piece of software on both our laptop and a server in the lab,
we could make different changes to each copy.

![Introduction](fig/slides/07-conflict/1_conflict_a.png){:width="20%"}
![Introduction](fig/slides/07-conflict/2_conflict_b.png){:width="20%"}

These situations are called **conflicts**
Version control helps us manage these [conflicts](reference.html#conflicts)
by giving us tools to [resolve](reference.html#resolve) overlapping changes.

To see how we can resolve conflicts, we must first create one.
The file `rainfall_conversion.py` currently looks like this
on the **dev** branch of our `climate-analysis` repository:

~~~
$ cat rainfall_conversion.py
~~~
{: .language-bash}

~~~
"""A library to perform rainfall unit conversions"""

def inches_to_mm(inches):
    """Convert inches to milimetres.

    Arguments:
    inches -- the rainfall inches
    """
    mm = inches * 25.4
    return mm
~~~
{: .output}

![First branch changes](fig/slides/07-conflict/3_changes.png){:width="20%"}

We're going to create a situation just like this.

### Feature branch 1

Let's say we want to add a new function to convert from inches to centimeters. We'll create a new branch, `feature_cm`, and add a placeholder there.

First we'll make sure we're branching out from our development branch, then we can create and switch to a new branch using one command- `git checkout -b`:

~~~
$ git checkout dev
~~~
{: .language-bash}
~~~
Switched to branch 'dev'
~~~
{: .output}

~~~
$ git checkout -b feature_cm
~~~
{: .language-bash}
~~~
Switched to a new branch 'feature_cm'
~~~
{: .output}

Now, let's add a small placeholder to the end of our rainfall file:

~~~
$ nano rainfall_conversion.py
$ cat rainfall_conversion.py
~~~
{: .language-bash}

~~~
"""A library to perform rainfall unit conversions"""

def inches_to_mm(inches):
    """Convert inches to milimetres.

    Arguments:
    inches -- the rainfall inches
    """
    mm = inches * 25.4
    return mm

# TODO: Add function inches_to_cm
~~~
{: .output}

and then push the change to GitHub:

~~~
$ git add rainfall_conversion.py
$ git commit -m "Added cm placeholder"
~~~
{: .language-bash}

~~~
[feature_cm 6288bd3] Added cm placeholder
 1 file changed, 2 insertions(+)
~~~
{: .output}


Now we'll push the feature branch up to GitHub. If we add the `-u` flag, then we set a **default 'upstream' for that branch**. After this, when we want to push any changes on this branch, we can just use `git push`- we don't have to specify where we're pushing to!

~~~
$ git push -u origin feature_cm
~~~
{: .language-bash}

~~~
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 323 bytes | 323.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'feature_cm' on GitHub by visiting:
remote:      https://github.com/smangham/climate-analysis/pull/new/feature_cm
remote:
To github.com:smangham/climate-analysis.git
 * [new branch]      feature_cm -> feature_cm
Branch 'feature_cm' set up to track remote branch 'feature_cm' from 'origin'.
~~~
{: .output}


![Second branch changes](fig/slides/07-conflict/4_changes.png){:width="20%"}

### Feature branch 2

Now, we're going to introduce a **conflict**. Let's switch back to `dev`, and create another branch. We also want a function that converts inches to meters. So we go back to `dev`, and create a new branch.

~~~
$ git checkout dev
~~~
{: .language-bash}
~~~
Switched to branch 'dev'
~~~
{: .output}

~~~
$ git checkout -b feature_m
~~~
{: .language-bash}
~~~
Switched to a new branch 'feature_m'
~~~
{: .output}

We're going to add another placeholder:

~~~
$ nano rainfall_conversion.py
$ cat rainfall_conversion.py
~~~
{: .language-bash}

~~~
"""A library to perform rainfall unit conversions"""

def inches_to_mm(inches):
    """Convert inches to milimetres.

    Arguments:
    inches -- the rainfall inches
    """
    mm = inches * 25.4
    return mm

# TODO: Add function inches_to_m
~~~
{: .output}

And again we commit and push the changes:

~~~
$ git add rainfall_conversion.py
$ git commit -m "Added m placeholder"
~~~
{: .language-bash}

~~~
[feature_m 2bc1789] Added m placeholder
 1 file changed, 2 insertions(+)
~~~
{: .output}

~~~
$ git push -u origin feature_m
~~~
{: .language-bash}

~~~
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 322 bytes | 322.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'feature_m' on GitHub by visiting:
remote:      https://github.com/smangham/climate-analysis/pull/new/feature_m
remote:
To github.com:smangham/climate-analysis.git
 * [new branch]      feature_m -> feature_m
Branch 'feature_m' set up to track remote branch 'feature_m' from 'origin'.
~~~
{: .output}


![Conflicts](fig/slides/07-conflict/5_conflicts.png){:width="20%"}

### Pull requests and conflicts

We've now created both our placeholders, so let's merge them into our `dev` branch. First, we go onto GitHub and create a pull request for `feature_cm` to `dev`- this should go fine!

Secondly, we try and create one for `feature_m` to `dev`. This time, we should see something new:


![Conflicts](fig/07-conflict/conflict_github.png)

We can't automatically merge these branches! Let's create the pull request anyway. It will show us which files are conflicting:

![Conflicting files](fig/07-conflict/conflict_files.png)

If you click **Resolve conflicts**, GitHub offers a nice interface to show which files are modified, and how they clash (GitLab also offers this functionality!). In our case, you can see both branches have edited the last line of the same file.

A `=======` splits the two sets of changes, and each side lets you know which branch the changes belong to. You can resolve the conflict here, but we're going to do it on the command line. Some conflicts can be too large or complicated to resolve through a web interface, so it's important to understand how to do it locally.

![Resolving conflicts](fig/07-conflict/resolve.png)


![Resolving conflicts](fig/slides/07-conflict/6_resolving.png){:width="20%"}

### Resolving conflicts

Conflicts happen when one branch contains **commits** that another branch doesn't. So in order to merge our `feature_m` branch in, we need to get it up to date with `dev`.

We can do this by **pulling the commits from dev into our current branch (feature_m)**.

~~~
$ git pull origin dev
~~~
{: .language-bash}

~~~
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), 631 bytes | 631.00 KiB/s, done.
From github.com:smangham/climate-analysis
 * branch            dev        -> FETCH_HEAD
   311e67e..35fd1b5  dev        -> origin/dev
Auto-merging rainfall_conversion.py
CONFLICT (content): Merge conflict in rainfall_conversion.py
Automatic merge failed; fix conflicts and then commit the result.
~~~
{: .output}

As we can see, this gives us a conflict, and it's one that we can fix. If we look inside the `rainfall_conversion.py` file, we'll see the same problems we saw on GitHub, though this time the labels will be slightly different. Instead of labelling branches, they label specific commits, where `HEAD` means the **latest commit on this branch** and the other one will be the ID of the latest commit on the `dev` branch:

~~~
$ cat rainfall_conversion.py
~~~
{: .language-bash}

~~~
"""A library to perform rainfall unit conversions"""

def inches_to_mm(inches):
    """Convert inches to milimetres.

    Arguments:
    inches -- the rainfall inches
    """
    mm = inches * 25.4
    return mm

<<<<<<< HEAD
#TODO: Add function inches_to_m
=======
# TODO: Add function inches_to_cm
>>>>>>> 35fd1b5cb0223d9e63b539854ba7317ac6ede614
~~~
{: .output}

In this case, we don't want to select only one change or the other- we want to keep both placeholders. So let's edit the file to remove the conflict markers:

~~~
$ nano rainfall_conversion.py
$ cat rainfall_conversion.py
~~~
{: .language-bash}

~~~
"""A library to perform rainfall unit conversions"""

def inches_to_mm(inches):
    """Convert inches to milimetres.

    Arguments:
    inches -- the rainfall inches
    """
    mm = inches * 25.4
    return mm

# TODO: Add function inches_to_m
# TODO: Add function inches_to_cm
~~~
{: .output}

We can add our fix, then commit and push it up to our remote repository:

~~~
$ git add rainfall_conversion.py
$ git commit -m "Fixed the conflict in rainfall module"
~~~
{: .language-bash}

~~~
[feature_m 7e1c7a6] Fixed the conflict in rainfall module
~~~
{: .output}

~~~
$ git push
~~~
{: .language-bash}

~~~
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 333 bytes | 333.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:smangham/climate-analysis.git
   2bc1789..7e1c7a6  feature_m -> feature_m
~~~
{: .output}

Remember, because we used `git push -u` earlier we didn't have to specify where we were pushing to. Now let's go back to GitHub, and look at the pull request there (you may need to refresh the page):

![Resolved the conflict](fig/07-conflict/merged.png)

We can see the new commit we added that fixes the problem, and now the commits can be merged. Our conflict is sorted.

If you want, you can always merge branches directly into `dev`, without going through a pull request, but this isn't a great habit to get into. If the conflict is large, complicated, or otherwise takes a long time to resolve, you won't be able to merge in any other branches until you've finished. This can mean essential bug fixes end up waiting for you to finish adding new bells and whistles!

![Remote Workflows](fig/slides/07-conflict/7_remote.png){:width="20%"}

Version control's ability to merge conflicting changes
is another reason users tend to divide their programs and papers into multiple files
instead of storing everything in one large file.
There's another benefit too:
whenever there are repeated conflicts in a particular file,
the version control system is essentially trying to tell its users
that they ought to clarify who's responsible for what,
or find a way to divide the work up differently.

> ## Conflicts on Non-textual files
>
> What does Git do
> when there is a conflict in an image or some other non-textual file
> that is stored in version control?
>
> {: .challenge}

{% include links.md %}
