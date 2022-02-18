## Git Setup ##

### Windows
We'll be using Git Bash for both git and a shell to run it in. If you've already installed Git Bash for a previous lesson, skip ahead to the [GitHub section](github). Otherwise, go to [git for windows](https://gitforwindows.org/) and click **Download**, then install it. 
Most of the options can be left on default, but be sure you check these:

- **Choosing the default editor used by Git:** Make sure **Nano** is selected from the drop-down. If you're comfortable with other editors, feel free to change it, but we recommend Nano - we use it as it's present on Windows, Mac *and* Linux. If you change it, you might not quite match what we're doing on-screen.
- **Adjusting your PATH environment:** Make sure **Git from the command line and also from 3rd-party software** is selected.
- **Choosing HTTPS transport backend:** Make sure **Use the native Windows Secure Channel Library** is selected.
- **Configuring the terminal emulator to use with Git Bash:** Make sure **Use Windows' default console window** is selected.

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
Later on in the session, we'll be demonstrating how to share work with collaborators using [GitHub](https://github.com/). You'll need to [create an account there](https://github.com/signup). As your GitHub username will appear in the URLs of your projects there, it's best to use a short, clear version of your name if you can.

In addition, we'll need to set up SSH access to GitHub from your computer. This is how GitHub checks your identity when you try to access it - and is more secure than a password. To set up SSH access, we generate a pair of keys - one public, one private. We want to add the public key to GitHub, whilst the private one stays on our computer.

There are full guides in the GitHub documentation for how to [Make an SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and [Add an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). However today we have simplified it like so:

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

You will need to press enter a few times to select default options, and set the passphrase to empty.

Copy the last line of output that starts with `ssh-ed25519` and ends with your email (it may have gone over multiple lines if your terminal isn't wide enough).

![SSH-Output](fig/SSH-Output.png){:width="50%"}

Finally, go to [your Settings -> SSH keys page and add a new SSH key](https://github.com/settings/ssh/new) (you'll need to be logged into GitHub with the account you have created). Give the key a memorable name (e.g. the name of the computer you are working on) and paste the key from your clipboard into the box labelled key. Then, click **Add SSH key** and you're done!

![SSH-Add](fig/SSH-Add.png){:width="50%"}

Now we are ready to download the code that we need for this lesson, using Git on the command line. Open a terminal on your machine, and enter:
~~~
$ cd
$ git clone https://github.com/Southampton-RSG-Training/git-novice
~~~
{: .language-bash}

`cd` will move to your home directory, and `git clone` will download a copy of the materials.

{% include links.md %}
