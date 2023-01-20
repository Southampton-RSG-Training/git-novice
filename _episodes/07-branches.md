---
title: "Branching"
slug: git-novice-control-branching
teaching: 10
exercises: 0
questions:
- "What are branches?"
objectives:
- "Understand what a branch is"
- "Understand when you would use a branch"
keypoints:
- "Branches are parallel versions of a repository"
- "You can easily switch between branches, and merge their changes"
- "Branches help with code sharing and collaboration"
---

> ## Optional Episode
> 
> If you don't want to do this section, [just head straight to the survey!]({{ site.url }}{{ site.baseurl }}/lesson-survey)
{: .callout}

We've seen branches mentioned a *lot* so far - mostly `main`. So what are they?

A branch is a **parallel version of a repository**. It can **branch off** from a commit, contain its own set of extra commits and edits to files, then easily **merge back** into the branch it came off (or even another!). We can visualise this flow of splitting and merging branches like this:

![Git Feature-branch workflow]({{ site.url }}{{ site.baseurl }}/fig/07-branches/git-feature-branch.svg){:width="60%"}

## Why Use Branches?

If you're a user of a code, and don't plan to do any development, you might never have to interact with branches. You'll download the `main` branch, containing the most recent, stable version of the code, and just use that. Likewise, if you create a new repository for a small code with only a single developer that you don't expect to share, you can just do all your work on the `main` branch like we've been doing.

However, if you plan on **making changes to an existing code**, **collaborating with others**, or **sharing your code**, then you'll definitely want to use branches - as they make your life a lot easier.

### Sharing Your Code: `main` and `dev` branches

As mentioned, if you're using an existing code written by somebody else, you'll typically just download the `main` branch and use that. What if, though, the author(s) of the code want to continue working on it without the potential users downloading half-finished or untested code? They could keep all their changes local and only commit and push once a new feature has been completed and rigorously tested, but that's not particularly sustainable for large features. It could potentially take months to add a new feature (a long time to go without a backup!), and you might want to share the work-in-progress version with others to test. 

The traditional way to do this is to create a **development branch (`dev` or `develop`) coming off the main branch (`main` or `master`)**. The **main branch** contains tested, finished code that can be shared with others, whilst the **development branch** contains work-in-progress code. Typically you **merge** your development branch into your master branch when your work on it has been tested and is ready to share - for example, when you release a paper using it. Then you can continue working on your development branch and sharing your development code with other other members of your group.

### Making Changes to an Existing Code: `feature` branches

Once you have a working code, particularly one that's being shared, you'll inevitably want to add new features. You could add them directly to your development branch - however, what happens if, mid-way through, you need to pause the feature and switch to something else as you wait for simulations to finish, new data to arrive, or similar? Instead of ending up with a mess of multiple half-finished modifications, which are impossible to evaluate independently of the other, you can instead create a new **feature branch coming off of your development branch** for each new feature. You work on each new feature or bugfix in their own  **feature branch**, and merge them back into your **development branch** once they're tested and complete. Then, as before, once you're ready to publish a paper using your new functionality you merge it all back into the **main branch**.

### Collaborating With Others: `feature` branches

Feature branches also make collaborating with others far easier! Instead of stepping on each other's toes by making conflicting edits to the same files, you can simply each work on your own branch. **GitHub** offers features to help manage collaborations too, by limiting who can merge their work into a branch without approval, allowing you to set up workflows where newer team members run their changes past those with experience.

## Merging

We've mentioned **merges** repeatedly; as Git tracks the *changes* made to each file in each commit, it can easily determine whether or not the changes made in two branches **conflict** with each other. It can intelligently merge together two modified versions of a file where their changes don't overlap, and highlight sections where they do for you to resolve, showing both versions of the code.

These use the same conflict resolution we saw earlier - new files are added seamlessly, whilst modified files use smart conflict resolution and might need your intervention if there's a clash!

## The Basics

You can check your current branch with: 

~~~
git branch
~~~
{: .bash}

~~~
main
~~~
{: .output}


then create a new branch with:

~~~
git branch dev
~~~
{: .bash}

and switch to it with:

~~~
git checkout dev
~~~
{: .bash}

~~~
Switched to branch 'dev'
~~~
{: .output}

Any commits you make on this branch will exist *only* on this branch - when you use `git checkout main` to switch back to your **main branch**, they won't show up in your `git log` results! To merge the commits from another branch into your current one, you can use `git pull <other branch>`.


{% include links.md %}
