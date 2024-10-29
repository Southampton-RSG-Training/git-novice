## Version Control with Git



## 0. Introduction


### Before We Start

- Create an account at [github.com](https://www.github.com)
- Open up a terminal


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
    <th>Sourcetree</th>
    <th>Git Kraken</th>
    <th>Git Desktop</th>
  </tr>
  <tr>
    <td>![Sourcetree](./images/01-background/sourcetree.png)</td>
    <td>![Git Kraken](./images/01-background/kraken.png)</td>
    <td>![Git Desktop](./images/01-background/desktop.png)</td>
  </tr>
</table>

### GUIs

<table>
  <tr>
    <th>PyCharm</th>
    <th>RStudio</th>
    <th>VS Code</th>
  </tr>
  <tr>
    <td>![PyCharm](./images/01-background/integration-pycharm.png)</td>
    <td>![RStudio](./images/01-background/integration-rstudio.png)</td>
    <td>![VS Code](./images/01-background/integration-vscode.png)</td>
  </tr>
</table>


## 2. Setting Up Git


### Key Commands

- `git config --global user.name "Your Name"`
- `git config --global user.email "yourname@gmail.com"`
- `git config --global core.editor "nano -w"`


### Setting Up GitHub

- Sign up to GitHub: [https://github.com/signup](https://github.com/signup)
- Open a terminal
- `ssh-keygen -t ed25519`
- Yes to everything
- `cat ~/.ssh/id_ed25519.pub`
- Copy the contents to GitHub: [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new)


## 3. Creating a Repository


### GitHub Template

- Go to [https://github.com/Southampton-RSG-Training/git-novice-template](https://github.com/Southampton-RSG-Training/git-novice-template)
- "Use This Template"
- Name it `climate-analysis`


### Downloading a Repository

- `git clone git@github.com:yourname/climate-analysis`


## 4. Tracking Changes


### Key Commands

- `nano README.md`
- `git add README.md`
- `git status`
- `git commit -m "Your commit message"`


### Adding & Committing

<center>
<div style="width: 60%">
![Repository structure](./images/04-changes/add.svg)
</div>
</center>


### Key Commands

- `git status`
- `git log`
- `nano climate_analysis.py`
- `git diff`
- `git add climate_analysis.py`
- `git commit -m "Your commit message"`


### Challenge

- Use `nano` to add `# TODO: Add rainfall processing code` to the end of `climate_analysis.py`
- Commit the change to the repository.


### Solution

- `nano climate_analysis.py`
- `git diff`
- `git add climate_analysis.py`
- `git commit -m "Your commit message"`


## 5. Exploring History


### Key Commands

- `git log`
- `git diff HEAD~1 climate_analysis.py`
- `git diff HEAD~2 climate_analysis.py`


### Challenge

- Use the first 7 characters of a commit ID to get a summary of the changes to `climate_analysis.py` since the initial commit.


### Solution

- `git log`
- Take the first 7 characters of the last commit
- `git diff <COMMIT ID> climate_analysis.py`


### More Differences

![Differences of specific commits](./images/05-history/diff.svg)


### Key Commands

- `rm climate_analysis.py`
- `git status`
- `git restore climate_analysis.py`


### Advanced Use

- `git checkout <COMMIT ID> climate_analysis.py`


### Restoring Files

<center>
<div style="width: 70%">
![Restore files to specific commits](./images/05-history/restore.svg)
</div>
</center>


## 6. Remote Repositories



### Local Repo

<center>
<div style="width:50%;">![Local repository workflows](./images/06-remote/local.png)</div>
</center>


### Remote Backups

<center>

<div style="width: 65%">![Mountbatten Fire](./images/06-remote/mountbatten-fire.jpg)</div>

</center>

### Collaboration

![Collaboration via remote repository](./images/06-remote/remote.svg)


### Remote Repositories

- `git push`
- `git pull`


### Remote Commands

<center>
<div style="width: 60%">![Remote workflows](./images/06-remote/remote.png)</div>
</center>


## 7. Branches


### Feature-branch

<center>
<div style="width: 80%">
![Branching off a master branch](./images/06-remote/git-feature-branch.svg)
</div>
</center>


### Creating branches

- `git branch dev`
- `git checkout dev`


### Branch files

- Create `rainfall_conversion.py`
- `git add rainfall_conversion.py`
- `git commit -m`


### Pushing & merging

- `git push origin dev`
- `git switch main`
- `git merge dev`


## 8. Ignoring Things


### Key Files

- `.gitignore`
- `.gitkeep`
