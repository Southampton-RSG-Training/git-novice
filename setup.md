## Git Setup ##

### Windows
To install git bash go here [https://gitforwindows.org/](https://gitforwindows.org/) click download and select 'Git-X.XX.X-64-bit.exe' from the assets list.
Before we get started, we'll have to do a few things.

#### Mac OS
To use Git you must install the Apple Command Line Tools.  You can obtain these [from Apple](https://developer.apple.com/download/more/?name=command%20line%20tools%20for%20xcode%2012) (requires your Apple ID)

- Select **Command Line Tools for Xcode 12** and click the link to download the dmg archive.
- If prompted, choose to allow downloads from developer.apple.com
- Open the downloaded dmg archive from the Downloads folder
- Double-click the Command Line Tools.pkg icon to install


{% if site.carpentry != "rsg" %}
{% assign slidelink = "../slides/index.html" %}
[The slides to accompany this material can be found here.]({{ slidelink }})
{% endif %}

### GitHub
Later on in the session, we'll be demonstrating how to share work with collaborators using GitHub. You'll need to create an account there: [https://github.com/](https://github.com/).

As your GitHub user name will appear in the URLs of your projects there, it's best to use a short, clear version of your name if you can.

In addition we will need to set up SSH access to GitHub from your computer. This is how GitHub checks that you are who you say you are when you try to add things from your computer.

When we do this, we generate a pair of keys - one public, one private. We want to add the public key to GitHub, whilst the private one stays on our computer.

There are full guides here [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](Make an SSH Key) and [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](Add an SSH key).

However today we have simplified it like so:

First we need to create a variable to store your GitHub email. Copy this command, substituting the email you signed up to GitHub with for `your_github_email@example.com`:
~~~
$ my_gh_email=your_github_email@example.com
~~~
{: .language-bash}

Then we can run the following command to generate a key-pair and display the public half:
~~~
$ ssh-keygen -t ed25519 -C $my_gh_email; eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_ed25519; cat ~/.ssh/id_ed25519.pub
~~~
{: .language-bash}

You will need to press enter a few times to select default options and set the passphrase to empty.

Copy the last output line that starts with `ssh-ed25519` and ends with your email (it may have gone over multiple lines if your terminal isn't wide enough).

![SSH-Output](fig/SSH-Output.png){:width="50%"}

Finally, go to [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new) (you will need to be logged into GitHub with the account you have created). Give the key a memorable name (the name of the computer you are working on is often a good choice) and paste the key from your clipboard into the box labelled key. Then, click add SSH key and you are done!

![SSH-Add](fig/SSH-Add.png){:width="50%"}

Now we are ready to download the code that we need for this lesson, using Git on the command line. Open a terminal on your machine, and enter:
~~~
$ cd
$ git clone https://github.com/Southampton-RSG/swc-git-novice
~~~
{: .language-bash}

`cd` will move to your home directory, and `git clone` will download a copy of the materials.

{% include links.md %}
