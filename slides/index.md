## Version Control with Git



## 0. Introduction


### Before We Start

- Create an account at [github.com](https://www.github.com)
- Open up a terminal
- Download the materials
- `git clone https://github.com/Southampton-RSG-Training/git-novice`



## 1. What is Version Control?


### What Does It Do?

- Tracks **changes** to files
- Any file can be tracked
- Text (.txt, .csv, .py, .c, .R, etc.) works best
  - These allow smart *diff* / *merge* etc.


### Why Use Version Control?

<div style="text-align: left; float: left; width: 45%;">
- A more <ins>efficient</ins> backup
- Reproducibility
</div>
<div style="text-align: right; float: right; width: 45%">![Revision management](./images/01-background/revisions.gif)</div>


### Why Use Version Control?

- Teamwork


### Version Control Tracks Changes

![Changes are tracked sequentially](./images/01-background/track_changes.svg)


### Version Control Tracks Changes

![Different versions can be saved](./images/01-background/versions.svg)


### Version Control Tracks Changes

![Multiple versions can be merged](./images/01-background/merge.svg)


### Version Control Alternatives

- Git
  - Distributed
- Subversion (svn)
  - Centralised
- Mercurial (hg)
  - Distributed

- Git most widely used in academia
  - GitHub
  - GitLab


### Graphical Version Control

<table>
  <tr>
    <th>SourceTree</th>
    <th>Git Kraken</th>
    <th>Git Desktop</th>
  </tr>
  <tr>
    <td>![Sourcetree](./images/01-background/sourcetree.png)</td>
    <td>![Kraken](./images/01-background/kraken.png)</td>
    <td>![Desktop](./images/01-background/desktop.png)</td>
  </tr>
</table>



## 2. Setting Up Git


### Getting Demo Files

- `git clone https://github.com/Southampton-RSG-Training/git-novice`


### Key Commands

- `git config`



## 3. Creating a Repository


### Key Commands

- `git init`
- `git status`



## 4. Tracking Changes


### Key Commands

- `git add`
- `git commit`


### Adding & Committing

![Repository structure](./images/04-changes/add.svg)


### History

- `git log`
- `git diff`


### Differences

![Types of differencing](./images/04-changes/diff.svg)



## 5. Exploring History


### More Differences

![Differences of specific commits](./images/05-history/diff.svg)


### Restoring Files

- `git checkout`


### Restoring Files

![Restore files to specific commits](./images/05-history/restore.svg)


## 6. Collaborating



### Local Repo

<center>

<div style="width:60%;">![Local repository workflows](./images/06-collab/local.png)</div>

</center>


### Collaboration

![Collaboration via remote repository](./images/06-collab/remote.svg)


### Remote Repositories

- Sign in to [github.com](https://www.github.com)
- Create repository
- `git remote add`
- `git push`


### Branches

![Branching off a master branch](./images/06-collab/git-feature-branch.svg)


### Creating branches

- `git branch dev`
- `git checkout dev`


### Branch files

- Create `rainfall_conversion.py`
- `git add rainfall_conversion.py`
- `git commit -m`


### Branches

![Remote workflows](./images/06-collab/remote.png)


### Branches

![Feature-branch workflow](./images/06-collab/git-feature-branch.svg)


### Exercises

- Create a new branch called `doc` coming off `dev`
- Add a `README.md` file
- Commit your change to `doc`, then push
- Create a pull request on GitHub
- Merge `doc` into `dev`, and pull `dev` back



## 7. Conflicts


### Changes

![One set of changes](./images/07-conflict/conflict_a.svg)


### Conflicting changes

![Two conflicting changes](./images/07-conflict/conflict_b.svg)


### Configure GitHub

- Go to your repository
- Settings -> Branches
- Switch default branch to 'dev'


### Branch 1

- `git checkout dev`
- `git checkout -b feature_cm`
- Add a line to the end of `rainfall_conversion.py` and commit
- `git push -u origin feature_cm`


### Branch 2

- `git checkout dev`
- `git checkout -b feature_m`
- Add a line to the end of `rainfall_conversion.py` and commit
- `git push -u origin feature_m`


### Pull requests

- Create a pull request from `feature_cm` to `dev`
- Create a pull request from `feature_m` to `dev`


### Conflict

- `git pull origin dev`
- Fix the conflict
- Commit and push
- Okay your pull request


### Remote workflows

![Two conflicting changes](./images/07-conflict/remote.png)



## 8. Ignoring Things


### Key Files

- `.gitignore`
- `.gitkeep`
