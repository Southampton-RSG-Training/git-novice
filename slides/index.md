% Software Carpentry
% Southampton RSG

## 0. Introduction


### Before We Start

- Create an account at [github.com](https://www.github.com)
- Partner up with the person next to you
- Open up a terminal
- Download the materials
- `git clone https://github.com/Southampton-RSG/swc-git-novice`


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
<div style="text-align: right; float: right; width: 45%">![Revision management](images/1_2_revisions.gif)</div>


### Why Use Version Control?

- Teamwork


### Version Control Tracks Changes

![Changes are tracked sequentially](images/1_4_track_changes.svg)


### Version Control Tracks Changes

![Different versions can be saved](images/1_5_versions.svg)


### Version Control Tracks Changes

![Multiple versions can be merged](images/1_6_merge.svg)



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
    <td>![Sourcetree](images/1_8_sourcetree.png)</td>
    <td>![Kraken](images/1_8_kraken.png)</td>
    <td>![Desktop](images/1_8_desktop.png)</td>
  </tr>
</table>

## 1. Setting Up Git


### Key Commands

- `git config`


## 2. Creating a Repository


### Key Commands

- `git init`
- `git status`



## 3. Tracking Changes


### Key Commands 

- `git add`
- `git commit`


### Adding & Committing

![Repository structure](images/3_2_add.svg)


### History

- `git log`
- `git diff`


### Differences

![Types of differencing](images/3_4_diff.svg)



## 4. Exploring History


### More Differences

![Differences of specific commits](images/4_1_diff.svg)


### Restoring Files

- `git checkout`


### Restoring Files

![Restore files to specific commits](images/4_3_restore.svg)


## 5. Collaborating



### Local Repo

<center>

<div style="width:60%;">![Local repository workflows](images/5_1_local.png)</div>

</center>


### Collaboration

![Collaboration via remote repository](images/5_2_remote.svg)


### Pair Up

- Let's collaborate via remote repo
- Working in pairs:
  - **Developer A**
  - **Developer B**


### Remote Repositories: A

- **Developer A**
  - Sign in to [github.com](https://www.github.com)
  - Create repository
  - `git remote add`
  - `git push`
  - Add **Developer B** as collaborator


### Remote Repositories: B

- **Developer B**
  - Clean up
  - `git clone`
  - `git add`
  - `git commit`
  - `git push`


### Remote Repositories: A

- **Developer A**
  - `git pull`


### Exercises

- **Developer A**
  - Add README.md containing authors & info
- **Developer B**
  - Sync up your repository



## 6. Conflicts


### Conflicts: A

![Developer A changes](images/6_1_conflict.svg)


### Conflicts: B

![Developer B creates a conflict](images/6_2_conflict.svg)


### Remote Summary

![Remote repo workflow](images/6_3_remote.png)


### Exercises

- **Developer A & B**
  - Add a line
- **Developer B**
  - Push your changes
- **Developer A**
  - Resolve the conflict
- **Developer A & B**
  - Get back in sync


## 7. Ignoring Things


### Key Files

- `.gitignore`
- `.gitkeep`