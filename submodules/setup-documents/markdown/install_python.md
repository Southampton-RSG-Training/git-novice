## Python Setup ##

We recommend using the [standard Python distribution version 3.8](https://www.python.org/downloads/) using `venv` 
for virtual environments and `pip` for package management.

To download a Python distribution for your operating system,
please head to [Python.org](https://www.python.org/downloads/).
>## Recommended Python Version
> We recommend using at least Python version 3.8+ but any [supported version](https://devguide.python.org/#status-of-python-branches) should work (i.e. 3.7 onward.
> Specifically, we recommend upgrading from Python 2.7 wherever possible. Continuing to use it will likely result in difficulty finding supported dependencies or syntax errors.
{: .callout}

You can
test your Python installation from the command line with:
~~~
$ python3 --version
~~~
{: .language-bash}
If all is well with your installation, you should see something like:
~~~       
Python 3.8.2
~~~
{: .output}

To make sure you are using the standard Python distribution and not some other distribution you may have on your system,
type the following in your shell:
 ~~~
 $ python3
 ~~~
{: .language-bash}
This should enter you into a Python console and you should see something like:
 ~~~
Python 3.8.2 (default, Jun  8 2021, 11:59:35) 
[Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
 ~~~
{: .language-bash}
Press `CONTROL-D` or type `exit()` to exit the Python console.

### `venv` and `pip`
If you are using a Python 3 distribution from [Python.org](https://www.python.org/),
`venv` and `pip` will be automatically installed for you. If not, please make sure you have these
two tools (that correspond to your Python distribution) installed on your machine.