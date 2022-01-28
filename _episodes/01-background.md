---
title: "What is Version Control"
slug: git-novice-what-is-version-control
teaching: 5
exercises: 0
questions:
- "What is version control and why should I use it?"
objectives:
- "Understand the benefits of an automated version control system."
- "Understand the basics of how automated version control systems work."
keypoints:
- "Version control is like an unlimited ‘undo’."
- "Version control also allows many people to work in parallel."
---

## What is Version Control? ##

![Introduction](fig/slides/01-background/0_introduction.png){:width="20%"}
![What is Version Control?](fig/slides/01-background/1_what_does_it_do.png){:width="20%"}

Also called **revision control** or **source control**.  At their simplest these are tools which track **changes** to files.
## Why should I use it? - Three reasons ##

### 1. A More Efficient Backup ###

![Why Use Version Control? #1](fig/slides/01-background/2_why_use.png){:width="20%"}

We've **all** been in this situation before -  **multiple nearly-identical** versions of the same file with no meaningful **explanation** of what the differences are.

If we're just dealing with Docs, some word processors let us deal with this a little better, like Microsoft Word ("Track Changes") or Google Docs version history. BUT **research isn't just Words docs**, it's code and data and diagrams too.

Using **version control** means **we don't keep dozens of different versions** of our files hanging about taking up **space**, and when we store a **revision**, we store an **explanation** of what changed.

### 2. Reproducibility ###

When you use  **version control**, at any point in the future, you can retrieve the **correct versions** of your documents, scripts or code.  So, for example, a year after **publication**, you can get hold of the **precise combination** of scripts and data that you used to assemble a paper.

Version control makes **reproducibility** simpler. Without using version control it's very hard to say that your research is truly reproducible...


### 3. To Aid Collaboration ###

![Why Use Version Control? #2](fig/slides/01-background/4_why_teamwork.png){:width="20%"}

As well as maintaining a revison history, VC tools also help multiple authors **collaborate** on the **same file** or set of files.

 **Professional software developers** use VC work in large **teams** and to keep track of what they've done.  They know who has changed what and when.  And who to **blame** when things break!

**Every** large software development project relies on VC, and most programmers use it for their small jobs as well.

**VC is not just for software**: papers, small data sets -  anything that changes over time, or needs to be shared **can**, and **probably should** be stored in a version control system.

We'll look at both the backup and collaboration scenarios, but first it's useful to understand what going on **under the hood**.

## How do Version Control Tools Work? ##

![Changes are tracked sequentially](fig/slides/01-background/5_track_changes.png){:width="20%"}

**Version control systems start by storing the base version** of the file that you save and then **store just the changes** you made at each step on the way. You can think of it as a tape: if you rewind the tape and **start** at the base document, then you can **play back** each change and end up with your latest version.


![Different versions can be saved](fig/slides/01-background/6_different_versions.png){:width="20%"}

Once you think of **changes as separate from the document** itself, you can then think about "playing back" different sets of changes onto the base document and getting different versions of the document. For example, **two users can make independent sets of changes** based on the same document.

![Multiple versions can be merged](fig/slides/01-background/7_merge.png){:width="20%"}

If there aren't conflicts, you can even try to play two sets of changes onto the same base document.  A process call **merging**.


## Version Control Alternatives ##

![Version Control Alternatives](fig/slides/01-background/8_alternatives.png){:width="20%"}

**These are the most popular current Version Control systems**:

**Git** is overwhelmingly the most popular version control system in academia, and beyond.
It's a **distributed** version control system, where every developer in a team has their own **full copy** of a repository, and can synchronise between them.

It's partly become such a success thanks to sites like **GitHub** and **GitLab**, which make it easy to collaborate on a Git repository,
and provide all kinds of extra tools to manage software projects.
Plus, GitHub offers free upgraded membership to academics, students and educators-
you can apply [here](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/apply-for-an-educator-or-researcher-discount).

If you're working on old projects, or ones with very specific needs, you might use **Mercurial**, another distributed system,
or possibly **Subversion**, a **centralised** system where there's a single copy of the repository that everyone connects to.

Because Git is so popular, and making a GitHub account is so easy, we're going to teach you how to use them.

## Graphical User Interfaces ##

![Graphical User Interfaces](fig/slides/01-background/9_guis.png){:width="20%"}

We're going to teach you how to use Git on the *command line*. This isn't the only way to use it, however- there are many different graphical user interfaces for Git, like:

* [SourceTree](https://www.sourcetreeapp.com/)
* [Git Kraken](https://www.gitkraken.com/)
* [Github Desktop](https://desktop.github.com/)

Fundamentally, though, these are all just 'wrappers' around the command line version of Git.
If you understand what they're doing under the hood, you can easily switch between versions.

{% include links.md %}
